### Pourquoi devrais-je choisir iPomodoro plutôt que d'autres applications Pomodoro ?

iPomodoro est une application **native SwiftUI** conçue pour les plateformes Apple — ce n'est pas un minuteur basé sur le web. Vous bénéficiez de **cinq onglets intégrés** (Pomodoro, Minuteur d'étude, Tâches, Statistiques, Paramètres), de **deux Live Activities**, de **cinq familles de widgets**, de **9 badges de réussite**, de **plus de 1000 citations sur l'appareil**, de **raccourcis Siri et URL**, et de **la synchronisation iCloud en option** — le tout avec **aucune analyse** et **aucun compte requis**. Une application apaisante qui couvre la concentration, les délais et le suivi des progrès de A à Z.

### Où se trouvent les paramètres du minuteur et des tâches ?

Les durées du minuteur, les sons, l’Activité en direct, les couleurs du thème de la page, le **rappel optionnel du mode Focus**, et (Pomodoro seulement) la **confirmation de la fin de phase optionnelle** se trouvent sous l’**icône d’engrenage** de chaque onglet (Pomodoro, Minuteur d’étude, Tâches ou **Statistiques**). L’onglet global **Paramètres** contient l’apparence, la langue, les **raccourcis sur l’écran d’accueil**, le **Guide de l’application**, l’autorisation des notifications, les citations motivantes (y compris la **notification de motivation quotidienne**), le guide des widgets, les retours et les informations — pas les durées propres à chaque mode. Les paramètres **Statistiques** (thème de la page, objectifs, synchronisation iCloud optionnelle, réussites, règles de comptage, CSV, conservation) se trouvent sous **Onglet Statistiques → engrenage**.

### Comment fonctionnent les raccourcis sur l’écran d’accueil et Siri ?

**Appuyez longuement sur l'icône de l'application** pour des actions rapides : ouvrez Pomodoro, le minuteur d'étude, les tâches, les statistiques, une citation de motivation ou des commentaires. Personnalisez les quatre qui apparaissent sous **Paramètres → Paramètres de l'application → Raccourcis de l'écran d'accueil** (faites glisser pour réorganiser). Vous pouvez également ouvrir les mêmes destinations via les URL **`iPomodoro://`** (`pomodoro`, `study`, `tasks`, `stats`, `motivation`, `feedback` ; `iPomodoros://` fonctionne également). Consultez la [Référence du schéma d'URL] complète (../url-scheme). **L'application Siri/Raccourcis** peut ouvrir des onglets ou répondre *"Combien de temps ai-je été concentré aujourd'hui dans iPomodoro ?"* via les raccourcis d'application intégrés. 

### Qu'est-ce que le guide de l'application intégré à l'application ? 

**Paramètres → Paramètres de l'application → Guide de l'application** — un didacticiel pliable couvrant les cinq onglets, widgets, raccourcis, iCloud et FAQ (style similaire au guide des widgets). 

### iPomodoro peut-il activer le mode Focus pour moi ? 

Non : iOS n'autorise pas les applications tierces à activer directement Focus. Le **Rappel du mode de mise au point** en option (paramètres d'équipement Pomodoro ou Study Timer) vérifie si la mise au point est désactivée lorsque vous démarrez une minuterie et affiche une alerte ; vous pouvez ouvrir les **Paramètres** à partir de l'alerte, mais vous devez activer Focus vous-même. 

### Puis-je choisir une couleur pour chaque tâche du compte à rebours ?

Oui. Lors de l'ajout ou de la modification d'une tâche, choisissez l'une des **9 couleurs d'accent**. La liste et le widget **Tâches à compte à rebours** utilisent cette couleur par ligne. Les couleurs se synchronisent via iCloud lorsque la synchronisation des tâches est activée.

### Puis-je filtrer les statistiques par une plage de dates personnalisée ?

Oui. Dans l'onglet Statistiques (ou le rapport de période), sélectionnez **Personnalisé** dans la barre de période, puis définissez les dates de début et de fin. La plage est sauvegardée lorsque **Se souvenir du filtre** est activé dans les paramètres des Statistiques.

### Puis-je recevoir une notification de motivation quotidienne ?

