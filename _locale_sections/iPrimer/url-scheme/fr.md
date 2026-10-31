iPrimer prend en charge les liens de raccourci ** `iprimer://` ** (plan URL). Les raccourcis de démarrage à froid et d'écran d'accueil sont livrés via un tampon unifié de sorte que les liens ne sont pas ouverts deux fois après l'embarquement.

## Format de lien


```
iprimer://{host}?{params}
```


## Chapitres & auteurs

| URL | Ouvre |
|-----|-------|
| `iprimer://chapter?id={id}` | Détail du chapitre |
| `iprimer://passage?id={id}` / `iprimer://poem?id={id}` | Même chapitre (compatibilité) |
| `iprimer://author?id={id}` | Détail de l’auteur |
| `iprimer://recite` / `iprimer://recite?id={id}` | Flux de récitation |

## Découverte

| URL | Ouvre |
|-----|-------|
| `iprimer://home` | Accueil |
| `iprimer://daily` | Aujourd'hui |
| `iprimer://random` | Chapitre aléatoire |
| `iprimer://favorites` | Favoris |
| `iprimer://famous` | Vers célèbres |
| `iprimer://search` / `iprimer://search?q={query}` | Recherche |
| `iprimer://study` | Étude de caractère |
| `iprimer://meditation` | Liste des cours de méditation |
| `iprimer://meditation?slug={slug}&autostart=1` | Ouvrir la session et démarrer automatiquement (précédent) |
| `iprimer://guidance` | Guide de vie (journal & habitudes) |
| `iprimer://hunt` | Chasse () ; alias « chasse aux mots clés » / « fleurs volantes » |
| `iprimer://mastered` | Chapitres maîtrisables |
| `iprimer://categories` / `iprimer://categories?section=` | Parcourir |
| `iprimer://collection?id=xiaoxue` | Collection Xiaoxue (`nom=` également supporté) |
| `iprimer://theme?id=lijiao` | Volume / thème (`name=. |
| `iprimer://last-read` | Dernière lecture |
| `iprimer://reading-history` | Historique de lecture |
| `iprimer://notes` | Notes |

## Réglages et guides

| URL | Ouvre |
|-----|-------|
| `iprimer://settings` | Réglages |
| `iprimer://usage-guide` | Guide d'utilisation |
| `iprimer://widget-guide` | Guide des widgets |
| `iprimer://shortcuts-guide` | Guide Raccourcis |
| `iprimer://feature-guide` | Rejouer l’accueil |
| `iprimer://feedback` | E-mail de commentaires |
| `iprimer://in-app-review` | Avis in-app / App Store |

## Exemples


```
iprimer://daily
iprimer://chapter?id=3
iprimer://collection?id=xiaoxue
iprimer://theme?id=lijiao
iprimer://study
iprimer://meditation?slug=emotion_calm&autostart=1
iprimer://guidance
iprimer://hunt
```


Utilisez-les dans l'application Raccourcis, les actions rapides Home Screen, les widgets ou Safari. Préférez les paramètres stables `iprimer://` lorsque disponibles. Voir aussi dans l'application **Paramètres → Guide des raccourcis**.


