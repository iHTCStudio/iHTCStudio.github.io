iLinux prend en charge ** `ilinux://` ** (également écrit ** `iLinux://` **) URL scheme deep links on **iPhone, iPad and Mac** — open command detail (Linux, CMD ou PowerShell), the Daily Quiz, Favorites or the Wrong Answer Book from Safari, another app, a widget tap (iOS/iPad), or Apple Shortcuts.

Les URLs de commande acceptent un paramètre de requête optionnel ** `ilinux://` ** afin que les touches de widget et les raccourcis puissent ouvrir les entrées Windows correctement.

**Écran d'accueil Actions rapides** (long-presse l'icône de l'application sur **iOS/iPad seulement**) couverture Recherche, catégories, rétroaction et taux. Les utilisateurs Mac peuvent utiliser le menu **iLinux** et les raccourcis clavier.

> **Important:** iLinux est une application **de référence et d'apprentissage**. Liens URL seulement **navigate dans l'application**. Ils ne **pas** exécuter des commandes Linux, ouvrir des sessions SSH ou se connecter à des serveurs distants.

## Spécification du protocole


```
ilinux://<host>[/<path>][?query]
iLinux://<host>[/<path>][?query]   ← same scheme, case-insensitive
```


| Rule | Détail |
|------|--------|
| **Scheme** | `ilinux` / `iLinux` — comparaison sensible aux cas |
| **Host routing** | Le routeur principal est l'URL **host**; certains chemins sont également acceptés (voir ci-dessous) |
| **Command detail** | Chemin `command` **ou** `/command` |
| **Command ID** | Query `name=<id>` **ou** `cmd=<id>` – doit correspondre à une touche de commande groupée (par exemple `ls`, `grep`, `dir`, `Get-ChildItem`) |
| **Platform** | Interroger `platform=<value>` — facultatif; par défaut **Linux** en cas d'omission |
| **Quiz** | Hébergement `quiz` **ou** chemin `/quiz` |
| **Favourites** | Hôtes `favorites` **ou** chemin `/favorites` |
| **Wrong book** | Hôte `mauvais`, `erreurs` ou `questions douteuses`; chemin `/mauvais` ou `/erreurs` également accepté |
| **Wrong record** | Interroger `record=<UUID>` sur une URL du mauvais livre — ouvre le détail de commande de cet enregistrement |
| **Query parameters** | Aucun autre paramètre de pré-remplissement n'est pris en charge |
| **Parser** | `ILinuxDeepLink.parse( :)` — consommé via `onOpenURL` → `AppRouter.pendingDeepLink` |

**Deux canaux de livraison**

| Channel | Handled by | Exemples |
|---------|------------|----------|
| **Universal deep link** (`onOpenURL`) | `ILinuxDeepLink.parse` → `RootTabView` | `commande`, `quiz`, `favorites`, `mauvais` |
| **Home Screen Quick Action** | `ShortcutSceneDelegate` → `ShortcutObserver.dispatch` | `recherche`, `catégories`, `feedback`, `review`, plus chevauchement `quiz` / `favorites` / `wrong` |

Les types d'action rapide utilisent ** `ilinux://` ** correspondant sur la chaîne de type, de sorte que les variantes `iLinux://` et les variantes héritées suivent toujours correctement.

---

## 1. Détail de la commande

Ouvrez la page de détails pour une seule commande groupée.

| Parameter | Required | Désignation des marchandises |
|-----------|----------|-------------|
| `name` | One of `name` / `cmd` | ID de commande (clé dictionnaire dans le paquet JSON plate-forme) |
| `cmd` | One of `name` / `cmd` | Synonyme pour `name` — utilisé par les liens widget |
| `platform` | No | Bibliothèque Shell: voir tableau ci-dessous. Par défaut à **Linux** |

**    C     valeurs** (insensible aux cas):

| Value | Shell library | Autres |
|-------|---------------|---------|
| *(omit)* or `linux` | Linux (1050 commands) | — |
| `cmd` | CMD / Batch (300 commands) | `bat', `bat' |
| `powershell` | PowerShell (300 commands) | `ps`, `pwsh` |

**Comportement**

- Switches vers l'onglet **Commandes**, sélectionne la plateforme **shell** demandée et pousse `CommandeDetailView` pour la commande résolue.
- Si l'ID est **inconnu ou vide**, le lien est **silencieusement ignoré** (interface utilisateur sans erreur).
- Les identifiants de commande sont **sensibles aux cas** et doivent correspondre exactement à la clé JSON groupée (généralement minuscule, par exemple `docker`, pas `Docker`).

**Ouvert `ilinux://` **


```
ilinux://command?name=ls
```


**Ouvrir `ilinux://` (Linux, par défaut)**


```
ilinux://command?cmd=grep
```


**Ouvrir CMD `ilinux://` **


```
ilinux://command?cmd=dir&platform=cmd
```


**Open PowerShell `ilinux://` **


```
ilinux://command?cmd=Get-ChildItem&platform=powershell
```


