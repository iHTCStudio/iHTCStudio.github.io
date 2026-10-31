iDeveloper prend en charge les liens de raccourci ** `ideveloper://` ** (schéma URL). Les raccourcis de démarrage à froid et d'écran d'accueil sont livrés via un tampon unifié de sorte que les liens ne sont pas ouverts deux fois après l'embarquement.

## Format de lien


```
ideveloper://{host}?{params}
```


## Outils et navigation

| URL | Ouvre |
|-----|-------|
| `ideveloper://home` | Accueil |
| `ideveloper://tool?id={id}` | Détails de l'outil (par exemple `json`, `base64`, `timestamp`) |
| `ideveloper://category?id={id}` | Catégorie (par exemple «encodage») |
| `ideveloper://search` / `ideveloper://search?q={query}` | Recherche |
| `ideveloper://favorites` | Favoris |
| `ideveloper://history` | Historique de l'opération |
| `ideveloper://reference` / `ideveloper://reference?id={id}` | Centre de référence / entrée |
| `ideveloper://new-snippet` | Nouveau extrait |
| `ideveloper://focus` | Temps de focalisation / Entrée d'activité en direct |
| `ideveloper://share?tool={id}` | Ouvrir le partage dans un outil (travaille avec l'extension Partager + charge utile du groupe App) |

## Réglages et guides

| URL | Ouvre |
|-----|-------|
| `ideveloper://settings` | Réglages |
| `ideveloper://usage-guide` | Guide d'utilisation |
| `ideveloper://widget-guide` | Guide des widgets |
| `ideveloper://shortcuts-guide` | Guide Raccourcis |
| `ideveloper://feature-guide` | Rejouer l’accueil |
| `ideveloper://feedback` | E-mail de commentaires |
| `ideveloper://in-app-review` | Avis in-app / App Store |

## Exemples


```
ideveloper://tool?id=json
ideveloper://search?q=base64
ideveloper://reference?id=http-200
ideveloper://favorites
ideveloper://focus
ideveloper://share?tool=json
ideveloper://category?id=encoding
```


Utilisez-les dans l'application Raccourcis, Actions rapides Home Screen, Widgets, Control Center ou Safari. Voir aussi dans l'application **Paramètres → Guide des raccourcis**.


