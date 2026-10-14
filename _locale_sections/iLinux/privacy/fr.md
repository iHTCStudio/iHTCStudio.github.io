iHTC Studio (« nous », « notre » ou « notre ») a construit iLinux (également connu sous le nom de « 爱 Linux »). Cette page vous informe de nos politiques concernant la collecte, l'utilisation et la divulgation des données personnelles lorsque vous utilisez notre application.

## Résumé

**iLinux ne collecte pas d'analyses et ne vend pas de données personnelles.** Les bibliothèques de commandes s'exécutent entièrement hors ligne sur votre appareil. La **synchronisation iCloud** facultative (lorsqu'elle est activée et connectée à iCloud) stocke les favoris, la progression du quiz, le thème et les préférences d'affichage dans **votre** stockage de valeurs de clé iCloud sous votre identifiant Apple — iHTC Studio n'exploite pas de serveur principal pour ces données.

## Collecte de données

Nous n'opérons pas d'analyse, de publicité ou de suivi. Plus précisément :

- **Aucune information personnelle** n'est collectée par iHTC Studio (pas de nom, email, numéro de téléphone ou compte iHTC Studio).
- **Aucune analyse d'utilisation** ou SDK de rapport d'erreur n'est intégré.
- **Vos données d'apprentissage** (favoris, résultats aux quiz, mauvaises réponses) restent sur vos appareils et, si vous activez la synchronisation, dans **Apple iCloud** — pas sur les serveurs iHTC Studio.
- **Pas de cookies ni de trackers tiers** dans l'application.

## Comment fonctionne l'application

iLinux stocke toutes les données générées par l'utilisateur (favoris, vues récentes, résultats de session de quiz, enregistrements de réponses erronées, préférences de plate-forme shell, portée des favoris, bibliothèque de commandes de widget et préférences d'application) localement sur votre appareil :

- Toutes les données de commande (résumés JSON et documentation Markdown pour **Linux, CMD et PowerShell**) sont regroupées dans l'application et ne sont jamais récupérées depuis un serveur externe.
- Aucune connexion Internet n'est requise pour parcourir les commandes ou répondre à des quiz.
- La **synchronisation iCloud** facultative utilise le **NSUbiquitousKeyValueStore** d'Apple lorsque vous êtes connecté à iCloud et laissez la synchronisation activée. Vous pouvez le désactiver par appareil dans Paramètres.
- L'ouverture de liens externes depuis l'application (par exemple, en appuyant sur une URL dans la section Commentaires) utilise le comportement réseau iOS standard ; la page liée est chargée par votre appareil directement depuis son hôte, et non via un serveur iHTC Studio.
- La **vérification de version de l'App Store** facultative (`AppStoreVersionChecker`) envoie une seule requête en lecture seule à l'API publique de recherche iTunes pour comparer la version installée avec la dernière version. Aucune donnée personnelle n'est envoyée dans cette demande.

## Autorisations

iLinux demande l'accès à la **Photothèque** uniquement lorsque vous choisissez de **enregistrer une carte de partage ou une capture d'écran de commande** dans Photos. Aucun accès à la caméra, au microphone, à l’emplacement ou aux contacts n’est requis.

## Stockage des données

| Données | Emplacement de stockage |
|------|-----------------|
| Favoris, vues récentes, enregistrements de mauvaises réponses, statut d'apprentissage (par plateforme) | Paramètres utilisateur par défaut locaux/groupe d'applications sur votre appareil |
| Progression du quiz et résultats de la session quotidienne (saisis par date et plate-forme shell) | Bac à sable d'application locale sur votre appareil |
| Thème, langue, disposition en liste/grille, plateforme shell, portée des favoris, bibliothèque de widgets | Paramètres utilisateur par défaut locaux/groupe d'applications sur votre appareil |
| Miroir de synchronisation iCloud (facultatif) | Apple iCloud Key-Value Storage (`crossSync.*` keys) — favourites, quiz progress, theme, app preferences |
| Instantané du widget (iOS/iPad uniquement) | Conteneur de groupe d'applications (`group.com.iHTCboy.iLinuxs`) |

Aucune donnée n'est stockée sur un serveur exploité par iHTC Studio. Les données iCloud facultatives sont régies par les conditions iCloud d'Apple.

## Synchronisation iCloud (facultatif)

Lorsque **iCloud Sync** est activé et que vous êtes connecté à iCloud :

- Données synchronisées : **progression de l'apprentissage** (favoris, récents, statut d'apprentissage, résultats du quiz, enregistrements de mauvaises réponses), **thème** et **préférences d'application** (langue, plate-forme shell, portée des favoris, paramètres de liste/grille).
- Stockage : Apple **iCloud Key-Value Storage**, associé à votre identifiant Apple.
- Fusionner : les mises à jour en conflit sont fusionnées sur l'appareil (par exemple, union des favoris, derniers horodatages).
- Désinscription : désactivez-la dans **Paramètres → iCloud Sync** sur n'importe quel appareil ; cet appareil arrête le téléchargement et la fusion mais conserve les données locales.
- iHTC Studio ne peut pas lire votre conteneur iCloud.

## Groupe d’applications (extension de widget – iOS/iPad uniquement)

iLinux utilise un groupe d'applications (`group.com.iHTCboy.iLinuxs`) pour partager une petite quantité de données avec son extension de widget Écran d'accueil. Ces données comprennent :

- The selected content language code (e.g. `en`, `zh-Hans`)
- Un instantané des couleurs du thème (valeurs d'accent hexadécimal et de dégradé)
- Un résumé de vos progrès d'apprentissage (nombre de favoris, statistiques de quiz) pour l'affichage du widget
- La **bibliothèque de commandes de widget** sélectionnée (Linux / CMD / PowerShell)
- Le compteur de lecture aléatoire du widget Daily Command (un simple entier utilisé pour choisir la commande suivante)

Ces données sont écrites dans un conteneur partagé sur votre appareil uniquement et ne sont jamais transmises nulle part.

## Ce qu'iLinux n'est pas

iLinux n'exécute pas de commandes shell, n'ouvre pas de sessions SSH et n'accède pas aux systèmes distants. Aucune entrée de ligne de commande que vous pourriez saisir ailleurs n'est collectée par cette application.

## Achat intégré

iLinux inclut une option facultative de pourboire/achat. Toutes les transactions de paiement sont gérées exclusivement par **le framework StoreKit d'Apple**. iHTC Studio ne reçoit, ne traite ni ne stocke aucune information de carte de paiement ou de facturation.

## Confidentialité des enfants

iLinux ne collecte sciemment aucune donnée personnelle de qui que ce soit, y compris des enfants de moins de 13 ans. Puisque nous ne collectons aucune donnée, aucune disposition particulière n'est nécessaire.

## Modifications de cette politique

Nous pouvons mettre à jour cette politique de confidentialité de temps à autre. Tout changement sera publié sur cette page avec une date mise à jour. Nous vous encourageons à consulter cette page périodiquement.

## Contactez-nous

Si vous avez des questions concernant cette politique de confidentialité, veuillez nous contacter :

- **E-mail :** [AppleOSer@gmail.com](mailto:AppleOSer@gmail.com)
