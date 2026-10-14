iHTC Studio (« nous », « notre » ou « nos ») a développé iCangJie (également connu sous le nom « 爱仓颉 » / « 愛倉頡 »). Cette page décrit nos politiques en matière de collecte, d'utilisation et de divulgation des données lorsque vous utilisez notre app.

## Résumé

**iCangJie ne collecte, ne stocke ni ne transmet aucune donnée personnelle.** Toutes les recherches de caractères, les quiz, l'entraînement à la saisie et la progression d'apprentissage sont traités entièrement sur votre appareil. Aucun compte n'est requis et aucune connexion Internet n'est nécessaire pour les fonctionnalités principales.

## Collecte de données

Nous ne collectons aucune donnée. Plus précisément :

- **Aucune information personnelle** n'est collectée (ni nom, ni e-mail, ni numéro de téléphone, ni compte).
- **Aucune donnée d'utilisation** ni analyse n'est collectée.
- **Aucun SDK tiers** de publicité, d'analyse ou de rapport de plantage n'est intégré.
- **Aucun cookie ni technologie de suivi** n'est utilisé.

## Synchronisation iCloud

iCangJie propose une synchronisation iCloud facultative (activable dans les Réglages). Lorsqu'elle est activée, les données suivantes sont synchronisées via le **stockage clé-valeur iCloud (iCloud KVS)**, un service entièrement fourni et géré par Apple :

| Données synchronisées | Finalité |
|-------------|---------|
| Favoris | Vos caractères mis en signet |
| Statut d'apprentissage | Niveau de progression pour chaque caractère |
| Carnet d'erreurs | Questions de quiz auxquelles vous avez mal répondu |
| Scores de quiz et série | Vos performances au quiz quotidien |
| Statistiques de saisie | Précision, série et nombre de sessions de l'entraînement à la saisie |
| Enregistrements quotidiens de saisie | Nombre de caractères par jour et histogrammes de longueur de code (~120 jours) |
| Progression des textes intégrés | Position de reprise dans les textes de saisie intégrés |

Ces données sont transmises directement entre vos appareils via l'infrastructure iCloud d'Apple. iHTC Studio n'exploite aucun serveur et n'a pas accès à vos données iCloud. Le traitement des données iCloud par Apple est régi par la [politique de confidentialité d'Apple](https://www.apple.com/privacy/).

Vous pouvez désactiver la synchronisation iCloud à tout moment dans les Réglages. Lorsqu'elle est désactivée, toutes les données restent locales sur chaque appareil.

Les préférences de l'interface de saisie (conservation des touches erronées, pinyin du texte) sont stockées localement sur chaque appareil et **ne** sont **pas** synchronisées via iCloud.

## Données stockées localement sur votre appareil

Toutes les données créées par iCangJie restent sur votre appareil :

| Données | Stockage | Contrôle de l'utilisateur |
|------|---------|--------------|
| Favoris | Local (UserDefaults / App Group) | Supprimer des éléments individuels ou tout effacer dans l'app |
| Statut d'apprentissage | Local (UserDefaults) | Réinitialisation dans les réglages de l'app |
| Carnet d'erreurs | Local (UserDefaults) | Effacement dans l'app |
| Scores de quiz et série | Local (UserDefaults) | Réinitialisation dans les réglages de l'app |
| Statistiques de saisie et enregistrements quotidiens | Local (UserDefaults / App Group) ; iCloud KVS facultatif | Effacés lors de la réinitialisation des données d'apprentissage |
| Progression des textes | Local (UserDefaults / App Group) ; iCloud KVS facultatif | Effacée lors de la réinitialisation des données d'apprentissage |
| Préférences de l'interface de saisie | Local (UserDefaults) | Modification dans Réglages → Saisie |
| Indicateurs de prise en main et de parcours débutant | Local (UserDefaults) | Réaffichés uniquement si vous réinitialisez les données de l'app |
| Préférences du quiz | Local (UserDefaults) | Modification dans les réglages du quiz |
| Préférence d'indexation Spotlight | Local (UserDefaults) | Commutateur dans Réglages → Raccourcis de l'écran d'accueil |
| Préférences de l'app et thème | Local (UserDefaults) | Réinitialisation en supprimant l'app |

Les widgets utilisent un conteneur **App Group** pour partager des données entre l'app principale et les extensions de widgets. Ce conteneur reste sur votre appareil et n'est accessible à aucun tiers.

### Sauvegarde JSON (à l'initiative de l'utilisateur)

Vous pouvez **exporter** un fichier de sauvegarde JSON (`.icangjie-backup`) contenant les données d'apprentissage. Le fichier est écrit à un emplacement **de votre choix** (Fichiers, AirDrop, etc.). **L'importation** lit un fichier que vous sélectionnez. iHTC Studio ne téléverse, n'héberge ni n'accède aux fichiers de sauvegarde.

### Indexation Spotlight (iOS, facultative)

Lorsqu'elle est activée, iCangJie indexe jusqu'à **80** favoris et caractères récents dans l'index Spotlight d'iOS **sur l'appareil** (domaine `com.iHTCboy.iCangJie.words`). Les entrées expirent après 30 jours. Ces données ne quittent jamais votre appareil, sauf via le système Spotlight d'Apple sur votre iPhone/iPad. Vous pouvez la désactiver à tout moment dans les Réglages.

## Autorisations

iCangJie ne demande **qu'une seule autorisation facultative** :

| Autorisation | Quand elle est demandée | Finalité |
|------------|----------------|---------|
| **Photothèque (ajout uniquement)** | Lorsque vous touchez **Enregistrer dans Photos** sur une image de tableau de racines dans un tutoriel | Enregistrer l'image dans votre photothèque |

iCangJie **ne** lit **pas** vos photos existantes. Il n'y a aucun accès à votre appareil photo, au microphone, aux contacts, à la localisation ni au réseau local pour les fonctionnalités principales.

Les fonctionnalités facultatives qui ouvrent des sites web externes (recherche en ligne Youdao, liens de tutoriel) utilisent le navigateur du système et n'accordent pas à iCangJie l'accès à votre historique de navigation.

## Confidentialité des enfants

iCangJie ne collecte sciemment de données personnelles auprès de personne, y compris des enfants de moins de 13 ans. Comme aucune donnée n'est collectée, aucune disposition particulière n'est nécessaire.

## Modifications de cette politique

Nous pouvons mettre à jour cette politique de confidentialité de temps à autre. Toute modification sera publiée sur cette page avec une date mise à jour. Nous vous encourageons à consulter régulièrement cette page.

## Nous contacter

Si vous avez des questions sur cette politique de confidentialité, veuillez nous contacter :

- **E-mail :** [AppleOSer@gmail.com](mailto:AppleOSer@gmail.com)
