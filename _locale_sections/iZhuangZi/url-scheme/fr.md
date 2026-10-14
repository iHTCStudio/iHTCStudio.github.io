iZhuangZi prend en charge les liens de raccourci **   C   ** (système URL). Les raccourcis de démarrage à froid et d'écran d'accueil sont livrés via un tampon unifié de sorte que les liens ne sont pas ouverts deux fois après l'embarquement.

## Format de lien


```
izhuangzi://{host}?{params}
```


## Passages et auteurs

| URL | Ouvre |
|-----|-------|
| `izhuangzi://passage?id={id}` | Détail du passage |
| `izhuangzi://saying?id={id}` / `izhuangzi://couplet?id={id}` / `izhuangzi://poem?id={id}` | Même chose que le passage (compatibilité) |
| `izhuangzi://passage?id={id}&card=1` | Détails du passage et feuille de carte |
| `izhuangzi://card?id={id}` / `izhuangzi://share-card?id={id}` | Cartes |
| `izhuangzi://author?id={id}` | Détail de l’auteur |
| `izhuangzi://recite` / `izhuangzi://recite?id={id}` | Flux de récitation |

## Découverte et pratique

| URL | Ouvre |
|-----|-------|
| `izhuangzi://home` | Accueil |
| `izhuangzi://daily` | Zhuangzi quotidien |
| `izhuangzi://random` | Passage aléatoire |
| `izhuangzi://favorites` | Favoris |
| `izhuangzi://famous` | Vers célèbres |
| `izhuangzi://search` / `izhuangzi://search?q={query}` | Recherche |
| `izhuangzi://study` / `izhuangzi://study?id={id}` | Étude Dao |
| `izhuangzi://hunt` | Zhuang Hunt ( ' chasse aux mots clés ' / `flyflower ') |
| `izhuangzi://handwriting` | Recherche d'écriture (`handwrite`; iOS) |
| `izhuangzi://mastered` | Maîtrise ('progrès') |
| `izhuangzi://categories` / `izhuangzi://categories?section=` | Parcourir |
| `izhuangzi://collection?id=` | Collection / livre (`neipian` / `waipian` / `zapian`) |
| `izhuangzi://corpus` | Tous les passages |
| `izhuangzi://last-read` | Dernière lecture |
| `izhuangzi://reading-history` | Historique de lecture |
| `izhuangzi://notes` | Notes |
| `izhuangzi://ask` | Demandez à Zhuangzi |
| `izhuangzi://allegories` | Paraboles |
| `izhuangzi://concepts` | Concepts |
| `izhuangzi://theme?id=neipian` | Intérieur / Extérieur / Divers |

## Réglages et guides

| URL | Ouvre |
|-----|-------|
| `izhuangzi://settings` | Réglages |
| `izhuangzi://usage-guide` | Guide d'utilisation |
| `izhuangzi://widget-guide` | Guide des widgets |
| `izhuangzi://shortcuts-guide` | Guide Raccourcis |
| `izhuangzi://feature-guide` | Rejouer l’accueil |
| `izhuangzi://feedback` | E-mail de commentaires |
| `izhuangzi://in-app-review` | Avis in-app / App Store |

## Exemples


```
izhuangzi://daily
izhuangzi://passage?id=1
izhuangzi://ask
izhuangzi://allegories
izhuangzi://collection?id=neipian
izhuangzi://study
izhuangzi://hunt
```


## Notes

- Les paramètres sont sensibles aux cas où les ID sont numériques.
- Les commandes Siri, Shortcuts, Widgets et Control Center utilisent les mêmes itinéraires de liaison profonde.
- Voir la page d'application **Paramètres → Aide** pour la dernière liste.


