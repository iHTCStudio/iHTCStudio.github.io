**Son güncelleme:** 23 Temmuz 2026

iHTC Studio ("biz" veya "bizim"), **iLunYu**'i (aynı zamanda "爱论语" / "愛論語" olarak bilinir, Bundle ID `com.iHTCboy.iLunYu`) geliştirmiştir. Bu Gizlilik Politikası, uygulamayı kullandığınızda hangi verilerin işlendiğini (ve işlenmediğini) açıklar. **Apple App Review** ve kullanıcılar bu sayfayı herkese açık gizlilik URL'si olarak kullanabilir.

## Özet (Apple Gizlilik Besin Etiketi ile uyum)

| Konu | Uygulamamız |
|-------|----------------|
| Hesap | **Gerekmez** — kayıt, e-posta ile giriş veya telefon numarası yok |
| iHTC Studio tarafından veri toplama | **Veri Toplanmaz** — kişisel verilerinizi alan bir arka uç **işletmiyoruz** |
| Ağ | Beyit (lunyu) kütüphanesi, okuma, seslendirme, çalışma, widget'lar ve günlük bildirimler kurulumdan sonra **çevrimdışı** çalışır |
| Analiz / reklam / izleme | **Yok** — üçüncü taraf analiz, reklam veya izleme SDK'sı yok; App Tracking Transparency kullanılmaz |
| İsteğe bağlı Apple hizmetleri | **iCloud** (özel KVS'niz), paylaşım kartları için **Fotoğraf Kitaplığı (Yalnızca Ekleme)**, isteğe bağlı bahşiş için **StoreKit**, **yerel bildirimler**, isteğe bağlı **Canlı Etkinlikler** |

## Veri Toplama

Reklam veya analiz amacıyla kişisel bilgileri **toplamıyor, satmıyor veya paylaşmıyoruz**.

- **Hesap yok** — Bizimle hesap oluşturmadan tüm temel özellikleri kullanabilirsiniz.
- **Analiz veya reklam yok** — Uygulama ikili dosyası, bize bilgi gönderen üçüncü taraf analiz, reklam veya çökme raporlama SDK'ları içermez.
- **Beyit içeriği yüklenmez** — Okuma geçmişiniz, favorileriniz, çalışma ilerlemeniz ve tercihleriniz cihazınızda (ve isteğe bağlı olarak **kendi** iCloud'unuzda) kalır. **Bu uygulama için böyle sunucular işletmediğimizden** iHTC Studio sunucularına asla yüklenmezler.

## Uygulama Nasıl Çalışır

- **Yerleşik kütüphane** — Beyit JSON'u ve dizinler uygulama / widget paketinin içinde gelir. Göz atma ve çalışma için ağ isteği gerekmez.
- **Cihaz üzerinde konuşma** — Seslendirme, Apple'ın cihaz içi / sistem **AVSpeechSynthesizer** (TTS) özelliğini kullanır. Beyit metnini iHTC Studio'ya göndermeyiz.
- **Widget'lar ve App Group** — Widget'lar ve uygulama, cihazınızdaki `group.com.iHTCboy.iLunYu` App Group'u üzerinden tercihleri ve hafif durumu paylaşır.
- **Günlük bildirimler** — User Notifications ile yerel olarak zamanlanır. Bir bildirime dokunmak, cihazdaki bir beyit kimliğine derin bağlantı açar; sunucudan toplu gönderim yoktur.
- **Paylaşım kartları** — Görseller cihazda oluşturulur. Kaydetme, yalnızca kaydet'e dokunduğunuzda **Fotoğraf Kitaplığı yalnızca ekleme** iznini kullanır. Sistem Paylaşım Sayfası görseli **sizin seçtiğiniz** bir uygulamaya gönderebilir; bu durumda o hedefin gizlilik politikası geçerli olur.
- **İsteğe bağlı bahşiş** — "Geliştiriciye Bahşiş", Apple tarafından işlenen tüketilebilir bir **StoreKit** satın alımıdır. Ödeme kartı bilgilerinizi almayız.

## Cihazınızda Saklanan Veriler

| Veri | Nerede | Amaç |
|------|-------|---------|
| Beyit veritabanı | Uygulama / Widget paketi | Çevrimdışı okuma ve çalışma |
| Favoriler ve beyit listeleri | App Group UserDefaults | Yıldızlanan eserler ve kullanıcı listeleri |
| Okuma geçmişi / son okunan | App Group UserDefaults | Okumaya devam etme, geçmiş arayüzü |
| Çalışma ilerlemesi ve ustalık | App Group UserDefaults | 4 seviyeli ustalık, test durumu |
| Seri / yoklama | App Group UserDefaults | Öğrenme serileri |
| Görünüm ve okuma tercihleri | App Group UserDefaults | Tema, vurgu, dil, düzen, TTS, sekmeler, widget'lar |
| Günün beyiti önbelleği ve bildirim tercihleri | App Group UserDefaults | Bugünün kimliği, zamanlama saati, bağlamsal anahtar |
| Paylaşım kartı tercihleri | App Group UserDefaults | Son stil / oran seçimleri |
| Karşılama ve TipKit durumu | Standart UserDefaults (cihaz) | Karşılama rehberi / keşif ipuçları |
| Ana Ekran hızlı eylemleri | Sistem + yerel tercihler | Yapılandırdığınız en fazla 4 kısayol |
| Widget / Canlı Etkinlik anlık görüntüleri | App Group / ActivityKit | Zaten açtığınız görüntülenen metin |

Uygulamayı kaldırmak, uygulamayla ilişkili kum havuzu (sandbox) ve App Group verilerini siler (iOS/macOS davranışına tabidir). İsteğe bağlı iCloud kopyaları, siz temizleyene veya senkronizasyonu kapatıp başka yerden silene kadar **sizin** iCloud'unuzda kalır.

## iCloud Senkronizasyonu (İsteğe Bağlı)

Ayarlar'da **iCloud Senkronizasyonu**'nu etkinleştirirseniz, uygulama seçili kullanıcı verilerini **Apple Kimliğinize** bağlı Apple'ın **`NSUbiquitousKeyValueStore`** hizmeti aracılığıyla yansıtır:

- Favoriler
- Beyit listeleri
- Okuma geçmişi
- Çalışma ilerlemesi / ustalık
- Seri günleri

Senkronizasyon trafiği iHTC Studio'ya değil, **Apple iCloud'a** gider. Senkronizasyonu Ayarlar'dan devre dışı bırakabilirsiniz. iCloud içeriğinizi okuyamayız.

## İzinler

iLunYu, yalnızca bir özellik gerektirdiğinde izin ister:

| İzin | Ne zaman | Neden |
|------------|------|-----|
| Bildirimler | Günün Beyiti hatırlatıcılarını etkinleştirdiğinizde | Hatırlatma bildirimlerinin yerel zamanlanması |
| Fotoğraf Kitaplığı (Yalnızca Ekleme) | Bir paylaşım kartını kaydettiğinizde | Oluşturulan görseli yazmak; kitaplığın tamamına okuma erişimine ihtiyacımız yok |
| iCloud | Senkronizasyonu etkinleştirdiğinizde | Favorileri / listeleri / geçmişi / ilerlemeyi / serileri senkronize etmek |
| Canlı Etkinlikler (iOS) | Okuma Canlı Etkinliği'ni etkinleştirdiğinizde | Okuduğunuz beyiti Kilit Ekranı / Dynamic Island'da göstermek |
| Arka plan sesi (yetenek) | Arka planda seslendirmeyi etkinleştirdiğinizde | Uygulama ön planda değilken TTS'yi sürdürmek |

Kişiler, kesin Konum, Kamera, Mikrofon (sistem TTS oynatımı dışında) veya İzleme için izin **istemiyoruz**.

## Çocukların Gizliliği

iLunYu, 13 yaşın altındaki çocuklar (veya bölgenizdeki eşdeğer yaş) dahil hiç kimseden bilerek kişisel veri toplamaz. Veri toplayan bir arka uç işletmediğimiz için bizde saklanan bir çocuk profili yoktur.

## Üçüncü Taraflar

- **Apple** — App Store dağıtımı, isteğe bağlı StoreKit satın alımları, isteğe bağlı iCloud KVS, sistem TTS, seçtiğiniz Paylaşım Sayfası hedefleri ve işletim sistemi düzeyinde bildirim / Canlı Etkinlik teslimi.
- Veri toplama amacıyla reklam, analiz veya sosyal giriş için **başka hiçbir üçüncü taraf SDK'sı** yoktur.

## Uluslararası Kullanıcılar

Uygulama, cihazınızda çevrimdışı çalışacak şekilde tasarlanmıştır. İsteğe bağlı Apple hizmetleri Apple'ın şartlarına ve bölgesel kullanılabilirliğe tabidir.

## Bu Politikadaki Değişiklikler

Bu Gizlilik Politikası'nı zaman zaman güncelleyebiliriz. En üstteki "Son güncelleme" tarihi değişecek ve revize edilen politika bu Gizlilik Politikası sayfasında yayımlanacaktır.

## Bize Ulaşın

Bu Gizlilik Politikası veya gizlilik uygulamaları hakkında sorularınız varsa:

- **E-posta:** [AppleOSer@gmail.com](mailto:AppleOSer@gmail.com)

Genellikle 48 saat içinde yanıt veririz.
