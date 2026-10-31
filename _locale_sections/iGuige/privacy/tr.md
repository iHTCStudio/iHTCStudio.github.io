**Son güncelleme:** 19 Eylül 2026

iHTC Studio ("biz", "bize" veya "bizim") **iLiezi**yi (ayrıca "爱列子 / 愛列子" olarak da bilinir, Paket Kimliği `com.iHTCboy.iLiezi`) geliştirdi. Bu Gizlilik Politikası, uygulamayı kullandığınızda hangi verilerin işlendiğini (ve hangilerinin işlenmediğini) açıklar. **Apple Uygulama İncelemesi** ve kullanıcılar, **bu sayfaya** kamuya açık gizlilik politikası olarak güvenebilir. App Store Connect için, bu Gizlilik Politikasını tarayıcınızda açın ve adres çubuğundan adresi kopyalayın (kamuya açık site alan adı zamanla değişebilir).

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
- **İçerik yüklenmez** — Okuma geçmişi, favoriler, listeler, notlar, çalışma ilerlemesi ve tercihler cihazınızda (ve isteğe bağlı **iCloud’unuzda**) kalır. **Bu uygulama için böyle sunucular işletmediğimizden** iHTC Studio sunucularına yüklenmez.

## Uygulama Nasıl Çalışır

## Uygulama Nasıl Çalışır

- **Paketlenmiş kitaplık** — Metin JSON, yerel dil/İngilizce, dizinler ve çalışma yardımcıları uygulama/widget paketinin içinde gönderilir.
- **Cihaz içi konuşma** — Okuma, Apple'ın **AVSpeechSynthesizer** (TTS) sistemini kullanır. iHTC Studio'ya pasaj metni göndermiyoruz.
- **Widget'lar ve Uygulama Grubu** — Cihazınızdaki Uygulama Grubu `group.com.iHTCboy.iLiezi` aracılığıyla widget'lar ve uygulama paylaşım tercihleri.
- **Günlük bildirimler** — Yerel olarak planlanmıştır. Bir bildirime dokunduğunuzda cihazda derin bir bağlantı açılır.
- **Siri / Kısayollar / Kontrol Merkezi** — İsteğe bağlı sistem entegrasyonları cihazdaki derin bağlantıları açar; kütüphanenizi bize göndermiyorlar.
- **El yazısı araması (iOS)** — İsteğe bağlı karakter tanıma, cihazda Apple **Vision**'ı kullanır. Konturlar yüklenmedi.
- **İsteğe bağlı ipucu** — "İpucu Geliştirici", Apple tarafından gerçekleştirilen bir **StoreKit** sarf malzemesidir.
- **Siri / Kısayollar / Kontrol Merkezi** — İsteğe bağlı sistem entegrasyonları cihazdaki derin bağlantıları açar.
- **İsteğe Bağlı Spot Işığı** — Dizin oluşturmayı etkinleştirirseniz sistem, cihazdaki içeriği dizine ekler.

## Cihazınızda Saklanan Veriler

| Veri | Nerede | Amaç |
|------|-------|-------------|
| Çalışma ilerlemesi ve ustalık | Uygulama Grubu Kullanıcı Varsayılanları | Sınıf durumu, sınav / Arama ilerlemesi |
| Favoriler ve listeler | Uygulama Grubu Kullanıcı Varsayılanları | Yıldızlı öğeler ve kullanıcı listeleri |
| Okuma geçmişi / son okuma | Uygulama Grubu Kullanıcı Varsayılanları | Okumaya devam et |
| Notlar | Uygulama Grubu Kullanıcı Varsayılanları | Yazdığınız notları okuma |
| Çalışma ilerlemesi ve ustalık | Uygulama Grubu Kullanıcı Varsayılanları | Sınıf / Av ilerlemesi |
| Seri / giriş | Uygulama Grubu Kullanıcı Varsayılanları | Günlük alışkanlık |
| Görünüm ve okuma tercihleri ​​| Uygulama Grubu Kullanıcı Varsayılanları | Tema, dil, TTS, widget'lar |
| Widget / Canlı Etkinlik anlık görüntüleri | Uygulama Grubu / ActivityKit | Daha önce açmış olduğunuz metni görüntüleyin |
| Kart tercihleri ​​| Uygulama Grubu Kullanıcı Varsayılanları | Son stil / oran |
| İlk katılım ve TipKit durumu | Standart Kullanıcı Varsayılanları | Hoş geldiniz kılavuzu |
| Widget / Canlı Etkinlik anlık görüntüleri | Uygulama Grubu / ActivityKit | Daha önce açmış olduğunuz metni görüntüleyin |