Oui. **Paramètres → Paramètres de citation motivationnelle** inclut une **notification de motivation quotidienne** optionnelle — choisissez une heure et iPomodoro planifie une **notification locale** récurrente avec une ligne aléatoire du pool de citations disponibles sur l'appareil (sans réseau). C'est séparé des alertes de fin de minuterie.

### Quelle est la différence entre les citations quotidiennes et les citations de notification ?

**Dialogues/citations quotidiennes** (**1000+** combinées lorsque le filtre est Tout — chinois simplifié + anglais) alimentent la fenêtre contextuelle au démarrage, la navigation dans les paramètres, l'indice Live Activity et le widget Motivation. **Citations de notifications** sont un pool séparé sur l'appareil (**365 lignes générales par langue**) utilisé uniquement pour les alertes de fin de minuterie en arrière-plan. Les deux respectent votre filtre de langue des citations dans les Paramètres.

### Qu'est-ce que la technique Pomodoro ?

La technique Pomodoro est une méthode de gestion du temps : travailler par intervalles concentrés (classiquement 25 minutes), puis prendre une courte pause. Après plusieurs cycles, prendre une pause plus longue. iPomodoro automatise ce rythme pour que vous puissiez vous concentrer sur le travail, pas sur l'horloge.

### En quoi iPomodoro est-il différent de l'ancienne version Flutter ?

Ceci est une **réécriture complète en SwiftUI** pour les plateformes Apple. Même idée de base — Pomodoro, minuterie d'étude, tâches avec compte à rebours — mais avec des performances natives, Live Activity, widgets modernes et intégration iOS plus poussée.

### Ai-je besoin d'un compte ou d'une connexion Internet ?

Aucun compte iPomodoro n'est requis. Les minuteries, les statistiques d'étude, les thèmes et les widgets fonctionnent **entièrement hors ligne** sur votre appareil. **Facultatif :** activez **Synchroniser les tâches avec iCloud** (Tâches → équipement) et/ou **Synchroniser les statistiques d'étude avec iCloud** (Statistiques → équipement) pour fusionner les données sur tous les appareils connectés au même identifiant Apple. Cela utilise Apple CloudKit, pas nos serveurs. Internet est également utilisé pour les mises à jour de l'App Store ou les e-mails de commentaires. 

### Comment fonctionnent les statistiques d'études ? 

Ouvrez l'onglet **Statistiques**. Filtrer par Tous / Pomodoro / Minuterie d'étude et par Aujourd'hui / Semaine / Mois / Année / Tout le temps / **Plage de dates personnalisée**. Le tableau de bord affiche l'**aperçu du jour**, la **progression des objectifs**, une comparaison semaine après semaine, une **carte thermique mensuelle**, des **réalisations**, des graphiques des jours de la semaine et de l'heure et une **répartition par tâche liée**. Appuyez sur l'**icône d'engrenage** pour les objectifs, la **synchronisation iCloud** facultative, les règles de comptage, l'**exportation/importation CSV** et la conservation des données. Les statistiques ne sont **jamais téléchargées sur nos serveurs** (en option, iCloud utilise Apple CloudKit sous votre identifiant Apple). 

### Puis-je exporter ou importer des statistiques d'études ?

Oui. **Onglet Statistiques → engrenage → Exporter** partage un fichier CSV via la feuille de partage système. **Importer** accepte le même format (`kind,started_at,ended_at,duration_seconds,outcome` plus `task_id,task_title,cloud_id` facultatif) : choisissez **fusionner** (ignorer les doublons) ou **remplacer tout**. Utile pour la sauvegarde ou la migration manuelle. Pour une synchronisation automatique entre appareils, activez plutôt **Synchroniser les statistiques d'étude avec iCloud**. 

### Puis-je partager mes statistiques sous forme d'image ? 

Oui. iPomodoro peut restituer des **cartes instantanées de marque** (métriques de focus + code QR de l'App Store) pour le **tableau de bord de statistiques** (partage de la barre d'outils), les **rapports périodiques**, les résumés de l'**année en revue** et les **réalisations** (liste complète ou badge unique). Les cartes de partage de statistiques utilisent les couleurs de votre **thème de page à onglet Statistiques**. Vous pouvez également partager une **carte de promotion d'application** depuis Paramètres → Partager l'application. 

