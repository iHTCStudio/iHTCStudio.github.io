iPrimer unterstützt ** `iprimer://` ** Shortcut Links (URL-Schema). Kaltstart- und Home Screen-Verknüpfungen werden über einen einheitlichen Puffer geliefert, so dass Links nach dem Onboarding nicht zweimal geöffnet werden.

## Linkformat


```
iprimer://{host}?{params}
```


## Kapitel & Autoren

| URL | Öffnet |
|-----|-------|
| `iprimer://chapter?id={id}` | Einzelheiten des Kapitels |
| `iprimer://passage?id={id}` / `iprimer://poem?id={id}` | Wie Kapitel (Kompatibilität) |
| `iprimer://author?id={id}` | Autorendetail |
| `iprimer://recite` / `iprimer://recite?id={id}` | Rezitationsablauf |

## Entdecken

| URL | Öffnet |
|-----|-------|
| `iprimer://home` | Startseite |
| `iprimer://daily` | Die heutige tägliche Studie |
| `iprimer://random` | Zufallskapitel |
| `iprimer://favorites` | Favoriten |
| `iprimer://famous` | Berühmte Zeilen |
| `iprimer://search` / `iprimer://search?q={query}` | Suche |
| `iprimer://study` | Charakterstudie |
| `iprimer://meditation` | Meditationskursliste |
| `iprimer://meditation?slug={slug}&autostart=1` | Offene Sitzung und Autostart (Vordergrund) |
| `iprimer://guidance` | Lebensberatung (Journal & Gewohnheiten) |
| `iprimer://hunt` | Jagd (寻句); alias `keyword-hunt` / `flyflower` |
| `iprimer://mastered` | Mastered Chapters |
| `iprimer://categories` / `iprimer://categories?section=` | Durchsuchen |
| `iprimer://collection?id=xiaoxue` | Xiaoxue Collection (`name=` wird auch unterstützt) |
| `iprimer://theme?id=lijiao` | Volume / Theme (`name=立教` oder `Relationships` auch unterstützt) |
| `iprimer://last-read` | Zuletzt gelesen |
| `iprimer://reading-history` | Leseverlauf |
| `iprimer://notes` | Notizen |

## Einstellungen & Anleitungen

| URL | Öffnet |
|-----|-------|
| `iprimer://settings` | Einstellungen |
| `iprimer://usage-guide` | Nutzungsanleitung |
| `iprimer://widget-guide` | Widget-Anleitung |
| `iprimer://shortcuts-guide` | Kurzbefehle-Anleitung |
| `iprimer://feature-guide` | Einführung erneut abspielen |
| `iprimer://feedback` | Feedback-E-Mail |
| `iprimer://in-app-review` | In-App- / App-Store-Bewertung |

## Beispiele


```
iprimer://daily
iprimer://chapter?id=3
iprimer://collection?id=xiaoxue
iprimer://theme?id=lijiao
iprimer://study
iprimer://meditation?slug=emotion_calm&autostart=1
iprimer://guidance
iprimer://hunt
```


Verwenden Sie diese in der Shortcuts-App, den Schnellaktionen für den Startbildschirm, den Widgets oder Safari. Bevorzugt stabile `iprimer://` -Parameter, wenn verfügbar. Siehe auch In-App **Settings → Shortcuts Guide**.


