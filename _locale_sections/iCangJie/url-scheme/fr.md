iCangJie supporte ** `iCangJie://` ** URL schéma de liens profonds — ouvert Recherche de recherche, de détail de mots, Daily Quiz, Typing, Favoris, mauvais livre, niveaux, ou apprendre de Safari, une autre application, un code QR, un widget tap, ou Apple Raccourcis.

Un ensemble parallèle de **Actions rapides d'écran d'accueil** (appuyer sur l'icône de l'application) couvre d'autres destinations telles que Search, Feedback et Rate. Configurez jusqu'à 4 raccourcis dans **Paramètres → Paramètres de l'application → Raccourcis d'écran d'accueil**.

## Spécification du protocole


```
iCangJie://<host>[?query]
```


| Rule | Détail |
|------|--------|
| **Scheme** | `icangjie` / `iCangJie` — comparaison insensible aux cas |
| **Host routing** | Le routeur principal est l'URL **host** |
| **Query aliases** | `q`, `word` et `name` sont interchangeables pour les hôtes de recherche/mot |
| **Parser** | `ICangJieDeepLink.parse( :)` — consommé via `onOpenURL` → `AppRouter.pendingDeepLink` |

**Trois canaux de livraison**

| Channel | Handled by | Exemples |
|---------|------------|----------|
| **Universal deep link** (`onOpenURL`) | `ICangJieDeepLink.parse` → `RootTabView` | `recherche`, `mot`, `quiz`, `typing`, `favorites`, `mauvais`, `niveaux`, `apprendre` |
| **Home Screen Quick Action** | `ShortcutObserver.dispatch` | `recherche`, `quiz`, `favorites`, `mauvais`, `niveaux`, `feedback`, `examen` |
| **App Intents / Siri / Widget pending URL** | Writes `AppGroup.pendingDeepLinkURL` → `RootTabView.consumePendingDeepLinkFromAppGroup()` | Code de recherche, quiz de démarrage, recherche ouverte |

Les types d'action rapide utilisent ** `iCangJie://` ** correspondant sur la chaîne de type, de sorte que les variantes `icangjie` et les variantes héritées suivent toujours correctement.

---

## 1. Recherche de recherche

Ouvrez l'onglet **Lookup**. En option, préremplissez le champ de recherche.

| Parameter | Required | Désignation des marchandises |
|-----------|----------|-------------|
| `q` | No | Requête de recherche (préfixe de code, caractère, pinyin, ou Jyutping) |
| `word` | No | Synonyme de `q` |
| `name` | No | Synonyme de `q` |

**Open Lookup (recherche vide)**


```
iCangJie://search
```


**Rechercher le préfixe de code `iCangJie://` **


```
iCangJie://search?q=ab
```


**Rechercher un personnage


```
iCangJie://search?q=颉
```


---

## 2. Détail des mots

Ouvrez la page de détails pour un seul caractère. Nécessite une requête non vide.

| Parameter | Required | Désignation des marchandises |
|-----------|----------|-------------|
| `q` | One of `q` / `word` / `name` | Caractère Han cible |
| `word` | One of `q` / `word` / `name` | Synonyme de `q` |
| `name` | One of `q` / `word` / `name` | Synonyme de `q` |

**Hosts acceptés :** `iCangJie://` , `icangjie` , `iCangJie` **Détails ouverts pour :**


```
iCangJie://word?q=倉
```


Autre hôte :


```
iCangJie://character?word=颉
```


Si la requête est **vide ou si le caractère n'est pas dans le dictionnaire**, le lien est ** silencieusement ignoré**.

---

## 3. Quiz quotidien

Sautez directement au Quiz quotidien**. Ne démarre pas automatiquement ou ne saute pas les questions.


```
iCangJie://quiz
```


Alias: `iCangJie://` ---

## 4. Pratique dactyloscopique

Ouvrez le centre d'onglet **Typing**.


```
iCangJie://typing
```


Alias : `iCangJie://` , `icangjie` ---

## 5. Favoris

Ouvrez la liste **Favorites**.


