**Dernière mise à jour :** 5 août 2026

iHTC Studio (« nous », « notre » ou « nos ») a créé **iYijing** (également connu sous le nom de « 爱周易 » / « 愛周易 », ID de l'application `com.iHTCboy.iYiJing`). Cette politique de confidentialité explique quelles données sont (et ne sont pas) traitées lorsque vous utilisez l'application. **Apple App Review** et les utilisateurs peuvent se référer à **cette page** comme politique de confidentialité publique pour l'application. Pour App Store Connect, ouvrez cette politique de confidentialité dans votre navigateur et copiez l'adresse depuis la barre d'adresse (le domaine public du site peut changer avec le temps).

## Résumé (alignement avec l'étiquette nutritionnelle de confidentialité Apple)

| Sujet | Notre pratique | 
|-------|----------------| 
| Compte | **Non requis** — pas d'inscription, de connexion par e-mail ou de numéro de téléphone | 
| Collecte de données par iHTC Studio | **Données non collectées** — nous n'exploitons **pas** de backend qui reçoit vos données personnelles | 
| Réseau | Bibliothèque, lecture, récitation, diffusion culturelle, salle d'étude, widgets et notifications quotidiennes fonctionnent **hors ligne** après l'installation | 
| Analyses / publicités / suivi | **Aucun** — pas de SDK tiers d'analyse, de publicité ou de suivi ; pas d'utilisation de la transparence du suivi des applications | 
| Services Apple en option | **iCloud** (votre KVS privé, fusionner), **Bibliothèque de photos (à ajouter uniquement)** pour les cartes d'étude, **StoreKit** pour des pourboires facultatifs, **notifications locales**, **Activités en direct** en option | 

## Collecte de données 

Nous ne collectons, vendons ou partageons **pas** d'informations personnelles à des fins publicitaires ou analytiques.

- **Pas de compte** — Vous pouvez utiliser toutes les fonctionnalités principales sans créer de compte chez nous.
- **Pas d'analytique ni de publicité** — Le binaire de l'application n'intègre pas de SDKs tiers pour l'analytique, la publicité ou le rapport de crash qui communiqueraient avec nous.
- **Pas de téléchargement de contenu** — Votre historique de lecture, vos favoris, listes, notes, enregistrements de diffusion, mauvais livres, maîtrise, séries et préférences restent sur votre appareil (et éventuellement dans **votre** iCloud). Ils ne sont jamais téléchargés sur les serveurs de iHTC Studio car **nous ne gérons pas de tels serveurs pour cette application**.

## Comment fonctionne l'application

- **Bibliothèque groupée** — Hexagram JSON, Ten Wings, trigrammes, lignes célèbres et index sont livrés dans le bundle application/widget. La navigation et l'étude ne nécessitent pas de requête réseau. 
- **Discours sur l'appareil** — La récitation utilise le système **AVSpeechSynthesizer** (TTS) d'Apple. Nous n'envoyons pas de texte hexagramme à iHTC Studio. 
- **Casting culturel** — Les procédures de pièces de monnaie et d'achillée millefeuille fonctionnent entièrement sur un appareil pour le symbolisme éducatif ; les enregistrements que vous choisissez de sauvegarder restent locaux (et éventuellement dans votre iCloud). 
- **Widgets et groupe d'applications** — Les widgets et l'application partagent les préférences et l'état léger via le groupe d'applications `group.com.iHTCboy.iYiJing` sur votre appareil. 
- **Notifications quotidiennes** — Planifiées localement avec les notifications utilisateur. Appuyer sur ouvre un lien profond vers un identifiant hexagramme sur l'appareil ; pas de distribution du serveur. 
- **Cartes d'étude** — Les images sont rendues sur l'appareil. L'enregistrement utilise **le module complémentaire Photothèque** uniquement lorsque vous appuyez sur Enregistrer. System Share Sheet peut envoyer l'image à une application **que** vous choisissez ; la politique de confidentialité de cette destination s’applique alors. 
- **Conseil facultatif** — « Tip Developer » est un achat de consommable **StoreKit** traité par Apple. Nous ne recevons pas les détails de votre carte de paiement. 
- **Siri / Raccourcis / Centre de contrôle** — Les intégrations système facultatives ouvrent des liens profonds sur l'appareil ; ils ne nous envoient pas votre bibliothèque. 
- **Spotlight facultatif** — Si vous activez l'indexation, le contenu est indexé par le système sur l'appareil pour la recherche locale ; nous n'exploitons pas de backend de recherche. 
- **Activité en direct facultative** — Désactivée par défaut ; lorsqu'il est activé, affiche l'hexagramme que vous lisez sur l'écran de verrouillage / Dynamic Island.

## Données stockées sur votre appareil 

| Données | Où | Objectif | 
|------|-------|--------------| 
| Base de données Hexagramme / Ailes / Trigramme | Offre groupée d'applications/widgets | Lecture et étude hors ligne | 
| Favoris et listes d'hexagrammes | Paramètres par défaut du groupe d'applications | Œuvres favorites et listes d'utilisateurs | 
| Historique de lecture / dernière lecture | Paramètres par défaut du groupe d'applications | Continuer la lecture, historique de l'interface utilisateur | 
| Progrès des études, maîtrise et mauvais livre | Paramètres par défaut du groupe d'applications | État de la salle d'étude | 
| Records de casting | Paramètres par défaut du groupe d'applications | L'histoire du casting culturel que vous enregistrez | 
| Remarques | Paramètres par défaut du groupe d'applications | Notes que vous écrivez | 
| Série / enregistrement | Paramètres par défaut du groupe d'applications | Habitude quotidienne | 
| Apparence et préférences de lecture | Paramètres par défaut du groupe d'applications | Thème, accent, langue, mise en page, TTS, onglets, widgets | 
| Cache Hexagram quotidien et préférences de notification | Paramètres par défaut du groupe d'applications | ID du jour, heure programmée | 
| Préférences de carte partagée | Paramètres par défaut du groupe d'applications | Derniers choix de style/ratio | 
| État d'intégration | Paramètres utilisateur standard (appareil) | Guide de bienvenue | 
| Widget / Instantanés d'activité en direct | Groupe d'applications / ActivityKit | Afficher le texte que vous avez déjà ouvert |

La désinstallation de l'application supprime le sandbox et les données du groupe d'applications associées à l'application (sous réserve du comportement d'iOS/macOS). Les copies optionnelles sur iCloud restent dans **votre** iCloud jusqu'à ce que vous les supprimiez ou que vous désactiviez la synchronisation et supprimiez les données ailleurs.

