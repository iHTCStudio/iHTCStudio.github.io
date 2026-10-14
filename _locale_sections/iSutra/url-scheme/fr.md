iSutra prend en charge les liens raccourcis **      ** (schéma URL). Les raccourcis de démarrage à froid et d'écran d'accueil sont livrés via un tampon unifié de sorte que les liens ne sont pas ouverts deux fois après l'embarquement.

## Format de lien


```
isutra://{host}?{params}
```


## Sutras & auteurs

| URL | Ouvre |
|-----|-------|
| `isutra://passage?id={id}` | Détail Sutra |
| `isutra://couplet?id={id}` / `isutra://poem?id={id}` | Même chose que le passage (compatibilité) |
| `isutra://author?id={id}` | Traducteur / détail de l'auteur |
| `isutra://recite` / `isutra://recite?id={id}` | Flux de récitation |
| `isutra://large?id=diamond` / `isutra://large?id=dizang` | Catalogue grand volume de livres |

## Découverte et pratique

| URL | Ouvre |
|-----|-------|
| `isutra://home` | Accueil |
| `isutra://daily` | Aujourd'hui |
| `isutra://random` | Passage aléatoire |
| `isutra://favorites` | Favoris |
| `isutra://famous` | Vers célèbres |
| `isutra://search` / `isutra://search?q={query}` | Recherche |
| `isutra://study` | Salle d'étude |
| `isutra://hunt` | Chasse; alias « chasse aux mots clés » / « fleurs volantes » |
| `isutra://count` | Chant de poisson en bois (`chant` / `muyu` / `counter`) |
| `isutra://copy` / `isutra://copy?id={id}` | Copie-sutra (iOS) |
| `isutra://practice` | Entraînement matin / soir |
| `isutra://mastered` | Maîtrise |
| `isutra://categories` / `isutra://categories?section=` | Parcourir |
| `isutra://collection?id=` | Collecte (par exemple, "prajna", "quarante-deux"; aussi "nom=") |
| `isutra://theme?id=` | Thème (par exemple "xingyuan", "yaoshi", "plateforme") |
| `isutra://last-read` | Dernière lecture |
| `isutra://reading-history` | Historique de lecture |
| `isutra://notes` | Notes |

## Réglages et guides

| URL | Ouvre |
|-----|-------|
| `isutra://settings` | Réglages |
| `isutra://usage-guide` | Guide d'utilisation |
| `isutra://widget-guide` | Guide des widgets |
| `isutra://shortcuts-guide` | Guide Raccourcis |
| `isutra://feature-guide` | Rejouer l’accueil |
| `isutra://privacy` | Confidentialité dans l'application |
| `isutra://feedback` | E-mail de commentaires |
| `isutra://in-app-review` | Avis in-app / App Store |

## Exemples


```
isutra://daily
isutra://passage?id=1
isutra://large?id=diamond
isutra://count
isutra://copy?id=1
isutra://practice
isutra://collection?id=prajna
isutra://theme?id=xingyuan
isutra://study
isutra://hunt
```


Utilisez-les dans l'application Raccourcis, les actions rapides Home Screen, les widgets ou Safari. Voir aussi dans l'application **Paramètres → Guide des raccourcis**.


