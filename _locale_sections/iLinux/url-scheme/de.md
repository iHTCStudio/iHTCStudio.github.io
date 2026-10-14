iLinux unterstützt ** `ilinux://` ** (auch geschrieben ** `iLinux://` **) URL-Schema Deep Links auf ** iPhone, iPad und Mac ** - offene Befehlsdetails (Linux, CMD oder PowerShell), das tägliche Quiz, Favoriten oder das falsche Antwortbuch von Safari, eine andere App, ein Widget-Tipp (iOS / iPad) oder Apple Shortcuts.

Befehls-URLs akzeptieren einen optionalen ** `ilinux://` ** Abfrageparameter, sodass Widget-Tipps und Shortcuts Windows-Einträge korrekt öffnen können.

**Home Screen Quick Actions** (langes Drücken des App-Symbols nur auf ** iOS / iPad**) decken Suche, Kategorien, Feedback und Rate ab. Mac-Benutzer können stattdessen das **iLinux**-Menü und die Tastenkombinationen verwenden.

> **Wichtig:** iLinux ist eine **Referenz- und Lern-App**. URL-Links **navigieren nur innerhalb der App**. Sie führen **nicht ** Linux-Befehle aus, öffnen SSH-Sitzungen oder stellen eine Verbindung zu Remote-Servern her.

## Protokollspezifikation


```
ilinux://<host>[/<path>][?query]
iLinux://<host>[/<path>][?query]   ← same scheme, case-insensitive
```


| Rule | Einzelheiten |
|------|--------|
| **Scheme** | `ilinux` / `iLinux` — fallunempfindlich verglichen |
| **Host routing** | Primärer Router ist die URL **host**; einige Pfade werden auch akzeptiert (siehe unten) |
| **Command detail** | Host `Befehl` **oder ** Pfad `/Befehl` |
| **Command ID** | Abfrage `name=<id>` **or** `cmd=<id>` muss mit einem gebündelten Befehlsschlüssel übereinstimmen (z.B. `ls`, `grep`, `dir`, `Get-ChildItem`). |
| **Platform** | Abfrage `platform=<value>` — optional; standardmäßig auf **Linux**, wenn weggelassen |
| **Quiz** | Host `quiz` **or** path `/quiz` |
| **Favourites** | Host `Favoriten` **oder** Pfad `/Favoriten` |
| **Wrong book** | Host `falsch`, `Fehler` oder `falsche Fragen`; Pfad `/falsch` oder `/Fehler` auch akzeptiert |
| **Wrong record** | Abfrage `record=<UUID>` auf einer falschen Buch-URL - öffnet die Befehlsdetails dieses Datensatzes |
| **Query parameters** | Keine anderen Vorfüllparameter werden unterstützt |
| **Parser** | `ILinuxDeepLink.parse( :):` — verbraucht über `onOpenURL` → `AppRouter.pendingDeepLink` |

**Zwei Lieferkanäle **

| Channel | Handled by | Beispiele |
|---------|------------|----------|
| **Universal deep link** (`onOpenURL`) | `ILinuxDeepLink.parse` → `RootTabView` | "Befehl", "Quiz", "Favoriten", "falsch" |
| **Home Screen Quick Action** | `ShortcutSceneDelegate` → `ShortcutObserver.dispatch` | `search`, `categories`, `feedback`, `review` plus überlappendes `quiz` / `favorites` / `falsch` |

Quick-Action-Typen verwenden ** `ilinux://` ** Matching auf der Typzeichenfolge, so dass sowohl `iLinux://` als auch Legacy-Varianten immer noch korrekt routen.

---

## 1. Befehlsdetail

Öffnen Sie die Detailseite für einen einzelnen gebündelten Befehl.

| Parameter | Required | Beschreibung |
|-----------|----------|-------------|
| `name` | One of `name` / `cmd` | Command ID (Wörterbuchschlüssel im Plattform-JSON-Bundle) |
| `cmd` | One of `name` / `cmd` | Synonym für `name` - wird von Widget-Links verwendet |
| `platform` | No | Shell-Bibliothek: siehe Tabelle unten. Standardmäßig **Linux** |

