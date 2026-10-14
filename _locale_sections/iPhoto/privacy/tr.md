iHTC Studio ("biz", "bize" veya "bizim") iPhoto'yu ("爱修图" / "愛修圖" olarak da bilinir) oluşturdu. Bu sayfada, uygulamayı kullandığınızda elde edilen verilere ilişkin politikalarımız açıklanmaktadır.

## Özet

**iPhoto bir hesap gerektirmez ve fotoğraflarınızı iHTC Studio sunucularına yüklemez.** Fotoğraf çekme, güzellik, filtreler ve dışa aktarma işlemleri cihazınızda çalışır. İsteğe bağlı **iCloud senkronizasyonu** yalnızca tercihleri ​​kapsar; fotoğraf dosyalarını kapsamaz.

## Veri Toplama

Kişisel bilgilerinizi toplayan bir arka uç işletmiyoruz:

- **Hesap yok** — Kayıt, e-posta veya telefon numarası gerekmez.
- **Analiz veya reklam yok** — Üçüncü taraf analiz, reklam veya izleme SDK'sı yok.
- **Analiz için fotoğraf yükleme yok** — Yüz önemli noktaları ve görüntüleme cihazda kalır.

## Uygulama Nasıl Çalışır?

- **Depolama** — Projeler (orijinal / küçük resim / düzenleme durumu) uygulama sanal alanında yayınlanır. Widget küçük resimleri Uygulama Grubu kapsayıcısını kullanır.
- **Yüz güzelliği** — Aşağıdaki **Yüz Verileri ve Cihaz Üzerinde Güzellik İşleme** konusuna bakın.
- **Fotoğraf Kitaplığı** — Erişim, seçtiğiniz içe aktarma işlemleriyle sınırlıdır ve isteğe bağlı dışa aktarma, başlattığınız kayıtları kaydeder.
- **Meta veri şeridi** — İsteğe bağlı olarak EXIF ​​/ GPS / cihaz alanlarını oluşturduğunuz dışa aktarmalardan kaldırır.

## Yüz Verileri ve Cihaz Üzerinde Güzellik İşleme

When you use beauty features (Capture live preview, shutter bake, or the editor Beauty tool), iPhoto analyzes faces **only on your device** using Apple’s Vision framework (`VNDetectFaceLandmarksRequest`). This is **not** face recognition, identity matching, biometrics enrollment, or authentication.

### Hangi yüz verileri işleniyor?

- **Geçici yer işaretleri (yalnızca bellek):** yüz sınırlayıcı kutu, yüz çevresi, gözler, kaşlar, dış/iç dudaklar, gözbebekleri ve isteğe bağlı kozmetik düzenlemelere (pürüzsüzleştirme, beyazlatma, inceltme, gözler, dişler, allık, ruj) yönelik maskeler oluşturmak için kullanılan ilgili geometri.
- **Bir projede ısrar edildi (isteğe bağlı):** **normalleştirilmiş yüz sınırlayıcı dikdörtgen** artı seçtiğiniz **güzellik gücü / renk parametreleri** (`FaceBeautyEdit`), böylece projeyi yeniden açtığınızda yüze özel ayarlar geri yüklenebilir. **Tam yer işareti koordinatları diske yazılmaz.**

### Kullanım

Yüz geometrisi yalnızca çekim önizlemesi, fotoğraf çekimi, düzenleyici önizlemesi, küçük resim yenileme ve dışa aktarma/paylaşma sırasında **sizin** etkinleştirdiğiniz güzellik ayarlarını uygulamak için kullanılır. Reklam, profil oluşturma veya tanımlama amacıyla kullanılmaz.

### Paylaşma

**Yüz verileri hiçbir zaman üçüncü taraflarla paylaşılmaz.** iHTC Studio sunucularına veya herhangi bir bulut analiz API'sine yüklenmez. İsteğe bağlı iCloud Anahtar-Değer senkronizasyonu **yalnızca tercihleri** kapsar (örneğin dil, tema, güzellik tarifi yakalama geçişleri) ve **fotoğrafları veya yüz yer işaretlerini senkronize etmez**.

### Depolama yeri

- Fotoğraflar ve proje düzenleme dosyaları: **cihazınızdaki uygulama sanal alanı**
- Geçici yer işaretleri: **Yalnızca RAM** (düzenleyiciden çıktığınızda temizlenir / analiz önbelleğini temizler)
- Widget küçük resimleri: Cihazınızdaki Uygulama Grubu (işlenen görüntüler, yer işareti veri kümeleri değil)

### Saklama ve silme

- Geçici yer işaretleri yalnızca işlem sırasında bulunur ve daha sonra atılır.
- Kalıcı yüz kutuları ve güzellik parametreleri **yalnızca ilgili fotoğraf projesini sakladığınızda** kalır.
- İlgili yüz meta verilerini ve yerel fotoğrafları kaldırmak için bir projeyi **silin**, düzenlemeleri **sıfırlayın** veya uygulamayı **kaldırın**.

### Üçüncü taraflar

Yok. Tüm yüz analizi ve görüntüleme, cihazdaki Apple Vision ve Core Image'ı kullanır.

## Cihazınızda Saklanan Veriler

| Veri | Nerede | Amaç |
|------|-------|---------|
| Fotoğraf projeleri | Uygulama Belgeleri | Orijinaller, başparmaklar, düzenleme durumu |
| Yüz güzelliği meta verilerini düzenleme | Proje düzenleme durumu (korumalı alan) | Normalleştirilmiş yüz kutusu + yalnızca güzellik parametreleri |
| Tercihler | Uygulama Grubu Kullanıcı Varsayılanları | Dil, tema, yakalama/dışa aktarma seçenekleri |
| Widget anlık görüntüleri | Uygulama Grubu | Widget'lar için son projeler / istatistikler |
| Güzellik tarifini yakalayın | Uygulama Grubu (isteğe bağlı hatırlayın) | Güç ve güzellik parametreleri |
| iCloud tercihleri | Özel iCloud KVS'niz | İsteğe bağlı tercih senkronizasyonu |

## iCloud Senkronizasyonu

Optional sync uses Apple's `NSUbiquitousKeyValueStore` for lightweight preferences (appearance, language, export defaults, capture beauty settings, and similar). **Photo files and face landmarks are not synced.** Sync can be turned off in Settings.

## İzinler

| İzin | Amaç |
|------------|---------|
| Kamera | Yakalama sekmesi |
| Fotoğraf Kitaplığı (oku) | İthalat |
| Fotoğraf Kitaplığı (yalnızca ekleme) | İsteğe bağlı olarak Fotoğraflar'a aktarma |
| Mikrofon | Sesli video kaydederken isteğe bağlı ses; fotoğraf çekimi bunu gerektirmez |

## Uygulama İçi Satın Alımlar

İsteğe bağlı **İpucu Geliştirici**, bir StoreKit sarf malzemesi satın alımıdır. Özelliklerin kilidini açmaz ve ayrı bir uygulama hesabı gerektirmez.

## Çocukların Gizliliği

iPhoto bilerek çocuklardan kişisel veri toplamaz. Çekirdek işleme, iHTC Studio veri toplama arka ucu olmadan cihazda kalır.

## Sorumluluk reddi beyanı

iPhoto **Apple Inc.'e bağlı değildir**

## Değişiklikler

Bu politikayı bu sayfada güncelleyebiliriz. Lütfen periyodik olarak gözden geçirin.

## İletişim

- **E-posta:** [AppleOSer@gmail.com](mailto:AppleOSer@gmail.com)
