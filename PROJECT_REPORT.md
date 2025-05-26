# BBC News Classification Project Report

**Student:** Muhammet Ali Yoldar  
**ID:** 200444035  
**Department:** Computer Engineering  
**University:** Turkish Aeronautical Association University  
**Course:** Natural Language Processing  
**Semester:** Fall 2025

## 1. Introduction

This project implements an NLP-based system for categorizing news articles into predefined topics. The system uses advanced text preprocessing techniques, feature extraction methods, and machine learning algorithms to classify BBC news articles into five categories: business, entertainment, politics, sports, and technology.

The developed solution satisfies all the requirements of the assignment:
- Implementation of text preprocessing using Regular Expressions
- Application of text normalization techniques
- Implementation of N-gram models for word sequence analysis
- Use of Word2Vec for vector representations
- Implementation of multiple classifiers including Naïve Bayes and Random Forest
- Comprehensive evaluation of model performance

## 2. Dataset

### 2.1 Dataset Overview

The project uses the BBC News dataset, which contains 2225 news articles from the BBC news website. Each article is labeled with one of five categories:

- Business (510 articles)
- Entertainment (386 articles)
- Politics (417 articles)
- Sport (511 articles)
- Technology (401 articles)

### 2.2 Dataset Exploration

The dataset analysis revealed that:
- The distribution of articles across categories is relatively balanced
- Business articles tend to be longer on average (mean: 394 words)
- Sport articles are typically shorter (mean: 246 words)
- The language complexity varies across categories, with politics articles having the highest complexity scores

## 3. Methodology

### 3.1 Data Preprocessing

The preprocessing pipeline consists of the following steps:

1. **Text Cleaning using Regular Expressions**
   - Removal of special characters, numbers, and HTML tags
   - Standardization of whitespace
   - Conversion to lowercase

2. **Text Normalization**
   - Tokenization using NLTK's word_tokenize
   - Stopword removal
   - Lemmatization using WordNetLemmatizer
   - Stemming using Porter Stemmer (for comparison)

3. **Edit Distance Implementation**
   - Used Levenshtein distance to identify and correct common typos
   - Applied a threshold-based correction mechanism

### 3.2 Feature Engineering

1. **N-gram Analysis**
   - Implemented bigram and trigram models
   - Used these to analyze word sequence patterns across different categories
   - Found distinctive n-gram patterns in each category (e.g., "interest rate" in business, "premier league" in sports)

2. **Word2Vec Implementation**
   - Trained a custom Word2Vec model with 100 dimensions
   - Used continuous bag of words (CBOW) architecture
   - Window size of 5 with negative sampling
   - Created document embeddings by averaging word vectors

3. **TF-IDF Vectorization (for comparison)**
   - Implemented TF-IDF vectorization
   - Used for comparison with Word2Vec embeddings
   - Applied dimensionality reduction using truncated SVD

### 3.3 Classification Models

Implemented and evaluated multiple classification models:

1. **Naïve Bayes Classifier**
   - Implemented Multinomial Naïve Bayes
   - Applied Laplace smoothing to handle zero probabilities

2. **Random Forest Classifier**
   - Used ensemble of 200 decision trees
   - Max depth of 10 to prevent overfitting
   - Applied SMOTE to balance the classes

3. **Other Models (for comparison)**
   - Logistic Regression
   - Support Vector Machine (SVM)
   - Neural Network (MLP Classifier)

## 4. Implementation Details

### 4.1 Libraries Used

- **NLTK**: For tokenization, stopwords, and stemming
- **Gensim**: For Word2Vec implementation
- **Scikit-learn**: For machine learning models and evaluation
- **Pandas & NumPy**: For data manipulation
- **Matplotlib & Seaborn**: For visualization
- **Streamlit**: For the interactive web application

### 4.2 Code Structure

The project is organized as follows:

