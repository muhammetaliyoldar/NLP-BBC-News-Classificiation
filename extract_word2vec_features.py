"""
Word2Vec Feature Extractor for BBC News Classification
-----------------------------------------------------
Bu betik, metin verilerini işler, Word2Vec modelini eğitir ve 
özellik vektörlerini SMOTE ve sınıflandırma modelleri için kaydeder.
"""

import os
import numpy as np
import pandas as pd
import nltk
import re
from nltk.corpus import stopwords
from nltk.stem import SnowballStemmer
from gensim.models import Word2Vec
import warnings
warnings.filterwarnings("ignore")

# NLTK kaynaklarını indir
try:
    nltk.data.find('corpora/stopwords')
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('stopwords')
    nltk.download('punkt')

# Parametreler
VECTOR_SIZE = 100
WINDOW = 50
MIN_COUNT = 5
RANDOM_STATE = 42

def preprocess(text):
    """Metin önişleme fonksiyonu"""
    # Stopwords ve stemmer hazırla
    stop_words = set(stopwords.words('english'))
    snowballstemmer = SnowballStemmer('english')
    
    # Alfabe dışı karakterleri temizle ve küçük harfe çevir
    text = re.sub("[^a-zA-Z]", " ", text)
    text = text.lower()
    
    # Tokenize et
    try:
        from nltk.tokenize import word_tokenize
        words = word_tokenize(text)
    except LookupError:
        words = text.split()  # Tokenizasyon başarısız olursa boşluklara göre böl
    
    # Stopwords'leri kaldır ve stemming uygula
    words = [snowballstemmer.stem(word) for word in words if word not in stop_words]
    
    # Temizlenmiş metni string olarak döndür
    return " ".join(words)

def vectorize(sentence, model):
    """Bir cümleyi Word2Vec vektörüne dönüştürür"""
    words = sentence.split()
    vec = np.zeros(VECTOR_SIZE)
    count = 0
    
    for word in words:
        try:
            if word in model.wv:
                vec += model.wv[word]
                count += 1
        except KeyError:
            continue  # Kelime modelde yoksa atla
    
    if count != 0:
        vec = vec / count
    
    return vec

def extract_features():
    """Veri setini işler, Word2Vec modelini eğitir ve özellikleri kaydeder"""
    print("Veri seti yükleniyor...")
    
    # Veri setini yükle
    input_file = os.path.join('inputs', 'news_category_dataset.csv')
    
    try:
        data = pd.read_csv(input_file)
        print(f"Veri seti yüklendi. Toplam {len(data)} satır.")
    except FileNotFoundError:
        print(f"Hata: {input_file} dosyası bulunamadı.")
        return
    
    # Metin verilerini işle
    print("Metin önişleme uygulanıyor...")
    data['processed_text'] = data['text'].apply(preprocess)
    
    print("Word2Vec modeli eğitiliyor...")
    # Word2Vec için cümleleri tokenize et
    sentences = [sentence.split() for sentence in data['processed_text']]
    
    # Word2Vec modelini eğit
    w2v_model = Word2Vec(sentences, vector_size=VECTOR_SIZE, window=WINDOW, min_count=MIN_COUNT)
    
    print("Metinler vektörlere dönüştürülüyor...")
    # Her metin için Word2Vec vektörünü hesapla
    features = np.array([vectorize(text, w2v_model) for text in data['processed_text']])
    
    # Vektörleri kaydet
    os.makedirs('inputs', exist_ok=True)
    features_file = os.path.join('inputs', 'word2vec_features.npy')
    np.save(features_file, features)
    
    # Word2Vec modelini kaydet
    os.makedirs('models', exist_ok=True)
    model_file = os.path.join('models', 'word2vec.model')
    w2v_model.save(model_file)
    
    print(f"Özellikler {features_file} dosyasına kaydedildi.")
    print(f"Word2Vec modeli {model_file} dosyasına kaydedildi.")
    print(f"Özellik vektörleri boyutu: {features.shape}")
    
    # İlk 5 vektörün şeklini göster
    print("\nİlk 5 özellik vektörü:")
    for i in range(min(5, len(features))):
        print(f"Vektör {i+1}: {features[i][:5]}... (Toplam {len(features[i])} boyutlu)")
    
    print("\nÖzellik çıkarımı tamamlandı! Şimdi train_with_smote.py betiğini çalıştırabilirsiniz.")

if __name__ == "__main__":
    extract_features() 