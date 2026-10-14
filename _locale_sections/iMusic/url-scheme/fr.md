iMusic supporte les liens de raccourci ** `imusic://` **. Cold start et Home Screen raccourcis passent par un tampon unifié de sorte qu'un lien n'est pas ouvert deux fois après l'embarquement.

## Format de lien


```
imusic://{host}?{params}
```


Le schéma est ** `imusic://` ** seulement.

## Accueil et aujourd'hui

| URL | Ouvre |
|-----|-------|
| `imusic://` / `imusic://home` | Accueil |
| `imusic://daily` / `imusic://today` | Daily Piece (queue est cette piste seulement) |
| `imusic://random` | Roam (bibliothèque entière) |
| `imusic://play` | Jouer |
| `imusic://last` / `imusic://lastheard` | Dernières nouvelles |

## Pièces & artistes

| URL | Ouvre |
|-----|-------|
| `imusic://piece?id={id}` | Guide de pièce (`passage` / `song` également accepté) |
| `imusic://artist?id={id}` / `imusic://artist?name={name}` | Bureau d'artiste |
| `imusic://artists` / `imusic://singers` | Répertoire des artistes |
| `imusic://famous` / `imusic://lines` | Vers célèbres |

Un pied de page de carte de partage peut ajouter `imusic://` (titre · artiste) pour les humains. La correspondance utilise toujours ** `imusic` seulement**.

## Parcourir, rechercher et écouter

| URL | Ouvre |
|-----|-------|
| `imusic://categories` / `imusic://browse` | Parcourir (`section=catalog` / `all` / `allpieces` → Toutes les pièces) |
| `imusic://collection?id={id}` | Collection (`id=col-all` est la liste virtuelle de toutes les pièces) |
| `imusic://search` / `imusic://search?q={query}` | Recherche |
| `imusic://favorites` | Favoris |
| `imusic://later` | Favoris, défilé à Plus tard |
| `imusic://lists` / `imusic://listenlists` | Listes d'écoute |
| `imusic://history` | Historique |
| `imusic://notes` | Notes |
| `imusic://mastered` | Terminé |
| `imusic://streak` / `imusic://footprint` | Streak |

Ouverture d'une seule pièce, la mini-bar, ou Song ID **resets** la file de lecture de cette pièce. Ouverture à partir d'une collection, d'une recherche, ou d'un artiste conserve cette liste si Prochain / Précédent séjour disponible.

## ID de chanson, école & humeur

| URL | Ouvre |
|-----|-------|
| `imusic://recognize` / `imusic://shazam` | ID de la chanson |
| `imusic://school` / `imusic://earschool` | École d'oreille |
| `imusic://timeline` / `imusic://corridor` | Corridor Era |
| `imusic://compare` | Comparer l'écoute |
| `imusic://mood?id={id}` | Démarrer cette humeur (`piece=` / `pieceId=` est la seule piste de départ; l'humeur correspond toujours `id`) |

## Réglages et guides

| URL | Ouvre |
|-----|-------|
| `imusic://settings` | Réglages |
| `imusic://usageguide` / `imusic://featureguide` | Guide d'utilisation / fonctionnalités |
| `imusic://widgetguide` | Guide des widgets |
| `imusic://shortcutsguide` | Guide Raccourcis |
| `imusic://feedback` | Commentaires |
| `imusic://review` / `imusic://in-app-review` | Revue de l'application (lorsque la liste des magasins est en direct) |

## Siri & Écran d'accueil

Demandez Siri pour aujourd'hui morceau, errez, recherchez, ou favoris après avoir ajouté des raccourcis. Configurez les actions rapides de l'écran d'accueil dans **Paramètres → Raccourcis**. Des exemples complets vivent dans le guide de raccourcis in-app.

[FAQ](../faq) · [Politique de confidentialité](../privacité) · [Soutien](../)


