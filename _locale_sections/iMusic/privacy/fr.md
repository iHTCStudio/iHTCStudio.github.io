**Dernière mise à jour :** 9 septembre 2026

iHTC Studio (« nous ») a développé **iMusic** (« 爱音乐 » / « 愛音樂 », Bundle ID `com.iHTCboy.iMusic`). Cette page explique quelles données sont (ou ne sont pas) traitées lorsque vous utilisez l'app et son extension widget. **Apple App Review** et les utilisateurs peuvent s'y référer comme politique de confidentialité publique. Pour App Store Connect : ouvrez cette [Politique de confidentialité](../privacy) dans le navigateur et copiez l'URL (le domaine public peut changer).

## Résumé (alignement Apple Privacy Nutrition Label)

| Sujet | Notre pratique |
|-------|----------------|
| Compte | **Non requis** — pas d'inscription, e-mail ou téléphone |
| Collecte par iHTC Studio | **Data Not Collected** — nous n'exploitons **pas** de backend recevant des données personnelles |
| Réseau | **Guides** lisibles **hors ligne** après installation ; **lecture** et **identification** utilisent les services Apple après autorisation |
| Analyse / pub / suivi | **Aucun** — pas de SDK analytics, publicité ou tracking tiers ; pas d'App Tracking Transparency |
| Services Apple optionnels | **Apple Music / MusicKit**, **ShazamKit**, **iCloud** (KVS privé), **Photothèque (ajout uniquement)** pour cartes de partage, pourboire **StoreKit** optionnel, **notifications locales**, **Live Activities** optionnelles |

## Collecte de données

Nous ne collectons, vendons ni partageons de données personnelles à des fins publicitaires ou analytiques.

