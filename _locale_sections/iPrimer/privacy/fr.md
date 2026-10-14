**Dernière mise à jour :** 18 août 2026

iHTC Studio (« nous ») a développé **iPrimer** (« 爱小学 » / « 爱小学 », Bundle ID `com.iHTCboy.iPrimer`). Cette politique de confidentialité explique quelles données sont (ou ne sont pas) traitées lorsque vous utilisez l’app. **Apple App Review** et les utilisateurs peuvent s’appuyer sur **cette page** comme politique publique. Pour App Store Connect, ouvrez cette page dans le navigateur et copiez l’URL depuis la barre d’adresse (le domaine public peut changer).

## Résumé (alignement sur l'étiquette nutritionnelle de confidentialité Apple)

| Sujet | Notre pratique |
|-------|----------------|
| Compte | **Non requis** — pas d'inscription, de connexion par e-mail ou de numéro de téléphone |
| Collecte de données par iHTC Studio | **Données non collectées** — nous n'exploitons **pas** de backend qui reçoit vos données personnelles |
| Réseau | Bibliothèque, reading, recite, Character Study, meditation, Life Guidance, widgets, and daily notifications work **offline** after install fonctionnent **hors ligne** après l’installation |
| Analyses / publicités / suivi | **Aucun** — pas de SDK tiers d'analyse, de publicité ou de suivi ; pas d'utilisation de la transparence du suivi des applications |
| Services Apple en option | **iCloud** (votre KVS privé), **Photothèque (ajout uniquement)** pour les cartes de partage, **StoreKit** pour les pourboires facultatifs, **notifications locales**, **Activités en direct** en option |

## Collecte de données

Nous ne collectons, vendons ou partageons **pas** d'informations personnelles à des fins publicitaires ou analytiques.

- **Aucun compte** — Vous pouvez utiliser toutes les fonctionnalités principales sans créer de compte chez nous.
- **Aucune analyse ni publicité** — Le binaire de l'application n'intègre pas de SDK tiers d'analyse, de publicité ou de rapport d'erreur qui nous contactent.
- **Aucun envoi de contenu** — Vos reading history, favorites, study lists, reflection journal entries, habit check-ins, meditation streaks, study progress, and preferences stay on your device (and optionally in **your** iCloud). They are never uploaded to iHTC Studio servers because **we do not run such servers for this app**.

## Comment fonctionne l'application

- **Bibliothèque incluse** — JSON texte, vernaculaire/anglais, index et aides d’étude sont dans le bundle app/widget. Parcourir et étudier ne nécessite pas le réseau.
- **Discours sur l'appareil** — La récitation utilise le système **AVSpeechSynthesizer** (TTS) d'Apple. Nous n'envoyons pas de texte de chapitre à iHTC Studio.
- **Widgets et App Group** — Les widgets et l’app partagent des préférences et un état léger via l’App Group `group.com.iHTCboy.iPrimer` sur votre appareil.
- **Notifications quotidiennes** — Planifiées localement avec les notifications utilisateur. Appuyer sur une notification ouvre un lien profond vers un ID de chapitre sur l'appareil ; pas de distribution du serveur.
- **Partager des cartes** : les images sont rendues sur l'appareil. L'enregistrement utilise **le module complémentaire Photothèque** uniquement lorsque vous appuyez sur Enregistrer. System Share Sheet peut envoyer l'image à une application **que** vous choisissez ; la politique de confidentialité de cette destination s’applique alors.
- **Pourboire facultatif** — « Tip Developer » (`com.iHTCboy.iPrimer.6`), **StoreKit** via Apple.
- **Siri / Raccourcis / Centre de contrôle** — Les intégrations système facultatives ouvrent des liens profonds sur l'appareil ; ils ne nous envoient pas votre bibliothèque.
- **Spotlight facultatif** — Si vous activez l'indexation, le contenu est indexé par le système sur l'appareil pour la recherche locale ; nous n'exploitons pas de backend de recherche.

## Données stockées sur votre appareil

