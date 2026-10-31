iPrecepts unterstützt ** `iprecepts://` ** Shortcut Links (URL-Schema). Kaltstart- und Home Screen-Verknüpfungen werden über einen einheitlichen Puffer geliefert, so dass Links nach dem Onboarding nicht zweimal geöffnet werden.

## Linkformat


```
iprecepts://{host}?{params}
```


## Passagen & Autoren

| URL | Öffnet |
|-----|-------|
| `iprecepts://passage?id={id}` | Passagen-Detail |
| `iprecepts://saying?id={id}` / `iprecepts://couplet?id={id}` / `iprecepts://poem?id={id}` | Wie Passage (Kompatibilität) |
| `iprecepts://passage?id={id}&card=1` | Angaben zum Durchgang und Kartenblatt |
| `iprecepts://card?id={id}` / `iprecepts://share-card?id={id}` | Rezeptkarten |
| `iprecepts://author?id={id}` | Autorendetail |
| `iprecepts://recite` / `iprecepts://recite?id={id}` | Rezitationsablauf |

## Entdeckung und Praxis

| URL | Öffnet |
|-----|-------|
| `iprecepts://home` | Startseite |
| `iprecepts://daily` | Tägliches Rezept |
| `iprecepts://random` | Zufällige Passage |
| `iprecepts://favorites` | Favoriten |
| `iprecepts://famous` | Berühmte Zeilen |
| `iprecepts://search` / `iprecepts://search?q={query}` | Suche |
| `iprecepts://study` / `iprecepts://study?id={id}` | Familienstudie |
| `iprecepts://hunt` | Precept Hunt (`keyword-hunt` / `flyflower`) |
| `iprecepts://handwriting` | Handschriftsuche (`handwrite`; iOS) |
| `iprecepts://mastered` | gemeistert („Fortschritt) |
| `iprecepts://categories` / `iprecepts://categories?section=` | Durchsuchen |
| `iprecepts://collection?id=` | Sammlung / Buch (zhuxi / zhubailu / yanshi / zhuge / zeng / yuanshi / qian / tingxun / shortworks) |
| `iprecepts://corpus` | Alle Passagen (`all`) |
| `iprecepts://last-read` | Zuletzt gelesen |
| `iprecepts://reading-history` | Leseverlauf |
| `iprecepts://notes` | Notizen |
| `iprecepts://compare` | Parallelvergleich |
| `iprecepts://theme?id=` | Thema |
| `iprecepts://authors` | Autoren |

## Einstellungen & Anleitungen

| URL | Öffnet |
|-----|-------|
| `iprecepts://settings` | Einstellungen |
| `iprecepts://usage-guide` | Nutzungsanleitung |
| `iprecepts://widget-guide` | Widget-Anleitung |
| `iprecepts://shortcuts-guide` | Kurzbefehle-Anleitung |
| `iprecepts://feature-guide` | Einführung erneut abspielen |
| `iprecepts://feedback` | Feedback-E-Mail |
| `iprecepts://in-app-review` | In-App- / App-Store-Bewertung |

## Beispiele


```
iprecepts://daily
iprecepts://passage?id=1
iprecepts://passage?id=1&card=1
iprecepts://compare
iprecepts://collection?id=yanshi
iprecepts://study
iprecepts://hunt
```


## Notizen

- Parameter sind fallsensibel, wo IDs numerisch sind.
- Siri, Shortcuts, Widgets und Control Center-Steuerelemente verwenden die gleichen Deep-Link-Routen.
- Sehen Sie sich die In-App **Einstellungen → Hilfe ** Anleitungen für die neueste Liste an.


