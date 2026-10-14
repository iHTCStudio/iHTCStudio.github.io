iWool unterstützt ** `iwool://` ** URL-Schema Deep Links - Öffnen Sie einen Tab, starten Sie eine In-App-Aktion oder springen Sie zu einer bestimmten Aktivität von Safari, Apple Shortcuts, einem Widget-Tipp oder einer Home Screen Quick Action (langes Drücken des App-Symbols).

> **Wichtig:** Nur tiefe Links **navigieren innerhalb von iWool**. Sie erstellen keine Serververbindungen oder synchronisieren Daten mit der Cloud.

## Protokollspezifikation


```
iwool://<path>[?query]
```


| Rule | Einzelheiten |
|------|--------|
| **Scheme** | "iwool" (fallunempfindlich) |
| **Routing** | Erstes Pfadsegment (Host oder Pfad) wählt das Ziel aus |
| **Empty URL** | "iwool://" ohne Pfad → **Home |
| **Unknown paths** | **Ignoriert** (kein stiller Fallback nach Hause) |
| **Parser** | `IWoolDeepLink.parse( :)` → `ContentView.applyDeepLink` |

---

## 1. Tab Destinationen

| URL | Öffnet |
|-----|--------|---------|
| `iwool://home` | **Home** tab | — |
| `iwool://calendar` | **Calendar** tab | „cal |
| `iwool://stats` | **Statistics** tab | "Statistik", "Statistik" |
| `iwool://settings` | **Settings** tab | "Setting", "Präferenzen" |

---

## 2. In-App-Maßnahmen

Diese Routen passen zu **Home Screen Quick Actions ** und öffnen Blätter oder Unterseiten:

| URL | Öffnet |
|-----|--------|---------|
| `iwool://new` | **Create activity** sheet | `create`, `add`, `new-event`, `newevent` |
| `iwool://island` | **Quick Countdown** (Dynamic Island reminder) sheet | "Island-Reminder", "Islandreminder", "Countdown", "Quick-Countdown", "QuickCountdown" |
| `iwool://reminders` | **Scheduled local reminders** list (Settings) | "Scheduled-Reminders", "Scheduled-Reminders", "Notification-Reminders" |
| `iwool://scanner` | **QR / barcode scanner** (Settings → Tools) | `scan`, `qrcode`, `barcode` |
| `iwool://rate` | In-app **App Store rating** prompt | `rating`, `review`, `rate-in-app`, `rateinapp` |
| `iwool://feedback` | **Feedback** email compose | `mail`, `support`, `contact` |

**Nested settings paths** (gleiche Aktionen):


```
iwool://settings/scanner
iwool://settings/reminders
iwool://settings/rate
iwool://settings/feedback
```


---

## 3. Angaben Tätigkeit

Öffnen Sie eine einzelne Wollaktivität nach Datenbank-ID.

| Parameter | Required | Beschreibung |
|-----------|----------|-------------|
| Path `event/{id}` | One of path / query | Aktivitätskennung (positive ganze Zahl) |
| Query `id={id}` | One of path / query | Gleiches wie Pfadform |
| Query `day={seconds}` | No | Für **wiederkehrende ** Aktivitäten - natürlicher Tagesbeginn als "timeIntervalSince1970" (Mitternacht dieses Ereignisses) |

**Offene Aktivität 42**


```
iwool://event/42
iwool://event?id=42
```


**Wiederholtes Ereignis an einem bestimmten Tag**


```
iwool://event/42?day=189345600
```


Beim Erstellen von Links für wiederkehrende Serien kann iWool `iwool://` aus derselben Logik wie die Heimatliste ( `iwool` ) ableiten.

---

## 4. Home Screen Quick Actions (iOS)

Langes Drücken des iWool-Symbols → bis zu **4** Aktionen. Anpassen in **Einstellungen → Tools → Home Screen Shortcuts** (9 Optionen, Drag to Reorder, Zurücksetzen auf Standard).

| Option | URL |
|--------|-----|
| Home | „iwool://home |
| Calendar | „iwool://calendar |
| Statistics | „iwool://stats |
| Quick Countdown | „iwool://island |
| New Activity | „iwool://new |
| Scheduled Reminders | „iwool://reminders |
| Scanner | „iwool://scanner |
| Rate App | „iwool://rate |
| Feedback | „iwool://feedback |

**Standard bei der ersten Installation:** Home · Kalender · Statistiken · Quick Countdown.

Quick-action `iwool://` Strings verwenden die gleichen `iwool` Pfade und Route durch `iwool://` → `IWoolDeepLink.parse(_:)` beim Kaltstart.

---

## 5. Widget Deep Links

Widget Taps verwenden die gleichen `iwool://` URLs:

| Widget | Tap target | URL |
|--------|------------|-----|
| Today Active / Today All / Today Upcoming / All Events | Home | „iwool://home |
| Stats Overview / Earnings / Top Platforms | Statistics | „iwool://stats |
| Glance | First event or Home | `iwool://event/{id}` oder `iwool://home` |
| Lock Screen accessories | First event or Home | `iwool://event/{id}` oder `iwool://home` |
| List row (iOS 17+) | Activity detail | „iwool://event/{id} |

Quick Countdown Live-Aktivitäten verwenden nur die In-App-Benutzeroberfläche - **keine separate URL **, um einen Insel-Countdown von außerhalb der App zu starten (verwenden Sie `iwool://` , um das Erstellungsblatt zu öffnen).

---

## Apple Shortcuts Beispiele

**Offene Statistiken**


```
iwool://stats
```


**Erstelle eine neue Aktivität**


```
iwool://new
```


** Schnelles Countdownblatt öffnen**


```
iwool://island
```


**Offene Aktivität nach Kopieren der ID**


```
iwool://event?id=42
```


---

## Startverhalten

| Scenario | Durchfluss |
|----------|------|
| **Widget / Shortcuts `onOpenURL`** | AppRouter → ApplyDeep Link |
| **Cold start — Quick Action** | ‘ShortcutSceneDelegate’ → ‘PendingShortcutBuffer’ → ‘ShortcutObserver’ |
| **Warm start — Quick Action** | Scene Callback → Benachrichtigung → `ShortcutObserver` |
| **Feedback / Rate (cold start)** | Kurze Verzögerung so Mailsheet / StoreKit hat eine aktive Fensterszene |
| **Invalid event ID** | Link ignoriert – keine Warnung |

---

## Fehlerbehebung

| Issue | Was zu überprüfen ist |
|-------|----------------|
| Link opens app but nothing happens | Pfad muss mit einer unterstützten Route übereinstimmen; unbekannte Pfade werden nicht nach Hause umgeleitet |
| `event` link shows wrong occurrence | Hinzufügen von `?day=` für wiederkehrende Aktivitäten |
| Quick Action does nothing on cold launch | Warten Sie ~ 0,4 s oder wiederholen Sie; Feedback / Rate benötigen UI-Montagezeit |
| `iwool://island` does not start countdown automatically | Öffnet das **Erstellungsblatt** – Dauer bestätigen und auf Start innerhalb der App tippen |
| Quick Countdown requires iOS 16.2+ | Event Live-Aktivitäten benötigen iOS 16.1+; Standalone-Insel-Countdown benötigt 16.2+ |

---

[Zurück zu iWool Support](..) · [FAQ](../faq) · [Privacy Policy](../privacy]


