### Cangjie giriş yöntemi nedir?

Cangjie (倉頡), Chu Bong-Foo tarafından icat edilen, şekil tabanlı bir Çince giriş yöntemidir. Her karakter, sanal klavyedeki 24 harf tuşuyla eşleştirilmiş yapısal bileşenleriyle (köklerle) kodlanır. Ustalaşıldığında Cangjie, eşsesli kelimeleri ayırt etmeye gerek kalmadan hızlı ve doğru Çince yazmanızı sağlar.

### Cangjie 3. Nesil ile 5. Nesil arasındaki fark nedir?

**3. Nesil** (三代倉頡) standardı, Hong Kong ve Tayvan'da yaygın olarak kullanılan klasik düzendir. **5. Nesil** (五代倉頡) bazı kodlamaları inceltir ve modern karakterlere kapsamı genişletir. iCangJie her iki standardı da barındırır — varsayılan sürümü **Ayarlar → Uygulama Ayarları** bölümünden değiştirin. **Tek karakter** kelime ayrıntı sayfalarında, **yan yana karşılaştırma kartı** her iki sürümü kök klavye şeritleriyle gösterir; herhangi bir kod rozetinde **kopyala**'ya dokunun veya karakteri ya da tüm kodları kopyalamak için araç çubuğunu kullanın.

### "Hızlı yöntem" (速成) ne anlama gelir?

Hızlı yöntem, tam Cangjie kodunun yalnızca **ilk ve son kök tuşlarını** kullanır (seviye 1–2). iCangJie, **Seviyeler**'de hızlı yöntem gezintisini, hızlı kod yazma alıştırmasını ve karışık modu (önce hızlıyı dene, hatadan sonra tam koda dön) destekler.

### Arama nasıl çalışır?

**Arama** sekmesini açın ve şunlardan birini yazın:

