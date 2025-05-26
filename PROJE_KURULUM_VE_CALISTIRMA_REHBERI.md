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

## Bölüm 4: Jupyter Notebook'un Çalıştırılması ve Test Edilmesi

Jupyter Notebook, veri ön işleme, model eğitimi ve değerlendirme adımlarını içerir.

1.  **Jupyter Notebook'u Başlatma:**
    *   Sanal ortamınız aktifken, terminalde aşağıdaki komutu çalıştırın:
        ```bash
        jupyter notebook
        ```
    *   Bu komut web tarayıcınızda Jupyter arayüzünü açacaktır. Genellikle `http://localhost:8888/` adresinde çalışır.

2.  **Notebook Dosyasını Açma:**
    *   Tarayıcıdaki Jupyter arayüzünden `bbc_news_classification_with_word2vec.ipynb` dosyasına tıklayarak açın.

3.  **Notebook Hücrelerini Çalıştırma:**
    *   **Veri Yükleme Hücresini Kontrol Etme:** Notebook'un başındaki veri yükleme hücresinin `KAGGLE_DATASET_KULLANIM_KILAVUZU.md` dosyasında belirtildiği gibi `pd.read_csv('inputs/news_category_dataset.csv')` şeklinde olduğundan emin olun.
    *   Hücreleri sırayla çalıştırmak için "Cell" menüsünden "Run All" seçeneğini kullanabilir veya her hücreyi seçip `Shift+Enter` tuşlarına basarak çalıştırabilirsiniz.
    *   NLTK kütüphanesi için bazı ek dosyaların (stopwords, wordnet) indirilmesi gerekebilir. Eğer hata alırsanız, notebook içindeki ilgili NLTK indirme komutlarını çalıştırın.

4.  **Notebook Testi ve Değerlendirme Adımları:**
    *   **Veri Yükleme ve Ön İşleme:** İlk hücrelerin hatasız çalıştığını ve `inputs/news_category_dataset.csv` dosyasının doğru yüklendiğini kontrol edin. Veri setinin şeklini (satır, sütun sayısı) ve ilk birkaç satırını inceleyin.
    *   **Metin Temizleme ve Normalizasyon:** Metin temizleme (noktalama işaretlerinin kaldırılması, küçük harfe çevirme) ve normalizasyon (lemmatization) adımlarının uygulandığını gözlemleyin.
    *   **Word2Vec Model Eğitimi:** Word2Vec modelinin kelime vektörlerini oluşturma sürecini takip edin.
    *   **Makine Öğrenmesi Modellerinin Eğitimi:** Logistic Regression, SVM gibi farklı sınıflandırıcıların eğitildiği bölümleri çalıştırın.
    *   **Model Değerlendirme:**
        *   Her model için oluşturulan **Sınıflandırma Raporu (Classification Report)** çıktısını dikkatlice inceleyin. Burada `Accuracy` (Doğruluk), `Precision` (Kesinlik), `Recall` (Duyarlılık) ve `F1-score` (F1 Puanı) metriklerini göreceksiniz. Bu metrikler modelin her bir kategori ve genel performansı hakkında bilgi verir.
        *   **Karışıklık Matrisi (Confusion Matrix)** görselini inceleyerek modelin hangi kategorileri doğru tahmin ettiğini, hangilerini karıştırdığını analiz edin.
    *   **Model Kaydetme:** Notebook'un sonlarına doğru en iyi performansı veren modelin (ve Word2Vec modelinin) `.pkl` veya `.joblib` dosyası olarak `models` klasörüne kaydedildiğini doğrulayın. Örneğin, `svc_model.pkl` ve `word2vec_model.pkl` gibi.

## Bölüm 5: Streamlit Web Uygulamasının Çalıştırılması ve Test Edilmesi

Streamlit uygulaması, eğittiğiniz modeli kullanarak canlı haber metni sınıflandırması yapmanızı sağlar.

1.  **Streamlit Uygulamasını Başlatma:**
    *   Sanal ortamınız aktifken ve proje ana klasöründeyken, (gerekirse) yeni bir terminal açın.
    *   Aşağıdaki komutu çalıştırın:
        ```bash
        streamlit run app.py
        ```
    *   Bu komut web tarayıcınızda Streamlit uygulamasını açacaktır. Genellikle `http://localhost:8501/` adresinde çalışır.

