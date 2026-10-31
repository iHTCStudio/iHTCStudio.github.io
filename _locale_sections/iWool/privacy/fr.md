iHTC Studio (« nous », « notre » ou « notre ») a créé iWool (également connu sous le nom de « 爱羊毛 »). Cette page vous informe de nos politiques concernant la collecte, l'utilisation et la divulgation des données personnelles lorsque vous utilisez notre application.

## Résumé

**iWool ne collecte, ne stocke ni ne transmet aucune donnée personnelle.** L'application fonctionne entièrement sur votre appareil local et ne nécessite aucun compte, aucune connexion Internet et aucun service cloud.

## Collecte de données

Nous ne collectons aucune donnée. Plus précisément :

- **Aucune information personnelle** n'est collectée (pas de nom, email, numéro de téléphone ou compte).
- **Aucune donnée d'utilisation** ou analyse n'est collectée.
- **Aucune activité, aucun gain ou tout contenu** que vous créez dans l'application ne nous est accessible.
- **Aucun cookie ni aucune technologie de suivi** n'est utilisé.
- **Aucun service tiers** (publicité, analyses, rapports d'erreur) n'est intégré.

## Comment fonctionne l'application

iWool stocke toutes les données (activités, rappels, enregistrements de revenus, états de récurrence et modèles) dans une base de données SQLite locale sur votre appareil :

- Les données ne quittent jamais votre appareil, sauf si vous exportez explicitement une sauvegarde et choisissez de la partager vous-même.
- Aucune connexion Internet n'est requise pour les fonctionnalités principales de l'application.
- L'ouverture de liens http/https depuis l'application (dans la vue Safari intégrée) suit le comportement réseau standard d'iOS ; la page liée est chargée par votre appareil directement depuis son hôte, et non via un serveur iHTC Studio.

## Autorisations

iWool demande les autorisations de périphérique suivantes, uniquement lorsque cela est nécessaire :

| Autorisation | Objectif |
|------------|---------|
| Notifications | Planifiez et envoyez des rappels locaux pour vos activités |
| Appareil photo | Scannez les codes QR et les codes-barres via l'outil de numérisation intégré |
| Photothèque (lire) | Choisissez des images pour la reconnaissance QR/code-barres |
| Activités en direct | Afficher l'activité en direct de l'îlot dynamique et de l'écran de verrouillage pour les activités à venir (iOS 16.1+) |

Ces autorisations sont utilisées uniquement aux fins indiquées. Aucune donnée accessible via ces autorisations n'est transmise à un serveur externe ou à un tiers.

## Stockage des données

- **Les données d'activité** (activités, rappels, enregistrements de revenus, états d'achèvement de récurrence, modèles) sont stockées localement dans un fichier de base de données SQLite (`iWool.sqlite`) dans le répertoire de support de l'application sur votre appareil.
- **Les préférences de l'application** (thème, langue, devise, stratégie de badge, paramètres de rappel, etc.) sont stockées localement à l'aide de UserDefaults sur votre appareil.
- **Instantané du widget** — un résumé JSON léger de vos activités et revenus actuels — est écrit dans un conteneur de groupe d'applications (`group.com.iHTCboy.iWool`) partagé entre l'application principale et l'extension du widget. Ces données ne quittent jamais votre appareil.
- Aucune donnée n'est stockée sur un serveur externe ou un service cloud.

## Sauvegarder des fichiers et partager des images

Lorsque vous utilisez **Paramètres → Données → Exporter la sauvegarde complète**, iWool génère un fichier CSV sur votre appareil. Le fichier contient vos activités, rappels, enregistrements de revenus, états de récurrence et modèles. Ce fichier est créé localement et n'est partagé que si vous choisissez explicitement de le partager (par exemple, en l'enregistrant dans Fichiers ou en l'envoyant via AirDrop ou par e-mail). Nous n'avons pas accès à ce fichier.

Les **Cartes d'image de partage** (PNG) s'affichent entièrement sur votre appareil lorsque vous appuyez sur Partager dans une vue d'activité ou de statistiques. iWool ne télécharge pas ces images.

## Confidentialité des enfants

iWool ne collecte sciemment aucune donnée personnelle de qui que ce soit, y compris des enfants de moins de 13 ans. Étant donné que nous ne collectons aucune donnée, aucune disposition particulière n'est nécessaire.

## Modifications de cette politique

Nous pouvons mettre à jour cette politique de confidentialité de temps à autre. Tout changement sera publié sur cette page avec une date mise à jour. Nous vous encourageons à consulter cette page périodiquement.

## Contactez-nous

Si vous avez des questions concernant cette politique de confidentialité, veuillez nous contacter :

- **E-mail :** [AppleOSer@gmail.com](mailto:AppleOSer@gmail.com)
