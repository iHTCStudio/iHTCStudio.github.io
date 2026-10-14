iXunZi prend en charge les liens de raccourci ** `ixunzi://` ** (schéma URL). Les raccourcis de démarrage à froid et d'écran d'accueil sont livrés via un tampon unifié de sorte que les liens ne sont pas ouverts deux fois après l'embarquement.

## Format de lien


```
ixunzi://{host}?{params}
```


## Passages et auteurs

| URL | Ouvre |
|-----|-------|
| `ixunzi://passage?id={id}` | Détail du passage |
| `ixunzi://saying?id={id}` / `ixunzi://couplet?id={id}` / `ixunzi://poem?id={id}` | Même chose que le passage (compatibilité) |
| `ixunzi://passage?id={id}&card=1` | Détails du passage et feuille de carte |
| `ixunzi://card?id={id}` / `ixunzi://share-card?id={id}` | Cartes |
| `ixunzi://author?id={id}` | Détail de l’auteur |
| `ixunzi://recite` / `ixunzi://recite?id={id}` | Flux de récitation |

## Découverte et pratique

| URL | Ouvre |
|-----|-------|
| `ixunzi://home` | Accueil |
| `ixunzi://daily` | Xun quotidien |
| `ixunzi://random` | Passage aléatoire |
| `ixunzi://favorites` | Favoris |
| `ixunzi://famous` | Vers célèbres |
| `ixunzi://search` / `ixunzi://search?q={query}` | Recherche |
| `ixunzi://study` / `ixunzi://study?id={id}` | Encourager l'Académie d'apprentissage |
| `ixunzi://hunt` | Xun Hunt ( ' chasse aux mots clés ' / ' flyflower ') |
| `ixunzi://handwriting` | Recherche d'écriture (`handwrite`; iOS) |
| `ixunzi://mastered` | Maîtrise ('progrès') |
| `ixunzi://categories` / `ixunzi://categories?section=` | Parcourir |
| `ixunzi://collection?id=` | Collection / livre |
| `ixunzi://corpus` | Tous les passages |
| `ixunzi://last-read` | Dernière lecture |
| `ixunzi://reading-history` | Historique de lecture |
| `ixunzi://notes` | Notes |
| `ixunzi://ask` | Demandez à Xunzi |
| `ixunzi://fables` / `ixunzi://allegories` / `ixunzi://concepts` | Étagères spéciales lorsque disponibles |

## Réglages et guides

| URL | Ouvre |
|-----|-------|
| `ixunzi://settings` | Réglages |
| `ixunzi://usage-guide` | Guide d'utilisation |
| `ixunzi://widget-guide` | Guide des widgets |
| `ixunzi://shortcuts-guide` | Guide Raccourcis |
| `ixunzi://feature-guide` | Rejouer l’accueil |
| `ixunzi://feedback` | E-mail de commentaires |
| `ixunzi://in-app-review` | Avis in-app / App Store |

## Exemples


```
ixunzi://daily
ixunzi://passage?id=1
ixunzi://ask
ixunzi://study
ixunzi://hunt
```



