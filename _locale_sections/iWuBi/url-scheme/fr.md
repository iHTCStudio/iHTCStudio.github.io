iWuBi prend en charge ** `iWuBi://` ** (case-insensibilise scheme `iwubi` ) liens profonds — recherche ouverte, quiz quotidien, favoris, mauvais livre, niveaux de longueur de code, apprendre le hub ou la pratique de dactylographie de Safari, Raccourcis, widgets, ou une autre application.

## Protocole


```
iWuBi://<host>[?query]
iWuBi:///path-style   ← host empty; first path segment is the action
```


| Host / action | Opens | Demande |
|---------------|-------|-------|
| `search` | Lookup tab, focus search | `q`, `word` ou `name` pré-remplis |
| `word`, `char`, `character` | Word detail (or search if query empty) | `q` / `word` / `name` = caractère |
| `quiz`, `test` | Learn → Daily Quiz | — |
| `favorites`, `favorite` | Settings → Favourites | — |
| `wrong`, `mistakes`, `wrongbook` | Wrong book | `registr=<UUID>` → un enregistrement |
| `levels`, `level`, `codes` | Levels tab | — |
| `learn`, `study` | Learn tab | — |
| `typing`, `type`, `practice` | Typing tab | — |

## Exemples


```
iWuBi://search?q=你好
iWuBi://word?q=好
iWuBi://quiz
iWuBi://wrong?record=550E8400-E29B-41D4-A716-446655440000
iWuBi://levels
iWuBi://typing
```


## Actions rapides de l'écran d'accueil

Jusqu'à **4** dans **Paramètres → raccourcis d'écran d'accueil**: `iWuBi://` , `iwubi` , `search` , `q` , `word` , `name` , `word` . **Feedback** et **review** ne sont que des actions rapides.

[Retour à l'aperçu](..) · [FAQ](../faq) · [Confidentialité](../privacité)


