### iWool iPad'de çalışıyor mu?

Evet. iWool **iPhone ve iPad** (iOS 15.0+) için evrensel bir uygulamadır. Düzen, iPad ekran boyutlarına uyum sağlar; Araç takımları ve Canlı Etkinlikler, iPhone'dakiyle aynı kurallara tabidir.

### iWool bir hesap veya internet bağlantısı gerektiriyor mu?

Hayır. iWool tamamen çevrimdışı çalışır. Tüm veriler SQLite kullanılarak cihazınızda yerel olarak depolanır. Herhangi bir özelliği kullanmak için hesap, kayıt veya ağ bağlantısı gerekmez (uygulama içinde http/https bağlantılarının açılması hariç).

### Verilerim nerede saklanıyor? Güvenli mi?

Etkinlikler, hatırlatıcılar, kazanç kayıtları, yinelenme durumları gibi tüm veriler cihazınızdaki yerel bir SQLite veritabanında saklanır. Hiçbir sunucuya hiçbir şey yüklenmez. Uygulamayı kaldırırsanız verileriniz silinir. **Ayarlar → Veri → Tam Yedeği Dışa Aktar** seçeneğini kullanarak düzenli olarak yedekleme yapın.

### Verilerimi nasıl yedekleyebilirim ve geri yükleyebilirim?

Bir CSV dosyası oluşturmak için **Ayarlar → Veri → Tam Yedeği Dışa Aktar** seçeneğine gidin. Dosyalara kaydedin, AirDrop'la Mac'inize gönderin veya e-postayla gönderin.

Geri yüklemek için **Ayarlar → Veri → Yedeği İçe Aktar** seçeneğine gidin ve dosyanızı seçin. Aşağıdakiler arasında seçim yapmanız istenecektir:

- **Tüm verileri değiştir** — her şeyi temizler ve yedeklemeden geri yükler. Cihazları değiştirirken veya yeniden yüklerken bunu kullanın.
- **Yalnızca ekle (var olanı tut)** — cihazınızdaki hiçbir şeyi silmeden yedekleme etkinliklerini yeni kayıtlar olarak ekler. Başka bir cihazdaki verileri birleştirmek için bunu kullanın.

### Tekrarlanan aktiviteler nasıl çalışır?

Bir yinelenme kuralı (günlük, haftalık, aylık, yıllık veya özel bir aralık) belirlediğinizde, iWool bir ana kaydı saklar ve onu sanal olarak her gün bireysel olaylara genişletir. Liste ve takvim, yinelenen bir seri için her zaman bugünün oluşumunu gösterir.

Belirli bir günün oluşumunu tamamlandı olarak işaretlemek için uzun basılan menüyü veya ayrıntı sayfasının altındaki araç çubuğunu kullanın. Bu sadece o güne işaret ediyor; seri devam ediyor.

### Bir hatırlatıcı neden görünmüyor?

iOS, her uygulamayı aynı anda yaklaşık 64 bekleyen yerel bildirimle sınırlandırır. iWool, yinelenmeyen etkinliklere öncelik verir ve yinelenen etkinlikler için 120 güne kadar gelecekte meydana gelecek olayları planlar, ancak yinelenen hatırlatıcılardan oluşan çok büyük koleksiyonlar kırpılabilir.

Tam olarak hangi hatırlatıcıların kayıtlı olduğunu görmek için **Ayarlar → Bildirimler → Planlanmış Yerel Hatırlatıcılar** seçeneğini işaretleyin.

Ayrıca şunları doğrulayın:

- Bildirim izni verildi (iOS Ayarları → iWool → Bildirimler).
- Etkinlik iptal edilmez (iptal edilen etkinliklerin hatırlatıcıları otomatik olarak temizlenir).
- Hatırlatma zamanı gelecektedir.

### "Tahmini kazançlar" ile "kaydedilen kazançlar" arasındaki fark nedir?

- **Tahmini kazançlar** — etkinlik formuna girilir. Etkinlik kartında görüntülenir. İstatistiklerde sayılmaz.
- **Kayıtlı kazançlar** — kazanç formu aracılığıyla etkinlik ayrıntıları sayfasına girilir. Bunlar, tüm İstatistik toplamlarında, trend çizelgelerinde ve platform sıralamalarında sayılan gerçek miktarlardır.

### Tekrarlanan bir aktivitenin belirli bir gününe ait kazançları nasıl kaydederim?

