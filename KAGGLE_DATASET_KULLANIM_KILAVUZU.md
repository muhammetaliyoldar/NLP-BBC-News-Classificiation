# Kaggle News Category Dataset Kullanım Kılavuzu

Bu belge, BBC News sınıflandırma projenizde Kaggle News Category Dataset'ini nasıl kullanacağınızı açıklamaktadır.

## Veri Seti Hazırlık Süreci

`prepare_kaggle_dataset.py` betiği ile otomatik olarak Kaggle veri setini projenize uygun bir formata dönüştürdük. Bu işlem:

1. Kaggle'dan indirdiğiniz `News_Category_Dataset_v3.json` dosyasını okudu
2. Veri setini Python DataFrame'e dönüştürdü
3. BBC veri setiyle aynı kategorilere sahip olması için eşleştirmeler yaptık:
   - business: BUSINESS, MONEY, FINANCE, ECONOMIC
   - entertainment: ENTERTAINMENT, ARTS, CULTURE, COMEDY, ARTS & CULTURE, MEDIA
   - politics: POLITICS, WORLDPOST, WORLD NEWS, WORLD
   - sport: SPORTS, SPORT
   - tech: TECH, SCIENCE & TECH, TECHNOLOGY, SCIENCE
4. Her makale için başlık ve kısa açıklama birleştirilerek "text" alanı oluşturuldu
5. Etiketler "labels" sütununda tutuldu
6. Sonuç, BBC veri seti ile aynı formatta ve aynı kategorilerde `inputs/news_category_dataset.csv` olarak kaydedildi

## Notebook'u Güncelleme Adımları

Jupyter notebook'unuzu elle aşağıdaki adımları izleyerek güncelleyin:

### 1. Veri Yükleme Hücresini Değiştirme

Notebook'ta şu satırları içeren kod hücresini bulun:
```python
# Original BBC Articles dataset
original_data = pd.read_csv(r'C:\Users\muham\PycharmProjects\NLP-BBC-News-Classificiation\News_Category_Dataset_v3.json')

original_data.head()
```

Bunu şu kodla değiştirin:
```python
# Hazırlanmış Kaggle News Category veri setini yükle
original_data = pd.read_csv('inputs/news_category_dataset.csv')

# İlk birkaç satırı görüntüle
original_data.head()
```

### 2. Bölüm Başlığını Güncelleme

"1.1 Original Dataset" başlığını içeren markdown hücresini bulun ve bunu:
```
## **1.1 Kaggle News Category Dataset**
```
olarak değiştirin.

### 3. Veri Seti Açıklaması Ekleme

Başlık hücresinin hemen altına yeni bir markdown hücresi ekleyin ve içeriğini şu şekilde doldurun:
```
Bu projede, Kaggle'dan alınan News Category Dataset'i kullanıyorum (https://www.kaggle.com/datasets/rmisra/news-category-dataset). Bu veri seti, 2012'den 2018'e kadar HuffPost'tan elde edilen yaklaşık 200.000 haber başlığını içermektedir.

Veri seti başlıklar, kısa açıklamalar, kategori etiketleri ve diğer meta verileri içerir. Bu sınıflandırma görevi için, original BBC veri setiyle aynı kategorilere (business, entertainment, politics, sport, tech) sahip olacak şekilde verileri eşleştirip dönüştürdüm ve sınıflandırma için kullanılacak metni oluşturmak üzere başlık ve kısa açıklamayı birleştirdim.
```

## Önemli Notlar

1. **Kategori Aynılığı**: Yeniden düzenlenen veri seti, BBC veri setindeki kategorilere göre eşleştirilmiştir:
   - business
   - entertainment
   - politics
   - sport
   - tech

2. **Veri Boyutu**: Kaggle veri seti, BBC veri setinden daha büyüktür. Bu, modelin eğitimi için daha fazla zaman gerektirebilir ama daha iyi sonuçlar verebilir.

3. **Veri Yapısı**: Her iki veri seti de aynı yapıya sahiptir (labels ve text sütunları) ve aynı kategorilere sahiptir, bu nedenle kodunuzda hiçbir değişiklik yapmanız gerekmez.

## Sorun Giderme

Eğer notebook'u çalıştırırken sorunlarla karşılaşırsanız:

1. Veri setinin doğru konumda olup olmadığını kontrol edin: `inputs/news_category_dataset.csv`
2. Veri setinin doğru formatta olup olmadığını kontrol edin (iki sütun: 'labels' ve 'text')
3. Gerekirse, `prepare_kaggle_dataset.py` betiğini tekrar çalıştırın

## Kaynak Kodu Açıklaması

`prepare_kaggle_dataset.py` betiği şu işlemleri gerçekleştirir:

1. JSON dosyasını okur ve bir pandas DataFrame'e dönüştürür
2. Kategori dağılımını analiz eder
3. BBC veri setindeki kategorilere benzer Kaggle kategorilerini seçer ve eşleştirir
4. Başlık ve kısa açıklamayı birleştirerek 'text' alanını oluşturur
5. BBC veri seti formatıyla uyumlu bir CSV dosyası oluşturur

Bu şekilde, orijinal notebook kodunuzun geri kalanında hiçbir değişiklik yapmadan Kaggle veri setini kullanabilirsiniz. 