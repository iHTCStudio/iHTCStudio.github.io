iWuBi unterstützt ** `iWuBi://` ** (case-insensitive scheme `iwubi` ) tiefe Links — offenes Nachschlagen, tägliches Quiz, Favoriten, falsches Buch, Codelängenstufen, Lernhub oder Tippübung aus Safari, Shortcuts, Widgets oder einer anderen App.

## Protokoll


```
iWuBi://<host>[?query]
iWuBi:///path-style   ← host empty; first path segment is the action
```


| Host / action | Opens | Abfrage |
|---------------|-------|-------|
| `search` | Lookup tab, focus search | `q`, `word` oder `name` pre-fills |
| `word`, `char`, `character` | Word detail (or search if query empty) | `q` / `word` / `name` = Zeichen |
| `quiz`, `test` | Learn → Daily Quiz | — |
| `favorites`, `favorite` | Settings → Favourites | — |
| `wrong`, `mistakes`, `wrongbook` | Wrong book | `record=<UUID> → ein Datensatz |
| `levels`, `level`, `codes` | Levels tab | — |
| `learn`, `study` | Learn tab | — |
| `typing`, `type`, `practice` | Typing tab | — |

## Beispiele


```
iWuBi://search?q=你好
iWuBi://word?q=好
iWuBi://quiz
iWuBi://wrong?record=550E8400-E29B-41D4-A716-446655440000
iWuBi://levels
iWuBi://typing
```


## Home Bildschirm Schnelle Aktionen

Bis zu **4** in **Einstellungen → Home Screen Shortcuts **: `iWuBi://` , `iwubi` , `search` , `q` , `word` , `name` , `word` . **Feedback** und **review** sind nur Quick Action.

[Zurück zur Übersicht](..) · [FAQ](../faq) · [Privacy](../privacy]


