iXin unterstützt ** `ixin://` ** Shortcut Links (URL-Schema). Kaltstart- und Home Screen-Verknüpfungen werden über einen einheitlichen Puffer geliefert, so dass Links nach dem Onboarding nicht zweimal geöffnet werden.

## Linkformat


```
ixin://{host}?{params}
```


## Passagen & Autoren

| URL | Öffnet |
|-----|-------|
| `ixin://passage?id={id}` | Passagen-Detail |
| `ixin://saying?id={id}` / `ixin://couplet?id={id}` / `ixin://poem?id={id}` | Wie Passage (Kompatibilität) |
| `ixin://passage?id={id}&card=1` | Angaben zum Durchgang und Kartenblatt |
| `ixin://card?id={id}` / `ixin://share-card?id={id}` | Insightkarten |
| `ixin://author?id={id}` | Autorendetail |
| `ixin://recite` / `ixin://recite?id={id}` | Rezitationsablauf |

## Entdeckung und Praxis

| URL | Öffnet |
|-----|-------|
| `ixin://home` | Startseite |
| `ixin://daily` | Tägliche Einsicht |
| `ixin://random` | Zufällige Passage |
| `ixin://favorites` | Favoriten |
| `ixin://famous` | Berühmte Zeilen |
| `ixin://search` / `ixin://search?q={query}` | Suche |
| `ixin://study` / `ixin://study?id={id}` | Herzschule |
| `ixin://hunt` | Heart Hunt (`keyword-hunt` / `flyflower`) |
| `ixin://handwriting` | Handschriftsuche (`handwrite`; iOS) |
| `ixin://mastered` | gemeistert („Fortschritt) |
| `ixin://categories` / `ixin://categories?section=` | Durchsuchen |
| `ixin://collection?id=` | Sammlung / Buch (`chuanxilu` / `daxuewen` / `jiaotiao` / `yilvwen` / Gedichte) |
| `ixin://corpus` | Alle Passagen (`all`) |
| `ixin://last-read` | Zuletzt gelesen |
| `ixin://reading-history` | Leseverlauf |
| `ixin://notes` | Notizen |
| `ixin://journal` | Knowing-Acting Journal |
| `ixin://liangzhi` | Drei Fragen von Liangzhi |
| `ixin://graph` | Konzeptgrafik |
| `ixin://timeline` | Annalen / Timeline |
| `ixin://map` | Karte |
| `ixin://people` | Menschen |
| `ixin://achievements` | Erfolge |
| `ixin://theme?id=` | Thema |

## Einstellungen & Anleitungen

| URL | Öffnet |
|-----|-------|
| `ixin://settings` | Einstellungen |
| `ixin://usage-guide` | Nutzungsanleitung |
| `ixin://widget-guide` | Widget-Anleitung |
| `ixin://shortcuts-guide` | Kurzbefehle-Anleitung |
| `ixin://feature-guide` | Einführung erneut abspielen |
| `ixin://feedback` | Feedback-E-Mail |
| `ixin://in-app-review` | In-App- / App-Store-Bewertung |

## Beispiele


```
ixin://daily
ixin://passage?id=1
ixin://journal
ixin://liangzhi
ixin://collection?id=chuanxilu
ixin://study
ixin://hunt
```


## Notizen

- Parameter sind fallsensibel, wo IDs numerisch sind.
- Siri, Shortcuts, Widgets und Control Center-Steuerelemente verwenden die gleichen Deep-Link-Routen.
- Sehen Sie sich die In-App **Einstellungen → Hilfe ** Anleitungen für die neueste Liste an.