** `ilinux://` -Werte** (fallunempfindlich):

| Value | Shell library | Aliasnamen |
|-------|---------------|---------|
| *(omit)* or `linux` | Linux (1050 commands) | — |
| `cmd` | CMD / Batch (300 commands) | Batch, Bat |
| `powershell` | PowerShell (300 commands) | ps, pwsh |

**Verhalten**

- Wechselt zur Registerkarte **Commands**, wählt die angeforderte **shell-Plattform** aus und drückt `CommandDetailView` für den aufgelösten Befehl.
- Wenn die ID **unbekannt oder leer ** ist, wird der Link **stillschweigend ignoriert ** (keine Fehler-Benutzeroberfläche).
- Befehls-IDs sind **case-sensitiv** und müssen genau mit dem gebündelten JSON-Schlüssel übereinstimmen (normalerweise Kleinbuchstaben, z.B. `Docker`, nicht `Docker`).

**Offen `ilinux://` **


```
ilinux://command?name=ls
```


**Offen `ilinux://` (Linux, standardmäßig)**


```
ilinux://command?cmd=grep
```


**Open CMD `ilinux://` **


```
ilinux://command?cmd=dir&platform=cmd
```


**Open PowerShell `ilinux://` **


```
ilinux://command?cmd=Get-ChildItem&platform=powershell
```


**Cloud-natives Linux-Beispiel**


```
ilinux://command?name=docker
```


---

## 2. Tägliches Quiz

Springen Sie direkt zum Tab **Daily Quiz**. Startet **nicht ** autostart oder überspringt fragen.


```
ilinux://quiz
```


Trassenform (auch akzeptiert):


```
ilinux:///quiz
```


---

## 3. Favoriten

Öffnen Sie die ** Favoriten** Liste unter Einstellungen Navigation.


```
ilinux://favorites
```


Trassenform (auch akzeptiert):


```
ilinux:///favorites
```


---

## 4. Falsches Antwortbuch

### 4.1 Liste

Öffnen Sie die **Wrong Answer Book** Liste unter Einstellungen Navigation.


```
ilinux://wrong
```


Aliasnamen (gleiches Verhalten):


```
ilinux://mistakes
ilinux://wrongquestions
```


### 4.2 Einzeldatensatz → Befehlsdetail

Wenn `ilinux://` eine gültige UUID eines gespeicherten Falschantworteintrags ist, öffnet die App die Registerkarte **Befehle** und drückt Details für den Befehl dieses Datensatzes (wenn der Datensatz und der Befehl noch vorhanden sind).

| Parameter | Required | Format |
|-----------|----------|--------|
| `record` | Yes | UUID-String, z. B. `550e8400-e29b-41d4-a716-446655440000` |


```
ilinux://wrong?record=550e8400-e29b-41d4-a716-446655440000
```


Wenn die UUID ungültig ist oder der Datensatz gelöscht wurde, fällt die Navigation auf die Liste der falschen Bücher zurück oder wird übersprungen.

---

## 5. Home Screen Schnelle Aktionen

Langes Drücken des iLinux-Symbols → bis zu **4** Aktionen. Konfigurieren Sie in ** Einstellungen → Home Screen Shortcuts ** (7 Optionen, Drag to Reorder, Zurücksetzen auf Standard).

| Option | Registered `type` | SF Symbol | Offen |
|--------|-------------------|-----------|--------|
| Search | `iLinux://search` | magnifyingglass | **Befehle** Tab + Suchleiste aktivieren |
| Daily Quiz | `iLinux://quiz` | checklist | **Daily Quiz** Tab |
| Favourites | `iLinux://favorites` | star.fill | ** Favoriten** Liste |
| Wrong Answer Book | `iLinux://wrong` | xmark.bin.fill | ** Falsches Antwortbuch** Liste |
| Categories | `iLinux://categories` | rectangle.grid.2x2.fill | **Tab Kategorien** |
| Send Feedback | `iLinux://feedback` | envelope.fill | In-App Mail Compose (oder `mailto:` Fallback) |
| Rate App | `iLinux://review` | star.bubble.fill | StoreKit Review prompt |

