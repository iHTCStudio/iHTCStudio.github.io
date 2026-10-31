**Son güncelleme:** 18 Ağustos 2026

iHTC Studio ("biz"), **iThousand** ("爱千字文" / "爱千字文", Bundle ID `com.iHTCboy.iThousand`) uygulamasını geliştirdi. Bu Gizlilik Politikası, uygulamayı kullandığınızda hangi verilerin işlendiğini (ve işlenmediğini) açıklar. **Apple App Review** ve kullanıcılar **bu sayfayı** herkese açık gizlilik politikası olarak kullanabilir. App Store Connect için tarayıcıda bu sayfayı açın ve adres çubuğundan URL’yi kopyalayın (genel site alan adı zamanla değişebilir).

## Özet (Apple Gizlilik Beslenme Etiketi uyumu)

| Konu | Uygulamamızın uygulaması |
|-------|----------------|
| Hesap | **Gerekli değil** — kayıt, e-posta ile giriş veya telefon numarası yok |
| iHTC Studio tarafından veri toplama | **Veri Toplanmıyor** — kişisel verilerinizi alan bir arka uç işletmiyoruz |
| Ağ | Kütüphane, character cards, reading, recite, Primer Hall, Hunt, widgets, and daily notifications work **offline** after install kurulumdan sonra **çevrimdışı** çalışır |
| Analitik / reklam / izleme | **Yok** — üçüncü taraf analitik, reklam veya izleme SDK'ları yok; Uygulama İzleme Şeffaflığı kullanılmaz |
| İsteğe bağlı Apple hizmetleri | **iCloud** (your private KVS), **Photo Library (Add Only)** for share cards, **StoreKit** for optional tipping, **local notifications**, optional **Live Activities**, optional **Spotlight** (off by default), optional **system speech / translation** |

## Veri Toplama

Kişisel bilgileri reklam veya analiz için **toplamıyoruz**, satmıyoruz veya paylaşmıyoruz.

- **Hesap gerekmez** — Tüm temel özellikleri bizde hesap oluşturmadan kullanabilirsiniz.
- **Analitik veya reklam yok** — Uygulama ikili dosyası üçüncü taraf analitik, reklam veya çökme bildirim SDK'larını içermez, telefonla bize veri göndermez.
- **İçerik yüklenmez** — reading history, favorites, lists (千单), saved characters, notes, study progress, streaks, and preferences stay on your device (and optionally in **your** iCloud). They are never uploaded to iHTC Studio servers because **we do not run such servers for this app**.

## Uygulama Nasıl Çalışır

- **Paketlenmiş kitaplık** — Metin JSON, vernacular/English, dizinler ve çalışma yardımcıları uygulama/widget paketinin içindedir. Gezinme ve çalışma için ağ gerekmez.
- **Cihaz içi konuşma** — Okuma, Apple'ın **AVSpeechSynthesizer** (TTS) sistemini kullanır. iHTC Studio'ya pasaj metni göndermiyoruz.
- **Sistem çevirisi** — Apple cihaz/sistem çevirisi; Apple OS.
- **Widget'lar ve App Group** — Widget'lar ve uygulama, cihazınızdaki `group.com.iHTCboy.iThousand` App Group'u üzerinden tercihleri ve hafif durumu paylaşır.
- **Günlük bildirimler** — Kullanıcı Bildirimleriyle yerel olarak planlanır. Bir bildirime dokunulduğunda cihazdaki pasaj kimliğine giden derin bağlantı açılır; sunucu çıkışı yok.
- **Kartları paylaş** — Görüntüler cihazda oluşturulur. Kaydetme, **Yalnızca Fotoğraf Kitaplığı eklentisini** yalnızca kaydet'e dokunduğunuzda kullanır. Sistem Paylaşım Sayfası, görüntüyü **seçtiğiniz** bir uygulamaya gönderebilir; o hedefin gizlilik politikası geçerli olur.
- **İsteğe bağlı bahşiş** — “Tip Developer” (`com.iHTCboy.iThousand.6`), Apple **StoreKit**.
- **Siri / Kısayollar / Kontrol Merkezi** — İsteğe bağlı sistem entegrasyonları cihazdaki derin bağlantıları açar; kütüphanenizi bize göndermiyorlar.
- **İsteğe bağlı Spotlight** — varsayılan kapalı. Pasajlar/kartlar cihazda dizinlenir; arama arka ucu yok.
- **Geri bildirim e-postası** — yalnızca sorun giderme için yazdığınız metin ve cihaz/uygulama tanılaması (sürüm, OS, dil) içerebilir.

## Cihazınızda Saklanan Veriler