**Exemple Linux natif-cloud**


```
ilinux://command?name=docker
```


---

## 2. Quiz quotidien

Sautez directement à l'onglet **Quiz quotidien**. Ne **pas** auto-démarrer ou sauter les questions.


```
ilinux://quiz
```


Formulaire de chemin (également accepté):


```
ilinux:///quiz
```


---

## 3. Favoris

Ouvrez la liste **Favourites** sous Paramètres de navigation.


```
ilinux://favorites
```


Formulaire de chemin (également accepté):


```
ilinux:///favorites
```


---

## 4. Livre de mauvaise réponse

### 4.1 Liste

Ouvrez la liste **Wrong Answer Book** sous Paramètres de navigation.


```
ilinux://wrong
```


Aliases (même comportement):


```
ilinux://mistakes
ilinux://wrongquestions
```


### 4.2 Détails de commande d'enregistrement unique →

Lorsque `ilinux://` est un UUID valide d'une entrée de mauvaise réponse enregistrée, l'application ouvre l'onglet **Commandes** et pousse le détail pour la commande de cet enregistrement (si l'enregistrement et la commande existent toujours).

| Parameter | Required | Format |
|-----------|----------|--------|
| `record` | Yes | Chaîne UUID, par exemple `550e8400-e29b-41d4-a716-446655440000` |


```
ilinux://wrong?record=550e8400-e29b-41d4-a716-446655440000
```


Si l'UUID est invalide ou que l'enregistrement a été supprimé, la navigation revient à la mauvaise liste de livres ou est ignorée.

---

## 5. Actions rapides de l'écran d'accueil

Appuyez longuement sur l'icône iLinux → jusqu'à **4** actions. Configurez dans **Paramètres → Raccourcis d'écran d'accueil** (7 options, faites glisser pour réorganiser, réinitialisez aux valeurs par défaut).

| Option | Registered `type` | SF Symbol | Ouvre |
|--------|-------------------|-----------|--------|
| Search | `iLinux://search` | magnifyingglass | **Commandes** onglet + barre de recherche active |
| Daily Quiz | `iLinux://quiz` | checklist | ** Jeu-questionnaire quotidien** |
| Favourites | `iLinux://favorites` | star.fill | ** Liste des favoris** |
| Wrong Answer Book | `iLinux://wrong` | xmark.bin.fill | **Liste des livres de réponses de Wong** |
| Categories | `iLinux://categories` | rectangle.grid.2x2.fill | **Catégories** onglet |
| Send Feedback | `iLinux://feedback` | envelope.fill | Le courrier dans l'application compose (ou `mailto:` fallback) |
| Rate App | `iLinux://review` | star.bubble.fill | Demande de révision de StoreKit |

** Sélection par défaut lors de la première installation :** Recherche · Quiz quotidien · Favoris · Envoyer des commentaires.

** Destinations à action rapide** (non traitées par `ilinux://` / `iLinux://` ):

- "iLinux://search"
- «iLinux://catégories»
- «iLinux://feedback»
- «iLinux://review»

Utilisez ceux-ci via l'icône **long-press** ou en affichant le même type dans le pipeline Quick Action — les ouvrant avec Raccourcis **Ouvrir l'URL** ne peut **pas** fonctionner à moins que l'application ajoute explicitement l'analyse de l'hôte plus tard.

**Type de légataire (toujours acheminé):**

| Type | Comportement |
|------|-----------|
| `iLinux://love` | Ouvre le blog de l'auteur dans l'application Feuille Safari (ancien raccourci statique) |

---

## 6. Liens profonds Widget

Les touches Widget utilisent les mêmes URLs `ilinux://` construites par `iLinux://` :

| Widget | Tap target | URL |
|--------|------------|-----|
| Daily Command | Command detail | `iLinux://command?cmd=<id>&platform=<linux\ | cmd\ | moteur >` |
| Category Spotlight | Sample command | `iLinux://command?cmd=<id>&platform=<platform>` |
| Quiz Glance | Daily Quiz | 'iLinux://quiz' |
| Favourites Glance | Favourites (or per-row command) | `iLinux://favorites` / `iLinux://command?cmd=<id>&platform=<platform>` |
| Wrong Book Glance | Wrong book (or per-row record) | `iLinux://wrong` / `iLinux://wrong?record=<UUID>` |

Les URLs Widget sont construites par `ilinux://` et incluent toujours ** `iLinux://` ** pour les touches de commande. La plate-forme correspond **Paramètres → Widgets → Bibliothèque de commandes Widget** (Linux / CMD / PowerShell).

Le bouton **Daily Command shuffle** (iOS 17+, App Intent) recharge uniquement la timeline du widget — il ne **pas** utiliser une URL.

---

## Raccourcis des pommes

### Ouvrir une commande après avoir copié son nom

1. **Obtenez le texte de l'entrée**
2. **Ouvrir les URL** → `ilinux://` + Texte

Ou Linux code dur :


```
ilinux://command?name=systemctl
```


Ouvrez une commande CMD :


