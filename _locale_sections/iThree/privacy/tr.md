**Son güncelleme:** 31 Temmuz 2026

iHTC Studio (“biz”, “bize” veya “bizim”) **iThree**’yı (diğer adıyla “爱三字经” / “愛三字經”, Paket Kimliği `com.iHTCboy.iThree`) geliştirdi. Bu Gizlilik Politikası, uygulamayı kullandığınızda hangi verilerin işlendiğini (ve hangilerinin işlenmediğini) açıklamaktadır. **Apple App Review** ve kullanıcılar, uygulamanın kamuya açık gizlilik politikası olarak **bu sayfaya** güvenebilir. App Store Connect için, bu Gizlilik Politikasını tarayıcınızda açın ve adres çubuğundaki adresi kopyalayın (kamu sitesi alan adı zaman içinde değişebilir).

## Özet (Apple Gizlilik Beslenme Etiketi uyumu)

| Konu | Uygulamamızın uygulaması |
|-------|----------------|
| Hesap | **Gerekli değil** — kayıt, e-posta ile giriş veya telefon numarası yok |
| iHTC Studio tarafından veri toplama | **Veri Toplanmıyor** — kişisel verilerinizi alan bir arka uç işletmiyoruz |
| Ağ | Kütüphane, okuma, ezberleme, çalışma, avlanma, widgetlar ve günlük bildirimler kurulumdan sonra **çevrimdışı** çalışır |
| Analitik / reklam / izleme | **Yok** — üçüncü taraf analitik, reklam veya izleme SDK'ları yok; Uygulama İzleme Şeffaflığı kullanılmaz |
| İsteğe bağlı Apple hizmetleri | **iCloud** (özel KVS'niz), paylaşım kartları için **Fotoğraf Kitaplığı (Only Add)**, isteğe bağlı bahşiş için **StoreKit**, **yerel bildirimler**, isteğe bağlı **Canlı Etkinlikler** |

## Veri Toplama

Kişisel bilgileri reklam veya analiz için **toplamıyoruz**, satmıyoruz veya paylaşmıyoruz.

- **Hesap gerekmez** — Tüm temel özellikleri bizde hesap oluşturmadan kullanabilirsiniz.
- **Analitik veya reklam yok** — Uygulama ikili dosyası üçüncü taraf analitik, reklam veya çökme bildirim SDK'larını içermez, telefonla bize veri göndermez.
- **İçerik yükleme yok** — Okuma geçmişiniz, favorileriniz (hikaye favorileri dahil), satır listeleri, çalışma ilerlemeniz, streakler ve tercihlerinizi cihazınızda (ve isteğe bağlı olarak **iCloud'unuzda**) kalır. Bunlar iHTC Studio sunucularına asla yüklenmez çünkü **bu uygulama için böyle sunucular çalıştırmıyoruz**.

## Uygulama Nasıl Çalışır

- **Paketlenmiş kitaplık** — JSON pasajı, karakter pinyin'i, yerel dil/İngilizce, öyküler, klasik dizinler ve hanedanlar, uygulama/widget paketinin içinde gönderilir. Tarama ve çalışma ağ isteği gerektirmez. 
- **Cihaz içi konuşma** — Okuma, Apple'ın **AVSpeechSynthesizer** (TTS) sistemini kullanır. iHTC Studio'ya pasaj metni göndermiyoruz. 
- **Widget'lar ve Uygulama Grubu** — Widget'lar ve uygulama, cihazınızdaki `group.com.iHTCboy.iThree` Uygulama Grubu aracılığıyla tercihleri ​​ve hafif durumu paylaşır. 
- **Günlük bildirimler** — Kullanıcı Bildirimleriyle yerel olarak planlanır. Bir bildirime dokunulduğunda cihazdaki pasaj kimliğine giden derin bağlantı açılır; sunucu çıkışı yok. 
- **Kartları paylaş** — Görüntüler cihazda oluşturulur. Kaydetme, **Yalnızca Fotoğraf Kitaplığı eklentisini** yalnızca kaydet'e dokunduğunuzda kullanır. Sistem Paylaşım Sayfası, görüntüyü **seçtiğiniz** bir uygulamaya gönderebilir; o hedefin gizlilik politikası geçerli olur. 
- **İsteğe bağlı ipucu** — "İpucu Geliştirici", Apple tarafından gerçekleştirilen bir **StoreKit** sarf malzemesidir. Ödeme kartı bilgilerinizi almıyoruz. 
- **Siri / Kısayollar / Kontrol Merkezi** — İsteğe bağlı sistem entegrasyonları cihazdaki derin bağlantıları açar; kütüphanenizi bize göndermiyorlar. 
- **İsteğe Bağlı Spotlight** — Dizin oluşturmayı etkinleştirirseniz içerik, yerel arama için cihazdaki sistem tarafından dizine eklenir; bir arama arka ucu kullanmıyoruz.

## Cihazınızda Saklanan Veriler 

| Veri | Nerede | Amaç | 
|------|-------|-------------| 
| Geçiş veritabanı (pinyin dahil) | Uygulama / Widget paketi | Çevrimdışı okuma ve çalışma | 
| Favoriler ve satır listeleri | Uygulama Grubu Kullanıcı Varsayılanları | Yıldızlı pasajlar / hikayeler ve kullanıcı listeleri | 
| Okuma geçmişi / son okuma | Uygulama Grubu Kullanıcı Varsayılanları | Okumaya devam et, geçmiş kullanıcı arayüzü | 
| Çalışma ilerlemesi ve ustalık | Uygulama Grubu Kullanıcı Varsayılanları | Sınıf durumu, sınav / Arama ilerlemesi | 
| Antrenman serisi / check-in | Uygulama Grubu Kullanıcı Varsayılanları | Günlük alışkanlık | 
| Görünüm ve okuma tercihleri ​​| Uygulama Grubu Kullanıcı Varsayılanları | Tema, aksan, dil, düzen, TTS, sekmeler, widget'lar | 
| Daily Line önbelleği ve bildirim tercihleri ​​| Uygulama Grubu Kullanıcı Varsayılanları | Bugünün kimliği, program zamanı, bağlamsal geçiş | 
| Paylaşımlı kart tercihleri ​​| Uygulama Grubu Kullanıcı Varsayılanları | Son stil/oran seçenekleri | 
| İlk katılım ve TipKit durumu | Standart Kullanıcı Varsayılanları (cihaz) | Hoş geldiniz kılavuzu / keşif ipuçları | 
| Ana Ekran hızlı eylemler | Sistem + yerel tercihler | Yapılandırdığınız kısayollar | 
| Widget / Canlı Etkinlik anlık görüntüleri | Uygulama Grubu / ActivityKit | Daha önce açmış olduğunuz metni görüntüleyin |

Uygulamayı kaldırmak, uygulamayla ilişkili sandbox ve Uygulama Grubu verilerini kaldırır (iOS/macOS davranışına tabidir). İsteğe bağlı iCloud kopyaları, siz temizleyene veya senkronizasyonu kapatıp başka yerde silene kadar **iCloud’unuzda** kalır.

## iCloud Senkronizasyonu (İsteğe Bağlı)

Eğer Ayarlar’dan **iCloud Senkronizasyonu**’nu etkinleştirirseniz, uygulama seçili kullanıcı verilerini Apple’ın **`NSUbiquitousKeyValueStore`** aracılığıyla **Apple Kimliğinizle** eşler:

- Passage favorileri
- Hikaye favorileri
- Satır listeleri
- Okuma geçmişi
- Çalışma ilerlemesi / ustalık
- Pratik serileri

Senkronizasyon trafiği **Apple iCloud**’a gider, iHTC Studio’ya değil. Ayarlardan senkronizasyonu devre dışı bırakabilirsiniz. iCloud içeriğinizi okuyamayız.

## İzinler

iThree, yalnızca bir özellik onları gerektirdiğinde izin ister:

| İzin | Ne zaman | Neden | 
|---------------|----------|-----| 
| Bildirimler | Günlük Hat hatırlatıcılarını etkinleştirirsiniz | Hatırlatma bildirimlerinin yerel planlanması | 
| Fotoğraf Kitaplığı (Yalnızca Ekle) | Bir paylaşım kartını kaydedersiniz | İşlenen görüntüyü yazın; tam kütüphane okuma erişimine ihtiyacımız yok | 
| iCloud | Senkronizasyonu etkinleştirirsiniz | Favorileri / listeleri / geçmişi / ilerlemeyi / serileri senkronize et | 
| Canlı Etkinlikler (iOS) | Canlı Okuma Etkinliğini etkinleştirirsiniz | Okuduğunuz pasajı Kilit Ekranında / Dinamik Ada'da gösterin | 
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

iThree, 13 yaşın altındaki çocuklar (veya bölgenizdeki eşdeğer yaş) dahil olmak üzere hiçbir kişisel veriyi bilerek toplamaz. Veri toplama altyapısı işletmediğimiz için bizimle kayıtlı bir çocuk profili bulunmamaktadır. Aileler, okuma ve çalışma özelliklerini kendi cihazlarında çevrimdışı olarak kullanabilirler.

## Üçüncü Taraflar

- **Apple** — App Store dağıtımı, isteğe bağlı StoreKit satın alımları, isteğe bağlı iCloud KVS, sistem TTS, sizin seçtiğiniz Paylaşım Sayfası hedefleri ve işletim sistemi düzeyinde bildirim / Canlı Aktivite / Siri / Kestirmeler teslimi.
- Reklam, analiz veya sosyal giriş için başka hiçbir üçüncü taraf SDK’sı veri toplama amacıyla dahil edilmemiştir.

## Uluslararası Kullanıcılar

Uygulama, cihazınızda çevrimdışı çalışacak şekilde tasarlanmıştır. İsteğe bağlı Apple hizmetleri Apple’ın şartlarına ve bölgesel kullanılabilirliğe tabidir.

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
