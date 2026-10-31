iWidget versteht **`iwidget://`** auf **iPhone, iPad und Mac**. Nutzen Sie Safari, Kurzbefehle, andere Apps oder einen QR-Code. Gesprochene Mond-/Festtage ohne App-Start: Siri. Werktag: separates Workday-Intent, keine URL.

`iwidget://<host>[?query]` — unbekannte Hosts werden ignoriert.

| Host | Öffnet | Query |
|------|--------|-------|
| `today` | Heute | — |
| `day` | Heute → Tagesdetail | `y` `m` `d` |
| `library` | Bibliothek | `preset=` / `set=`, `detail=1` |
| `mine` | Meine Widgets | `design=` / `id=`, `preset=` / `set=` |
| `editor` | Editor | `design=` / `id=` (sonst zuletzt) |
| `import` | Import | — |
| `settings` | Einstellungen | `scroll=festivals` · `weather` · `editor` · `access` |
| `membership` | Mitgliedschaft | pausierte Widgets öffnen dies |
| `launch` | Starter-Handoff (iOS) | vom Widget |

Beispiele: `iwidget://today` · `iwidget://library?set=small.calendar&detail=1` · `iwidget://membership`

[Zurück zum Support](../) · [FAQ](../faq) · [Mitgliedschaft](../membership) · [Datenschutz](../privacy)
