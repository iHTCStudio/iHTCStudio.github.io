iPrecepts prend en charge les liens de raccourci ** `iprecepts://` ** (schéma URL). Les raccourcis de démarrage à froid et d'écran d'accueil sont livrés via un tampon unifié de sorte que les liens ne sont pas ouverts deux fois après l'embarquement.

## Format de lien


```
iprecepts://{host}?{params}
```


## Passages et auteurs

| URL | Ouvre |
|-----|-------|
| `iprecepts://passage?id={id}` | Détail du passage |
| `iprecepts://saying?id={id}` / `iprecepts://couplet?id={id}` / `iprecepts://poem?id={id}` | Même chose que le passage (compatibilité) |
| `iprecepts://passage?id={id}&card=1` | Détails du passage et feuille de carte |
| `iprecepts://card?id={id}` / `iprecepts://share-card?id={id}` | Cartes préceptes |
| `iprecepts://author?id={id}` | Détail de l’auteur |
| `iprecepts://recite` / `iprecepts://recite?id={id}` | Flux de récitation |

## Découverte et pratique

| URL | Ouvre |
|-----|-------|
| `iprecepts://home` | Accueil |
| `iprecepts://daily` | Précepte quotidien |
| `iprecepts://random` | Passage aléatoire |
| `iprecepts://favorites` | Favoris |
| `iprecepts://famous` | Vers célèbres |
| `iprecepts://search` / `iprecepts://search?q={query}` | Recherche |
| `iprecepts://study` / `iprecepts://study?id={id}` | Étude familiale |
| `iprecepts://hunt` | Chasse au précepte ( ' chasse au mot clé ' / ' flyflower ') |
| `iprecepts://handwriting` | Recherche d'écriture (`handwrite`; iOS) |
| `iprecepts://mastered` | Maîtrise ('progrès') |
| `iprecepts://categories` / `iprecepts://categories?section=` | Parcourir |
| `iprecepts://collection?id=` | Collection / livre (zhuxi / zhubailu / yanshi / zuge / yuanshi / qian / tingxun / shortworks) |
| `iprecepts://corpus` | Tous les passages |
| `iprecepts://last-read` | Dernière lecture |
| `iprecepts://reading-history` | Historique de lecture |
| `iprecepts://notes` | Notes |
| `iprecepts://compare` | Comparaison parallèle |
| `iprecepts://theme?id=` | Thème |
| `iprecepts://authors` | Auteurs |

## Réglages et guides

| URL | Ouvre |
|-----|-------|
| `iprecepts://settings` | Réglages |
| `iprecepts://usage-guide` | Guide d'utilisation |
| `iprecepts://widget-guide` | Guide des widgets |
| `iprecepts://shortcuts-guide` | Guide Raccourcis |
| `iprecepts://feature-guide` | Rejouer l’accueil |
| `iprecepts://feedback` | E-mail de commentaires |
| `iprecepts://in-app-review` | Avis in-app / App Store |

## Exemples


```
iprecepts://daily
iprecepts://passage?id=1
iprecepts://passage?id=1&card=1
iprecepts://compare
iprecepts://collection?id=yanshi
iprecepts://study
iprecepts://hunt
```


## Notes

- Les paramètres sont sensibles aux cas où les ID sont numériques.
- Les commandes Siri, Shortcuts, Widgets et Control Center utilisent les mêmes itinéraires de liaison profonde.
- Voir la page d'application **Paramètres → Aide** pour la dernière liste.


