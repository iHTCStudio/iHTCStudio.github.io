**Dernière mise à jour :** 3 septembre 2026

iHTC Studio (« nous ») a développé **iZhuangZi** (« 爱庄子 / 愛莊子 », Bundle ID `com.iHTCboy.iZhuangZi`). Cette politique de confidentialité explique quelles données sont (ou ne sont pas) traitées lorsque vous utilisez l’app. **Apple App Review** et les utilisateurs peuvent s’appuyer sur **cette page** comme politique publique. Pour App Store Connect, ouvrez cette page dans le navigateur et copiez l’URL depuis la barre d’adresse (le domaine public peut changer).

## Résumé (alignement sur l'étiquette nutritionnelle de confidentialité Apple)

| Sujet | Notre pratique |
|-------|----------------|
| Compte | **Non requis** — pas d'inscription, de connexion par e-mail ou de numéro de téléphone |
| Collecte de données par iHTC Studio | **Données non collectées** — nous n'exploitons **pas** de backend qui reçoit vos données personnelles |
| Réseau | La bibliothèque, la lecture, la récitation, l'étude, la chasse, les widgets et les notifications quotidiennes fonctionnent **hors ligne** après l'installation |
| Analyses / publicités / suivi | **Aucun** — pas de SDK tiers d'analyse, de publicité ou de suivi ; pas d'utilisation de la transparence du suivi des applications |
| Services Apple facultatifs | **iCloud** (your private KVS), **Photo Library (Add Only)** for 逍遥 cards, **StoreKit** for pourboire facultatif, **local notifications**, optional **Live Activities**, optional **on-device handwriting** (Vision), optional **Ask Zhuangzi** (on-device Apple Intelligence when available) |

## Collecte de données

Nous ne collectons, vendons ou partageons **pas** d'informations personnelles à des fins publicitaires ou analytiques.

- **Aucun compte** — Vous pouvez utiliser toutes les fonctionnalités principales sans créer de compte chez nous.
- **Aucune analyse ni publicité** — Le binaire de l'application n'intègre pas de SDK tiers d'analyse, de publicité ou de rapport d'erreur qui nous contactent.
- **Aucun envoi de contenu** — historique, favoris, listes, notes, progression d’étude et préférences restent sur l’appareil (et, en option, dans **votre** iCloud). Ils ne sont jamais envoyés aux serveurs iHTC Studio car **nous n’exploitons pas de tels serveurs pour cette app**.

## Comment fonctionne l'application

- **Bibliothèque incluse** — JSON texte, vernaculaire/anglais, index et aides d’étude sont dans le bundle app/widget. Parcourir et étudier ne nécessite pas le réseau.
- **Discours sur l'appareil** — La récitation utilise le système **AVSpeechSynthesizer** (TTS) d'Apple. Nous n'envoyons pas de texte de passage à iHTC Studio.
- **Widgets et App Group** — Les widgets et l’app partagent des préférences et un état léger via l’App Group `group.com.iHTCboy.iZhuangZi` sur votre appareil.
- **Notifications quotidiennes** — Planifiées localement avec les notifications utilisateur. Appuyer sur une notification ouvre un lien profond vers un identifiant de passage sur l'appareil ; pas de distribution du serveur.
- **Cartes 逍遥** — Les images sont générées sur l’appareil. L’enregistrement utilise **Photothèque (ajout uniquement)** seulement lorsque vous touchez Enregistrer. La feuille de partage peut envoyer l’image à une app **que vous choisissez** ; la politique de confidentialité de cette destination s’applique alors.
- **Recherche d'écriture manuscrite (iOS)** : la reconnaissance de caractères facultative utilise Apple **Vision** sur l'appareil. Les traits ne sont pas téléchargés.
- **Conseil facultatif** — « Tip Developer » est un achat de consommable **StoreKit** traité par Apple. Nous ne recevons pas les détails de votre carte de paiement.
- **Siri / Raccourcis / Centre de contrôle** — Les intégrations système facultatives ouvrent des liens profonds sur l'appareil ; ils ne nous envoient pas votre bibliothèque.
- **Spotlight facultatif** — Si vous activez l'indexation, le contenu est indexé par le système sur l'appareil pour la recherche locale ; nous n'exploitons pas de backend de recherche.
- **Ask Zhuangzi** — Sur les appareils pris en charge (iOS 26+ / macOS 26+ avec Apple Intelligence), le guide optionnel utilise les **Foundation Models sur l’appareil** d’Apple. Le contexte du passage et votre question restent sur l’appareil ; nous ne les **envoyons pas** à iHTC Studio. Si le modèle est indisponible, l’app utilise les commentaires intégrés.

## Données stockées sur votre appareil

