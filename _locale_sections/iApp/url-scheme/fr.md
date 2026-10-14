iApp prend en charge les liens de raccourci ** `iapp://` ** et ** `iappstore://` **. Utilisez-les dans **Shortcuts**, signets Safari, ou à partir de **Widgets d'écran d'accueil** et **Activité en direct** pour **ouvrir une page de détail de l'application**, **retourner à une vue des classements filtrés**, **switch onglets**, ou **jeter vers des pages secondaires** ( favorites du développeur, parcourir l'historique, suivi des classements, etc.).

> **Note:** Long-press **Home Screen Quick Actions** utilisent le même texte de lien `iapp://` , mais sont envoyés comme actions rapides — non analysé par le même chemin que les URL Safari / Raccourcis lorsqu'elles sont ouvertes depuis le menu icône seulement.

## Format de lien


```
iapp://...
iappstore://...   (older alias, works the same)
```


Les hôtes sont **insensibles aux cas** et normalisés à **cas de kebab** ( `iapp://` et `iappstore://` → `iapp://{host}` ). Legacy alias: `developer_favorites` → rang, `developer.favorites` → abonnement, `developer-favorites` → revue.

| What you want | Type de lien |
|---------------|-----------|
| Open an app detail page | "iapp://app ?" |
| Open Rankings with filters | "iapp://rank?" |
| Switch tabs or open settings pages | `iapp://{host}` (voir tableaux ci-dessous) |
| Tap an app in a widget | Ouvre la page de détail |
| Tap the widget title / blank area | Ouvre la vue correspondante des classements |
| Tap a rank **Live Activity** | Ouvre la vue correspondante des classements |
| Tap a subscription **Live Activity** | Ouvre la page de détail de l'application |

---

## Ouvrir une page de détail de l'application


```
iapp://app?id={APP_ID}&region={region}&country={cc}
```


| Parameter | Required | Désignation des marchandises |
|-----------|----------|-------------|
| `id` | **Yes** | ID de l'App Store |
| `region` | No | Code régional, par exemple `cn`, `us`, `jp` (par défaut: `us`) |
| `country` | No | Code régional facultatif si la "région" est omise |

**Exemple**


```
iapp://app?id=6446581591&region=cn
```


Utilisé par : **Mes favoris widget** (tap une application), **s'abonner Activité en direct** (tap l'activité), et **Shortcuts** / signets.

---

## Ouvrir les classements avec les filtres

Passez à l'onglet **Rankings** et applique votre carte, catégorie et région choisie.


```
iapp://rank?type={chart}&category={category}&region={region}
```


| Parameter | Désignation des marchandises |
|-----------|-------------|
| `type` | Code graphique (voir tableau ci-dessous) |
| `category` | Code de la catégorie — catégorie principale ou sous-catégorie de jeu |
| `region` | Code régional, par exemple `cn`, `us` |

Les valeurs non reconnues sont ignorées; les valeurs reconnues sont rappelées.

### Codes graphiques ( `iapp://` ) — 12 graphiques

| Code | Graphique |
|------|-------|
| `topFreeApplications` | Haut de l'iPhone Gratuit |
| `topPaidApplications` | iPhone Top payé |
| `topGrossingApplications` | iPhone Top Grossing |
| `newApplications` | Nouvelles applications |
| `newFreeApplications` | Nouveau gratuit |
| `newPaidApplications` | Nouveaux paiements |
| `topFreeiPadApplications` | Haut de iPad Gratuit |
| `topPaidiPadApplications` | iPad Top payé |
| `topGrossingiPadApplications` | iPad Top Grossing |
| `topFreeMacApplications` | Mac Haut libre |
| `topPaidMacApplications` | Mac Haut payé |
| `topGrossingMacApplications` | Mac Top Grossage |

### Codes de catégorie ( `iapp://` )

| Code | Catégorie |
|------|----------|
| `0` | Toutes les applications |
| `6014` | Jeux (tous les jeux) |
| `6005` | Social |
| `6007` | Productivité |
| `6002` | Services publics |
| `6008` | Photo & Vidéo |
| `6017` | Éducation |
| `6015` | Financement |
| … | 26 catégories principales |

** Sous-catégories de jeux :** `iapp://` C1   , `iapp://{host}` C3   (18 genres). Exemple : `developer.favorites` = Action.

### Exemples


```
iapp://rank?type=topFreeApplications&category=6014&region=cn
iapp://rank?type=topFreeMacApplications&category=0&region=us
```


### Liens plus anciens de style chinois (toujours pris en charge)


```
iapp://rank?type=热门免费榜&category=游戏&region=中国
```


