**Son Güncelleme:** 5 Ağustos 2026

iHTC Studio ("biz", "bize" veya "bizim") **iYijing**i (diğer adıyla "爱周易" / "愛周易", Paket Kimliği `com.iHTCboy.iYiJing`) geliştirdi. Bu Gizlilik Politikası, uygulamayı kullandığınızda hangi verilerin işlendiğini (ve hangilerinin işlenmediğini) açıklar. **Apple App Review** ve kullanıcılar, uygulamanın kamuya açık gizlilik politikası olarak **bu sayfaya** güvenebilir. App Store Connect için, bu Gizlilik Politikasını tarayıcınızda açın ve adres çubuğundan adresi kopyalayın (kamu sitesi alan adı zamanla değişebilir).

## Özet (Apple Gizlilik Beslenme Etiketi uyumu)

| Konu | Uygulamamız |
|-------|----------------|
| Hesap | **Gerekli değil** — kayıt, e-posta ile giriş veya telefon numarası yok |
| iHTC Studio tarafından veri toplama | **Veri Toplanmıyor** — kişisel verilerinizi alan bir arka uç işlemi yürütmüyoruz |
| Ağ | Kütüphane, okuma, ezberleme, kültürel yayın, Çalışma Salonu, widget'lar ve günlük bildirimler kurulumdan sonra **çevrimdışı** çalışır |
| Analitik / reklam / izleme | **Yok** — üçüncü taraf analitik, reklam veya izleme SDK'ları yok; App Tracking Transparency kullanılmaz |
| İsteğe bağlı Apple hizmetleri | **iCloud** (özel KVS'iniz, birleştirme), **Fotoğraf Kitaplığı (Sadece Ekleme)** çalışma kartları için, **StoreKit** isteğe bağlı bahşiş için, **yerel bildirimler**, isteğe bağlı **Canlı Aktiviteler** |

## Veri Toplama

Kişisel bilgileri reklam veya analiz amacıyla **toplamıyor**, **satmıyor** veya **paylaşmıyoruz**.

- **Hesap gerekmiyor** — Tüm temel özellikleri bizimle bir hesap oluşturmadan kullanabilirsiniz.
- **Analitik veya reklam yok** — Uygulama ikili dosyası, üçüncü taraf analitik, reklam veya hata raporlama SDK'larını entegre etmez ve bu SDK'lar bize veri göndermez.
- **İçerik yükleme yok** — Okuma geçmişiniz, favorileriniz, listeleriniz, notlarınız, yayın kayıtlarınız, yanlış kitaplar, ustalık, seri ve tercihleriniz cihazınızda (ve isteğe bağlı olarak **iCloud’unuzda**) kalır. Bu veriler asla iHTC Studio sunucularına yüklenmez çünkü **bu uygulama için böyle sunucular çalıştırmıyoruz**.

## Uygulama Nasıl Çalışır

- **Paketlenmiş kitaplık** — Hexagram JSON, Ten Wings, trigramlar, ünlü çizgiler ve dizinler uygulama/widget paketinin içinde gönderilir. Tarama ve çalışma ağ isteği gerektirmez. 
- **Cihaz içi konuşma** — Okuma, Apple'ın **AVSpeechSynthesizer** (TTS) sistemini kullanır. Heksagram metni iHTC Studio'ya göndermiyoruz. 
- **Kültürel döküm** — Madeni para ve civanperçemi prosedürleri tamamen eğitimsel sembolizm amacıyla cihaz üzerinde yürütülür; Kaydetmeyi seçtiğiniz kayıtlar yerel kalır (ve isteğe bağlı olarak iCloud'unuzda). 
- **Widget'lar ve Uygulama Grubu** — Widget'lar ve uygulama, cihazınızdaki `group.com.iHTCboy.iYiJing` Uygulama Grubu aracılığıyla tercihleri ​​ve hafif durumu paylaşır. 
- **Günlük bildirimler** — Kullanıcı Bildirimleriyle yerel olarak planlanır. Dokunduğunuzda cihazdaki heksagram kimliğine derin bir bağlantı açılır; sunucu çıkışı yok. 
- **Çalışma kartları** — Görüntüler cihazda oluşturulur. Kaydetme, **Yalnızca Fotoğraf Kitaplığı eklentisini** yalnızca kaydet'e dokunduğunuzda kullanır. Sistem Paylaşım Sayfası, görüntüyü **seçtiğiniz** bir uygulamaya gönderebilir; o hedefin gizlilik politikası geçerli olur. 
- **İsteğe bağlı ipucu** — "İpucu Geliştirici", Apple tarafından gerçekleştirilen bir **StoreKit** sarf malzemesidir. Ödeme kartı bilgilerinizi almıyoruz. 
- **Siri / Kısayollar / Kontrol Merkezi** — İsteğe bağlı sistem entegrasyonları cihazdaki derin bağlantıları açar; kütüphanenizi bize göndermiyorlar. 
- **İsteğe Bağlı Spotlight** — Dizin oluşturmayı etkinleştirirseniz içerik, yerel arama için cihazdaki sistem tarafından dizine eklenir; bir arama arka ucu kullanmıyoruz. 
- **İsteğe Bağlı Canlı Etkinlik** — Varsayılan olarak kapalıdır; etkinleştirildiğinde, okuduğunuz heksagramı Kilit Ekranı / Dinamik Ada'da gösterir.

## Cihazınızda Saklanan Veriler 

| Veri | Nerede | Amaç | 
|------|-------|-------------| 
| Heksagram / Kanatlar / trigram veritabanı | Uygulama / Widget paketi | Çevrimdışı okuma ve çalışma | 
| Favoriler ve heksagram listeleri | Uygulama Grubu Kullanıcı Varsayılanları | Yıldızlı çalışmalar ve kullanıcı listeleri | 
| Okuma geçmişi / son okuma | Uygulama Grubu Kullanıcı Varsayılanları | Okumaya devam et, geçmiş kullanıcı arayüzü | 
| Çalışma ilerlemesi, ustalık ve yanlış kitap | Uygulama Grubu Kullanıcı Varsayılanları | Çalışma Salonu durumu | 
| Döküm kayıtları | Uygulama Grubu Kullanıcı Varsayılanları | Kaydettiğiniz kültürel döküm geçmişi | 
| Notlar | Uygulama Grubu Kullanıcı Varsayılanları | Yazdığınız notlar | 
| Seri / giriş | Uygulama Grubu Kullanıcı Varsayılanları | Günlük alışkanlık | 
| Görünüm ve okuma tercihleri ​​| Uygulama Grubu Kullanıcı Varsayılanları | Tema, aksan, dil, düzen, TTS, sekmeler, widget'lar | 
| Günlük Heksagram önbelleği ve bildirim tercihleri ​​| Uygulama Grubu Kullanıcı Varsayılanları | Bugünün kimliği, program zamanı | 
| Paylaşımlı kart tercihleri ​​| Uygulama Grubu Kullanıcı Varsayılanları | Son stil/oran seçenekleri | 
| İlk katılım durumu | Standart Kullanıcı Varsayılanları (cihaz) | Hoş geldiniz kılavuzu | 
| Widget / Canlı Etkinlik anlık görüntüleri | Uygulama Grubu / ActivityKit | Daha önce açmış olduğunuz metni görüntüleyin |

Uygulamayı kaldırmak, uygulama ile ilişkili sandbox ve Uygulama Grubu verilerini kaldırır (iOS/macOS davranışına tabi). İsteğe bağlı iCloud kopyaları, siz bunları temizleyene kadar veya senkronizasyonu kapatıp başka yerde silene kadar **iCloud'unuzda** kalır.

## iCloud Senkronizasyonu (İsteğe Bağlı)

Ayarlar’da **iCloud Senkronizasyonu**’nu etkinleştirirseniz, uygulama, favoriler, listeler, geçmiş, ustalık, notlar, casting kayıtları, yanış kitabı ve başarı zincirleri için birleştirme kuralları kullanarak, Apple ID’nize bağlı Apple’ın **`NSUbiquitousKeyValueStore`** servisi aracılığıyla seçilen kullanıcı verilerini yansıtır.

Senkronizasyon trafiği **Apple iCloud**’a gider, iHTC Studio’ya gitmez. Senkronizasyonu Ayarlar’dan devre dışı bırakabilirsiniz. iCloud içeriğinizi okuyamayız.

## İzinler

iYijing, yalnızca bir özellik izin gerektirdiğinde izin ister:

| İzin | Ne Zaman | Neden |
|------------|------|-----|
| Bildirimler | Günlük Heksagram hatırlatmalarını etkinleştirdiğinizde | Hatırlatma bildirimlerinin yerel olarak planlanması |
| Fotoğraf Kütüphanesi (Sadece Ekle) | Bir çalışma kartını kaydettiğinizde | Render edilmiş görüntüyü yazın; tam kütüphane okuma erişimine gerek yok |
| iCloud | Senkronizasyonu etkinleştirdiğinizde | Favoriler / listeler / geçmiş / ustalık / notlar / atma / yanlış kitap / seri hatalarını senkronize edin |
| Canlı Aktiviteler (iOS) | Okuma Canlı Aktivitesini etkinleştirdiğinizde | Okuduğunuz heksagramı Kilit Ekranında / Dynamic Island'da gösterin |
| Arka plan sesi (özellik) | Arka plan okumasını etkinleştirdiğinizde | Uygulama ön planda olmadığında TTS'i devam ettirin |

Kişiler, kesin Konum, Kamera, Mikrofon (sistem TTS oynatımı dışında) veya İzleme talep etmiyoruz.

## Yapmadıklarımız

- Kişisel verileri **satmıyoruz**. 
- Reklam profilleri **oluşturmuyoruz**. 
- Bir hesaba veya sosyal girişe **gerek duymayız**. 
- Veri toplama amacıyla üçüncü taraf reklamları, analizleri veya sosyal SDK'ları **yerleştirmeyiz**. 
- Bir kartı kaydetmeyi seçtiğinizde **yalnızca eklenti** dışında Fotoğraf Kitaplığınıza **erişmeyiz**. 
- StoreKit ödeme kartı numaralarını **almıyoruz** (ödemeleri Apple işler). 
- Döküm sorularını veya sonuçlarını herhangi bir sunucuya **göndermiyoruz**. 

## Çocukların Gizliliği 

iYijing, 13 yaşın (veya bölgenizdeki eşdeğer yaşın) altındaki çocuklar da dahil olmak üzere hiç kimseden kişisel veri toplamaz. Bir veri toplama arka ucu çalıştırmadığımız için bizde saklanan bir alt profil yoktur. Aileler okuma ve çalışma özelliklerini kendi cihazlarında çevrimdışı olarak kullanabilir. 

## Üçüncü Taraflar 

- **Apple** — App Store dağıtımı, isteğe bağlı StoreKit satın alımları, isteğe bağlı iCloud KVS, sistem TTS'si, seçtiğiniz Paylaşım Sayfası hedefleri ve işletim sistemi düzeyinde bildirim / Canlı Etkinlik / Siri / Kısayol teslimi. 
- **Veri toplama amacıyla reklamlara, analizlere veya sosyal oturum açmaya yönelik başka hiçbir üçüncü taraf SDK'sı** dahil edilmemiştir. 

## Uluslararası Kullanıcılar

Uygulama, cihazınızda çevrimdışı çalışacak şekilde tasarlanmıştır. İsteğe bağlı Apple hizmetleri, Apple'ın koşullarına ve bölgesel kullanılabilirliğe uygundur. 

## Veri Saklama ve Silme 

- **Cihazda** — Yerel tercihler ve ilerleme durumu, siz bunları uygulama içinde temizleyene (varsa), cihazı sıfırlayana veya uygulamayı kaldırana kadar kalır. 
- **iCloud (isteğe bağlı)** — Senkronize ettiğiniz veriler, siz senkronizasyonu devre dışı bırakana ve/veya Apple'ın araçları aracılığıyla temizleyene kadar Apple politikaları kapsamında **iCloud hesabınızda kalır. 
- **iHTC Studio** — Sunucularımızda kişisel veri toplamadığımız için, e-posta sorularınızı yanıtlamanın ötesinde talep üzerine silebileceğimiz bir hesap veri kümesi yoktur. 

## Bu Politikadaki Değişiklikler 

Bu Gizlilik Politikasını zaman zaman güncelleyebiliriz. Üst kısımdaki “Son güncelleme” tarihi değişecek ve revize edilen politika bu Gizlilik Politikası sayfasında yayınlanacaktır. 

## Bize Ulaşın 

Bu Gizlilik Politikası veya gizlilik uygulamaları hakkında sorularınız varsa: 

- **E-posta:** [AppleOSer@gmail.com](mailto:AppleOSer@gmail.com) 

Genellikle 48 saat içinde yanıt veririz.
