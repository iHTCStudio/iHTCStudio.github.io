iMille supporte les liens de raccourci ** `ithousand://` ** (schéma URL). Les raccourcis de démarrage à froid et d'écran d'accueil sont livrés via un tampon unifié de sorte que les liens ne sont pas ouverts deux fois après l'embarquement.

## Format de lien


```
ithousand://{host}?{params}
```


## Passages, auteurs et personnages

| URL | Ouvre |
|-----|-------|
| `ithousand://passage?id={id}` | Détail du passage |
| `ithousand://passage?id={id}&open=study` | Passage → Salle des Primers |
| `ithousand://passage?id={id}&open=characters` | Passage → table de caractères |
| `ithousand://passage?id={id}&open=note` | Passage → note |
| `ithousand://author?id={id}` | Détail de l’auteur |
| `ithousand://recite` / `ithousand://recite?id={id}` | Flux de récitation |
| `ithousand://characters` | Bibliothèque de caractères |
| `ithousand://character?char=天` | Concentrez une carte de caractères |
| `ithousand://characters?id={id}` | Carte de caractère par ID |
| `ithousand://saved-characters` | Personnages sauvegardés |
| `ithousand://saved-famous` | Sauvé des lignes célèbres |

## Découverte

| URL | Ouvre |
|-----|-------|
| `ithousand://home` | Accueil |
| `ithousand://daily` | Aujourd'hui Ligne quotidienne |
| `ithousand://random` | Passage aléatoire |
| `ithousand://favorites` | Favoris |
| `ithousand://list?id={uuid}` | Une liste personnelle |
| `ithousand://famous` | Vers célèbres |
| `ithousand://search` / `ithousand://search?q={query}` | Recherche |
| `ithousand://study` | Salle d'introduction |
| `ithousand://hunt` | Chasse () ; alias « chasse aux mots clés » / « fleurs volantes » |
| `ithousand://mastered` | Maîtrise |
| `ithousand://categories` / `ithousand://categories?section=` | Parcourir |
| `ithousand://collection?id=qianziwen` | Primer collection (`nom=` également supporté) |
| `ithousand://theme?id=dizigui-filial` | Thème |
| `ithousand://last-read` | Dernière lecture |
| `ithousand://reading-history` | Historique de lecture |
| `ithousand://notes` | Notes |

## Réglages et guides

| URL | Ouvre |
|-----|-------|
| `ithousand://settings` | Réglages |
| `ithousand://privacy` | Confidentialité dans l'application |
| `ithousand://usage-guide` | Guide d'utilisation |
| `ithousand://widget-guide` | Guide des widgets |
| `ithousand://shortcuts-guide` | Guide Raccourcis |
| `ithousand://feature-guide` | Rejouer l’accueil |
| `ithousand://feedback` | E-mail de commentaires |
| `ithousand://in-app-review` | Avis in-app / App Store |

## Exemples


```
ithousand://daily
ithousand://passage?id=1
ithousand://passage?id=1&open=characters
ithousand://character?char=天
ithousand://collection?id=qianziwen
ithousand://study
ithousand://hunt
ithousand://saved-characters
```


Utilisez-les dans l'application Raccourcis, les actions rapides Home Screen, les widgets ou Safari. Préférez les paramètres stables `ithousand://` lorsque disponibles. Voir aussi dans l'application **Paramètres → Guide des raccourcis**.