**Standardauswahl bei der ersten Installation:** Suche · Tägliches Quiz · Favoriten · Feedback senden.

** Quick-Action-only Destinationen** (nicht behandelt von `ilinux://` / `iLinux://` ):

- „iLinux://search
- „iLinux://categories
- „iLinux://feedback
- „iLinux://review

Verwenden Sie diese über **Long-Press-Symbol ** oder indem Sie den gleichen Typ über die Quick Action-Pipeline veröffentlichen - Öffnen Sie sie mit Shortcuts **Open URL ** kann **nicht ** funktionieren, es sei denn, die App fügt später explizites Host-Parsing hinzu.

**Legacy-Typ (noch geroutet):**

| Type | Verhalten |
|------|-----------|
| `iLinux://love` | Öffnet Autor Blog in In-App Safari Blatt (alte statische Verknüpfung) |

---

## 6. Widget Deep Links

Widget Taps verwenden die gleichen `ilinux://` URLs, die von `iLinux://` erstellt wurden:

| Widget | Tap target | URL |
|--------|------------|-----|
| Daily Command | Command detail | `iLinux://command?cmd=<id>&platform=<linux\ | cmd\ | powershell> |
| Category Spotlight | Sample command | `iLinux://command?cmd=<id>&plattform=<plattform>` |
| Quiz Glance | Daily Quiz | „iLinux://quiz |
| Favourites Glance | Favourites (or per-row command) | `iLinux://favorites` / `iLinux://command?cmd=<id>&platform=<plattform>` |
| Wrong Book Glance | Wrong book (or per-row record) | `iLinux://wrong` / `iLinux://wrong?record=<UUID>` |

Widget-URLs werden von `ilinux://` erstellt und enthalten immer ** `iLinux://` ** für Kommando-Taps. Die Plattform passt **Einstellungen → Widgets → Widget-Befehlsbibliothek** (Linux / CMD / PowerShell).

Die Schaltfläche **Daily Command shuffle ** (iOS 17+, App Intent) lädt nur die Widget-Timeline neu – sie verwendet **nicht ** eine URL.

---

## Apple Shortcuts

### Öffnen Sie einen Befehl nach dem Kopieren seines Namens

1. ** Holen Sie sich Text von Input **
2. **Offene URLs** → `ilinux://` + Text

Oder Hard-Code Linux:


```
ilinux://command?name=systemctl
```


Öffnen Sie einen CMD-Befehl:


```
ilinux://command?cmd=ipconfig&platform=cmd
```


### Tägliche Studie Erinnerung → Quiz


```
ilinux://quiz
```


Fügen Sie **Open URLs** in einer Personal Automation hinzu (z.B. jeden Wochentag um 9:00 Uhr).

### Überprüfen Sie falsche Antworten


```
ilinux://wrong
```


### Offene Favoriten aus einer Focus Mode Shortcut


```
ilinux://favorites
```


---

## Startverhalten

Wenn die App eine URL oder Quick Action erhält:

| Scenario | Durchfluss |
|----------|------|
| **Cold start — Quick Action (iOS/iPad only)** | `ShortcutSceneDelegate` → `PendingShortcutBuffer` → `ShortcutObserver.onAppear` → `dispatch(type:)` |
| **Warm start — Quick Action (iOS/iPad only)** | Scene Callback → Benachrichtigung → `dispatch(type:)` |
| **Cold / warm — `onOpenURL` (iOS, iPad, Mac)** | `AppRouter.handleIncomingURL` → `pendingDeepLink` → `RootTabView.onChange` navigiert |
| **Feedback / Rate (cold start)** | `deferSheetWork` Verzögerungen **~0,4 s** so Mailsheet / StoreKit hat eine aktive Fensterszene |
| **Search quick action** | `openSearchTab()` → `searchPulse += 1` → `BrowseCommandsView` präsentiert die Suche (iOS 17+: Autofokus über `isPresented`) |
| **Unknown command ID** | Deep Link analysiert, Navigation übersprungen – kein Alarm |

