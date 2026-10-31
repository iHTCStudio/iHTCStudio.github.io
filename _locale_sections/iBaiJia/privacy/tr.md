**Son güncelleme:** 18 Ağustos 2026

iHTC Studio ("biz"), **iBaiJia** ("爱百家姓" / "爱百家姓", Bundle ID `com.iHTCboy.iBaiJia`) uygulamasını geliştirdi. Bu Gizlilik Politikası, uygulamayı kullandığınızda hangi verilerin işlendiğini (ve işlenmediğini) açıklar. **Apple App Review** ve kullanıcılar **bu sayfayı** herkese açık gizlilik politikası olarak kullanabilir. App Store Connect için tarayıcıda bu sayfayı açın ve adres çubuğundan URL’yi kopyalayın (genel site alan adı zamanla değişebilir).

## Özet (Apple Gizlilik Beslenme Etiketi uyumu)

| Konu | Uygulamamızın uygulaması |
|-------|----------------|
| Hesap | **Gerekli değil** — kayıt, e-posta ile giriş veya telefon numarası yok |
| iHTC Studio tarafından veri toplama | **Veri Toplanmıyor** — kişisel verilerinizi alan bir arka uç işletmiyoruz |
| Ağ | Surname library, detail reading, recite, Study Hall, naming inspiration, widgets, and daily notifications work **offline** after install |
| Analitik / reklam / izleme | **Yok** — üçüncü taraf analitik, reklam veya izleme SDK'ları yok; Uygulama İzleme Şeffaflığı kullanılmaz |
| İsteğe bağlı Apple hizmetleri | **iCloud** (your private KVS), **Photo Library (Add Only)** for share cards, **StoreKit** for optional tipping, **local notifications**, optional **Live Activities**, optional **Spotlight** (off by default), optional **system speech / translation** |

## Veri Toplama

Kişisel bilgileri reklam veya analiz için **toplamıyoruz**, satmıyoruz veya paylaşmıyoruz.

- **Hesap gerekmez** — Tüm temel özellikleri bizde hesap oluşturmadan kullanabilirsiniz.
- **Analitik veya reklam yok** — Uygulama ikili dosyası üçüncü taraf analitik, reklam veya çökme bildirim SDK'larını içermez, telefonla bize veri göndermez.
- **İçerik yüklenmez** — favorites, surname lists, notes, reading history, study progress, streaks, naming preferences, and settings stay on your device (and optionally in **your** iCloud). They are never uploaded to iHTC Studio servers because **we do not run such servers for this app**.

## Uygulama Nasıl Çalışır

- **Paketlenmiş kitaplık** — Metin JSON, vernacular/English, dizinler ve çalışma yardımcıları uygulama/widget paketinin içindedir. Gezinme ve çalışma için ağ gerekmez.
- **Cihaz içi konuşma** — okuma Apple **AVSpeechSynthesizer**. Soyadı metni iHTC Studio’ya gönderilmez.
- **İsteğe bağlı sistem çevirisi** — Apple Translation; işlem Apple OS’te.
- **İsim ilhamı** — paket veriden tamamen cihazda. İsim veya tercih yüklenmez.
- **Widget'lar ve App Group** — Widget'lar ve uygulama, cihazınızdaki `group.com.iHTCboy.iBaiJia` App Group'u üzerinden tercihleri ve hafif durumu paylaşır.
- **Günlük bildirimler** — User Notifications ile yerel. Dokununca deep link; sunucu yok.
- **Kartları paylaş** — Görüntüler cihazda oluşturulur. Kaydetme, **Yalnızca Fotoğraf Kitaplığı eklentisini** yalnızca kaydet'e dokunduğunuzda kullanır. Sistem Paylaşım Sayfası, görüntüyü **seçtiğiniz** bir uygulamaya gönderebilir; o hedefin gizlilik politikası geçerli olur.
- **İsteğe bağlı bahşiş** — “Tip Developer” (`com.iHTCboy.iBaiJia.6`), Apple **StoreKit**.
- **Siri / Kısayollar / Kontrol Merkezi** — İsteğe bağlı sistem entegrasyonları cihazdaki derin bağlantıları açar; kütüphanenizi bize göndermiyorlar.
- **İsteğe bağlı Spotlight** — soyadları cihazda dizinlenir.
- **Geri bildirim e-postası** — yalnızca sorun giderme için yazdığınız metin ve cihaz/uygulama tanılaması (sürüm, OS, dil) içerebilir.

## Cihazınızda Saklanan Veriler

