iDao unterstützt ** `idao://` ** Shortcut Links (URL-Schema). Kaltstart- und Home Screen-Verknüpfungen werden über einen einheitlichen Puffer geliefert, so dass Links nach dem Onboarding nicht zweimal geöffnet werden.

## Linkformat


```
idao://{host}?{params}
```


## Kapitel & Entdeckung

| URL | Öffnet |
|-----|-------|
| `idao://home` | Startseite |
| `idao://daily` | Das heutige tägliche Kapitel |
| `idao://random` | Zufallskapitel |
| `idao://chapter?id={id}` | Einzelheiten des Kapitels |
| `idao://recite` / `idao://recite?id={id}` | Rezitationsablauf |
| `idao://favorites` | Favoriten |
| `idao://famous` | Berühmte Zeilen |
| `idao://search` / `idao://search?q={query}` | Suche |
| `idao://study` | Studienhalle |
| `idao://hunt` | Suche das Tao (寻道) |
| `idao://mastered` | Beherrscht |
| `idao://categories` / `?section=` | Browse (optionaler Abschnitt) |
| `idao://book?id=` | Buchsammlung (`ddj` / `qingjing` / `yinfu`) |
| `idao://author` | Laozi intro |
| `idao://last-read` | Zuletzt gelesen |
| `idao://reading-history` | Leseverlauf |
| `idao://notes` | Notizen |

> Kompatibilitätsalias: `idao://` / `idao://home` → Kapitel; `idao://daily` → Studie; `idao://random` → Jagd; `idao://chapter?id={id}` → Autor; `idao://recite` → Kategorienabschnitt; `idao://recite?id={id}` → Kategorien.

## Einstellungen & Anleitungen

| URL | Öffnet |
|-----|-------|
| `idao://settings` | Einstellungen |
| `idao://usage-guide` | Nutzungsanleitung |
| `idao://widget-guide` | Widget-Anleitung |
| `idao://shortcuts-guide` | Kurzbefehle-Anleitung |
| `idao://feature-guide` | Einführung erneut abspielen |
| `idao://feedback` | Feedback-E-Mail |
| `idao://in-app-review` | In-App- / App-Store-Bewertung |

## Beispiele


```
idao://daily
idao://chapter?id=1
idao://recite?id=1
idao://study
idao://hunt
idao://famous
idao://book?id=ddj
idao://author
idao://search?q=上善若水
```


Verwenden Sie diese in der Shortcuts-App, den Schnellaktionen für den Startbildschirm, den Widgets, dem Control Center oder Safari. Siehe auch In-App **Settings → Shortcuts Guide**.


