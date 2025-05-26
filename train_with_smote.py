"""
SMOTE ve Sınıflandırma Modelleri Eğitimi
----------------------------------------
Bu script, Word2Vec kullanarak işlenmiş metin verilerini dengeli hale getirmek için SMOTE uygular 
ve Lojistik Regresyon ile Random Forest sınıflandırıcılarını eğitir.
"""

import os
import numpy as np
import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score, confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns
from imblearn.over_sampling import SMOTE

def load_features(file_path):
    """Word2Vec özelliklerini yükler"""
    try:
        features = np.load(file_path)
        print(f"Özellikler başarıyla yüklendi. Şekil: {features.shape}")
        return features
    except FileNotFoundError:
        print(f"Hata: {file_path} dosyası bulunamadı.")
        print("Lütfen önce Word2Vec modelini eğitip özellikleri kaydettiğinizden emin olun.")
        return None
    except Exception as e:
        print(f"Özellikleri yüklerken beklenmeyen hata: {e}")
        return None

def load_labels(file_path):
    """Etiketleri yükler"""
    try:
        df = pd.read_csv(file_path)
        labels = df['labels'].values
        print(f"Etiketler başarıyla yüklendi. Toplam etiket sayısı: {len(labels)}")
        return labels
    except FileNotFoundError:
        print(f"Hata: {file_path} dosyası bulunamadı.")
        return None
    except Exception as e:
        print(f"Etiketleri yüklerken beklenmeyen hata: {e}")
        return None

def apply_smote_and_train():
    """SMOTE uygulayarak veri dengelemesi yapar ve modelleri eğitir"""
    
    # Özellik ve etiketleri yükle
    print("Veri yükleniyor...")
    features = load_features(os.path.join('inputs', 'word2vec_features.npy'))
    labels = load_labels(os.path.join('inputs', 'news_category_dataset.csv'))
    
    if features is None or labels is None:
        print("Veri yüklenirken hata oluştu. İşlem durduruluyor.")
        return
    
    # Veri setini eğitim ve test olarak böl
    print("Veri seti eğitim/test olarak bölünüyor...")
    X_train, X_test, y_train, y_test = train_test_split(
        features, labels, test_size=0.2, random_state=42, stratify=labels
    )
    
    print(f"Eğitim seti boyutu: {X_train.shape}")
    print(f"Test seti boyutu: {X_test.shape}")
    
    # Sınıf dağılımını kontrol et ve göster
    train_class_dist = pd.Series(y_train).value_counts()
    print("\nSMOTE öncesi eğitim seti sınıf dağılımı:")
    print(train_class_dist)
    
    # SMOTE uygula
    print("\nSMOTE uygulanıyor...")
    try:
        smote = SMOTE(random_state=42)
        X_resampled, y_resampled = smote.fit_resample(X_train, y_train)
        
        # SMOTE sonrası sınıf dağılımını göster
        resampled_class_dist = pd.Series(y_resampled).value_counts()
        print("\nSMOTE sonrası eğitim seti sınıf dağılımı:")
        print(resampled_class_dist)
        
        # Görselleştir
        plt.figure(figsize=(12, 6))
        
        plt.subplot(1, 2, 1)
        sns.barplot(x=train_class_dist.index, y=train_class_dist.values)
        plt.title('SMOTE Öncesi Sınıf Dağılımı')
        plt.xticks(rotation=45)
        plt.ylabel('Örnek Sayısı')
        
        plt.subplot(1, 2, 2)
        sns.barplot(x=resampled_class_dist.index, y=resampled_class_dist.values)
        plt.title('SMOTE Sonrası Sınıf Dağılımı')
        plt.xticks(rotation=45)
        plt.ylabel('Örnek Sayısı')
        
        plt.tight_layout()
        os.makedirs('outputs', exist_ok=True)
        plt.savefig(os.path.join('outputs', 'smote_class_distribution.png'))
        plt.close()
        
        # Modelleri eğit
        print("\nLojistik Regresyon modeli eğitiliyor...")
        lr_model = LogisticRegression(random_state=42, max_iter=1000, n_jobs=-1)
        lr_model.fit(X_resampled, y_resampled)
        
        print("\nRandom Forest modeli eğitiliyor...")
        rf_model = RandomForestClassifier(random_state=42, n_jobs=-1)
        rf_model.fit(X_resampled, y_resampled)
        
        # Test seti üzerinde değerlendirme
        print("\nModeller test seti üzerinde değerlendiriliyor...")
        
        # Lojistik Regresyon
        lr_preds = lr_model.predict(X_test)
        lr_accuracy = accuracy_score(y_test, lr_preds)
        print(f"\nLojistik Regresyon Doğruluk: {lr_accuracy:.4f}")
        print("\nLojistik Regresyon Sınıflandırma Raporu:")
        print(classification_report(y_test, lr_preds))
        
        # Random Forest
        rf_preds = rf_model.predict(X_test)
        rf_accuracy = accuracy_score(y_test, rf_preds)
        print(f"\nRandom Forest Doğruluk: {rf_accuracy:.4f}")
        print("\nRandom Forest Sınıflandırma Raporu:")
        print(classification_report(y_test, rf_preds))
        
        # Confusion Matrix Görselleştirmesi
        plt.figure(figsize=(18, 8))
        
        plt.subplot(1, 2, 1)
        cm_lr = confusion_matrix(y_test, lr_preds)
        sns.heatmap(cm_lr, annot=True, fmt='d', cmap='Blues', 
                    xticklabels=np.unique(labels), yticklabels=np.unique(labels))
        plt.title(f'Lojistik Regresyon Confusion Matrix\nAccuracy: {lr_accuracy:.4f}')
        plt.xlabel('Tahmin Edilen Etiket')
        plt.ylabel('Gerçek Etiket')
        
        plt.subplot(1, 2, 2)
        cm_rf = confusion_matrix(y_test, rf_preds)
        sns.heatmap(cm_rf, annot=True, fmt='d', cmap='Blues', 
                    xticklabels=np.unique(labels), yticklabels=np.unique(labels))
        plt.title(f'Random Forest Confusion Matrix\nAccuracy: {rf_accuracy:.4f}')
        plt.xlabel('Tahmin Edilen Etiket')
        plt.ylabel('Gerçek Etiket')
        
        plt.tight_layout()
        plt.savefig(os.path.join('outputs', 'model_confusion_matrices.png'))
        plt.close()
        
        # Modelleri kaydet
        print("\nModeller kaydediliyor...")
        os.makedirs('models', exist_ok=True)
        joblib.dump(lr_model, os.path.join('models', 'logistic_regression_model.pkl'))
        joblib.dump(rf_model, os.path.join('models', 'random_forest_model.pkl'))
        
        print("\nEğitim tamamlandı! Modeller 'models' klasörüne kaydedildi.")
        print("Görselleştirmeler 'outputs' klasörüne kaydedildi.")
        
    except Exception as e:
        print(f"\nHata: {e}")
        print("SMOTE veya model eğitimi sırasında bir hata oluştu.")

if __name__ == "__main__":
    apply_smote_and_train() 