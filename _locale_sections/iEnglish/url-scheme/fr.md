iEnglish supporte ** `ienglish://` ** URL schéma de liens profonds — ouvrir un mot, le Daily Quiz, Favoris, mauvais livre, playlist ou des catégories de Safari, Raccourcis, widgets, ou une autre application.

**Actions rapides à l'écran d'accueil** (cliquez sur l'icône de l'application) ajouter Search, Feedback and Rate — ces types ne sont pas **** analysés par `ienglish://` , mais toujours ouvrir l'application via l'observateur du raccourci.

> **Note :** Liens seulement **navigate** dans l'application. Ils ne commencent pas la prononciation ou changent les paramètres d'étude à distance.

## Protocole


```
ienglish://<host>[?query]
```


| Rule | Détail |
|------|--------|
| **Scheme** | "ifrancais" (insensible aux cas) |
| **Word detail** | Hôte `word` — requête **`id=<wordID>`** (obligatoire, non vide) |
| **Quiz** | Hébergement "quiz" |
| **Favourites** | Accueillir des "favorites" |
| **Wrong book** | Host `wrong` ou `mistakes` — optionnel `record=<UUID>` ouvre une erreur |
| **Playlist** | Hôte `playlist` |
| **Categories** | Catégories d ' hôtes |

## Exemples


```
ienglish://word?id=apple
ienglish://quiz
ienglish://favorites
ienglish://wrong
ienglish://wrong?record=550E8400-E29B-41D4-A716-446655440000
ienglish://playlist
ienglish://categories
```


## Actions rapides de l'écran d'accueil

Configurez jusqu'à **4** dans **Paramètres → raccourcis d'écran d'accueil**. Les types comprennent : `ienglish://` , `IEnglishDeepLink` , `ienglish` , `word` , `id=<wordID>` , `quiz` , `favorites` — Recherche / Rétroaction / Examen ne sont fournis que sous forme de mesures rapides.

## Widget liens profonds

Les touches Widget utilisent les mêmes hôtes `ienglish://` (p. ex. Quiz quotidien → `IEnglishDeepLink` , Coup d'oeil favori → `ienglish` ).

[Retour à l'aperçu](..) · [FAQ](../faq) · [Confidentialité](../privacité)


