### iLinux bir hesap veya internet bağlantısı gerektiriyor mu?

Hayır. iLinux komut kitaplıkları için tamamen çevrimdışı çalışır. Tüm komut verileri (JSON özetleri ve Markdown belgeleri) uygulamanın içinde paketlenmiştir. Belgelere göz atmak, belgeleri okumak veya sınavlara katılmak için kaydolmanıza gerek yoktur. İsteğe bağlı **iCloud senkronizasyonu**, favorilerinizi hizalamak ve cihazlar arasında ilerlemek için Apple Kimliğinizi kullanır; komut içeriğini yüklemez.

### iLinux Mac'i destekliyor mu?

Evet. iLinux **kenar çubuğu masaüstü düzeni**, yeniden boyutlandırılabilir pencere ve genişletilmiş klavye kısayolları (**⌘,**, **⌘[**, **Esc**, **⌘←/→**, test tuşları **1–4** / **⌘R** / **Return**) içeren **yerel bir macOS uygulamasıdır** (macOS **13.0+**, Mac Catalyst değil). Tüm temel özellikler (üç kabuk kitaplığı, eşdeğerleri, sınav, derin bağlantılar ve temalar) Mac'te çalışır.

**Mac'te geçerli değildir:** Ana Ekran widget'ları, Ana Ekran hızlı eylemleri ve alternatif uygulama simgeleri **yalnızca iPhone/iPad'de mevcuttur**. İOS'ta widget'ları yapılandırın; Mac, uygulama içi bir bildirim gösteriyor.

### iCloud senkronizasyonu nasıl çalışır?

**iCloud**'da aynı Apple kimliğiyle oturum açtığınızda, **Ayarlar → Öğrenme istatistikleri** bölümünde **iCloud Senkronizasyonu**'nu etkinleştirin. iLinux, **favorileri**, **sınav ilerlemesini**, **temayı** ve **görüntüleme tercihlerini** (dil, kabuk platformu, favori kapsamı, liste/tablo) iCloud Anahtar-Değer Depolama aracılığıyla **iPhone, iPad ve Mac** genelinde senkronize eder. Çatışmalar otomatik olarak birleşir (örneğin, favorilerin birleşmesi). Diğerlerini etkilemeden **bir cihazdaki senkronizasyonu devre dışı bırakabilirsiniz**. Komut kitaplıkları tamamen çevrimdışı kalır; yalnızca kişisel ilerlemeniz senkronize edilir.

### iLinux komutları gerçek bir Linux terminalinde çalıştırıyor mu?

Hayır. iLinux **yalnızca bir referans ve öğrenme aracıdır**. Bir kabuk, SSH istemcisi veya uzaktan yürütme ortamı sağlamaz. Komutlar çalışma amacıyla belgelenmiştir; bunları kendi Linux makinenizde, Windows PC'nizde, sunucunuzda veya bulut örneğinizde uygularsınız.

### iLinux hangi kabuk platformlarını destekliyor?

iLinux içerik dili başına üç çevrimdışı komut kütüphanesi sunar:

- **Linux** — 14 kategoride 1050 komut
- **Windows CMD / Batch** — 10 kategoride 300 komut
- **PowerShell** — 10 kategoride 300 komut

Dil başına **toplam 1650'den fazla komut** (İngilizce, Basitleştirilmiş Çince, Geleneksel Çince). Araç çubuğu Kabuk menüsünden **Komutlar**, **Kategoriler** veya **Günlük Sınav** üzerinden kitaplıklar arasında geçiş yapın.

### Linux, CMD ve PowerShell arasında nasıl geçiş yapabilirim?

Komutlar, Kategoriler veya Günlük Test sekmesindeki araç çubuğundaki **Shell platformu** menüsüne (terminal simgesi) dokunun. Seçiminiz devam eder ve o platform için aramayı, kategorileri, sınav sorularını ve öğrenme istatistiklerini kapsar.

**Ayarlar → Ana sayfa hızlı erişimi** bölümünde ayrıca varsayılan bir kabuk platformu, **sık kullanılanlar kapsamı** (tüm platformlar ve yalnızca mevcut platform) ve Günlük Komut ve Kategori Gündemi widget'ları için **widget komut kitaplığı** da ayarlayabilirsiniz.

### Platformlar arası eşdeğer komutlar nelerdir?

**100+ equivalent groups** link commands that accomplish the same task across Linux, CMD and PowerShell — for example `ls`, `dir` and `Get-ChildItem`. On a command detail page, the **Equivalents** bar shows related entries; tap one to jump to that platform's documentation instantly.

### Kaç tane komut yer alıyor?

Her içerik dili, üç kabuk kitaplığında **1650+** komutlar içerir:

| platformu | Komutlar | Kategoriler |
|----------|----------|------------|
| Linux | 1050 | 14 |
| CMD / Toplu | 300 | 10 |
| PowerShell | 300 | 10 |

Tüm belgeler çevrimdışı olarak İngilizce, Basitleştirilmiş Çince ve Geleneksel Çince dillerinde mevcuttur.

### Bir komutu nasıl arayabilirim?

Komutlar sekmesindeki büyüteç simgesine dokunun veya donanım klavyesinde **⌘F** tuşuna basın. Bir komut adı, anahtar kelime veya açıklamanın bir kısmını yazın. Sonuçlar siz yazdıkça gerçek zamanlı olarak güncellenir.

### Liste ve tablo görünümü arasında nasıl geçiş yapabilirim?

**Komutlar** veya **Kategoriler** sekmesinde araç çubuğu filtre menüsünü (huni simgesi) açın. **Görüntüleme Modu** altında **Liste** veya **Izgara**'yı seçin. Izgara modunda, satır başına sütunları ayarlamak için **+ / −** düğmelerini kullanın (iPhone'da **1–6**, iPad ve Mac'te **1–8**). Varsayılanı **Ayarlar → Ekran** bölümünden de değiştirebilirsiniz.

### Öğrenme ilerlememi nasıl takip ederim?

Bir komutun ayrıntı sayfasını açın ve durumunu **Öğrenilmemiş**, **Öğrenilmiş** veya **Uzmanlaşmış** olarak ayarlayın. Liste görünümünde hızlı durum ve favori eylemler için bir satırı kaydırın. Izgara görünümünde favorilere eklemek için yıldız düğmesini ve durum için içerik menüsünü kullanın. Henüz çalışmadığınız komutlara odaklanmak için araç çubuğu menüsünden **Öğrenilmemiş** olarak filtreleyin.

### Hangi diller mevcut?

iLinux, hem uygulama arayüzü hem de komut belgeleri için üç dili destekler:

- **İngilizce**
- **Basitleştirilmiş Çince (简体中文)**
- **Geleneksel Çince (繁體中文)**

Cihazınızın yerel ayarını takip etmek için **Sistem**'i de seçebilirsiniz. **Ayarlar → Dil** bölümünden dili değiştirin. Widget'lar da dahil olmak üzere uygulamanın tamamı anında güncellenir.

### Günlük Sınav nasıl çalışır?

Her gün, **aktif kabuk platformuna göre belirlenen** (Linux, CMD veya PowerShell) tarihe dayalı bir tohum kullanılarak yeni bir test soruları seti oluşturulur. iLinux'u aynı gün kullanan herkes, o platform için aynı temel sınav setini alır. İki soru türü görünür:

- **Eşleşme Özeti** — kısa bir açıklama görürsünüz ve doğru komut adını seçmelisiniz.
- **Eşleştirme Seçeneği Anlamı** — bir bayrağın açıklamasını görürsünüz (ör. `-r: recursive`) ve bunun hangi komuta ait olduğunu tanımlamanız gerekir.

Tap the **refresh button** (circular arrow) in the toolbar to get a different randomised set at any time. **Perfect streak** days (consecutive days with a perfect score) are tracked per platform and shown in the quiz screen and Quiz Glance widget. Generic help flags like `-h` and `--version` are excluded to keep questions unambiguous.

### Yanlış cevaplarım kaydedilmiyor. Ne yapmalıyım?

Bir sınav oturumunu tamamladıktan sonra yanlış cevaplar otomatik olarak kaydedilir. Test turunun tamamını bitirdiğinizden emin olun (tüm soruları yanıtlayın ve sonuç ekranına ulaşın). Kısmen tamamlanan oturumlar kaydedilmez.

Kaydedilen tüm yanlış cevapları **Ayarlar → Yanlış Cevap Defteri** bölümünden inceleyebilirsiniz.

### Favorilere nasıl komut eklerim?

Herhangi bir komutun ayrıntı sayfasını açın ve sağ üst köşedeki **yıldız simgesine** dokunun. **tablo görünümünde** doğrudan komut hücresindeki yıldıza dokunun. Tüm favorilere **Ayarlar → Favoriler** veya **Favoriler** hızlı filtresinden erişin.

### Ana Ekran Widget'larını nasıl ayarlarım?

1. Ana Ekranınızın boş bir alanına uzun basın ve üst köşedeki **+** düğmesine dokunun.
2. Widget galerisinde **iLinux**'u arayın.
3. Bir widget stili seçin ve **Widget Ekle**'ye dokunun.

Adım adım **Widget Kılavuzu** ayrıca **Ayarlar → Widget Kılavuzu**'nda da mevcuttur. Widget arka planlarının uygulama temanızın eğimini takip etmesini sağlamak için **Ayarlar → Widget'lar** bölümündeki seçeneği etkinleştirin.

**Widget komut kitaplığı:** **Ayarlar → Widget'lar** bölümünde, Günlük Komut ve Kategori Spot Işığı widget'larını hangi kabuk kitaplığının (Linux / CMD / PowerShell) besleyeceğini seçin. Bu, uygulama içi kabuk anahtarından bağımsızdır; uygulama içinde Linux'a göz atarken widget'ların Windows komutlarını göstermesini istiyorsanız kullanışlıdır.

### Günlük Komut widget'ı her gün aynı komutu gösterir. Bunu nasıl değiştiririm?

Hemen farklı bir komut yüklemek için Günlük Komut widget'ının sağ üst köşesindeki **dairesel ok (karıştır) düğmesine** dokunun. Bu özellik **iOS 17 veya üzeri** gerektirir.

iOS 16'da Günlük Komut widget'ı her gün için sabit bir komut görüntüler ve karıştırma düğmesini içermez.

### Ana Ekran Hızlı Eylemlerini nasıl yapılandırabilirim?

**4** adede kadar hızlı eylemi görmek için iLinux uygulama simgesine uzun basın. **Ayarlar → Ana Ekran Kısayolları**'nda hangi eylemlerin görüneceğini seçin. Yedi seçenek mevcuttur: **Arama**, **Günlük Test**, **Favoriler**, **Yanlış Cevap Defteri**, **Kategoriler**, **Geri Bildirim Gönder** ve **Uygulamaya Puan Ver**. Aynı ekrandan yeniden sıralayabilir ve varsayılanlara sıfırlayabilirsiniz.

### iLinux'u Kısayollar uygulamasıyla nasıl kullanırım?

iLinux supports the `ilinux://` URL scheme. Use an **Open URLs** action in the Shortcuts app. Examples:

- `ilinux://command?name=grep` — Linux komutu `grep`i açar (`cmd=` da çalışır)
- `ilinux://command?cmd=dir&platform=cmd` — CMD komutu `dir`i açar
- `ilinux://command?cmd=Get-ChildItem&platform=powershell` — PowerShell komutunu açar
- `ilinux://quiz` — opens the Daily Quiz tab
- `ilinux://favorites` — Favoriler listenizi açar
- `ilinux://wrong` veya `ilinux://mistakes` — Yanlış Yanıtlar Kitabı'nı açar

**Platform parameter:** `platform=linux` (default), `cmd` (aliases: `batch`, `bat`), or `powershell` (aliases: `ps`, `pwsh`). Omit for Linux commands.

Not: **Arama** ve **Kategoriler** Ana Ekrandaki hızlı işlemler olarak kullanılabilir ancak evrensel derin bağlantı ana bilgisayarları olarak kayıtlı değildir. [URL Şeması Referansı](../url-scheme)'nin tamamına bakın.

### Bir komutu nasıl paylaşabilirim?

Herhangi bir komut ayrıntısı sayfasında, araç çubuğunda **Paylaş**'a dokunun. Komutu bir **Markdown dosyası** olarak dışa aktarabilir veya sistem Paylaşım Sayfası aracılığıyla göndermek üzere **stillendirilmiş bir PNG paylaşım kartı** (App Store QR koduyla) oluşturabilirsiniz. Görüntülerin Fotoğraflar'a kaydedilmesi, fotoğraf kitaplığına erişim gerektirebilir.

### Tema rengini nasıl değiştiririm?

**Ayarlar → Tema**'ya gidin. 15 yerleşik renk ön ayarı arasında ilerleyin veya sistemin renk seçicisini kullanarak herhangi bir rengi seçmek için **Özel Renk** satırına dokunun. Vurgu rengi, degradeler ve widget aynasının tümü anında güncellenir.

### Uygulama simgesini değiştirebilir miyim?

Evet. **6 simge** (varsayılan artı 5 alternatif) arasından seçim yapmak için **Ayarlar → Uygulama Simgesi**'ne gidin. Ayar, uygulamayı yeniden başlatmaya gerek kalmadan anında uygulanır.

### Widget rengi temamla eşleşmiyor. Bunu nasıl düzeltebilirim?

Widget'lar, ana uygulama ile widget uzantısı arasında paylaşılan bir Uygulama Grubu aracılığıyla tema renklerini senkronize eder. Widget güncelliğini kaybetmiş görünüyorsa:

1. iLinux'u bir kez açın; bu, Uygulama Grubu verilerinin yenilenmesini zorlar.
2. Widget hâlâ güncellenmiyorsa, zaman çizelgesinin yeniden yüklenmesini tetiklemek için widget'a uzun basın ve **Widget'ı Düzenle**'ye dokunun (veya kaldırıp yeniden ekleyin).

**iLinux Widget** uzantısının ve ana uygulamanın güncel (aynı sürüm) olduğundan emin olun.

### iLinux iPad'i destekliyor mu?

Evet. iLinux, uyarlanabilir düzenlerle iPad'de yerel olarak çalışır. Izgara modu **8 sütuna** kadar destekler. Widget'lar, alternatif simgeler, Ana Ekran kısayolları ve dokunsal özellikler iPad'de tam olarak desteklenir.

### Mac'te dili nasıl değiştiririm?

Uygulama içi **dil seçici**, **iPhone ve iPad**'de **Ayarlar → Dil** bölümünde bulunur. **Mac**'te dil tercihi genellikle başka bir cihazdan **iCloud senkronizasyonu** yoluyla gelir veya ilk başlatmada kayıtlı tercihinizi/sistem yerel ayarınızı takip eder. Dili cihazlar arasında uyumlu tutmak için iCloud senkronizasyonunu etkinleştirin.

### Hala yardıma mı ihtiyacınız var?

Bize [AppleOSer@gmail.com](mailto:AppleOSer@gmail.com) adresinden ulaşın veya uygulama içi **Ayarlar → Geri Bildirim Gönder** seçeneğini kullanın. Genellikle 48 saat içinde yanıt veririz.
