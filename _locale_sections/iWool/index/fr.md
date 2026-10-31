iWool est un tracker local axé sur la confidentialité, conçu pour capturer des transactions, suivre des activités et compter les revenus sur **iPhone et iPad**. **`iwool://` liens profonds** ouvrent l'accueil, le calendrier, les statistiques, les paramètres, les actions dans l'application (nouvelle activité, compte à rebours rapide, scanner, rappels) ou une activité spécifique — à partir de widgets, de raccourcis ou d'actions rapides sur l'écran d'accueil. **Pas d'inscription, pas de téléchargement : vos données restent sur l'appareil.**

Consultez la [**`iwool://` référence du schéma d'URL**](url-scheme) pour tous les chemins et alias pris en charge.

## Commencer

1. Appuyez sur **++** sur l'écran d'accueil pour créer votre première activité.
2. Remplissez le titre, la plateforme, l'heure de début et de fin. Ajoutez des rappels si nécessaire.
3. Appuyez sur **Enregistrer**. L'activité apparaît dans votre liste, regroupée par statut.
4. Lorsque l'accord porte ses fruits, appuyez sur la page de détails et appuyez sur **Enregistrer les revenus**.
5. Consultez les **Statistiques** à tout moment pour voir vos totaux, vos tendances et le classement de votre plateforme.
6. Ajoutez un widget Écran d'accueil ou Écran de verrouillage pour ne jamais avoir à ouvrir l'application pour rester à jour.

## Caractéristiques

### Écran d'accueil

- **Sept cartes récapitulatives d'état** : Actif, À venir, Tous, Expiré, Terminé, Annulé, En pause. Appuyez sur n'importe quelle carte pour filtrer instantanément ; appuyez à nouveau pour revenir à Aujourd'hui.
- **Suspendez ou annulez avec une date d'entrée en vigueur** : masquez-vous du jour/du calendrier et arrêtez les rappels tout en conservant l'historique des revenus.
- **Exportation de partage d'activité** : exportez un pack de partage que vos amis peuvent importer pour suivre (séparé de la sauvegarde complète).
- **Recherche en texte intégral** : recherchez dans le titre, les notes, la plate-forme, les exigences et les règles.
- **Actions en appuyant longuement** : marquer comme terminé, mettre en pause/reprendre, annuler/restaurer, archiver, dupliquer comme nouveau ou supprimer.
- Les activités récurrentes affichent toujours **l'événement du jour**, de sorte que le statut et l'heure correspondent à votre emploi du temps réel.

### Calendrier

- Basculez entre la **vue mensuelle** et la **chronologie hebdomadaire** : votre préférence est mémorisée.
- Appuyez sur n'importe quelle date pour voir les activités de cette journée. Les couleurs des points et de la barre de gauche suivent la couleur de la plateforme.
- Appuyez longuement sur n'importe quelle ligne de la liste pour les mêmes actions rapides que sur l'écran d'accueil.
- Tirez pour actualiser à tout moment.

### Détail de l'activité

- **Démarre dans le compte à rebours** — affiche le temps jusqu'à l'occurrence actuelle ou suivante ; s'illumine en orange en moins de 24 heures.
- **Date de la prochaine occurrence** affichée pour les activités récurrentes ; "pas de prochaine occurrence" à la fin de la série.
- L'URL de l'activité, les exigences, les règles et les notes rendent tous les liens. **Un simple clic** s'ouvre dans Safari (http/https) ou dans l'application associée ; **Appuyez longuement** pour afficher le menu de liens iOS natif, notamment « Ouvrir dans [Application] », « Ouvrir dans Safari », « Copier le lien » et « Partager ».

### Des gains records

- Formulaire demi-feuille avec montant, note facultative et **date d'enregistrement**.
- Plusieurs entrées par activité, chacune modifiable ou supprimable indépendamment.
- Les revenus n'apparaissent dans les statistiques que lorsqu'ils sont enregistrés ici ; les revenus estimés sont uniquement à titre d'affichage.

### Statistiques

- Totaux pour aujourd'hui, cette semaine, ce mois et cette année.
- **Graphique de tendance mensuelle** — appuyez sur n'importe quelle barre (si le montant > 0) pour voir chaque entrée de revenus au cours de cette période.
- **Classement des plateformes** — sélecteur de durée indépendant (année/mois/semaine) ; appuyez sur une ligne de plate-forme pour accéder aux détails par entrée.
- **Aperçu de l'activité** : appuyez sur une ligne d'état ou sur la ligne du total pour voir la liste des activités correspondantes.
- La politique de revenus d’activité récurrents (stricte ou indulgente) est configurable dans Paramètres.

### Rappels

- Plusieurs rappels par activité : au début, avant le début, avant la date limite ou à une heure fixe quotidienne.
- Notifications locales du système. Les plannings de rappel sont rangés à chaque fois que vous ouvrez l'application.
- Les activités annulées arrêtent de sonner automatiquement.
- Les lignes de la liste d'accueil et de calendrier affichent un **petit glyphe de rappel** afin que vous puissiez voir ce qui est programmé en un coup d'œil.

### Partager des cartes d'images

Partagez une **activité** ou votre **tableau de bord de statistiques** sous la forme d'une **carte image PNG de marque** via la feuille de partage du système : arrière-plan dégradé, code QR de l'App Store et filigrane facultatif. Indiquez si les revenus apparaissent sur les cartes partagées dans Paramètres (**désactivé par défaut**). Les images sont rendues sur l'appareil ; rien n'est téléchargé. Enregistrer dans Photos peut demander l’accès à la photothèque.

### Actions rapides sur l’écran d’accueil

Appuyez longuement sur l'icône iWool sur iOS pour lancer jusqu'à **4** raccourcis. Choisissez parmi **9** préréglages dans **Paramètres → Outils → Raccourcis de l'écran d'accueil** :

Accueil · Calendrier · Statistiques · **Compte à rebours rapide** · Nouvelle activité · Rappels programmés · Scanner · Évaluer l'application · Commentaires

Par défaut : **Accueil, Calendrier, Statistiques, Compte à rebours rapide**. Chaque action utilise une URL `iwool://` (même routeur que les widgets et les raccourcis).

### Île dynamique et activités en direct

Deux types d'activité en direct sur les modèles d'iPhone pris en charge :

**1. Compte à rebours des événements** (iOS 16.1+)

- Lié aux activités de laine : activez dans **Paramètres → Notifications → Activité en direct**.
- Réglez le **délai de livraison** (1 à 480 minutes avant le début). Plusieurs activités dans la fenêtre peuvent chacune afficher une île ou effectuer une rotation.
- Appuyez longuement sur une activité éligible dans Accueil ou Calendrier → **Ajouter à Dynamic Island**.

**2. Compte à rebours rapide** (iOS 16.2+)

- Compte à rebours **autonome** sur l'île/l'écran de verrouillage — **non enregistré** dans votre base de données d'activités.
- Créez à partir de **Paramètres → Rappel d'île** ou `iwool://island` / Action rapide sur l'écran d'accueil.
- Durée **1 seconde à 8 heures** — puces prédéfinies (30 s, 1 à 480 min) ou choisissez une date limite ; Affichage facultatif du titre, de la note, de la couleur d’accentuation et des secondes.
- Se termine automatiquement lorsque le temps est écoulé ; idéal pour les ventes flash, les fenêtres de connexion ou les minuteries ad hoc.

### Widgets de l’écran d’accueil et de l’écran de verrouillage

**12 familles de widgets** au total (8 styles d'accessoires pour écran d'accueil + 4 styles d'accessoires pour écran de verrouillage) :

| Widget | Descriptif |
|--------|-------------|
| Actif aujourd'hui | Les activités du jour actuellement en cours |
| Aujourd'hui tout | Toutes les activités du jour |
| Aujourd'hui À venir | Les activités d'aujourd'hui non encore commencées |
| Tous les événements | Aperçu de la liste complète, triée par statut |
| Aperçu des statistiques | Actif / À venir / Tous les comptes — Ajouts de grande taille Expirés / Terminés / Annulés |
| Gains | Aujourd'hui, cette semaine, ce mois et cette année |
| Coup d'oeil | Nombre d'activités + gains + nombre actif en un coup d'œil |
| Principales plateformes | Classement des gains de cette année par plateforme |
| Écran de verrouillage (4 styles) | Accessoires circulaires, rectangulaires et en ligne — iOS 16+ |

Sur iOS 17 et versions ultérieures, les widgets de liste prennent en charge **appuyer par ligne** pour ouvrir directement l'activité correspondante.

Un **Guide des widgets** intégré dans Paramètres vous guide pas à pas dans l'ajout de widgets, avec une galerie de widgets et une FAQ.

### Extras du formulaire d’activité

- **Liens d'applications populaires** : remplissez en un seul clic les schémas d'URL courants des applications de paiement, de banque et d'achat.
- **Scannez ou choisissez dans l'album** : scannez un code QR ou choisissez une image pour remplir automatiquement l'URL de l'activité.

### Lecteur de codes QR/codes-barres

Un scanner autonome dans **Paramètres → Outils** :

- Analyse de caméra en temps réel avec prise en charge d'une lampe de poche.
- Faites votre choix dans un album photo avec détection basée sur Vision.
- Liste des résultats avec copie en un clic, Safari intégré à l'application pour les liens http/https et exportation via Share Sheet.

### Apparence et langue

- Plus de 8 couleurs thématiques (Or, Bleu océan, Vert forêt, Rose rose, Lavande, Orange coucher de soleil, Menthe, Rouge cerise…)
- Aspect clair/sombre/système — avec retour haptique sur l'interrupteur.
- **20 icônes d'application alternatives sur l'écran d'accueil.**
- 13 langues d'affichage : anglais, chinois simplifié, chinois traditionnel, japonais, coréen, thaï, hindi, espagnol, français, allemand, portugais brésilien, russe, arabe — commutables indépendamment de la langue du système.
- Plusieurs devises (ISO 4217) ; **places décimales** personnalisables pour les montants généraux (par défaut 2) et les étiquettes de graphique (par défaut 0).
- **Stratégie de badge d'application** configurable (désactivée/compte du jour/total en attente).
- **Plus de recommandations** — lien vers la page App Store du développeur dans Paramètres → À propos.

### Données et confidentialité

- **Exporter la sauvegarde complète** — Fichier CSV avec toutes les activités, rappels, revenus, états de récurrence et modèles.
- **Importer une sauvegarde** : remplacez la bibliothèque entière ou fusionnez uniquement en ajout (conserve les données existantes).
- **Archive en un clic** : archivez toutes les activités non récurrentes terminées/expirées/annulées en même temps.
- Les archives peuvent être restaurées à tout moment à partir des paramètres.
- Partager une activité copie le texte dans le presse-papiers. Une bascule **partage-inclut-gains** (désactivée par défaut) maintient le montant de vos revenus privé.

## Règles de récurrence

| Tapez | Possibilités |
|------|---------|
| Quotidiennement | Tous les N jours |
| Hebdomadaire | Toute combinaison de jours de la semaine |
| Mensuel | Un seul jour, jusqu'à la date de fin ou jusqu'à la fin du mois |
| Annuel | Un seul jour, jusqu'à la date de fin ou jusqu'au 31 décembre |
| Personnalisé | Intervalle personnalisé en jours |

Conditions de fin : une date de fin spécifique ou un nombre maximum d'occurrences.

## Configuration système requise

| Caractéristique | Minimum |
|---------|---------|
| iPhone/iPad | iOS 15.0+ |
| Widgets d'écran de verrouillage | iOS 16.0+ |
| Dynamic Island — compte à rebours de l'événement | iOS 16.1+ (matériel pris en charge) |
| Activité en direct avec compte à rebours rapide | iOS 16.2+ |
| Widget par ligne, appuyez sur | iOS 17.0+ |

## Contactez-nous

Des questions, des commentaires ou besoin d'aide ? Contactez-nous à :

- **Dans l'application :** Paramètres → Envoyer des commentaires
- **E-mail :** [AppleOSer@gmail.com](mailto:AppleOSer@gmail.com)

Nous répondons généralement dans les 48 heures.

[FAQ](faq) · [Schéma d'URL](url-scheme) · [Politique de confidentialité](privacy)
