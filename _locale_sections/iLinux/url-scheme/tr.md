iLinux ** `ilinux://` ** (ayrıca yazılmıştır ** `iLinux://` **) URL programı, **iPhone, iPad ve Mac** ile ilgili derin bağlantılar - açık komut detay (Linux, CMD veya PowerShell), Daily Quiz, Favourites veya yanlış cevap Kitabı Safari, başka bir uygulama, bir widget dokunuş (iOS/iPad) veya Apple Shortcuts.

Komut URL'leri isteğe bağlı olarak kabul eder ** `ilinux://` ** sorgu parametresi bu yüzden widget musluklar ve Kısa kesimler Windows girişlerini doğru şekilde açabilir.

**Home Ekran Hızlı Eylemler **iOS /iPad'in yalnızca**) kapak Arama, Kategoriler, Geri bildirim ve Puan. Mac kullanıcıları bunun yerine **iLinux** menü ve klavye kısayollarını kullanabilir.

> **İmportant: ** iLinux bir **reference ve öğrenme uygulaması**. URL bağlantıları sadece ** uygulama içinde iptal edin**. **Not ** Linux komutları, açık SSH seansları veya uzaktan sunuculara bağlanır.

## Protokol Doğrulaması


```
ilinux://<host>[/<path>][?query]
iLinux://<host>[/<path>][?query]   ← same scheme, case-insensitive
```