```
ilinux://command?cmd=ipconfig&platform=cmd
```


### Rappel quotidien d'étude → quiz


```
ilinux://quiz
```


Ajouter **Ouvrir les URL** dans une automatisation personnelle (par exemple tous les jours de la semaine à 9h).

### Examiner les mauvaises réponses


```
ilinux://wrong
```


### Ouvrir les favoris à partir d'un raccourci mode Focus


```
ilinux://favorites
```


---

## Comportement de lancement

Lorsque l'application reçoit une URL ou une action rapide :

| Scenario | Débit |
|----------|------|
| **Cold start — Quick Action (iOS/iPad only)** | `ScorecutSceneDelegate` → `PendingShortcutBuffer` → `ShortcutObserver.onAppear` → `dispatch(type:)` |
| **Warm start — Quick Action (iOS/iPad only)** | Callback de scène → notification → `dispatch(type:)` |
| **Cold / warm — `onOpenURL` (iOS, iPad, Mac)** | `AppRouter.handleIncomingURL` → `pendingDeepLink` → `RootTabView.onChange` navigue |
| **Feedback / Rate (cold start)** | `deferSheetWork` retards **~0.4 s** donc feuille de courrier / StoreKit a une scène de fenêtre active |
| **Search quick action** | `openSearchTab()` → `searchPulse += 1` → `BrowseCommandsView` présente la recherche (iOS 17+: auto-focus via `isPresented`) |
| **Unknown command ID** | Lien profond analysé mais la navigation sautée — pas d'alerte |

---

## Raccourcis clavier

### iPad & Mac (partagé)

Clavier hardware sur iPad et le menu **iLinux** sur Mac partage:

| Shortcut | Décision |
|----------|--------|
| ⌘F | Onglet Commandes + recherche (même intention que Recherche action rapide sur iOS) |
| ⌘1 | onglet Commandes |
| ⌘2 | Onglet Catégories |
| ⌘3 | Onglet Quiz quotidien |
| ⌘4 | Onglet Paramètres |

La recherche auto-focus via la touche F nécessite **iOS 17.0+** ou **macOS 14.0+**.

### Mac seulement

| Shortcut | Décision |
|----------|--------|
| ⌘, | Onglet Paramètres |
| ⌘[ / Esc | Pile de navigation pop (arrière) |
| ⌘← / ⌘→ | Catégorie précédente / suivante (onglet Catégories) |
| 1–4 | Sélectionnez l'option de réponse au quiz |
| ⌘R | Remaniement du quiz quotidien |
| Return | Question suivante (après réponse) |

Les liens profonds ( `ilinux://` ) et les raccourcis de menu utilisent le même routeur in-app sur Mac que sur iOS.

---

## URLs non prises en charge & invalides

| URL | Result |
|-----|--------|
| `ilinux://command` (no `name` / `cmd`) | Ignorées |
| `ilinux://command?name=NotARealCmd` | Ignoré (ID non dans la bibliothèque pour la plateforme résolue) |
| `ilinux://command?cmd=dir` (no platform) | Ouvre la bibliothèque **Linux** — utilisez `platform=cmd` pour Windows CMD |
| `ilinux://search` via Shortcuts Open URL | **Non** analysé par `ILinuxDeepLink` — Utilisez une action rapide sur **iOS/iPad**, ou sur **Mac/iPad** |
| `ilinux://categories` via Shortcuts Open URL | Comme ci-dessus |
| `ilinux://feedback` / `ilinux://review` via Open URL | Comme ci-dessus |
| Non-`ilinux` schemes | Ignorées |

---

## Dépannage

**Shortcut ouvre l'application mais rien ne se passe (lancement froid)**

Feedback, Rate et les feuilles de courrier ont besoin ~0.4 s après le lancement. Essayez de nouveau de l'intérieur de l'application, ou attendez un moment sur le démarrage froid.

**La recherche rapide ne focalise pas le champ de recherche (iOS 16)**

Autofocus nécessite iOS 17+. Sur iOS 16, l'onglet Commandes s'ouvre toujours; appuyez manuellement sur le champ de recherche.

**Le bouton Widget n'ouvre pas la commande attendue**

Assurez-vous que la commande existe toujours dans votre version d'application installée pour le bon **platform**. Les liens Widget utilisent `ilinux://` + `iLinux://` et nécessitent un identifiant de commande exact. Exemple : `platform` nécessite `ilinux` , pas la bibliothèque Linux par défaut.

**Les titres d'action rapide sont dans la mauvaise langue**

Changer de langue dans **Paramètres → Langue** — l'application ré-enregistre automatiquement les éléments raccourcis.

**Le lien profond fonctionne sur l'appareil mais pas sur une page Web**

Confirmer que le lien utilise le schéma `ilinux://` et est ouvert par le système (tap dans Notes/Messages), non bloqué par un navigateur in-app qui bande les schémas personnalisés.

---

[Retour à iLinux Support](../) &middot; [FAQ](../faq) &middot; [Politique de confidentialité](../privacy)


