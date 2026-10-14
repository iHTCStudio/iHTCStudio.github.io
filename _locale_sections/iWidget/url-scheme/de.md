iWidget unterstützt das URL-Schema ** `iwidget://` ** auf **iPhone, iPad und Mac**. Verwenden Sie es in **Safari **, **Apple Shortcuts **, einer anderen App oder einem QR-Code, um in die Haupt-App zu springen. Diese Links **navigieren nur ** - sie übergeben keine Widget-Design-IDs oder Edit-Board-Layouts.

Für gesprochene Mond- / Festival-Antworten **ohne das Öffnen der App verwenden Sie **Siri App Shortcuts ** (siehe [FAQ] (../faq) → Siri). Für ** Arbeit / Ruhe an einem Datum ** fügen Sie die separate ** Workday ** App Intent in Shortcuts hinzu.

## Format


```
iwidget://<host>[?query]
```


| Rule | Einzelheiten |
|------|--------|
| **Scheme** | Iwidget (Kleinbuchstabe) |
| **Host** | Trassensegment — siehe Tabelle |
| **Query** | Optional; nur dokumentierte Schlüssel werden gelesen |

Unbekannte Hosts werden sicher ignoriert (kein Absturz).

---

## Gastgeber

| Host | Opens | Abfrage |
|------|--------|-------|
| `today` | **Today** tab | — |
| `day` | **Today** tab and queues **day detail** for the given date | **`y`** Jahr · **`m`** Monat · **`d`** Tag (ganzzahlig) |
| `settings` | **Settings** tab | **`scroll=festivals`** scrollt zum Filterbereich Festival |

Wenn `iwidget://` Abfragewerte fehlen oder ungültig sind, wechselt die App weiterhin zu Heute, ohne ein Tagesblatt zu öffnen.

---

## Beispiele

**Heute geöffnet**


```
iwidget://today
```


**Offen 1. Januar 2026 Detail **


```
iwidget://day?y=2026&m=1&d=1
```


**Offene Einstellungen → Festivalfilter**


```
iwidget://settings?scroll=festivals
```


---

## Widget & Control Center Verhalten

- Tippen Sie auf ein **home-screen-board**, wenn **intercept taps** ausgeschaltet ist, kann öffnen `iwidget://today` (oder Ihr konfiguriertes offenes Verhalten über widget Absicht).
- **Lock Screen** und **Control Center** Einträge verwenden App Intents; sie sind keine zusätzlichen URL-Hosts.
- **Mac Menüleiste** Kalender verwendet das gleiche "Tag" URL-Muster, wenn Sie auf ein Datum klicken.

---

## Abkürzungen

1. Fügen Sie ** URL ** hinzu und fügen Sie einen `iwidget://` -Link ein.
2. Für **Workday**-Checks suchen Sie in der Aktionsbibliothek Shortcuts nach der **Work/Ruhetag**-Absicht von iWidget und geben Sie ein Datum an – es ist **not** als URL-Abfrage verfügbar.

[Zurück zu iWidget Support](../) · [FAQ](../faq) · [Privacy Policy](../privacy]


