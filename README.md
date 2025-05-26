![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Status](https://img.shields.io/badge/Project%20Status-Completed-brightgreen)

# 📰 BBC News Classification and Analysis

This project implements an NLP-based system that categorizes news articles into predefined topics using advanced text processing techniques. Developed as part of my coursework in Natural Language Processing at Turkish Aeronautical Association University.

## 👨‍🎓 Student Information
- **Name**: Muhammet Ali Yoldar
- **Student ID**: 200444035
- **Program**: Computer Engineering, 4th Year
- **University**: Turkish Aeronautical Association University

---

## 📋 Project Overview

This project demonstrates a complete text classification pipeline that satisfies the following requirements:

1. **Data Collection and Preprocessing**
   - Implemented Regular Expressions for text cleaning
   - Applied Text Normalization (lowercasing, stemming, and lemmatization)
   - Used Edit Distance for handling text variations and typo correction

2. **Feature Engineering**
   - Implemented N-gram models to analyze word sequences
   - Used Word2Vec to create vector representations of words

3. **Text Classification**
   - Implemented and evaluated multiple classifiers, with Random Forest providing the best results
   - Trained using the BBC News dataset
   - Evaluated performance using Accuracy, Precision, Recall, and F1-score

---

## 📁 Dataset

- **Source**: BBC News dataset
- Each record contains:
  - The full text of a news article
  - The corresponding category label (business, entertainment, politics, sport, tech)

---

## 🛠️ Methodology

1. **Text Preprocessing Pipeline**
   - Cleaned text by removing special characters and normalizing
   - Applied tokenization, stopword removal, and stemming using NLTK
   - Implemented typo correction mechanisms

2. **Feature Extraction**
   - Created a custom Word2Vec model trained on the preprocessed corpus
   - Generated document embeddings by averaging word vectors
   - Experimented with TF-IDF vectorization for comparison

3. **Model Training and Evaluation**
   - Trained a Random Forest classifier with optimized hyperparameters
   - Implemented cross-validation to ensure model robustness
   - Generated detailed evaluation metrics and visualizations

---

## 📊 Results

- **Train Accuracy**: ~93%  
- **Test Accuracy**: ~94%
- **Detailed Performance by Category**:
  - Business: 95% F1-score
  - Entertainment: 92% F1-score
  - Politics: 91% F1-score
  - Sport: 97% F1-score
  - Tech: 93% F1-score

---

## 🚀 Interactive Demo

A Streamlit web application is included that allows for real-time classification of news articles:

```
streamlit run app.py
```

---

## 📦 Installation

```bash
# Clone the repository
git clone https://github.com/muhammetaliyoldar/NLP-BBC-News-Classification.git

# Install dependencies
pip install -r requirements.txt

# Run the demo application
streamlit run app.py
```

---

## 🔍 Future Improvements

- Implement more advanced deep learning models (LSTM, Transformers)
- Expand the dataset to include more recent articles
- Add multilingual support for classification

---

*This project was completed as part of the Natural Language Processing course requirements at Turkish Aeronautical Association University, Fall 2023.*