O günün gerçekleşmesine ilişkin etkinlik ayrıntısını açın (o gündeki listedeki veya takvimdeki etkinliğe dokunun). Ayrıntılar sayfasında, kazançlar bölümünde **Kaydet**'e dokunun. Kayıt tarihi varsayılan olarak o günün oluşum tarihine göre ayarlanacaktır.

### Etkinliği etkilemeden tek bir kazanç girişini silebilir miyim?

Evet. Etkinlik ayrıntısını açın, düzenlemek istediğiniz kazanç satırına dokunun ve düzenleme formunda en alta doğru kaydırın. **Bu kazanç kaydını sil**'e dokunun ve onaylayın. Yalnızca bu tek giriş kaldırılır; aktiviteye ve diğer tüm kayıtlara dokunulmaz.

### İstatistik tablosu Japon Yeni (JPY) / Kore Wonu (KRW) için yanlış tutarları gösteriyor.

Bu para birimlerinde varsayılan olarak ondalık basamak yoktur; bu da eski sürümlerde tutarların tam sayı olarak görünmesine neden olmuş olabilir. Mevcut sürümde ondalık basamak sayısını bağımsız olarak yapılandırabilirsiniz:

- Tüm tutar ekranlarında ondalık basamak sayısını ayarlamak için **Ayarlar → Görünüm ve Dil → Ondalık Tutar** seçeneğine gidin (varsayılan: 2).
- Grafik çubuğu etiketlerinin ondalık basamaklarını özel olarak ayarlamak için **Ayarlar → Görünüm ve Dil → Grafik Tutarı Ondalık Sayıları** seçeneğine gidin (varsayılan: 0).

### Dinamik Ada / Canlı Etkinlik özelliğini nasıl kullanırım?

**Etkinlik geri sayımı** (iOS 16.1+, desteklenen iPhone): **Ayarlar → Bildirimler → Canlı Etkinlik** bölümünden etkinleştirin. Teslim süresini ayarlayın (1–480 dakika). Penceredeki etkinlikler otomatik olarak seçilir; Ana Sayfa veya Takvim'e uzun basın → **Dinamik Ada'ya Ekle**.

**Quick Countdown** (iOS 16.2+): a **standalone** island timer **not tied to your activity database**. Open **Settings → Island Reminder**, use a Home Screen Quick Action, or `iwool://island`. Duration **1 second to 8 hours**; optional title, note and accent colour. When it ends, the Live Activity dismisses — nothing is saved unless you create a wool activity separately.

### Hızlı Geri Sayım ve etkinlik Canlı Etkinliği nedir?

|  | Etkinlik geri sayımı | Hızlı Geri Sayım |
|---|-----------------|-----------------|
| Etkinliğe bağlı | Evet | Hayır |
| Uygulamada kalıcı | Evet | Hayır |
| Minimum iOS | 16.1 | 16.2 |
| Nasıl başlanır | Otomatik veya uzun basma etkinliği | Ayarlar / kısayol / `iwool://island` |

### Ana Ekran Hızlı Eylemleri nasıl çalışır?

Long-press the iWool icon (iOS). Choose up to **4** from **9** presets in **Settings → Tools → Home Screen Shortcuts**: Home, Calendar, Statistics, Quick Countdown, New Activity, Scheduled Reminders, Scanner, Rate, Feedback. Default: Home, Calendar, Statistics, Quick Countdown. Each uses an `iwool://` URL.

### How do `iwool://` deep links work?

iWool, widget'lar, Kısayollar ve Hızlı Eylemler tarafından kullanılan sekmeler, eylemler ve etkinlik ayrıntıları için **`iwool://`**'u destekler. Örnekler:

- `iwool://home`, `iwool://calendar`, `iwool://stats`, `iwool://settings`
- `iwool://new`, `iwool://island`, `iwool://scanner`, `iwool://reminders`
- `iwool://event/42`, `iwool://event/42?day=189345600` (yinelenen oluşum)

