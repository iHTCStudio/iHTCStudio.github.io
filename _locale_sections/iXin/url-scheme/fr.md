iXin prend en charge ** `ixin://` ** liens de raccourci (schéma URL). Les raccourcis de démarrage à froid et d'écran d'accueil sont livrés via un tampon unifié de sorte que les liens ne sont pas ouverts deux fois après l'embarquement.

## Format de lien


```
ixin://{host}?{params}
```


## Passages et auteurs

| URL | Ouvre |
|-----|-------|
| `ixin://passage?id={id}` | Détail du passage |
| `ixin://saying?id={id}` / `ixin://couplet?id={id}` / `ixin://poem?id={id}` | Même chose que le passage (compatibilité) |
| `ixin://passage?id={id}&card=1` | Détails du passage et feuille de carte |
| `ixin://card?id={id}` / `ixin://share-card?id={id}` | Cartes d'affichage |
| `ixin://author?id={id}` | Détail de l’auteur |
| `ixin://recite` / `ixin://recite?id={id}` | Flux de récitation |

## Découverte et pratique

| URL | Ouvre |
|-----|-------|
| `ixin://home` | Accueil |
| `ixin://daily` | Aperçu quotidien |
| `ixin://random` | Passage aléatoire |
| `ixin://favorites` | Favoris |
| `ixin://famous` | Vers célèbres |
| `ixin://search` / `ixin://search?q={query}` | Recherche |
| `ixin://study` / `ixin://study?id={id}` | École de cardiologie |
| `ixin://hunt` | Chasse au cœur ( ' chasse au mot clé ' / ' flyflower ') |
| `ixin://handwriting` | Recherche d'écriture (`handwrite`; iOS) |
| `ixin://mastered` | Maîtrise ('progrès') |
| `ixin://categories` / `ixin://categories?section=` | Parcourir |
| `ixin://collection?id=` | Collection / livre (`chuanxilu` / `daxuewen` / `jiaotiao` / `yilvwen` / poèmes) |
| `ixin://corpus` | Tous les passages |
| `ixin://last-read` | Dernière lecture |
| `ixin://reading-history` | Historique de lecture |
| `ixin://notes` | Notes |
| `ixin://journal` | Journal de connaissance-action |
| `ixin://liangzhi` | Trois questions de Liangzhi |
| `ixin://graph` | Graphique conceptuel |
| `ixin://timeline` | Annales / chronologie |
| `ixin://map` | Carte |
| `ixin://people` | Personnes |
| `ixin://achievements` | Réalisations |
| `ixin://theme?id=` | Thème |

## Réglages et guides

| URL | Ouvre |
|-----|-------|
| `ixin://settings` | Réglages |
| `ixin://usage-guide` | Guide d'utilisation |
| `ixin://widget-guide` | Guide des widgets |
| `ixin://shortcuts-guide` | Guide Raccourcis |
| `ixin://feature-guide` | Rejouer l’accueil |
| `ixin://feedback` | E-mail de commentaires |
| `ixin://in-app-review` | Avis in-app / App Store |

## Exemples


```
ixin://daily
ixin://passage?id=1
ixin://journal
ixin://liangzhi
ixin://collection?id=chuanxilu
ixin://study
ixin://hunt
```


## Notes

- Les paramètres sont sensibles aux cas où les ID sont numériques.
- Les commandes Siri, Shortcuts, Widgets et Control Center utilisent les mêmes itinéraires de liaison profonde.
- Voir la page d'application **Paramètres → Aide** pour la dernière liste.


