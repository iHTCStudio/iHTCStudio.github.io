**Dernière mise à jour :** 19 septembre 2026

iHTC Studio (« nous », « notre » ou « nos ») a créé **iLiezi** (également connu sous le nom de « 爱列子 / 愛列子 », ID de bundle `com.iHTCboy.iLiezi`). Cette politique de confidentialité explique quelles données sont (et ne sont pas) traitées lorsque vous utilisez l'application. **Apple App Review** et les utilisateurs peuvent se référer à **cette page** comme politique de confidentialité publique. Pour App Store Connect, ouvrez cette politique de confidentialité dans votre navigateur et copiez l'adresse depuis la barre d'adresse (le domaine du site public peut changer avec le temps).

## Résumé (alignement sur l'étiquette nutritionnelle de confidentialité Apple)

| Sujet | Notre pratique |
|-------|----------------|
| Compte | **Non requis** — pas d'inscription, de connexion par e-mail ou de numéro de téléphone |
| Collecte de données par iHTC Studio | **Données non collectées** — nous n'exploitons **pas** de backend qui reçoit vos données personnelles |
| Réseau | La bibliothèque, la lecture, la récitation, l'étude, la chasse, les widgets et les notifications quotidiennes fonctionnent **hors ligne** après l'installation |
| Analyses / publicités / suivi | **Aucun** — pas de SDK tiers d'analyse, de publicité ou de suivi ; pas d'utilisation de la transparence du suivi des applications |
| Services Apple facultatifs | **iCloud** (your private KVS), **Photo Library (Add Only)** for study cards, **StoreKit** for pourboire facultatif, **local notifications**, optional **Live Activities**, optional on-device **handwriting** (Vision), optional **HealthKit** mood write (off by default) |

## Collecte de données

Nous ne collectons, vendons ou partageons **pas** d'informations personnelles à des fins publicitaires ou analytiques.

- **Aucun compte** — Vous pouvez utiliser toutes les fonctionnalités principales sans créer de compte chez nous.
- **Aucune analyse ni publicité** — Le binaire de l'application n'intègre pas de SDK tiers d'analyse, de publicité ou de rapport d'erreur qui nous contactent.
- **Aucun envoi de contenu** — historique, favoris, listes, notes, progression d’étude et préférences restent sur l’appareil (et, en option, dans **votre** iCloud). Ils ne sont jamais envoyés aux serveurs iHTC Studio car **nous n’exploitons pas de tels serveurs pour cette app**.

**Journal trois questions** privé. **HealthKit** **désactivé**, depuis réglages journal, **Santé** uniquement, **pas** un diagnostic.

## Comment fonctionne l'application

- **Bibliothèque groupée** — Texte JSON, langue vernaculaire/anglais, index et aides à l'étude livrés dans l'ensemble application/widget.
- **Discours sur l'appareil** — La récitation utilise le système **AVSpeechSynthesizer** (TTS) d'Apple. Nous n'envoyons pas de texte de passage à iHTC Studio.
- **Widgets et groupe d'applications** — Les widgets et l'application partagent les préférences via le groupe d'applications `group.com.iHTCboy.iLiezi` sur votre appareil.
- **Notifications quotidiennes** — Planifiées localement. Appuyer sur une notification ouvre un lien profond sur l'appareil.
- **Cartes d'étude** — Les images sont rendues sur l'appareil. L'enregistrement utilise **le module complémentaire Photothèque** uniquement lorsque vous appuyez sur Enregistrer.
- **Recherche d'écriture manuscrite (iOS)** : la reconnaissance de caractères facultative utilise Apple **Vision** sur l'appareil. Les traits ne sont pas téléchargés.
- **Conseil facultatif** — « Tip Developer » est un achat de consommable **StoreKit** traité par Apple.
- **Siri / Raccourcis / Centre de contrôle** — Les intégrations système facultatives ouvrent des liens profonds sur l'appareil.
- **Spotlight facultatif** : si vous activez l'indexation, le système indexe le contenu sur l'appareil.

## Données stockées sur votre appareil

| Données | Où | Objectif |
|------|-------|--------------|
| Bibliothèque ligne Zengzi | Bundle App / Widget | Lecture et étude hors ligne |
| Favoris et listes | Paramètres par défaut du groupe d'applications | Éléments favoris et listes d'utilisateurs |
| Historique de lecture / dernière lecture | Paramètres par défaut du groupe d'applications | Continuer la lecture |
| Remarques | Paramètres par défaut du groupe d'applications | Notes de lecture que vous écrivez |
| Avancement et maîtrise des études | Paramètres par défaut du groupe d'applications | Classe / Progrès de la chasse |
| Série / enregistrement | Paramètres par défaut du groupe d'applications | Habitude quotidienne |
| Apparence et préférences de lecture | Paramètres par défaut du groupe d'applications | Thème, langue, TTS, widgets |
| Daily Reflection cache & notification prefs | UserDefaults de l’App Group | ID du jour and schedule |
| Préférences de carte | Paramètres par défaut du groupe d'applications | Dernier style/ratio |
| État d’intégration et de TipKit | Valeurs par défaut de l'utilisateur standard | Guide de bienvenue |
| Widget / Instantanés d'activité en direct | Groupe d'applications / ActivityKit | Afficher le texte que vous avez déjà ouvert |