2.  **Streamlit Uygulamasını Test Etme Adımları:**
    *   **Arayüz Kontrolü:** Uygulamanın başlığının ("📰 BBC News Classifier"), öğrenci bilgilerinizin ve diğer metinlerin doğru göründüğünü kontrol edin.
    *   **Model Yükleme:** Uygulamanın başlangıçta `models` klasöründen kaydedilmiş sınıflandırma modelini ve Word2Vec modelini başarıyla yüklediğinden emin olun. Terminalde hata mesajı olup olmadığını kontrol edin.
    *   **Metin Girişi:** Kenar çubuğundaki "Haber Metnini Girin" alanına çeşitli haber metinleri yapıştırın.
        *   **Örnek 1 (Spor):** "Fenerbahçe, Avrupa Ligi çeyrek final maçında rakibini 2-0 mağlup ederek tur için avantaj sağladı. Maçta etkili bir futbol sergilendi."
        *   **Örnek 2 (Teknoloji):** "Yeni tanıtılan akıllı telefon modeli, gelişmiş kamera özellikleri ve uzun pil ömrü ile dikkat çekiyor. Yapay zeka entegrasyonu da kullanıcı deneyimini artırıyor."
        *   **Örnek 3 (Ekonomi/İş Dünyası):** "Merkez Bankası'nın faiz kararı sonrası döviz kurlarında hareketlilik yaşandı. Enflasyonla mücadele kapsamında yeni tedbirler alınması bekleniyor."
    *   **Sınıflandırma Butonu:** "Sınıflandır" butonuna tıklayın.
    *   **Sonuçları İnceleme:**
        *   Uygulamanın tahmin ettiği kategoriyi ("Tahmin Edilen Kategori") ve bu tahmine ne kadar güvendiğini gösteren olasılık grafiğini ("Tahmin Olasılıkları") inceleyin.
        *   Tahminin doğruluğunu kendi bilginizle veya metnin gerçek kategorisiyle karşılaştırın.
    *   **Farklı Metinlerle Kapsamlı Test:**
        *   Her bir kategoriye (business, entertainment, politics, sport, tech) ait olduğundan emin olduğunuz en az 2-3 farklı metinle test yapın.
        *   Çok kısa metinler girerek modelin nasıl tepki verdiğini gözlemleyin.
        *   Birden fazla konuyu içeren veya kategorisi belirsiz metinler kullanarak modelin sınırlarını test edin.
        *   Türkçe olmayan metinler girin (model Türkçe metinler için eğitildiğinden bu durumda düşük olasılıklı veya anlamsız bir kategori tahmini yapması beklenir).

## Bölüm 6: Genel Proje Değerlendirmesi ve Raporlama

1.  **Ödev Gereksinimleri Kontrolü:**
    *   Projenizin, ödev tanımında belirtilen tüm NLP tekniklerini (RegEx, metin normalizasyonu, N-gram, Word2Vec/TF-IDF, sınıflandırıcı, performans metrikleri) içerdiğinden veya bu tekniklerin neden kullanılıp/kullanılmadığının raporunuzda açıklandığından emin olun.

2.  **Rapor ve Sunum Dosyaları:**
    *   `PROJECT_REPORT.md` (Proje Raporu) ve `PRESENTATION.md` (Sunum Taslağı) dosyalarının metodolojinizi, kullandığınız veri setini, modelleri, elde ettiğiniz sonuçları ve değerlendirme metriklerini kapsamlı ve anlaşılır bir şekilde açıkladığını kontrol edin.
    *   Özellikle `PROJECT_REPORT.md` dosyasında, Kaggle veri setini neden seçtiğinizi, BBC kategorileriyle nasıl eşleştirdiğinizi ve bu veri setiyle elde ettiğiniz sonuçları (notebook'taki metrikler) detaylandırın.

3.  **Kod Kalitesi:**
    *   Hem Jupyter Notebook (`bbc_news_classification_with_word2vec.ipynb`) hem de Streamlit uygulaması (`app.py`) içindeki Python kodlarının okunabilir, anlaşılır ve iyi yapılandırılmış olduğundan emin olun. Değişken ve fonksiyon adlarının açıklayıcı olmasına özen gösterin.

## Sonuç

Bu rehberdeki adımları izleyerek projenizi başarılı bir şekilde kurmuş, çalıştırmış ve test etmiş olmalısınız. Projenizin tüm bileşenlerinin doğru çalıştığından, raporlarınızın eksiksiz olduğundan ve ödev gereksinimlerini karşıladığınızdan emin olun. Başarılar! 