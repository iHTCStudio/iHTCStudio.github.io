### iAppManager nedir?

iPhone, iPad ve Mac için **yerel App Store Connect çalışma istasyonu**. **API Key** ile oturum açın; sürümler, ekran görüntüleri, IAP, TestFlight, sertifikalar, raporlar ve yorumlar — trafik **doğrudan Apple'a**. iHTC Studio hesabı gerekmez.

### API Key nasıl alınır?

1. [App Store Connect](https://appstoreconnect.apple.com) → **Users and Access** → **Integrations** → **App Store Connect API**
2. Anahtar oluşturun (Admin veya App Manager önerilir)
3. `.p8` dosyasını **bir kez** indirin; **Issuer ID** ve **Key ID**'yi not edin
4. iAppManager'a yapıştırın (veya dosyayı seçin). Uygulama içi rehber ekran görüntüleriyle adım adım anlatır.

### `.p8` iHTC Studio'ya yüklenir mi?

**Hayır.** Özel anahtar yalnızca **cihaz Keychain**'inde kalır. İstekler yerelde imzalanır ve `api.appstoreconnect.apple.com`'a gider. Hesabı kaldırmak yerel anahtarı siler.

### Uygulama içinde Apple ID parolası gerekir mi?

**Hayır.** Kimlik doğrulama **yalnızca API Key** (Issuer ID + Key ID + `.p8`). Herkese açık API olmayan özellikler (ör. privacy nutrition labels, ücretsiz uygulama promosyon kodları) için uygulama Apple sitesini açar — Apple ID'yi Safari/ASC tarafında kullanırsınız.

### Transporter olmadan IPA / PKG yüklenebilir mi?

**Evet.** iAppManager Apple **Build Upload REST** (WWDC25) kullanır. Büyük dosyalar için **Mac** tercih edin; iOS aynı API'yi destekler ama büyük yüklemeler zor.

### Filtreler / widget'larda "on sale" ne demek?

**En az bir App Store bölgesinde kullanılabilir.** Pipeline kovaları (waiting / in review / rejected / pending developer release) ayrı izlenir. Widget **Needs attention** = waiting + in review + rejected + pending release (yerel toplam, ASC alanı değil).

### Gönderimden önce hard vs soft kontroller?

**Hard blockers** gönderimi durdurur (ör. build hazır değil, demo hesap gerekli ama yok). **Soft checks** uyarır (ana ekran görüntüsü boyutu, telif, yaş derecesi vb.) — onaylayıp devam edebilirsiniz. Overview / Versions / Submissions `?` veya `iappmanager://release-guide`.

### Hangi diller?

**English · 简体中文 · 繁體中文** — sistemi izleyin veya Ayarlar'da zorlayın. Dil hot-swap **kökü yeniden mount etmeden** (gezinme ve taslaklar kalır).

### Widget'lar neden canlı ASC sayılarını göstermiyor?

Widget'lar **ASC'yi çağırmaz**. Ana uygulama tarar ve anlık görüntü yazar (~10 dk TTL, My Apps ile aynı kovalar). Uygulamayı açıp listeyi yenileyin (veya durumu zorla yenileyin).

### macOS vs iOS?

Her ikisi de mağaza, monetizasyon, TestFlight, Game Center, kullanıcılar, raporlar, yorumlar, Webhooks. **Büyük IPA** ve sertifikaları sistem Keychain'e kurma — **Mac** tercih. Alternatif uygulama simgeleri **yalnızca iOS**.

### App Store Connect gizlilik politikası URL'si?

Bu sitenin [Privacy Policy](../privacy) sayfasını açıp tarayıcı adres çubuğundan URL'yi kopyalayın.

### Sistem gereksinimleri?

iPhone / iPad **iOS 17.0+**, Mac **macOS 14.0+**.

### Destek?

[AppleOSer@gmail.com](mailto:AppleOSer@gmail.com) — genelde 48 saat içinde.