La désinstallation de l'application supprime les données du bac à sable et du groupe d'applications (sous réserve du comportement du système d'exploitation). Les copies iCloud facultatives restent dans **votre** iCloud jusqu'à ce que vous les effaciez.

## Synchronisation iCloud (Facultative)

Si vous activez **la synchronisation iCloud** dans les Réglages, l'application reflète les données utilisateur sélectionnées via le **`NSUbiquitousKeyValueStore`** d'Apple lié à **votre identifiant Apple** :

- Favoris
- Listes
- Historique de lecture
- Progression / maîtrise des études
- Séries de pratique
- Remarques
- Journal trois questions

Le trafic de synchronisation va vers **Apple iCloud**, pas vers iHTC Studio. Nous ne pouvons pas lire votre contenu iCloud.

## Autorisations

iLiezi demande des autorisations uniquement lorsqu'une fonctionnalité en a besoin :

| Autorisation | Quand | Pourquoi |
|------------|------|-----|
| Notifications | Vous activez Daily Reflection reminders | Planification locale |
| Bibliothèque de photos (Ajouter uniquement) | Vous enregistrez une carte | Écrivez l'image rendue |
| iCloud | Vous activez la synchronisation | Synchroniser les favoris/listes/historique/progression/notes |
| Activités en direct (iOS) | Vous activez l'activité de lecture en direct | Afficher le passage sur l'écran de verrouillage / Dynamic Island |
| Audio de fond (capacité) | Vous activez la récitation en arrière-plan | Continuer TTS en arrière-plan |
| Santé (humeur) | Sync journal dans Réglages | Marque trois axes dans **Santé** ; pas au premier lancement |

Nous ne demandons **pas** de contacts, de localisation précise, de caméra, de microphone (au-delà de la lecture TTS du système) ou de suivi.
- Écriture d’humeur HealthKit **désactivée par défaut**, jamais au premier lancement.

## Ce que nous ne faisons pas

- Nous ne vendons **pas** de données personnelles.
- Nous ne créons **pas** de profils publicitaires.
- Nous n'exigeons **pas** de compte ou de connexion sociale.
- Nous n'intégrons **pas** de publicités tierces, d'analyses ou de SDK sociaux pour la collecte de données.
- Nous n'accédons **pas** à votre photothèque au-delà du **ajout uniquement** lorsque vous choisissez d'enregistrer une carte.
- Nous ne recevons **pas** de numéros de carte de paiement StoreKit (Apple traite les paiements).

## Confidentialité des enfants

iLiezi est une application d'alphabétisation éducative destinée à un public général et n'est **pas** dans la catégorie Enfants. Nous ne collectons pas sciemment d’informations personnelles auprès des enfants. Les familles peuvent utiliser les fonctionnalités de lecture et d’étude hors ligne sur leurs propres appareils.

## Tiers

- **Apple** — App Store, StoreKit, iCloud KVS, TTS, Share Sheet, notifications/Live Activity/Siri/Shortcuts/Vision/HealthKit
- **Aucun autre SDK tiers** pour la publicité, l'analyse ou la connexion sociale n'est inclus pour la collecte de données.

## Utilisateurs internationaux

L'application est conçue pour fonctionner hors ligne sur votre appareil. Les services Apple optionnels suivent les conditions et la disponibilité régionale d'Apple.

## Conservation et suppression des données

- **Sur l'appareil** — Supprimez l'application pour retirer les données locales du bac à sable et du groupe d'applications (sous réserve du comportement du système d'exploitation).
- **iCloud** — Désactivez la synchronisation et supprimez les clés associées de votre compte iCloud si nécessaire ; nous ne pouvons pas effacer votre iCloud pour vous.
- **Nous ne conservons rien** sur les serveurs iHTC Studio pour cette application car nous ne collectons pas ces données.

## Modifications de la politique

Nous pouvons mettre à jour cette politique de confidentialité. La date « Dernière mise à jour » en haut sera modifiée. L'utilisation continue après une mise à jour signifie que vous acceptez la politique révisée.

## Nous contacter

Questions sur la vie privée : [AppleOSer@gmail.com](mailto:AppleOSer@gmail.com)
