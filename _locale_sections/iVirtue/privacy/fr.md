**Dernière mise à jour :** 23 juillet 2026

iHTC Studio (« nous », « notre » ou « nos ») a développé **iVirtue** (également connu sous le nom « 爱弟子规 » / « 愛弟子規 », Bundle ID `com.iHTCboy.iVirtue`). Cette politique de confidentialité explique quelles données sont (ou ne sont pas) traitées lorsque vous utilisez l'app. **Apple App Review** et les utilisateurs peuvent s'appuyer sur cette page comme URL publique de confidentialité.

## Résumé (alignement sur l'étiquette de confidentialité d'Apple)

| Sujet | Notre pratique |
|-------|----------------|
| Compte | **Non requis** — aucune inscription, connexion par e-mail ni numéro de téléphone |
| Collecte de données par iHTC Studio | **Aucune donnée collectée** — nous n'exploitons **aucun** serveur qui recevrait vos données personnelles |
| Réseau | La bibliothèque de virtues, la lecture, la récitation, l'étude, les widgets et les notifications quotidiennes fonctionnent **hors ligne** après l'installation |
| Analyse / publicité / suivi | **Aucun** — aucun SDK tiers d'analyse, de publicité ou de suivi ; pas d'App Tracking Transparency |
| Services Apple facultatifs | **iCloud** (votre KVS privé), **Photothèque (ajout uniquement)** pour les cartes de partage, **StoreKit** pour un pourboire facultatif, **notifications locales**, **activités en direct** facultatives |

## Collecte de données

Nous ne collectons, ne vendons ni ne partageons **aucune** information personnelle à des fins publicitaires ou d'analyse.

- **Aucun compte** — Vous pouvez utiliser toutes les fonctionnalités principales sans créer de compte chez nous.
- **Aucune analyse ni publicité** — L'app n'intègre aucun SDK tiers d'analyse, de publicité ou de rapport de plantage qui nous renverrait des informations.
- **Aucun envoi du contenu des virtues** — Votre historique de lecture, vos favoris, votre progression d'étude et vos préférences restent sur votre appareil (et, en option, dans **votre** iCloud). Ils ne sont jamais envoyés aux serveurs d'iHTC Studio, car **nous n'exploitons pas de tels serveurs pour cette app**.

## Fonctionnement de l'app

- **Bibliothèque intégrée** — Le JSON des virtues et les index sont fournis dans le bundle de l'app / du widget. Parcourir et étudier ne nécessite aucune requête réseau.
- **Voix sur l'appareil** — La récitation utilise **AVSpeechSynthesizer** (TTS), la synthèse vocale du système Apple sur l'appareil. Nous n'envoyons aucun texte de virtue à iHTC Studio.
- **Widgets et App Group** — Les widgets et l'app partagent des préférences et un état léger via l'App Group `group.com.iHTCboy.iVirtue` sur votre appareil.
- **Notifications quotidiennes** — Planifiées localement avec User Notifications. Toucher une notification ouvre un lien profond vers l'identifiant d'un virtue sur l'appareil ; aucune diffusion depuis un serveur.
- **Cartes de partage** — Les images sont générées sur l'appareil. L'enregistrement utilise **Photothèque (ajout uniquement)** seulement lorsque vous touchez Enregistrer. La feuille de partage du système peut envoyer l'image à une app **que vous choisissez** ; la politique de confidentialité de cette destination s'applique alors.
- **Pourboire facultatif** — « Soutenir le développeur » est un achat consommable **StoreKit** traité par Apple. Nous ne recevons pas les données de votre carte de paiement.

## Données stockées sur votre appareil

