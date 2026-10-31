iHTC Studio (« nous », « notre » ou « nos ») a développé iWuBi (également connu sous le nom « 爱五笔 »). Cette page décrit nos politiques en matière de collecte, d'utilisation et de divulgation des données lorsque vous utilisez notre app.

## Résumé

**iWuBi ne collecte, ne stocke ni ne transmet aucune donnée personnelle.** Toutes les recherches de mots, les quiz et la progression d'apprentissage sont traités entièrement sur votre appareil. Aucun compte n'est requis et aucune connexion Internet n'est nécessaire pour les fonctionnalités principales.

## Collecte de données

Nous ne collectons aucune donnée. Plus précisément :

- **Aucune information personnelle** n'est collectée (ni nom, ni e-mail, ni numéro de téléphone, ni compte).
- **Aucune donnée d'utilisation** ni analyse n'est collectée.
- **Aucun SDK tiers** de publicité, d'analyse ou de rapport de plantage n'est intégré.
- **Aucun cookie ni technologie de suivi** n'est utilisé.

## Synchronisation iCloud

iWuBi propose une synchronisation iCloud facultative (activable dans les Réglages). **La synchronisation iCloud est activée par défaut pour les nouveaux utilisateurs.** Lorsqu'elle est activée, les données suivantes sont synchronisées via le **stockage clé-valeur iCloud (iCloud KVS)**, un service entièrement fourni et géré par Apple :

| Données synchronisées | Finalité |
|-------------|---------|
| Favoris | Vos caractères mis en signet |
| Statut d'apprentissage | Niveau de progression pour chaque caractère |
| Carnet d'erreurs | Questions de quiz auxquelles vous avez mal répondu |
| Meilleur score de quiz | Votre meilleur score au quiz quotidien |
| Série | Votre série de quiz quotidiens consécutifs |
| Statistiques de saisie | Précision, série et nombre de sessions de l'entraînement à la saisie |
| Progression des textes intégrés | Position de reprise dans les textes de saisie intégrés |

Ces données sont transmises directement entre vos appareils via l'infrastructure iCloud d'Apple. iHTC Studio n'exploite aucun serveur et n'a pas accès à vos données iCloud. Le traitement des données iCloud par Apple est régi par la [politique de confidentialité d'Apple](https://www.apple.com/privacy/).

Vous pouvez désactiver la synchronisation iCloud à tout moment dans les Réglages. Lorsqu'elle est désactivée, toutes les données restent locales sur chaque appareil.

Les préférences de l'interface de saisie (clavier à l'écran, pinyin du texte, conservation des touches erronées) sont stockées localement sur chaque appareil et **ne** sont **pas** synchronisées via iCloud.

## Données stockées localement sur votre appareil

Toutes les données créées par iWuBi restent sur votre appareil :

| Données | Stockage | Contrôle de l'utilisateur |
|------|---------|--------------|
| Favoris | Local (UserDefaults) | Supprimer des éléments individuels ou tout effacer dans l'app |
| Statut d'apprentissage | Local (UserDefaults) | Réinitialisation dans les réglages de l'app |
| Carnet d'erreurs | Local (UserDefaults) | Effacement dans l'app |
| Scores de quiz et série | Local (UserDefaults) | Réinitialisation dans les réglages de l'app |
| Statistiques de saisie et progression des textes | Local (UserDefaults / App Group) ; iCloud KVS facultatif | Effacées lors de la réinitialisation des données d'apprentissage |
| Préférences de l'interface de saisie | Local (UserDefaults) | Modification dans Réglages → Saisie |
| Préférences de l'app et thème | Local (UserDefaults) | Réinitialisation en supprimant l'app |

Les widgets utilisent un conteneur **App Group** pour partager des données entre l'app principale et les extensions de widgets. Ce conteneur reste sur votre appareil et n'est accessible à aucun tiers.

## Pourboires dans l'app

iWuBi propose des pourboires facultatifs via **StoreKit 2**. Tout le traitement des paiements est entièrement géré par Apple. Nous ne recevons, ne stockons ni n'avons accès à aucune information financière, aucune donnée de carte bancaire ni aucune donnée d'identifiant Apple. Les transactions de pourboire sont régies par la politique de confidentialité et les conditions d'Apple.

## Autorisations

iWuBi ne demande aucune autorisation particulière sur l'appareil. Il n'y a aucun accès à votre appareil photo, au microphone, aux contacts, à la localisation, à la photothèque ni au réseau local.

## Confidentialité des enfants

iWuBi ne collecte sciemment de données personnelles auprès de personne, y compris des enfants de moins de 13 ans. Comme aucune donnée n'est collectée, aucune disposition particulière n'est nécessaire.

## Modifications de cette politique

Nous pouvons mettre à jour cette politique de confidentialité de temps à autre. Toute modification sera publiée sur cette page avec une date mise à jour. Nous vous encourageons à consulter régulièrement cette page.

## Nous contacter

Si vous avez des questions sur cette politique de confidentialité, veuillez nous contacter :

- **E-mail :** [AppleOSer@gmail.com](mailto:AppleOSer@gmail.com)
