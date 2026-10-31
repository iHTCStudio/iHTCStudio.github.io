iZhuangZi unterstützt ** `izhuangzi://` ** Shortcut Links (URL-Schema). Kaltstart- und Home Screen-Verknüpfungen werden über einen einheitlichen Puffer geliefert, so dass Links nach dem Onboarding nicht zweimal geöffnet werden.

## Linkformat


```
izhuangzi://{host}?{params}
```


## Passagen & Autoren

| URL | Öffnet |
|-----|-------|
| `izhuangzi://passage?id={id}` | Passagen-Detail |
| `izhuangzi://saying?id={id}` / `izhuangzi://couplet?id={id}` / `izhuangzi://poem?id={id}` | Wie Passage (Kompatibilität) |
| `izhuangzi://passage?id={id}&card=1` | Angaben zum Durchgang und Kartenblatt |
| `izhuangzi://card?id={id}` / `izhuangzi://share-card?id={id}` | 逍遥 Karten |
| `izhuangzi://author?id={id}` | Autorendetail |
| `izhuangzi://recite` / `izhuangzi://recite?id={id}` | Rezitationsablauf |

## Entdeckung und Praxis

| URL | Öffnet |
|-----|-------|
| `izhuangzi://home` | Startseite |
| `izhuangzi://daily` | Tägliche Zhuangzi |
| `izhuangzi://random` | Zufällige Passage |
| `izhuangzi://favorites` | Favoriten |
| `izhuangzi://famous` | Berühmte Zeilen |
| `izhuangzi://search` / `izhuangzi://search?q={query}` | Suche |
| `izhuangzi://study` / `izhuangzi://study?id={id}` | Dao-Studie |
| `izhuangzi://hunt` | Zhuang Hunt (`keyword-hunt` / `flyflower`) |
| `izhuangzi://handwriting` | Handschriftsuche (`handwrite`; iOS) |
| `izhuangzi://mastered` | gemeistert („Fortschritt) |
| `izhuangzi://categories` / `izhuangzi://categories?section=` | Durchsuchen |
| `izhuangzi://collection?id=` | Sammlung/Buch (`neipian`/`waipian`/`zapian`) |
| `izhuangzi://corpus` | Alle Passagen (`all`) |
| `izhuangzi://last-read` | Zuletzt gelesen |
| `izhuangzi://reading-history` | Leseverlauf |
| `izhuangzi://notes` | Notizen |
| `izhuangzi://ask` | Fragen Sie Zhuangzi |
| `izhuangzi://allegories` | Gleichnisse |
| `izhuangzi://concepts` | Konzepte |
| `izhuangzi://theme?id=neipian` | Innerer / Äußerer / Verschiedenes |

## Einstellungen & Anleitungen

| URL | Öffnet |
|-----|-------|
| `izhuangzi://settings` | Einstellungen |
| `izhuangzi://usage-guide` | Nutzungsanleitung |
| `izhuangzi://widget-guide` | Widget-Anleitung |
| `izhuangzi://shortcuts-guide` | Kurzbefehle-Anleitung |
| `izhuangzi://feature-guide` | Einführung erneut abspielen |
| `izhuangzi://feedback` | Feedback-E-Mail |
| `izhuangzi://in-app-review` | In-App- / App-Store-Bewertung |

## Beispiele


```
izhuangzi://daily
izhuangzi://passage?id=1
izhuangzi://ask
izhuangzi://allegories
izhuangzi://collection?id=neipian
izhuangzi://study
izhuangzi://hunt
```


## Notizen

- Parameter sind fallsensibel, wo IDs numerisch sind.
- Siri, Shortcuts, Widgets und Control Center-Steuerelemente verwenden die gleichen Deep-Link-Routen.
- Sehen Sie sich die In-App **Einstellungen → Hilfe ** Anleitungen für die neueste Liste an.


