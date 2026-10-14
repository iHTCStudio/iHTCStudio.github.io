iSage unterstützt ** `isage://` ** Shortcut Links (URL-Schema). Kaltstart- und Home Screen-Verknüpfungen werden über einen einheitlichen Puffer geliefert, so dass Links nach dem Onboarding nicht zweimal geöffnet werden.

## Linkformat


```
isage://{host}?{params}
```


## Sprüche & Autoren

| URL | Öffnet |
|-----|-------|
| `isage://passage?id={id}` | Details sagen |
| `isage://saying?id={id}` / `isage://couplet?id={id}` / `isage://poem?id={id}` | Wie Passage (Kompatibilität) |
| `isage://passage?id={id}&card=1` | Details und Salbei-Kartenblatt |
| `isage://card?id={id}` / `isage://share-card?id={id}` | Salbeikarte |
| `isage://author?id={id}` | Autorendetail |
| `isage://recite` / `isage://recite?id={id}` | Rezitationsablauf |

## Entdeckung und Praxis

| URL | Öffnet |
|-----|-------|
| `isage://home` | Startseite |
| `isage://daily` | Die Weisheit von heute |
| `isage://random` | Zufälliges Sprichwort |
| `isage://favorites` | Favoriten |
| `isage://famous` | Berühmte Zeilen |
| `isage://search` / `isage://search?q={query}` | Suche |
| `isage://study` / `isage://study?id={id}` | Sage Akademie |
| `isage://hunt` | Sage Hunt (`keyword-hunt` / `flyflower`) |
| `isage://handwriting` | Handschriftsuche (`handwrite`; iOS) |
| `isage://mastered` | gemeistert („Fortschritt) |
| `isage://categories` / `isage://categories?section=` | Durchsuchen |
| `isage://collection?id=guxun` | Klassische Rezension (`zhou-shang` / `zhou-xia`; auch `book` / `form`) |
| `isage://corpus` | Alle Worte (`all`) |
| `isage://theme?id=conduct` | Thema (z.B. `Kultivierung`, `Lernen`, `Freundschaft`, `Haushalt`, `Wohlstand`, `Tugend`, `Geschick`, `Sprache`, `Loyalität`, `Fleiß`, `Welt`) |
| `isage://last-read` | Zuletzt gelesen |
| `isage://reading-history` | Leseverlauf |
| `isage://notes` | Notizen |

## Einstellungen & Anleitungen

| URL | Öffnet |
|-----|-------|
| `isage://settings` | Einstellungen |
| `isage://usage-guide` | Nutzungsanleitung |
| `isage://widget-guide` | Widget-Anleitung |
| `isage://shortcuts-guide` | Kurzbefehle-Anleitung |
| `isage://feature-guide` | Einführung erneut abspielen |
| `isage://feedback` | Feedback-E-Mail |
| `isage://in-app-review` | In-App- / App-Store-Bewertung |

## Beispiele


```
isage://daily
isage://passage?id=1
isage://passage?id=1&card=1
isage://collection?id=guxun
isage://theme?id=conduct
isage://study
isage://hunt
isage://handwriting
```


## Notizen

- Parameter sind fallsensibel, wo IDs numerisch sind.
- Siri, Shortcuts, Widgets und Control Center-Steuerelemente verwenden die gleichen Deep-Link-Routen.
- Sehen Sie sich die In-App **Einstellungen → Hilfe ** Anleitungen für die neueste Liste an.


