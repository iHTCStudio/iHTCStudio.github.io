**Son güncelleme:** 5 Eylül 2026

iHTC Studio ("biz"), **iMencius** ("爱孟子 / 愛孟子", Bundle ID `com.iHTCboy.iMencius`) uygulamasını geliştirdi. Bu Gizlilik Politikası, uygulamayı kullandığınızda hangi verilerin işlendiğini (ve işlenmediğini) açıklar. **Apple App Review** ve kullanıcılar **bu sayfayı** herkese açık gizlilik politikası olarak kullanabilir. App Store Connect için tarayıcıda bu sayfayı açın ve adres çubuğundan URL’yi kopyalayın (genel site alan adı zamanla değişebilir).

## Özet (Apple Gizlilik Beslenme Etiketi uyumu)

| Konu | Uygulamamızın uygulaması |
|-------|----------------|
| Hesap | **Gerekli değil** — kayıt, e-posta ile giriş veya telefon numarası yok |
| iHTC Studio tarafından veri toplama | **Veri Toplanmıyor** — kişisel verilerinizi alan bir arka uç işletmiyoruz |
| Ağ | Kütüphane, okuma, seslendirme, Nurturing Qi Study, widget’lar ve günlük bildirimler kurulumdan sonra **çevrimdışı** çalışır |
| Analitik / reklam / izleme | **Yok** — üçüncü taraf analitik, reklam veya izleme SDK'ları yok; Uygulama İzleme Şeffaflığı kullanılmaz |
| İsteğe bağlı Apple hizmetleri | **iCloud** (özel KVS), 孟 kartları için **Fotoğraf Kitaplığı (yalnızca ekleme)**, isteğe bağlı **StoreKit** bahşiş, **yerel bildirimler**, isteğe bağlı **Canlı Etkinlikler**, isteğe bağlı cihaz içi **el yazısı** (Vision) |

## Veri Toplama

Kişisel bilgileri reklam veya analiz için **toplamıyoruz**, satmıyoruz veya paylaşmıyoruz.

- **Hesap gerekmez** — Tüm temel özellikleri bizde hesap oluşturmadan kullanabilirsiniz.
- **Analitik veya reklam yok** — Uygulama ikili dosyası üçüncü taraf analitik, reklam veya çökme bildirim SDK'larını içermez, telefonla bize veri göndermez.
- **İçerik yüklenmez** — Okuma geçmişi, favoriler, listeler, notlar, çalışma ilerlemesi ve tercihler cihazınızda (ve isteğe bağlı **iCloud’unuzda**) kalır. **Bu uygulama için böyle sunucular işletmediğimizden** iHTC Studio sunucularına yüklenmez.

## Uygulama Nasıl Çalışır

- **Paketlenmiş kitaplık** — Metin JSON, vernacular/English, dizinler ve çalışma yardımcıları uygulama/widget paketinin içindedir. Gezinme ve çalışma için ağ gerekmez.
- **Cihaz içi konuşma** — Okuma, Apple'ın **AVSpeechSynthesizer** (TTS) sistemini kullanır. iHTC Studio'ya pasaj metni göndermiyoruz.
- **Widget'lar ve App Group** — Widget'lar ve uygulama, cihazınızdaki `group.com.iHTCboy.iMencius` App Group'u üzerinden tercihleri ve hafif durumu paylaşır.
- **Günlük bildirimler** — Kullanıcı Bildirimleriyle yerel olarak planlanır. Bir bildirime dokunulduğunda cihazdaki pasaj kimliğine giden derin bağlantı açılır; sunucu çıkışı yok.
- **孟 kartları** — Görseller cihazda oluşturulur. Kaydetme yalnızca kaydet’e dokunduğunuzda **Fotoğraf Kitaplığı (yalnızca ekleme)** kullanır. Paylaşım Sayfası görseli **sizin seçtiğiniz** bir uygulamaya gönderebilir; o hedefin gizlilik politikası geçerli olur.
- **El yazısı araması (iOS)** — İsteğe bağlı karakter tanıma, cihazda Apple **Vision**'ı kullanır. Konturlar yüklenmedi.
- **İsteğe bağlı ipucu** — "İpucu Geliştirici", Apple tarafından gerçekleştirilen bir **StoreKit** sarf malzemesidir. Ödeme kartı bilgilerinizi almıyoruz.
- **Siri / Kısayollar / Kontrol Merkezi** — İsteğe bağlı sistem entegrasyonları cihazdaki derin bağlantıları açar; kütüphanenizi bize göndermiyorlar.
- **İsteğe Bağlı Spotlight** — Dizin oluşturmayı etkinleştirirseniz içerik, yerel arama için cihazdaki sistem tarafından dizine eklenir; bir arama arka ucu kullanmıyoruz.

## Cihazınızda Saklanan Veriler

| Veri | Nerede | Amaç |
|------|-------|-------------|
| Mencius veritabanı | App / Widget paketi | Çevrimdışı okuma ve çalışma |
| Favoriler ve listeler (读孟单 lists) | App Group UserDefaults | Yıldızlı pasajlar ve kullanıcı listeleri |
| Okuma geçmişi / son okuma | Uygulama Grubu Kullanıcı Varsayılanları | Okumaya devam et, geçmiş kullanıcı arayüzü |
| Notlar | Uygulama Grubu Kullanıcı Varsayılanları | Yazdığınız notları okuma |
| Çalışma ilerlemesi ve ustalık | Uygulama Grubu Kullanıcı Varsayılanları | Sınıf durumu, sınav / Arama ilerlemesi |
| Antrenman serisi / check-in | Uygulama Grubu Kullanıcı Varsayılanları | Günlük alışkanlık |
| Paylaşım kartı tercihleri | App Group UserDefaults | Son stil / oran seçimleri |
| Daily Saying cache & notification prefs | App Group UserDefaults | Bugünün ID’si, schedule time, contextual toggle |
| Kart tercihleri | App Group UserDefaults | Son stil/oran |
| İlk katılım ve TipKit durumu | Standart Kullanıcı Varsayılanları (cihaz) | Hoş geldiniz kılavuzu / keşif ipuçları |
| Son aramalar | Standard UserDefaults (device) | Yazdığınız arama geçmişi |
| Ana Ekran hızlı eylemler | Sistem + yerel tercihler | Yapılandırdığınız kısayollar |
| Widget / Canlı Etkinlik anlık görüntüleri | Uygulama Grubu / ActivityKit | Daha önce açmış olduğunuz metni görüntüleyin |

