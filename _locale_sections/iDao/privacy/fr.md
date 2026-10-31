**Dernière mise à jour :** 3 août 2026

iHTC Studio (« nous » ou « notre ») a créé **iDao** (également connu sous le nom « 爱道德经 » / « 愛道德經 », ID de bundle `com.iHTCboy.iDao`). Cette politique de confidentialité explique quelles données sont (et ne sont pas) traitées lorsque vous utilisez l'application. **Apple App Review** et les utilisateurs peuvent se référer à **cette page** comme politique de confidentialité publique de l'application. Pour App Store Connect, ouvrez cette politique de confidentialité dans votre navigateur et copiez l'adresse depuis la barre d'adresse (le domaine du site public peut changer avec le temps).

## Résumé (alignement avec l'étiquette nutritionnelle de confidentialité Apple)

| Sujet | Notre pratique |
|-------|----------------|
| Compte | **Non requis** — aucune inscription, connexion par e-mail ou numéro de téléphone |
| Collecte de données par iHTC Studio | **Données non collectées** — nous n'exploitons **aucun** backend qui reçoit vos données personnelles |
| Réseau | Bibliothèque, lecture, récitation, salle d'étude, Chercher le Tao, widgets et notifications quotidiennes fonctionnent **hors ligne** après installation |
| Analytique / publicités / suivi | **Aucun** — aucun SDK tiers d'analytics, de publicité ou de suivi ; aucune utilisation de la Transparence sur le Suivi des Apps |
| Services Apple optionnels | **iCloud** (votre KVS privé, fusion bidirectionnelle), **Bibliothèque de photos (ajout uniquement)** pour les cartes Dao, **StoreKit** pour pourboires optionnels, **notifications locales**, **Activités en direct** optionnelles |

## Collecte de données

Nous ne collectons, ne vendons ni ne partageons d'informations personnelles à des fins publicitaires ou analytiques.

- **Pas de compte** — Vous pouvez utiliser toutes les fonctionnalités principales sans créer de compte chez nous.
- **Pas d’analytique ni de publicités** — Le binaire de l’application n’intègre pas de SDK tiers d’analytique, de publicité ou de rapport de plantage qui communiqueraient avec nous.
- **Pas de téléchargement de contenu** — Votre historique de lecture, favoris, listes, notes, maîtrise, séries et préférences restent sur votre appareil (et éventuellement dans **votre** iCloud). Ils ne sont jamais téléchargés sur les serveurs de iHTC Studio car **nous n’exploitons pas de tels serveurs pour cette application**.

## Comment fonctionne l’application

- **Bibliothèque groupée** — Les chapitres JSON, vernaculaires, pinyin, commentaires, éditions anglaises, lignes célèbres et index sont livrés dans l'ensemble application/widget. La navigation et l'étude ne nécessitent pas de requête réseau. 
- **Discours sur l'appareil** — La récitation utilise le système **AVSpeechSynthesizer** (TTS) d'Apple. Nous n'envoyons pas de texte de chapitre à iHTC Studio. 
- **Widgets et groupe d'applications** — Les widgets et l'application partagent les préférences et l'état léger via le groupe d'applications `group.com.iHTCboy.iDao` sur votre appareil. 
- **Notifications quotidiennes** — Planifiées localement avec les notifications utilisateur. Appuyer sur une notification ouvre un lien profond vers un ID de chapitre sur l'appareil ; pas de distribution du serveur. 
- **Cartes Dao** — Les images sont rendues sur l'appareil. L'enregistrement utilise **le module complémentaire Photothèque** uniquement lorsque vous appuyez sur Enregistrer. System Share Sheet peut envoyer l'image à une application **que** vous choisissez ; la politique de confidentialité de cette destination s’applique alors. 
- **Conseil facultatif** — « Tip Developer » est un achat de consommable **StoreKit** traité par Apple. Nous ne recevons pas les détails de votre carte de paiement. 
- **Siri / Raccourcis / Centre de contrôle** — Les intégrations système facultatives ouvrent des liens profonds sur l'appareil ; ils ne nous envoient pas votre bibliothèque. 
- **Spotlight facultatif** — Désactivé par défaut. Si vous activez l'indexation, le contenu est indexé par le système sur l'appareil pour la recherche locale ; nous n'exploitons pas de backend de recherche.

## Données stockées sur votre appareil 

| Données | Où | Objectif | 
|------|-------|--------------| 
| Base de données de chapitres (y compris les éditions pinyin/notes) | Offre groupée d'applications/widgets | Lecture et étude hors ligne | 
| Favoris et listes (道单) | Paramètres par défaut du groupe d'applications | Chapitres favoris et listes d'utilisateurs | 
| Historique de lecture / dernière lecture | Paramètres par défaut du groupe d'applications | Continuer la lecture, historique de l'interface utilisateur | 
| Avancement et maîtrise des études | Paramètres par défaut du groupe d'applications | État de la salle d'étude, quiz / Cherchez les progrès du Tao | 
| Remarques | Paramètres par défaut du groupe d'applications | Notes de chapitre que vous écrivez | 
| Séquence d'entraînement / enregistrement | Paramètres par défaut du groupe d'applications | Habitude quotidienne | 
| Apparence et préférences de lecture | Paramètres par défaut du groupe d'applications | Thème, accent, langue, mise en page, TTS, onglets, widgets | 
| Préférences de cache et de notification des chapitres quotidiens | Paramètres par défaut du groupe d'applications | ID du jour, heure de programmation, bascule contextuelle | 
| Préférences de carte partagée | Paramètres par défaut du groupe d'applications | Derniers choix de style/ratio | 
| État d’intégration et de TipKit | Paramètres utilisateur standard (appareil) | Guide d'accueil / conseils découverte | 
| Actions rapides sur l'écran d'accueil | Système + préférences locales | Raccourcis que vous configurez | 
| Widget / Instantanés d'activité en direct | Groupe d'applications / ActivityKit | Afficher le texte que vous avez déjà ouvert |

