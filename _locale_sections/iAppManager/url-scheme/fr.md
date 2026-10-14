iAppManager prend en charge ** `iappmanager://` ** liens pour raccourcis, widgets, App Intents et Home Screen actions.

## Format de lien


```
iappmanager://{host}[/…]
```


## Applications & modules

| URL | Ouvre |
|-----|-------|
| `iappmanager://apps` | Mes applications |
| `iappmanager://apps/{appleId}` | App spécifique (Aperçu) |
| `iappmanager://apps/{appleId}/{tab}` | Module de détail de l'application | `iappmanager://` C1    exemples :

| Tab | Module |
|-----|--------|
| `overview` | Aperçu général |
| `versions` | Versions |
| `builds` | Constructions |
| `backgroundAssets` | Actifs de base |
| `encryption` | Chiffrement |
| `submissions` | Demandes de réexamen |
| `reviewDetail` | Détail du réexamen |
| `metadata` | Métadonnées |
| `media` | Captures d'écran et aperçus |
| `productPages` | Pages de produits personnalisées |
| `appEvents` | Événements dans l'application |
| `appClips` | Clips d'application |
| `experiments` | Expériences de stockage |
| `nominations` | Présentation de candidatures |
| `availability` | Disponibilité |
| `pricing` | Prix |
| `ageRating` | Taux d'âge |
| `accessibility` | Accessibilité |
| `appTags` | Étiquettes de l'application |
| `iap` | Achats dans l'application |
| `gameCenter` | Centre de jeu |
| `testflight` | Essai |
| `reviews` | Avis clients |
| `privacy` | Vie privée (note de nutrition) |
| `promoCodes` | Codes promotionnels |
| `webhooks` | Boucliers Web |

Exemple : `iappmanager://` ## Barre latérale & outils

| URL | Ouvre |
|-----|-------|
| `iappmanager://certificates` | Certificats et identifiants |
| `iappmanager://users` | Utilisateurs & Accès |
| `iappmanager://reports` | Rapports |
| `iappmanager://settings` | Réglages |
| `iappmanager://add-account` | Ajouter un compte API Key |
| `iappmanager://about` | À propos |
| `iappmanager://feedback` | E-mail de commentaires |
| `iappmanager://in-app-review` | Taux |

## Guides d'application

| URL | Guide |
|-----|-------|
| `iappmanager://feature-guide` | Visite principale |
| `iappmanager://usage-guide` | Guide d'utilisation |
| `iappmanager://widget-guide` | Guide des widgets |
| `iappmanager://shortcuts-guide` | Guide Raccourcis |
| `iappmanager://release-guide` | Préparation à la libération |
| `iappmanager://iap-guide` | IAP & abonnements |
| `iappmanager://testflight-guide` | Essai |
| `iappmanager://reports-guide` | Rapports |

Les lancements froids et chauds tampons liens profonds brièvement afin que l'embarquement peut terminer en premier. App Intents peut également ouvrir une application gérée avec un module optionnel.


