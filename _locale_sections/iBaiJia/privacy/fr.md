**Dernière mise à jour :** 18 août 2026

iHTC Studio (« nous ») a développé **iBaiJia** (« 爱百家姓 » / « 爱百家姓 », Bundle ID `com.iHTCboy.iBaiJia`). Cette politique de confidentialité explique quelles données sont (ou ne sont pas) traitées lorsque vous utilisez l’app. **Apple App Review** et les utilisateurs peuvent s’appuyer sur **cette page** comme politique publique. Pour App Store Connect, ouvrez cette page dans le navigateur et copiez l’URL depuis la barre d’adresse (le domaine public peut changer).

## Résumé (alignement sur l'étiquette nutritionnelle de confidentialité Apple)

| Sujet | Notre pratique |
|-------|----------------|
| Compte | **Non requis** — pas d'inscription, de connexion par e-mail ou de numéro de téléphone |
| Collecte de données par iHTC Studio | **Données non collectées** — nous n'exploitons **pas** de backend qui reçoit vos données personnelles |
| Réseau | Surname library, detail reading, recite, Study Hall, naming inspiration, widgets, and daily notifications work **offline** after install |
| Analyses / publicités / suivi | **Aucun** — pas de SDK tiers d'analyse, de publicité ou de suivi ; pas d'utilisation de la transparence du suivi des applications |
| Services Apple facultatifs | **iCloud** (your private KVS), **Photo Library (Add Only)** for share cards, **StoreKit** for pourboire facultatif, **local notifications**, optional **Live Activities**, optional **Spotlight** (off by default), optional **system speech / translation** |

## Collecte de données

Nous ne collectons, vendons ou partageons **pas** d'informations personnelles à des fins publicitaires ou analytiques.

- **Aucun compte** — Vous pouvez utiliser toutes les fonctionnalités principales sans créer de compte chez nous.
- **Aucune analyse ni publicité** — Le binaire de l'application n'intègre pas de SDK tiers d'analyse, de publicité ou de rapport d'erreur qui nous contactent.
- **Aucun envoi de contenu** — Vos favorites, surname lists, notes, reading history, study progress, streaks, naming preferences, and settings stay on your device (and optionally in **your** iCloud). They are never uploaded to iHTC Studio servers because **we do not run such servers for this app**.

## Comment fonctionne l'application

- **Bibliothèque incluse** — JSON texte, vernaculaire/anglais, index et aides d’étude sont dans le bundle app/widget. Parcourir et étudier ne nécessite pas le réseau.
- **Voix sur l’appareil** — lecture/récitation via **AVSpeechSynthesizer**. Pas de texte de noms à iHTC Studio.
- **Traduction système facultative** — Apple Translation ; traitement dans l’OS Apple.
- **Inspiration de noms** — entièrement sur l’appareil à partir de données intégrées. Aucun envoi de noms ou préférences.
- **Widgets et App Group** — Les widgets et l’app partagent des préférences et un état léger via l’App Group `group.com.iHTCboy.iBaiJia` sur votre appareil.
- **Notifications quotidiennes** — planifiées localement. Ouvre un lien profond ; pas de serveur.
- **Partager des cartes** : les images sont rendues sur l'appareil. L'enregistrement utilise **le module complémentaire Photothèque** uniquement lorsque vous appuyez sur Enregistrer. System Share Sheet peut envoyer l'image à une application **que** vous choisissez ; la politique de confidentialité de cette destination s’applique alors.
- **Pourboire facultatif** — « Tip Developer » (`com.iHTCboy.iBaiJia.6`), **StoreKit** via Apple.
- **Siri / Raccourcis / Centre de contrôle** — Les intégrations système facultatives ouvrent des liens profonds sur l'appareil ; ils ne nous envoient pas votre bibliothèque.
- **Spotlight facultatif** — noms indexés sur l’appareil.
- **Email de commentaires** — peut inclure votre texte et des diagnostics appareil/app (version, OS, langue) pour le dépannage.

## Données stockées sur votre appareil

