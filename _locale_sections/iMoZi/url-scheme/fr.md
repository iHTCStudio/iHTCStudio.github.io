iMoZi prend en charge ** `imozi://` ** liens de raccourci (schéma URL). Les raccourcis de démarrage à froid et d'écran d'accueil sont livrés via un tampon unifié de sorte que les liens ne sont pas ouverts deux fois après l'embarquement.

## Format de lien


```
imozi://{host}?{params}
```


## Passages et auteurs

| URL | Ouvre |
|-----|-------|
| `imozi://passage?id={id}` | Détail du passage |
| `imozi://saying?id={id}` / `imozi://couplet?id={id}` / `imozi://poem?id={id}` | Même chose que le passage (compatibilité) |
| `imozi://passage?id={id}&card=1` | Détails du passage et feuille de carte |
| `imozi://card?id={id}` / `imozi://share-card?id={id}` | Cartes |
| `imozi://author?id={id}` | Détail de l’auteur |
| `imozi://recite` / `imozi://recite?id={id}` | Flux de récitation |

## Découverte et pratique

| URL | Ouvre |
|-----|-------|
| `imozi://home` | Accueil |
| `imozi://daily` | Aujourd'hui |
| `imozi://random` | Passage aléatoire |
| `imozi://favorites` | Favoris |
| `imozi://famous` | Vers célèbres |
| `imozi://search` / `imozi://search?q={query}` | Recherche |
| `imozi://study` / `imozi://study?id={id}` | Étude sur le mohisme |
| `imozi://hunt` | Chasse à la peine ( ' chasse aux mots clés ' / ' fleurs volantes ') |
| `imozi://handwriting` | Recherche d'écriture (`handwrite`; iOS) |
| `imozi://mastered` | Maîtrise ('progrès') |
| `imozi://categories` / `imozi://categories?section=` | Parcourir |
| `imozi://collection?id=` | Collection / livre |
| `imozi://corpus` | Tous les passages |
| `imozi://last-read` | Dernière lecture |
| `imozi://reading-history` | Historique de lecture |
| `imozi://notes` | Notes |
| `imozi://ask` | Demandez à Mozi |
| `imozi://fables` / `imozi://allegories` / `imozi://concepts` | Étagères spéciales lorsque disponibles |

## Réglages et guides

| URL | Ouvre |
|-----|-------|
| `imozi://settings` | Réglages |
| `imozi://usage-guide` | Guide d'utilisation |
| `imozi://widget-guide` | Guide des widgets |
| `imozi://shortcuts-guide` | Guide Raccourcis |
| `imozi://feature-guide` | Rejouer l’accueil |
| `imozi://feedback` | E-mail de commentaires |
| `imozi://in-app-review` | Avis in-app / App Store |

## Exemples


```
imozi://daily
imozi://passage?id=1
imozi://ask
imozi://study
imozi://hunt
```



