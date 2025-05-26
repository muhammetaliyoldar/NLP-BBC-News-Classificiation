# Notebook Update Guide for Kaggle News Category Dataset

Bu rehber, BBC News Classification notebookunu Kaggle News Category veri setini kullanacak şekilde güncellemenize yardımcı olacaktır.

## Ön Hazırlık

1. Önce, veriyi hazırlama scriptini çalıştırın:
```bash
pip install matplotlib seaborn
python prepare_kaggle_dataset.py
```

## Notebook Güncelleme Adımları

### Adım 1: Veri Seti Yükleme Bölümünü Değiştirme

1. `bbc_news_classification_with_word2vec.ipynb` notebookunu açın
2. "1.1 Original Dataset" bölümü altındaki BBC veri setini yükleyen hücreyi bulun
3. O hücredeki kodu şununla değiştirin:

```python
# Hazırlanmış Kaggle News Category veri setini yükle
original_data = pd.read_csv('inputs/news_category_dataset.csv')

# İlk birkaç satırı görüntüle
original_data.head()
```

### Adım 2: Bölüm Başlığını Güncelleme

1. Bölüm başlığını "1.1 Original Dataset" yerine "1.1 Kaggle News Category Dataset" olarak değiştirin

### Adım 3: Veri Seti Açıklaması Ekleme

Bölüm başlığının altına bu içerikle yeni bir markdown hücresi ekleyin:

```markdown
Bu projede, Kaggle'dan alınan News Category Dataset'i kullanıyorum (https://www.kaggle.com/datasets/rmisra/news-category-dataset). Bu veri seti, 2012'den 2018'e kadar HuffPost'tan elde edilen yaklaşık 200.000 haber başlığını içermektedir.

Veri seti başlıklar, kısa açıklamalar, kategori etiketleri ve diğer meta verileri içerir. Bu sınıflandırma görevi için, en popüler 5 kategoriye odaklandım ve sınıflandırma için kullanılacak metni oluşturmak üzere başlık ve kısa açıklamayı birleştirdim.
```

### Adım 4: Notebook'u Çalıştırma

Veri setini orijinal BBC veri setinin formatına uyacak şekilde hazırladığımız için notebookun geri kalanı yeni veri setiyle beklendiği gibi çalışmalıdır.

## Veri Seti Farklılıkları Hakkında Not

Kaggle News Category veri seti, BBC veri setinden farklı kategorilere sahiptir:
- Orijinal BBC veri seti şu kategorilere sahiptir: tech, business, sport, entertainment, politics
- Kaggle veri setinin en popüler kategorileri farklı olabilir (POLITICS, WELLNESS, ENTERTAINMENT, vb. gibi)

Bu, orijinal notebooka kıyasla sınıflandırma performansını ve sonuçları etkileyebilir, ancak metodoloji geçerli kalır.

## Ek Görselleştirmeler

Hazırlama scripti ayrıca `outputs` klasöründe kategori dağılımının bir görselleştirmesini oluşturur, bunu analizinize dahil edebilirsiniz. 