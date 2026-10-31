### iWool fonctionne-t-il sur iPad ?

Oui. iWool est une application universelle pour **iPhone et iPad** (iOS 15.0+). La mise en page s'adapte aux tailles d'écran de l'iPad ; les widgets et les activités en direct suivent les mêmes règles que sur iPhone.

### iWool nécessite-t-il un compte ou une connexion Internet ?

Non, iWool fonctionne entièrement hors ligne. Toutes les données sont stockées localement sur votre appareil à l'aide de SQLite. Aucun compte, aucune inscription et aucune connexion réseau ne sont requis pour utiliser une fonctionnalité (sauf l'ouverture de liens http/https dans l'application).

### Où sont stockées mes données ? Est-ce sécuritaire?

Toutes les données (activités, rappels, enregistrements de revenus, états de récurrence) sont stockées dans une base de données SQLite locale sur votre appareil. Rien n'est téléchargé sur un serveur. Si vous désinstallez l'application, vos données seront supprimées. Sauvegardez régulièrement en utilisant **Paramètres → Données → Exporter la sauvegarde complète**.

### Comment sauvegarder et restaurer mes données ?

Accédez à **Paramètres → Données → Exporter la sauvegarde complète** pour générer un fichier CSV. Enregistrez-le dans Fichiers, AirDrop sur votre Mac ou envoyez-le par e-mail.

Pour restaurer, accédez à **Paramètres → Données → Importer une sauvegarde** et choisissez votre fichier. Il vous sera demandé de choisir entre :

