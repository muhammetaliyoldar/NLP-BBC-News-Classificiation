import streamlit as st
import numpy as np
import nltk
import re
import string
import joblib
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from gensim.models import Word2Vec
from PIL import Image
import time
import os

# --- Page Configuration ---
st.set_page_config(
    page_title="BBC News Classifier",
    page_icon="📰",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- Styling ---
st.markdown(
    """
    <style>
    .reportview-container .main .block-container{
        max-width: 80%;
        padding-top: 2rem;
        padding-bottom: 2rem;
    }
    .stTextArea textarea {
        height: 200px;
    }
    .big-font {
        font-size:1.5rem !important;
    }
    .smaller-font {
        font-size:0.8rem !important;
        color: #888;
    }
    .student-info {
        background-color: #f0f2f6;
        padding: 1rem;
        border-radius: 5px;
        margin-bottom: 1rem;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# --- Sidebar ---
with st.sidebar:
    # Student Information
    st.markdown("<div class='student-info'>", unsafe_allow_html=True)
    st.title("Student Information")
    st.markdown("**Name:** Muhammet Ali Yoldar")
    st.markdown("**ID:** 200444035")
    st.markdown("**University:** Turkish Aeronautical Association University")
    st.markdown("**Department:** Computer Engineering")
    st.markdown("</div>", unsafe_allow_html=True)
    
    # Load and display the BBC logo
    try:
        bbc_logo = Image.open(os.path.join("inputs", "BBC_World_News_2022.svg.png"))
        st.image(bbc_logo, width=200)
    except FileNotFoundError:
        st.warning("BBC News Logo not found.")

    st.title("BBC News Classifier")
    st.markdown("This app classifies news articles into the following categories:")
    st.markdown("*Business, Entertainment, Politics, Sport, Tech*")
    st.markdown("---")
    st.info("Please enter the full text of a news article in the box. The classifier will then predict its category.")

# --- NLTK Downloads ---
def download_nltk_resources():
    """Download all required NLTK resources."""
    resources = ['punkt', 'stopwords', 'wordnet']
    for resource in resources:
        try:
            nltk.data.find(f'{resource}')
            st.sidebar.success(f"NLTK resource '{resource}' is available.")
        except LookupError:
            st.sidebar.warning(f"Downloading NLTK resource '{resource}'...")
            nltk.download(resource, quiet=True)
            st.sidebar.success(f"Downloaded NLTK resource '{resource}'.")

# Download resources
download_nltk_resources()

# --- Load Models ---
@st.cache_resource
def load_models():
    model = None
    w2v_model = None
    error_messages = []
    
    # Try to load the classifier model
    try:
        model = joblib.load(os.path.join("models", "news_classifier_model.pkl"))
    except FileNotFoundError:
        try:
            # Try root directory as fallback
            model = joblib.load("news_classifier_model.pkl")
        except FileNotFoundError:
            error_messages.append("Classifier model not found. Please run the notebook first to generate the model.")
    
    # Try to load Word2Vec model from different locations
    try:
        # First try in models directory
        w2v_model = Word2Vec.load(os.path.join("models", "word2vec.model"))
    except FileNotFoundError:
        try:
            # Then try in root directory
            w2v_model = Word2Vec.load("word2vec.model")
        except FileNotFoundError:
            error_messages.append("Word2Vec model not found. Please run the notebook first to generate the model.")
    
    # Display error messages if any
    if error_messages:
        for msg in error_messages:
            st.error(msg)
    
    return model, w2v_model

model, w2v_model = load_models()

# --- Preprocessing and Vectorization ---
def safe_tokenize(text):
    """Tokenize text safely without relying on punkt_tab."""
    try:
        return nltk.word_tokenize(text)
    except LookupError:
        # Fallback tokenization if punkt_tab is missing
        return text.lower().split()

def preprocess_text(text):
    lemmatizer = WordNetLemmatizer()
    text = re.sub(r'\W', ' ', text.lower())
    tokens = safe_tokenize(text)
    tokens = [lemmatizer.lemmatize(word)
              for word in tokens
              if word not in stopwords.words('english') and word not in string.punctuation]
    return tokens


def vectorize_text(tokens):
    vec = np.zeros(100)
    count = 0
    for word in tokens:
        if word in w2v_model.wv:
            vec += w2v_model.wv[word]
            count += 1
    return vec / count if count != 0 else vec

# --- Main Section ---
st.title("News Article Classification")
st.markdown("""
This application uses Natural Language Processing techniques to classify BBC news articles into five categories:
business, entertainment, politics, sport, and tech.

The classification pipeline includes:
- Text preprocessing (cleaning, tokenization, lemmatization)
- Word2Vec embeddings for feature extraction
- Random Forest classifier for prediction
""")

user_input = st.text_area("Enter News Article Text Here:", "")

if st.button("✨ Classify"):
    if user_input.strip() == "":
        st.warning("Please enter some text.")
    elif model is None and w2v_model is None:
        st.error("Both models failed to load. Please run the notebook first to generate the models.")
    elif model is None:
        st.error("Classifier model failed to load. Please run the notebook first to generate the model.")
    elif w2v_model is None:
        st.error("Word2Vec model failed to load. Please run the notebook first to generate the model.")
    else:
        with st.spinner("Analyzing text..."):
            tokens = preprocess_text(user_input)
            vector = vectorize_text(tokens).reshape(1, -1)
            prediction = model.predict(vector)
            
            # Display prediction with custom styling
            st.success(f"Classification complete!")
            st.markdown("<p class='big-font'><b>Predicted Category:</b></p>", unsafe_allow_html=True)
            st.markdown(f"<p class='big-font'>{prediction[0].upper()}</p>", unsafe_allow_html=True)
            
            # Show confidence scores if available
            if hasattr(model, "predict_proba"):
                proba = model.predict_proba(vector)[0]
                categories = model.classes_
                
                st.markdown("### Confidence Scores")
                for i, category in enumerate(categories):
                    st.progress(proba[i])
                    st.markdown(f"{category.title()}: {proba[i]*100:.2f}%")
            
            st.balloons()  # Launch the balloons!

# --- Footer ---
st.markdown("---")
st.caption("Developed by Muhammet Ali Yoldar | Turkish Aeronautical Association University")
st.caption("Natural Language Processing Course Project | Fall 2025")
