"""
Readability Score Calculator for BBC News Classification Project
------------------------------------------------------------
Bu betik, veriniz için Dale-Chall ve Flesch Reading Ease skorlarını hesaplar
ve bu skorları içeren bir CSV dosyası oluşturur.
"""

import pandas as pd
import textstat
import os
from tqdm import tqdm

# Veri setini yükle
print("Veri seti yükleniyor...")
input_file = os.path.join('inputs', 'news_category_dataset.csv')
output_file = os.path.join('inputs', 'news_category_dataset_with_scores.csv')

try:
    data = pd.read_csv(input_file)
    print(f"Toplam {len(data)} satır içeren veri seti başarıyla yüklendi.")
except FileNotFoundError:
    print(f"Hata: {input_file} dosyası bulunamadı.")
    print("Lütfen veri setinizin 'inputs' klasöründe olduğundan emin olun.")
    exit(1)

# Okunabilirlik skorlarını hesaplama
print("\nOkunabilirlik skorları hesaplanıyor (bu işlem birkaç dakika sürebilir)...")

# İlerleme çubuğu için tqdm kullan
tqdm.pandas(desc="Hesaplanıyor")

# Okunabilirlik skorlarını hesapla
data['Flesch Reading Ease Score'] = data['text'].progress_apply(textstat.flesch_reading_ease)
data['Dale-Chall Readability Score'] = data['text'].progress_apply(textstat.dale_chall_readability_score)

# Sonuçları kaydet
print(f"\nSonuçlar {output_file} dosyasına kaydediliyor...")
data.to_csv(output_file, index=False)

# Özet istatistikleri göster
print("\nKategorilere göre ortalama okunabilirlik skorları:")
avg_scores = data.groupby('labels')[['Flesch Reading Ease Score', 'Dale-Chall Readability Score']].mean()
print(avg_scores)

print("\nKategorilere göre okunabilirlik skor istatistikleri:")
score_stats = data.groupby('labels')[['Flesch Reading Ease Score', 'Dale-Chall Readability Score']].describe()
print(score_stats)

print("\nİşlem tamamlandı!")
print(f"Okunabilirlik skorları eklenen yeni veri seti: {output_file}")
print("Şimdi bu dosyayı Jupyter Notebook'unuzda kullanabilirsiniz.") 