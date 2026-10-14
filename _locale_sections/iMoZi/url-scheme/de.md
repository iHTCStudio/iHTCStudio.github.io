iMoZi unterstützt ** `imozi://` ** Shortcut Links (URL-Schema). Kaltstart- und Home Screen-Verknüpfungen werden über einen einheitlichen Puffer geliefert, so dass Links nach dem Onboarding nicht zweimal geöffnet werden.

## Linkformat


```
imozi://{host}?{params}
```


## Passagen & Autoren

| URL | Öffnet |
|-----|-------|
| `imozi://passage?id={id}` | Passagen-Detail |
| `imozi://saying?id={id}` / `imozi://couplet?id={id}` / `imozi://poem?id={id}` | Wie Passage (Kompatibilität) |
| `imozi://passage?id={id}&card=1` | Angaben zum Durchgang und Kartenblatt |
| `imozi://card?id={id}` / `imozi://share-card?id={id}` | 墨 Karten |
| `imozi://author?id={id}` | Autorendetail |
| `imozi://recite` / `imozi://recite?id={id}` | Rezitationsablauf |

## Entdeckung und Praxis

| URL | Öffnet |
|-----|-------|
| `imozi://home` | Startseite |
| `imozi://daily` | Der heutige Mo |
| `imozi://random` | Zufällige Passage |
| `imozi://favorites` | Favoriten |
| `imozi://famous` | Berühmte Zeilen |
| `imozi://search` / `imozi://search?q={query}` | Suche |
| `imozi://study` / `imozi://study?id={id}` | Mohismus-Studie |
| `imozi://hunt` | Sentence Hunt (`keyword-hunt` / `flyflower`) |
| `imozi://handwriting` | Handschriftsuche (`handwrite`; iOS) |
| `imozi://mastered` | gemeistert („Fortschritt) |
| `imozi://categories` / `imozi://categories?section=` | Durchsuchen |
| `imozi://collection?id=` | Sammlung/Buch |
| `imozi://corpus` | Alle Passagen (`all`) |
| `imozi://last-read` | Zuletzt gelesen |
| `imozi://reading-history` | Leseverlauf |
| `imozi://notes` | Notizen |
| `imozi://ask` | Fragen Sie Mozi |
| `imozi://fables` / `imozi://allegories` / `imozi://concepts` | Spezialregale, wenn verfügbar |

## Einstellungen & Anleitungen

| URL | Öffnet |
|-----|-------|
| `imozi://settings` | Einstellungen |
| `imozi://usage-guide` | Nutzungsanleitung |
| `imozi://widget-guide` | Widget-Anleitung |
| `imozi://shortcuts-guide` | Kurzbefehle-Anleitung |
| `imozi://feature-guide` | Einführung erneut abspielen |
| `imozi://feedback` | Feedback-E-Mail |
| `imozi://in-app-review` | In-App- / App-Store-Bewertung |

## Beispiele


```
imozi://daily
imozi://passage?id=1
imozi://ask
imozi://study
imozi://hunt
```



