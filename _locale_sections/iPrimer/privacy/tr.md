**Son güncelleme:** 18 Ağustos 2026

iHTC Studio ("biz"), **iPrimer** ("爱小学" / "爱小学", Bundle ID `com.iHTCboy.iPrimer`) uygulamasını geliştirdi. Bu Gizlilik Politikası, uygulamayı kullandığınızda hangi verilerin işlendiğini (ve işlenmediğini) açıklar. **Apple App Review** ve kullanıcılar **bu sayfayı** herkese açık gizlilik politikası olarak kullanabilir. App Store Connect için tarayıcıda bu sayfayı açın ve adres çubuğundan URL’yi kopyalayın (genel site alan adı zamanla değişebilir).

## Özet (Apple Gizlilik Beslenme Etiketi uyumu)

| Konu | Uygulamamızın uygulaması |
|-------|----------------|
| Hesap | **Gerekli değil** — kayıt, e-posta ile giriş veya telefon numarası yok |
| iHTC Studio tarafından veri toplama | **Veri Toplanmıyor** — kişisel verilerinizi alan bir arka uç işletmiyoruz |
| Ağ | Kütüphane, reading, recite, Character Study, meditation, Life Guidance, widgets, and daily notifications work **offline** after install kurulumdan sonra **çevrimdışı** çalışır |
| Analitik / reklam / izleme | **Yok** — üçüncü taraf analitik, reklam veya izleme SDK'ları yok; Uygulama İzleme Şeffaflığı kullanılmaz |
| İsteğe bağlı Apple hizmetleri | **iCloud** (özel KVS'niz), paylaşım kartları için **Fotoğraf Kitaplığı (Only Add)**, isteğe bağlı bahşiş için **StoreKit**, **yerel bildirimler**, isteğe bağlı **Canlı Etkinlikler** |

## Veri Toplama

Kişisel bilgileri reklam veya analiz için **toplamıyoruz**, satmıyoruz veya paylaşmıyoruz.

- **Hesap gerekmez** — Tüm temel özellikleri bizde hesap oluşturmadan kullanabilirsiniz.
- **Analitik veya reklam yok** — Uygulama ikili dosyası üçüncü taraf analitik, reklam veya çökme bildirim SDK'larını içermez, telefonla bize veri göndermez.
- **İçerik yüklenmez** — reading history, favorites, study lists, reflection journal entries, habit check-ins, meditation streaks, study progress, and preferences stay on your device (and optionally in **your** iCloud). They are never uploaded to iHTC Studio servers because **we do not run such servers for this app**.

## Uygulama Nasıl Çalışır

- **Paketlenmiş kitaplık** — Metin JSON, vernacular/English, dizinler ve çalışma yardımcıları uygulama/widget paketinin içindedir. Gezinme ve çalışma için ağ gerekmez.
- **Cihaz içi konuşma** — Okuma, Apple'ın **AVSpeechSynthesizer** (TTS) sistemini kullanır. Bölüm metnini iHTC Studio'ya göndermiyoruz.
- **Widget'lar ve App Group** — Widget'lar ve uygulama, cihazınızdaki `group.com.iHTCboy.iPrimer` App Group'u üzerinden tercihleri ve hafif durumu paylaşır.
- **Günlük bildirimler** — Kullanıcı Bildirimleriyle yerel olarak planlanır. Bir bildirime dokunduğunuzda cihazdaki bölüm kimliğine giden derin bir bağlantı açılır; sunucu çıkışı yok.
- **Kartları paylaş** — Görüntüler cihazda oluşturulur. Kaydetme, **Yalnızca Fotoğraf Kitaplığı eklentisini** yalnızca kaydet'e dokunduğunuzda kullanır. Sistem Paylaşım Sayfası, görüntüyü **seçtiğiniz** bir uygulamaya gönderebilir; o hedefin gizlilik politikası geçerli olur.
- **İsteğe bağlı bahşiş** — “Tip Developer” (`com.iHTCboy.iPrimer.6`), Apple **StoreKit**.
- **Siri / Kısayollar / Kontrol Merkezi** — İsteğe bağlı sistem entegrasyonları cihazdaki derin bağlantıları açar; kütüphanenizi bize göndermiyorlar.
- **İsteğe Bağlı Spotlight** — Dizin oluşturmayı etkinleştirirseniz içerik, yerel arama için cihazdaki sistem tarafından dizine eklenir; bir arama arka ucu kullanmıyoruz.

## Cihazınızda Saklanan Veriler

| Veri | Nerede | Amaç |
|------|-------|-------------|
| Chapter veritabanı | App / Widget paketi | Çevrimdışı okuma ve çalışma |
| Favoriler ve çalışma listeleri | App Group UserDefaults | Yıldızlı eserler ve listeler |
| Okuma geçmişi / son okuma | Uygulama Grubu Kullanıcı Varsayılanları | Okumaya devam et, geçmiş kullanıcı arayüzü |
| Çalışma ilerlemesi ve ustalık | App Group UserDefaults | Character Study state, quiz / Hunt progress |
| Çalışma serisi / check-in | App Group UserDefaults | Daily Study alışkanlığı |
| Yansıma günlüğü | App Group UserDefaults | Life Guidance günlüğü |
| Alışkanlık check-in (洒扫应对) | App Group UserDefaults | Life Guidance alışkanlıkları |
| Meditasyon serisi ve oturum | App Group UserDefaults | Meditasyon sürekliliği |
| Paylaşım kartı tercihleri | App Group UserDefaults | Son stil / oran seçimleri |
| Daily Study cache & notification prefs | App Group UserDefaults | Bugünün ID’si, schedule time, contextual toggle |
| Paylaşımlı kart tercihleri ​​| Uygulama Grubu Kullanıcı Varsayılanları | Son stil/oran seçenekleri |
| İlk katılım ve TipKit durumu | Standart Kullanıcı Varsayılanları (cihaz) | Hoş geldiniz kılavuzu / keşif ipuçları |
| Ana Ekran hızlı eylemler | Sistem + yerel tercihler | Yapılandırdığınız kısayollar |
| Widget / Canlı Etkinlik anlık görüntüleri | Uygulama Grubu / ActivityKit | Daha önce açmış olduğunuz metni görüntüleyin |

Uygulamayı kaldırmak, uygulamayla ilişkili sandbox ve Uygulama Grubu verilerini kaldırır (iOS/macOS davranışına tabidir). İsteğe bağlı iCloud kopyaları, siz temizleyene veya senkronizasyonu kapatıp başka yerde silene kadar **iCloud’unuzda** kalır.

## iCloud Senkronizasyonu (İsteğe Bağlı)

Eğer Ayarlar’dan **iCloud Senkronizasyonu**’nu etkinleştirirseniz, uygulama seçili kullanıcı verilerini Apple’ın **`NSUbiquitousKeyValueStore`** aracılığıyla **Apple Kimliğinizle** eşler:

- Favoriler
- Çalışma listeleri
- Okuma geçmişi
- Çalışma ilerlemesi / ustalık
- Çalışma serileri
- Yansıma günlüğü
- Alışkanlık check-in geçmişi

Senkronizasyon trafiği **Apple iCloud**’a gider, iHTC Studio’ya değil. Ayarlardan senkronizasyonu devre dışı bırakabilirsiniz. iCloud içeriğinizi okuyamayız.

## İzinler

iLiezi yalnızca bir özellik ihtiyaç duyduğunda izin ister:

| İzin | Ne zaman | neden |
|------------|------|-----|
| Bildirimler | Daily Study or meditation reminders etkinleştirirsiniz | Yerel zamanlama |
## iCloud Senkronizasyonu (İsteğe Bağlı)
| iCloud | Senkronizasyonu açarsınız | Favoriler/listeler/geçmiş/ilerleme/seriler/günlük/alışkanlıklar |
| Live Activities (iOS) | Reading/Meditation Live Activity | Kilit Ekranı / Dynamic Island |
| Arka plan sesi | Arka planda okuma | Arka planda TTS |

Kişiler, kesin Konum, Kamera, Mikrofon (sistem TTS oynatmanın ötesinde) veya İzleme **talebi etmeyiz**.

## Çocukların Gizliliği

iPrimer **12+**, Kids Category **değil**. Çocuk verisi toplanmaz.

## Üçüncü Taraflar

Normal kullanımda üçüncü taraf yalnızca **Apple**.

## Veri Saklama ve Silme

- **Cihazda:** uygulamayı silmek sandbox ve App Group verisini kaldırır (sisteme bağlı).
- **iCloud:** Ayarlar’da senkronizasyonu kapatın; iCloud depolamayı sistem Ayarları’ndan yönetin.
- **Kopya tutmuyoruz** — okuma/günlük/alışkanlık verilerini iHTC Studio sunucularında.

## Bu Politika ile İlgili Değişiklikler

Yasal, ürün veya App Store uyumluluğu nedenleriyle bu sayfayı güncelleyebiliriz. 「Son güncelleme」 tarihi değişir. Güncellemeden sonra kullanıma devam etmek, revize edilmiş politikayı kabul ettiğiniz anlamına gelir.

## İletişim

Gizlilik ile ilgili sorular: [AppleOSer@gmail.com](mailto:AppleOSer@gmail.com)
