**Dernière mise à jour :** 18 août 2026

iHTC Studio (« nous ») a développé **iSutra** (« 爱佛经 » / « 爱佛经 », Bundle ID `com.iHTCboy.iSutra`). Cette politique de confidentialité explique quelles données sont (ou ne sont pas) traitées lorsque vous utilisez l’app. **Apple App Review** et les utilisateurs peuvent s’appuyer sur **cette page** comme politique publique. Pour App Store Connect, ouvrez cette page dans le navigateur et copiez l’URL depuis la barre d’adresse (le domaine public peut changer).

## Résumé (alignement sur l'étiquette nutritionnelle de confidentialité Apple)

| Sujet | Notre pratique |
|-------|----------------|
| Compte | **Non requis** — pas d'inscription, de connexion par e-mail ou de numéro de téléphone |
| Collecte de données par iHTC Studio | **Données non collectées** — nous n'exploitons **pas** de backend qui reçoit vos données personnelles |
| Réseau | Bibliothèque, reading, recite, Study Hall, Hunt, chant, practice, widgets, and daily notifications work **offline** after install fonctionnent **hors ligne** après l’installation |
| Analyses / publicités / suivi | **Aucun** — pas de SDK tiers d'analyse, de publicité ou de suivi ; pas d'utilisation de la transparence du suivi des applications |
| Services Apple facultatifs | **iCloud** (your private KVS), **Photo Library (Add Only)** for Dharma cards / exports, **StoreKit** for pourboire facultatif, **local notifications**, optional **Live Activities**, optional **Spotlight** (off by default) |

## Collecte de données

Nous ne collectons, vendons ou partageons **pas** d'informations personnelles à des fins publicitaires ou analytiques.

- **Aucun compte** — Vous pouvez utiliser toutes les fonctionnalités principales sans créer de compte chez nous.
- **Aucune analyse ni publicité** — Le binaire de l'application n'intègre pas de SDK tiers d'analyse, de publicité ou de rapport d'erreur qui nous contactent.
- **Aucun envoi de contenu** — Vos reading history, favorites, lists, notes, mastery, streaks, chant counts, practice checklists, and preferences stay on your device (and optionally in **your** iCloud). They are never uploaded to iHTC Studio servers because **we do not run such servers for this app**.

## Comment fonctionne l'application

- **Bibliothèque incluse** — JSON texte, vernaculaire/anglais, index et aides d’étude sont dans le bundle app/widget. Parcourir et étudier ne nécessite pas le réseau.
- **Voix sur l’appareil** — **AVSpeechSynthesizer**. Pas de texte de sutra à iHTC Studio.
- **Widgets et App Group** — Les widgets et l’app partagent des préférences et un état léger via l’App Group `group.com.iHTCboy.iSutra` sur votre appareil.
- **Notifications quotidiennes** — Planifiées localement avec les notifications utilisateur. Appuyer sur une notification ouvre un lien profond vers un identifiant de passage sur l'appareil ; pas de distribution du serveur.
- **Cartes Dharma / export** — images et PDF sur l’appareil. **Photothèque (ajout uniquement)** à l’enregistrement.
- **Copie de sutra (iOS)** — traits PencilKit dans Application Support (`CopySutra/…`). **Pas** dans App Group, **pas** de sync iCloud.
- **Conseil facultatif** — « Tip Developer » est un achat de consommable **StoreKit** traité par Apple. Nous ne recevons pas les détails de votre carte de paiement.
- **Siri / Raccourcis / Centre de contrôle** — Les intégrations système facultatives ouvrent des liens profonds sur l'appareil ; ils ne nous envoient pas votre bibliothèque.
- **Spotlight facultatif** — Désactivé par défaut. Si vous activez l'indexation, le contenu est indexé par le système sur l'appareil pour la recherche locale ; nous n'exploitons pas de backend de recherche.

## Données stockées sur votre appareil

