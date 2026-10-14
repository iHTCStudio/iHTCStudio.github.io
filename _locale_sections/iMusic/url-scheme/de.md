iMusic unterstützt ** `imusic://` ** Shortcut Links. Kaltstart und Home Screen Shortcuts durchlaufen einen einheitlichen Puffer, so dass ein Link nicht zweimal nach dem Onboarding geöffnet wird.

## Linkformat


```
imusic://{host}?{params}
```


Schema ist nur ** `imusic://` **.

## Home & Heute

| URL | Öffnet |
|-----|-------|
| `imusic://` / `imusic://home` | Startseite |
| `imusic://daily` / `imusic://today` | Daily Piece (Warteschlange ist nur dieser Track) |
| `imusic://random` | Roam (Ganzbibliothek shuffle) |
| `imusic://play` | Spiel |
| `imusic://last` / `imusic://lastheard` | Zuletzt gehört |

## Stücke und Künstler

| URL | Öffnet |
|-----|-------|
| `imusic://piece?id={id}` | Piece Guide (`passage` / `song` auch akzeptiert) |
| `imusic://artist?id={id}` / `imusic://artist?name={name}` | Artist Desk |
| `imusic://artists` / `imusic://singers` | Künstlerverzeichnis |
| `imusic://famous` / `imusic://lines` | Berühmte Zeilen |

Eine Share-Card-Fußzeile kann `imusic://` (Titel · Künstler) für Menschen hinzufügen. Matching verwendet immer noch nur ** `imusic` **.

## Browsen, Suchen & Hören

| URL | Öffnet |
|-----|-------|
| `imusic://categories` / `imusic://browse` | Browse (`section=catalog` / `all` / `allpieces` → All Pieces) |
| `imusic://collection?id={id}` | Collection (`id=col-all` ist die virtuelle All Pieces Liste) |
| `imusic://search` / `imusic://search?q={query}` | Suche |
| `imusic://favorites` | Favoriten |
| `imusic://later` | Favoriten, gescrollt nach Später |
| `imusic://lists` / `imusic://listenlists` | Listenlisten |
| `imusic://history` | Geschichte |
| `imusic://notes` | Notizen |
| `imusic://mastered` | fertig |
| `imusic://streak` / `imusic://footprint` | Streifen |

Das Öffnen eines einzelnen Stücks, der Minibar oder der Song ID setzt die Lesewarteschlange auf dieses Stück zurück. Das Öffnen aus einer Sammlung, einer Suche oder einem Künstler führt diese Liste, sodass Next / Previous verfügbar bleibt.

## Song ID, Schule & Stimmung

| URL | Öffnet |
|-----|-------|
| `imusic://recognize` / `imusic://shazam` | Song ID |
| `imusic://school` / `imusic://earschool` | Ohrschule |
| `imusic://timeline` / `imusic://corridor` | Era-Korridor |
| `imusic://compare` | Vergleichen Sie das Zuhören |
| `imusic://mood?id={id}` | Starten Sie diese Stimmung (`piece=` / `pieceId=` ist nur der Starttrack; die Stimmung stimmt immer noch mit `id` überein) |

## Einstellungen & Anleitungen

| URL | Öffnet |
|-----|-------|
| `imusic://settings` | Einstellungen |
| `imusic://usageguide` / `imusic://featureguide` | Verwendung/Feature Guide |
| `imusic://widgetguide` | Widget-Anleitung |
| `imusic://shortcutsguide` | Kurzbefehle-Anleitung |
| `imusic://feedback` | Feedback |
| `imusic://review` / `imusic://in-app-review` | In-App-Überprüfung (wenn der Store-Eintrag live ist) |

## Siri & Home Bildschirm

Fragen Sie Siri nach dem heutigen Stück, dem Roaming, der Suche oder den Favoriten, nachdem Sie Verknüpfungen hinzugefügt haben. Schnelle Aktionen für den Startbildschirm in **Settings → Shortcuts** konfigurieren. Vollständige Beispiele live im In-App Shortcuts Guide.

[FAQ](../faq) · [Privacy Policy](../Privacy) · [Support](../)


