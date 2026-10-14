iSage supporte les liens de raccourci ** `isage://` ** (schéma URL). Les raccourcis de démarrage à froid et d'écran d'accueil sont livrés via un tampon unifié de sorte que les liens ne sont pas ouverts deux fois après l'embarquement.

## Format de lien


```
isage://{host}?{params}
```


## Sayings & auteurs

| URL | Ouvre |
|-----|-------|
| `isage://passage?id={id}` | Les détails |
| `isage://saying?id={id}` / `isage://couplet?id={id}` / `isage://poem?id={id}` | Même chose que le passage (compatibilité) |
| `isage://passage?id={id}&card=1` | Décrire les détails et la feuille de la fiche de sauge |
| `isage://card?id={id}` / `isage://share-card?id={id}` | Carte d'âge |
| `isage://author?id={id}` | Détail de l’auteur |
| `isage://recite` / `isage://recite?id={id}` | Flux de récitation |

## Découverte et pratique

| URL | Ouvre |
|-----|-------|
| `isage://home` | Accueil |
| `isage://daily` | Aujourd'hui la sagesse |
| `isage://random` | Aléatoire |
| `isage://favorites` | Favoris |
| `isage://famous` | Vers célèbres |
| `isage://search` / `isage://search?q={query}` | Recherche |
| `isage://study` / `isage://study?id={id}` | Académie des sages |
| `isage://hunt` | Chasse aux sages ( ' chasse aux mots clés ' / ' fleurs volantes ') |
| `isage://handwriting` | Recherche d'écriture (`handwrite`; iOS) |
| `isage://mastered` | Maîtrise ('progrès') |
| `isage://categories` / `isage://categories?section=` | Parcourir |
| `isage://collection?id=guxun` | Recension classique (`zhou-shang` / `zhou-xia`; aussi `book` / `form`) |
| `isage://corpus` | Toutes les paroles |
| `isage://theme?id=conduct` | Thème (par exemple: «culture», «apprentissage», «amitié», «ménage», «pauvreté», «virtue», «fortune», «discipline», «monde»), |
| `isage://last-read` | Dernière lecture |
| `isage://reading-history` | Historique de lecture |
| `isage://notes` | Notes |

## Réglages et guides

| URL | Ouvre |
|-----|-------|
| `isage://settings` | Réglages |
| `isage://usage-guide` | Guide d'utilisation |
| `isage://widget-guide` | Guide des widgets |
| `isage://shortcuts-guide` | Guide Raccourcis |
| `isage://feature-guide` | Rejouer l’accueil |
| `isage://feedback` | E-mail de commentaires |
| `isage://in-app-review` | Avis in-app / App Store |

## Exemples


```
isage://daily
isage://passage?id=1
isage://passage?id=1&card=1
isage://collection?id=guxun
isage://theme?id=conduct
isage://study
isage://hunt
isage://handwriting
```


## Notes

- Les paramètres sont sensibles aux cas où les ID sont numériques.
- Les commandes Siri, Shortcuts, Widgets et Control Center utilisent les mêmes itinéraires de liaison profonde.
- Voir la page d'application **Paramètres → Aide** pour la dernière liste.


