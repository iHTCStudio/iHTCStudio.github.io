iThousand unterstützt ** `ithousand://` ** Shortcut Links (URL-Schema). Kaltstart- und Home Screen-Verknüpfungen werden über einen einheitlichen Puffer geliefert, so dass Links nach dem Onboarding nicht zweimal geöffnet werden.

## Linkformat


```
ithousand://{host}?{params}
```


## Passagen, Autoren & Charaktere

| URL | Öffnet |
|-----|-------|
| `ithousand://passage?id={id}` | Passagen-Detail |
| `ithousand://passage?id={id}&open=study` | Passage: Primer Hall |
| `ithousand://passage?id={id}&open=characters` | Passage → Charaktertabelle |
| `ithousand://passage?id={id}&open=note` | Passage → Note |
| `ithousand://author?id={id}` | Autorendetail |
| `ithousand://recite` / `ithousand://recite?id={id}` | Rezitationsablauf |
| `ithousand://characters` | Charakterbibliothek |
| `ithousand://character?char=天` | Fokussieren einer Charakterkarte |
| `ithousand://characters?id={id}` | Zeichenkarte nach ID |
| `ithousand://saved-characters` | Gespeicherte Charaktere |
| `ithousand://saved-famous` | Berühmte Linien gerettet |

## Entdecken

| URL | Öffnet |
|-----|-------|
| `ithousand://home` | Startseite |
| `ithousand://daily` | Die heutige tägliche Linie |
| `ithousand://random` | Zufällige Passage |
| `ithousand://favorites` | Favoriten |
| `ithousand://list?id={uuid}` | Eine persönliche Liste (千单) |
| `ithousand://famous` | Berühmte Zeilen |
| `ithousand://search` / `ithousand://search?q={query}` | Suche |
| `ithousand://study` | Primer Hall |
| `ithousand://hunt` | Jagd (寻�); alias `keyword-hunt` / `flyflower` |
| `ithousand://mastered` | Beherrscht |
| `ithousand://categories` / `ithousand://categories?section=` | Durchsuchen |
| `ithousand://collection?id=qianziwen` | Primer Collection (`name=` wird ebenfalls unterstützt) |
| `ithousand://theme?id=dizigui-filial` | Thema |
| `ithousand://last-read` | Zuletzt gelesen |
| `ithousand://reading-history` | Leseverlauf |
| `ithousand://notes` | Notizen |

## Einstellungen & Anleitungen

| URL | Öffnet |
|-----|-------|
| `ithousand://settings` | Einstellungen |
| `ithousand://privacy` | In-App Datenschutz |
| `ithousand://usage-guide` | Nutzungsanleitung |
| `ithousand://widget-guide` | Widget-Anleitung |
| `ithousand://shortcuts-guide` | Kurzbefehle-Anleitung |
| `ithousand://feature-guide` | Einführung erneut abspielen |
| `ithousand://feedback` | Feedback-E-Mail |
| `ithousand://in-app-review` | In-App- / App-Store-Bewertung |

## Beispiele


```
ithousand://daily
ithousand://passage?id=1
ithousand://passage?id=1&open=characters
ithousand://character?char=天
ithousand://collection?id=qianziwen
ithousand://study
ithousand://hunt
ithousand://saved-characters
```


Verwenden Sie diese in der Shortcuts-App, den Schnellaktionen für den Startbildschirm, den Widgets oder Safari. Bevorzugt stabile `ithousand://` -Parameter, wenn verfügbar. Siehe auch In-App **Settings → Shortcuts Guide**.


