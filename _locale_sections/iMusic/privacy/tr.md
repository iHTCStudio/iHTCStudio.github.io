**Son güncelleme:** 9 Eylül 2026

iHTC Studio («biz») **iMusic** («爱音乐» / «愛音樂», Bundle ID `com.iHTCboy.iMusic`) uygulamasını geliştirdi. Bu sayfa, uygulama ve widget uzantısı kullanılırken hangi verilerin işlendiğini (ve işlenmediğini) açıklar. **Apple App Review** ve kullanıcılar bunu herkese açık gizlilik politikası olarak kullanabilir. App Store Connect: [Privacy Policy](../privacy) sayfasını tarayıcıda açıp URL'yi kopyalayın (alan adı değişebilir).

## Özet (Apple Privacy Nutrition Label)

| Konu | Uygulamamız |
|-------|----------------|
| Hesap | **Gerekmez** — kayıt, e-posta, telefon yok |
| iHTC Studio veri toplama | **Data Not Collected** — kişisel veri alan backend **yok** |
| Ağ | **Rehberler** kurulumdan sonra **çevrimdışı**; **oynatma** ve **şarkı tanıma** izin sonrası Apple |
| Analitik/reklam/izleme | **Yok** — üçüncü taraf analytics/reklam/tracking SDK yok; ATT yok |
| İsteğe bağlı Apple | **Apple Music/MusicKit**, **ShazamKit**, **iCloud** (private KVS), paylaşım kartları için **Fotoğraflar (yalnızca ekleme)**, **StoreKit** bahşiş, **yerel bildirimler**, **Live Activities** |

## Veri toplama

Reklam veya analiz için kişisel veri **toplamıyor**, satmıyor veya paylaşmıyoruz.

- **Hesap yok** — iHTC Studio hesabı olmadan tüm rehberler.
- **Analitik/reklam yok** — bizi arayan üçüncü taraf SDK yok.
- **Rehber yükleme yok** — favoriler, listeler, notlar, geçmiş, ayarlar cihazda (isteğe bağlı **sizin** iCloud); iHTC Studio sunucularına gitmez (**böyle bir backend yok**).
- **Müzik barındırma yok** — tam ses dosyası yok; eşleşen oynatma **Apple Music**; abonelik yoksa **30 sn önizleme** önbelleği.

## Uygulama nasıl çalışır

- **Gömülü kütüphane** — dizin, rehberler, sanatçı notları, kategoriler, koleksiyonlar, bundle içinde; rehberler çevrimdışı.
- **Apple Music (MusicKit)** — ISRC öncelikli eşleme ve Apple oynatıcı; abonelik durumu Apple'a sorulur.
- **30 sn önizleme** — `Caches`; hücresel/düşük güç modunda sonraki önizleme önceden yüklenmez.
- **ShazamKit** — yalnızca Recognize açıkken; mikrofon **Apple** tarafından işlenir.
- **Cihaz içi konuşma** — **AVSpeechSynthesizer**; metin iHTC Studio'ya gitmez.
- **Widget & App Group** — `group.com.iHTCboy.iMusic`
- **Günlük bildirimler** — yerel zamanlama.
- **Paylaşım kartları** — cihazda render; **yalnızca ekleme**.

## Cihazda saklanan veriler

Favoriler, listeler, notlar, geçmiş, streak, ayarlar, Daily Piece önbelleği, artwork URL'leri, 30 sn dosyaları, Live Activity küçük resmi — App Group / bundle / Caches (JA/EN tablosuyla aynı kapsam).

Kaldırma sandbox ve App Group'u siler; isteğe bağlı iCloud **sizin** iCloud'unuzda kalır.

## iCloud (isteğe bağlı)

**iCloud Sync** açıkken **`NSUbiquitousKeyValueStore`** favoriler, listeler, notlar, geçmiş, streak yansıtır; rehber metni zaten bundle'da; artwork/önizleme KVS ile senkronize edilmez.

## İzinler

Apple Music, mikrofon, bildirimler, Fotoğraflar (ekleme), iCloud, Live Activities, arka plan sesi — yalnızca ilgili özellik açıkken. Kişiler, hassas konum, kamera, tracking **yok**.

## Yapmadıklarımız

Veri satışı yok; zorunlu hesap yok; veri toplama SDK'sı yok; tam parça sunucuda yok; Shazam tamponu saklanmaz; **müzik çalma** için özel Dynamic Island yok — yalnızca rehber okuma.

## Çocuklar / üçüncü taraflar / uluslararası / silme

Kasıtlı çocuk verisi yok; veri toplama backend'i yok. **Apple** hizmet sağlayıcı. Önbellek **Ayarlar → Depolama**'dan silinir.

## Değişiklikler

Politika güncellenebilir; üstteki tarih değişir.

## İletişim

- **E-posta:** [AppleOSer@gmail.com](mailto:AppleOSer@gmail.com)

Genelde 48 saat içinde yanıt.