| Données | Où | Objectif |
|------|-------|--------------|
| Base sutras (index, shards) | Bundle App / Widget | Lecture et étude hors ligne |
| Favoris et listes (经单) | UserDefaults de l’App Group | Passages favoris et listes utilisateur |
| Historique de lecture / dernière lecture | Paramètres par défaut du groupe d'applications | Continuer la lecture, historique de l'interface utilisateur |
| Progression d’étude et maîtrise | UserDefaults de l’App Group | Study Hall state, quiz / Hunt progress |
| Notes | UserDefaults de l’App Group | Notes de passages |
| Séquence d'entraînement / enregistrement | Paramètres par défaut du groupe d'applications | Habitude quotidienne |
| Compteurs de chant et son | UserDefaults de l’App Group | Wooden-fish, objectifs, tons |
| Pratique matin/soir | UserDefaults de l’App Group | Checklist liturgie |
| Apparence et préférences de lecture | Paramètres par défaut du groupe d'applications | Thème, accent, langue, mise en page, TTS, onglets, widgets |
| Daily Sutra cache & notification prefs | UserDefaults de l’App Group | ID du jour, schedule time |
| Préférences de carte partagée | Paramètres par défaut du groupe d'applications | Derniers choix de style/ratio |
| Dessins Copy-sutra (iOS) | Application Support (`CopySutra/`) | Brouillons par ligne |
| État d’intégration et de TipKit | Paramètres utilisateur standard (appareil) | Guide d'accueil / conseils découverte |
| Actions rapides sur l'écran d'accueil | Système + préférences locales | Raccourcis que vous configurez |
| Instantanés Widget / Live Activity | App Group / ActivityKit | Texte/chant déjà ouverts |

La désinstallation de l'application supprime les données du bac à sable et du groupe d'applications associées à l'application (selon le comportement d'iOS/macOS). Les copies facultatives dans iCloud restent dans **votre** iCloud jusqu'à ce que vous les supprimiez ou que vous désactiviez la synchronisation et supprimiez ailleurs.

## Synchronisation iCloud (Facultative)

Avec **iCloud Sync**, miroir via **`NSUbiquitousKeyValueStore`**. Trafic vers **Apple iCloud**. Copy-sutra **non** inclus.

## Autorisations

iLiezi demande des autorisations uniquement lorsqu'une fonctionnalité en a besoin :

| Autorisation | Quand | Pourquoi |
|------------|------|-----|
| Notifications | Vous activez Daily Sutra reminders | Planification locale of reminder notifications |
| Photothèque (ajout uniquement) | Carte Dharma/enregistrement | Image/PDF rendu ; pas de lecture complète |
| iCloud | Activez la sync | Favoris/listes/historique/maîtrise/notes/chant |
| Live Activities (iOS) | Reading/Chant Live Activity | Lecture/chant sur écran verrouillé |
| Audio de fond (capacité) | Vous activez la récitation en arrière-plan | Continuer TTS lorsque l'application n'est pas au premier plan |

Nous ne demandons **pas** de contacts, de localisation précise, de caméra, de microphone (au-delà de la lecture TTS du système) ou de suivi.

## Ce que nous ne faisons pas

- Nous ne vendons **pas** de données personnelles.
- Nous ne créons **pas** de profils publicitaires.
- Nous n'exigeons **pas** de compte ou de connexion sociale.
- Nous n'intégrons **pas** de publicités tierces, d'analyses ou de SDK sociaux pour la collecte de données.
- **Pas** d’accès à Photothèque au-delà de **l’ajout uniquement** lors de l’enregistrement.
- Nous ne recevons **pas** de numéros de carte de paiement StoreKit (Apple traite les paiements).
- **Pas** de divination ni commerce de bénédictions payantes à partir du contenu religieux.

## Confidentialité des enfants

iSutra ne collecte pas sciemment de données, y compris enfants de moins de 13 ans.

## Tiers

- **Apple** — Distribution via l'App Store, achats facultatifs via StoreKit, KVS iCloud facultatif, synthèse vocale système, destinations du partage choisies par vous, et notifications / Live Activity / Siri / Raccourcis au niveau du système d'exploitation.
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
