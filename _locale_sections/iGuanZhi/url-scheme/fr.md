iGuanZhi prend en charge les liens de raccourci ** `iguanzhi://` ** (schéma URL). Les raccourcis de démarrage à froid et d'écran d'accueil sont livrés via un tampon unifié de sorte que les liens ne sont pas ouverts deux fois après l'embarquement.

## Format de lien


```
iguanzhi://{host}?{params}
```


## Passages et auteurs

| URL | Ouvre |
|-----|-------|
| `iguanzhi://passage?id={id}` | Détail du passage |
| `iguanzhi://saying?id={id}` / `iguanzhi://couplet?id={id}` / `iguanzhi://poem?id={id}` | Même chose que le passage (compatibilité) |
| `iguanzhi://passage?id={id}&card=1` | Détails du passage et feuille de carte |
| `iguanzhi://card?id={id}` / `iguanzhi://share-card?id={id}` | Cartes |
| `iguanzhi://author?id={id}` | Détail de l’auteur |
| `iguanzhi://recite` / `iguanzhi://recite?id={id}` | Flux de récitation |

## Découverte et pratique

| URL | Ouvre |
|-----|-------|
| `iguanzhi://home` | Accueil |
| `iguanzhi://daily` | Aujourd'hui Essay |
| `iguanzhi://random` | Passage aléatoire |
| `iguanzhi://favorites` | Favoris |
| `iguanzhi://famous` | Vers célèbres |
| `iguanzhi://search` / `iguanzhi://search?q={query}` | Recherche |
| `iguanzhi://study` / `iguanzhi://study?id={id}` | Études classiques |
| `iguanzhi://hunt` | Chasse aux mots clés / chasse aux fleurs volantes |
| `iguanzhi://handwriting` | Recherche d'écriture (`handwrite`; iOS) |
| `iguanzhi://mastered` | Maîtrise ('progrès') |
| `iguanzhi://categories` / `iguanzhi://categories?section=` | Parcourir |
| `iguanzhi://collection?id=` | Collection / livre |
| `iguanzhi://corpus` | Tous les passages |
| `iguanzhi://last-read` | Dernière lecture |
| `iguanzhi://reading-history` | Historique de lecture |
| `iguanzhi://notes` | Notes |
| `iguanzhi://fables` / `iguanzhi://allegories` / `iguanzhi://concepts` | Étagères spéciales lorsque disponibles |

## Réglages et guides

| URL | Ouvre |
|-----|-------|
| `iguanzhi://settings` | Réglages |
| `iguanzhi://usage-guide` | Guide d'utilisation |
| `iguanzhi://widget-guide` | Guide des widgets |
| `iguanzhi://shortcuts-guide` | Guide Raccourcis |
| `iguanzhi://feature-guide` | Rejouer l’accueil |
| `iguanzhi://feedback` | E-mail de commentaires |
| `iguanzhi://in-app-review` | Avis in-app / App Store |

## Exemples


```
iguanzhi://daily
iguanzhi://passage?id=1
iguanzhi://study
iguanzhi://hunt
```



