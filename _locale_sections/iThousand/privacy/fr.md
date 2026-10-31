**Dernière mise à jour :** 18 août 2026

iHTC Studio (« nous ») a développé **iThousand** (« 爱千字文 » / « 爱千字文 », Bundle ID `com.iHTCboy.iThousand`). Cette politique de confidentialité explique quelles données sont (ou ne sont pas) traitées lorsque vous utilisez l’app. **Apple App Review** et les utilisateurs peuvent s’appuyer sur **cette page** comme politique publique. Pour App Store Connect, ouvrez cette page dans le navigateur et copiez l’URL depuis la barre d’adresse (le domaine public peut changer).

## Résumé (alignement sur l'étiquette nutritionnelle de confidentialité Apple)

| Sujet | Notre pratique |
|-------|----------------|
| Compte | **Non requis** — pas d'inscription, de connexion par e-mail ou de numéro de téléphone |
| Collecte de données par iHTC Studio | **Données non collectées** — nous n'exploitons **pas** de backend qui reçoit vos données personnelles |
| Réseau | Bibliothèque, character cards, reading, recite, Primer Hall, Hunt, widgets, and daily notifications work **offline** after install fonctionnent **hors ligne** après l’installation |
| Analyses / publicités / suivi | **Aucun** — pas de SDK tiers d'analyse, de publicité ou de suivi ; pas d'utilisation de la transparence du suivi des applications |
| Services Apple facultatifs | **iCloud** (your private KVS), **Photo Library (Add Only)** for share cards, **StoreKit** for pourboire facultatif, **local notifications**, optional **Live Activities**, optional **Spotlight** (off by default), optional **system speech / translation** |

## Collecte de données

Nous ne collectons, vendons ou partageons **pas** d'informations personnelles à des fins publicitaires ou analytiques.

- **Aucun compte** — Vous pouvez utiliser toutes les fonctionnalités principales sans créer de compte chez nous.
- **Aucune analyse ni publicité** — Le binaire de l'application n'intègre pas de SDK tiers d'analyse, de publicité ou de rapport d'erreur qui nous contactent.
- **Aucun envoi de contenu** — Vos reading history, favorites, lists (千单), saved characters, notes, study progress, streaks, and preferences stay on your device (and optionally in **your** iCloud). They are never uploaded to iHTC Studio servers because **we do not run such servers for this app**.

## Comment fonctionne l'application

- **Bibliothèque incluse** — JSON texte, vernaculaire/anglais, index et aides d’étude sont dans le bundle app/widget. Parcourir et étudier ne nécessite pas le réseau.
- **Discours sur l'appareil** — La récitation utilise le système **AVSpeechSynthesizer** (TTS) d'Apple. Nous n'envoyons pas de texte de passage à iHTC Studio.
- **Traduction système** — fonctions Apple ; OS Apple.
- **Widgets et App Group** — Les widgets et l’app partagent des préférences et un état léger via l’App Group `group.com.iHTCboy.iThousand` sur votre appareil.
- **Notifications quotidiennes** — Planifiées localement avec les notifications utilisateur. Appuyer sur une notification ouvre un lien profond vers un identifiant de passage sur l'appareil ; pas de distribution du serveur.
- **Partager des cartes** : les images sont rendues sur l'appareil. L'enregistrement utilise **le module complémentaire Photothèque** uniquement lorsque vous appuyez sur Enregistrer. System Share Sheet peut envoyer l'image à une application **que** vous choisissez ; la politique de confidentialité de cette destination s’applique alors.
- **Pourboire facultatif** — « Tip Developer » (`com.iHTCboy.iThousand.6`), **StoreKit** via Apple.
- **Siri / Raccourcis / Centre de contrôle** — Les intégrations système facultatives ouvrent des liens profonds sur l'appareil ; ils ne nous envoient pas votre bibliothèque.
- **Spotlight facultatif** — désactivé par défaut. Passages et cartes indexés sur l’appareil ; pas de backend de recherche.
- **Email de commentaires** — peut inclure votre texte et des diagnostics appareil/app (version, OS, langue) pour le dépannage.

## Données stockées sur votre appareil

