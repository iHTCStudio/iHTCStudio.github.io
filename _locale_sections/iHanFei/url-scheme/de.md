iHanFei unterstützt ** `ihanfei://` ** Shortcut Links (URL-Schema). Kaltstart- und Home Screen-Verknüpfungen werden über einen einheitlichen Puffer geliefert, so dass Links nach dem Onboarding nicht zweimal geöffnet werden.

## Linkformat


```
ihanfei://{host}?{params}
```


## Passagen & Autoren

| URL | Öffnet |
|-----|-------|
| `ihanfei://passage?id={id}` | Passagen-Detail |
| `ihanfei://saying?id={id}` / `ihanfei://couplet?id={id}` / `ihanfei://poem?id={id}` | Wie Passage (Kompatibilität) |
| `ihanfei://passage?id={id}&card=1` | Angaben zum Durchgang und Kartenblatt |
| `ihanfei://card?id={id}` / `ihanfei://share-card?id={id}` | Σ Karten |
| `ihanfei://author?id={id}` | Autorendetail |
| `ihanfei://recite` / `ihanfei://recite?id={id}` | Rezitationsablauf |

## Entdeckung und Praxis

| URL | Öffnet |
|-----|-------|
| `ihanfei://home` | Startseite |
| `ihanfei://daily` | Tägliche Stratagem |
| `ihanfei://random` | Zufällige Passage |
| `ihanfei://favorites` | Favoriten |
| `ihanfei://famous` | Berühmte Zeilen |
| `ihanfei://search` / `ihanfei://search?q={query}` | Suche |
| `ihanfei://study` / `ihanfei://study?id={id}` | Legalismusstudie |
| `ihanfei://hunt` | Law Hunt (`keyword-hunt` / `flyflower`) |
| `ihanfei://handwriting` | Handschriftsuche (`handwrite`; iOS) |
| `ihanfei://mastered` | gemeistert („Fortschritt) |
| `ihanfei://categories` / `ihanfei://categories?section=` | Durchsuchen |
| `ihanfei://collection?id=` | Sammlung/Buch |
| `ihanfei://corpus` | Alle Passagen (`all`) |
| `ihanfei://last-read` | Zuletzt gelesen |
| `ihanfei://reading-history` | Leseverlauf |
| `ihanfei://notes` | Notizen |
| `ihanfei://fables` / `ihanfei://allegories` / `ihanfei://concepts` | Spezialregale, wenn verfügbar |

## Einstellungen & Anleitungen

| URL | Öffnet |
|-----|-------|
| `ihanfei://settings` | Einstellungen |
| `ihanfei://usage-guide` | Nutzungsanleitung |
| `ihanfei://widget-guide` | Widget-Anleitung |
| `ihanfei://shortcuts-guide` | Kurzbefehle-Anleitung |
| `ihanfei://feature-guide` | Einführung erneut abspielen |
| `ihanfei://feedback` | Feedback-E-Mail |
| `ihanfei://in-app-review` | In-App- / App-Store-Bewertung |

## Beispiele


```
ihanfei://daily
ihanfei://passage?id=1
ihanfei://study
ihanfei://hunt
```