```
iCangJie://favorites
```


Étrangères :

---

## 6. Livre de mauvaise réponse

### 6.1 Liste

Ouvrez la liste **Wrong Answer Book**.


```
iCangJie://wrong
```


Alias : `iCangJie://` , `icangjie` ### 6.2 Enregistrement unique

Lorsque `iCangJie://` | Parameter | Required | Format |
|-----------|----------|--------|
| `record` | Yes | Chaîne UUID |
| `id` | Yes | Synonyme de `record` |


```
iCangJie://wrong?record=550e8400-e29b-41d4-a716-446655440000
```


---

## 7. Niveaux (longueur du code)

Ouvrez l'onglet **Nivaux**.


```
iCangJie://levels
```


Alias : `iCangJie://` , `icangjie` ---

## 8. Apprendre (tutoriels)

Ouvrez le centre **Learn**.


```
iCangJie://learn
```


Alias: `iCangJie://` ---

## 9. Rétroaction (action rapide seulement)

Ouvrez l'éditeur de courriels de rétroaction prérempli (ou `iCangJie://` ```
iCangJie://feedback
```


Géré par **Action rapide de l'écran d'accueil** / `iCangJie://` , pas `icangjie` .

---

## 10. App Store Review (action rapide seulement)

Demander un avis App Store in-app rapide.


```
iCangJie://review
```


Alias matching accepte également `iCangJie://` dans la chaîne de type action rapide.

---

## 11. App Intents & Siri (iOS 16+)

Les raccourcis de l'application** apparaissent dans l'application Raccourcis et Siri. Chaque intention définit `iCangJie://` dans le groupe App; l'application la consomme au lancement.

| Intent | Action | URL en attente |
|--------|--------|-------------|
| **Look up Cangjie code** | Opens word detail for the given character | `iCangJie://word?q=<char>` |
| **Start daily quiz** | Opens Daily Quiz | 'iCangJie://quiz' |
| **Open lookup search** | Opens Lookup tab | "iCangJie://search" |

**Exemple de phrases Siri (anglais)**

- *"Regardez le code Cangjie pour "" dans iCangJie"*
- *"Démarrer le quiz quotidien en iCangJie"*
- *"Rechercher Cangjie en iCangJie"*

Dans **Shortcuts**, ajoutez l'action de la section application iCangJie. L'intention **Look up** nécessite un paramètre **Chinois** ( `iCangJie://` ).

> App Intents sont **iOS seulement**. macOS compte sur `iCangJie://` URLs et la navigation de menu.

---

## Widget Liens profonds

Widgets tapez sur les mêmes URLs. Exemples:

| Widget | URL typique |
|--------|-------------|
| Daily Character | `iCangJie://word?q=<char>` |
| Code Length | «iCangJie://niveaux» |
| Daily Quiz | 'iCangJie://quiz' |
| Typing Glance | "iCangJie://typing" |
| Favorites | `iCangJie://favorites` |
| Wrong Book | 'iCangJie://wrong' |
| Recent | "iCangJie://search" |
| Learning Progress | <iCangJie://learn> |

---

## Exemples de raccourcis

**Ouvrir le questionnaire d'aujourd'hui**


```
iCangJie://quiz
```


**Regardez un personnage du presse-papiers**

Utilisez un raccourci **Obtenez l'action Clipboard**, puis **Ouvrir l'URL** avec :


```
iCangJie://word?q=[Clipboard]
```


**Démarrer la pratique de dactylographie**


```
iCangJie://typing
```


---

## Actions rapides de l'écran d'accueil

Appuyez sur l'icône iCangJie. Options par défaut (cochez jusqu'à 4 dans Paramètres) :

| Action | URL |
|--------|-----|
| Search | "iCangJie://search" |
| Daily Quiz | 'iCangJie://quiz' |
| Favorites | `iCangJie://favorites` |
| Wrong Book | 'iCangJie://wrong' |
| Code Length | «iCangJie://niveaux» |
| Feedback | «iCangJie://feedback» |
| Rate App | 'iCangJie://review' |


