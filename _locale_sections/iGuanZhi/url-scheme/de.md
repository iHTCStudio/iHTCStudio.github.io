iGuanZhi unterstützt ** `iguanzhi://` ** Shortcut Links (URL-Schema). Kaltstart- und Home Screen-Verknüpfungen werden über einen einheitlichen Puffer geliefert, so dass Links nach dem Onboarding nicht zweimal geöffnet werden.

## Linkformat


```
iguanzhi://{host}?{params}
```


## Passagen & Autoren

| URL | Öffnet |
|-----|-------|
| `iguanzhi://passage?id={id}` | Passagen-Detail |
| `iguanzhi://saying?id={id}` / `iguanzhi://couplet?id={id}` / `iguanzhi://poem?id={id}` | Wie Passage (Kompatibilität) |
| `iguanzhi://passage?id={id}&card=1` | Angaben zum Durchgang und Kartenblatt |
| `iguanzhi://card?id={id}` / `iguanzhi://share-card?id={id}` | 古 Karten |
| `iguanzhi://author?id={id}` | Autorendetail |
| `iguanzhi://recite` / `iguanzhi://recite?id={id}` | Rezitationsablauf |

## Entdeckung und Praxis

| URL | Öffnet |
|-----|-------|
| `iguanzhi://home` | Startseite |
| `iguanzhi://daily` | Der heutige Essay |
| `iguanzhi://random` | Zufällige Passage |
| `iguanzhi://favorites` | Favoriten |
| `iguanzhi://famous` | Berühmte Zeilen |
| `iguanzhi://search` / `iguanzhi://search?q={query}` | Suche |
| `iguanzhi://study` / `iguanzhi://study?id={id}` | Klassiker Studie |
| `iguanzhi://hunt` | Essay Hunt ('keyword-hunt' / 'flyflower') |
| `iguanzhi://handwriting` | Handschriftsuche (`handwrite`; iOS) |
| `iguanzhi://mastered` | gemeistert („Fortschritt) |
| `iguanzhi://categories` / `iguanzhi://categories?section=` | Durchsuchen |
| `iguanzhi://collection?id=` | Sammlung/Buch |
| `iguanzhi://corpus` | Alle Passagen (`all`) |
| `iguanzhi://last-read` | Zuletzt gelesen |
| `iguanzhi://reading-history` | Leseverlauf |
| `iguanzhi://notes` | Notizen |
| `iguanzhi://fables` / `iguanzhi://allegories` / `iguanzhi://concepts` | Spezialregale, wenn verfügbar |

## Einstellungen & Anleitungen

| URL | Öffnet |
|-----|-------|
| `iguanzhi://settings` | Einstellungen |
| `iguanzhi://usage-guide` | Nutzungsanleitung |
| `iguanzhi://widget-guide` | Widget-Anleitung |
| `iguanzhi://shortcuts-guide` | Kurzbefehle-Anleitung |
| `iguanzhi://feature-guide` | Einführung erneut abspielen |
| `iguanzhi://feedback` | Feedback-E-Mail |
| `iguanzhi://in-app-review` | In-App- / App-Store-Bewertung |

## Beispiele


```
iguanzhi://daily
iguanzhi://passage?id=1
iguanzhi://study
iguanzhi://hunt
```



