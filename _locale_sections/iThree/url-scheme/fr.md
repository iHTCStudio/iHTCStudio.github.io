iTrois prend en charge les liens de raccourci ** `ithree://` ** (schéma URL). Les raccourcis de démarrage à froid et d'écran d'accueil sont livrés via un tampon unifié de sorte que les liens ne sont pas ouverts deux fois après l'embarquement.

## Format de lien


```
ithree://{host}?{params}
```


## Passages & découverte

| URL | Ouvre |
|-----|-------|
| `ithree://home` | Accueil |
| `ithree://daily` | Aujourd'hui Ligne quotidienne |
| `ithree://random` | Passage aléatoire |
| `ithree://passage?id={id}` | Détail du passage |
| `ithree://recite` / `ithree://recite?id={id}` | Flux de récitation |
| `ithree://favorites` | Favoris |
| `ithree://famous` | Vers célèbres |
| `ithree://search` / `ithree://search?q={query}` | Recherche |
| `ithree://study` | Cours |
| `ithree://quiz` | Quizz d'aujourd'hui |
| `ithree://hunt` | Chasse |
| `ithree://mastered` | Maîtrise |
| `ithree://categories` | Parcourir |
| `ithree://chapter?id={id}` | Chapitre |
| `ithree://stories` / `ithree://story?id={id}` | Histoires / détails de l'histoire |
| `ithree://books` / `ithree://book?id={id}` | Index classique / livre |
| `ithree://dynasties` / `ithree://dynasty?id={id}` | Dynasties / dynastie |
| `ithree://collection?id=` / `?name=` | Collection (ou livres si vide) |
| `ithree://last-read` | Dernière lecture |
| `ithree://reading-history` | Historique de lecture |
| `ithree://notes` | Notes |

> Note : `ithree://` est un alias de compatibilité et ouvre la correspondance **chapitre**.

## Réglages et guides

| URL | Ouvre |
|-----|-------|
| `ithree://settings` | Réglages |
| `ithree://usage-guide` | Guide d'utilisation |
| `ithree://widget-guide` | Guide des widgets |
| `ithree://shortcuts-guide` | Guide Raccourcis |
| `ithree://feature-guide` | Rejouer l’accueil |
| `ithree://feedback` | E-mail de commentaires |
| `ithree://in-app-review` | Avis in-app / App Store |
| `ithree://privacy` | Confidentialité dans l'application |

## Exemples


```
ithree://daily
ithree://passage?id=1
ithree://recite?id=1
ithree://study
ithree://hunt
ithree://quiz
ithree://stories
ithree://search?q=人之初
```


Utilisez-les dans l'application Raccourcis, Actions rapides Home Screen, Widgets, Control Center ou Safari. Voir aussi dans l'application **Paramètres → Guide des raccourcis**.


