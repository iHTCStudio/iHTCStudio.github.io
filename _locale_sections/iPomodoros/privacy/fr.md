iHTC Studio (« nous », « notre » ou « notre ») a créé **iPomodoro** (également connu sous le nom de « 爱番茄 » / « 愛番茄 ») en tant qu'application de productivité pour iPhone et iPad. Cette page explique comment nous traitons les informations lorsque vous utilisez l'application. 

## Résumé 

**iPomodoro ne collecte, ne stocke ni ne transmet de données personnelles à nos serveurs.** Les minuteries, les statistiques d'étude, les paramètres et le contenu de motivation fonctionnent sur votre appareil. La **synchronisation iCloud** facultative pour les tâches et/ou les statistiques d'étude utilise Apple CloudKit sous votre identifiant Apple — nous n'exécutons pas ce service cloud. 

## Données que nous ne collectons pas 

- Aucun nom, e-mail, numéro de téléphone ou compte utilisateur (sauf si vous nous envoyez volontairement un e-mail pour obtenir de l'aide). 
- Pas d'analyse d'utilisation, de SDK de rapport d'erreur ou d'identifiant publicitaire. 
- Aucun suivi de localisation. 
- Pas de téléchargement de sessions chronométrées ou de statistiques d'étude sur **nos serveurs** (la synchronisation iCloud facultative stocke les données dans votre compte Apple iCloud). 
- Les listes de tâches ne nous sont **pas** téléchargées : la synchronisation iCloud facultative s'effectue directement entre vos appareils via Apple CloudKit lorsque vous l'activez. 

## Données stockées sur votre appareil 

Les éléments suivants restent **localement** sur votre iPhone ou iPad :

| Données | Stockage | Objectif | 
|------|---------|---------| 
| Paramètres de Pomodoro et de la minuterie d'étude | Paramètres par défaut de l'utilisateur | Durées, sons, thèmes, préférences de notification, facultatif **Confirmer l'achèvement de la phase** (Pomodoro) | 
| Tâches du compte à rebours (titre, date, notes, indicateur de rappel, épingle, ordre, **couleur d'accent**) | Base de données SQLite | Liste des tâches, rappels de date d'échéance, couleurs des widgets | 
| Historique des sessions d'études | Base de données SQLite | Onglet Statistiques (temps de concentration, graphiques, répartition des tâches) | 
| Préférences d'affichage des statistiques | Paramètres par défaut de l'utilisateur | Filtres par défaut, **plage de dates personnalisée**, règles de comptage, couleurs du thème de l'onglet Statistiques | 
| Objectifs de concentration et préférences de réalisation | Paramètres par défaut de l'utilisateur | Objectifs quotidiens/hebdomadaires, badges débloqués | 
| Préférences de raccourci de l'écran d'accueil | Paramètres par défaut de l'utilisateur | Quelles actions rapides apparaissent lorsque vous appuyez longuement sur l'icône de l'application (jusqu'à 4) | 
| Le rappel du mode de mise au point bascule | Paramètres par défaut de l'utilisateur | Invite facultative lors du démarrage d'une minuterie sans Focus activé | 
| Calendrier de notification de motivation quotidienne | Paramètres par défaut de l'utilisateur | Heure de notification locale répétitive facultative | 
| Aperçu de la progression des statistiques d'aujourd'hui | Paramètres par défaut du groupe d'applications | Widget de statistiques du jour | 
| Corpus de citations de motivation (dialogue/quotidien + notification) | Offre groupée d'applications JSON | Pools de devis sur l'appareil (**1 000+** dialogue/quotidien combiné) ; le pool de notifications est séparé | 
| Préférences de thème et de langue | Paramètres par défaut de l'utilisateur | Apparition et localisation | 
| Index des citations de motivation quotidiennes | Paramètres par défaut du groupe d'applications | Widget de motivation et synchronisation des conseils d'activité en direct | 
| Filtre de langue de citation de motivation | Paramètres par défaut du groupe d'applications | Le pool de devis du widget correspond aux paramètres de l'application | 
| Miroir de thème global pour les widgets | Paramètres par défaut du groupe d'applications | Couleurs d’accent du widget et arrière-plan dégradé en option | 
| Instantané de la minuterie Pomodoro | Conteneur partagé du groupe d'applications | Widget Pomodoro et activité en direct | 
| Instantané de la minuterie d'étude | Conteneur partagé du groupe d'applications | Widget Minuterie d'étude et activité en direct | 
| Instantané du widget Tâches | Conteneur partagé du groupe d'applications | Widget Tâches de compte à rebours |

Ces données ne nous sont pas accessibles. La désinstallation de l'application supprime le stockage local (à l'exception des sauvegardes du système iOS que vous avez peut-être activées). 