### Puis-je synchroniser les statistiques d'études avec iCloud ? 

Oui — **Onglet Statistiques → Équipement → Synchroniser les statistiques de l'étude avec iCloud**. Ceci est ** distinct ** de la tâche de synchronisation iCloud. Les sessions fusionnent par `cloudId` sur vos appareils Apple ID via le type d'enregistrement CloudKit `StudySession`. **Paramètres d'objectifs quotidiens** (`StatsGoals`) et **état de déverrouillage/célébration des succès** (`StatsAchievements`) se synchronisent sous la même bascule lorsqu'ils sont activés.

### Comment fonctionnent les objectifs de concentration quotidiens ? 

**Statistiques → équipement → Objectifs** : définissez le nombre quotidien de pomodoro, les minutes de concentration quotidiennes et les minutes de concentration hebdomadaires. La progression apparaît sur le tableau de bord Statistiques et sur le widget **Statistiques du jour** lorsqu'il est activé. 

### Comment lier une tâche de compte à rebours à une session de focus ? 

Sur l'écran Pomodoro ou Study Timer, appuyez sur **Lier la tâche** et choisissez une tâche. Ou depuis **Tâches**, appuyez longuement sur une tâche → **Concentrez-vous avec Pomodoro** ou **Concentrez-vous avec Study Timer**. Les sessions terminées stockent le titre de la tâche pour la **répartition par tâche** dans les statistiques. 

### Comment puis-je épingler ou réorganiser des tâches ? 

Dans l'onglet **Tâches**, faites glisser une ligne vers **Épingler** ou utilisez le menu de tri dans la barre de navigation. Passez en mode de réorganisation pour **faire glisser** les tâches : le tri passe automatiquement à l'ordre personnalisé. Les tâches épinglées apparaissent dans leur propre section en haut. 

### Comment fonctionne la synchronisation des tâches iCloud ? 

Onglet Tâches → équipement → basculer **Synchroniser les tâches avec iCloud**. Les tâches sont fusionnées selon l'heure de la dernière modification sur vos appareils Apple ID. Les minuteries Pomodoro / étude restent locales. **Les statistiques d'étude** peuvent éventuellement être synchronisées séparément (Statistiques → équipement). Vous devez être connecté à iCloud dans les paramètres iOS. La synchronisation s'exécute également lorsque vous revenez à l'application.

### Que comprend l'image de partage du tableau de bord des statistiques ?

Appuyez sur **Partager** dans la barre d'outils de l'onglet Statistiques. La grande carte reflète vos filtres **périmètre et période actuels** — héros du jour, progression des objectifs, carte de chaleur, graphiques par jour de la semaine/heure, répartition des tâches, barres de tendance et sessions récentes — ainsi que la marque et un code QR de l'App Store. Les couleurs correspondent à votre **thème de la page de l'onglet Statistiques**.

### Puis-je personnaliser le thème de l'onglet Statistiques ?

Oui. **Onglet Statistiques → engrenage → Thème** — mêmes contrôles de barre de titre et de dégradé de fond que Pomodoro, Minuteur d'étude et Tâches. La valeur par défaut est rouge focus (`#E53935` / `#EF9A9A`). La teinte de l'onglet Statistiques, la barre de navigation et les **cartes de partage des statistiques** suivent toutes ces couleurs de thème de la page.

### Comment fonctionnent les réalisations ?

Neuf badges locaux se débloquent à mesure que vous franchissez des étapes : premier pomodoro, séquences, total de pomodoros, heures de concentration, réalisation d'objectifs quotidiens, et plus encore. Lorsque vous déverrouillez un nouveau badge, une **célébration en plein écran** apparaît dans l'onglet Statistiques (appuyez sur **Continuer** pour ignorer). Ouvrez **Statistiques → Équipement → Réalisations** pour parcourir la grille. **Appuyez sur un badge** pour obtenir une fiche détaillée ; partagez la **liste complète** depuis la barre d'outils des réalisations ou un **badge unique** depuis l'écran de détail. Les badges sont stockés sur l'appareil ; avec la synchronisation iCloud activée, l'état de déverrouillage et de célébration fusionne sur vos appareils via CloudKit - non téléchargé sur nos serveurs. 

