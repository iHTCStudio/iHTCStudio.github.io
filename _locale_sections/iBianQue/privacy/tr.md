**Son güncelleme:** 19 Eylül 2026

iHTC Studio (“biz”, “bize” veya “bizim”) **iBianQue**’yi geliştirdi (aynı zamanda “爱扁鹊 / 愛扁鵲” olarak da bilinir, Paket Kimliği `com.iHTCboy.iBianQue`). Bu Gizlilik Politikası, uygulamayı kullandığınızda hangi verilerin işlendiğini (ve işlenmediğini) açıklar. **Apple App Review** ve kullanıcılar, **bu sayfayı** kamuya açık gizlilik politikası olarak kullanabilir. App Store Connect için bu Gizlilik Politikasını tarayıcınızda açın ve adres çubuğundan adresi kopyalayın (kamu sitesi alan adı zamanla değişebilir).

## Özet (Apple Gizlilik Beslenme Etiketi uyumu)

| Konu | Uygulamamızın uygulaması |
|-------|----------------|
| Hesap | **Gerekli değil** — kayıt, e-posta ile giriş veya telefon numarası yok |
| iHTC Studio tarafından veri toplanması | **Veri Toplanmıyor** — kişisel verilerinizi alan bir arka uç işletmiyoruz |
| Ağ | Kütüphane, okuma, ezberleme, Que Çalışma, widgetlar ve günlük bildirimler kurulumdan sonra **çevrimdışı** çalışır |
| Analitik / reklam / izleme | **Hiçbiri** — üçüncü taraf analitik, reklam veya izleme SDK'ları yok; App Tracking Transparency kullanılmıyor |
| İsteğe bağlı Apple hizmetleri | **iCloud** (özel KVS'niz), çalışma kartları için **Fotoğraf Kitaplığı (Sadece Ekleme)**, isteğe bağlı bahşişler için **StoreKit**, **yerel bildirimler**, isteğe bağlı **Canlı Aktiviteler**, cihazda isteğe bağlı **el yazısı** (Vision) |

## Veri Toplama

Kişisel bilgileri reklam veya analiz amacıyla **toplamıyoruz**, satmıyoruz veya paylaşmıyoruz.

- **Hesap gerekmiyor** — Tüm temel özellikleri bizimle hesap oluşturmadan kullanabilirsiniz.
- **Analitik veya reklam yok** — Uygulama ikili dosyası üçüncü taraf analitik, reklam veya arıza raporlama SDK'larını entegre etmez ve bize veri göndermez.
- **İçerik yükleme yok** — Okuma geçmişiniz, favorileriniz, listeleriniz, notlarınız, çalışma ilerlemeniz ve tercihlerinize cihazınızda (ve isteğe bağlı olarak **iCloud’unuzda**) kalır. Bunlar iHTC Studio sunucularına asla yüklenmez çünkü **bu uygulama için böyle sunucular işletmiyoruz**.

Dört Sınav sahnesi, meridyen atlası dokunuşları ve cihazdaki dil rengi taslağı yerel olarak kalır. Bunlar kültürel diyagramlardır. **Tanı, reçete veya HealthKit entegrasyonu değildir**.

## Uygulama Nasıl Çalışır

- **Paketlenmiş kitaplık** — Metin JSON, yerel dil/İngilizce, dizinler ve çalışma yardımcıları uygulama/widget paketinin içinde gönderilir. 
- **Cihaz içi konuşma** — Okuma, Apple'ın **AVSpeechSynthesizer** (TTS) sistemini kullanır. iHTC Studio'ya pasaj metni göndermiyoruz. 
- **Widget'lar ve Uygulama Grubu** — Cihazınızdaki Uygulama Grubu `group.com.iHTCboy.iBianQue` aracılığıyla widget'lar ve uygulama paylaşım tercihleri. 
- **Günlük bildirimler** — Yerel olarak planlanmıştır. Bir bildirime dokunduğunuzda cihazda derin bir bağlantı açılır. 
- **Çalışma kartları** — Görüntüler cihazda oluşturulur. Kaydetme, **Yalnızca Fotoğraf Kitaplığı eklentisini** yalnızca kaydet'e dokunduğunuzda kullanır. 
- **El yazısı araması (iOS)** — İsteğe bağlı karakter tanıma, cihazda Apple **Vision**'ı kullanır. Konturlar yüklenmedi. 
- **İsteğe bağlı ipucu** — "İpucu Geliştirici", Apple tarafından gerçekleştirilen bir **StoreKit** sarf malzemesidir. 
- **Siri / Kısayollar / Kontrol Merkezi** — İsteğe bağlı sistem entegrasyonları cihazdaki derin bağlantıları açar. 
- **İsteğe Bağlı Spot Işığı** — Dizin oluşturmayı etkinleştirirseniz sistem, cihazdaki içeriği dizine ekler. 

## Cihazınızda Saklanan Veriler

| Veri | Nerede | Amaç | 
|------|-------|-------------| 
| Bian Que / Nan Jing kütüphanesi | Uygulama / Widget paketi | Çevrimdışı okuma ve çalışma | 
| Favoriler ve listeler | Uygulama Grubu Kullanıcı Varsayılanları | Yıldızlı öğeler ve kullanıcı listeleri | 
| Okuma geçmişi / son okuma | Uygulama Grubu Kullanıcı Varsayılanları | Okumaya devam et | 
| Notlar | Uygulama Grubu Kullanıcı Varsayılanları | Yazdığınız notları okuma | 
| Çalışma ilerlemesi ve ustalık | Uygulama Grubu Kullanıcı Varsayılanları | Sınıf / Av ilerlemesi | 
| Seri / giriş | Uygulama Grubu Kullanıcı Varsayılanları | Günlük alışkanlık | 
| Görünüm ve okuma tercihleri ​​| Uygulama Grubu Kullanıcı Varsayılanları | Tema, dil, TTS, widget'lar | 
| Daily Art önbelleği ve bildirim tercihleri ​​| Uygulama Grubu Kullanıcı Varsayılanları | Bugünün kimliği ve programı | 
| Kart tercihleri ​​| Uygulama Grubu Kullanıcı Varsayılanları | Son stil / oran | 
| İlk katılım ve TipKit durumu | Standart Kullanıcı Varsayılanları | Hoş geldiniz kılavuzu | 
| Widget / Canlı Etkinlik anlık görüntüleri | Uygulama Grubu / ActivityKit | Daha önce açmış olduğunuz metni görüntüleyin | 

Uygulamanın kaldırılması, korumalı alanı ve Uygulama Grubu verilerini kaldırır (işletim sistemi davranışına bağlıdır). İsteğe bağlı iCloud kopyaları, siz onları temizleyene kadar **iCloud'unuzda** kalır. 

## iCloud Senkronizasyonu (İsteğe bağlı)

Ayarlar'da **iCloud Senkronizasyonu**'nu etkinleştirirseniz uygulama, seçilen kullanıcı verilerini Apple'ın **`NSUbiquitousKeyValueStore`_** aracılığıyla **Apple Kimliğinize** bağlı olarak yansıtır: 

- Favoriler 
- Listeler 
- Tarih okuma 
- Çalışma ilerlemesi / ustalığı 
- Seri antrenman yapın 
- Notlar 

Senkronizasyon trafiği iHTC Studio'ya değil **Apple iCloud**'a gider. iCloud içeriklerinizi okuyamıyoruz. 

## İzinler 

iBianQue yalnızca bir özellik ihtiyaç duyduğunda izin ister: 

| İzin | Ne zaman | Neden | 
|---------------|----------|-----| 
| Bildirimler | Günlük Sanat hatırlatıcılarını etkinleştirirsiniz | Yerel planlama | 
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

iBianQue, genel kitleye yönelik bir eğitim okuryazarlığı uygulamasıdır ve Çocuk Kategorisinde **değildir**. Çocuklardan bilerek kişisel bilgi toplamıyoruz. Aileler okuma ve çalışma özelliklerini kendi cihazlarında çevrimdışı olarak kullanabilir. 

## Üçüncü Taraflar 

- **Apple** — App Store dağıtımı, isteğe bağlı StoreKit, isteğe bağlı iCloud KVS, sistem TTS, seçtiğiniz Paylaşım Sayfası hedefleri ve işletim sistemi düzeyinde bildirim / Canlı Etkinlik / Siri / Kısayollar / Vision dağıtımı. 
- **Veri toplama amacıyla reklamlara, analizlere veya sosyal oturum açmaya yönelik başka hiçbir üçüncü taraf SDK'sı** dahil edilmemiştir. 

## Uluslararası Kullanıcılar 

Uygulama, cihazınızda çevrimdışı çalışacak şekilde tasarlanmıştır. İsteğe bağlı Apple hizmetleri, Apple'ın koşullarına ve bölgesel kullanılabilirliğe uygundur. 

## Veri Saklama ve Silme

- **Cihazda** — Yerel sandbox ve App Group verilerini kaldırmak için uygulamayı silin (işletim sistemi davranışına bağlıdır).
- **iCloud** — Senkronizasyonu kapatın ve gerekirse ilgili anahtarları iCloud hesabınızdan temizleyin; iCloud hesabınızı sizin için silemeyiz.
- **Hiçbir şeyi** iHTC Studio sunucularında bu uygulama için saklamıyoruz çünkü bunu toplamıyoruz.

## Politika Değişiklikleri

Bu Gizlilik Politikasını güncelleyebiliriz. Üstteki "Son güncelleme" tarihi değişecektir. Güncellemeden sonra devam eden kullanım, revize edilen politikayı kabul ettiğiniz anlamına gelir.

## İletişim

Gizlilik ile ilgili sorular: [AppleOSer@gmail.com](mailto:AppleOSer@gmail.com)