| Rule | Detaylı Bilgi |
|------|--------|
| **Scheme** | "ilinux" / "iLinux" - vakaya karşı hassas bir şekilde karşılaştırıldığında |
| **Host routing** | Birincil yönlendirici URL **host**; bazı yollar da kabul edilir (aşağıda bakın) |
| **Command detail** | Host "command" **or ** yol "/command" |
| **Command ID** | Sorgu "isim=<id>" **or** "cmd=<id>" - bir paketli komut anahtarla eşleştirmeli (e.g. "ls', "grep', " |
| **Platform** | Sorgu " platform =<value>" - isteğe bağlı; **Linux**'ye varsayılan olarak |
| **Quiz** | Host "quiz" **or ** yol " /quiz" |
| **Favourites** | Host "favorites" **or ** yol "/favorites" |
| **Wrong book** | Host "wrong", "mistakes", ya da "wrongquestions"; yol "/wrong" veya " /mistakes" de kabul edildi |
| **Wrong record** | Sorgu "record=<UUUID>" yanlış bir kitap URL'de - bu rekorun komut detayını açıyor |
| **Query parameters** | Diğer önceden tamamlanma parametreleri desteklenmez |
| **Parser** | "ILinux DeepLink.parse( :)" - "onOpenURL" → "AppRouter.pending DeepLink" |

** İki teslimat kanalı**

| Channel | Handled by | Örnekler |
|---------|------------|----------|
| **Universal deep link** (`onOpenURL`) | `ILinuxDeepLink.parse` → `RootTabView` | "Amand", "quiz", "favorites", "wrong" |
| **Home Screen Quick Action** | `ShortcutSceneDelegate` → `ShortcutObserver.dispatch` | “Arapçalar”, “sağlık”, “öğrenme”, artı örtüşme ‘quiz’ / “favorites’ / “wrong’ |

Hızlı aksiyon türleri ** `ilinux://` ** tipi dizede eşleşen, bu yüzden hem de `iLinux://` ve mirası seçenekleri hala doğru rotayı doğru şekilde rotalar.

---

## 1. Komut Detayları

Tek bir paketli komut için detay sayfasını açın.

| Parameter | Required | Açıklama |
|-----------|----------|-------------|
| `name` | One of `name` / `cmd` | Komutan ID (Rehlikeary key in the platform JSONpack) |
| `cmd` | One of `name` / `cmd` | "isim" için eş anlamlı - widget bağlantıları tarafından kullanılır |
| `platform` | No | Shell kütüphanesi: aşağıda masayı görün. **Linux** |

** `ilinux://` values ** (case-in sensitive):

| Value | Shell library | Aliases |
|-------|---------------|---------|
| *(omit)* or `linux` | Linux (1050 commands) | — |
| `cmd` | CMD / Batch (300 commands) | "batch", "bat" |
| `powershell` | PowerShell (300 commands) | "Pwsh" |

** Davranışı

- Anahtarlar **Commands ** sekmesi, talep edilen **shell platform**'i seçin ve "CommandDetailView"'i çözdü.
- Eğer kimlik ** bilinen veya boş** ise, bağlantı ** açıkça göz ardı edilir** (no error UI).
- Komutan kimlikleri **case-sensitive** ve tam olarak paketlenmiş JSON anahtarını eşleştirmeli (tipik olarak daha düşük, e.g. "docker", "Docker" değil.

**Açık `ilinux://` **


```
ilinux://command?name=ls
```


**Açık `ilinux://` (Linux, varsayılan)**


```
ilinux://command?cmd=grep
```


**Açık CMD `ilinux://` **


```
ilinux://command?cmd=dir&platform=cmd
```


**Open PowerShell `ilinux://` **


```
ilinux://command?cmd=Get-ChildItem&platform=powershell
```


**Cloud-native Linux örneği**


```
ilinux://command?name=docker
```


---

## 2. Günlük Quiz

Doğrudan **Daily Quiz** sekmesine atlayın. **Not ** auto-start veya soruları atlar.


```
ilinux://quiz
```


Pat formu (ayrıca kabul):


```
ilinux:///quiz
```


---

## 3. Favourites

**Favourites** listesi Ayarlar navigasyon altında.


```
ilinux://favorites
```


Pat formu (ayrıca kabul):


```
ilinux:///favorites
```


---

## 4. Yanlış Cevap Kitabı

### 4.1 Listesi

**Wrong Answer Book** listesini Ayarlar navigasyon altında açın.


```
ilinux://wrong
```


Aliases (same davranışı):


```
ilinux://mistakes
ilinux://wrongquestions
```


### 4.2 Tek kayıt → komut detay `ilinux://` , kurtarılmış bir yanlış cevap girişinin geçerli bir UUID'si olduğunda, uygulama **Commands ** sekmesini açar ve bu rekorun komutunu detaylandırır (eğer kayıt ve komut hala mevcutsa).

| Parameter | Required | Format |
|-----------|----------|--------|
| `record` | Yes | UUID string, e.g. "550e8400-e29b-41d4-a716-446655440000" |


```
ilinux://wrong?record=550e8400-e29b-41d4-a716-446655440000
```


UUID geçersizyse veya kayıt silindiyse, navigasyon yanlış kitap listesine geri döner veya atılır.

---

## 5. Ev Ekran Hızlı Eylemler

Long-press the iLinux icon → up to **4** actions. **Ev Ekran Kısakesler** (7 seçenek, yeniden sipariş için sürüklenme, varsayılanlara sıfırlama).

| Option | Registered `type` | SF Symbol | Açıklar |
|--------|-------------------|-----------|--------|
| Search | `iLinux://search` | magnifyingglass | **Commands ** sekmesi + aktif arama çubuğu |
| Daily Quiz | `iLinux://quiz` | checklist | **Daily Quiz ** sekmesi |
| Favourites | `iLinux://favorites` | star.fill | **Favourites ** listesi |
| Wrong Answer Book | `iLinux://wrong` | xmark.bin.fill | **Wrong Cevap Kitabı** listesi |
| Categories | `iLinux://categories` | rectangle.grid.2x2.fill | **Kategoriler ** sekmesi |
| Send Feedback | `iLinux://feedback` | envelope.fill | In-app mail form (veya "mailto:' fallback) |
| Rate App | `iLinux://review` | star.bubble.fill | StoreKit incelemesi Hızlı |

**İlk yüklemedeDefault seçimi: ** Arama · Günlük Quiz · Favourites · Geri bildirim gönderin.

**Quick-action-only destinasyonlar** ( `ilinux://` / `iLinux://` tarafından ele alınma):

- "iLinux"
- "iLinux http://categories"
- "iLinux:
- "iLinux http

Bunu **long-press i + veya Quick Action boru hattı aracılığıyla aynı türü yayınlayarak - onları kısa kesimlerle açın **Open URL **, **, uygulama daha sonra açık ev sahibi parsing eklerken çalışmayabilir.

**Legacy type (still rotad):**

| Type | Davranış |
|------|-----------|
| `iLinux://love` | Opens author blog in in-app Safari page (eski statik kısayol) |

---

## 6. Widget Deep Links

Widget musluklar, `ilinux://` URL'ler tarafından inşa edilen aynı `iLinux://` :

| Widget | Tap target | URL URL URL URL |
|--------|------------|-----|
| Daily Command | Command detail | `iLinux://command?cmd=<id>&platform=<linux\ | cmd\ | ► |
| Category Spotlight | Sample command | "iLinux httpcommand?cmd=<id>&shop=< platform>" |
| Quiz Glance | Daily Quiz | "iLinux " |
| Favourites Glance | Favourites (or per-row command) | "iLinux http://favorites' / "iLinux httpcommand?cmd=<id>&shop=< platform> |
| Wrong Book Glance | Wrong book (or per-row record) | "iLinux httpwrong' / "iLinux http://wrong?record=<UUID>" |

Widget URL'ler, `ilinux://` tarafından inşa edilir ve her zaman ** `iLinux://` ** komut parçaları için içerir. Platform maçları **Settings → Widgets → Widget komut kütüphanesi** (Linux / CMD / PowerShell).

**Daily Komutanlığı shuffle düğmesine ** (iOS 17+, App Niye) sadece widget zaman çizelgesini yeniden yükler - ** değil ** URL kullanın.

---

## Apple Shortcuts

### Adını kopyalamaktan sonra bir komut açın

1. ** Girişten Text alın**
2. **Açık URLler** → `ilinux://` + Text

Ya da zor kod Linux:


```
ilinux://command?name=systemctl
```


Bir CMD komut açın:


```
ilinux://command?cmd=ipconfig&platform=cmd
```


### Günlük çalışma hatırlatması → sınav


```
ilinux://quiz
```


Add **Open URLs ** in a Personal Automation (e.g. every weekday at 9:00).

### Yanlış cevaplar


```
ilinux://wrong
```


### Bir Focus modundan açık favoriler


```
ilinux://favorites
```


---

## Behaviour

Uygulama bir URL veya Hızlı Eylem aldığında:

| Scenario | Akış Akış |
|----------|------|
| **Cold start — Quick Action (iOS/iPad only)** | "ShortcutSceneDelegate" → "PendingShortcutBuffer" → "ShortcutObserver.onAppear' → "dispatch (tip:)" |
| **Warm start — Quick Action (iOS/iPad only)** | Sahne geri dönüş → bildirim → "dispatch (tip:)" |
| **Cold / warm — `onOpenURL` (iOS, iPad, Mac)** | "AppRouter.handleIncomingURL" → "Zending DeepLink" → "RootTabView.onChange' navigates |
| **Feedback / Rate (cold start)** | "deferSheetWork'in gecikmeleri **~0.4 s** bu yüzden posta sayfası / MağazaKit aktif bir pencere sahnesine sahiptir |
| **Search quick action** | "Açık AramaTab()" → "searchPulse + = 1' → "BrowseCommandsView" (iOS 17+: oto-focus via "isPresented") |
| **Unknown command ID** | Derin bağlantı parsed ama navigasyon atladı - uyarı yok |

---

## Finger Shortcuts

### iPad & Mac (shared)

iPad'de Donanım klavyesi ve **iLinux** Mac Share:

| Shortcut | Eylem |
|----------|--------|
| ⌘F | Komutanlar sekmesi + arama ( iOS'ta hızlı bir eylem olarak niyet) |
| ⌘1 | Komutanlar sekmesi |
| ⌘2 | Kategoriler sekmesi |
| ⌘3 | Daily Quiz sekmesi |
| ⌘4 | Ayarlar sekmesi |

Arama otomatik-focus via .F requires **iOS 17.0+** veya **macOS 14.0+**.

### Mac sadece Mac

| Shortcut | Eylem |
|----------|--------|
| ⌘, | Ayarlar sekmesi |
| ⌘[ / Esc | Pop navigasyon yığını (geri) |
| ⌘← / ⌘→ | Önceki / sonraki kategori (Kategoriler sekmesi) |
| 1–4 | Test cevabı seçeneği seçeneği seçin |
| ⌘R | Reshuffle günlük test |
| Return | Sonraki sınav sorusu (ondan sonra) |

Derin bağlantılar ( `ilinux://` ) ve menü kısayolları Mac'de iOS'ta olduğu gibi aynı uygulama yönlendiricisini kullanır.

---

## Desteksiz ve Invalid URLs

| URL | Result |
|-----|--------|
| `ilinux://command` (no `name` / `cmd`) | Ignored |
| `ilinux://command?name=NotARealCmd` | Ignored (ID not in library for solution platform) |
| `ilinux://command?cmd=dir` (no platform) | Opens **Linux** kütüphanesi - Windows CMD için "platform=cmd" kullanın |
| `ilinux://search` via Shortcuts Open URL | **ILinux DeepLink tarafından parsed değil - **iOS /iPad** veya PadF üzerinde Hızlı Eylem kullanın **Mac/iPad ** |
| `ilinux://categories` via Shortcuts Open URL | Yukarıdaki gibi |
| `ilinux://feedback` / `ilinux://review` via Open URL | Yukarıdaki gibi |
| Non-`ilinux` schemes | Ignored |

---

## Sorun Giderme

**Shortcut uygulamayı açar ama hiçbir şey olmaz (cold lansmanı)**

Geri bildirim, Puan ve posta çarşafları başlatıldıktan sonra ~0.4 s gerekir. Uygulamanın içinde tekrar deneyin veya soğuk bir başlangıçta bir anı bekleyin.

**Hızlı eylem arama alanına odaklanmıyor (iOS 16)**

Auto-focus iOS 17+ gerektirir. iOS 16'da Komutlar sekmesi hala açılıyor; arama alanına el bas.

**Widget dokunuşu beklenen komutu açmaz**

komutun hala doğru ** platform** için yüklü uygulama sürüminizde var olmasını sağlayın. Widget bağlantıları, `ilinux://` + `iLinux://` ve tam bir komut ID'sini gerektirir: `platform` 'nin varsayılan Linux kütüphanesi değil.

**Quick-action başlıkları yanlış dildedir**

Change language in **Settings → Dil** - Uygulama otomatik olarak kayıt yaptırır.

** Deep link cihaz üzerinde çalışır, ancak bir web sayfasından değil**

Bağlantının kullanım biçimini onaylayın `ilinux://` ve sistem tarafından açılır ( Notlar/Messages'ta), striptizcilerin özel programları tarafından engellenmez.

---

[Back to iLinux Support](./) &middot; [FAQ](./faq) &middot; [Privacy Policy](./privacy)