| Données | Où | Objectif |
|------|-------|--------------|
| Base Zhuangzi | Bundle App / Widget | Lecture et étude hors ligne |
| Favoris et listes (庄单) | UserDefaults de l’App Group | Passages favoris et listes utilisateur |
| Historique de lecture / dernière lecture | Paramètres par défaut du groupe d'applications | Continuer la lecture, historique de l'interface utilisateur |
| Remarques | Paramètres par défaut du groupe d'applications | Notes de lecture que vous écrivez |
| Progression d’étude et maîtrise | UserDefaults de l’App Group | Dao Study state, quiz / Hunt progress |
| Séquence d'entraînement / enregistrement | Paramètres par défaut du groupe d'applications | Habitude quotidienne |
| Préférences des cartes de partage | UserDefaults de l'App Group | Derniers choix de style / de format |
| Daily Zhuangzi cache & notification prefs | UserDefaults de l’App Group | ID du jour, schedule time, contextual toggle |
| Préférences de cartes | UserDefaults de l’App Group | Dernier style/ratio |
| État d’intégration et de TipKit | Paramètres utilisateur standard (appareil) | Guide d'accueil / conseils découverte |
| Recherches récentes | Standard UserDefaults (device) | Historique saisi |
| Actions rapides sur l'écran d'accueil | Système + préférences locales | Raccourcis que vous configurez |
| Widget / Instantanés d'activité en direct | Groupe d'applications / ActivityKit | Afficher le texte que vous avez déjà ouvert |

La désinstallation de l'application supprime les données du bac à sable et du groupe d'applications associées à l'application (selon le comportement d'iOS/macOS). Les copies facultatives dans iCloud restent dans **votre** iCloud jusqu'à ce que vous les supprimiez ou que vous désactiviez la synchronisation et supprimiez ailleurs.

## Synchronisation iCloud (Facultative)

Si vous activez **la synchronisation iCloud** dans les Réglages, l'application reflète les données utilisateur sélectionnées via le **`NSUbiquitousKeyValueStore`** d'Apple lié à **votre identifiant Apple** :

- Favoris
- Listes (庄单)
- Historique de lecture
- Progression / maîtrise des études
- Séries de pratique
- Remarques

Le trafic de synchronisation passe par **Apple iCloud**, et non par iHTC Studio. Vous pouvez désactiver la synchronisation dans les Réglages. Nous ne pouvons pas lire le contenu de votre iCloud.

## Autorisations

iLiezi demande des autorisations uniquement lorsqu'une fonctionnalité en a besoin :

| Autorisation | Quand | Pourquoi |
|------------|------|-----|
| Notifications | Vous activez Daily Zhuangzi reminders | Planification locale of reminder notifications |
| Photothèque (ajout uniquement) | Enregistrer une carte | Image rendu |
| iCloud | Activez la sync | Favoris/listes/historique/progression/séries/notes |
| Activités en direct (iOS) | Vous activez l'activité de lecture en direct | Affichez le passage que vous lisez sur l'écran de verrouillage / Dynamic Island |
| Audio de fond (capacité) | Vous activez la récitation en arrière-plan | Continuer TTS lorsque l'application n'est pas au premier plan |

**Pas** de contacts, localisation précise, caméra, micro (hors TTS), suivi. Écriture — Vision sur l’appareil.

## Ce que nous ne faisons pas

- Nous ne vendons **pas** de données personnelles.
- Nous ne créons **pas** de profils publicitaires.
- Nous n'exigeons **pas** de compte ou de connexion sociale.
- Nous n'intégrons **pas** de publicités tierces, d'analyses ou de SDK sociaux pour la collecte de données.
- Nous n'accédons **pas** à votre photothèque au-delà du **ajout uniquement** lorsque vous choisissez d'enregistrer une carte.
- Nous ne recevons **pas** de numéros de carte de paiement StoreKit (Apple traite les paiements).
- **Pas** d’envoi d’écriture manuscrite ou de passages à iHTC Studio.
- **Pas** d’envoi des questions Ask Zhuangzi à iHTC Studio (Apple Intelligence sur l’appareil).

## Confidentialité des enfants

iZhuangZi est une application éducative de lecture pour le grand public et **n’est pas** dans la Kids Category. Nous ne collectons pas sciemment d’informations personnelles auprès d’enfants. L’app ne nécessite pas de compte. Les familles peuvent utiliser lecture et étude hors ligne sur leurs propres appareils.

## Tiers

- **Apple** — App Store, StoreKit, iCloud KVS, TTS système, Share Sheet, notifications/Live Activity/Siri/Shortcuts/Vision, Apple Intelligence sur l’appareil (Ask Zhuangzi)
- **Aucun autre SDK tiers** pour la publicité, l'analyse ou la connexion sociale n'est inclus pour la collecte de données.

## Utilisateurs internationaux

L'application est conçue pour fonctionner hors ligne sur votre appareil. Les services Apple optionnels suivent les conditions et la disponibilité régionale d'Apple.

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
