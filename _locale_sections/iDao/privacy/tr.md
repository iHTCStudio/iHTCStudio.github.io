**Son güncelleme:** 3 Ağustos 2026

iHTC Studio ("biz", "bize" veya "bizim") **iDao**yu (diğer adıyla "爱道德经" / "愛道德經", Bundle ID `com.iHTCboy.iDao`) geliştirdi. Bu Gizlilik Politikası, uygulamayı kullandığınızda hangi verilerin işlenip işlenmediğini açıklar. **Apple App Review** ve kullanıcılar, uygulamanın halka açık gizlilik politikası olarak **bu sayfaya** güvenebilir. App Store Connect için, bu Gizlilik Politikasını tarayıcınızda açın ve adres çubuğundan adresi kopyalayın (halka açık site alan adı zamanla değişebilir).

## Özet (Apple Gizlilik Beslenme Etiketi uyumu)

| Konu | Uygulamamız |
|-------|----------------|
| Hesap | **Gerekmiyor** — kayıt, e-posta ile giriş veya telefon numarası yok |
| iHTC Studio tarafından veri toplama | **Veri Toplanmıyor** — kişisel verilerinizi alan bir sunucu işletmiyoruz |
| Ağ | Kütüphane, okuma, ezber, Çalışma Salonu, Tao’yu Ara, widget’lar ve günlük bildirimler kurulum sonrası **çevrimdışı** çalışır |
| Analitik / reklam / takip | **Yok** — üçüncü taraf analitik, reklam veya takip SDK’ları yok; Uygulama Takip Şeffaflığı kullanılmıyor |
| İsteğe Bağlı Apple servisleri | **iCloud** (özel KVS’niz, çift yönlü birleştirme), **Fotoğraf Kitaplığı (Sadece Ekle)** Dao kartları için, **StoreKit** isteğe bağlı bahşiş için, **yerel bildirimler**, isteğe bağlı **Canlı Aktiviteler** |

## Veri Toplama

Kişisel bilgileri reklam veya analitik için **toplamıyoruz, satmıyoruz veya paylaşmıyoruz**.