### Comment puis-je parcourir les mois passés sur la carte thermique de focus ? 

Sur le tableau de bord Statistiques, utilisez les flèches **Mois précédent/Mois suivant** sur la carte thermique, appuyez sur le **titre du mois** pour ouvrir une feuille **sélecteur d'année + mois**, ou appuyez sur **Ce mois** pour revenir au mois en cours. 

### Pourquoi les dates futures sur la carte thermique sont-elles différentes ? 

Les jours après aujourd'hui dans le mois en cours apparaissent sous la forme de **espaces réservés à contour en pointillés** avec un remplissage plus clair : ils ne sont pas comptés comme jours de concentration. Les jours passés et aujourd’hui utilisent les couleurs d’intensité normale. 

### Comment ajouter le widget Statistiques du jour ?

Appuyez longuement sur l'écran d'accueil → **+** → recherchez **iPomodoro** → ajoutez **Statistiques du jour** (Petit, **Moyen, Grand** ou Écran de verrouillage rectangulaire/en ligne). Il montre la concentration d'aujourd'hui, la progression des objectifs Pomodoro et **hebdomadaires** et la séquence. 

### Comment ajouter le widget de tâches ? 

Appuyez longuement sur l'écran d'accueil → **+** → recherchez **iPomodoro** → ajoutez **Tâches de compte à rebours** (Petite/Moyenne/Grande). Il affiche les tâches épinglées à venir et les jours restants. Ouvrez l'application après avoir modifié les tâches pour une actualisation plus rapide. 

### Puis-je actualiser le devis du widget de motivation ? 

Sur **iOS 17+**, appuyez sur le bouton **Actualiser** du widget Motivation quotidienne pour choisir instantanément une autre citation sans ouvrir l'application. 

### Pourquoi les notifications ne fonctionnent-elles pas ? 

Vérifiez **Onglet Paramètres → Notifications** pour connaître votre statut d'autorisation iOS actuel. Les rappels de minuterie et de tâches nécessitent un accès aux notifications. Ouvrez les paramètres système si l'autorisation a été refusée. 

### Comment personnaliser les durées de travail et de pause ? 

Appuyez sur l'**icône d'engrenage** sur l'onglet Pomodoro → ajustez les lignes pas à pas, ou **appuyez sur les grands chiffres de la minuterie** sur l'écran principal pour ouvrir un sélecteur de durée. Un intervalle de pause long (tous les N pomodoros) est également configurable. 

### Qu'est-ce que l'achèvement de la phase de confirmation ?

**Onglet Pomodoro → roue dentée → Confirmer la fin de la phase**. Lorsque **activé**, iPomodoro affiche une boîte de dialogue après chaque segment de travail ou de pause avant de commencer la phase suivante. Lorsque **désactivé** (par défaut), la phase suivante démarre automatiquement après l'alarme de fin — flux Pomodoro classique sans intervention.

### Comment fonctionnent Live Activity et Dynamic Island ?

Activez **Live Activity** séparément dans les paramètres de Pomodoro et de Study Timer (icône de roue dentée). Chaque mode possède son **propre** compte à rebours sur l’écran verrouillé et dans Dynamic Island — ils ne s’écrasent jamais mutuellement. Pendant qu’une session est en cours, vous voyez un compte à rebours en direct ; lorsqu’elle se termine, une brève célébration apparaît pendant 10 secondes. Si iOS ferme l’application alors que votre minuteur est encore visible sur l’écran verrouillé, la réouverture de iPomodoro **restaure** la session et passe à l’onglet actif — **sauf** si vous l’avez lancée via une **Action rapide de l’écran d’accueil**, qui prévaut.

### Comment ajouter des widgets ?

Appuyez longuement sur l’écran d’accueil → **+** → recherchez **iPomodoro** (ou 爱番茄 / 愛番茄). Choisissez **iPomodoro · Pomodoro** ou **iPomodoro · Study Timer** pour les comptes à rebours du minuteur (ce sont des widgets séparés), **Today's Stats** pour le suivi de votre concentration quotidienne, **Countdown Tasks** pour les échéances ou **Daily Motivational Quote** pour la citation quotidienne. Pour une aide étape par étape, ouvrez **Réglages → Widgets → Comment utiliser**.

