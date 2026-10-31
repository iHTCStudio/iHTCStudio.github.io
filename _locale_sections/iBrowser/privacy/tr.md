**Son güncelleme:** 6 Eylül 2026 

iHTC Studio ("biz", "bize" veya "bizim") **iBrowser**'ı oluşturdu ("全屏浏览器" / "全螢幕瀏覽器", Paket Kimliği `full.screen.browser` olarak da bilinir). Bu Gizlilik Politikası, uygulamayı kullandığınızda hangi verilerin işlendiğini (ve işlenmediğini) açıklar. **Apple Uygulama İncelemesi** ve kullanıcılar, genel gizlilik URL'si olarak bu sayfaya güvenebilirler. App Store Connect için bu [Gizlilik Politikası](../privacy) sayfasını açın ve tarayıcının adres çubuğundan adresi kopyalayın. 

## Özet (Apple Gizlilik Beslenme Etiketi uyumu) 

| Konu | Uygulamamız | 
|----------|----------------| 
| Hesap | **Gerekli değil** — iHTC Studio'ya kaydolmak veya oturum açmak gerekmez | 
| iHTC Studio tarafından veri toplama | **Veri Toplanmadı** — yer işaretlerinizi veya ayarlarınızı alan bir arka uç **işletmiyoruz** | 
| Reklam | **Yok** — reklam yok, reklam SDK'sı yok, reklamlar için Uygulama İzleme Şeffaflığı istemi yok | 
| İçeriğe göz atılıyor | Açtığınız sayfalar **doğrudan WebKit** tarafından bu sitelerden yüklenir; bir tarama proxy'si kullanmıyoruz | 
| İsteğe bağlı Apple senkronizasyonu | **iCloud Anahtar-Değer Depolaması** — varsayılan olarak kapalıdır; yalnızca Ayarlar | 

## Veri Toplama

