iCoder prend en charge ** `iLeetCoder://` ** (insensible aux cas) les liens profonds — ouvrir un problème, quiz quotidien, favoris, mauvais livre, ou filtrer par tag / entreprise de Safari, Raccourcis, widgets, ou une autre application.

## Protocole

| Host | Opens | Demande |
|------|-------|-------|
| `problem` | Problem detail | `leetId=` ou `id=` (par exemple `1`, `206`) |
| `quiz` | Daily Quiz tab | — |
| `favorites` | Favourites list | — |
| `wrong`, `mistakes`, `wrongquestions` | Wrong book | `registr=<UUID>` → problème lié |
| `tag` | Problems filtered by tag | `nom=` |
| `company` | Problems filtered by company | `nom=` |

## Exemples


```
iLeetCoder://problem?leetId=1
iLeetCoder://problem?id=206
iLeetCoder://quiz
iLeetCoder://tag?name=Array
iLeetCoder://company?name=Google
iLeetCoder://wrong?record=550E8400-E29B-41D4-A716-446655440000
```


## Actions rapides de l'écran d'accueil

Jusqu'à **4** dans **Paramètres → raccourcis d'écran d'accueil**: `iLeetCoder://` , `problem` , `leetId=` , `id=` , `1` , `206` , `quiz` . Rechercher / catégories / feedback / review sont des canaux d'action rapide.

[Retour à l'aperçu](..) · [FAQ](../faq) · [Confidentialité](../privacité)


