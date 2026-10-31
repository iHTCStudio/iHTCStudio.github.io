iHTC Studio («biz»; eski adı iHTCTeam) **iVeil** uygulamasını geliştirir (爱修图 / 愛修圖; önceki sürümler iPhoto adını taşıyordu). Bu politika, uygulamayı ve Paylaş uzantısını, Fotoğraflar düzenleme uzantısını, widget’ları, Denetim Merkezi denetimlerini ve Kilit Ekranı kamerasını kullandığınızda verilerinize ne olduğunu açıklar.

*Son güncelleme: 18 Ekim 2026*

## Özet

- **Hesap yok, reklam yok, analiz yok, izleme yok.** iVeil’de üçüncü taraf analiz, reklam veya izleme SDK’sı yoktur.
- **Fotoğraflarınız ve videolarınız iVeil üzerinden cihazınızdan çıkmaz.** Algılama, düzenleme ve dışa aktarma cihazınızda çalışır. İçeriğinizi alan sunucularımız yoktur.
- **Neyin paylaşılacağına siz karar verirsiniz.** iVeil yeni kopyalar oluşturur. Fotoğraflar’daki özgünleriniz yalnızca Fotoğraflar düzenleme uzantısıyla bir düzenlemeyi kaydettiğinizde değişir ve bu düzenleme Fotoğraflar’da geri alınabilir.

## iVeil’in cihazınızda işlediği veriler

| Veri | Neden | Ne saklanır |
|------|-----|--------------|
| Seçtiğiniz fotoğraflar ve videolar (Fotoğraflar, Paylaş menüsü, Dosyalar veya kamera) | Kontrol etmek, gizlemek ve düzenlemek için | Siz silene kadar uygulama kum havuzunda saklanır. Paylaş uzantısından gelen fotoğraflar kısa süre App Group kabından geçer, sonra uygulamaya taşınır. |
| Yüzler ve kişiler (Apple Vision) | Yüzleri bulup gizlemek, seçtiğiniz kişileri tutmak, emoji örtüsünü başın eğimine uydurmak, tuttuğunuz kişiyi kesmek ve isteğe bağlı portre rötuşu | Gizlemelerinizi yeniden çizmek için gereken dikdörtgenler veya dış çizgiler projeyle birlikte saklanır. Yüz işaret noktaları yalnızca bellekte kalır. |
| Görüntülerdeki metin (Vision metin tanıma ve Apple veri algılayıcıları) | Telefon numaralarını, e-postaları, adresleri, kart ve kimlik numaralarını, pasaport satırlarını, sipariş numaralarını, hesap kimliklerini ve bağlantıları bulmak için | Yalnızca alan ve tür saklanır. Tanınan metnin kendisi saklanmaz. |
| QR kodları ve barkodlar | Onları gizlemek ve «Kodun içinde ne var» ile ne tür bilgi taşıdıklarını söylemek için | Yalnızca kategori ve alan adları saklanır (örneğin «biniş kartı: koltuk»), içerik asla saklanmaz. |
| Dosya ayrıntıları (konum, çekim zamanı, kamera, lens, seri numaraları) | Bir dosyanın ne açığa çıkardığını göstermek ve paylaştığınız kopyalardan kaldırmak için | Dosyanızdan okunur. Kopyalar yalnızca sizin seçtiklerinizi tutar; seri numaraları ve sahip adları her zaman kaldırılır. |
| Hassas olabilecek görüntüler (Apple Hassas İçerik Analizi) | Ayarlar’da Hassas İçerik Uyarısı veya İletişim Güvenliği açıksa, paylaşmadan önce çıplaklığı veya rahatsız edici içeriği bulandırmak için | Analiz, Apple’ın çerçevesi içinde cihazda çalışır. Sonuçlar saklanmaz ve gönderilmez. |
| Apple Intelligence (isteğe bağlı, iOS 26) | «Apple Intelligence ile yeniden bak» ve «Bir görünümü tanımla» | Apple’ın cihazdaki modelinde çalışır. Yalnızca tanınan metin satırlarını ve sayılarını ya da yazdığınız cümleyi alır; görüntü veya yüz verisi almaz. |
| Görünmez İşaret (isteğe bağlı) | Bir fotoğrafı daha sonra kime gönderdiğinizi kontrol etmek için | 32 bitlik bir kod görüntünün parlaklığına gizlenir. Girdiğiniz alıcı adları cihazınızdaki bir listede kalır (en fazla 500 kayıt). Ayarlar → Görünmez İşaret bölümünden düzenlenebilir veya temizlenebilir. |
| Kesmeler ve Genmoji örtüleri | Kesilen kişileri ve özel emojiyi yeniden kullanmak için | Siz kaldırana kadar cihazınızdaki App Group kabında görüntü olarak saklanır. |
| Son Silinenler | Bir silmeyi geri almak için | Silinen projeler 30 gün tutulur, sonra kalıcı olarak kaldırılır. |
| Tercihler | Dil, görünüm, çekim ve dışa aktarma seçenekleri | Cihazınızdaki App Group kabında saklanır. |

