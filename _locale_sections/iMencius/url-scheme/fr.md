iMencius prend en charge les liens de raccourci ** `imencius://` ** (schéma URL). Les raccourcis de démarrage à froid et d'écran d'accueil sont livrés via un tampon unifié de sorte que les liens ne sont pas ouverts deux fois après l'embarquement.

## Format de lien


```
imencius://{host}?{params}
```


## Passages et auteurs

| URL | Ouvre |
|-----|-------|
| `imencius://passage?id={id}` | Détail du passage |
| `imencius://saying?id={id}` / `imencius://couplet?id={id}` / `imencius://poem?id={id}` | Même chose que le passage (compatibilité) |
| `imencius://passage?id={id}&card=1` | Détails du passage et feuille de carte |
| `imencius://card?id={id}` / `imencius://share-card?id={id}` | Cartes |
| `imencius://author?id={id}` | Détail de l’auteur |
| `imencius://recite` / `imencius://recite?id={id}` | Flux de récitation |

## Découverte et pratique

| URL | Ouvre |
|-----|-------|
| `imencius://home` | Accueil |
| `imencius://daily` | Dire quotidiennement |
| `imencius://random` | Passage aléatoire |
| `imencius://favorites` | Favoris |
| `imencius://famous` | Vers célèbres |
| `imencius://search` / `imencius://search?q={query}` | Recherche |
| `imencius://study` / `imencius://study?id={id}` | Favoriser l'étude du Qi |
| `imencius://hunt` | Yi Hunt (chasse de mots clés / flyflower) |
| `imencius://handwriting` | Recherche d'écriture (`handwrite`; iOS) |
| `imencius://mastered` | Maîtrise ('progrès') |
| `imencius://categories` / `imencius://categories?section=` | Parcourir |
| `imencius://collection?id=` | Collection / livre |
| `imencius://corpus` | Tous les passages |
| `imencius://last-read` | Dernière lecture |
| `imencius://reading-history` | Historique de lecture |
| `imencius://notes` | Notes |
| `imencius://fables` / `imencius://allegories` / `imencius://concepts` | Étagères spéciales lorsque disponibles |

## Réglages et guides

| URL | Ouvre |
|-----|-------|
| `imencius://settings` | Réglages |
| `imencius://usage-guide` | Guide d'utilisation |
| `imencius://widget-guide` | Guide des widgets |
| `imencius://shortcuts-guide` | Guide Raccourcis |
| `imencius://feature-guide` | Rejouer l’accueil |
| `imencius://feedback` | E-mail de commentaires |
| `imencius://in-app-review` | Avis in-app / App Store |

## Exemples


```
imencius://daily
imencius://passage?id=1
imencius://study
imencius://hunt
```



