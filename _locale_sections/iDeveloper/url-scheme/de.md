iDeveloper unterstützt ** `ideveloper://` ** Shortcut Links (URL-Schema). Kaltstart- und Home Screen-Verknüpfungen werden über einen einheitlichen Puffer geliefert, so dass Links nach dem Onboarding nicht zweimal geöffnet werden.

## Linkformat


```
ideveloper://{host}?{params}
```


## Tools & Browsing

| URL | Öffnet |
|-----|-------|
| `ideveloper://home` | Startseite |
| `ideveloper://tool?id={id}` | Werkzeugdetail (z.B. `json`, `base64`, `timestamp`) |
| `ideveloper://category?id={id}` | Kategorie (z. B. 'encoding') |
| `ideveloper://search` / `ideveloper://search?q={query}` | Suche |
| `ideveloper://favorites` | Favoriten |
| `ideveloper://history` | Betriebsgeschichte |
| `ideveloper://reference` / `ideveloper://reference?id={id}` | Referenzzentrum / Eingang |
| `ideveloper://new-snippet` | Neues Snippet |
| `ideveloper://focus` | Focus Timer / Live Activity Eintrag |
| `ideveloper://share?tool={id}` | Open Share Handoff in ein Tool (funktioniert mit der Share Extension + App Group Payload) |

## Einstellungen & Anleitungen

| URL | Öffnet |
|-----|-------|
| `ideveloper://settings` | Einstellungen |
| `ideveloper://usage-guide` | Nutzungsanleitung |
| `ideveloper://widget-guide` | Widget-Anleitung |
| `ideveloper://shortcuts-guide` | Kurzbefehle-Anleitung |
| `ideveloper://feature-guide` | Einführung erneut abspielen |
| `ideveloper://feedback` | Feedback-E-Mail |
| `ideveloper://in-app-review` | In-App- / App-Store-Bewertung |

## Beispiele


```
ideveloper://tool?id=json
ideveloper://search?q=base64
ideveloper://reference?id=http-200
ideveloper://favorites
ideveloper://focus
ideveloper://share?tool=json
ideveloper://category?id=encoding
```


Verwenden Sie diese in der Shortcuts-App, den Schnellaktionen für den Startbildschirm, den Widgets, dem Control Center oder Safari. Siehe auch In-App **Settings → Shortcuts Guide**.


