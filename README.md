![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Status](https://img.shields.io/badge/Project%20Status-Completed-brightgreen)

# 📰 BBC News Classification with Word2Vec

An NLP-based system that categorizes news articles into predefined topics using advanced text processing techniques and Word2Vec embeddings. Developed as coursework for Natural Language Processing at Turkish Aeronautical Association University.

## 👨‍🎓 Student Information
- **Name**: Muhammet Ali Yoldar
- **Student ID**: 200444035
- **Program**: Computer Engineering
- **University**: Turkish Aeronautical Association University

## 📋 Project Overview

This project implements a complete text classification pipeline that:

1. **Preprocesses Text Data**
   - Uses Regular Expressions for text cleaning
   - Applies Text Normalization (lowercasing, stemming, lemmatization)
   - Handles text variations with Edit Distance

2. **Extracts Semantic Features**
   - Implements Word2Vec (100-dimensional embeddings) for word representation
   - Creates document vectors via word vector averaging
   - Analyzes N-gram patterns for context understanding

3. **Classifies News Articles**
   - Implements Random Forest, Naïve Bayes, and other classifiers
   - Achieves >94% classification accuracy
   - Evaluates with precision, recall, and F1-score metrics

## 📊 Results

| Model | Accuracy | Precision | Recall | F1-Score |
|-------|----------|-----------|--------|----------|
| Random Forest | 94.3% | 94.2% | 94.3% | 94.2% |
| Naïve Bayes | 91.2% | 91.3% | 91.2% | 91.1% |
| Logistic Regression | 93.1% | 93.0% | 93.1% | 93.0% |

## 🚀 Usage

1. **Set up environment**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Prepare dataset**:
   ```bash
   python prepare_kaggle_dataset.py
   ```

3. **Run notebook**:
   Open and run `bbc_news_classification_with_word2vec.ipynb`

4. **Launch interactive demo**:
   ```bash
   streamlit run app.py
   ```

## 📦 Repository Structure

- `app.py`: Streamlit web application for interactive classification
- `bbc_news_classification_with_word2vec.ipynb`: Main notebook with all analysis
- `extract_word2vec_features.py`: Script for Word2Vec feature extraction
- `train_with_smote.py`: Script for training with SMOTE balancing
- `models/`: Directory for saved models
- `inputs/`: Directory for dataset files
- `outputs/`: Directory for analysis outputs
- `PROJECT_REPORT.md`: Detailed methodology and results
- `PRESENTATION.md`: Presentation slides content

## 🔍 Word2Vec Implementation

This project implements Word2Vec using Gensim with the following parameters:
- 100-dimensional word embeddings
- Window size of 50 for capturing context
- Minimum count of 5 to filter rare words
- CBOW architecture with negative sampling

Word2Vec provides several advantages for this classification task:
1. Captures semantic relationships between words
2. Enables dimensionality reduction (from ~10,000 to 100 dimensions)
3. Improves classification accuracy by ~3% over traditional bag-of-words
4. Makes results more interpretable through word similarity

## 🔄 Handling Imbalanced Data

The project uses SMOTE (Synthetic Minority Over-sampling Technique) to:
- Balance the class distribution in the training set
- Create synthetic examples for minority classes
- Improve model performance across all categories

## 🛠️ Troubleshooting

If you encounter issues with models not loading:
1. Ensure you've run the notebook completely
2. Check that model files exist in either `models/` or root directory
3. For NLTK resource issues, run `python download_nltk_resources.py`

---

*This project was completed for the Natural Language Processing course at Turkish Aeronautical Association University.*
