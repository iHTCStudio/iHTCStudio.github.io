iWidget prend en charge **`iwidget://`** sur **iPhone, iPad et Mac**. Safari, Raccourcis, une autre app ou un QR. Pour la lune / les fêtes à la voix sans ouvrir l’app : Siri. Jour ouvré : intent Workday, pas une URL.

`iwidget://<host>[?query]` — les hôtes inconnus sont ignorés.

| Host | Ouvre | Query |
|------|-------|-------|
| `today` | Aujourd’hui | — |
| `day` | Aujourd’hui → détail du jour | `y` `m` `d` |
| `library` | Bibliothèque | `preset=` / `set=`, `detail=1` |
| `mine` | Mes widgets | `design=` / `id=`, `preset=` / `set=` |
| `editor` | Éditeur | `design=` / `id=` (sinon le plus récent) |
| `import` | Import | — |
| `settings` | Réglages | `scroll=festivals` · `weather` · `editor` · `access` |
| `membership` | Adhésion | les widgets en pause ouvrent ceci |
| `launch` | Handoff d’un lanceur (iOS) | fourni par le widget |

Exemples : `iwidget://today` · `iwidget://library?set=small.calendar&detail=1` · `iwidget://membership`

[Retour au support](../) · [FAQ](../faq) · [Adhésion](../membership) · [Confidentialité](../privacy)
