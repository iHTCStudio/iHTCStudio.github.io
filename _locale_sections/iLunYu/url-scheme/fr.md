iLunYu prend en charge les liens de raccourci ** `ilunyu://` ** (schéma URL). Les raccourcis de démarrage à froid et d'écran d'accueil sont livrés via un tampon unifié de sorte que les liens ne sont pas ouverts deux fois après l'embarquement.

## Format de lien


```
ilunyu://{host}?{params}
```


## Chapitres & auteurs

| URL | Ouvre |
|-----|-------|
| `ilunyu://passage?id={id}` | Détail du chapitre |
| `ilunyu://couplet?id={id}` / `ilunyu://poem?id={id}` | Même chose que le passage (compatibilité) |
| `ilunyu://author?id={id}` | Détail de l’auteur |
| `ilunyu://recite` | Flux de récitation |
| `ilunyu://recite?id={id}` | Ouvrir le chapitre et la lecture automatique |

## Découverte

| URL | Ouvre |
|-----|-------|
| `ilunyu://home` | Onglet Accueil |
| `ilunyu://daily` | Aujourd'hui verset quotidien |
| `ilunyu://random` | Chapitre aléatoire |
| `ilunyu://favorites` | Favoris |
| `ilunyu://famous` | Vers célèbres |
| `ilunyu://search` / `ilunyu://search?q={query}` | Recherche |
| `ilunyu://study` | Cours |
| `ilunyu://hunt` | Chasse () ; alias « chasse aux mots clés » / « fleurs volantes » |
| `ilunyu://mastered` / `ilunyu://progress` | Maîtrise / progrès |
| `ilunyu://categories` / `ilunyu://categories?section=` | Parcourir |
| `ilunyu://collection?id=lunyu` | Collection de livres (alias `book` / `form`; aussi `name=`) |
| `ilunyu://theme?id=` | Thème ou volume (par exemple `junzi`, `xue-er`; alias `suite` / `volume`) |
| `ilunyu://last-read` | Dernière lecture |
| `ilunyu://reading-history` | Historique de lecture |
| `ilunyu://notes` | Notes |

## Réglages et guides

| URL | Ouvre |
|-----|-------|
| `ilunyu://settings` | Réglages |
| `ilunyu://usage-guide` | Guide d'utilisation |
| `ilunyu://widget-guide` | Guide des widgets |
| `ilunyu://shortcuts-guide` | Guide Raccourcis |
| `ilunyu://feature-guide` | Rejouer l’accueil |
| `ilunyu://feedback` | E-mail de commentaires |
| `ilunyu://in-app-review` | Avis in-app / App Store |

## Exemples


```
ilunyu://daily
ilunyu://passage?id=1
ilunyu://recite?id=20
ilunyu://theme?id=junzi
ilunyu://study
ilunyu://hunt
```


Utilisez-les dans l'application Raccourcis, les actions rapides Home Screen, les widgets ou Safari. Voir aussi dans l'application **Paramètres → Guide des raccourcis**.