---

## Tastenkürzel

### iPad & Mac (geteilt)

Hardware-Tastatur auf dem iPad und das **iLinux**-Menü auf dem Mac:

| Shortcut | Aktion |
|----------|--------|
| ⌘F | Befehle tab + suche (gleiche absicht wie search quick action auf ios). |
| ⌘1 | Tab Befehle |
| ⌘2 | Tab Kategorien |
| ⌘3 | Täglicher Quiz Tab |
| ⌘4 | Tab Einstellungen |

Suchen Sie Autofokus über ⌘F erfordert **iOS 17.0+** oder **macOS 14.0+**.

### Nur Mac

| Shortcut | Aktion |
|----------|--------|
| ⌘, | Tab Einstellungen |
| ⌘[ / Esc | Pop Navigation Stack (zurück) |
| ⌘← / ⌘→ | Vorherige / nächste Kategorie (Tab Kategorien) |
| 1–4 | Wählen Sie Quiz-Antwort-Option |
| ⌘R | Reshuffing tägliches Quiz |
| Return | Nächste Quizfrage (nach der Beantwortung) |

Deep Links ( `ilinux://` ) und Menükombinationen verwenden den gleichen In-App-Router auf dem Mac wie auf iOS.

---

## Nicht unterstützte und ungültige URLs

| URL | Result |
|-----|--------|
| `ilinux://command` (no `name` / `cmd`) | ignoriert |
| `ilinux://command?name=NotARealCmd` | Ignoriert (ID nicht in Bibliothek für aufgelöste Plattform) |
| `ilinux://command?cmd=dir` (no platform) | Öffnet **Linux**-Bibliothek - verwenden Sie `platform=cmd` für Windows CMD |
| `ilinux://search` via Shortcuts Open URL | **Nicht ** analysiert von `ILinuxDeepLink` — verwenden Sie Quick Action auf **iOS/iPad** oder ⌘F auf **Mac/iPad** |
| `ilinux://categories` via Shortcuts Open URL | Wie oben |
| `ilinux://feedback` / `ilinux://review` via Open URL | Wie oben |
| Non-`ilinux` schemes | ignoriert |

---

## Fehlerbehebung

** Shortcut öffnet die App, aber nichts passiert (Kaltstart) **

Feedback, Rate und Mailsheets benötigen ~ 0,4 s nach dem Start. Versuchen Sie es erneut aus der App heraus oder warten Sie einen Moment beim Kaltstart.

**Die Suche nach einer schnellen Aktion fokussiert das Suchfeld nicht (iOS 16)**

Autofokus erfordert iOS 17+. Unter iOS 16 wird die Registerkarte Befehle immer noch geöffnet; tippen Sie manuell auf das Suchfeld.

**Widget tap öffnet den erwarteten Befehl nicht **

Stellen Sie sicher, dass der Befehl in Ihrer installierten App-Version für die richtige ** Plattform ** noch vorhanden ist. Widget-Links verwenden `ilinux://` + `iLinux://` und erfordern eine genaue Befehls-ID. Beispiel: `platform` braucht `ilinux` , nicht die Standard-Linux-Bibliothek.

** Quick-Action-Titel sind in der falschen Sprache**

Ändern Sie die Sprache in **Einstellungen → Sprache ** - die App registriert die Verknüpfungselemente automatisch neu.

** Deep Link funktioniert auf dem Gerät, aber nicht von einer Webseite **

Bestätigen Sie, dass der Link das Schema `ilinux://` verwendet und vom System geöffnet wird (Tipp in Notizen / Nachrichten), nicht von einem In-App-Browser blockiert, der benutzerdefinierte Schemata entfernt.

---

[Zurück zu iLinux Support](../) &middot; [FAQ](../faq) &middot; [Privacy Policy](../privacy]


