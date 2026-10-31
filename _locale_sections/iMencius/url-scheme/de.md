iMencius unterstützt ** `imencius://` ** Shortcut Links (URL-Schema). Kaltstart- und Home Screen-Verknüpfungen werden über einen einheitlichen Puffer geliefert, so dass Links nach dem Onboarding nicht zweimal geöffnet werden.

## Linkformat


```
imencius://{host}?{params}
```


## Passagen & Autoren

| URL | Öffnet |
|-----|-------|
| `imencius://passage?id={id}` | Passagen-Detail |
| `imencius://saying?id={id}` / `imencius://couplet?id={id}` / `imencius://poem?id={id}` | Wie Passage (Kompatibilität) |
| `imencius://passage?id={id}&card=1` | Angaben zum Durchgang und Kartenblatt |
| `imencius://card?id={id}` / `imencius://share-card?id={id}` | 孟 Karten |
| `imencius://author?id={id}` | Autorendetail |
| `imencius://recite` / `imencius://recite?id={id}` | Rezitationsablauf |

## Entdeckung und Praxis

| URL | Öffnet |
|-----|-------|
| `imencius://home` | Startseite |
| `imencius://daily` | Tägliches Sagen |
| `imencius://random` | Zufällige Passage |
| `imencius://favorites` | Favoriten |
| `imencius://famous` | Berühmte Zeilen |
| `imencius://search` / `imencius://search?q={query}` | Suche |
| `imencius://study` / `imencius://study?id={id}` | Qi-Studie fördern |
| `imencius://hunt` | Yi Hunt (`keyword-hunt` / `flyflower`) |
| `imencius://handwriting` | Handschriftsuche (`handwrite`; iOS) |
| `imencius://mastered` | gemeistert („Fortschritt) |
| `imencius://categories` / `imencius://categories?section=` | Durchsuchen |
| `imencius://collection?id=` | Sammlung/Buch |
| `imencius://corpus` | Alle Passagen (`all`) |
| `imencius://last-read` | Zuletzt gelesen |
| `imencius://reading-history` | Leseverlauf |
| `imencius://notes` | Notizen |
| `imencius://fables` / `imencius://allegories` / `imencius://concepts` | Spezialregale, wenn verfügbar |

## Einstellungen & Anleitungen

| URL | Öffnet |
|-----|-------|
| `imencius://settings` | Einstellungen |
| `imencius://usage-guide` | Nutzungsanleitung |
| `imencius://widget-guide` | Widget-Anleitung |
| `imencius://shortcuts-guide` | Kurzbefehle-Anleitung |
| `imencius://feature-guide` | Einführung erneut abspielen |
| `imencius://feedback` | Feedback-E-Mail |
| `imencius://in-app-review` | In-App- / App-Store-Bewertung |

## Beispiele


```
imencius://daily
imencius://passage?id=1
imencius://study
imencius://hunt
```