| Veri | Nerede | Amaç |
|------|-------|-------------|
| Pasaj ve karakter veritabanı | App / Widget paketi | Çevrimdışı, okuryazarlık kartları |
| Favoriler ve listeler (千单) | App Group UserDefaults | Yıldızlı pasajlar ve kullanıcı listeleri |
| Kayıtlı karakterler ve dizeler | App Group UserDefaults | Zor karakterler, yıldızlı satırlar |
| Okuma geçmişi / son okuma | Uygulama Grubu Kullanıcı Varsayılanları | Okumaya devam et, geçmiş kullanıcı arayüzü |
| Çalışma ilerlemesi ve ustalık | App Group UserDefaults | Primer Hall state, quiz / Hunt progress |
| Notlar | App Group UserDefaults | Pasaj notları |
| Çalışma serisi / check-in | App Group UserDefaults | Günlük alışkanlık |
| Paylaşım kartı tercihleri | App Group UserDefaults | Son stil / oran seçimleri |
| Daily Line önbelleği ve bildirim tercihleri ​​| Uygulama Grubu Kullanıcı Varsayılanları | Bugünün kimliği, program zamanı, bağlamsal geçiş |
| Paylaşımlı kart tercihleri ​​| Uygulama Grubu Kullanıcı Varsayılanları | Son stil/oran seçenekleri |
| İlk katılım ve TipKit durumu | Standart Kullanıcı Varsayılanları (cihaz) | Hoş geldiniz kılavuzu / keşif ipuçları |
| Ana Ekran hızlı eylemler | Sistem + yerel tercihler | Yapılandırdığınız kısayollar |
| Widget / Canlı Etkinlik anlık görüntüleri | Uygulama Grubu / ActivityKit | Daha önce açmış olduğunuz metni görüntüleyin |

Uygulamayı kaldırmak, uygulamayla ilişkili sandbox ve Uygulama Grubu verilerini kaldırır (iOS/macOS davranışına tabidir). İsteğe bağlı iCloud kopyaları, siz temizleyene veya senkronizasyonu kapatıp başka yerde silene kadar **iCloud’unuzda** kalır.

## iCloud Senkronizasyonu (İsteğe Bağlı)

Eğer Ayarlar’dan **iCloud Senkronizasyonu**’nu etkinleştirirseniz, uygulama seçili kullanıcı verilerini Apple’ın **`NSUbiquitousKeyValueStore`** aracılığıyla **Apple Kimliğinizle** eşler:

- Favoriler
- Listeler (千单)
- Kayıtlı karakterler / favori dizeler
- Okuma geçmişi
- Çalışma ilerlemesi / ustalık
- Çalışma serileri
- Notlar

Senkronizasyon trafiği **Apple iCloud**’a gider, iHTC Studio’ya değil. Ayarlardan senkronizasyonu devre dışı bırakabilirsiniz. iCloud içeriğinizi okuyamayız.

## İzinler

iLiezi yalnızca bir özellik ihtiyaç duyduğunda izin ister:

| İzin | Ne zaman | neden |
|------------|------|-----|
| Bildirimler | Daily Line reminders etkinleştirirsiniz | Yerel zamanlama |
| Fotoğraf Kitaplığı (yalnızca ekleme) | Paylaşım kartı/karakter | Write the rendered image |
| iCloud | Senkronizasyonu açarsınız | Favoriler/listeler/geçmiş/ilerleme/seriler/notlar/kayıtlı karakterler |
Ayarlar'da **iCloud Senkronizasyonu**'nu etkinleştirirseniz, uygulama seçili kullanıcı verilerini **Apple Kimliğinize** bağlı Apple'ın **`NSUbiquitousKeyValueStore`** hizmeti aracılığıyla yansıtır:
| Arka plan sesi | Arka planda okuma | Arka planda TTS |

Kişiler, kesin Konum, Kamera, Mikrofon (sistem TTS oynatmanın ötesinde) veya İzleme **talebi etmeyiz**.

## Çocukların Gizliliği

iThousand — eğitim uygulaması, Kids Category **değil**.

## Üçüncü Taraflar

Üçüncü taraf: **Apple** (…sistem çevirisi, Spotlight).

## Veri Saklama ve Silme

- **Cihazda:** ilerleme/geçmiş/notları temizleyin. Uygulamayı silmek sandbox/App Group’u kaldırır.
- **iCloud:** Ayarlar’da senkronizasyonu kapatın; iCloud depolamayı sistem Ayarları’ndan yönetin.
- **Kopya yok** — okuma, notlar, karakter yer imleri.

## Bu Politika ile İlgili Değişiklikler

Yasal, ürün veya App Store uyumluluğu nedenleriyle bu sayfayı güncelleyebiliriz. 「Son güncelleme」 tarihi değişir. Güncellemeden sonra kullanıma devam etmek, revize edilmiş politikayı kabul ettiğiniz anlamına gelir.

## İletişim

Gizlilik ile ilgili sorular: [AppleOSer@gmail.com](mailto:AppleOSer@gmail.com)
