**Dernière mise à jour :** 6 septembre 2026 

iHTC Studio ("nous", "notre" ou "notre") a créé **iBrowser** (également connu sous le nom de "全屏浏览器" / "全螢幕瀏覽器", ID de bundle `full.screen.browser`). Cette politique de confidentialité explique quelles données sont (et ne sont pas) traitées lorsque vous utilisez l'application. **Apple App Review** et les utilisateurs peuvent se fier à cette page comme URL de confidentialité publique. Pour App Store Connect, ouvrez cette page [Politique de confidentialité](../privacy) et copiez l'adresse de la barre d'adresse du navigateur. 

## Résumé (alignement sur l'étiquette nutritionnelle de confidentialité Apple) 

| Sujet | Notre pratique | 
|-------|----------------| 
| Compte | **Non requis** — pas d'inscription ni de connexion avec iHTC Studio | 
| Collecte de données par iHTC Studio | **Données non collectées** — nous n'exploitons **pas** de backend qui reçoit vos favoris ou vos paramètres | 
| Publicité | **Aucun** — pas de publicité, pas de SDK publicitaire, pas d'invite de transparence du suivi des applications pour les publicités | 
| Navigation dans le contenu | Les pages que vous ouvrez sont chargées **directement par WebKit** à partir de ces sites ; nous n'exploitons pas de proxy de navigation | 
| Synchronisation Apple en option | **Stockage de valeurs-clés iCloud** — désactivé par défaut ; seulement si vous l'activez dans Paramètres | 

## Collecte de données

- **Aucun compte** — Vous pouvez utiliser l'application sans créer de compte chez nous. 
- **Pas de SDK de publicité ou d'analyse** — L'application ne diffuse pas de publicités ni d'analyses téléphoniques sur iHTC Studio. 
- **Pas de backend iHTC Studio pour vos favoris** — Les préférences restent sur votre appareil (et éventuellement dans **votre** Apple iCloud). Nous n'hébergeons pas de serveur qui reçoit votre liste de favoris. 

### Navigation sur le Web 

Lorsque vous naviguez sur un site Web ou utilisez un moteur de recherche : 

