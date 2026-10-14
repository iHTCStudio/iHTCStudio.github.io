### Bölge değiştirme nasıl çalışır?

iStore, seçtiğiniz bölge için Apple'ın **resmi App Store yönlendirme bağlantısını** açar. Ardından App Store, değişikliği Apple'ın kendi ekranında onaylamanızı ister. iStore Apple Kimliğinizi, parolanızı veya ödeme ayrıntılarınızı asla görmez.

### Oturum açmam gerekiyor mu?

Hayır. iStore **hesap ve giriş gerektirmez**. Mevcut Apple Kimliğinizle yalnızca bir değiştirmeyi onayladığınızda Apple'ın kendi App Store ekranında etkileşime girersiniz.

### Bölge değiştirmek oturumumu kapatır veya uygulamalarımı kaybettirir mi?

Hayır. Mağaza bölgesini değiştirmek yalnızca hangi bölgenin App Store'unda gezindiğinizi ve alışveriş yaptığınızı değiştirir. Yüklü uygulamalarınız yüklü kalır. Apple, yeni bir bölgede satın alma yapabilmeniz için fatura bölgenizin ve ödeme yönteminizin eşleşmesini isteyebilir.

### iStore, Apple ile bağlantılı mı?

Hayır. iStore, iHTC Studio katkıda bulunanları tarafından geliştirilmiş bağımsız bir araçtır ve **Apple Inc. ile bağlantılı değildir.** Bölge değiştirmek için yalnızca Apple'ın resmi yönlendirme bağlantısını kullanır.

### Kaç bölge destekleniyor?

7 kıtada **175 bölge**; her birinin bayrağı ve yerelleştirilmiş adı (İngilizce / Basitleştirilmiş / Geleneksel Çince) vardır.

### Uygulama Kullanılabilirliği kontrolü nedir?

Bir **App Store bağlantısı veya sayısal Uygulama Kimliği** yapıştırın; iStore (Apple'ın herkese açık iTunes Lookup API'si aracılığıyla) **uygulamanın hangi bölgelerde bulunduğunu** kontrol eder. Kontrolü **Popüler**, **Favoriler** veya **Tüm** bölgelerle sınırlayın, ardından tek dokunuşla kullanılabilir herhangi bir bölgeye geçin. Hem uygulamada hem de **Paylaşım Uzantısı**'ndan çalışır.

### Başka bir uygulamadan kullanılabilirliği nasıl kontrol ederim?

Herhangi bir App Store bağlantısında (Safari, Mesajlar, App Store vb.) **Paylaş** sayfasını kullanın ve **iStore**'u seçin. Paylaşım Uzantısı popüler bölgeleri kontrol eder ve sonucu geçiş yapmak için uygulamada açmanızı sağlar.

### Favoriler ile Sabitlenenler arasındaki fark nedir?

**Favoriler**, yıldızladığınız bölgelerdir. **Sabitlenmiş** bölgeler ise her yerde (mağaza, favoriler ve widget'lar) en üstte tutmak istediğiniz bir alt kümedir. Bir bölgeyi favorilerden çıkarmak, onu sabitlenenlerden de kaldırır.

### Harita Seçici nedir?

Her bölge için bir iğne bulunan **tam ekran harita**. Popüler, Favoriler veya Tümü ile sınırlayın, ardından geçiş yapmak için bir iğneye dokunun. Mağazaları konuma göre görsel olarak keşfetmenin bir yoludur.

### Hangi widget'lar var?

- **Hızlı Bölgeler** ve **Son Kullanılanlar** widget'ları (Ana ve Kilit Ekranı)
- Kendi bölgelerinizle yapılandırdığınız **Özel** widget (iOS 17+)
- **Etkileşimli widget'lar** (iOS 17+) — doğrudan geçiş yapmak için bir bölge kutucuğuna dokunun

### Denetim Merkezi kontrolü nedir?

**iOS 18+** sürümünde, en son hedef bölgenize tek dokunuşla yeniden geçmek için Denetim Merkezi'ne **Sonuncuya Geç** kontrolünü ekleyin.

### Siri veya Kısayollar ile geçiş yapabilir miyim?

Evet. iStore, **bir bölgeye geçmek**, **son bölgeye geçmek**, **bir favoriye geçmek**, **mağazayı açmak** veya **kullanılabilirliği kontrol etmek** için Siri ve Kısayollar eylemleri sunar. Bkz. [Kısayol Bağlantıları](../url-scheme).

### Spotlight araması çalışıyor mu?

Evet. 175 bölgenin tamamı **Spotlight**'ta dizinlenmiştir — Ana Ekran'dan bir bölge arayın ve sonuca dokunarak doğrudan iStore'da geçiş yapın.

### iCloud Senkronizasyonu neleri kapsar?

İsteğe bağlı iCloud senkronizasyonu şunları cihazlarınız arasında eşit tutar: **favoriler**, **sabitlenmiş bölgeler**, **hızlı bölgeler**, **değiştirme geçmişi**, **son değiştirilen bölge** ve görünüm / düzen / favoriler tercihleri. Veriler iHTC Studio sunucuları üzerinden değil, **özel iCloud'unuz** üzerinden senkronize edilir. Senkronizasyon varsayılan olarak açıktır ve Ayarlar'dan kapatılabilir.

### Değiştirmeden önceki onayı kapatabilir miyim?

Evet. Yanlış dokunuşları önlemek için **Değiştirmeden önce onayla** varsayılan olarak açıktır; Ayarlar'dan devre dışı bırakabilirsiniz.

### iStore hangi dilleri destekler?

**English, 简体中文 ve 繁體中文.** Bölge adlarının nasıl görüntüleneceğini de seçebilirsiniz (bölge adı görüntüleme modu).

### Hangi cihazlar desteklenir?

- **iPhone / iPad** — iOS 16.2+ (ana uygulama)
- **Yapılandırılabilir / etkileşimli widget'lar** — iOS 17.0+
- **Denetim Merkezi kontrolü ve iPhone Arama sekmesi** — iOS 18.0+
- **Kısayollar ve Siri** — iOS 16.2+

### iStore çevrimdışı çalışır mı?

Göz atma ve geçiş bağlantıları çevrimdışı çalışır, ancak **Uygulama Kullanılabilirliği** kontrolü ağ bağlantısı gerektirir (Apple'ın herkese açık Lookup API'sini sorgular). Favorileriniz, sabitlenmiş bölgeleriniz ve geçmişiniz cihazınıza kaydedilir.

### iStore'u nasıl edinirim?

[App Store](https://apps.apple.com/app/id6786123132)'dan indirin.

### Hâlâ yardıma mı ihtiyacınız var?

[AppleOSer@gmail.com](mailto:AppleOSer@gmail.com) ile iletişime geçin. Genellikle 48 saat içinde yanıt veririz.
