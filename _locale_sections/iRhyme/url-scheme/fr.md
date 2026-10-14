iRhyme prend en charge les liens de raccourci ** `irhyme://` ** (schéma URL). Les raccourcis de démarrage à froid et d'écran d'accueil sont livrés via un tampon unifié de sorte que les liens ne sont pas ouverts deux fois après l'embarquement.

## Format de lien


```
irhyme://{host}?{params}
```


## Passages et auteurs

| URL | Ouvre |
|-----|-------|
| `irhyme://passage?id={id}` | Détail du passage |
| `irhyme://saying?id={id}` / `irhyme://couplet?id={id}` / `irhyme://poem?id={id}` | Même chose que le passage (compatibilité) |
| `irhyme://passage?id={id}&card=1` | Détails du passage et feuille de carte |
| `irhyme://card?id={id}` / `irhyme://share-card?id={id}` | Cartes de rythme |
| `irhyme://author?id={id}` | Détail de l’auteur |
| `irhyme://recite` / `irhyme://recite?id={id}` | Flux de récitation |

## Découverte et pratique

| URL | Ouvre |
|-----|-------|
| `irhyme://home` | Accueil |
| `irhyme://daily` | Aujourd'hui |
| `irhyme://random` | Passage aléatoire |
| `irhyme://favorites` | Favoris |
| `irhyme://famous` | Vers célèbres |
| `irhyme://search` / `irhyme://search?q={query}` | Recherche |
| `irhyme://study` / `irhyme://study?id={id}` | Académie de rythme |
| `irhyme://hunt` | Chasse aux rimes ( ' chasse aux mots clés ' / ' fleurs volantes ') |
| `irhyme://handwriting` | Recherche d'écriture (`handwrite`; iOS) |
| `irhyme://mastered` | Maîtrise ('progrès') |
| `irhyme://categories` / `irhyme://categories?section=` | Parcourir |
| `irhyme://collection?id=` | Collection / livre (`shenglv` / `liweng` / `qianjia` / `youxue`) |
| `irhyme://corpus` | Tous les passages |
| `irhyme://last-read` | Dernière lecture |
| `irhyme://reading-history` | Historique de lecture |
| `irhyme://notes` | Notes |
| `irhyme://pair` | La pratique du parallélisme |
| `irhyme://prosody` | Bureau de prosodie |
| `irhyme://rhyme?id=dong` | Une classe de rimes |
| `irhyme://compare?rhyme=dong` | Comparaison des mêmes rythmes |
| `irhyme://glossary?id=` | Glossaire |

## Réglages et guides

| URL | Ouvre |
|-----|-------|
| `irhyme://settings` | Réglages |
| `irhyme://usage-guide` | Guide d'utilisation |
| `irhyme://widget-guide` | Guide des widgets |
| `irhyme://shortcuts-guide` | Guide Raccourcis |
| `irhyme://feature-guide` | Rejouer l’accueil |
| `irhyme://feedback` | E-mail de commentaires |
| `irhyme://in-app-review` | Avis in-app / App Store |

## Exemples


```
irhyme://daily
irhyme://passage?id=1001
irhyme://pair
irhyme://compare?rhyme=dong
irhyme://collection?id=shenglv
irhyme://study
irhyme://hunt
```


## Notes

- Les paramètres sont sensibles aux cas où les ID sont numériques.
- Les commandes Siri, Shortcuts, Widgets et Control Center utilisent les mêmes itinéraires de liaison profonde.
- Voir la page d'application **Paramètres → Aide** pour la dernière liste.