## Synchronisation iCloud facultative (tâches et statistiques d'étude) 

**Tâches :** Si vous activez **Synchroniser les tâches avec iCloud**, les tâches de compte à rebours se synchronisent via CloudKit (`iCloud.com.iHTCboy.iPomodoros`). 

**Statistiques d'étude :** Si vous activez **Synchroniser les statistiques d'étude avec iCloud** (paramètres de statistiques), les enregistrements de session de focus sont synchronisés en tant qu'enregistrements CloudKit de type `StudySession` — y compris le titre/l'identifiant de la tâche liée en option et un `cloudId` pour la fusion. **Paramètres d'objectifs quotidiens** (`StatsGoals`) et **état de déverrouillage/célébration des succès** (`StatsAchievements`) se synchronisent sous la même bascule. La synchronisation utilise des jetons de modification CloudKit incrémentiels après la première extraction complète. Ceci est **indépendant** de la synchronisation des tâches. 

Dans les deux cas, les données restent dans **votre compte iCloud privé** via l'infrastructure d'Apple, et non dans les serveurs iHTC Studio. Désactivez l’une ou l’autre bascule à tout moment ; des copies locales restent sur chaque appareil. 

## Notifications 

Si vous accordez l'autorisation de notification, iPomodoro planifie des **notifications locales** sur votre appareil pour :

- Rappels d'achèvement du minuteur et d'étude de fond (lorsqu'ils sont activés dans les paramètres) — le texte du message est choisi parmi un pool de devis de notification groupé sur l'appareil ; pas de récupération réseau 
- **Notification de motivation quotidienne** (facultatif, Paramètres) — notification locale répétée à l'heure choisie 
- Rappels de date d'échéance des tâches (lorsqu'ils sont activés par tâche) 

Ces notifications sont créées et envoyées par iOS sur l'appareil. Nous n'exploitons pas de serveur de notification push et ne téléchargeons pas de texte de devis depuis nos serveurs. 

## Groupe d'applications (Widgets et activité en direct) 

L'application principale et l'extension de widget partagent un minimum de minuterie, de motivation, de thème, de **tâches** et de **progression des statistiques du jour** via le groupe d'applications d'Apple (`group.com.iHTCboy.iPomodoros`). Pomodoro et Study Timer utilisent des clés d'instantané **séparées** sur l'appareil afin que les deux widgets puissent coexister. Ce conteneur reste sur votre appareil et est utilisé uniquement pour afficher les widgets et l'activité en direct, et non pour l'accès de tiers. 

## Achat intégré 

Un achat facultatif de support intégré à l'application est entièrement traité par **Apple StoreKit**. Nous recevons uniquement des reçus d’achat standard sur l’App Store via Apple ; nous ne collectons pas directement les détails de paiement. 

## Services tiers

iPomodoro n'intègre **pas** de SDK d'analyse, de publicité ou de connexion sociale de tiers.

Lorsque vous appuyez sur **Retour d'information**, l'application peut ouvrir votre client de messagerie avec un modèle pré-rempli incluant le modèle de l'appareil et la version de l'application — vous choisissez si vous l'envoyez ou non.

## Vie privée des enfants

Nous ne collectons pas sciemment d'informations personnelles auprès des enfants. Parce que nous ne collectons pas de données personnelles via l'application, aucune disposition spéciale pour les enfants au-delà des classifications d'âge standard de l'App Store ne s'applique.

## Modifications de cette politique

Nous pouvons mettre à jour cette Politique de confidentialité de temps à autre. Les modifications seront publiées sur cette page.

## Contactez-nous

Des questions sur la confidentialité ?

- **Email:** [AppleOSer@gmail.com](mailto:AppleOSer@gmail.com)
