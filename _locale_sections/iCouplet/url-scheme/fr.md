iCouplet prend en charge les liens de raccourci ** `icouplet://` ** (schéma URL). Les raccourcis de démarrage à froid et d'écran d'accueil sont livrés via un tampon unifié de sorte que les liens ne sont pas ouverts deux fois après l'embarquement.

## Format de lien


```
icouplet://{host}?{params}
```


## Couplets & auteurs

| URL | Ouvre |
|-----|-------|
| `icouplet://couplet?id={id}` | Détail du couple |
| `icouplet://poem?id={id}` | Même chose que couplet (alias de compatibilité) |
| `icouplet://author?id={id}` | Description de l'auteur |
| `icouplet://recite` | Débit de récitation (parler automatiquement si possible) |
| `icouplet://recite?id={id}` | Ouvrir le couplet et la lecture automatique |

## Découverte

| URL | Ouvre |
|-----|-------|
| `icouplet://home` | Onglet Accueil |
| `icouplet://daily` | Aujourd'hui est le couplet quotidien |
| `icouplet://random` | Couplet aléatoire |
| `icouplet://favorites` | Favoris |
| `icouplet://famous` | Liste des lignes célèbres |
| `icouplet://search` | Recherche |
| `icouplet://search?q={query}` | Recherche avec requête |
| `icouplet://study` | Étude / Entrée |
| `icouplet://categories` | Parcourir les catégories |
| `icouplet://categories?section=form` | Section du formulaire |
| `icouplet://categories?section=theme` | Section thématique |
| `icouplet://categories?section=author` | Section d'auteur |
| `icouplet://categories?section=famous` | Section des lignes célèbres |
| `icouplet://categories?section=corpus` | Collections / corpus |
| `icouplet://last-read` | Dernière lecture couplet |
| `icouplet://reading-history` | Historique de lecture |

## Réglages et guides

| URL | Ouvre |
|-----|-------|
| `icouplet://settings` | Configuration racine |
| `icouplet://usage-guide` | Guide d'utilisation |
| `icouplet://widget-guide` | Guide des widgets |
| `icouplet://shortcuts-guide` | Guide Raccourcis |
| `icouplet://feature-guide` | Fonction de replay à bord |
| `icouplet://feedback` | E-mail de commentaires |
| `icouplet://in-app-review` | Avis in-app / App Store |

## Exemples


```
icouplet://daily
icouplet://couplet?id=1
icouplet://recite?id=1
icouplet://search?q=春
icouplet://categories?section=famous
icouplet://widget-guide
```


Utilisez-les dans l'application Raccourcis, les actions rapides Home Screen, les widgets ou Safari. Voir aussi dans l'application **Paramètres → Guide des raccourcis**.


