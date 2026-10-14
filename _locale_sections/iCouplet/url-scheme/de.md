iCouplet unterstützt ** `icouplet://` ** Shortcut Links (URL-Schema). Kaltstart- und Home Screen-Verknüpfungen werden über einen einheitlichen Puffer geliefert, so dass Links nach dem Onboarding nicht zweimal geöffnet werden.

## Linkformat


```
icouplet://{host}?{params}
```


## Couplets & Autoren

| URL | Öffnet |
|-----|-------|
| `icouplet://couplet?id={id}` | Einzelheiten der Kupplung |
| `icouplet://poem?id={id}` | Gleiches wie Couplet (Kompatibilitätsalias) |
| `icouplet://author?id={id}` | Angaben zum Autor (联家) |
| `icouplet://recite` | Recite Flow (Auto-Sprache, wenn möglich) |
| `icouplet://recite?id={id}` | Open Couplet und Auto-Recite |

## Entdecken

| URL | Öffnet |
|-----|-------|
| `icouplet://home` | Register „Start“ |
| `icouplet://daily` | Das heutige tägliche Paar |
| `icouplet://random` | Zufallspaar |
| `icouplet://favorites` | Favoriten |
| `icouplet://famous` | Berühmte Linienliste |
| `icouplet://search` | Suche |
| `icouplet://search?q={query}` | Suche mit Suchbegriff |
| `icouplet://study` | Studie / 对对子 Eintrag |
| `icouplet://categories` | Kategorien durchsuchen |
| `icouplet://categories?section=form` | Formular (体裁) Abschnitt |
| `icouplet://categories?section=theme` | Themenbereich |
| `icouplet://categories?section=author` | Autorenteil |
| `icouplet://categories?section=famous` | Berühmter Streckenabschnitt |
| `icouplet://categories?section=corpus` | Sammlungen/Corpus |
| `icouplet://last-read` | Zuletzt gelesenes Paar |
| `icouplet://reading-history` | Leseverlauf |

## Einstellungen & Anleitungen

| URL | Öffnet |
|-----|-------|
| `icouplet://settings` | Grundeinstellungen |
| `icouplet://usage-guide` | Nutzungsanleitung |
| `icouplet://widget-guide` | Widget-Anleitung |
| `icouplet://shortcuts-guide` | Kurzbefehle-Anleitung |
| `icouplet://feature-guide` | Wiedergabefunktion Onboarding |
| `icouplet://feedback` | Feedback-E-Mail |
| `icouplet://in-app-review` | In-App- / App-Store-Bewertung |

## Beispiele


```
icouplet://daily
icouplet://couplet?id=1
icouplet://recite?id=1
icouplet://search?q=春
icouplet://categories?section=famous
icouplet://widget-guide
```


Verwenden Sie diese in der Shortcuts-App, den Schnellaktionen für den Startbildschirm, den Widgets oder Safari. Siehe auch In-App **Settings → Shortcuts Guide**.