- **Cangjie kodu öneki** — ör. `ab`, AB ile başlayan kodlarla eşleşir.
- **Tam karakter** — tek bir Han karakteri yapıştırın veya seçin.
- **Pinyin öneki** — tonsuz pinyin (Ayarlar'dan açılıp kapatılır).
- **Jyutping öneki** — Kantonca romanizasyonu.

Bir mod sonuç döndürmediğinde iCangJie mod değiştirmeyi önerir. Dört **karakter seti önceliği** (Hong Kong, Tayvan Geleneksel, Basitleştirilmiş, Genel) sıralamayı etkiler.

### Yazma Alıştırması nasıl çalışır?

**Yazma**'yı açın ve bir mod seçin:

- **Tam kod** — her karakter için eksiksiz Cangjie kodunu yazın.
- **Hızlı kod** — yalnızca seviye 1–2 hızlı kodlarıyla alıştırma yapın.
- **Karışık** — önce hızlı kodu deneyin; bir hatadan sonra uygulama cevabı gösterir ve tam koda geçer.

İçerik kaynakları arasında 16 yerleşik klasik metin (Basitleştirilmiş ve Geleneksel), rastgele kelime listeleri, yapıştırılan metin, favoriler ve yanlış defteriniz (doğru Han karakterini otomatik çözer) bulunur. Canlı **kök tuşu vurguları**, hangi tuşlara basacağınızı görmenize yardımcı olur. Yanlış tuş davranışı Ayarlar'da **koru veya temizle** olarak belirlenebilir.

Oturum istatistikleri (doğruluk, seri) ve **günlük toplamlar** (~120 gün saklanır), etkinleştirildiğinde iCloud ile senkronize edilir. 7/30 günlük eğilim grafikleri ve kod uzunluğu dağılımı için Yazma merkezinden **Alıştırma Raporu**'nu veya **Ayarlar → Öğrenme İstatistikleri**'ni açın.

### Günlük Test nasıl çalışır?

Her gün ayarlanabilir sayıda soru alırsınız (**5 / 8 / 10 / 15**, varsayılan 8). **Test Ayarları**'nı açmak için test ekranındaki **dişli simgesine** dokunun:

- **Kelime kaynağı** — tüm sözlük, favoriler veya yanlış defteri
- **Kod uzunluğu** — herhangi biri veya 1–5
- **Soru türleri** — karakter→kod, kod→karakter ve ilk tuş sorularını açıp kapatın

Etkinleştirilen üç tür sırayla gelir. Anında geri bildirimli kart tarzı seçenekler; tur sonundaki **yanlış incelemesi** kelime ayrıntısına bağlanır. Yeni bir set için **Yeniden Karıştır**. Yanlış kayıtlar Yanlış Defteri'ne ve yazma tekrarına beslenir.

### Yeni Başlayan Yolu ve tanıtım nedir?

İlk açılışta **5 ekranlık tanıtım**; arama, öğrenme/test, yazma ve widget'ları tanıtır (atlanabilir). İstediğiniz zaman **Ayarlar → Uygulama Ayarları**'ndan yeniden çalıştırabilirsiniz. **Öğren** sekmesinde, **Yeni Başlayan Yolu** kartı aramayı, bugünün testini, ilk eğitimi ve widget kılavuzunu (iOS) tek dokunuşla denemek için bağlantılar sunar. Kartı kalıcı olarak gizlemek için ✕ ile kapatın.

### Öğrenme verilerini nasıl yedekler ve geri yüklerim?

**Ayarlar → Öğrenme İstatistikleri → Yedekle ve Geri Yükle**'ye gidin. **JSON Dışa Aktar**, favorileri, öğrenme durumunu, yanlış defterini, test puanlarını, yazma istatistiklerini, günlük yazma kayıtlarını ve metin ilerlemesini bir `.icangjie-backup` dosyasına kaydeder. **İçe Aktar**, mevcut verilerle **birleştirmenize** veya yerel öğrenme verilerini tamamen **değiştirmenize** olanak tanır. Yedekler cihazınızda veya seçtiğiniz bulut depolamada kalır — iHTC Studio bunları asla almaz.

### Öğrenme Durumu nasıl çalışır?

Her karakterin dört durumdan biri vardır: Öğrenilmedi, Öğreniliyor, Öğrenildi veya Ustalaşıldı. Kelime ayrıntı sayfasında elle yükseltin veya düşürün. Ayarlar'daki İstatistikler kartı dökümünüzü gösterir. **Learning Progress** widget'ı bu sayıları yansıtır.

### Eğitimleri nasıl okurum?

11 HTML ders ve gruplanmış kök tablosu görselleri için **Öğren**'e gidin. Eğitim araç çubuğunda **okuma boyutunu** (%85–%160) ayarlayın. HTML açık/koyu moda uyum sağlar; uygulama dili zh-Hant olduğunda Geleneksel yazı kullanılır. Tabloları sıkıştırarak yakınlaştırın; 1× yakınlaştırmada görseller arasında kaydırın; Fotoğraflar'a kaydedin veya paylaşın (iOS).

### Pinyin ve Cangjie Dönüştürücü nedir?

**Ayarlar → Metin Araçları → Pinyin ve Cangjie Dönüştürücü** altında Çince metni yapıştırın ve birden fazla çıktı stilini (tonlu, düz, numaralı, açıklamalı, hizalı ızgara ve daha fazlası) önizleyin. İsteğe bağlı olarak mevcut standardınızın Cangjie kodlarını üst üste bindirebilir, ardından kopyalayabilir veya önizleme görseli olarak paylaşabilirsiniz.

### iCloud senkronizasyonunu nasıl ayarlarım?

**Ayarlar → iCloud Senkronizasyonu**'na gidin ve açın. iCloud'a giriş yaptığınızdan emin olun. Etkinleştiğinde iCangJie; favorileri, öğrenme durumunu, yanlış soru defterini, test puanlarını ve seriyi, yazma istatistiklerini ve yerleşik metin ilerlemesini cihazlarınız arasında senkronize eder. İstediğiniz zaman kapatabilirsiniz.

Yazma arayüzü tercihleri (yanlış tuşları koruma, metin pinyin'i) yalnızca her cihazda kalır.

### Widget'ları nasıl eklerim ve kullanırım?

Ana Ekran'a veya Kilit Ekranı'na uzun basın, **+** simgesine dokunun ve "iCangJie" araması yapın. iCangJie **8 widget türü** sunar: Daily Character (küçük ve ortada karıştırma), Code Length (eklerken 1–5 seçin; üçlüyü yenilemek için küçük ve ortada **karıştırma düğmesi**), Daily Quiz, Typing Glance, Favorites, Wrong Book, Recent ve Learning Progress. Favorites / Wrong / Recent, kodlu pirinç ızgarası önizlemeleri gösterir. Widget'lar StandBy'da da çalışır (iOS 17+). Adım adım kurulum için uygulama içindeki **Widget Kılavuzu**'na bakın.

### Temaları ve dili nasıl özelleştiririm?

**15 hazır gradyan tema** veya özel bir vurgu rengi için **Ayarlar → Tema**'ya gidin. Karakter **karo ızgaraları**, liste ve ızgara görünümlerinde **temanızın** vurgu rengini izler. Görünümü sistem / açık / koyu olarak ayarlayın. **Uygulama Ayarları** altında **uygulama içi dili** seçin (İngilizce, Basitleştirilmiş Çince, Geleneksel Çince veya sistemi izle) — arayüz anında yenilenir. Widget'lar dili ve vurguyu App Group üzerinden yansıtır.

**Ayarlar → Uygulama Ayarları → Ana Ekran kısayolları** altında en fazla **4 Ana Ekran Hızlı İşlemi** yapılandırın. iOS'ta, favorileri ve son karakterleri sistem Spotlight'ında dizinlemek için aynı karttaki **Spotlight Araması**'nı açıp kapatın (en fazla 80 girdi, 30 günde sona erer).

### Siri ve Kısayollar App Intent'leri nedir?

iOS 16+ sürümünde iCangJie, yerleşik **App Intent'leri** kaydeder: bir karakterin Cangjie kodunu arama, günlük testi başlatma ve arama ekranını açma. Bunları **Kısayollar** uygulamasında bulun veya *"iCangJie'de 颉 için Cangjie kodunu ara"* gibi ifadeler söyleyin. Intent'ler, uygulama açıldığında işlenen bekleyen bir derin bağlantı yazar. [URL Şeması Başvurusu](../url-scheme)'na bakın.

### Derin Bağlantılar nedir ve nasıl kullanılır?

iCangJie, `iCangJie://` URL şemasını destekler. Yollar: `search`, `word`, `quiz`, `typing`, `favorites`, `wrong`, `levels`, `learn`, `feedback` ve `review`. Bunları Kısayollar'da, yer imlerinde veya otomasyonlarda kullanın. [URL Şeması Başvurusu](../url-scheme)'na bakın.

### iCangJie Mac'te çalışır mı?

Evet. iCangJie; saydam gezinti çubuğu, Esc ile geri gitme, sistem paylaşım sayfası ve tam yazma alıştırması içeren yerel bir macOS uygulamasıdır. Arama, sistem arama çubuğuyla bütünleşir; eğitimlerdeki harici bağlantılar Safari'de açılır.

### iCangJie çevrimdışı çalışır mı?

Evet. Sözlük, testler, eğitimler, yazma alıştırması ve dönüştürücü araçları çevrimdışı çalışır. İsteğe bağlı iCloud senkronizasyonu Apple'ın iCloud Anahtar-Değer Depolaması'nı kullanır. Çevrimiçi arama (Youdao) ve harici eğitim bağlantıları ağ gerektirir.

### iCangJie neden Fotoğraf Kitaplığı erişimi ister?

Yalnızca bir eğitimdeki kök tablosu görselinde **Fotoğraflar'a Kaydet**'e dokunduğunuzda. iCangJie yalnızca **ekleme** yetkisi ister — mevcut fotoğraflarınızı asla okumaz.

### iCangJie herhangi bir kişisel veri toplar mı?

Hayır. iCangJie kişisel veri toplamaz, saklamaz veya iletmez. Analiz, reklam SDK'sı veya izleme yoktur. [Gizlilik Politikası](../privacy)'na bakın.

### Hâlâ yardıma mı ihtiyacınız var?

Bize [AppleOSer@gmail.com](mailto:AppleOSer@gmail.com) adresinden ulaşın, 48 saat içinde size dönüş yapacağız.