Uygulamayı kaldırmak, uygulamayla ilişkili sandbox ve Uygulama Grubu verilerini kaldırır (iOS/macOS davranışına tabidir). İsteğe bağlı iCloud kopyaları, siz temizleyene veya senkronizasyonu kapatıp başka yerde silene kadar **iCloud’unuzda** kalır.

## iCloud Senkronizasyonu (İsteğe Bağlı)

Eğer Ayarlar’dan **iCloud Senkronizasyonu**’nu etkinleştirirseniz, uygulama seçili kullanıcı verilerini Apple’ın **`NSUbiquitousKeyValueStore`** aracılığıyla **Apple Kimliğinizle** eşler:

- Favoriler
- Listeler (读孟单 lists)
- Okuma geçmişi
- Çalışma ilerlemesi / ustalık
- Pratik serileri
- Notlar

Senkronizasyon trafiği **Apple iCloud**’a gider, iHTC Studio’ya değil. Ayarlardan senkronizasyonu devre dışı bırakabilirsiniz. iCloud içeriğinizi okuyamayız.

## İzinler

iLiezi yalnızca bir özellik ihtiyaç duyduğunda izin ister:

| İzin | Ne zaman | neden |
|------------|------|-----|
| Bildirimler | Daily Saying reminders etkinleştirirsiniz | Yerel zamanlama of reminder notifications |
| Fotoğraf Kitaplığı (yalnızca ekleme) | Kart kaydetme | İşlenmiş görsel yaz |
| iCloud | Senkronizasyonu açarsınız | Favoriler/listeler/geçmiş/ilerleme/seriler/notlar |
| Canlı Etkinlikler (iOS) | Canlı Okuma Etkinliğini etkinleştirirsiniz | Okuduğunuz pasajı Kilit Ekranında / Dinamik Ada'da gösterin |
| Arka planda ses (yetenek) | Arka planda okumayı etkinleştirirsiniz | Uygulama ön planda olmadığında TTS'ye devam edin |

Kişiler, konum, kamera, mikrofon (TTS hariç), izleme **istenmez**. El yazısı — cihaz Vision.

## Ne Yapmıyoruz

- Kişisel verileri **satmıyoruz**.
- Reklam profilleri **oluşturmuyoruz**.
- Bir hesaba veya sosyal girişe **gerek duymayız**.
- Veri toplama amacıyla üçüncü taraf reklamları, analizleri veya sosyal SDK'ları **yerleştirmeyiz**.
- Bir kartı kaydetmeyi seçtiğinizde **yalnızca eklenti** dışında Fotoğraf Kitaplığınıza **erişmeyiz**.
- StoreKit ödeme kartı numaralarını **almıyoruz** (ödemeleri Apple işler).
- El yazısı/pasaj metni iHTC Studio’ya **yüklenmez**.

## Çocukların Gizliliği

iMencius, genel kitleye yönelik bir eğitim/okuma uygulamasıdır ve **Kids Category**’de değildir. Çocuklardan bilerek kişisel bilgi toplamayız. Uygulama hesap gerektirmez. Aileler kendi cihazlarında okuma ve çalışma özelliklerini çevrimdışı kullanabilir.

## Üçüncü Taraflar

- **Apple** — App Store dağıtımı, isteğe bağlı StoreKit satın alımları, isteğe bağlı iCloud KVS, sistem TTS, seçtiğiniz Paylaşım Sayfası hedefleri ve işletim sistemi düzeyinde bildirim/Canlı Etkinlik/Siri/Kestirmeler/Vision.
- Reklam, analiz veya sosyal giriş için başka hiçbir üçüncü taraf SDK’sı veri toplama amacıyla dahil edilmemiştir.

## Uluslararası Kullanıcılar

Uygulama, cihazınızda çevrimdışı çalışacak şekilde tasarlanmıştır. İsteğe bağlı Apple hizmetleri Apple’ın şartlarına ve bölgesel kullanılabilirliğe tabidir.

## Veri Saklama ve Silme

- **Cihazda** — Yerel sandbox ve App Group verilerini kaldırmak için uygulamayı silin (işletim sistemi davranışına bağlıdır).
- **iCloud** — Senkronizasyonu kapatın ve gerektiğinde iCloud hesabınızdan / cihazlarınızdan ilgili anahtarları temizleyin; iCloud’unuzu sizin adınıza silemeyiz.
- **Hiçbir şeyi** iHTC Studio sunucularında bu uygulama için saklamıyoruz çünkü bunu toplamıyoruz.

## Politika Değişiklikleri

Bu Gizlilik Politikasını güncelleyebiliriz. Üstteki 「Son güncelleme」 tarihi değişir. Güncellemeden sonra kullanıma devam etmek, revize edilmiş politikayı kabul ettiğiniz anlamına gelir. Önemli değişiklikler uygun olduğunda App Store 「Yenilikler」 metninde de belirtilebilir.

## İletişim

Gizlilik ile ilgili sorular: [AppleOSer@gmail.com](mailto:AppleOSer@gmail.com)
