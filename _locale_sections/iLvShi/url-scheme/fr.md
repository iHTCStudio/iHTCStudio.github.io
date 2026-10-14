iLvShi prend en charge les liens de raccourci ** `ilvshi://` ** (schéma URL). Les raccourcis de démarrage à froid et d'écran d'accueil sont livrés via un tampon unifié de sorte que les liens ne sont pas ouverts deux fois après l'embarquement.

## Format de lien


```
ilvshi://{host}?{params}
```


## Passages et auteurs

| URL | Ouvre |
|-----|-------|
| `ilvshi://passage?id={id}` | Détail du passage |
| `ilvshi://saying?id={id}` / `ilvshi://couplet?id={id}` / `ilvshi://poem?id={id}` | Même chose que le passage (compatibilité) |
| `ilvshi://passage?id={id}&card=1` | Détails du passage et feuille de carte |
| `ilvshi://card?id={id}` / `ilvshi://share-card?id={id}` | Cartes |
| `ilvshi://author?id={id}` | Détail de l’auteur |
| `ilvshi://recite` / `ilvshi://recite?id={id}` | Flux de récitation |

## Découverte et pratique

| URL | Ouvre |
|-----|-------|
| `ilvshi://home` | Accueil |
| `ilvshi://daily` | Passage quotidien |
| `ilvshi://random` | Passage aléatoire |
| `ilvshi://favorites` | Favoris |
| `ilvshi://famous` | Vers célèbres |
| `ilvshi://search` / `ilvshi://search?q={query}` | Recherche |
| `ilvshi://study` / `ilvshi://study?id={id}` | Étude printemps-automne |
| `ilvshi://hunt` | Chasse d'automne ( ' chasse aux mots clés ' / 'flyflower ') |
| `ilvshi://handwriting` | Recherche d'écriture (`handwrite`; iOS) |
| `ilvshi://mastered` | Maîtrise ('progrès') |
| `ilvshi://categories` / `ilvshi://categories?section=` | Parcourir |
| `ilvshi://collection?id=` | Collection / livre |
| `ilvshi://corpus` | Tous les passages |
| `ilvshi://last-read` | Dernière lecture |
| `ilvshi://reading-history` | Historique de lecture |
| `ilvshi://notes` | Notes |
| `ilvshi://fables` / `ilvshi://allegories` / `ilvshi://concepts` | Étagères spéciales lorsque disponibles |

## Réglages et guides

| URL | Ouvre |
|-----|-------|
| `ilvshi://settings` | Réglages |
| `ilvshi://usage-guide` | Guide d'utilisation |
| `ilvshi://widget-guide` | Guide des widgets |
| `ilvshi://shortcuts-guide` | Guide Raccourcis |
| `ilvshi://feature-guide` | Rejouer l’accueil |
| `ilvshi://feedback` | E-mail de commentaires |
| `ilvshi://in-app-review` | Avis in-app / App Store |

## Exemples


```
ilvshi://daily
ilvshi://passage?id=1
ilvshi://study
ilvshi://hunt
```