- **Sans compte** — tous les guides fournis sont utilisables sans compte iHTC Studio.
- **Sans analyse ni publicité** — pas de SDK analytics, pub ou crash tiers nous contactant.
- **Pas d'envoi de vos guides** — favoris, listes, « écouter plus tard », notes, historique et réglages restent sur l'appareil (et optionnellement **votre** iCloud), jamais vers nos serveurs (**nous n'exploitons pas un tel backend pour cette app**).
- **Pas d'hébergement musical** — pas de fichiers audio complets dans l'app. La lecture correspondante est fournie par **Apple Music**. Sans abonnement, jusqu'à **30 s d'aperçu catalogue** peuvent être mis en cache localement.

## Fonctionnement de l'app

- **Bibliothèque incluse** — index, guides, notes d'artistes, catégories, collections, citations, calendrier quotidien dans le bundle app/widget ; guides sans réseau.
- **Apple Music (MusicKit)** — après autorisation, correspondance avec le catalogue (ISRC d'abord, puis artiste + titre) et lecture via le lecteur Apple. Statut d'abonnement auprès d'Apple ; délai dépassé = **inconnu** (pas de « non abonné » forcé). URLs d'illustrations pour les pochettes. Pas d'Apple ID ni de paiement chez nous.
- **Aperçu 30 s** — sans abonnement, l'aperçu Apple peut être stocké dans `Caches` (LRU, pas la piste complète). Pas de préchargement de l'aperçu suivant en cellulaire / économie d'énergie / données réduites. Cache artwork et aperçu effaçable dans Réglages sans toucher favoris/listes.
- **Identification (ShazamKit)** — uniquement à l'ouverture de Recognize ; micro traité par **Apple** ; pas d'archives d'enregistrement. Un hit ouvre le guide sur l'appareil.
- **Synthèse vocale locale** — lecture des guides via **AVSpeechSynthesizer** ; texte non envoyé à iHTC Studio.
- **Widget & App Group** — `group.com.iHTCboy.iMusic` partage les réglages ; artwork Live Activity = petit JPEG + jeton.
- **Notifications quotidiennes** — planification locale ; toucher → deep link vers l'ID du morceau.
- **Cartes de partage** — rendu sur l'appareil ; **Photothèque ajout uniquement** à l'enregistrement.
- **Pourboire optionnel** — consommable **StoreKit**.
- **Spotlight optionnel** — **désactivé par défaut** ; si activé, indexation par le système sur l'appareil.

## Données stockées sur l'appareil

| Donnée | Emplacement | Objectif |
|------|-------|---------|
| Bibliothèque de guides | Bundle app/widget | Lecture hors ligne |
| Favoris, listes, plus tard | App Group UserDefaults | Vos listes |
| Notes, historique, progression lecture | App Group UserDefaults | Reprise |
| Séries / check-in | App Group UserDefaults | Habitude quotidienne |
| Apparence, langue, onglets | App Group UserDefaults | Réglages |
| Cache Daily Piece & notifications | App Group UserDefaults | ID du jour & planning |
| Réglages cartes de partage | App Group UserDefaults | Dernier style |
| URLs artwork & images décodées | App Group + cache | Pochettes ; prefetch après MusicKit |
| Fichiers aperçu 30 s | App Caches | Hors ligne après premier hit |
| Miniature Live Activity | App Group JPEG + jeton | Écran verrouillé / Dynamic Island pendant **lecture à voix haute** |
| Autorisations MusicKit / Shazam | Système | Mémorisation du choix |
| Onboarding & invite avis | UserDefaults appareil | Accueil / avis |

La désinstallation supprime sandbox et App Group (selon iOS/macOS). Les copies iCloud optionnelles restent dans **votre** iCloud. Bibliothèque et abonnement Apple Music restent chez Apple.

## Sync iCloud (optionnelle)

Avec **iCloud Sync** activé, **`NSUbiquitousKeyValueStore`** sous **votre Apple ID** reflète :

- Favoris, listes, plus tard, notes, historique d'écoute/lecture, progression de lecture à voix haute, séries

Le texte des guides est déjà dans le bundle. Pas de sync KVS pour fichiers artwork ni audio d'aperçu. Trafic vers **iCloud Apple** uniquement, pas via iHTC Studio. Désactivable ; nous ne lisons pas votre iCloud.

## Autorisations

| Autorisation | Quand | Pourquoi |
|------------|------|-----|
| **Apple Music / Médias** | Explication MusicKit ou lecture | Correspondance & lecture ; pochettes |
| **Microphone** | Ouvrir Song ID | Reconnaître la musique ambiante |
| **Notifications** | Rappel Daily Piece | Planification locale |
| **Photothèque (ajout)** | Enregistrer carte musique | Image rendue ; pas de lecture complète de la photothèque |
| **iCloud** | Activer la sync | Listes/notes/historique/séries |
| **Live Activities (iOS)** | Reading Live Activity (activé par défaut) | Guide à l'**écran verrouillé** pendant la lecture à voix haute |
| **Audio arrière-plan** | Option activée | MusicKit / aperçu / TTS en arrière-plan |

Pas de contacts, localisation précise, caméra ni tracking. Pas de **lecture** de photothèque.

## Ce que nous ne faisons pas

- Pas de vente de données ni de profils publicitaires
- Pas de compte imposé ni login social
- Pas de SDK tiers orientés collecte
- Pas de pistes complètes sur nos serveurs ou stockées pour nous
- Pas de conservation des tampons micro Shazam après reconnaissance
- Pas de Dynamic Island personnalisée pour **lecture musicale** — uniquement lecture de guide (si activée)
- Pas de numéros de carte StoreKit chez nous

## Enfants

Pas de collecte volontaire chez les moins de 13 ans (ou âge local). Pas de backend de collecte → pas de profils enfants chez nous. Apple Music et Shazam suivent les règles Apple.

## Tiers

- **Apple** — App Store, MusicKit, ShazamKit, StoreKit, iCloud KVS, TTS, partage, notifications, Live Activities, Siri/Raccourcis
- **Aucun** autre SDK tiers collectant des données

## Utilisateurs internationaux

Guides hors ligne sur l'appareil. Apple Music, Shazam, iCloud selon Apple. Correspondance catalogue selon la boutique de l'Apple ID connecté.

## Conservation & suppression

- **Appareil** — cache artwork/aperçu dans **Réglages → Stockage** ; désinstallation supprime sandbox/App Group.
- **iCloud (optionnel)** — reste dans **votre** iCloud jusqu'à désactivation ou outils Apple.
- **iHTC Studio** — aucun compte serveur à supprimer.

## Modifications

Nous pouvons mettre à jour cette politique ; la date « Dernière mise à jour » changera en tête de page.

## Contact

- **E-mail :** [AppleOSer@gmail.com](mailto:AppleOSer@gmail.com)

Réponse en général sous 48 h.