Utilisé par : **Rankings widget** (titre de tap / zone vide), **rank Live Activity** (tap l'activité), et **Shortcuts**.

---

## Widget liens profonds

Les widgets n'utilisent pas un format URL séparé — ils génèrent automatiquement les mêmes liens `iapp://` et `iappstore://` .

| Widget | Tap target | Ouvre |
|--------|------------|-------|
| **Rankings · iApp** | An app row | «iapp://app?id=...&region=...» |
| **Rankings · iApp** | Title or blank area | «iapp://rank?type=...&category=...&region=...» |
| **My Favorites · iApp** | An app row | «iapp://app?id=...&region=...» |

Les favoris épinglés apparaissent en premier dans le widget Mes Favoris. Widget thème et langue suivent **Paramètres → Widgets** et votre langue de l'application (l'une des 18 langues). Lors de la configuration des régions de widgets, HK / TW / MO affichent des noms d'affichage plus clairs dans la liste et la recherche unifiée (par exemple, Chine, Chine, Chine, Chine); la région stockée **codes** dans les liens reste `iapp://` , `iappstore://` , `iapp://{host}` .

---

## Parcourir l'historique (pas un lien URL)

**App Parcourir l'histoire** est géré dans **Paramètres → Données → App Parcourir l'histoire**. Taper une entrée rouvre la page de détail à l'intérieur de iApp — il ne **pas** utiliser une URL `iapp://` que vous pouvez copier ou partager à l'extérieur.

---

## Live Activity liens profonds

| Live Activity type | Tap behavior | Lien généré |
|--------------------|--------------|----------------|
| **Rankings** (tracking preset) | Opens filtered Rankings | "iapp://rank?" |
| **Subscriptions** (per subscription) | Opens app detail | «iapp://app?id=...&region=...» |

Activer l'activité en direct par suivi préréglé dans **Paramètres → Avancé**. Activer l'abonnement Activité en direct dans **Paramètres → Avancé → Activité en direct** (séparer du rang Activité en direct); puis par abonnement lors de l'ajout ou de l'édition. Les moniteurs de baisse des prix indiquent le prix de base par rapport au prix actuel sur l'écran de verrouillage.

---

## Liens d'action (pas de requête)

Ils ouvrent un onglet ou déclenchent une action dans l'application. Fonctionne à partir de ** Raccourcis**, Safari et **Actions rapides d'écran d'accueil**.

### Onglets primaires

| URL | Ouvre |
|-----|--------|
| `iapp://search` | Onglet de recherche + champ de recherche |
| `iapp://rank` | Onglet de classement (aucun filtre ne change quand aucune requête) |
| `iapp://favorites` | **Onglet Favorites** si activé dans **Paramètres → Paramètres de l'application**; sinon **Paramètres → Favoris de l'application** |
| `iapp://subscription` | Onglet Abonnements si visible; sinon **Paramètres → Abonnements** |
| `iapp://settings` | Onglet Paramètres |
| `iapp://feedback` | E-mail de commentaires |
| `iapp://review` | Note App Store in-app (alias: `iapp://rate`) |

### Pages secondaires

Ouvre l'onglet **Paramètres** d'abord, puis pousse la page cible. Si un onglet correspondant existe (p. ex. Favoris du développeur), ouvre plutôt cet onglet.

