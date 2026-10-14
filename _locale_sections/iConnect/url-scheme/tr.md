iConnect ** `iconnect://` ** URL programı derin bağlantıları - bir sekme açın, bir Ayarlar sayfası veya Safari'den bir in-app sayfası, başka bir uygulama, bir kitap işareti veya Apple Shortcuts. Bu URL'ler **Home Ekran Hızlı Eylemler ** iPhone ve iPad'de ( Uygulama ikonunu uzun baskı) mevcut destinasyonları yansıtıyor.

> **Not: ** URL bağlantıları sadece ** iConnect** içinde kısaltılır. Bir eşe bağlanmazlar, bir transfere başlayın veya belirli bir sohbet ipine açın.

## Protokol Doğrulaması


```
iconnect://<host>
iconnect://<host>?refresh=1
```


| Rule | Detaylı Bilgi |
|------|--------|
| **Scheme** | " |
| **Host / path** | Single segment, **case-in sensitive** - URL **host** veya ilk **path** segmenti |
| **Aliases** | Birkaç ev eş anlamlı kabul eder (aşağıdaki tabloya bakın) |
| **Query** | Sadece "refresh=1" / "refresh=gerçek", **Devices** bir keşif yeniledi |

eşdeğer formların örnekleri:


```
iconnect://devices
iconnect://open/devices
```


---

## Tab destinasyonları

| URL | Açar |
|-----|--------|---------|
| `iconnect://devices` | **Devices** tab (radar / discovery) | " |
| `iconnect://devices?refresh=1` | **Devices** tab and **refreshes** nearby discovery | — |
| `iconnect://chat` | **Chats** tab | “Yeminler” |
| `iconnect://transfers` | **Transfers** tab | "Transfer" |
| `iconnect://history` | **History** tab (transfer log) | — |
| `iconnect://settings` | **Settings** tab | " |

**Refresh keşif**


```
iconnect://devices?refresh=1
iconnect://devices/refresh
```


---

## Ayarlar alt sayfalar

Bu bağlantılar **Settings **, sonra eşleşen sayfasını açın:

| URL | Açar |
|-----|--------|---------|
| `iconnect://about` | About | — |
| `iconnect://usage` | Usage Guide | “ Rehberlik”, “yardım”, “öğrenme” |
| `iconnect://shortcuts` | Home Screen shortcuts picker (iOS) | "Ev 6:cuts" |
| `iconnect://debug` | Debug / diagnostics info | "debuginfo" |

---

## In-app actions

| URL | Açar |
|-----|--------|
| `iconnect://share` | Share iConnect page (App Store link + öneri metni) |
| `iconnect://feedback` | Geri bildirim e-postası (postaya geri dönüyorsa) |
| `iconnect://review` | In-app App Mağaza derecelendirmesi |

**Review alias:** `iconnect://` , `iconnect` ---

## Örnekler

**Açık Sohbetler sekmesi **


```
iconnect://chat
```


**Açık Transferler sekmesi **


```
iconnect://transfers
```


**Refresh cihazı keşfi**


```
iconnect://devices?refresh=1
```


**Açık Kullanım Kılavuzu**


```
iconnect://usage
```


** Uygulamayı paylaşın **


```
iconnect://share
```


---

## Home Screen Quick Actions (iOS)

Long-press the iConnect icon. **4 ** kısayollarına kadar özelleştirin ** Ev Ekran kısayolları** (drag yeniden sipariş vermek için).

| Quick Action | URL URL URL URL |
|--------------|-----|
| Devices | "Ininvices" |
| Chats | "Saç" |
| Transfers | "Aptallar" |
| History | "Aptal" |
| Share | "Seks" |
| Feedback | "Arapback" |
| Rate | "In" (İngilizce). |
| About | "Saç" |

Varsayılan olarak etkinleştirin: **Devices**, **Chats**, **Share**, **Feedback**.

Hızlı aksiyon türleri aynı `iconnect://` dizeleri kullanır ve dış URL'ler olarak aynı . aracılığıyla yönlendirilir.

---

## Apple Shortcuts

**Açık Transferler sekmesi **

1. Hareket ekleyin **Open URL**
2. URL: `iconnect://` **Refresh, Wi-Fi'ye katıldıktan sonra yakın cihazlara üye oldu**


```
iconnect://devices?refresh=1
```


Use **Open URL ** in a Personal Automation (e.g. when Wi-Fi connect) to navigation and rescan.

---

## başlangıç davranışı

IConnect bir URL aldığında (cold start or while running):

1. bağlantı, `iconnect://` tarafından parsedilir.
2. Tab hemen animate kilitler; **share**, **feedback**, ve ** hakem ** kısa bir gecikmeden sonra açılır (~0.4 s iOS'ta) böylece UI monte edilebilir.
3. **Feedback** mevcut olduğunda Mail'de kullanılır; aksi takdirde varsayılan posta istemcisini `iconnect://` ile açın.
4. **Share** on Mac sistem pay seçiciini kullanır; iOS'ta bir pay sayfası sunar.

---

## Sorun Giderme

| Issue | Ne kontrol edecek |
|-------|----------------|
| Link does nothing | Emin iConnect kurulur; host yukarıda desteklenen bir isim eşleştirmeli |
| `feedback` opens Mail only | Cihazda yapılandırılan Mail hesabı yok - beklenen geri çekilme |
| `shortcuts` has no effect on Mac | Home Ekran kısayol özelleştirmesi **iOS-only** |
| URL does not connect to a device | Derin bağlantılar sadece gezinmek - akranları manuel olarak keşfetmek için cihazlar sekmesi kullanın |

---

[Back to iConnect Support](.)


