iDao prend en charge les liens de raccourci ** `idao://` ** (schéma URL). Les raccourcis de démarrage à froid et d'écran d'accueil sont livrés via un tampon unifié de sorte que les liens ne sont pas ouverts deux fois après l'embarquement.

## Format de lien


```
idao://{host}?{params}
```


## Chapitres et découvertes

| URL | Ouvre |
|-----|-------|
| `idao://home` | Accueil |
| `idao://daily` | Aujourd'hui le chapitre quotidien |
| `idao://random` | Chapitre aléatoire |
| `idao://chapter?id={id}` | Détail du chapitre |
| `idao://recite` / `idao://recite?id={id}` | Flux de récitation |
| `idao://favorites` | Favoris |
| `idao://famous` | Vers célèbres |
| `idao://search` / `idao://search?q={query}` | Recherche |
| `idao://study` | Salle d'étude |
| `idao://hunt` | Cherchez le Tao ( |
| `idao://mastered` | Maîtrise |
| `idao://categories` / `?section=` | Parcourir (section facultative) |
| `idao://book?id=` | Collection de livres ( ' ddj ' / ' qingjing ' / ' yinfu ') |
| `idao://author` | Intro Laozi |
| `idao://last-read` | Dernière lecture |
| `idao://reading-history` | Historique de lecture |
| `idao://notes` | Notes |

> Alias de compatibilité : `idao://` / `idao://home` → chapitre; `idao://daily` → étude; `idao://random` → chasse; `idao://chapter?id={id}` → auteur; `idao://recite` → catégorie; `idao://recite?id={id}` → catégorie.

## Réglages et guides

| URL | Ouvre |
|-----|-------|
| `idao://settings` | Réglages |
| `idao://usage-guide` | Guide d'utilisation |
| `idao://widget-guide` | Guide des widgets |
| `idao://shortcuts-guide` | Guide Raccourcis |
| `idao://feature-guide` | Rejouer l’accueil |
| `idao://feedback` | E-mail de commentaires |
| `idao://in-app-review` | Avis in-app / App Store |

## Exemples


```
idao://daily
idao://chapter?id=1
idao://recite?id=1
idao://study
idao://hunt
idao://famous
idao://book?id=ddj
idao://author
idao://search?q=上善若水
```


Utilisez-les dans l'application Raccourcis, Actions rapides Home Screen, Widgets, Control Center ou Safari. Voir aussi dans l'application **Paramètres → Guide des raccourcis**.