## Yüz verisi

iVeil, yüzleri ve kişileri **konumlandırmak** için cihazınızdaki Apple Vision çerçevesini kullanır. Bu yüz tanıma **değildir:** iVeil kim olduğunu belirlemez, yüzleri karşılaştırmaz ve biyometrik şablon oluşturmaz.

- **Kullanım:** yüzleri gizlemek, seçtiğiniz kişileri tutmak, emoji örtülerini hizalamak, tuttuğunuz kişiyi kesmek ve isteğe bağlı portre rötuşu.
- **Saklama:** normalleştirilmiş yüz dikdörtgenleri, kişi dış çizgileri ve rötuş ayarlarınız uygulama kum havuzundaki projenin içinde saklanır. Tam yüz işaret noktaları diske yazılmaz.
- **Paylaşım:** yüz verisi yüklenmez, bize veya üçüncü taraflara verilmez ve iCloud ile eşitlenmez.
- **Saklama süresi:** yüz verisi yalnızca proje durduğu sürece kalır. Bir projeyi silmek (Son Silinenler’de 30 gün sonra) veya uygulamayı kaldırmak onu siler.

## Ağ kullanımı

iVeil’in kendi sunucusu yoktur. Ağ istekleri yalnızca Apple hizmetlerinden gelir:

- **Haritalar.** Bir fotoğrafın konumu varsa iVeil onu bir Apple Haritası üzerinde gösterir; harita o bölgenin karolarını Apple’dan yükler. **Kabaca konum** seçildiğinde yer adı, tam koordinatlar yerine yaklaşık 5 km’lik bir ızgara hücresinin merkezinden Apple’a sorulur. Görüntü içeriği gönderilmez. Apple bu istekleri [Apple’ın Gizlilik İlkesi](https://www.apple.com/legal/privacy/) kapsamında işler.
- **İsteğe bağlı bahşiş.** «Geliştiriciye bahşiş», Apple’ın StoreKit ile işlediği tüketilebilir bir uygulama içi satın almadır. Hiçbir şeyin kilidini açmaz ve biz kişisel bilgi almayız.
- **İsteğe bağlı iCloud eşitlemesi (varsayılan olarak kapalı).** Açtığınızda dil, görünüm ve çekim veya dışa aktarma seçenekleri gibi birkaç tercih, özel iCloud anahtar-değer deponuz üzerinden eşitlenir. Fotoğraflar, videolar, yüz verisi ve Görünmez İşaret listesi asla eşitlenmez.

## İzinler

| İzin | Amaç |
|------------|---------|
| Fotoğraflar | Seçtiğiniz fotoğrafları açmak ve konum ile kamera ayrıntılarını göstermek |
| Fotoğraflar (yalnızca ekleme) | Dışa aktardığınız kopyaları kaydetmek |
| Kamera | Çekim sekmesi, Canlı Örtü ve Kilit Ekranındaki Örtü Kamerası |

iVeil mikrofon, konum, kişiler veya izleme izni istemez. Video Örtüsü, seçtiğiniz videoda zaten bulunan sesi kullanır ve onu kaldırabilir.

## Arka plan işi ve Canlı Etkinlikler

**Sizin başlattığınız** toplu Güvenli Paylaşım ve Video Örtüsü dışa aktarmaları kısa süre arka planda sürebilir. Bir Canlı Etkinlik, Kilit Ekranında işin adını ve ilerlemesini gösterebilir. Görüntü içeriğini asla göstermez.

## Çocuklar

İçerik cihazda işlendiği ve veri toplayan bir arka ucumuz olmadığı için iVeil, çocuklar dahil hiç kimseden bilerek kişisel veri toplamaz.

## Sorumluluk reddi

iVeil bağımsız bir uygulamadır ve **Apple Inc. ile bağlantılı değildir.** Otomatik algılama bir ilk geçiştir, garanti değildir. Paylaşmadan önce fotoğrafa bir kez daha bakın.

## Değişiklikler

Uygulamamız değişirse bu sayfayı günceller ve yukarıdaki tarihi yenileriz.

## İletişim

- **E-posta:** [AppleOSer@gmail.com](mailto:AppleOSer@gmail.com)
