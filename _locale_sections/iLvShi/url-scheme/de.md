iLvShi unterstützt ** `ilvshi://` ** Shortcut Links (URL-Schema). Kaltstart- und Home Screen-Verknüpfungen werden über einen einheitlichen Puffer geliefert, so dass Links nach dem Onboarding nicht zweimal geöffnet werden.

## Linkformat


```
ilvshi://{host}?{params}
```


## Passagen & Autoren

| URL | Öffnet |
|-----|-------|
| `ilvshi://passage?id={id}` | Passagen-Detail |
| `ilvshi://saying?id={id}` / `ilvshi://couplet?id={id}` / `ilvshi://poem?id={id}` | Wie Passage (Kompatibilität) |
| `ilvshi://passage?id={id}&card=1` | Angaben zum Durchgang und Kartenblatt |
| `ilvshi://card?id={id}` / `ilvshi://share-card?id={id}` | 秋 Karten |
| `ilvshi://author?id={id}` | Autorendetail |
| `ilvshi://recite` / `ilvshi://recite?id={id}` | Rezitationsablauf |

## Entdeckung und Praxis

| URL | Öffnet |
|-----|-------|
| `ilvshi://home` | Startseite |
| `ilvshi://daily` | Tägliche Passage |
| `ilvshi://random` | Zufällige Passage |
| `ilvshi://favorites` | Favoriten |
| `ilvshi://famous` | Berühmte Zeilen |
| `ilvshi://search` / `ilvshi://search?q={query}` | Suche |
| `ilvshi://study` / `ilvshi://study?id={id}` | Frühjahr-Herbst-Studie |
| `ilvshi://hunt` | Autumn Hunt (`keyword-hunt` / `flyflower`) |
| `ilvshi://handwriting` | Handschriftsuche (`handwrite`; iOS) |
| `ilvshi://mastered` | gemeistert („Fortschritt) |
| `ilvshi://categories` / `ilvshi://categories?section=` | Durchsuchen |
| `ilvshi://collection?id=` | Sammlung/Buch |
| `ilvshi://corpus` | Alle Passagen (`all`) |
| `ilvshi://last-read` | Zuletzt gelesen |
| `ilvshi://reading-history` | Leseverlauf |
| `ilvshi://notes` | Notizen |
| `ilvshi://fables` / `ilvshi://allegories` / `ilvshi://concepts` | Spezialregale, wenn verfügbar |

## Einstellungen & Anleitungen

| URL | Öffnet |
|-----|-------|
| `ilvshi://settings` | Einstellungen |
| `ilvshi://usage-guide` | Nutzungsanleitung |
| `ilvshi://widget-guide` | Widget-Anleitung |
| `ilvshi://shortcuts-guide` | Kurzbefehle-Anleitung |
| `ilvshi://feature-guide` | Einführung erneut abspielen |
| `ilvshi://feedback` | Feedback-E-Mail |
| `ilvshi://in-app-review` | In-App- / App-Store-Bewertung |

## Beispiele


```
ilvshi://daily
ilvshi://passage?id=1
ilvshi://study
ilvshi://hunt
```