### Pourquoi mon widget de minuteur ne se met-il pas à jour ?

Pomodoro et Study Timer sont des **widgets séparés**. Démarrez ou mettez en pause une session dans l’**onglet correspondant** et assurez-vous d’avoir ajouté le bon widget. iOS peut retarder les actualisations pour économiser la batterie — ouvrez l’application une fois pour synchroniser plus rapidement.

### Où est passé l’ancien widget de minuteur ?

Les minuteurs sont maintenant **iPomodoro · Pomodoro** et **iPomodoro · Study Timer**. Supprimez tout ancien widget de minuteur et ajoutez les nouveaux depuis la galerie de widgets.

### Comment fonctionne la citation motivationnelle quotidienne ?

Un devis est sélectionné de manière déterministe chaque jour à l'aide de `(year × 400 + dayOfYear) % total`. Filtrez la langue des citations sous **Paramètres → Paramètres des citations de motivation → Langues des citations de motivation** (Toutes / Simplifiées / Traditionnelles / Anglais). La même citation apparaît dans le widget Motivation et l'indice d'activité en direct jusqu'à minuit. Parcourez des citations aléatoires dans **Paramètres → Paramètres des citations de motivation → Anthologie des citations de motivation** (en plein écran, une à la fois). 

### Les arrière-plans des widgets peuvent-ils suivre mon thème ? 

Oui. **Paramètres → Widgets → L'arrière-plan du widget suit le thème** reflète votre dégradé d'accent global sur les widgets d'accueil et d'écran de verrouillage. Désactivez-le pour obtenir un arrière-plan blanc pur (clair) ou sombre tout en conservant les couleurs d'accent sur les titres. 

### Comment fonctionnent les rappels de tâches à échéance ? 

Lors de la création ou de la modification d'une tâche, activez **Rappel de date d'échéance** et définissez une date/heure cible future. Une notification locale se déclenche à ce moment précis. Gérez les rappels en attente sous **onglet Tâches → équipement → Rappels de tâches dues** — appuyez sur une ligne pour modifier ou **supprimer** la tâche du bas de la feuille de modification. Le glisser pour supprimer sur la liste des tâches fonctionne toujours également. 

### Comment supprimer une tâche en cours d'édition ?

Ouvrez une tâche dans la liste ou dans **Rappels de tâches dues**, puis faites défiler vers le bas de la feuille de modification et appuyez sur **Supprimer**. Confirmez dans l'alerte. Les nouvelles tâches (créer un flux) n'affichent pas de bouton de suppression. 

### Pourquoi ne puis-je pas activer un rappel pour une date passée ? 

Si la date/heure cible est déjà passée, la bascule de rappel est masquée et tout rappel existant est automatiquement désactivé — il n'y a plus rien d'important à planifier. 

### Puis-je utiliser une langue différente de celle de mon système ? 

Oui. Accédez à **onglet Paramètres → Langue** et choisissez Anglais, Chinois simplifié ou Chinois traditionnel. Le nom de l'application sur votre écran d'accueil suit la langue du système ; L'interface utilisateur intégrée à l'application suit votre choix dans l'application. 

### L'application collecte-t-elle mes données ? 

Pas d'analyse, pas de suivi. Les minuteries et les statistiques d'étude restent sur votre appareil par défaut. Les tâches et les sessions d'étude se synchronisent sur **votre iCloud** uniquement si vous activez les bascules séparées. Nous ne recevons pas vos données de tâches ou de minuterie sur nos serveurs. Consultez notre [Politique de confidentialité](../privacy) pour plus de détails. 

### macOS sera-t-il pris en charge ? 

Le support de macOS est prévu. Le projet Xcode inclut déjà la configuration du SDK macOS ; restez à l'écoute des mises à jour sur l'App Store. 

### Vous avez encore besoin d'aide ?

Contactez-nous à [AppleOSer@gmail.com](mailto:AppleOSer@gmail.com). Nous répondons généralement dans les 48 heures.

&lt;/section&gt;
