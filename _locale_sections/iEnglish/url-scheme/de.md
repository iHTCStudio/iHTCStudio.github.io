iEnglisch unterstützt ** `ienglish://` ** URL-Schema Deep Links - öffnen Sie ein Wort, das Daily Quiz, Favoriten, Wrong Book, Playlist oder Kategorien von Safari, Shortcuts, Widgets oder einer anderen App.

**Home Screen Quick Actions** (langes Drücken des App-Symbols) fügen Sie Suchen, Feedback und Rate hinzu - diese Typen werden **nicht ** durch `ienglish://` analysiert, aber öffnen Sie die App trotzdem über den Shortcut-Beobachter.

> **Hinweis:** Links nur **navigieren** innerhalb der App. Sie beginnen nicht mit der Aussprache oder ändern die Studieneinstellungen aus der Ferne.

## Protokoll


```
ienglish://<host>[?query]
```


| Rule | Einzelheiten |
|------|--------|
| **Scheme** | `ienglish` (fallunempfindlich) |
| **Word detail** | Host `word` — abfrage **`id=<wordID>`** (erforderlich, nicht leer) |
| **Quiz** | Host "Quiz" |
| **Favourites** | Gastgeber `Favoriten` |
| **Wrong book** | Host `falsch` oder `Fehler` — optional `record=<UUID>` öffnet einen Fehler |
| **Playlist** | Host "Playlist" |
| **Categories** | Host "Kategorien" |

## Beispiele


```
ienglish://word?id=apple
ienglish://quiz
ienglish://favorites
ienglish://wrong
ienglish://wrong?record=550E8400-E29B-41D4-A716-446655440000
ienglish://playlist
ienglish://categories
```


## Home Bildschirm Schnelle Aktionen

Konfigurieren Sie bis zu **4** in **Einstellungen → Home Screen Shortcuts **. Zu den Typen gehören `ienglish://` , `IEnglishDeepLink` , `ienglish` , `word` , `id=<wordID>` , `quiz` , `favorites` Suchen / Feedback / Review werden nur als Quick Actions geliefert.

## Widget Deep Links

Widget-Haps verwenden die gleichen `ienglish://` -Hosts (z. B. Daily Quiz → `IEnglishDeepLink` , Favoritenblick → `ienglish` ).

[Zurück zur Übersicht](..) · [FAQ](../faq) · [Privacy](../privacy]


