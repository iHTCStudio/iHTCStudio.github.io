iPomodoro unterstützt ** `iPomodoro://` ** und ** `iPomodoros://` ** URL-Schema Deep Links - Öffnen Sie einen Tab oder In-App-Blatt von Safari, einer anderen App, einem QR-Code oder Apple Shortcuts. Diese URLs spiegeln die verfügbaren Ziele als **Home Screen Quick Actions** wider (langes Drücken des App-Symbols).

> **Hinweis:** URL-Links starten oder stoppen keine Timer, übergeben Aufgaben-IDs oder Vorfülldauern. Sie navigieren nur innerhalb der App. Für gesprochene Fokuszusammenfassungen, ohne die App zu öffnen, verwenden Sie **Siri App Shortcuts** (siehe [Related: Siri & App Shortcuts](#related-siri--app-shortcuts) unten).

## Protokollspezifikation


```
iPomodoro://<path>
iPomodoros://<path>
```


| Rule | Einzelheiten |
|------|--------|
| **Schemes** | `iPomodoro` (primär) · `iPomodoros` (auch akzeptiert) |
| **Path** | Ein einzelnes Segment, **case-unsensitive ** - aufgelöst von der URL **host ** |
| **Query parameters** | Nicht unterstützt (ignoriert, wenn vorhanden) |
| **Equivalent Quick Action type** | `iPomodoro://<path>` (gleicher String auf den Home Screen Shortcuts registriert) |

Pfadmatching ist ** genau ** auf dem segmentnamen - die app hat keine fuzzy-match-substrings wie     c0   .

---

## Ziele

| Path | Opens | Notizen |
|------|--------|-------|
| `pomodoro` | **Pomodoro** tab | Startet eine Sitzung nicht automatisch |
| `study` | **Study Timer** tab | Startet eine Sitzung nicht automatisch |
| `tasks` | **Tasks** tab |  |
| `stats` | **Statistics** tab |  |
| `motivation` | **Motivational Quote Anthology** full-screen gallery | Gleiche Benutzeroberfläche wie ** Einstellungen → Motivational Quote Settings → Motivational Quote Anthology** |
| `feedback` | **Feedback** sheet | Verwendet In-App-Mail-Compose, wenn verfügbar; fällt zurück auf "mailto:" |

---

## Beispiele

** Öffnen Sie Pomodoro Tab**


```
iPomodoro://pomodoro
```


**Open Study Timer Registerkarte** (alternatives Schema)


```
iPomodoros://study
```


**Open Statistics Dashboard**


```
iPomodoro://stats
```


** Zeigen Sie ein Motivationsangebot **


```
iPomodoro://motivation
```


**Offenes Feedback**


```
iPomodoro://feedback
```


---

## Startverhalten

Wenn die App eine URL erhält (Kaltstart oder während des Laufens):

1. `iPomodoro://` löst den Pfad über `iPomodoros://` auf.
2. Navigation ist **aufgeschoben ~ 0,45 s **, so dass SwiftUI die Montage beenden kann.
3. Am **kalten Start ** nimmt eine URL / Quick Action ** Vorrang vor dem automatischen Springen zu einem aktiven Pomodoro- oder Study-Tab aus einer wiederhergestellten Live-Aktivitätssitzung.

**Motivation** und **Feedback** öffnen Overlays direkt – sie wechseln nicht zuerst die Tabs.

---

## Apple Shortcuts

** Öffnen Sie Pomodoro Tab**

1. Aktion hinzufügen **Offene URL**
2. URL: `iPomodoro://` **Open Statistics nach einem Fokusblock**


```
iPomodoro://stats
```


Verwenden Sie **Offene URL** in einer persönlichen Automatisierung (z. B. nach Beendigung eines Fokusmodus), um direkt zu Ihrem Dashboard zu springen.

---

## Related: Siri & App Shortcuts

**App Shortcuts** (Siri / Shortcuts App) ergänzen URL-Links:

| Intent | Verhalten |
|--------|----------|
| Open Pomodoro | Wechsel zu Pomodoro Tab |
| Open Study Timer | Wechsel zum Study Timer Tab |
| Open Statistics | Wechsel zum Register Statistik |
| Today's focus summary | Gibt die heutige Fokusdauer und pomodoro-Anzahl ** zurück, ohne dass die App-Benutzeroberfläche erforderlich ist ** |

Beispiel Siri Satz: *"Wie lange habe ich mich heute in iPomodoro konzentriert?" *

Konfigurieren Sie, welche vier Elemente auf dem Home Screen-Symbol unter **Einstellungen → App-Einstellungen → Home Screen-Verknüpfungen** erscheinen (drag zum Nachbestellen). URL-Pfade oben decken alle sechs möglichen Ziele ab; nur vier können auf dem Symbol gleichzeitig erscheinen.

---

## Fehlerbehebung

| Issue | Was zu überprüfen ist |
|-------|----------------|
| Link does nothing | Stellen Sie sicher, dass die App installiert ist; Pfad muss einer der sechs oben genannten Namen sein |
| Wrong tab after reopening | Wenn ein Timer Live Activity aktiv ist, überschreibt ein ** Quick Action / URL-Start die automatische Tab-Wiederherstellung |
| `feedback` opens Mail app only | Gerät hat kein konfiguriertes Mail-Konto - iPomodoro fällt auf "mailto" zurück: |

---

[Zurück zu iPomodoro Support](../) &middot; [FAQ](../faq) &middot; [Privacy Policy](../privacy]