Uygulamanın kaldırılması, korumalı alanı ve Uygulama Grubu verilerini kaldırır (işletim sistemi davranışına bağlıdır). İsteğe bağlı iCloud kopyaları, siz onları temizleyene kadar **iCloud'unuzda** kalır.

## iCloud Senkronizasyonu (İsteğe Bağlı)

Eğer Ayarlar’dan **iCloud Senkronizasyonu**’nu etkinleştirirseniz, uygulama seçili kullanıcı verilerini Apple’ın **`NSUbiquitousKeyValueStore`** aracılığıyla **Apple Kimliğinizle** eşler:

- Favoriler
- Listeler
- Okuma geçmişi
- Çalışma ilerlemesi / ustalık
- Pratik serileri
- Notlar

Senkronizasyon trafiği iHTC Studio'ya değil **Apple iCloud**'a gider. iCloud içeriklerinizi okuyamıyoruz.

## İzinler

iLiezi yalnızca bir özellik ihtiyaç duyduğunda izin ister:

| İzin | Ne zaman | neden |
|------------|------|-----|
| Canlı Etkinlikler (iOS) | Canlı Okuma Etkinliğini etkinleştirirsiniz | Okuduğunuz pasajı Kilit Ekranında / Dinamik Ada'da gösterin |
| Fotoğraf Kitaplığı (Yalnızca Ekle) | Bir kartı kaydedersiniz | İşlenen görüntüyü yazın |
| iCloud | Senkronizasyonu etkinleştirirsiniz | Favorileri / listeleri / geçmişi / ilerlemeyi / notları senkronize et |
| Canlı Etkinlikler (iOS) | Canlı Okuma Etkinliğini etkinleştirirsiniz | Pasajı Kilit Ekranında / Dinamik Adada göster |
| Arka planda ses (yetenek) | Arka planda okumayı etkinleştirirsiniz | Arka planda TTS'ye devam et |

Kişiler, kesin Konum, Kamera, Mikrofon (sistem TTS oynatmanın ötesinde) veya İzleme **talebi etmeyiz**.

## Ne Yapmıyoruz

- Kişisel verileri **satmıyoruz**.
- Reklam profilleri **oluşturmuyoruz**.
- Bir hesaba veya sosyal girişe **gerek duymayız**.
- Veri toplama amacıyla üçüncü taraf reklamları, analizleri veya sosyal SDK'ları **yerleştirmeyiz**.
- Bir kartı kaydetmeyi seçtiğinizde **yalnızca eklenti** dışında Fotoğraf Kitaplığınıza **erişmeyiz**.
- StoreKit ödeme kartı numaralarını **almıyoruz** (ödemeleri Apple işler).

## Çocukların Gizliliği

iLiezi genel kitleye yönelik bir eğitim okuryazarlığı uygulamasıdır ve Çocuk Kategorisinde **değildir**. Çocuklardan bilerek kişisel bilgi toplamıyoruz. Aileler okuma ve çalışma özelliklerini kendi cihazlarında çevrimdışı olarak kullanabilir.

## Üçüncü Taraflar

- **Apple** — App Store dağıtımı, isteğe bağlı StoreKit, isteğe bağlı iCloud KVS, sistem TTS, seçtiğiniz Paylaşım Sayfası hedefleri ve işletim sistemi düzeyinde bildirim / Canlı Etkinlik / Siri / Kısayollar / Vision dağıtımı.
- Reklam, analiz veya sosyal giriş için başka hiçbir üçüncü taraf SDK’sı veri toplama amacıyla dahil edilmemiştir.

## Uluslararası Kullanıcılar

Uygulama, cihazınızda çevrimdışı çalışacak şekilde tasarlanmıştır. İsteğe bağlı Apple hizmetleri Apple’ın şartlarına ve bölgesel kullanılabilirliğe tabidir.

## Veri Saklama ve Silme

- **Cihazda** — Yerel sandbox ve App Group verilerini kaldırmak için uygulamayı silin (işletim sistemi davranışına bağlıdır).
- **iCloud** — Senkronizasyonu kapatın ve gerekirse ilgili anahtarları iCloud hesabınızdan temizleyin; iCloud hesabınızı sizin için silemeyiz.
- **Hiçbir şeyi** iHTC Studio sunucularında bu uygulama için saklamıyoruz çünkü bunu toplamıyoruz.

## Politika Değişiklikleri

Bu Gizlilik Politikasını güncelleyebiliriz. Üstteki "Son güncelleme" tarihi değişecektir. Güncellemeden sonra devam eden kullanım, revize edilen politikayı kabul ettiğiniz anlamına gelir.

## İletişim

Gizlilik ile ilgili sorular: [AppleOSer@gmail.com](mailto:AppleOSer@gmail.com)