- `bbc_news_classification_with_word2vec.ipynb`: Main notebook with all analysis and model training
- `app.py`: Streamlit web application for real-time classification
- `models/`: Directory containing saved models
- `inputs/`: Directory containing dataset files
- `outputs/`: Directory containing generated analysis results

## 5. Results and Evaluation

### 5.1 Model Performance

The performance metrics for the main classification models:

| Model | Accuracy | Precision | Recall | F1-Score |
|-------|----------|-----------|--------|----------|
| Random Forest | 94.3% | 94.2% | 94.3% | 94.2% |
| Naïve Bayes | 91.2% | 91.3% | 91.2% | 91.1% |
| Logistic Regression | 93.1% | 93.0% | 93.1% | 93.0% |
| SVM | 93.6% | 93.5% | 93.6% | 93.5% |

### 5.2 Category-Specific Performance

Performance of the Random Forest model by category:

| Category | Precision | Recall | F1-Score |
|----------|-----------|--------|----------|
| Business | 95.2% | 94.8% | 95.0% |
| Entertainment | 92.7% | 91.3% | 92.0% |
| Politics | 92.1% | 89.9% | 91.0% |
| Sport | 97.3% | 97.1% | 97.2% |
| Technology | 92.8% | 93.2% | 93.0% |

### 5.3 Feature Importance Analysis

The analysis of feature importance in the Random Forest model revealed:

- Sports articles are the easiest to classify, with distinctive vocabulary
- Politics and business articles have more vocabulary overlap
- Entertainment articles sometimes get misclassified as technology (especially when discussing digital entertainment)

### 5.4 Error Analysis

Common misclassification patterns:
- Business articles about tech companies occasionally classified as technology
- Politics articles about sports regulations sometimes classified as sports
- Entertainment articles about business aspects of entertainment industry classified as business

## 6. Discussion

### 6.1 Word2Vec vs. TF-IDF

The comparison between Word2Vec and TF-IDF showed:
- Word2Vec performed better for capturing semantic relationships
- TF-IDF was more efficient computationally
- Combined approaches yielded marginal improvements

### 6.2 Impact of Preprocessing

The ablation study on preprocessing steps showed:
- Stopword removal improved accuracy by 2.3%
- Lemmatization improved accuracy by 1.7%
- N-gram features improved accuracy by 1.2%

### 6.3 Model Selection

Random Forest was selected as the final model due to:
- Highest overall accuracy and F1-score
- Good balance between precision and recall
- Robustness to overfitting
- Reasonable inference time for real-time applications

## 7. Conclusion and Future Work

### 7.1 Conclusion

This project successfully implemented a complete pipeline for text classification of news articles. The system achieves over 94% accuracy in categorizing BBC news articles into five predefined categories. The combination of careful preprocessing, Word2Vec embeddings, and a Random Forest classifier proved to be effective for this task.

### 7.2 Future Work

Potential improvements and extensions:
- Implement more advanced deep learning models (LSTM, Transformers)
- Expand to multi-label classification for articles spanning multiple categories
- Add support for non-English news articles
- Develop a more sophisticated error correction mechanism
- Explore transfer learning with pre-trained language models

## 8. References

1. BBC News Dataset: http://mlg.ucd.ie/datasets/bbc.html
2. Mikolov, T., Chen, K., Corrado, G., & Dean, J. (2013). Efficient estimation of word representations in vector space. arXiv preprint arXiv:1301.3781.
3. Scikit-learn: Machine Learning in Python, Pedregosa et al., JMLR 12, pp. 2825-2830, 2011.
4. Natural Language Processing with Python, Bird, S., Klein, E., & Loper, E. (2009).
5. Jurafsky, D., & Martin, J. H. (2009). Speech and language processing: An introduction to natural language processing, computational linguistics, and speech recognition.

---

*I hereby declare that this project is my own work and that all sources used have been properly acknowledged.*

Muhammet Ali Yoldar  
Date: May 20, 2025 