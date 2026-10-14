iArtOfWar prend en charge les liens de raccourci ** `iartofwar://` ** (schéma URL). Les raccourcis de démarrage à froid et d'écran d'accueil sont livrés via un tampon unifié de sorte que les liens ne sont pas ouverts deux fois après l'embarquement.

## Format de lien


```
iartofwar://{host}?{params}
```


## Passages et auteurs

| URL | Ouvre |
|-----|-------|
| `iartofwar://passage?id={id}` | Détail du passage |
| `iartofwar://couplet?id={id}` / `iartofwar://poem?id={id}` | Même chose que le passage (compatibilité) |
| `iartofwar://author?id={id}` | Détail de l’auteur |
| `iartofwar://recite` / `iartofwar://recite?id={id}` | Flux de récitation |

## Découverte

| URL | Ouvre |
|-----|-------|
| `iartofwar://home` | Accueil |
| `iartofwar://daily` | Aujourd'hui |
| `iartofwar://random` | Passage aléatoire |
| `iartofwar://favorites` | Favoris |
| `iartofwar://famous` | Lignes célèbres / stratagèmes |
| `iartofwar://search` / `iartofwar://search?q={query}` | Recherche |
| `iartofwar://study` | Salle de classe stratégique |
| `iartofwar://hunt` | Chasse () ; alias « chasse aux mots clés » / « fleurs volantes » |
| `iartofwar://mastered` | Maîtrise |
| `iartofwar://categories` / `iartofwar://categories?section=` | Parcourir (`theme`, `volume`, ...) |
| `iartofwar://collection?id=` | Collection de livres (par exemple `sunzi`, `wujing`, `wuzi`; aussi `name=` / `theme=`) |
| `iartofwar://theme?id=` | Suite ou volume Stratagem (par exemple "wen-tao", "winning", "sunbin-a") |
| `iartofwar://last-read` | Dernière lecture |
| `iartofwar://reading-history` | Historique de lecture |
| `iartofwar://notes` | Notes |

## Réglages et guides

| URL | Ouvre |
|-----|-------|
| `iartofwar://settings` | Réglages |
| `iartofwar://usage-guide` | Guide d'utilisation |
| `iartofwar://widget-guide` | Guide des widgets |
| `iartofwar://shortcuts-guide` | Guide Raccourcis |
| `iartofwar://feature-guide` | Rejouer l’accueil |
| `iartofwar://feedback` | E-mail de commentaires |
| `iartofwar://in-app-review` | Avis in-app / App Store |

## Exemples


```
iartofwar://daily
iartofwar://passage?id=1
iartofwar://collection?id=wuzi
iartofwar://theme?id=wen-tao
iartofwar://study
iartofwar://hunt
```


Utilisez-les dans l'application Raccourcis, les actions rapides Home Screen, les widgets ou Safari. Voir aussi dans l'application **Paramètres → Guide des raccourcis**.