| Veri | Nerede | Amaç |
|------|-------|-------------|
| Soyadı DB ve vuruşlar | App paketi | Çevrimdışı, izleme, çalışma |
| Favoriler ve soyadı listeleri | App Group UserDefaults | Yıldızlı soyadları ve listeler |
| Notlar | App Group UserDefaults | Soyadı notları |
| Soyadım | App Group UserDefaults | Kişiselleştirilmiş ana ekran |
| Okuma geçmişi / son okuma | App Group UserDefaults | Gezinme, geçmiş UI |
| İlerleme ve skorlar | App Group UserDefaults | Study Hall durumu |
| Check-in serisi | App Group UserDefaults | Günlük alışkanlık |
| Görünüm ve okuma tercihleri ​​| Uygulama Grubu Kullanıcı Varsayılanları | Tema, aksan, dil, düzen, TTS, sekmeler, widget'lar |
| Daily Surname cache & notification prefs | App Group UserDefaults | Bugünün ID’si, schedule time |
| Paylaşım kartı tercihleri | App Group UserDefaults | Last style choices |
| İlk katılım ve TipKit durumu | Standart Kullanıcı Varsayılanları (cihaz) | Hoş geldiniz kılavuzu / keşif ipuçları |
| Ana Ekran hızlı eylemler | Sistem + yerel tercihler | Yapılandırdığınız kısayollar |
| Widget / Canlı Etkinlik anlık görüntüleri | Uygulama Grubu / ActivityKit | Daha önce açmış olduğunuz metni görüntüleyin |

Uygulamayı kaldırmak, uygulamayla ilişkili sandbox ve Uygulama Grubu verilerini kaldırır (iOS/macOS davranışına tabidir). İsteğe bağlı iCloud kopyaları, siz temizleyene veya senkronizasyonu kapatıp başka yerde silene kadar **iCloud’unuzda** kalır.

## iCloud Senkronizasyonu (İsteğe Bağlı)

Eğer Ayarlar’dan **iCloud Senkronizasyonu**’nu etkinleştirirseniz, uygulama seçili kullanıcı verilerini Apple’ın **`NSUbiquitousKeyValueStore`** aracılığıyla **Apple Kimliğinizle** eşler:

- Favoriler
- Soyadı listeleri
- Notlar
- Okuma geçmişi
- İlerleme / yüksek skorlar
- Check-in serileri
- İlgili tercihler

Senkronizasyon trafiği **Apple iCloud**’a gider, iHTC Studio’ya değil. Ayarlardan senkronizasyonu devre dışı bırakabilirsiniz. iCloud içeriğinizi okuyamayız.

## İzinler

iLiezi yalnızca bir özellik ihtiyaç duyduğunda izin ister:

| İzin | Ne zaman | neden |
|------------|------|-----|
| Bildirimler | Daily Surname reminders etkinleştirirsiniz | Yerel zamanlama |
## iCloud Senkronizasyonu (İsteğe Bağlı)
| iCloud | Senkronizasyonu açarsınız | Favoriler/listeler/geçmiş/ilerleme/seriler/notlar |
Ayarlar'da **iCloud Senkronizasyonu**'nu etkinleştirirseniz, uygulama seçili kullanıcı verilerini **Apple Kimliğinize** bağlı Apple'ın **`NSUbiquitousKeyValueStore`** hizmeti aracılığıyla yansıtır:
| Arka plan sesi (iOS) | Arka planda okuma | Arka planda TTS |

Kişiler, kesin Konum, Kamera, Mikrofon (sistem TTS oynatmanın ötesinde) veya İzleme **talebi etmeyiz**.

## Çocukların Gizliliği

iBaiJia, genel kitleye yönelik bir kültür öğrenme uygulamasıdır ve **Kids Category**’de değildir. Çocuklardan bilerek kişisel bilgi toplamayız. Uygulama hesap gerektirmez. Aileler kendi cihazlarında okuma ve çalışma özelliklerini çevrimdışı kullanabilir.

## Üçüncü Taraflar

Üçüncü taraf: **Apple**. Soyadı veri setleri CC BY 4.0, LGPL/Arphic (About).

## Veri Saklama ve Silme

- **Cihazda:** temizleme, Ayarlar’da dışa/içe aktarma. Uygulamayı silmek.
- **iCloud:** Ayarlar’da senkronizasyonu kapatın; iCloud depolamayı sistem Ayarları’ndan yönetin.
- **Kopya yok** — okuma, notlar, favoriler.

## Bu Politika ile İlgili Değişiklikler

Yasal, ürün veya App Store uyumluluğu nedenleriyle bu sayfayı güncelleyebiliriz. 「Son güncelleme」 tarihi değişir. Güncellemeden sonra kullanıma devam etmek, revize edilmiş politikayı kabul ettiğiniz anlamına gelir.

## İletişim

Gizlilik ile ilgili sorular: [AppleOSer@gmail.com](mailto:AppleOSer@gmail.com)