Bilinmeyen yollar göz ardı edilir (Giriş'e sessiz yönlendirme yapılmaz). [**URL Şeması referansı**](../url-scheme)'ın tamamına bakın.

### Bir etkinliği veya istatistikleri resim olarak nasıl paylaşırım?

Etkinlik ayrıntıları sayfasından veya **İstatistikler** sekmesi araç çubuğundan, markalı bir **PNG resim kartı** (gradyan, QR kodu, Ayarlar'da etkinleştirildiyse isteğe bağlı kazançlar) oluşturmak için **Paylaş**'ı kullanın. Görüntü cihazda oluşturulur; Fotoğraflar'a kaydetme, fotoğraf kitaplığına erişim talebinde bulunabilir.

### iWool kaç tane widget içerir?

**12 widget ailesi** — sekiz Ana Ekran widget'ı (Bugün Aktif, Bugünün Tümü, Bugün Yaklaşan, Tüm Etkinlikler, İstatistiklere Genel Bakış, Kazançlar, Bakış, En Popüler Platformlar) artı dört Kilit Ekranı aksesuar stili (iOS 16+).

### Ana Ekranıma veya Kilit Ekranıma nasıl widget eklerim?

Ayrıntılı adım adım talimatlar uygulamanın içindeki **Ayarlar → Widget'lar → Widget Kılavuzu** bölümünde mevcuttur. Kısaca:

1. Ana Ekranınızın boş bir alanına uzun basın ve **+** düğmesine dokunun.
2. Widget galerisinde **iWool**'u arayın.
3. Bir widget stili ve boyutu seçin, ardından **Widget Ekle**'ye dokunun.

Kilit Ekranı widget'ları için (iOS 16+): Kilit Ekranınıza uzun basın ve **Özelleştir**'e dokunun, ardından Kilit Ekranı widget satırına iWool widget'larını ekleyin.

### Widget neden güncel olmayan verileri gösteriyor?

Uygulamayı açtığınızda veya veriler değiştiğinde widget'lar yenilenir. iOS ayrıca arka planda widget zaman çizelgelerini periyodik olarak (en iyi ihtimalle yaklaşık 15 dakikada bir) yeniler. Widget eskiyse yenilemeyi zorlamak için iWool'u bir kez açın.

### Ekran dilini nasıl değiştiririm?

**Ayarlar → Görünüm ve Dil → Görüntüleme Dili**'ne gidin. Cihazınızın sistem dilinden bağımsız olarak 13 dil arasından seçim yapabilirsiniz:

İngilizce, Basitleştirilmiş Çince, Geleneksel Çince, Japonca, Korece, Tayca, Hintçe, İspanyolca, Fransızca, Almanca, Brezilya Portekizcesi, Rusça, Arapça.

Değişiklik uygulama genelinde anında etkili olur.

### Kazanç tutarlarımı paylaşmadan bir aktiviteyi paylaşabilir miyim?

Evet. Varsayılan olarak bir etkinliğin kopyalanması veya paylaşılması kazanç kayıtlarınızı içermez. Bunları eklemek istiyorsanız **Ayarlar → Görünüm ve Dil**'e gidin ve **Paylaşım sırasında kazançları dahil et** seçeneğini etkinleştirin.

### QR kodunu veya barkodu nasıl tarayabilirim?

**Ayarlar → Araçlar → QR / Barkod Tarayıcı**'ya gidin. Bir resim seçmek için kameranızı bir koda doğrultun veya albüm simgesine dokunun. Sonuçlar, kopyalayabileceğiniz veya Safari'de açabileceğiniz bir listede görünür.

Doğrudan etkinlik formundan da tarayabilirsiniz: Etkinlik URL'si alanını doldururken, kodu taramak ve URL'yi otomatik olarak doldurmak için yanındaki tarama simgesine dokunun.

### "Arşiv" ne anlama geliyor? Silmekle aynı şey mi?

Hayır. Arşivleme, bir etkinliği silmeden ana listeden gizler. Arşivlenen etkinlikler **Ayarlar → Etkinlik Yönetimi → Arşivlenen Etkinlikler**'den görüntülenebilir, geri yüklenebilir veya silinebilir.

Arşiv seçeneğini görmek için tamamlanmış, süresi dolmuş veya iptal edilmiş bir etkinliğe uzun basın. Tamamlanan, süresi dolan ve iptal edilen yinelenmeyen etkinliklerin tümünü aynı anda arşivlemek için **Ayarlar → Etkinlik Yönetimi → Tamamlananların Tümünü Arşivle** seçeneğini kullanın.

### Hala yardıma mı ihtiyacınız var?

Bize [AppleOSer@gmail.com](mailto:AppleOSer@gmail.com) adresinden ulaşın veya uygulama içi **Ayarlar → Geri Bildirim Gönder** seçeneğini kullanın. Genellikle 48 saat içinde yanıt veririz.