La désinstallation de l’application supprime les données du bac à sable et du groupe d’applications associées à l’application (selon le comportement d’iOS/macOS). Les copies iCloud optionnelles restent dans **votre** iCloud jusqu’à ce que vous les supprimiez ou désactiviez la synchronisation et supprimiez ailleurs.

## Synchronisation iCloud (optionnelle)

Si vous activez la **synchronisation iCloud** dans les Réglages, l’application reflète certaines données utilisateur via le **`NSUbiquitousKeyValueStore`** d’Apple lié à **votre identifiant Apple**, en utilisant une **fusion bidirectionnelle** (favoris, listes, historique, maîtrise, notes, séries) afin que les mises à jour cloud et appareil soient combinées plutôt que remplacées aveuglément.

Le trafic de synchronisation passe par **Apple iCloud**, et non par iHTC Studio. Vous pouvez désactiver la synchronisation dans les Réglages. Nous ne pouvons pas lire le contenu de votre iCloud.

## Autorisations

iDao demande les autorisations uniquement lorsqu’une fonctionnalité en a besoin :

| Autorisation | Quand | Pourquoi | 
|------------|------|-----| 
| Notifications | Vous activez les rappels de chapitre quotidiens | Planification locale des notifications de rappel | 
| Bibliothèque de photos (Ajouter uniquement) | Vous sauvegardez une carte Dao | Écrivez l'image rendue ; nous n'avons pas besoin d'un accès complet en lecture à la bibliothèque | 
| iCloud | Vous activez la synchronisation | Synchroniser les favoris/listes/historique/maîtrise/notes/séries | 
| Activités en direct (iOS) | Vous activez l'activité de lecture en direct | Affichez le chapitre que vous lisez sur l'écran de verrouillage / Dynamic Island | 
| Audio de fond (capacité) | Vous activez la récitation en arrière-plan | Continuer TTS lorsque l'application n'est pas au premier plan | 

Nous ne demandons **pas** de contacts, de localisation précise, de caméra, de microphone (au-delà de la lecture TTS du système) ou de suivi. 

## Ce que nous ne faisons pas 

- Nous ne vendons **pas** de données personnelles. 
- Nous ne créons **pas** de profils publicitaires. 
- Nous n'exigeons **pas** de compte ou de connexion sociale. 
- Nous n'intégrons **pas** de publicités tierces, d'analyses ou de SDK sociaux pour la collecte de données. 
- Nous n'accédons **pas** à votre photothèque au-delà du **ajout uniquement** lorsque vous choisissez d'enregistrer une carte. 
- Nous ne recevons **pas** de numéros de carte de paiement StoreKit (Apple traite les paiements). 

## Confidentialité des enfants

iDao ne collecte pas sciemment de données personnelles auprès de quiconque, y compris les enfants de moins de 13 ans (ou l'âge équivalent dans votre région). Comme nous n'exploitons pas de système de collecte de données, aucun profil enfant n'est stocké chez nous. Les familles peuvent utiliser les fonctionnalités de lecture et d'étude hors ligne sur leurs propres appareils.

## Tiers

- **Apple** — Distribution via l'App Store, achats facultatifs via StoreKit, KVS iCloud facultatif, synthèse vocale système, destinations du partage que vous choisissez et livraison des notifications / Live Activity / Siri / Raccourcis au niveau du système d'exploitation.
- **Aucun autre SDK tiers** pour la publicité, l'analyse ou la connexion sociale n'est inclus pour la collecte de données.

## Utilisateurs internationaux

L'application est conçue pour fonctionner hors ligne sur votre appareil. Les services Apple facultatifs suivent les conditions d'Apple et la disponibilité régionale.

## Conservation et suppression des données

- **Sur l'appareil** — Les préférences locales et la progression restent jusqu'à ce que vous les effaciez dans l'application (lorsque disponible), que vous réinitialisiez l'appareil ou que vous désinstalliez l'application.
- **iCloud (facultatif)** — Les données que vous avez synchronisées restent dans **votre** compte iCloud selon les politiques d’Apple jusqu’à ce que vous désactiviez la synchronisation et/ou les effaciez via les outils d’Apple.
- **iHTC Studio** — Comme nous ne collectons pas de données personnelles sur nos serveurs, il n’existe aucun jeu de données de compte que nous puissions supprimer sur demande, hormis répondre à vos questions par email.

## Modifications de cette politique

Nous pouvons mettre à jour cette politique de confidentialité de temps à autre. La date « Dernière mise à jour » en haut changera, et la politique révisée sera publiée sur cette page de politique de confidentialité.

## Contactez-nous

Si vous avez des questions concernant cette politique de confidentialité ou nos pratiques en matière de confidentialité :

- **Email :** [AppleOSer@gmail.com](mailto:AppleOSer@gmail.com)

Nous répondons généralement sous 48 heures.
