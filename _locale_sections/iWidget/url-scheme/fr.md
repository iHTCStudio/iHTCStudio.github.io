iWidget prend en charge le schéma d'URL ** `iwidget://` ** sur **iPhone, iPad et Mac**. Utilisez-le dans **Safari**, **Shortcuts d'Apple**, une autre application ou un code QR pour sauter dans l'application principale. Ces liens **navigate seulement** — ils ne passent pas les identifiants de conception de widget ou de modification de la configuration du tableau.

Pour les réponses orales lunaires / festival **sans** ouverture de l'application, utilisez **Séri App Raccourcis** (voir [FAQ](../faq) → Siri). Pour **travail / repos à une date**, ajouter le **Travail** App Intent dans Raccourcis.

## Format


```
iwidget://<host>[?query]
```


| Rule | Détail |
|------|--------|
| **Scheme** | `iwidget` (cas inférieur) |
| **Host** | Segment de trajectoire — voir tableau ci-dessous |
| **Query** | Optionnel; seules les clés documentées sont lues |

Les hôtes inconnus sont ignorés en toute sécurité (pas de crash).

---

## Hôtes

| Host | Opens | Demande |
|------|--------|-------|
| `today` | **Today** tab | — |
| `day` | **Today** tab and queues **day detail** for the given date | **'y'** année * **`m`** mois * **`d`** jour (integers) |
| `settings` | **Settings** tab | **`scroll=festivals`** défile vers la section filtre du festival |

Si `iwidget://` ---

## Exemples

**Ouvert aujourd'hui**


```
iwidget://today
```


**Ouvert le 1er janvier 2026 detail**


```
iwidget://day?y=2026&m=1&d=1
```


**Ouvrir les paramètres → filtres du festival**


```
iwidget://settings?scroll=festivals
```


---

## Comportement Widget & Control Center

- Cartographier un tableau d'écran ** à la maison** lorsque **intercept taps** est désactivé peut ouvrir `iwidget://today` (ou votre comportement ouvert configuré via l'intention de widget).
- **Lock Screen** et **Control Center** les entrées utilisent App Intents; ce ne sont pas des hôtes URL supplémentaires.
- **La barre de menu Mac** utilise le même modèle d'URL `jour` lorsque vous cliquez sur une date.

---

## Conseils de raccourcis

1. Ajouter **Ouvrir l'URL** et coller un lien `iwidget://` .
2. Pour les vérifications de **jour de travail**, recherchez la bibliothèque d'action Raccourcis pour iWidgets **jour de travail/rest** intention et fournir une date — il est **non** disponible en tant que requête URL.

[Retour à iWidget Support](../) · [FAQ](../faq) · [Politique de confidentialité](../privacy)


