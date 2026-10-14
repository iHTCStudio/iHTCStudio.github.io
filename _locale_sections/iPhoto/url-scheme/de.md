iPhoto unterstützt ** `iphoto://` ** Deep Links und **App Intents / Siri Shortcuts**. Links navigieren nur innerhalb der App - sie laden keine Daten hoch.

## Regelung


```
iphoto://<host>[?query]
```


| Rule | Einzelheiten |
|------|--------|
| Scheme | „iphoto |
| Empty | Öffnet den Standard-Tab der App |
| Unknown hosts | Ignoriert sicher |

---

## Tabs & Navigation

| URL | Öffnet |
|-----|-------|
| `iphoto://library` | Bibliotheksregister |
| `iphoto://capture` | Fanglasche |
| `iphoto://settings` | Tab Einstellungen |
| `iphoto://search` | Such-Tab (iOS 18+) |
| `iphoto://recent-projects` | Bibliothek konzentriert sich auf die jüngsten Arbeiten |

---

## Herausgeber

| URL | Öffnet |
|-----|-------|
| `iphoto://editor?id=<projectID>` | Editor für die angegebene Projekt-ID |

---

## Leitfäden und Maßnahmen

| URL | Öffnet |
|-----|-------|
| `iphoto://usage-guide` | Nutzungsanleitung |
| `iphoto://widget-guide` | Widget-Anleitung |
| `iphoto://shortcuts-guide` | Kurzbefehle-Anleitung |
| `iphoto://feature-guide` | Feature / Onboarding Replay |
| `iphoto://export-presets` | Einstellungen für Ausfuhren |
| `iphoto://feedback` | Feedback-E-Mail |
| `iphoto://in-app-review` | In-App Review prompt |

---

## Siri & Shortcuts

Eingebaute Absichten umfassen:

- Open Capture
- Offene Bibliothek
- Importfotos
- Offene Einstellungen

Fügen Sie sie in der Shortcuts-App hinzu oder rufen Sie mit Siri die in Shortcuts gezeigten Phrasen auf.

## Beispiele


```
iphoto://capture
iphoto://library
iphoto://editor?id=YOUR-PROJECT-ID
iphoto://widget-guide
```


[FAQ](../faq) · [Privacy Policy](../Privacy) · [Zurück zu iPhoto](../]


