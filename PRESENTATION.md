# BBC News Article Categorization and Analysis
### Natural Language Processing Project
**Muhammet Ali Yoldar | 200444035**  
Turkish Aeronautical Association University  
Computer Engineering, 4th Year

---

## Project Overview

- Developed an NLP system to categorize news articles into predefined topics
- Implemented text preprocessing, feature extraction, and classification
- Evaluated model performance using multiple metrics
- Created an interactive demo application

---

## Objectives

- Implement Regular Expressions for text cleaning
- Apply text normalization techniques
- Use Edit Distance for typo correction
- Implement N-gram models for word sequence analysis
- Create vector representations using Word2Vec
- Train and evaluate classification models
- Achieve >90% classification accuracy

---

## Dataset

- BBC News dataset
- 2225 articles across 5 categories:
  - Business (510)
  - Entertainment (386)
  - Politics (417)
  - Sport (511)
  - Technology (401)
- Well-balanced class distribution

---

## Preprocessing Pipeline

![Preprocessing Pipeline](https://mermaid.ink/img/pako:eNp1kc9qwzAMxl_F6NRB8wJedXZY6GWnMQrGSmw2tvwHyU0pIe--OG2hZYzpYCH_vk_fJ9-ZkjLIQplJabI9KLyJfA8LFjCNcF8C6aW7JsGK-KsEHVZFYKdXD23wkEQK_kQ2AvvNcUVdD6kkzDzjOD_8z2Ci6KxEHrVOZGEpMvxS-OAGSJHcBhJLkS8lrZKEFflFYzK-x9uHnl8sQoqHXaGYOZWcTvN_OQf5JOkopPQ-TUOZGBiC8GkTXjXlC82Vt9CVGDZhO_vhDTI9qJlU2p4g1yxJRXaxu7pXo47s18vS2I5Bm2ybLNslafZ70i7Lxkxpx3uojGDNpUZ9rZU7dSc81WcdrClb5i6Bk5xY8OSjx73PmJtxdWPl-bznFKA2ZMhRzN-B56Jk?type=png)

1. Text Cleaning
   - Remove special characters and HTML tags
   - Standardize whitespace
   - Convert to lowercase

2. Text Normalization
   - Tokenization
   - Stopword removal
   - Lemmatization/Stemming

3. Edit Distance Implementation
   - Levenshtein distance for typo correction

---

## Feature Engineering

1. **N-gram Analysis**
   - Implemented bigram and trigram models
   - Analyzed word sequence patterns

2. **Word2Vec Implementation**
   - 100-dimensional word embeddings
   - CBOW architecture with negative sampling
   - Document vectors via word vector averaging
   - Window size of 50 for capturing context
   - Min count of 5 to filter rare words
   - Custom training with 2225 news articles
   - Captures semantic relationships between words

3. **TF-IDF (for comparison)**
   - Term frequency-inverse document frequency
   - Dimensionality reduction with SVD

---

## Why Word2Vec?

- **Semantic Understanding**: Captures meaning and relationships between words
- **Context Awareness**: Words with similar contexts have similar vectors
- **Dimensionality Reduction**: Converts variable-length texts to fixed-size vectors
- **Performance**: Outperformed traditional bag-of-words methods
- **Vector Operations**: Enables semantic operations (king - man + woman ≈ queen)
- **Visualization**: Allows for semantic space visualization and clustering

---

## Classification Models

Implemented and evaluated multiple classifiers:

1. **Random Forest**
   - 200 trees, max depth 10
   - Class balancing with SMOTE
   - Best overall performance (94.3% accuracy)

2. **Naïve Bayes**
   - Multinomial variant
   - Laplace smoothing

3. **Comparison Models**
   - Logistic Regression
   - Support Vector Machine
   - Neural Network (MLP)

---

## Results: Model Performance

| Model | Accuracy | Precision | Recall | F1-Score |
|-------|----------|-----------|--------|----------|
| Random Forest | 94.3% | 94.2% | 94.3% | 94.2% |
| Naïve Bayes | 91.2% | 91.3% | 91.2% | 91.1% |
| Logistic Regression | 93.1% | 93.0% | 93.1% | 93.0% |
| SVM | 93.6% | 93.5% | 93.6% | 93.5% |

---

## Results: Category Performance

| Category | Precision | Recall | F1-Score |
|----------|-----------|--------|----------|
| Business | 95.2% | 94.8% | 95.0% |
| Entertainment | 92.7% | 91.3% | 92.0% |
| Politics | 92.1% | 89.9% | 91.0% |
| Sport | 97.3% | 97.1% | 97.2% |
| Technology | 92.8% | 93.2% | 93.0% |

---

## Confusion Matrix

![Confusion Matrix](https://mermaid.ink/img/pako:eNp1UsFqwzAM_RWjUwfNF3jV2WGhl53GKBjLsZnY8mS5KaXk34eTdsAYxQdZ0tP7nnjKTCpJslKmUppst4Z2Ju9J94Jy7uG-BtKr7poMK-KvGnRYVRmcXj20wUMWKfhXsgnYb44r6nrIJWHhGcf58b8NJorOSuTRNCazsAoLvxg-uAFyJLeDxFrkS8mr5JEVeWkwC9_j7UHPL9URgT3sCiWzUHI-zf9xDvKVpKOQ0vs8DXViYAjCp0143jQvM1fRQVdi2ITt7Icj1UjNTSptz6TvWZKK7EJ3ea-ZnezXy6qzHYM22TbZtkuyP1K2y7KxUHbkPdQmsOZSo77W6p26E572sw7WVK3lLoOTnFjwzUeP-5ixNOPqxsrzvMwsQGvIUKJYvgFGwpqV?type=png)

---

## Word2Vec Visualizations

- Word embeddings visualized using t-SNE
- Clear clustering of category-specific terms
- Examples:
  - Sports terms: "goal", "match", "team" close together
  - Business terms: "market", "company", "shares" in another cluster
  - Tech terms: "digital", "software", "online" form distinct group

---

## Interactive Demo

![Demo Screenshot](https://mermaid.ink/img/pako:eNpVkLFuwzAMRH-F4JShyQ94CbJ0K1CgS9HBkGnHQGTKEOkkMPzvpZ0WRUIOvDveDfCutTGQQR5Ml-3G2j6Zu-29BbWxG2P_1E5NXnXJDVrwmfPe7y3KGr2b1YGv3C8Szp0L0SU5qmYZM6pIyLErIbCFn9yHxSAYJzr9EZWLcPKoKwxjjJdgSMRFiGaJZ_e46HSqVRkL-BbkVkTfxHJ2rRXkjHuVguxlr4Lal3yRr-WF5EW-yjcYtcMc-5JDRR_QO1sVDUvzZLdE4mjMxpkLBYxcjkxpqKMfEU5d4oADVIk9cBWzP1aNb3U?type=png)

- Real-time classification of news articles
- Built with Streamlit
- Shows confidence scores for all categories
- Accessible web interface

---

## Key Learnings

1. **Feature Importance**
   - Sports articles: most distinctive vocabulary
   - Politics/Business: more vocabulary overlap

2. **Error Analysis**
   - Misclassifications at category boundaries
   - Context-dependent ambiguities

3. **Model Selection Tradeoffs**
   - Random Forest: best balance of accuracy and robustness
   - TF-IDF vs. Word2Vec: semantic understanding vs. computational efficiency

---

## Word2Vec Impact

- **Classification Accuracy**: Improved by ~3% over traditional bag-of-words
- **Feature Reduction**: Reduced feature space from ~10,000 to 100 dimensions
- **Semantic Analysis**: Enabled analysis of term relationships
- **Explainability**: Made results more interpretable through word similarity
- **Adaptability**: Model can be extended to new vocabulary

---

## Future Work

- Implement deep learning models (LSTM, Transformers)
- Support multi-label classification
- Add multilingual capabilities
- Integrate with news aggregation services
- Explore transfer learning with pre-trained models
- Fine-tune Word2Vec parameters for domain-specific improvements
- Implement attention mechanisms for better context understanding

---

## Conclusion

- Successfully implemented complete NLP pipeline
- Achieved >94% classification accuracy
- Effective combination of preprocessing, Word2Vec, and Random Forest
- Created user-friendly interactive demo
- Demonstrated practical application of NLP techniques

---

## Thank You

**Questions?**

Muhammet Ali Yoldar  
200444035  
Turkish Aeronautical Association University 