| Données | Où | Objectif |
|------|-------|--------------|
| Base noms et traits | Bundle de l’app | Lecture, tracé, étude |
| Favoris et listes de noms | UserDefaults de l’App Group | Noms favoris et listes |
| Notes | UserDefaults de l’App Group | Notes sur noms |
| Mon nom de famille | UserDefaults de l’App Group | Accueil et widgets personnalisés |
| Historique / dernière lecture | UserDefaults de l’App Group | Poursuite, UI historique |
| Progression et scores | UserDefaults de l’App Group | État Study Hall |
| Série de check-in | UserDefaults de l’App Group | Habitude quotidienne |
| Apparence et préférences de lecture | Paramètres par défaut du groupe d'applications | Thème, accent, langue, mise en page, TTS, onglets, widgets |
| Daily Surname cache & notification prefs | UserDefaults de l’App Group | ID du jour, schedule time |
| Préférences cartes partagées | UserDefaults de l’App Group | Last style choices |
| État d’intégration et de TipKit | Paramètres utilisateur standard (appareil) | Guide d'accueil / conseils découverte |
| Actions rapides sur l'écran d'accueil | Système + préférences locales | Raccourcis que vous configurez |
| Widget / Instantanés d'activité en direct | Groupe d'applications / ActivityKit | Afficher le texte que vous avez déjà ouvert |

La désinstallation de l'application supprime les données du bac à sable et du groupe d'applications associées à l'application (selon le comportement d'iOS/macOS). Les copies facultatives dans iCloud restent dans **votre** iCloud jusqu'à ce que vous les supprimiez ou que vous désactiviez la synchronisation et supprimiez ailleurs.

## Synchronisation iCloud (Facultative)

Si vous activez **la synchronisation iCloud** dans les Réglages, l'application reflète les données utilisateur sélectionnées via le **`NSUbiquitousKeyValueStore`** d'Apple lié à **votre identifiant Apple** :

- Favoris
- Listes de noms
- Remarques
- Historique de lecture
- Progression / meilleurs scores
- Séries de check-in
- Préférences associées

Le trafic de synchronisation passe par **Apple iCloud**, et non par iHTC Studio. Vous pouvez désactiver la synchronisation dans les Réglages. Nous ne pouvons pas lire le contenu de votre iCloud.

## Autorisations

iLiezi demande des autorisations uniquement lorsqu'une fonctionnalité en a besoin :

| Autorisation | Quand | Pourquoi |
|------------|------|-----|
| Notifications | Vous activez Daily Surname reminders | Planification locale |
## Synchronisation iCloud (facultative)
| iCloud | Activez la sync | Favoris/listes/historique/progression/séries/notes |
Si vous activez la **synchronisation iCloud** dans les Réglages, l'app reflète certaines données utilisateur via **`NSUbiquitousKeyValueStore`** d'Apple, lié à **votre identifiant Apple** :
| Audio de fond (iOS) | Récitation en arrière-plan | TTS en arrière-plan |

Nous ne demandons **pas** de contacts, de localisation précise, de caméra, de microphone (au-delà de la lecture TTS du système) ou de suivi.

## Confidentialité des enfants

iBaiJia est une application d’apprentissage culturel pour le grand public et **n’est pas** dans la Kids Category. Nous ne collectons pas sciemment d’informations personnelles auprès d’enfants. L’app ne nécessite pas de compte. Les familles peuvent utiliser lecture et étude hors ligne sur leurs propres appareils.

## Tiers

Tiers : **Apple**. Jeux de noms : CC BY 4.0, LGPL/Arphic (About).

## Conservation et suppression des données

- **Sur l’appareil :** effacer, export/import dans Réglages. Supprimer l’app.
- **iCloud :** désactivez la sync dans Réglages ; gérez le stockage iCloud dans Réglages système.
- **Pas de copies** de lecture, notes, favoris.

## Modifications de cette politique

Nous pouvons mettre à jour cette page pour des raisons juridiques, produit ou conformité App Store. La date « Dernière mise à jour » changera. L’utilisation continue après une mise à jour vaut acceptation de la politique révisée.

## Nous contacter

Questions sur la vie privée : [AppleOSer@gmail.com](mailto:AppleOSer@gmail.com)
