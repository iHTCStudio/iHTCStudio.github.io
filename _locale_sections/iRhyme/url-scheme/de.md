iRhyme unterstützt ** `irhyme://` ** Shortcut Links (URL-Schema). Kaltstart- und Home Screen-Verknüpfungen werden über einen einheitlichen Puffer geliefert, so dass Links nach dem Onboarding nicht zweimal geöffnet werden.

## Linkformat


```
irhyme://{host}?{params}
```


## Passagen & Autoren

| URL | Öffnet |
|-----|-------|
| `irhyme://passage?id={id}` | Passagen-Detail |
| `irhyme://saying?id={id}` / `irhyme://couplet?id={id}` / `irhyme://poem?id={id}` | Wie Passage (Kompatibilität) |
| `irhyme://passage?id={id}&card=1` | Angaben zum Durchgang und Kartenblatt |
| `irhyme://card?id={id}` / `irhyme://share-card?id={id}` | Reimkarten |
| `irhyme://author?id={id}` | Autorendetail |
| `irhyme://recite` / `irhyme://recite?id={id}` | Rezitationsablauf |

## Entdeckung und Praxis

| URL | Öffnet |
|-----|-------|
| `irhyme://home` | Startseite |
| `irhyme://daily` | Der heutige Reim |
| `irhyme://random` | Zufällige Passage |
| `irhyme://favorites` | Favoriten |
| `irhyme://famous` | Berühmte Zeilen |
| `irhyme://search` / `irhyme://search?q={query}` | Suche |
| `irhyme://study` / `irhyme://study?id={id}` | Rhyme Akademie |
| `irhyme://hunt` | Rhyme Hunt (`keyword-hunt` / `flyflower`) |
| `irhyme://handwriting` | Handschriftsuche (`handwrite`; iOS) |
| `irhyme://mastered` | gemeistert („Fortschritt) |
| `irhyme://categories` / `irhyme://categories?section=` | Durchsuchen |
| `irhyme://collection?id=` | Sammlung/Buch (`shenglv`/`liweng`/`qianjia`/`youxue`) |
| `irhyme://corpus` | Alle Passagen (`all`) |
| `irhyme://last-read` | Zuletzt gelesen |
| `irhyme://reading-history` | Leseverlauf |
| `irhyme://notes` | Notizen |
| `irhyme://pair` | Parallelitätspraxis |
| `irhyme://prosody` | Prosodie Schreibtisch |
| `irhyme://rhyme?id=dong` | Eine Reimklasse |
| `irhyme://compare?rhyme=dong` | Gleicher Reim Vergleich |
| `irhyme://glossary?id=` | Glossar |

## Einstellungen & Anleitungen

| URL | Öffnet |
|-----|-------|
| `irhyme://settings` | Einstellungen |
| `irhyme://usage-guide` | Nutzungsanleitung |
| `irhyme://widget-guide` | Widget-Anleitung |
| `irhyme://shortcuts-guide` | Kurzbefehle-Anleitung |
| `irhyme://feature-guide` | Einführung erneut abspielen |
| `irhyme://feedback` | Feedback-E-Mail |
| `irhyme://in-app-review` | In-App- / App-Store-Bewertung |

## Beispiele


```
irhyme://daily
irhyme://passage?id=1001
irhyme://pair
irhyme://compare?rhyme=dong
irhyme://collection?id=shenglv
irhyme://study
irhyme://hunt
```


## Notizen

- Parameter sind fallsensibel, wo IDs numerisch sind.
- Siri, Shortcuts, Widgets und Control Center-Steuerelemente verwenden die gleichen Deep-Link-Routen.
- Sehen Sie sich die In-App **Einstellungen → Hilfe ** Anleitungen für die neueste Liste an.