| Données | Où | Objectif |
|------|-------|--------------|
| Base passages et caractères | Bundle App / Widget | Lecture, cartes d’alphabétisation |
| Favoris et listes (千单) | UserDefaults de l’App Group | Passages favoris et listes utilisateur |
| Caractères et lignes favorites | UserDefaults de l’App Group | Caractères difficiles, lignes favorites |
| Historique de lecture / dernière lecture | Paramètres par défaut du groupe d'applications | Continuer la lecture, historique de l'interface utilisateur |
| Progression d’étude et maîtrise | UserDefaults de l’App Group | Primer Hall state, quiz / Hunt progress |
| Notes | UserDefaults de l’App Group | Notes de passages |
| Série d’étude / check-in | UserDefaults de l’App Group | Habitude quotidienne |
| Préférences des cartes de partage | UserDefaults de l'App Group | Derniers choix de style / de format |
| Préférences de cache et de notification de la ligne quotidienne | Paramètres par défaut du groupe d'applications | ID du jour, heure de programmation, bascule contextuelle |
| Préférences de carte partagée | Paramètres par défaut du groupe d'applications | Derniers choix de style/ratio |
| État d’intégration et de TipKit | Paramètres utilisateur standard (appareil) | Guide d'accueil / conseils découverte |
| Actions rapides sur l'écran d'accueil | Système + préférences locales | Raccourcis que vous configurez |
| Widget / Instantanés d'activité en direct | Groupe d'applications / ActivityKit | Afficher le texte que vous avez déjà ouvert |

La désinstallation de l'application supprime les données du bac à sable et du groupe d'applications associées à l'application (selon le comportement d'iOS/macOS). Les copies facultatives dans iCloud restent dans **votre** iCloud jusqu'à ce que vous les supprimiez ou que vous désactiviez la synchronisation et supprimiez ailleurs.

## Synchronisation iCloud (Facultative)

Si vous activez **la synchronisation iCloud** dans les Réglages, l'application reflète les données utilisateur sélectionnées via le **`NSUbiquitousKeyValueStore`** d'Apple lié à **votre identifiant Apple** :

- Favoris
- Listes (千单)
- Caractères enregistrés / passages favoris
- Historique de lecture
- Progression / maîtrise des études
- Séries d’étude
- Remarques

Le trafic de synchronisation passe par **Apple iCloud**, et non par iHTC Studio. Vous pouvez désactiver la synchronisation dans les Réglages. Nous ne pouvons pas lire le contenu de votre iCloud.

## Autorisations

iLiezi demande des autorisations uniquement lorsqu'une fonctionnalité en a besoin :

| Autorisation | Quand | Pourquoi |
|------------|------|-----|
| Notifications | Vous activez Daily Line reminders | Planification locale |
| Photothèque (ajout uniquement) | Carte partagée/caractère | Write the rendered image |
| iCloud | Activez la sync | Favoris/listes/historique/progression/séries/notes/caractères enregistrés |
Si vous activez la **synchronisation iCloud** dans les Réglages, l'app reflète certaines données utilisateur via **`NSUbiquitousKeyValueStore`** d'Apple, lié à **votre identifiant Apple** :
| Audio de fond | Récitation en arrière-plan | TTS en arrière-plan |

Nous ne demandons **pas** de contacts, de localisation précise, de caméra, de microphone (au-delà de la lecture TTS du système) ou de suivi.

## Confidentialité des enfants

iThousand — app éducative, **pas** Kids Category.

## Tiers

Tiers : **Apple** (…traduction système, Spotlight).

## Conservation et suppression des données

- **Sur l’appareil :** effacer progression/historique/notes. Supprimer l’app efface sandbox/App Group.
- **iCloud :** désactivez la sync dans Réglages ; gérez le stockage iCloud dans Réglages système.
- **Pas de copies** de lecture, notes, signets de caractères.

## Modifications de cette politique

Nous pouvons mettre à jour cette page pour des raisons juridiques, produit ou conformité App Store. La date « Dernière mise à jour » changera. L’utilisation continue après une mise à jour vaut acceptation de la politique révisée.

## Nous contacter

Questions sur la vie privée : [AppleOSer@gmail.com](mailto:AppleOSer@gmail.com)
