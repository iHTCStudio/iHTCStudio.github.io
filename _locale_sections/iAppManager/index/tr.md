**Daha hızlı yayınlayın. Tarayıcı labirentinden çıkın.**

iAppManager (爱应用者), iPhone, iPad ve Mac için **yerel bir App Store Connect istasyonudur**. **API Key** ile oturum açın, kimlik bilgilerini **Keychain**'de tutun ve **doğrudan Apple** ile konuşun — sürümler, ekran görüntüleri, IAP, TestFlight, sertifikalar, satış raporları ve müşteri yorumları tek yerde. **iHTC Studio hesabı yok. Reklam yok. Analytics SDK yok. ASC verileriniz için üçüncü taraf backend yok.**

**Özet:** çoklu hesap API Key · platform ve pipeline filtreli uygulama listesi · Overview hazırlık kontrol listesi · sürümler ve review gönderimleri · Build Upload REST (IPA/PKG) · cross-locale kopyalı metadata ve medya · Custom Product Pages · In-App Events · App Clips · store deneyleri · featuring adaylıkları · availability ve fiyatlandırma · yaş derecelendirmesi · erişilebilirlik · App Tags · IAP ve abonelikler · Game Center · TestFlight · müşteri yorumları · sertifikalar ve cihazlar · kullanıcılar ve roller · sales / finance / Analytics raporları · Webhooks · widget'lar ve `iappmanager://` deep link'leri · English / 简体 / 繁體

> Her hafta App Store Connect'te yaşayan indie geliştiriciler ve küçük ekipler için — sekme çiftliği değil, Mac uygulaması gibi bir masa.

## Başlarken

1. **App Store Connect API Key** oluşturun (Admin veya App Manager önerilir): App Store Connect → **Users and Access** → **Integrations** → **App Store Connect API** → anahtar oluşturun, **`.p8`'i bir kez** indirin, **Issuer ID** + **Key ID** not edin.
2. iAppManager'ı açın → Issuer ID / Key ID / PEM yapıştırın (veya `.p8` seçin) → doğrulayın (`GET /v1/apps`). Anahtarlar bu cihazın **Keychain**'inde saklanır.
3. Kısa **onboarding**'i bitirin (sertifikalar · raporlar · widget'lar · gizlilik). **Ayarlar → Yardım**'dan rehberleri tekrarlayın.
4. **My Apps**'te **liste / ızgara / kartlar**, favorileri sabitleyin, **platform** (iOS / macOS / tvOS / visionOS) veya **durum** (satışta · satış dışı · bekliyor · incelemede · reddedildi · geliştirici release bekliyor) filtreleyin.
5. Uygulamayı açın → **Overview**'dan başlayın (son sürüm/build, kısayollar, yumuşak kontrol listesi, son gönderimler).
6. Release yolu: **Versions** → **Build** ekle → **Metadata / Media** → **Review Detail** → **Review Submissions** ile gönderin (veya "hemen gönder").
7. **Ana Ekran widget'ları** ekleyin (Account Hub, Apps Pulse, Review Desk, Quick Actions) ve Shortcuts'tan `iappmanager://` deneyin.

> Uygulama içi **Release / IAP / TestFlight / Reports** rehberleri bir dokunuşta (deep link'ler de).

## Neden indirmelisiniz

- **Tüm yayın için tek yerel masa** — sürümler, varlıklar, IAP, TestFlight, sertifikalar ve raporlar için ASC web sekmeleri arasında zıplamayı bırakın.
- **API Key, başka bir parola dansı değil** — Issuer ID + Key ID + `.p8` Keychain'de; çoklu hesap; hesap kaldırma yerel anahtarı siler.
- **Transporter olmadan build yükleme** — WWDC25 **Build Upload REST** IPA/PKG için; iOS'ta aynı pipeline (büyük dosyalar Mac'te).
- **Uygulama içi ayrıntılı rehberler** — release hazırlığı, IAP, TestFlight ve raporlar hard vs soft kontrolleri açıklar.
- **Kilit Ekranı'nda pipeline** — widget'lar satışta / bekliyor / incelemede / reddedildi / release bekliyor sayılarını yansıtır.
- **Mimariyle gizlilik** — ASC trafiği `api.appstoreconnect.apple.com`; iHTC Studio uygulamalarınızı, anahtarlarınızı veya raporlarınızı barındırmaz.

## Özellikler

### Oturum ve hesaplar

- **Yalnızca API Key** (Issuer ID / Key ID / `.p8`) — uygulama içi Apple ID OAuth yok
- Keychain; **çoklu hesap**; çıkış / kaldırma yerel gizli anahtarı siler
- Uygulama içi **"API Key nasıl alınır"** rehberi

### My Apps

- **Liste / ızgara / kartlar** (varsayılan liste) sütun kontrolleri
- Hesap başına **sabitleme**; **platform** ve **durum** filtreleri ~10 dk önbellek
- **Satışta = en az bir bölgede kullanılabilir**
- Bağlam menüsü: sabitle, modüllere atla, kopyala; App Store veya ASC aç
- İkonlar: ASC build artwork → iTunes Lookup → monogram

### Overview ve release hazırlığı

- Son sürüm/build özeti, modül kısayolları, son review gönderimleri
- **Yumuşak kontrol listesi**
- **Sert blockers** Versions / Submissions'ta
- Rehber: `iappmanager://release-guide`

### Sürümler, build'ler ve gönderimler

- Sürüm oluşturma, build ekleme, gönder / iptal, release modları, **Release Now**
- **Build Upload REST**, Background Assets, encryption declarations
- **Review Submissions** ve **Review Detail**

### Store listesi ve büyüme

- **Metadata**, screenshots, batch assets, download-size workbench
- **Custom Product Pages**, In-App Events, App Clips, store experiments, featuring
- **Availability**, **pricing**, age rating, accessibility, App Tags
- Mac'te **⌘S** kaydet

### Monetizasyon ve Game Center

- IAP / abonelik grupları, teklifler, CSV
- Rehber: `iappmanager://iap-guide`
- **Game Center**

### TestFlight

- Gruplar, public link'ler, metrikler, feedback export
- Rehber: `iappmanager://testflight-guide`

### Sertifikalar, kullanıcılar, raporlar, yorumlar

- Certificates, profiles, devices, reports, customer reviews, webhooks
- Rehber: `iappmanager://reports-guide`

### Widget'lar ve kısayollar

- Account Hub, Apps Pulse, Review Desk, Quick Actions
- `iappmanager://` — [Shortcut Links](url-scheme)

### Gizlilik

- API sırları **Keychain**'de; yalnızca **Apple**'a çağrılar
- Ayrıntılar: [Privacy Policy](privacy)

## Uygulamayı edinin

| Kanal | Bağlantı |
|-------|----------|
| App Store | [Download on the App Store](https://apps.apple.com/app/id6794497110) |

## Sistem gereksinimleri

| Bileşen | Minimum |
|---------|---------|
| iPhone / iPad | iOS 17.0+ |
| Mac | macOS 14.0+ |
| Widget'lar | iOS 17.0+ |
| Büyük IPA | **Mac** önerilir |

## İletişim

- **E-posta:** [AppleOSer@gmail.com](mailto:AppleOSer@gmail.com)

Genelde 48 saat içinde yanıt veririz.

[FAQ](faq) · [Shortcut Links](url-scheme) · [Privacy Policy](privacy)