## Synchronisation iCloud (Optionnelle)

Si vous activez **la synchronisation iCloud** dans les Réglages, l'application reflète certaines données utilisateur sélectionnées via le **`NSUbiquitousKeyValueStore`** d'Apple lié à **votre identifiant Apple**, en utilisant des règles de fusion pour les favoris, listes, historique, maîtrise, notes, enregistrements de tirage, livre des erreurs et séries consécutives.

Le trafic de synchronisation passe par **Apple iCloud**, pas par iHTC Studio. Vous pouvez désactiver la synchronisation dans les Réglages. Nous ne pouvons pas lire le contenu de votre iCloud.

## Autorisations

iYijing demande des autorisations uniquement lorsqu'une fonctionnalité en a besoin :

| Autorisation | Quand | Pourquoi |
|------------|------|-----|
| Notifications | Vous activez les rappels quotidiens de l’hexagramme | Planification locale des notifications de rappel |
| Bibliothèque de photos (ajout uniquement) | Vous enregistrez une carte d’étude | Écrire l’image rendue ; nous n’avons pas besoin d’un accès complet à la bibliothèque |
| iCloud | Vous activez la synchronisation | Synchroniser les favoris / listes / historique / maîtrise / notes / tirage / mauvaise-livre / séries |
| Activités en direct (iOS) | Vous activez l’activité en direct de lecture | Afficher l’hexagramme que vous lisez sur l’écran de verrouillage / l’île dynamique |
| Audio en arrière-plan (capacité) | Vous activez la récitation en arrière-plan | Continuer la synthèse vocale lorsque l’application n’est pas au premier plan |

Nous ne demandons **pas** l’accès aux Contacts, à la position précise, à la Caméra, au Microphone (au-delà de la lecture du TTS système), ou au Suivi.

## Ce que nous ne faisons pas

- Nous ne vendons **pas** de données personnelles. 
- Nous ne créons **pas** de profils publicitaires. 
- Nous n'exigeons **pas** de compte ou de connexion sociale. 
- Nous n'intégrons **pas** de publicités tierces, d'analyses ou de SDK sociaux pour la collecte de données. 
- Nous n'accédons **pas** à votre photothèque au-delà du **ajout uniquement** lorsque vous choisissez d'enregistrer une carte. 
- Nous ne recevons **pas** de numéros de carte de paiement StoreKit (Apple traite les paiements). 
- Nous n'envoyons **pas** de questions ou de résultats de casting à aucun serveur. 

## Confidentialité des enfants 

iYijing ne collecte sciemment aucune donnée personnelle de quiconque, y compris les enfants de moins de 13 ans (ou l'âge équivalent dans votre région). Parce que nous n’exploitons pas de backend de collecte de données, aucun profil enfant n’est stocké chez nous. Les familles peuvent utiliser les fonctionnalités de lecture et d’étude hors ligne sur leurs propres appareils. 

## Tiers 

- **Apple** — Distribution sur l'App Store, achats StoreKit en option, iCloud KVS en option, TTS système, destinations de feuille de partage que vous choisissez et notification au niveau du système d'exploitation/activité en direct/Siri/livraison de raccourcis. 
- **Aucun autre SDK tiers** pour les publicités, les analyses ou la connexion sociale n'est inclus pour la collecte de données. 

## Utilisateurs internationaux

L'application est conçue pour fonctionner hors ligne sur votre appareil. Les services Apple en option suivent les conditions d’Apple et la disponibilité régionale. 

## Conservation et suppression des données 

- **Sur l'appareil** : les préférences locales et la progression restent jusqu'à ce que vous les effaciez dans l'application (le cas échéant), réinitialisiez l'appareil ou désinstalliez l'application. 
- **iCloud (facultatif)** — Les données que vous avez synchronisées restent dans **votre** compte iCloud conformément aux politiques d'Apple jusqu'à ce que vous désactiviez la synchronisation et/ou les effaciez via les outils d'Apple. 
- **iHTC Studio** — Étant donné que nous ne collectons pas de données personnelles sur nos serveurs, nous ne pouvons supprimer aucun ensemble de données de compte sur demande au-delà de répondre à vos questions par courrier électronique. 

## Modifications apportées à cette politique 

Nous pouvons mettre à jour cette politique de confidentialité de temps à autre. La date de « Dernière mise à jour » en haut changera et la politique révisée sera publiée sur cette page Politique de confidentialité. 

## Contactez-nous 

Si vous avez des questions sur cette politique de confidentialité ou sur les pratiques de confidentialité : 

- **E-mail :** [AppleOSer@gmail.com](mailto:AppleOSer@gmail.com) 

Nous répondons généralement dans les 48 heures.