- **Hesap yok** — Uygulamayı bizde bir hesap oluşturmadan kullanabilirsiniz. 
- **Reklam veya analiz SDK'sı yok** — Uygulama, iHTC Studio'ya reklam veya telefonla ev analizi göstermez. 
- **Yer işaretleriniz için iHTC Studio arka ucu yok** — Tercihler cihazınızda kalır (ve isteğe bağlı olarak **Apple iCloud'unuzda** kalır). Yer imi listenizi alan bir sunucuyu barındırmıyoruz. 

### Web'de gezinme 

Bir web sitesine gittiğinizde veya bir arama motorunu kullandığınızda: 

- Cihazınız herhangi bir tarayıcıda olduğu gibi ağ üzerinden **o siteyle** (veya arama sağlayıcısıyla) iletişim kurar. 
- Bu üçüncü taraflar standart istek meta verilerini (IP adresi, kullanıcı aracısı, ayarladıkları çerezler, talep ettiğiniz sayfa içeriği) görebilir. Gizlilik politikaları geçerlidir. 
- Yerleşik veya özel bir **arama motoru** seçildiğinde yalnızca cihazda bir arama URL'si öneki ayarlanır. 

### Widget'lar, Kısayollar ve derin bağlantılar 

Ana Ekran / Kilit Ekranı widget'ları, Siri, Kısayollar, Ana Ekran hızlı eylemleri ve `ibrowser://` bağlantıları **cihazınızda** hedefleri açar. Tarama geçmişinizi iHTC Studio'ya göndermezler. 

## Cihazınızda Saklanan Veriler

| Veri | Nerede | Amaç | 
|------|-------|-------------| 
| Ana sayfa URL'si | UserDefaults (+ Uygulama Grubu anlık görüntüsü) | Başlangıç ​​sayfası; widget ekranı | 
| Arama motoru öneki | Kullanıcı Varsayılanları | Adres çubuğu araması | 
| Yer İmleri | UserDefaults (JSON) (+ Uygulama Grubu anlık görüntüsü) | Yerel favoriler; yer imi widget'ları | 
| Çocuk kilidi / kromu zorla gizleme | Kullanıcı Varsayılanları (+ Uygulama Grubu) | Sürükleyici ve çocuk / kiosk modları | 
| Şamandıra topu açma/kapama ve menü sırası | Kullanıcı Varsayılanları | Kısayol olanağı | 
| Yüzen top **konumu** | Kullanıcı Varsayılanları (yalnızca cihaz) | Topu bıraktığınız yer — iCloud ile **senkronize edilmedi** | 
| Başarıyla yüklenen son sayfa | Kullanıcı Varsayılanları (+ Uygulama Grubu) | “Sonuncuya devam et” — **yalnızca cihaz**, iCloud değil | 
| Ayarlar şifresi | **Anahtarlık** (`WhenUnlockedThisDeviceOnly`) | İsteğe Bağlı Ayarlar kilidi — UserDefaults, Uygulama Grubu veya iCloud'da **değil** | 
| Tarayıcı kenar boşlukları | Kullanıcı Varsayılanları | İçerik ekleri | 
| Görünüm / dil | Kullanıcı Varsayılanları (yalnızca cihaz) | Tema ve kullanıcı arayüzü dili — iCloud **değil** | 
| Ana Ekran hızlı işlem sırası | Kullanıcı Varsayılanları (yalnızca cihaz) | Menüye uzun basın — **değil** iCloud | 
| İlk çalıştırma kılavuzu ve şartlar bayrakları | Kullanıcı Varsayılanları (yalnızca cihaz) | İlk Katılım | 
| Widget anlık görüntüleri | Uygulama Grubu `group.full.screen.browser` | Widget uzantısı için salt okunur ekran |

Uygulamanın kaldırılması, uygulamanın korumalı alanını ve Uygulama Grubu verilerini kaldırır (iOS davranışına bağlıdır). İsteğe bağlı iCloud kopyaları, siz bunları temizleyene veya senkronizasyonu başka bir yerde kapatana kadar **iCloud'unuzda** kalır. 

## İsteğe Bağlı iCloud Senkronizasyonu 

Ayarlar'da **iCloud Senkronizasyonu**'nu etkinleştirirseniz (varsayılan **kapalı**), seçilen tercihler, **Apple Kimliğinize** bağlı olan Apple'ın **`NSUbiquitousKeyValueStore`_** aracılığıyla yansıtılır: 

**Senkronize edilebilecekler:** yer işaretleri, ana sayfa, arama motoru, kenar boşlukları, adres çubuğu/araç çubuğu ekran kilitleri, kayan top açma/kapama, kayan top menü sırası. 

**Senkronize edilmiyor:** Ayarlar şifresi, son sayfa (“sonuncuya devam et”), kayan top konumu, görünüm, dil, Ana Ekran hızlı işlem sırası, kılavuz / terimler bayrakları. 

Senkronizasyon trafiği iHTC Studio'ya değil **Apple iCloud**'a gider. Senkronizasyonu devre dışı bırakabilir veya Ayarlar'da **Şimdi Senkronize Et**'e dokunabilirsiniz. iCloud içeriklerinizi okuyamıyoruz. 

## İzinler 

Web sayfaları, siteye bağlı olarak WebKit aracılığıyla cihaz özellikleri (örneğin kamera, mikrofon veya konum) talep edebilir. Sistem istemleri yalnızca bir sayfa sorduğunda görünür. Uygulama ayrıca web içeriğinin ihtiyaç duyabileceği yetenek dizelerini de bildirir; bu izinleri ayrı bir yerel sosyal veya reklam özelliği için kullanmayız.

| Alan | Notlar |
|------|--------|
| Ağ | Web sitelerini yüklemek ve arama yapmak için gereklidir |
| Hareket (sallama) | **iPhone** üzerinde float ball / chrome'u geri almak için kullanılır — işlem yerel olarak gerçekleşir; **iPad** bunun yerine üst yakına dokunma kullanır |
| iCloud | Sadece senkronizasyonu etkinleştirirseniz |
| Mail / Paylaşım Menüsü | Başlattığınız isteğe bağlı geri bildirim veya paylaşım eylemleri |
| StoreKit (isteğe bağlı ipucu) | Apple tarafından işlenen tüketilebilir ipucu; özelliklerin kilidini açmaz |

## Çocukların Gizliliği

Çocuk kilidi bir **yerel kullanıcı arayüzü kısıtlamasıdır** (adres çubuğunu gizler / isteğe bağlı Ayarlar şifresi). Açıkken, widget'lar, Kestirmeler ve ana sayfa olmayan yer imleri yerine **ana sayfa** açılır. Bu, bizimle bir çocuk hesabı oluşturmaz. Pazarlama amacıyla bilinçli olarak çocuklardan kişisel bilgi talep etmiyoruz. Ebeveynler açılan siteleri denetlemelidir.

## Yapmadıklarımız

- Bir iHTC Studio hesabına **gerek duymayız**. 
- Uygulama içi reklamları veya geçiş reklamı promosyon açılır pencerelerini **göstermiyoruz** (gerekli ilk çalıştırma koşulları dışında). 
- Bu uygulama için kendi bulut senkronizasyon sunucularımızı **işletmiyoruz** (isteğe bağlı senkronizasyon yalnızca **sizin** Apple iCloud'unuzu kullanır). 
- Verilerinizi **satmıyoruz**. 
- Ayarlar şifresini düz UserDefaults'ta **depolamayız** (cihazda Anahtar Zinciri kullanır). 

## Üçüncü Taraflar 

| Parti | Rol | 
|----------|------| 
| **Elma** | App Store dağıtımı; isteğe bağlı iCloud KVS; widget'lar / Siri / Kısayollar; Posta, Paylaşım Sayfası, Safari Görünüm Denetleyicisi; isteğe bağlı StoreKit ipucu | 
| **Açtığınız web siteleri ve arama motorları** | Ziyaret ettiğiniz sayfalar için normal tarayıcı trafiği alın | 

## Saklama ve Silme 

Yerel tercihler ve yer işaretleri, siz onları değiştirene, temizleyene ya da uygulamayı kaldırana kadar kalır. İsteğe bağlı iCloud verileri, siz senkronizasyonu devre dışı bırakana ve/veya Apple'ın araçları aracılığıyla temizleyene kadar Apple'ın politikaları kapsamında kalır. Sunucularımızda kişisel veri toplamadığımız için e-postanıza yanıt vermenin ötesinde silebileceğimiz bir hesap veri kümesi yoktur. 

## Bu Politikadaki Değişiklikler

Bu sayfayı zaman zaman güncelleyebiliriz. Yukarıdaki “Son güncelleme” tarihi, yaptığımız değişikliklerle birlikte değişecektir. Değişikliklerden sonra devam eden kullanım, güncellenmiş politikayı kabul ettiğiniz anlamına gelir.

## Bizimle İletişime Geçin

- **E-posta:** [AppleOSer@gmail.com](mailto:AppleOSer@gmail.com)

Uygulama Mağazası Bağlantısı için genel bağlantıya ihtiyacınız varsa, bu [Gizlilik Politikası](../privacy) sayfasını tarayıcıda açın ve adres çubuğundaki URL’yi kopyalayın.
