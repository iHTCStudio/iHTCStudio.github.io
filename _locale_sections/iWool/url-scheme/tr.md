iWool, ** `iwool://` ** URL planı derin bağlantıları - bir sekme açın, bir in-app eylemine başlayın veya Safari'den belirli bir aktiviteye atlamak, Apple Shortcuts, bir widget dokunuşu veya bir Ev Ekran Hızlı Eylem (Uygulama ikonunu baskılayın).

> **İmportant:** Derin bağlantılar sadece ** içinde iWool**. Buluta sunucu bağlantıları veya senkronize verileri yaratmazlar.

## Protokol Doğrulaması


```
iwool://<path>[?query]
```


| Rule | Detaylı Bilgi |
|------|--------|
| **Scheme** | "iwool" (case-in sensitive) |
| **Routing** | İlk yol segmenti (hayal veya yol) varış noktasını seçer |
| **Empty URL** | “iwool https://’ with no road → **Home** |
| **Unknown paths** | **Ignored** (Evde sessiz bir düşüş yok) |
| **Parser** | "IWool DeepLink.parse( :)" → "ContentView.apply DeepLink" |

---

## 1. Tab destinasyonları

| URL | Açar |
|-----|--------|---------|
| `iwool://home` | **Home** tab | — |
| `iwool://calendar` | **Calendar** tab | "cal" |
| `iwool://stats` | **Statistics** tab | "statistikler", "stat" |
| `iwool://settings` | **Settings** tab | "Hayır", "preferences" |

---

## 2.In-app actions

Bu rotalar maç **Home Quick Actions ** ve açık çarşaflar veya alt sayfalar:

| URL | Açar |
|-----|--------|---------|
| `iwool://new` | **Create activity** sheet | "create", "add", "newevent", "newevent" |
| `iwool://island` | **Quick Countdown** (Dynamic Island reminder) sheet | “Köpücü”, “Kırdar”, “saygınlık”, “hakkınlık”, “hakkın” |
| `iwool://reminders` | **Scheduled local reminders** list (Settings) | “Kömürgeciler”, “sömürgeciler”, “dövülsüzler”, “göçücüler” |
| `iwool://scanner` | **QR / barcode scanner** (Settings → Tools) | "Scan", "qrcode", "barcode" |
| `iwool://rate` | In-app **App Store rating** prompt | "Şeytan", "düşün", " |
| `iwool://feedback` | **Feedback** email compose | "mail", "support", "Contact" |

**Nested ayarları yolları** (same eylemleri):


```
iwool://settings/scanner
iwool://settings/reminders
iwool://settings/rate
iwool://settings/feedback
```


---

## 3. Aktivite detayı

Veritabanı ID tarafından tek bir yün aktivite açın.

| Parameter | Required | Açıklama |
|-----------|----------|-------------|
| Path `event/{id}` | One of path / query | Faaliyet ID (pozitif tamsayı) |
| Query `id={id}` | One of path / query | Aynı şekilde yol formu |
| Query `day={seconds}` | No | **recurring ** aktiviteler – doğal gün 1970'ten beri “timeInterval” olarak başlıyor (bu olayın gecesi). |

**Açık aktivite 42**


```
iwool://event/42
iwool://event?id=42
```


** Belirli bir günde meydana gelen olaylar**


```
iwool://event/42?day=189345600
```


Tekrarlanan seriler için bina bağlantıları inşa ederken, iWool, ev listesi ( `iwool` ) ile aynı mantıktan `iwool://` elde edebilir.

---

## 4. Ev Ekran Hızlı Eylemler (iOS)

IWool i →'a kadar, **4** eylemleri. **Aptallar → Tools → Ev Ekran Kısakesler** (9 seçenek, yeniden sipariş etmeye sürüklenmek, varsayılanlere sıfırlamak).

| Option | URL URL URL URL |
|--------|-----|
| Home | "iwool httphome" |
| Calendar | "iwool httpcalendar" |
| Statistics | "iwool httpstats" |
| Quick Countdown | "iwool httpisland" |
| New Activity | "iwool httpnew" |
| Scheduled Reminders | "iwool httpreminders" |
| Scanner | "iwool httpscanner" |
| Rate App | "iwool httprate" |
| Feedback | "iwool httpfeedback" |

**İlk yüklemedeDefault:** Home · Takvim · İstatistikler · Hızlı Kontdown.

Quick-action `iwool://` stringler aynı `iwool` yolları ve rota aracılığıyla `iwool://` → `IWoolDeepLink.parse(_:)` soğuk başlangıç.

---

## 5. Widget derin bağlantılar

Widget musluklar aynı `iwool://` URL'leri kullanır:

| Widget | Tap target | URL URL URL URL |
|--------|------------|-----|
| Today Active / Today All / Today Upcoming / All Events | Home | "iwool httphome" |
| Stats Overview / Earnings / Top Platforms | Statistics | "iwool httpstats" |
| Glance | First event or Home | "iwool httpevent/{id}" veya "iwool: |
| Lock Screen accessories | First event or Home | "iwool httpevent/{id}" veya "iwool: |
| List row (iOS 17+) | Activity detail | “iwool https://event/{id} |

Hızlı Kontdown Canlı Etkinlikler sadece uygulama arayüzünde kullanılır - ** farklı URL ** uygulamanın dışında bir ada sayımı başlatmak için (foto `iwool://` 'i oluşturma sayfası açmak için).

---

## Apple Shortcuts örnekler

**Açık İstatistikler**


```
iwool://stats
```


**Yeni bir aktivite oluşturun**


```
iwool://new
```


**Open Quick Countdown sayfası**


```
iwool://island
```


** ID'yi kopyalamaktan sonra açık aktivite**


```
iwool://event?id=42
```


---

## Başlangıç davranışı

| Scenario | Akış Akış |
|----------|------|
| **Widget / Shortcuts `onOpenURL`** | "AppRouter" → "Uygulamalı Link' |
| **Cold start — Quick Action** | "ShortcutSceneDelegate" → "PendingShortcutBuffer" → "ShortcutObserver" |
| **Warm start — Quick Action** | Sahne geri dönüş → “ShortcutObserver’ |
| **Feedback / Rate (cold start)** | Kısa gecikme o posta sayfası / MağazaKit aktif bir pencere sahnesine sahiptir |
| **Invalid event ID** | Link görmezden gelin - hiçbir uyarı |

---

## Sorun Giderme

| Issue | Ne kontrol edecek |
|-------|----------------|
| Link opens app but nothing happens | Yol desteklenen bir rotayla eşleşmeli; bilinmeyen yollar Home'a yönlendirilmiyor |
| `event` link shows wrong occurrence | Tekrarlanan aktiviteler için "?day=" ekleyin |
| Quick Action does nothing on cold launch | Bekle ~0.4 s veya yeniden deneme; geri bildirim / ihtiyaç UI Dağı zamanı |
| `iwool://island` does not start countdown automatically | **kreasyon sayfası** - onay süresi ve uygulama içine başlayın |
| Quick Countdown requires iOS 16.2+ | Event Live Activities iOS 16.1+'ya ihtiyaç duyar; standalone ada sayısı 16.2+ |

---

[Privacy Policy](./privacy)