| Données | Où | Finalité |
|------|-------|---------|
| Base de données des virtues | Bundle de l'app / du widget | Lecture et étude hors ligne |
| Favoris et listes de virtues | UserDefaults de l'App Group | Œuvres marquées d'une étoile et listes de l'utilisateur |
| Historique de lecture / dernière lecture | UserDefaults de l'App Group | Reprendre la lecture, interface d'historique |
| Progression d'étude et maîtrise | UserDefaults de l'App Group | 4 niveaux de maîtrise, état du quiz |
| Série / pointage | UserDefaults de l'App Group | Séries d'apprentissage |
| Préférences d'apparence et de lecture | UserDefaults de l'App Group | Thème, accent, langue, mise en page, TTS, onglets, widgets |
| Cache du virtue du jour et préférences de notification | UserDefaults de l'App Group | Identifiant du jour, heure de planification, bascule contextuelle |
| Préférences des cartes de partage | UserDefaults de l'App Group | Derniers choix de style / de format |
| État d'accueil et TipKit | UserDefaults standard (appareil) | Guide de bienvenue / astuces de découverte |
| Actions rapides de l'écran d'accueil | Système + préférences locales | Jusqu'à 4 raccourcis que vous configurez |
| Instantanés de widgets / activités en direct | App Group / ActivityKit | Texte affiché que vous avez déjà ouvert |

La désinstallation de l'app supprime les données du bac à sable et de l'App Group associées à l'app (selon le comportement d'iOS/macOS). Les copies iCloud facultatives restent dans **votre** iCloud jusqu'à ce que vous les effaciez, ou que vous désactiviez la synchronisation et supprimiez ailleurs.

## Synchronisation iCloud (facultative)

Si vous activez la **synchronisation iCloud** dans les Réglages, l'app reflète certaines données utilisateur via **`NSUbiquitousKeyValueStore`** d'Apple, lié à **votre identifiant Apple** :

- Favoris
- Listes de virtues
- Historique de lecture
- Progression d'étude / maîtrise
- Jours de série

Le trafic de synchronisation est envoyé à **Apple iCloud**, et non à iHTC Studio. Vous pouvez désactiver la synchronisation dans les Réglages. Nous ne pouvons pas lire le contenu de votre iCloud.

## Autorisations

iVirtue ne demande des autorisations que lorsqu'une fonctionnalité en a besoin :

| Autorisation | Quand | Pourquoi |
|------------|------|-----|
| Notifications | Vous activez les rappels du virtue du jour | Planification locale des notifications de rappel |
| Photothèque (ajout uniquement) | Vous enregistrez une carte de partage | Écrire l'image générée ; nous n'avons pas besoin d'un accès en lecture à toute la photothèque |
| iCloud | Vous activez la synchronisation | Synchroniser favoris / listes / historique / progression / séries |
| Activités en direct (iOS) | Vous activez l'activité en direct de lecture | Afficher le virtue que vous lisez sur l'écran verrouillé / la Dynamic Island |
| Audio en arrière-plan (capacité) | Vous activez la récitation en arrière-plan | Poursuivre la synthèse vocale lorsque l'app n'est pas au premier plan |

Nous ne demandons **aucun** accès aux contacts, à la localisation précise, à l'appareil photo, au microphone (au-delà de la lecture de la synthèse vocale du système) ni au suivi.

## Confidentialité des enfants

iVirtue ne collecte sciemment de données personnelles auprès de personne, y compris des enfants de moins de 13 ans (ou l'âge équivalent dans votre région). Comme nous n'exploitons aucun serveur de collecte de données, aucun profil d'enfant n'est conservé chez nous.

## Tiers

- **Apple** — distribution sur l'App Store, achats StoreKit facultatifs, iCloud KVS facultatif, synthèse vocale du système, destinations de la feuille de partage que vous choisissez, et acheminement des notifications / activités en direct au niveau du système.
- **Aucun autre SDK tiers** de publicité, d'analyse ou de connexion sociale à des fins de collecte de données n'est inclus.

## Utilisateurs internationaux

L'app est conçue pour fonctionner hors ligne sur votre appareil. Les services Apple facultatifs sont soumis aux conditions d'Apple et à la disponibilité régionale.

## Modifications de cette politique

Nous pouvons mettre à jour cette politique de confidentialité de temps à autre. La date de « Dernière mise à jour » en haut sera modifiée, et la politique révisée sera publiée sur cette page de politique de confidentialité.

## Nous contacter

- **E-mail :** [AppleOSer@gmail.com](mailto:AppleOSer@gmail.com)