- **Hesap yok** — Bizimle bir hesap oluşturmadan tüm temel özellikleri kullanabilirsiniz.
- **Analitik veya reklam yok** — Uygulama ikili dosyası, bize veri gönderen üçüncü taraf analitik, reklam veya hata raporlama SDK'larını içermez.
- **İçerik yükleme yok** — Okuma geçmişiniz, favorileriniz, listeleriniz, notlarınız, ustalık seviyeleriniz, art arda kullanım günleriniz ve tercihlerinizi cihazınızda (ve isteğe bağlı olarak **iCloud'unuzda**) kalır. Bunlar iHTC Studio sunucularına asla yüklenmez çünkü **bu uygulama için böyle sunucular çalıştırmıyoruz**.

## Uygulama Nasıl Çalışır

- **Paketlenmiş kitaplık** — Bölüm JSON, yerel dil, pinyin, yorumlar, İngilizce basımlar, ünlü satırlar ve dizinler uygulama/widget paketinin içinde gönderilir. Tarama ve çalışma ağ isteği gerektirmez. 
- **Cihaz içi konuşma** — Okuma, Apple'ın **AVSpeechSynthesizer** (TTS) sistemini kullanır. Bölüm metnini iHTC Studio'ya göndermiyoruz. 
- **Widget'lar ve Uygulama Grubu** — Widget'lar ve uygulama, cihazınızdaki `group.com.iHTCboy.iDao` Uygulama Grubu aracılığıyla tercihleri ​​ve hafif durumu paylaşır. 
- **Günlük bildirimler** — Kullanıcı Bildirimleriyle yerel olarak planlanır. Bir bildirime dokunduğunuzda cihazdaki bölüm kimliğine giden derin bir bağlantı açılır; sunucu çıkışı yok. 
- **Dao kartları** — Görüntüler cihazda oluşturulur. Kaydetme, **Yalnızca Fotoğraf Kitaplığı eklentisini** yalnızca kaydet'e dokunduğunuzda kullanır. Sistem Paylaşım Sayfası, görüntüyü **seçtiğiniz** bir uygulamaya gönderebilir; o hedefin gizlilik politikası geçerli olur. 
- **İsteğe bağlı ipucu** — "İpucu Geliştirici", Apple tarafından gerçekleştirilen bir **StoreKit** sarf malzemesidir. Ödeme kartı bilgilerinizi almıyoruz. 
- **Siri / Kısayollar / Kontrol Merkezi** — İsteğe bağlı sistem entegrasyonları cihazdaki derin bağlantıları açar; kütüphanenizi bize göndermiyorlar. 
- **İsteğe Bağlı Spot Işığı** — Varsayılan olarak kapalıdır. Dizin oluşturmayı etkinleştirirseniz içerik, yerel arama için cihazdaki sistem tarafından dizine eklenir; bir arama arka ucu kullanmıyoruz.

## Cihazınızda Saklanan Veriler 

| Veri | Nerede | Amaç | 
|------|-------|-------------| 
| Bölüm veritabanı (pinyin / not baskıları dahil) | Uygulama / Widget paketi | Çevrimdışı okuma ve çalışma | 
| Favoriler ve listeler (道单) | Uygulama Grubu Kullanıcı Varsayılanları | Yıldızlı bölümler ve kullanıcı listeleri | 
| Okuma geçmişi / son okuma | Uygulama Grubu Kullanıcı Varsayılanları | Okumaya devam et, geçmiş kullanıcı arayüzü | 
| Çalışma ilerlemesi ve ustalık | Uygulama Grubu Kullanıcı Varsayılanları | Çalışma Salonu durumu, sınav / Tao ilerlemesini arayın | 
| Notlar | Uygulama Grubu Kullanıcı Varsayılanları | Yazdığınız bölüm notları | 
| Antrenman serisi / check-in | Uygulama Grubu Kullanıcı Varsayılanları | Günlük alışkanlık | 
| Görünüm ve okuma tercihleri ​​| Uygulama Grubu Kullanıcı Varsayılanları | Tema, aksan, dil, düzen, TTS, sekmeler, widget'lar | 
| Günlük Bölüm önbelleği ve bildirim tercihleri ​​| Uygulama Grubu Kullanıcı Varsayılanları | Bugünün kimliği, program zamanı, bağlamsal geçiş | 
| Paylaşımlı kart tercihleri ​​| Uygulama Grubu Kullanıcı Varsayılanları | Son stil/oran seçenekleri | 
| İlk katılım ve TipKit durumu | Standart Kullanıcı Varsayılanları (cihaz) | Hoş geldiniz kılavuzu / keşif ipuçları | 
| Ana Ekran hızlı eylemler | Sistem + yerel tercihler | Yapılandırdığınız kısayollar | 
| Widget / Canlı Etkinlik anlık görüntüleri | Uygulama Grubu / ActivityKit | Daha önce açmış olduğunuz metni görüntüleyin |

Uygulamayı kaldırmak, uygulamayla ilişkili sandbox ve Uygulama Grubu verilerini kaldırır (iOS/macOS davranışına tabidir). Opsiyonel iCloud kopyaları, siz temizleyene veya eşitlemeyi kapatıp başka yerde silene kadar **iCloud’unuzda** kalır. 

## iCloud Eşitleme (Opsiyonel)

Ayarlar’da **iCloud Eşitlemeyi** etkinleştirirseniz, uygulama seçilen kullanıcı verilerini **Apple Kimliğiniz** ile ilişkili Apple’ın **`NSUbiquitousKeyValueStore`** üzerinden yansıtır, **çift yönlü birleştirme** kullanarak (favoriler, listeler, geçmiş, ustalık, notlar, zincirler) bulut ve cihaz güncellemelerinin körü körüne üzerine yazılmak yerine birleştirilmesini sağlar.

Eşitleme trafiği **Apple iCloud** üzerinden gider, iHTC Studio’ya gitmez. Ayarlardan eşitlemeyi devre dışı bırakabilirsiniz. iCloud içeriklerinizi okuyamayız.

## İzinler

iDao, yalnızca bir özellik izin gerektirdiğinde izin ister:

| İzin | Ne zaman | Neden | 
|---------------|----------|-----| 
| Bildirimler | Günlük Bölüm hatırlatıcılarını etkinleştirirsiniz | Hatırlatma bildirimlerinin yerel planlanması | 
| Fotoğraf Kitaplığı (Yalnızca Ekle) | Bir Dao kartını kaydedersiniz | İşlenen görüntüyü yazın; tam kütüphane okuma erişimine ihtiyacımız yok | 
| iCloud | Senkronizasyonu etkinleştirirsiniz | Favorileri / listeleri / geçmişi / ustalığı / notları / serileri senkronize et | 
| Canlı Etkinlikler (iOS) | Canlı Okuma Etkinliğini etkinleştirirsiniz | Okuduğunuz bölümü Kilit Ekranı / Dinamik Ada'da gösterin | 
| Arka planda ses (yetenek) | Arka planda okumayı etkinleştirirsiniz | Uygulama ön planda olmadığında TTS'ye devam edin | 

Kişiler, kesin Konum, Kamera, Mikrofon (sistem TTS oynatmanın ötesinde) veya İzleme **talebi etmeyiz**. 

## Ne Yapmıyoruz 

- Kişisel verileri **satmıyoruz**. 
- Reklam profilleri **oluşturmuyoruz**. 
- Bir hesaba veya sosyal girişe **gerek duymayız**. 
- Veri toplama amacıyla üçüncü taraf reklamları, analizleri veya sosyal SDK'ları **yerleştirmeyiz**. 
- Bir kartı kaydetmeyi seçtiğinizde **yalnızca eklenti** dışında Fotoğraf Kitaplığınıza **erişmeyiz**. 
- StoreKit ödeme kartı numaralarını **almıyoruz** (ödemeleri Apple işler). 

## Çocukların Gizliliği

iDao, 13 yaşın altındaki çocuklar (veya bölgenizdeki eşdeğer yaş) dahil olmak üzere hiçbir kişisel veriyi bilerek toplamaz. Veri toplama altyapısı işletmediğimiz için bizimle kayıtlı bir çocuk profili bulunmamaktadır. Aileler, okuma ve çalışma özelliklerini kendi cihazlarında çevrimdışı olarak kullanabilirler.

## Üçüncü Taraflar

- **Apple** — App Store dağıtımı, isteğe bağlı StoreKit satın alımları, isteğe bağlı iCloud KVS, sistem TTS, sizin seçtiğiniz Paylaşım Sayfası hedefleri ve işletim sistemi düzeyinde bildirim / Canlı Aktivite / Siri / Kestirmeler teslimi.
- Veri toplama için başka hiçbir üçüncü taraf SDK’sı reklam, analiz veya sosyal giriş amacıyla dahil edilmemiştir.

## Uluslararası Kullanıcılar

Uygulama cihazınızda çevrimdışı çalışacak şekilde tasarlanmıştır. İsteğe bağlı Apple hizmetleri Apple’ın şartlarına ve bölgesel kullanım uygunluğuna tabidir.

## Veri Saklama ve Silme

- **Cihazda** — Yerel tercih ve ilerleme, uygulama içinden (varsa) temizleyene, cihazı sıfırlayana veya uygulamayı kaldırana kadar kalır.
- **iCloud (isteğe bağlı)** — Senkronize ettiğiniz veriler, Apple’ın politikaları uyarınca, senkronizasyonu devre dışı bırakana ve/veya Apple’ın araçlarıyla temizleyene kadar **iCloud** hesabınızda kalır.
- **iHTC Studio** — Sunucularımızda kişisel veri toplamadığımız için, e-posta sorularınıza cevap vermenin ötesinde silinebilecek bir hesap veri setimiz yoktur.

## Bu Politika ile İlgili Değişiklikler

Bu Gizlilik Politikasını zaman zaman güncelleyebiliriz. En üstteki "Son güncelleme" tarihi değişecek ve revize edilmiş politika bu Gizlilik Politikası sayfasında yayınlanacaktır.

## İletişim

Bu Gizlilik Politikası veya gizlilik uygulamaları hakkında sorularınız varsa:

- **E-posta:** [AppleOSer@gmail.com](mailto:AppleOSer@gmail.com)

Genellikle 48 saat içinde yanıt veririz.