- Votre appareil contacte **ce site** (ou ce fournisseur de recherche) via le réseau, comme avec n'importe quel navigateur. 
- Ces tiers peuvent voir les métadonnées de demande standard (adresse IP, agent utilisateur, cookies qu'ils définissent, contenu de la page que vous demandez). Leurs politiques de confidentialité s’appliquent. 
- Le choix d'un **moteur de recherche** intégré ou personnalisé définit uniquement un préfixe d'URL de recherche sur l'appareil. 

### Widgets, raccourcis et liens profonds 

Les widgets de l'écran d'accueil/de l'écran de verrouillage, Siri, les raccourcis, les actions rapides de l'écran d'accueil et les liens `ibrowser://` ouvrent des destinations **sur votre appareil**. Ils n'envoient pas votre historique de navigation à iHTC Studio. 

## Données stockées sur votre appareil

| Données | Où | Objectif | 
|------|-------|--------------| 
| URL de la page d'accueil | UserDefaults (+ instantané du groupe d'applications) | Page de démarrage ; affichage des widgets | 
| Préfixe du moteur de recherche | Paramètres par défaut de l'utilisateur | Recherche dans la barre d'adresse | 
| Signets | UserDefaults (JSON) (+ instantané du groupe d'applications) | Favoris locaux ; widgets de favoris | 
| Sécurité enfant / masquage forcé chrome | Paramètres par défaut (+ groupe d'applications) | Modes immersif & enfant / kiosque | 
| Boule flottante marche/arrêt et commande de menu | Paramètres par défaut de l'utilisateur | Possibilité de raccourci | 
| Ballon flottant **position** | UserDefaults (appareil uniquement) | Où vous avez laissé le ballon – **non** synchronisé avec iCloud | 
| Dernière page chargée avec succès | Paramètres par défaut (+ groupe d'applications) | « Continuer en dernier » – **appareil uniquement**, pas iCloud | 
| Mot de passe des paramètres | **Porte-clés** (`WhenUnlockedThisDeviceOnly`) | Verrouillage des paramètres facultatif – **pas** dans UserDefaults, App Group ou iCloud | 
| Marges du navigateur | Paramètres par défaut de l'utilisateur | Encarts de contenu | 
| Apparence / langage | UserDefaults (appareil uniquement) | Langue du thème et de l'interface utilisateur – **pas** iCloud | 
| Commande d'action rapide sur l'écran d'accueil | UserDefaults (appareil uniquement) | Menu à pression longue — **pas** iCloud | 
| Guide de première diffusion et indicateurs de termes | UserDefaults (appareil uniquement) | Intégration | 
| Instantanés de widgets | Groupe d'applications `group.full.screen.browser` | Affichage en lecture seule pour l'extension du widget |

La désinstallation de l'application supprime ses données sandbox et App Group (sous réserve du comportement d'iOS). Les copies iCloud facultatives restent dans **votre** iCloud jusqu'à ce que vous les effaciez ou désactiviez la synchronisation ailleurs. 

## Synchronisation iCloud en option 

Si vous activez **iCloud Sync** dans Paramètres (**désactivé** par défaut), les préférences sélectionnées sont reflétées via le **`NSUbiquitousKeyValueStore`_** d'Apple lié à **votre identifiant Apple** : 

**Peut synchroniser :** signets, page d'accueil, moteur de recherche, marges, verrouillages d'affichage de la barre d'adresse/barre d'outils, activation/désactivation de la boule flottante, ordre du menu de la boule flottante. 

**Ne synchronise pas :** Mot de passe des paramètres, dernière page (« continuer en dernier »), position de la boule flottante, apparence, langue, ordre d'action rapide sur l'écran d'accueil, indicateurs de guide/termes. 

Le trafic de synchronisation va vers **Apple iCloud**, pas vers iHTC Studio. Vous pouvez désactiver la synchronisation ou appuyer sur **Synchroniser maintenant** dans Paramètres. Nous ne pouvons pas lire votre contenu iCloud. 

## Autorisations 

Les pages Web peuvent demander des fonctionnalités de périphérique via WebKit (par exemple une caméra, un microphone ou un emplacement) en fonction du site. Les invites du système apparaissent uniquement lorsqu'une page le demande. L'application déclare également les chaînes de capacités dont le contenu Web peut avoir besoin ; nous n'utilisons pas ces autorisations pour une fonctionnalité sociale ou publicitaire native distincte.

| Zone | Remarques |
|------|--------|
| Réseau | Nécessaire pour charger les sites web et effectuer des recherches |
| Mouvement (secouer) | Utilisé sur **iPhone** pour récupérer la boule flottante / Chrome — le traitement reste local ; **iPad** utilise plutôt un tapotement près du haut |
| iCloud | Seulement si vous activez la synchronisation |
| Mail / Feuille de partage | Retour facultatif ou actions de partage que vous initiez |
| StoreKit (pourboire optionnel) | Pourboire consommable traité par Apple ; ne déverrouille pas de fonctionnalités |

## Confidentialité des enfants

Le verrouillage pour enfant est une **restriction UI locale** (cacher la barre d’adresse / mot de passe facultatif dans les Réglages). Tant qu’il est activé, les widgets, Raccourcis et favoris non domestiques s’ouvrent **à la page d’accueil**. Il ne crée **pas** de compte enfant chez nous. Nous ne sollicitons pas sciemment d’informations personnelles auprès des enfants à des fins de marketing. Les parents doivent superviser les sites qui sont ouverts.

## Ce que nous ne faisons pas

- Nous n'avons **pas** besoin d'un compte iHTC Studio. 
- Nous ne diffusons **pas** de publicités dans l'application ni de pop-ups promotionnels interstitiels (en dehors des conditions de première diffusion requises). 
- Nous n'exploitons **pas** nos propres serveurs de synchronisation cloud pour cette application (la synchronisation facultative utilise **votre** Apple iCloud uniquement). 
- Nous ne vendons **pas** vos données. 
- Nous ne stockons **pas** le mot de passe des paramètres dans UserDefaults (il utilise le trousseau sur l'appareil). 

## Tiers 

| Fête | Rôle | 
|-------|------| 
| **Pomme** | Distribution sur l'App Store ; iCloud KVS en option ; widgets / Siri / Raccourcis ; Courrier, feuille de partage, contrôleur Safari View ; Astuce StoreKit en option | 
| **Sites Web et moteurs de recherche que vous ouvrez** | Recevez le trafic normal du navigateur pour les pages que vous visitez | 

## Conservation et suppression 

Les préférences locales et les favoris restent jusqu'à ce que vous les modifiiez ou les supprimiez, ou que vous désinstalliez l'application. Les données iCloud facultatives restent soumises aux politiques d'Apple jusqu'à ce que vous désactiviez la synchronisation et/ou les effaciez via les outils d'Apple. Étant donné que nous ne collectons pas de données personnelles sur nos serveurs, nous ne pouvons supprimer aucun ensemble de données de compte au-delà de la réponse à votre courrier électronique. 

## Modifications apportées à cette politique

Nous pouvons mettre à jour cette page de temps en temps. La date « Dernière mise à jour » ci-dessus changera lorsque nous le ferons. L'utilisation continue après les modifications signifie que vous acceptez la politique mise à jour.

## Contactez-nous

- **Email :** [AppleOSer@gmail.com](mailto:AppleOSer@gmail.com)

Ouvrez cette page [Politique de confidentialité](../privacy) dans un navigateur et copiez l'URL de la barre d'adresse si vous avez besoin du lien public pour App Store Connect.
