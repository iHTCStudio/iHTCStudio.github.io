iHTC Studio («biz») iAppManager'ı (爱应用者 / 愛應用者) geliştirdi.

## Özet

**iHTC Studio, App Store Connect verileriniz için bir backend işletmez.** **API Key** ile oturum açarsınız; anahtar **cihaz Keychain**'inde kalır. İş istekleri **doğrudan Apple'a** gider (`api.appstoreconnect.apple.com`). **iHTC Studio hesabı yok. Reklam yok. Analytics / crash SDK yok.** İsteğe bağlı StoreKit bahşişlerini **Apple** işler.

## Cihazda saklanan veriler

| Veri | Amaç |
|------|------|
| API Key hesapları (Issuer ID, Key ID, `.p8` PEM) | App Store Connect API kimliği — Keychain |
| Hesap dizini / geçerli hesap / tercihler | Çoklu hesap, görünüm, dil, vurgu rengi |
| Uzak görsel önbelleği | App simgeleri ve medya küçük resimleri (Ayarlar'da temizlenebilir) |
| Yorum yanıt şablonları, rapor ön ayarları / yıldızlar | Hesap başına yerel verimlilik araçları |
| App Group widget anlık görüntüsü | Pipeline sayıları, tema / dil — **yalnızca cihazda** |

## Ağ

| Hedef | Neden |
|-------------|-----|
| `api.appstoreconnect.apple.com` | Tüm ASC yönetimi (JWT cihazda imzalanır) |
| Apple iTunes Lookup (çoklu bölge) | İsteğe bağlı simge zenginleştirme |
| Apple CDN / önceden imzalı yükleme URL'leri | Ekran görüntüleri, önizlemeler, IPA/PKG parça yüklemeleri (PUT'ta Bearer yok) |
| `apps.apple.com` / App Store | Ürün sayfalarını açma (sistem / harici) |
| Posta istemcisi | Göndermeyi seçtiğiniz geri bildirim |

iHTC Studio API özel anahtarınızı, App meta verilerini, IPA içeriğini, satış raporlarını veya müşteri yorumlarını **almaz**.

## İzinler ve platform

| Yetenek | Ne zaman | Neden |
|------------|------|-----|
| Giden ağ | ASC özellikleri kullanılırken | Apple API'leri |
| Kullanıcının seçtiği dosyalar | IPA/ekran görüntüsü yükleme, rapor dışa aktarma | Dosyaları siz seçersiniz |
| Keychain | API Key kaydet / kaldır | Güvenli yerel depolama |
| App Group | Widget'lar | Yalnızca yerel özet paylaşımı |
| Fotoğraflar / paylaşım sayfası (OS) | Dışa aktarır / kaydederseniz | Kullanıcı başlatır |

Sertifikaların **sistem Keychain'ine kurulumu** **macOS** içindir. iOS: liste / indir / paylaş.

## Yapmadıklarımız

- ASC verileri için iHTC Studio bulut hesabı yok
- Reklam veya üçüncü taraf izleyici yok
- Kişisel veri satışı yok
- Widget'lar kendi başına ASC çağırmaz

## İletişim

[AppleOSer@gmail.com](mailto:AppleOSer@gmail.com)
