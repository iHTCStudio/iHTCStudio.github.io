iHanFei prend en charge les liens de raccourci ** `ihanfei://` ** (système URL). Les raccourcis de démarrage à froid et d'écran d'accueil sont livrés via un tampon unifié de sorte que les liens ne sont pas ouverts deux fois après l'embarquement.

## Format de lien


```
ihanfei://{host}?{params}
```


## Passages et auteurs

| URL | Ouvre |
|-----|-------|
| `ihanfei://passage?id={id}` | Détail du passage |
| `ihanfei://saying?id={id}` / `ihanfei://couplet?id={id}` / `ihanfei://poem?id={id}` | Même chose que le passage (compatibilité) |
| `ihanfei://passage?id={id}&card=1` | Détails du passage et feuille de carte |
| `ihanfei://card?id={id}` / `ihanfei://share-card?id={id}` | Cartes |
| `ihanfei://author?id={id}` | Détail de l’auteur |
| `ihanfei://recite` / `ihanfei://recite?id={id}` | Flux de récitation |

## Découverte et pratique

| URL | Ouvre |
|-----|-------|
| `ihanfei://home` | Accueil |
| `ihanfei://daily` | Stratagème quotidien |
| `ihanfei://random` | Passage aléatoire |
| `ihanfei://favorites` | Favoris |
| `ihanfei://famous` | Vers célèbres |
| `ihanfei://search` / `ihanfei://search?q={query}` | Recherche |
| `ihanfei://study` / `ihanfei://study?id={id}` | Étude sur le légalisme |
| `ihanfei://hunt` | Chasse aux lois ( ' chasse aux mots clés ' / `flyflower ') |
| `ihanfei://handwriting` | Recherche d'écriture (`handwrite`; iOS) |
| `ihanfei://mastered` | Maîtrise ('progrès') |
| `ihanfei://categories` / `ihanfei://categories?section=` | Parcourir |
| `ihanfei://collection?id=` | Collection / livre |
| `ihanfei://corpus` | Tous les passages |
| `ihanfei://last-read` | Dernière lecture |
| `ihanfei://reading-history` | Historique de lecture |
| `ihanfei://notes` | Notes |
| `ihanfei://fables` / `ihanfei://allegories` / `ihanfei://concepts` | Étagères spéciales lorsque disponibles |

## Réglages et guides

| URL | Ouvre |
|-----|-------|
| `ihanfei://settings` | Réglages |
| `ihanfei://usage-guide` | Guide d'utilisation |
| `ihanfei://widget-guide` | Guide des widgets |
| `ihanfei://shortcuts-guide` | Guide Raccourcis |
| `ihanfei://feature-guide` | Rejouer l’accueil |
| `ihanfei://feedback` | E-mail de commentaires |
| `ihanfei://in-app-review` | Avis in-app / App Store |

## Exemples


```
ihanfei://daily
ihanfei://passage?id=1
ihanfei://study
ihanfei://hunt
```



