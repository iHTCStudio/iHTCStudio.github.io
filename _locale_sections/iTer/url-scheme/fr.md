iTer supporte le schéma d'URL ** `iTer://` ** sur **iPhone et iPad**. Utilisez-le dans Raccourcis, Safari, Widgets, ou d'autres applications pour ouvrir une question, le quiz quotidien, les favoris, ou le livre de mauvaise réponse.

**Actions rapides à l'écran d'accueil** (appuyer sur l'icône de l'application) réutiliser les mêmes chaînes `iTer://` . Choisissez jusqu'à **4** parmi **7** options dans **Paramètres → raccourcis d'écran d'accueil**.

> **Note:** Liens profonds **navigate** dans l'application. Ils ne changent pas les paramètres du quiz ou ne marquent pas les questions à distance. **Mac** ne enregistre pas Home Screen Quick Actions; les widgets et la navigation dans l'application fonctionnent toujours sur Mac.

## Protocole


```
iTer://<host>[?query]
```


| Rule | Détail |
|------|--------|
| **Scheme** | `iTer` (insensible aux cas) |
| **Question detail** | Question de l'hôte — requête **`id=<questionID>`** ou **`q=<questionID>`** (obligatoire) |
| **Daily Quiz** | Hébergement "quiz" |
| **Favourites** | Hôte `favorites` → Paramètres → Liste des favoris |
| **Wrong book** | Hôte `wrong`, `mistakes` ou `wrongquestions` — optionnel **`record=<UUID>`** ouvre une erreur |
| **Search** | Host `search` — Action rapide / raccourci uniquement (ouvre l'onglet recherche globale) |
| **Categories** | Hôte `category` — Action rapide / raccourci uniquement (ouvre l'onglet Catégories) |
| **Feedback** | Hôte `feedback` — Action rapide seulement (le courriel compose ou `mailto:` repli) |
| **Rate app** | Host `review` — Action rapide seulement (StoreKit in-app review). Les types d'héritage contenant "star" fonctionnent également. |

Des chemins tels que `iTer://` sont acceptés lorsque l'hôte est vide et que le segment de chemin correspond.

## Exemples


```
iTer://question?id=94c34bb2bdef11e6a0e100163e0021c8
iTer://quiz
iTer://favorites
iTer://wrong
iTer://wrong?record=550E8400-E29B-41D4-A716-446655440000
```


## Actions rapides de l'écran d'accueil

| Type | Utilisation typique |
|------|-------------|
| `iTer://search` | Recherche mondiale |
| `iTer://quiz` | Onglet Quiz quotidien |
| `iTer://favorites` | Liste des favoris |
| `iTer://wrong` | Livre de réponses erronées |
| `iTer://categories` | Onglet Catégories |
| `iTer://feedback` | Envoyer des commentaires |
| `iTer://review` | Noter l'application (StoreKit) |

Sélection par défaut : Recherche, Quiz, Favoris, Commentaires. Réorganiser ou remplacer **Paramètres → raccourcis d'écran d'accueil** (maximum 4). L'application correspond à des chaînes de raccourci `iTer://` avec **contient**, de sorte que les variantes héritées qui incluent ces chemins suivent toujours correctement.

## Widget liens profonds

| Widget | URL typique |
|--------|-------------|
| Daily Question | `iTer://question?id=...` |
| Quiz Glance | 'iTer://quiz' |
| Favourites Glance | `iTer://favorites` |
| Wrong Book Glance | `iTer://wrong` ou `iTer://wrong?record=<UUID>` |

---

[Retour à iTer Support](../) · [FAQ](../faq) · [Politique de confidentialité](../privacy)


