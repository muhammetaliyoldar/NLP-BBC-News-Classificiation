# Proje Kurulum, Çalıştırma ve Test Rehberi

## Giriş

Bu rehber, "Haber Makalesi Sınıflandırma ve Analiz" projesini baştan sona nasıl kuracağınızı, çalıştıracağınızı ve test edeceğinizi adım adım açıklamaktadır. Projenin amacı, verilen haber metinlerini NLP teknikleri kullanarak business, entertainment, politics, sport, ve tech gibi önceden tanımlanmış kategorilere ayırmaktır.

## Bölüm 1: Proje Dosyalarının Hazırlanması

1.  **Proje Klasörünü Oluşturma:**
    *   Bilgisayarınızda proje için bir ana klasör oluşturun (örneğin, `NLP_Odevim`).

2.  **Gerekli Dosyaları Kopyalama:**
    *   Aşağıdaki tüm dosyaları ve `images` klasörünü bu ana klasöre (`NLP_Odevim`) kopyalayın:
        *   `News_Category_Dataset_v3.json` (Bu dosyayı Kaggle'dan indirip ana klasöre kendiniz kopyalamalısınız.)
        *   `app.py` (Streamlit Uygulaması)
        *   `bbc_news_classification_with_word2vec.ipynb` (Jupyter Notebook)
        *   `prepare_kaggle_dataset.py` (Veri Hazırlama Betiği)
        *   `requirements.txt` (Gerekli Kütüphaneler)
        *   `README.md`
        *   `PROJECT_REPORT.md`
        *   `PRESENTATION.md`
        *   `SUMMARY.md`
        *   `KAGGLE_DATASET_KULLANIM_KILAVUZU.md`
        *   `.gitignore`
        *   `images/` (klasör ve içindeki `bbc_logo.png`, `news_classification_icon.png`)

3.  **Klasör Yapısı Kontrolü:**
    *   Ana klasörünüzün (`NLP_Odevim`) yapısı şu şekilde görünmelidir:

    ```
    NLP_Odevim/
    ├── News_Category_Dataset_v3.json
    ├── app.py
    ├── bbc_news_classification_with_word2vec.ipynb
    ├── prepare_kaggle_dataset.py
    ├── requirements.txt
    ├── README.md
    ├── PROJECT_REPORT.md
    ├── PRESENTATION.md
    ├── SUMMARY.md
    ├── KAGGLE_DATASET_KULLANIM_KILAVUZU.md
    ├── .gitignore
    ├── images/
    │   ├── bbc_logo.png
    │   └── news_classification_icon.png
    ├── inputs/      (Bu klasör prepare_kaggle_dataset.py çalıştırılınca oluşturulacak)
    ├── models/      (Bu klasör prepare_kaggle_dataset.py çalıştırılınca oluşturulacak, notebook tarafından kullanılacak)
    └── outputs/     (Bu klasör prepare_kaggle_dataset.py çalıştırılınca oluşturulacak)
    ```

## Bölüm 2: Gerekli Ortamın Kurulumu

1.  **Python Kurulumu (Eğer Yoksa):**
    *   Python 3.8 veya üzeri bir sürümün kurulu olduğundan emin olun. Python'ı resmi web sitesinden indirebilirsiniz: [https://www.python.org/downloads/](https://www.python.org/downloads/)

2.  **Sanal Ortam Oluşturma (Önemle Önerilir):**
    *   Terminali (Komut İstemi, PowerShell veya Linux/macOS terminali) proje ana klasöründe (`NLP_Odevim`) açın.
    *   Aşağıdaki komutla bir sanal ortam (`.venv` adında) oluşturun:
        ```bash
        python -m venv .venv
        ```

3.  **Sanal Ortamı Aktif Etme:**
    *   **Windows için:**
        ```bash
        .venv\Scripts\activate
        ```
    *   **Linux/macOS için:**
        ```bash
        source .venv/bin/activate
        ```
    *   Sanal ortam aktif olduğunda, terminalde komut satırının başında `(.venv)` ibaresi görünecektir.

4.  **Gerekli Kütüphaneleri Yükleme:**
    *   Aktif sanal ortamda, aşağıdaki komutla `requirements.txt` dosyasındaki tüm kütüphaneleri yükleyin:
        ```bash
        pip install -r requirements.txt
        ```
    *   Bu komut, projenin ihtiyaç duyduğu `pandas`, `nltk`, `scikit-learn`, `gensim`, `streamlit`, `matplotlib`, `seaborn` gibi tüm kütüphaneleri kuracaktır.

## Bölüm 3: Veri Setinin Hazırlanması

1.  **`News_Category_Dataset_v3.json` Dosyasının Yerleşimi:**
    *   Kaggle'dan indirdiğiniz `News_Category_Dataset_v3.json` dosyasının proje ana klasöründe (`NLP_Odevim`) olduğundan emin olun.

2.  **Veri Hazırlama Betiğini Çalıştırma:**
    *   Sanal ortamınız aktifken ve proje ana klasöründeyken, aşağıdaki komutu çalıştırın:
        ```bash
        python prepare_kaggle_dataset.py
        ```
    *   Bu işlem `News_Category_Dataset_v3.json` dosyasını işleyerek `inputs/news_category_dataset.csv` dosyasını (BBC kategorilerine eşlenmiş veri içerir) ve `inputs/category_mapping.json` dosyasını oluşturacaktır. Ayrıca `outputs` klasörüne `bbc_categories_distribution.png` adlı bir kategori dağılım grafiği kaydedecektir.
    *   Terminalde işlemin başarıyla tamamlandığına dair mesajları görmelisiniz.

## Bölüm 4: Jupyter Notebook'un Çalıştırılması, Model Eğitimi ve Test Edilmesi

Jupyter Notebook, veri ön işleme, özellik çıkarma, model eğitimi, değerlendirme ve bu süreçlerin detaylı analizini içerir.

1.  **Jupyter Notebook'u Başlatma:**
    *   Sanal ortamınız aktifken, terminalde aşağıdaki komutu çalıştırın:
        ```bash
        jupyter notebook
        ```
    *   Bu komut web tarayıcınızda Jupyter arayüzünü açacaktır.

2.  **Notebook Dosyasını Açma:**
    *   Tarayıcıdaki Jupyter arayüzünden `bbc_news_classification_with_word2vec.ipynb` dosyasına tıklayarak açın.

3.  **Notebook Hücrelerini Çalıştırma ve Metodolojiyi Anlama:**
    *   **Veri Yükleme Hücresini Kontrol Etme:** Notebook'un başındaki veri yükleme hücresinin `pd.read_csv('inputs/news_category_dataset.csv')` şeklinde olduğundan emin olun.
    *   Hücreleri sırayla (`Shift+Enter` veya "Cell" > "Run Cells") çalıştırarak adımları takip edin.

    *   **4.1. Veri Ön İşleme (Text Preprocessing):**
        *   **Metin Temizleme:** Özel karakterlerin, sayıların ve gereksiz boşlukların kaldırılması için **Regular Expressions (RegEx)** kullanılmıştır.
        *   **Metin Normalizasyon:**
            *   **Lowercasing:** Tüm metin küçük harfe çevrilmiştir.
            *   **Lemmatization (NLTK WordNetLemmatizer):** Kelimeler kök formlarına (lemma) indirgenmiştir. Örneğin, "running" -> "run", "better" -> "good". Bu, kelime dağarcığını azaltır ve modelin genelleme yapmasına yardımcı olur.
            *   **Stop Words Kaldırma (NLTK):** İngilizce için yaygın olan ve anlam taşımayan kelimeler (örn: "the", "is", "in") metinden çıkarılmıştır.
        *   **Tokenization (NLTK):** Metinler kelime listelerine (token) bölünmüştür.
        *   **Edit Distance (Düzeltme):** Bu projede doğrudan bir edit distance tabanlı yazım düzeltme adımı uygulanmamıştır. Lemmatization ve stop word kaldırma gibi adımlar, bazı küçük yazım hatalarının etkisini dolaylı olarak azaltabilir. Daha kapsamlı bir yazım düzeltme için ek kütüphaneler (örn: `pyspellchecker`) entegre edilebilir, ancak bu projenin mevcut kapsamında yer almamaktadır.

    *   **4.2. Özellik Çıkarma (Feature Engineering):**
        *   **Word2Vec (Gensim):** Kelimeleri yoğun vektör temsillerine dönüştürmek için Word2Vec modeli kullanılmıştır. Bu model, kelimelerin anlamsal benzerliklerini yakalayabilir. Her bir haber metni, içerdiği kelimelerin Word2Vec vektörlerinin ortalaması alınarak tek bir vektörle temsil edilmiştir. Bu, metnin genel anlamsal içeriğini yansıtan bir özelliktir.
        *   **N-gram Modelleri:**
            *   Bu projede özellik çıkarma aşamasında Word2Vec öncelikli olarak kullanılmıştır. N-gram'lar (örneğin bigram veya trigram), metin içindeki ardışık kelime dizilerini analiz etmek için güçlü bir tekniktir ve TF-IDF gibi yöntemlerle birleştirilerek özellik olarak kullanılabilir.
            *   Notebook'ta doğrudan bir N-gram tabanlı özellik vektörü oluşturulup sınıflandırıcıya verilmemiştir. Ancak, N-gram analizi, metinlerin yapısını ve sık kullanılan ifadeleri anlamak için keşifsel veri analizi (EDA) aşamasında veya Word2Vec'e alternatif/tamamlayıcı olarak düşünülebilir.
            *   Ödev gereksinimlerinde N-gram analizi istendiği için, `PROJECT_REPORT.md` dosyasında N-gram'ların ne olduğunu, nasıl çalıştığı ve bu projede neden Word2Vec'in tercih edildiği veya N-gram'ların nasıl entegre edilebileceği tartışılabilir.

    *   **4.3. Metin Sınıflandırma (Text Classification) - Model Eğitimi:**
        *   Veri seti, eğitim (%80) ve test (%20) olmak üzere ikiye ayrılmıştır.
        *   Aşağıdaki sınıflandırma algoritmaları denenmiş ve karşılaştırılmıştır:
            *   **Logistic Regression:** Doğrusal bir modeldir, olasılıksal tahminler yapar.
            *   **Support Vector Machine (SVM):** Özellikle yüksek boyutlu uzaylarda etkili olan bir sınıflandırıcıdır.
            *   **Naive Bayes:** Olasılıksal bir sınıflandırıcıdır, kelime frekanslarına dayanır. (Bu projede doğrudan kullanılmamış olabilir, ancak ödev gereksinimlerinde alternatif olarak belirtilmiştir.)
            *   **Decision Trees / Random Forest:** Karar ağacı tabanlı modellerdir. (Bu projede doğrudan kullanılmamış olabilir, ancak ödev gereksinimlerinde alternatif olarak belirtilmiştir.)
        *   Seçilen modeller, Word2Vec ile oluşturulan metin vektörleri ve bunlara karşılık gelen kategori etiketleri kullanılarak eğitilmiştir.

    *   **4.4. Model Değerlendirme (Model Evaluation):**
        *   Eğitilen modellerin performansı test seti üzerinde değerlendirilmiştir.
        *   **Önemli Metrikler:**
            *   **Accuracy (Doğruluk):** Modelin doğru yaptığı tahminlerin toplam tahmin sayısına oranı. Genel performansı gösterir.
            *   **Precision (Kesinlik):** Bir kategori için pozitif olarak tahmin edilen örneklerden kaçının gerçekten pozitif olduğu. (TP / (TP + FP)). Yanlış pozitiflerin maliyetli olduğu durumlarda önemlidir.
            *   **Recall (Duyarlılık veya Hassasiyet):** Bir kategorideki gerçekten pozitif olan örneklerden kaçının model tarafından doğru tahmin edildiği. (TP / (TP + FN)). Yanlış negatiflerin maliyetli olduğu durumlarda önemlidir.
            *   **F1-Score (F1 Puanı):** Precision ve Recall metriklerinin harmonik ortalamasıdır (2 * (Precision * Recall) / (Precision + Recall)). Dengesiz veri setlerinde veya hem precision hem de recall önemli olduğunda iyi bir ölçüttür.
        *   Bu metrikler, her bir kategori için ayrı ayrı ve genel (makro/mikro ortalamalar) olarak hesaplanmıştır. **Sınıflandırma Raporu (Classification Report)** bu metrikleri özetler.
        *   **Karışıklık Matrisi (Confusion Matrix):** Modelin hangi kategorileri birbiriyle karıştırdığını görsel olarak gösterir. Matrisin köşegenleri doğru tahminleri, diğer hücreler ise yanlış tahminleri gösterir.

    *   **4.5. Model Kaydetme:**
        *   Notebook'un sonlarına doğru, genellikle en iyi performansı veren sınıflandırma modeli (örneğin, SVM) ve eğitilmiş Word2Vec modeli, daha sonra Streamlit uygulamasında kullanılmak üzere `models` klasörüne `.pkl` veya `.joblib` formatında kaydedilmiştir.

## Bölüm 5: Streamlit Web Uygulamasının Çalıştırılması ve Test Edilmesi

Streamlit uygulaması, eğittiğiniz modeli kullanarak canlı haber metni sınıflandırması yapmanızı sağlar.

1.  **Streamlit Uygulamasını Başlatma:**
    *   Sanal ortamınız aktifken ve proje ana klasöründeyken, (gerekirse) yeni bir terminal açın.
    *   Aşağıdaki komutu çalıştırın:
        ```bash
        streamlit run app.py
        ```
    *   Bu komut web tarayıcınızda Streamlit uygulamasını açacaktır.

2.  **Streamlit Uygulamasını Test Etme Adımları:**
    *   **Arayüz Kontrolü:** Uygulamanın başlığının ("📰 BBC News Classifier"), öğrenci bilgilerinizin ve diğer metinlerin doğru göründüğünü kontrol edin.
    *   **Model Yükleme:** Uygulamanın başlangıçta `models` klasöründen kaydedilmiş sınıflandırma modelini ve Word2Vec modelini başarıyla yüklediğinden emin olun.
    *   **Metin Girişi:** Kenar çubuğundaki "Haber Metnini Girin" alanına çeşitli haber metinleri yapıştırın.
        *   Örnekler için önceki yanıtlara veya kendi bulacağınız haber metinlerine bakabilirsiniz.
    *   **Sınıflandırma Butonu:** "Sınıflandır" butonuna tıklayın.
    *   **Sonuçları İnceleme:** Tahmin edilen kategoriyi ve olasılık grafiğini inceleyin.
    *   **Kapsamlı Test:** Farklı kategorilerden, farklı uzunluklarda ve belirsiz metinlerle testler yapın.

## Bölüm 6: Genel Proje Değerlendirmesi ve Raporlama

1.  **Ödev Gereksinimleri Kontrolü:**
    *   Projenizin, ödev tanımında belirtilen tüm NLP tekniklerini içerdiğinden emin olun.

2.  **Rapor ve Sunum Dosyaları:**
    *   `PROJECT_REPORT.md` ve `PRESENTATION.md` dosyalarının metodolojinizi, veri setinizi, modelleri, sonuçları ve metrikleri detaylıca açıkladığını kontrol edin.
    *   **Özellikle N-gram ve Edit Distance konularına değinin:** `PROJECT_REPORT.md` dosyasında, N-gram modellerinin ne olduğunu, kelime dizilerini analiz etmedeki önemini, TF-IDF gibi yöntemlerle nasıl kullanılabileceğini ve bu projede neden doğrudan bir özellik olarak kullanılmadığını (örneğin, Word2Vec'in anlamsal temsildeki gücü nedeniyle) veya nasıl entegre edilebileceğini açıklayın. Benzer şekilde, Edit Distance'ın yazım düzeltmedeki rolünü ve bu projede neden doğrudan bir adım olarak eklenmediğini (belki lemmatization'ın kısmi faydası veya projenin mevcut kapsamı nedeniyle) belirtin.

3.  **Kod Kalitesi:**
    *   Jupyter Notebook ve Streamlit uygulamasındaki kodların okunabilir ve anlaşılır olduğundan emin olun.

## Sonuç

Bu rehberdeki adımları izleyerek projenizi başarılı bir şekilde kurmuş, çalıştırmış ve test etmiş olmalısınız. Başarılar! 