- **Remplacer toutes les données** : efface tout et restaure à partir de la sauvegarde. Utilisez-le lors du changement d'appareil ou de la réinstallation.
- **Ajouter uniquement (conserver l'existant)** : insère les activités de sauvegarde en tant que nouveaux enregistrements sans rien supprimer sur votre appareil. Utilisez-le pour fusionner les données d'un autre appareil.

### Comment fonctionnent les activités récurrentes ?

Lorsque vous définissez une règle de récurrence (quotidienne, hebdomadaire, mensuelle, annuelle ou intervalle personnalisé), iWool stocke un enregistrement principal et l'étend virtuellement en occurrences individuelles chaque jour. La liste et le calendrier affichent toujours l'occurrence du jour pour une série récurrente.

Pour marquer l'événement d'un jour spécifique comme terminé, utilisez le menu à pression longue ou la barre d'outils inférieure de la page de détail. Cela marque seulement ce jour-là ; la série continue.

### Pourquoi un rappel ne s'affiche-t-il pas ?

iOS limite chaque application à environ 64 notifications locales en attente à la fois. iWool donne la priorité aux activités non récurrentes et planifie jusqu'à 120 jours d'occurrences futures pour les activités récurrentes, mais de très grandes collections de rappels récurrents peuvent être supprimées.

Vérifiez **Paramètres → Notifications → Rappels locaux programmés** pour voir exactement quels rappels sont actuellement enregistrés.

Vérifiez également :

- L'autorisation de notification est accordée (Paramètres iOS → iWool → Notifications).
- L'activité n'est pas annulée (les activités annulées voient leurs rappels effacés automatiquement).
- L'heure de rappel est dans le futur.

### Quelle est la différence entre les « gains estimés » et les « gains enregistrés » ?

- **Revenus estimés** — saisis dans le formulaire d'activité. Affiché sur la carte d'activité. Ne compte pas dans les statistiques.
- **Revenus enregistrés** — saisis dans la page de détail de l'activité via le formulaire de gains. Il s’agit des montants réels comptabilisés dans tous les totaux statistiques, graphiques de tendances et classements des plateformes.

### Comment enregistrer les gains pour une journée spécifique d'une activité récurrente ?

Ouvrez les détails de l'activité pour l'événement de ce jour (appuyez sur l'activité dans la liste ou le calendrier de ce jour). Dans la page de détails, appuyez sur **Enregistrer** dans la section des revenus. La date d'enregistrement sera par défaut la date d'occurrence de ce jour.

### Puis-je supprimer une seule entrée de revenus sans affecter l’activité ?

Oui. Ouvrez les détails de l'activité, appuyez sur la ligne de revenus que vous souhaitez modifier et, dans le formulaire de modification, faites défiler vers le bas. Appuyez sur **Supprimer cet enregistrement de revenus** et confirmez. Seule cette entrée est supprimée ; l'activité et tous les autres enregistrements restent intacts.

### Le tableau des statistiques affiche des montants erronés pour le yen japonais (JPY)/le won coréen (KRW).

Ces devises n'ont pas de décimale par défaut, ce qui pouvait faire apparaître les montants sous forme de nombres entiers dans les anciennes versions. Dans la version actuelle, vous pouvez configurer indépendamment le nombre de décimales :

- Accédez à **Paramètres → Apparence et langue → Décimales du montant** pour définir le nombre de décimales pour tous les affichages des montants (par défaut : 2).
- Accédez à **Paramètres → Apparence et langue → Décimales du montant du graphique** pour définir spécifiquement les décimales des étiquettes des barres du graphique (par défaut : 0).

### Comment utiliser la fonctionnalité Dynamic Island / Live Activity ?

**Compte à rebours de l'événement** (iOS 16.1+, iPhone pris en charge) : activez dans **Paramètres → Notifications → Activité en direct**. Définissez le délai de livraison (1 à 480 minutes). Les activités dans la fenêtre sont sélectionnées automatiquement ; appuyez longuement sur Accueil ou Calendrier → **Ajouter à Dynamic Island**.

**Quick Countdown** (iOS 16.2+): a **standalone** island timer **not tied to your activity database**. Open **Settings → Island Reminder**, use a Home Screen Quick Action, or `iwool://island`. Duration **1 second to 8 hours**; optional title, note and accent colour. When it ends, the Live Activity dismisses — nothing is saved unless you create a wool activity separately.

### Qu'est-ce que le compte à rebours rapide par rapport à l'activité en direct d'un événement ?

|  | Compte à rebours de l'événement | Compte à rebours rapide |
|---|-----------------|-----------------|
| Lié à l'activité | Oui | Non |
| Persisté dans l'application | Oui | Non |
| iOS minimum | 16.1 | 16.2 |
| Comment commencer | Activité automatique ou appui long | Paramètres / raccourci / `iwool://island` |

### Comment fonctionnent les actions rapides de l'écran d'accueil ?

Appuyez longuement sur l'icône iWool (iOS). Choisissez jusqu'à **4** parmi **9** préréglages dans **Paramètres → Outils → Raccourcis de l'écran d'accueil** : Accueil, Calendrier, Statistiques, Compte à rebours rapide, Nouvelle activité, Rappels programmés, Scanner, Taux, Commentaires. Par défaut : Accueil, Calendrier, Statistiques, Compte à rebours rapide. Chacun utilise une URL `iwool://`.

### Comment fonctionnent les liens profonds `iwool://` ?

iWool prend en charge **`iwool://`** pour les onglets, les actions et les détails des événements — utilisés par les widgets, les raccourcis et les actions rapides. Exemples :

- `iwool://home`, `iwool://calendar`, `iwool://stats`, `iwool://settings`
- `iwool://new`, `iwool://island`, `iwool://scanner`, `iwool://reminders`
- `iwool://event/42`, `iwool://event/42?day=189345600` (occurrence récurrente)

Les chemins inconnus sont ignorés (pas de redirection silencieuse vers Home). Consultez la [**référence du schéma d'URL**](../url-scheme) complète.

### Comment partager une activité ou des statistiques sous forme d'image ?

À partir d'une page de détails d'activité ou de la barre d'outils de l'onglet **Statistiques**, utilisez **Partager** pour afficher une **carte image PNG** de marque (dégradé, code QR, gains facultatifs si activés dans les paramètres). L'image est générée sur l'appareil ; l'enregistrement dans Photos peut demander l'accès à la photothèque.

### Combien de widgets iWool inclut-il ?

**12 familles de widgets** : huit widgets d'écran d'accueil (Aujourd'hui actif, Aujourd'hui tout, Aujourd'hui à venir, Tous les événements, Aperçu des statistiques, Gains, Aperçu, Principales plates-formes) ainsi que quatre styles d'accessoires d'écran de verrouillage (iOS 16+).

### Comment ajouter des widgets à mon écran d'accueil ou à mon écran de verrouillage ?

Des instructions détaillées étape par étape sont disponibles dans **Paramètres → Widgets → Guide des widgets** dans l'application. En bref :

1. Appuyez longuement sur une zone vide de votre écran d'accueil et appuyez sur le bouton **+**.
2. Recherchez **iWool** dans la galerie de widgets.
3. Choisissez un style et une taille de widget, puis appuyez sur **Ajouter un widget**.

Pour les widgets d'écran de verrouillage (iOS 16+) : appuyez longuement sur votre écran de verrouillage et appuyez sur **Personnaliser**, puis ajoutez les widgets iWool à la rangée de widgets d'écran de verrouillage.

### Pourquoi le widget affiche-t-il des données obsolètes ?

Les widgets s'actualisent lorsque vous ouvrez l'application ou lorsque les données changent. iOS actualise également périodiquement la chronologie des widgets en arrière-plan (environ toutes les 15 minutes au mieux). Si le widget est obsolète, ouvrez iWool une fois pour forcer une actualisation.

### Comment changer la langue d'affichage ?

Accédez à **Paramètres → Apparence et langue → Langue d'affichage**. Vous pouvez choisir parmi 13 langues indépendamment de la langue système de votre appareil :

Anglais, chinois simplifié, chinois traditionnel, japonais, coréen, thaï, hindi, espagnol, français, allemand, portugais brésilien, russe, arabe.

Le changement prend effet immédiatement dans toute l’application.

### Puis-je partager une activité sans partager le montant de mes gains ?

Oui. Par défaut, la copie ou le partage d'une activité n'inclut pas vos enregistrements de revenus. Si vous souhaitez les inclure, accédez à **Paramètres → Apparence et langue** et activez **Inclure les revenus lors du partage**.

### Comment scanner un code QR ou un code-barres ?

Accédez à **Paramètres → Outils → Scanner QR/code-barres**. Pointez votre appareil photo sur un code ou appuyez sur l'icône de l'album pour choisir une image. Les résultats apparaissent dans une liste que vous pouvez copier ou ouvrir dans Safari.

Vous pouvez également scanner directement à partir du formulaire d'activité : lorsque vous remplissez le champ URL de l'activité, appuyez sur l'icône de numérisation à côté pour scanner un code et remplir automatiquement l'URL.

### Que signifie « archiver » ? Est-ce la même chose que supprimer ?

Non. L'archivage masque une activité de la liste principale sans la supprimer. Les activités archivées peuvent être consultées, restaurées ou supprimées depuis **Paramètres → Gestion des activités → Activités archivées**.

Appuyez longuement sur une activité terminée, expirée ou annulée pour voir l'option Archiver. Pour archiver toutes les activités non récurrentes terminées, expirées et annulées en même temps, utilisez **Paramètres → Gestion des activités → Archiver tout terminé**.

### Vous avez encore besoin d'aide ?

Contactez-nous à [AppleOSer@gmail.com](mailto:AppleOSer@gmail.com) ou utilisez l'option **Paramètres → Envoyer des commentaires** de l'application. Nous répondons généralement dans les 48 heures.
