### iLinux nécessite-t-il un compte ou une connexion Internet ?

Non, iLinux fonctionne entièrement hors ligne pour les bibliothèques de commandes. Toutes les données de commande (résumés JSON et documentation Markdown) sont regroupées dans l'application. Aucune inscription n'est nécessaire pour parcourir, lire la documentation ou répondre à des quiz. La **synchronisation iCloud** facultative utilise votre identifiant Apple pour aligner les favoris et la progression sur tous les appareils — elle ne télécharge pas le contenu des commandes.

### Does iLinux support Mac?

Oui. iLinux est une **application macOS native** (macOS **13.0+**, pas Mac Catalyst) avec une **disposition de bureau en barre latérale**, une fenêtre redimensionnable et des raccourcis clavier étendus (**⌘,**, **⌘[**, **Esc**, **⌘←/→**, touches de quiz **1–4** / **⌘R** / **Return**). Toutes les fonctionnalités principales (trois bibliothèques shell, équivalents, quiz, liens profonds et thèmes) fonctionnent sur Mac.

**Pas sur Mac :** Les widgets de l'écran d'accueil, les actions rapides de l'écran d'accueil et les icônes d'applications alternatives sont **iPhone/iPad uniquement**. Configurer les widgets sur iOS ; Mac affiche une notification dans l'application.

### Comment fonctionne la synchronisation iCloud ?

Une fois connecté à **iCloud** avec le même identifiant Apple, activez **iCloud Sync** dans **Paramètres → Statistiques d'apprentissage**. iLinux synchronise les **favoris**, la **progression du quiz**, le **thème** et les **préférences d'affichage** (langue, plate-forme shell, portée des favoris, liste/grille) sur **iPhone, iPad et Mac** via le stockage de valeurs-clés iCloud. Les conflits fusionnent automatiquement (par exemple union des favoris). Vous pouvez **désactiver la synchronisation sur un appareil** sans affecter les autres. Les bibliothèques de commandes restent entièrement hors ligne ; seule votre progression personnelle est synchronisée.

### iLinux exécute-t-il des commandes sur un vrai terminal Linux ?

Non. iLinux est un **outil de référence et d'apprentissage uniquement**. Il ne fournit pas de shell, de client SSH ou d'environnement d'exécution à distance. Les commandes sont documentées pour étude : vous les pratiquez sur votre propre machine Linux, PC Windows, serveur ou instance cloud.

### Quelles plates-formes shell iLinux prend-il en charge ?

iLinux propose trois bibliothèques de commandes hors ligne par langue de contenu :

- **Linux** — 1 050 commandes réparties en 14 catégories
- **Windows CMD / Batch** — 300 commandes réparties en 10 catégories
- **PowerShell** — 300 commandes réparties en 10 catégories

**Plus de 1 650 commandes au total** par langue (anglais, chinois simplifié, chinois traditionnel). Changez de bibliothèque à partir du menu Shell de la barre d'outils sur **Commandes**, **Catégories** ou **Daily Quiz**.

### Comment basculer entre Linux, CMD et PowerShell ?

Appuyez sur le menu **Plateforme Shell** (icône de terminal) dans la barre d'outils sous l'onglet Commandes, Catégories ou Quiz quotidien. Votre sélection persiste et couvre la recherche, les catégories, les questions de quiz et les statistiques d'apprentissage pour cette plate-forme.

Dans **Paramètres → Accès rapide à l'accueil**, vous pouvez également définir une plate-forme shell par défaut, une **portée des favoris** (toutes les plates-formes par rapport à la plate-forme actuelle uniquement) et la **bibliothèque de commandes de widget** pour les widgets Daily Command et Category Spotlight.

### Que sont les commandes équivalentes multiplateformes ?

**Plus de 100 groupes équivalents** lient des commandes qui accomplissent la même tâche sur Linux, CMD et PowerShell — par exemple `ls`, `dir` et `Get-ChildItem`. Sur une page de détails de commande, la barre **Équivalents** affiche les entrées associées ; appuyez sur un pour accéder instantanément à la documentation de cette plate-forme.

### Combien de commandes sont incluses ?

Chaque langage de contenu comprend **1 650+** commandes réparties dans trois bibliothèques shell :

| Plateforme | Commandes | Catégories |
|----------|----------|------------|
| Linux | 1050 | 14 |
| CMD / Batch | 300 | 10 |
| PowerShell | 300 | 10 |

Toute la documentation est disponible hors ligne en anglais, chinois simplifié et chinois traditionnel.

### Comment rechercher une commande ?

Appuyez sur l'icône en forme de loupe dans l'onglet Commandes ou appuyez sur **⌘F** sur un clavier matériel. Tapez un nom de commande, un mot-clé ou une partie d'une description. Les résultats sont mis à jour en temps réel au fur et à mesure que vous tapez.

### Comment puis-je basculer entre la vue liste et la vue grille ?

Dans l'onglet **Commandes** ou **Catégories**, ouvrez le menu de filtrage de la barre d'outils (icône en forme d'entonnoir). Sous **Mode d'affichage**, choisissez **Liste** ou **Grille**. En mode grille, utilisez les boutons **+ / −** pour définir les colonnes par ligne (**1 à 6 sur iPhone**, **1 à 8 sur iPad et Mac**). Vous pouvez également modifier la valeur par défaut dans **Paramètres → Affichage**.

### Comment puis-je suivre mes progrès d’apprentissage ?

Ouvrez la page de détails d'une commande et définissez son état sur **Non appris**, **Appris** ou **Maîtrisé**. En mode liste, faites glisser une ligne pour afficher un état rapide et des actions favorites. En mode grille, utilisez le bouton étoile pour favoris et le menu contextuel pour l'état. Filtrez sur **Non appris** dans le menu de la barre d'outils pour vous concentrer sur les commandes que vous n'avez pas encore étudiées.

### Quelles langues sont disponibles ?

iLinux prend en charge trois langues pour l'interface de l'application et la documentation des commandes :

- **English**
- **Chinois simplifié (简体中文)**
- **Chinois traditionnel (繁體中文)**

Vous pouvez également choisir **Système** pour suivre les paramètres régionaux de votre appareil. Changez la langue dans **Paramètres → Langue**. L'ensemble de l'application, y compris les widgets, est mis à jour immédiatement.

### Comment fonctionne le Quiz Quotidien ?

Chaque jour, un nouvel ensemble de questions de quiz est généré à l'aide d'une graine basée sur la date, **portée sur la plate-forme shell active** (Linux, CMD ou PowerShell). Toute personne utilisant iLinux le même jour reçoit le même jeu de quiz de base pour cette plate-forme. Deux types de questions apparaissent :

- **Résumé du match** : vous voyez une brève description et devez choisir le nom de commande correct.
- **Match Option Meaning** — you see a flag's description (e.g. `-r: recursive`) and must identify which command it belongs to.

Appuyez sur le **bouton d'actualisation** (flèche circulaire) dans la barre d'outils pour obtenir un ensemble aléatoire différent à tout moment. Les jours **de séquence parfaite** (jours consécutifs avec un score parfait) sont suivis par plateforme et affichés dans l'écran du quiz et le widget Quiz Glance. Les indicateurs d'aide génériques comme `-h` et `--version` sont exclus pour garder les questions sans ambiguïté.

### Mes mauvaises réponses ne sont pas enregistrées. Que dois-je faire?

Les mauvaises réponses sont automatiquement enregistrées une fois que vous avez terminé une session de quiz. Assurez-vous de terminer le tour de quiz complet (répondez à toutes les questions et accédez à l'écran des résultats). Les sessions partiellement terminées ne sont pas enregistrées.

Vous pouvez consulter toutes les mauvaises réponses enregistrées dans **Paramètres → Carnet de mauvaises réponses**.

### Comment ajouter une commande aux Favoris ?

Ouvrez la page de détails de n'importe quelle commande et appuyez sur l'**icône étoile** dans le coin supérieur droit. En **vue grille**, appuyez directement sur l'étoile sur la cellule de commande. Accédez à tous les favoris depuis **Paramètres → Favoris** ou le filtre rapide **Favoris**.

### Comment configurer les widgets de l'écran d'accueil ?

1. Appuyez longuement sur une zone vide de votre écran d'accueil et appuyez sur le bouton **+** dans le coin supérieur.
2. Recherchez **iLinux** dans la galerie de widgets.
3. Choisissez un style de widget et appuyez sur **Ajouter un widget**.

Un **Guide des widgets** étape par étape est également disponible dans **Paramètres → Guide des widgets**. Pour que les arrière-plans des widgets suivent le dégradé du thème de votre application, activez l'option dans **Paramètres → Widgets**.

**Bibliothèque de commandes de widget :** Dans **Paramètres → Widgets**, choisissez quelle bibliothèque shell (Linux / CMD / PowerShell) alimente les widgets Daily Command et Category Spotlight. Ceci est indépendant du commutateur shell intégré à l'application - utile si vous souhaitez que les widgets affichent les commandes Windows lors de la navigation sur Linux dans l'application.

### Le widget Daily Command affiche la même commande chaque jour. Comment puis-je le changer ?

Appuyez sur le **bouton flèche circulaire (lecture aléatoire)** dans le coin supérieur droit du widget Commande quotidienne pour charger immédiatement une commande différente. Cette fonctionnalité nécessite **iOS 17 ou version ultérieure**.

Sur iOS 16, le widget Daily Command affiche une commande fixe pour chaque jour et n'inclut pas le bouton de lecture aléatoire.

### Comment configurer les actions rapides de l'écran d'accueil ?

Appuyez longuement sur l'icône de l'application iLinux pour voir jusqu'à **4** actions rapides. Choisissez les actions à afficher dans **Paramètres → Raccourcis de l'écran d'accueil**. Sept options sont disponibles : **Rechercher**, **Quiz quotidien**, **Favoris**, **Cahier de mauvaises réponses**, **Catégories**, **Envoyer des commentaires** et **Évaluer l'application**. Vous pouvez réorganiser et réinitialiser les paramètres par défaut à partir du même écran.

### Comment utiliser iLinux avec l'application Raccourcis ?

iLinux prend en charge le schéma d'URL `ilinux://`. Utilisez une action **Ouvrir les URL** dans l'application Raccourcis. Exemples :

- `ilinux://command?name=grep` — ouvre la commande Linux `grep` (`cmd=` fonctionne aussi)
- `ilinux://command?cmd=dir&platform=cmd` — ouvre la commande CMD `dir`
- `ilinux://command?cmd=Get-ChildItem&platform=powershell` — ouvre la commande PowerShell
- `ilinux://quiz` — ouvre l'onglet Quiz quotidien
- `ilinux://favorites` — ouvre votre liste de favoris
- `ilinux://wrong` ou `ilinux://mistakes` — ouvre le livre des mauvaises réponses

**Paramètre de plate-forme :** `platform=linux` (par défaut), `cmd` (alias : `batch`, `bat`) ou `powershell` (alias : `ps`, `pwsh`). Omettre pour les commandes Linux.

Note: **Search** and **Categories** are available as Home Screen quick actions but are not registered as universal deep-link hosts. See the full [URL Scheme Reference](../url-scheme).

### Comment partager une commande ?

Sur n'importe quelle page de détails de commande, appuyez sur **Partager** dans la barre d'outils. Vous pouvez exporter la commande sous forme de **fichier Markdown** ou générer une **carte de partage PNG stylisée** (avec le code QR de l'App Store) à envoyer via la feuille de partage du système. L'enregistrement d'images dans Photos peut nécessiter l'accès à la photothèque.

### Comment changer la couleur du thème ?

Accédez à **Paramètres → Thème**. Faites défiler les 15 préréglages de couleurs intégrés ou appuyez sur la ligne **Couleur personnalisée** pour sélectionner n'importe quelle couleur à l'aide du sélecteur de couleurs du système. La couleur d'accent, les dégradés et le widget reflètent tous les mises à jour immédiatement.

### Puis-je changer l’icône de l’application ?

Oui. Accédez à **Paramètres → Icône de l'application** pour choisir parmi **6 icônes** (par défaut plus 5 alternatives). Le paramètre est appliqué instantanément sans relancer l'application.

### La couleur du widget ne correspond pas à mon thème. Comment puis-je le réparer ?

Les widgets synchronisent la couleur de leur thème via un groupe d'applications partagé entre l'application principale et l'extension du widget. Si le widget semble obsolète :

1. Ouvrez iLinux une fois : cela force l'actualisation des données du groupe d'applications.
2. Si le widget ne se met toujours pas à jour, appuyez longuement sur le widget et appuyez sur **Modifier le widget** (ou supprimez-le et rajoutez-le) pour déclencher un rechargement de la chronologie.

Assurez-vous que l'extension **iLinux Widget** et l'application principale sont toutes deux à jour (même version).

### iLinux prend-il en charge l'iPad ?

Oui. iLinux fonctionne nativement sur iPad avec des mises en page adaptatives. Le mode Grille prend en charge jusqu'à **8 colonnes**. Les widgets, les icônes alternatives, les raccourcis de l'écran d'accueil et les haptiques sont entièrement pris en charge sur iPad.

### Comment changer la langue sur Mac ?

Le **sélecteur de langue** intégré à l'application se trouve dans **Paramètres → Langue** sur **iPhone et iPad**. Sur **Mac**, les préférences linguistiques arrivent généralement via la **synchronisation iCloud** à partir d'un autre appareil, ou suivent vos préférences enregistrées/paramètres régionaux du système lors du premier lancement. Activez la synchronisation iCloud pour que la langue reste alignée sur tous les appareils.

### Vous avez encore besoin d'aide ?

Contactez-nous à [AppleOSer@gmail.com](mailto:AppleOSer@gmail.com) ou utilisez l'option **Paramètres → Envoyer des commentaires** de l'application. Nous répondons généralement dans les 48 heures.
