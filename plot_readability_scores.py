"""
Readability Score Visualization for BBC News Classification Project
------------------------------------------------------------
Bu betik, hesaplanan readability skorlarının görselleştirmesini yapar.
"""

import pandas as pd
import matplotlib.pyplot as plt
import os
import numpy as np

# Veri setini yükle
print("Readability skorlarını içeren veri seti yükleniyor...")
input_file = os.path.join('inputs', 'news_category_dataset_with_scores.csv')

try:
    data = pd.read_csv(input_file)
    print(f"Toplam {len(data)} satır içeren veri seti başarıyla yüklendi.")
except FileNotFoundError:
    print(f"Hata: {input_file} dosyası bulunamadı.")
    print("Lütfen önce calculate_readability_scores.py betiğini çalıştırın.")
    exit(1)

# Dale-Chall ve Flesch skorlarını kategorilere göre hesapla
print("Kategorilere göre ortalama skorlar hesaplanıyor...")
Dale_Chall = (data.groupby('labels')['Dale-Chall Readability Score'].mean()
              .reset_index(name='mean Dale-Chall Readability Score')
              .sort_values(by='mean Dale-Chall Readability Score',ascending=False))

Flesch = (data.groupby('labels')['Flesch Reading Ease Score'].mean()
          .reset_index(name='mean Flesch Reading Ease Score')
          .sort_values(by='mean Flesch Reading Ease Score',ascending=False))

# Görselleştirme
print("Görselleştirme hazırlanıyor...")
fig,(ax1,ax2) = plt.subplots(ncols=2,figsize=(12,6))

# Flesch Reading Ease Score grafiği
ax1.bar(data=Flesch,x='labels',height='mean Flesch Reading Ease Score',
        color=['red','g','orange','y','navy'],edgecolor='black')
ax1.axhline(y=50,color='purple',linestyle='--',label='Fairly Difficult')
ax1.axhline(y=60,color='black',linestyle='--',label='Standard')
ax1.axhline(y=70,color='b',linestyle='--',label='Fairly Easy')
ax1.set_title('Mean Value of the Flesch Reading Ease Score by Article Class')
ax1.set_xlabel('article class')
ax1.set_ylabel('score')
ax1.legend(loc='lower right',title='Flesch Reading Ease Scores')

# Dale-Chall Readability Score grafiği
ax2.bar(data=Dale_Chall,x='labels',height='mean Dale-Chall Readability Score',
        color=['orange','g','navy','y','red'],edgecolor='black')
ax2.axhline(y=7,color='purple',linestyle='--',
            label="Average 9th or 10th-grade student")
ax2.axhline(y=8,color='black',linestyle='--',
            label="Average 11th or 12th-grade student")
ax2.axhline(y=9,color='b',linestyle='--',
            label="Average 13th to 15th-grade (college) student")
ax2.set_title('Mean Value of the Dale-Chall Readability Score by Article Class')
ax2.set_xlabel('article class')
ax2.set_ylabel('score')
ax2.legend(loc='lower right',title='(Upper) Dale-Chall Readability Scores')

plt.suptitle('Reading Scores of BBC Articles',size=30)
plt.tight_layout()

# Grafiği kaydet
output_path = os.path.join('outputs', 'readability_scores.png')
os.makedirs(os.path.dirname(output_path), exist_ok=True)
plt.savefig(output_path, dpi=300, bbox_inches='tight')
print(f"Grafik {output_path} dosyasına kaydedildi.")

# Kategorilere göre readability skorlarını ayrıntılı göster
print("\nKategorilere göre readability skorları:")
print("\n1. Flesch Reading Ease Score (Yüksek = Kolay okunur):")
print(Flesch)
print("\n2. Dale-Chall Readability Score (Yüksek = Zor okunur):")
print(Dale_Chall)

# Grafiği göster
plt.show()
print("\nGrafik gösteriliyor. Kapatmak için grafik penceresini kapatın.") 