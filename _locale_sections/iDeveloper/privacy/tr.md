**Son güncelleme:** 29 Temmuz 2026

iHTC Studio (“biz”, “bize” veya “bizim”), **iDeveloper**’ı (“爱开发者” / “愛開發者” olarak da bilinir, Bundle ID `com.iHTCboy.iDeveloper`) geliştirdi. Bu Gizlilik Politikası, uygulamayı kullandığınızda hangi verilerin işlendiğini (ve işlenmediğini) açıklar. **Apple App Review** ve kullanıcılar bu sayfayı herkese açık gizlilik URL’si olarak kullanabilir.

## Özet (Apple Gizlilik Besin Etiketi ile uyum)

| Konu | Uygulamamız |
|------|-------------|
| Hesap | **Gerekmez** |
| iHTC Studio tarafından veri toplama | **Veri Toplanmaz** — araç girdilerinizi veya kişisel verilerinizi alan bir arka uç **işletmiyoruz** |
| Ağ | Araçlar ve kopya kâğıtları varsayılan olarak **çevrimdışı** çalışır. Ağ özellikli araçlar yalnızca **siz** başlattığınızda istek gönderir |
| Analiz / reklam / izleme | **Yok** — üçüncü taraf analiz, reklam veya izleme SDK’sı yok |
| İsteğe bağlı Apple hizmetleri | **iCloud** (özel KVS’niz), **StoreKit** bahşişi, seçtiğiniz sistem Paylaş hedefleri, Apple tarafından sunulan widget’lar / Canlı Etkinlikler / Siri |

## Veri Toplama

Reklam veya analiz amacıyla kişisel bilgi toplamaz, satmaz veya paylaşmayız. Girdileriniz, çıktılarınız, favorileriniz, geçmişiniz ve snippet’leriniz cihazınızda (ve isteğe bağlı olarak **sizin** iCloud’unuzda) kalır. **Bu uygulama için bu tür sunucular işletmediğimizden** iHTC Studio sunucularına hiçbir zaman yüklenmezler.

## Uygulama Nasıl Çalışır

- **Gömülü araçlar ve referanslar** — Motorlar ve kopya kâğıdı JSON’u uygulama / widget / paylaşım uzantısı paketlerinin içinde gelir.
- **Cihaz üzerinde işleme** — Biçimlendirme, kodlama, kriptografi yardımcıları, regex ve çoğu yardımcı program yerel olarak çalışır.
- **İsteğe bağlı ağ** — Bir araç internete ihtiyaç duyarsa arayüz bir uyarı gösterir; istek yalnızca sizin eyleminizle başlatılır ve o aracın hedef sunucusuna gider — iHTC Studio proxy’si üzerinden değil.
- **Paylaş uzantısı** — Paylaşılan metin/veriler cihazınızda `group.com.iHTCboy.iDeveloper` App Group’u üzerinden aktarılır.
- **Widget’lar ve Canlı Etkinlik** — Daha önce açtığınız içeriklerin veya başlattığınız zamanlayıcıların anlık görüntülerini App Group / ActivityKit aracılığıyla gösterir.
- **İsteğe bağlı bahşiş** — Apple tarafından işlenen tüketilebilir **StoreKit** satın alımı.

## Cihazınızda Saklanan Veriler

| Veri | Amaç |
|------|------|
| Araç kataloğu ve referans kitaplığı | Çevrimdışı araçlar ve kopya kâğıtları |
| Favoriler / son araçlar | Hızlı erişim |
| İşlem geçmişi | Önceki girdi/çıktıları geri yükleme |
| Snippet’ler | Kaydettiğiniz yeniden kullanılabilir parçalar |
| Paylaşım gelen kutusu tamponları | Paylaş / Araca Gönder’den geçici aktarım |
| Görünüm ve tercihler | Tema, vurgu, dil, sekmeler, widget’lar |
| Odak / Canlı Etkinlik durumu | Zamanlayıcı gösterimi |
| Tanıtım ve puanlama istemleri | Karşılama / değerlendirme deneyimi |

## iCloud Eşitleme (İsteğe Bağlı)

Etkinleştirilirse seçili tercihler / iş akışı durumu, **Apple Kimliğinize** bağlı Apple’ın **`NSUbiquitousKeyValueStore`** hizmeti üzerinden eşitlenebilir. Eşitleme trafiği iHTC Studio’ya değil, **Apple iCloud**’a gider.

## İzinler

iDeveloper izinleri yalnızca bir özellik gerektirdiğinde ister (örneğin bir araç dışa aktardığınız görseli kaydediyorsa Fotoğraf Kitaplığı, ağ aracı çalıştırdığınızda ağ). Analiz için İzleme, Kişiler veya hassas Konum **istemeyiz**.

## İletişim

[AppleOSer@gmail.com](mailto:AppleOSer@gmail.com)
