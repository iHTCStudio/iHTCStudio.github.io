iPomodoro, ** `iPomodoro://` ** ve ** `iPomodoros://` ** URL planı derin bağlantıları - bir sekme açın veya Safari'den başka bir uygulama, bir QR kodu veya Apple Shortcuts. Bu URL'ler **Home Ekran Hızlı Eylemler ** olarak mevcut olan yerleri yansıtıyor ( Uygulama ikonunu uzun baskı).

> **Not: ** URL bağlantıları ** başlangıç veya zamanlayıcıları durdurmuyor, görev kimliklerini veya önceden teslimat süresini geç. Sadece uygulama içinde dolaşıyorlar. For speak focus summaries without open the app, use **Siri App Shortcuts ** (see [Related: Siri & App Shortcuts] (# related-siri-app-cuts) aşağıda).

## Protokol Doğrulaması


```
iPomodoro://<path>
iPomodoros://<path>
```


| Rule | Detaylı Bilgi |
|------|--------|
| **Schemes** | "iPomodoro" (primary) · "iPomodoros" (ayrıca kabul edildi) |
| **Path** | Single segment, **case-in sensitive** - URL'den çözüldü **host** |
| **Query parameters** | Desteklenen değil (şimdiyse) |
| **Equivalent Quick Action type** | "iPomodoro:<path>" (Ev Ekran kısayollarında kayıtlı bir dize) |

Yol eşleştirmesi ** segment adında - uygulama `iPomodoro://` gibi bulanık olmayan substrings değildir.

---

## Hedefler

| Path | Opens | Notlar |
|------|--------|-------|
| `pomodoro` | **Pomodoro** tab | Bir seans otomatik olarak başlama |
| `study` | **Study Timer** tab | Bir seans otomatik olarak başlama |
| `tasks` | **Tasks** tab |  |
| `stats` | **Statistics** tab |  |
| `motivation` | **Motivational Quote Anthology** full-screen gallery | Aynı UI as **Settings → Motivasyonel Sözlüğü Ayarlar → Motivasyonel Sözlüğü |
| `feedback` | **Feedback** sheet | Mevcut olduğunda Mail'i kullanın; "mailto'ya geri dönün:" |

---

## Örnekler

**Açık Pomodoro sekmesi **


```
iPomodoro://pomodoro
```


**Open Study Timer sekmesi ** (alternate program)


```
iPomodoros://study
```


**Açık İstatistikler paneli**


```
iPomodoro://stats
```


**Bir motivasyon alıntısını göster**


```
iPomodoro://motivation
```


**Open feedback**


```
iPomodoro://feedback
```


---

## Başlangıç Davranışları

Uygulama bir URL aldığında (cold start or while running):

1. `iPomodoro://` , yolu `iPomodoros://` ile çözer.
2. Navigation **dedilmiş ~0.45 s** bu yüzden SwiftUI monte edilebilir.
3. **cold start**, bir URL / Hızlı Eylem **priority** otomatik olarak restore edilmiş bir Canlı Aktivite seansından aktif bir Pomodoro veya Çalışma sekmesine atlamak.

**Motivation** ve ** feedback** doğrudan açılır - ilk önce sekmeleri değiştirmezler.

---

## Apple Shortcuts

**Açık Pomodoro sekmesi **

1. Hareket ekleyin **Open URL**
2. URL: `iPomodoro://` **Open Statistics after a focus block**


```
iPomodoro://stats
```


Use **Open URL ** in a Personal Automation (e.g. after a Focus mode end) doğrudan paniğe atlamak için.

---

## İlgili: Siri & App Shortcuts

Yerleşik **App Shortcuts** (Siri / Kısakes uygulama) URL bağlantılarını tamamlamak:

| Intent | Davranış Davranış |
|--------|----------|
| Open Pomodoro | Pomodoro sekmesine Anahtarlar |
| Open Study Timer | Zamanlayıcı sekmesine Anahtarlar |
| Open Statistics | İstatistikler sekmesine Anahtarlar |
| Today's focus summary | Bugünün odak süresi ve pomodoro sayısı ** Uygulamayı gerektirmez ** |

Örnek Siri cümlesi: *"Bugün iPomodoro'da ne kadar süre odaklandığımı?*

Home Ekran simgesinde hangi dört öğenin ortaya çıktığını yapılandırın **Settings → App ayarları → Ev Ekran kısayolları ** (drag to reorder). Yukarıdaki URL yolları tüm altı olası destinasyonları kapsar; sadece dört tanesi bir anda ikonda görünebilir.

---

## Sorun Giderme

| Issue | Ne kontrol edecek |
|-------|----------------|
| Link does nothing | Uygulamanın yüklenmesini sağlamak; yol yukarıdaki altı isimden biri olmalıdır |
| Wrong tab after reopening | Bir zamanlayıcı Canlı Aktivite aktifse, a **Quick Action / URL lansmanı overrides ** otomatik sekme geri yükleme |
| `feedback` opens Mail app only | Cihazın yapılandırılmış bir Mail hesabı yoktur - iPomodoro "mailto:" |

---

[Back to iPomodoro Support](./) &middot; [FAQ](./faq) &middot; [Privacy Policy](./privacy)