| Données | Où | Objectif |
|------|-------|--------------|
| Base Chapter | Bundle App / Widget | Lecture et étude hors ligne |
| Favoris et listes d’étude | UserDefaults de l’App Group | Œuvres favorites et listes |
| Historique de lecture / dernière lecture | Paramètres par défaut du groupe d'applications | Continuer la lecture, historique de l'interface utilisateur |
| Progression d’étude et maîtrise | UserDefaults de l’App Group | Character Study state, quiz / Hunt progress |
| Série d’étude / check-in | UserDefaults de l’App Group | Habitude Daily Study |
| Journal de réflexion | UserDefaults de l’App Group | Journal Life Guidance |
| Check-ins d’habitude (洒扫应对) | UserDefaults de l’App Group | Habitudes Life Guidance |
| Série méditation et prefs | UserDefaults de l’App Group | Continuité méditation |
| Préférences des cartes de partage | UserDefaults de l'App Group | Derniers choix de style / de format |
| Daily Study cache & notification prefs | UserDefaults de l’App Group | ID du jour, schedule time, contextual toggle |
| Préférences de carte partagée | Paramètres par défaut du groupe d'applications | Derniers choix de style/ratio |
| État d’intégration et de TipKit | Paramètres utilisateur standard (appareil) | Guide d'accueil / conseils découverte |
| Actions rapides sur l'écran d'accueil | Système + préférences locales | Raccourcis que vous configurez |
| Widget / Instantanés d'activité en direct | Groupe d'applications / ActivityKit | Afficher le texte que vous avez déjà ouvert |

La désinstallation de l'application supprime les données du bac à sable et du groupe d'applications associées à l'application (selon le comportement d'iOS/macOS). Les copies facultatives dans iCloud restent dans **votre** iCloud jusqu'à ce que vous les supprimiez ou que vous désactiviez la synchronisation et supprimiez ailleurs.

## Synchronisation iCloud (Facultative)

Si vous activez **la synchronisation iCloud** dans les Réglages, l'application reflète les données utilisateur sélectionnées via le **`NSUbiquitousKeyValueStore`** d'Apple lié à **votre identifiant Apple** :

- Favoris
- Listes d’étude
- Historique de lecture
- Progression / maîtrise des études
- Séries d’étude
- Journal de réflexion
- Historique d’habitudes

Le trafic de synchronisation passe par **Apple iCloud**, et non par iHTC Studio. Vous pouvez désactiver la synchronisation dans les Réglages. Nous ne pouvons pas lire le contenu de votre iCloud.

## Autorisations

iLiezi demande des autorisations uniquement lorsqu'une fonctionnalité en a besoin :

| Autorisation | Quand | Pourquoi |
|------------|------|-----|
| Notifications | Vous activez Daily Study or meditation reminders | Planification locale |
## Synchronisation iCloud (facultative)
| iCloud | Activez la sync | Favoris/listes/historique/progression/séries/journal/habitudes |
| Live Activities (iOS) | Reading/Meditation Live Activity | Écran verrouillé / Dynamic Island |
| Audio de fond | Récitation en arrière-plan | TTS en arrière-plan |

Nous ne demandons **pas** de contacts, de localisation précise, de caméra, de microphone (au-delà de la lecture TTS du système) ou de suivi.

## Confidentialité des enfants

iPrimer **12+**, **pas** Kids Category. Pas de collecte d’enfants.

## Tiers

Services tiers : **Apple** uniquement (App Store, iCloud, StoreKit, TTS, notifications, Live Activities).

## Conservation et suppression des données

- **Sur l’appareil :** supprimer l’app efface le sandbox et l’App Group (selon le système).
- **iCloud :** désactivez la sync dans Réglages ; gérez le stockage iCloud dans Réglages système.
- **Nous ne conservons pas de copies** de lecture, journal ou habitudes sur les serveurs iHTC Studio.

## Modifications de cette politique

Nous pouvons mettre à jour cette page pour des raisons juridiques, produit ou conformité App Store. La date « Dernière mise à jour » changera. L’utilisation continue après une mise à jour vaut acceptation de la politique révisée.

## Nous contacter

Questions sur la vie privée : [AppleOSer@gmail.com](mailto:AppleOSer@gmail.com)