| URL | Ouvre |
|-----|--------|
| `iapp://developer-favorites` | Onglet Favoris du développeur ou **Paramètres → Favoris du développeur** |
| `iapp://browse-history` | **Paramètres → Données → App Parcourir l'histoire** |
| `iapp://favorite-groups` | **Paramètres → Données → Groupes favoris** |
| `iapp://rank-tracking` | **Paramètres → Avancé → Suivi des classements** |
| `iapp://live-activity` | **Paramètres → Avancé → Activité en direct** |
| `iapp://apple-services` | **Paramètres → tiers → Services Apple** |
| `iapp://region-switch` | **Paramètres → tiers → App Store Region** |
| `iapp://usage-guide` | **Paramètres → Aide → Instructions d'utilisation** |
| `iapp://widget-guide` | **Paramètres → Widgets → Widget Guide** (iOS 17+ seulement; URL fonctionne mais n'est pas répertorié dans Quick Actions Selecter) |

---

## Actions rapides de l'écran d'accueil

Appuyez longuement sur l'icône de l'application. Personnalisez jusqu'à **4** à partir de **15** options dans **Paramètres → Écran d'accueil Presse longue → Personnalisez les raccourcis**.

Sélection par défaut : recherche, rang, favoris, rétroaction.

Chaque option utilise les mêmes URL que ci-dessus. Les actions rapides sont envoyées par le menu icône ; les raccourcis externes / Safari utilisent le chemin unifié `iappstore://` .

| Lien | Ouvre |
|------|--------|
| `iapp://search` | Onglet de recherche + focus |
| `iapp://rank` | Tableau des classements |
| `iapp://favorites` | onglet ou paramètres favoris → App Favoris |
| `iapp://developer-favorites` | Onglet ou paramètres favoris du développeur → Favoris du développeur |
| `iapp://subscription` | Onglet ou paramètres d'abonnement → Abonnements |
| `iapp://browse-history` | App Parcourir l'historique |
| `iapp://favorite-groups` | Paramètres des groupes favoris |
| `iapp://rank-tracking` | Suivi des classements |
| `iapp://live-activity` | Paramètres d'activité en direct |
| `iapp://apple-services` | Liens Apple Services |
| `iapp://region-switch` | Commutateur de région App Store |
| `iapp://usage-guide` | Instructions d'utilisation |
| `iapp://settings` | Onglet Paramètres |
| `iapp://feedback` | E-mail de commentaires |
| `iapp://review` | Note dans l'application | `iapp://` ---

## Siri & Raccourcis (iOS 16+)

Trouvez des actions intégrées dans l'application **Shortcuts** ou demandez **Siri**. Tous les titres d'intention, étiquettes de paramètres et phrases Siri sont ** entièrement localisés** dans chaque langue de l'application — ils mettent à jour lorsque vous changez **Paramètres → Apparence → Langue**.

| Action | What you can set | Effet |
|--------|------------------|--------|
| Search apps | Keyword and region | Ouvre l'onglet Recherche avec la requête |
| Open charts | Chart, category, and region | Ouvre les classements avec filtres (même que `iapp://rank`) |
| Add favorite | App ID and region | Ajoute aux favoris silencieusement |

**Exemple Siri phrases (interface utilisateur) :** *"Rechercher des applications dans iApp"*, *"Ouvrir des graphiques dans iApp"*, *"Ajouter des favoris dans iApp"*. Dans la version 简体中文, les phrases apparaissent en chinois, même pour les 18 langues.

---

## raccourcis clavier Mac

Sur Mac, utilisez **. Les nombres sont attribués **dynamiquement** en fonction des onglets visibles:

| When visible | Raccourci typique |
|--------------|------------------|
| Rankings | 1 |
| Search | *2 |
| Subscriptions (if shown) | Numéro suivant |
| Favorites (if tab enabled) | Numéro suivant |
| Developer Favorites (if tab enabled) | Numéro suivant |
| Settings | Dernier numéro |

Exemple avec tous les onglets optionnels sur: -1 Classements · -2 Recherche · -3 Abonnements · -4 Favoris · -5 Favoris du développeur · -6 Paramètres.

Lorsqu'un onglet est caché, les onglets restants renumérotent automatiquement.

---

## Codes régionaux en liens

Les liens profonds et les URL générées par widget utilisent toujours des codes stables **region** ( `iapp://` , `iappstore://` , `iapp://{host}` , `developer_favorites` , `developer.favorites` , ...) — non pas des noms d'affichage localisés. Les récupérateurs régionaux et les chercheurs peuvent afficher des étiquettes plus claires, mais les codes stockés restent les mêmes.

**Exemples**


```
iapp://app?id=6446581591&region=hk
iapp://rank?type=topFreeApplications&category=0&region=tw
```


---

## Recherche dans l'application (pas les liens URL)

Ces travaux à l'intérieur de iApp mais ne sont pas **** URLs :

| Action | Comment |
|--------|-----|
| **Single App ID search** | Saisissez un ID numérique (6–12 chiffres, pas de virgule) dans Recherche |
| **Batch App ID search** | Jusqu'à 50 identifiants séparés par des virgules |
| **Add Subscription** | Appuyez sur n'importe quelle ligne d'application |
| **Save Developer** | Long-press → **Développeur** sous-menu, ou détail **Plus** menu |
| **Open by-ranking view** | Menu contextuel → apps ou favoris du développeur |
| **Pause / resume subscription** | Long-press sur une ligne d'abonnement |
| **Reopen from browse history** | **Paramètres → Données → App Parcourir l'histoire** → tap entry |

Utilisez des liens **        ** ou **Siri / Raccourcis** lorsque vous devez ouvrir iApp depuis l'extérieur de l'application.

---

## Conseils

- Link codes work in any app language — Ils ne changent pas lorsque vous changez de langue d'assurance-chômage.
- Widgets et **Live Activity** génèrent ces liens automatiquement lorsque vous appuyez sur.
- Les données des graphiques Widget pour certains graphiques de Mac/iPad payés et de grossissement peuvent différer légèrement de l'application principale.
- **Add favorite** via Shortcuts does not open the app UI — il écrit directement à votre liste de favoris.
- **Content compare** mode in all-region info cannot export share images — passer d'abord à la liste ou à la grille.

[Retour à l'aperçu](..) · [FAQ](../faq) · [Confidentialité](../privacité)


