iPomodoro prend en charge ** `iPomodoro://` ** et ** `iPomodoros://` ** Les liens profonds du schéma URL — ouvrez un onglet ou une feuille d'application depuis Safari, une autre application, un code QR ou des raccourcis Apple. Ces URL reflètent les destinations disponibles sous la forme de **Home Screen Quick Actions** (cliquez sur l'icône de l'application).

> **Note:** Liens URL ne **pas** timers de démarrage ou d'arrêt, pass IDs de tâches, ou durées de pré-remplissage. Ils naviguent seulement dans l'application. Pour les résumés de focus parlés sans ouvrir l'application, utilisez **Shortcuts d'application Siri** (voir [Related: Siri & App Shortcuts] (#related-siri--app-shortcuts) ci-dessous).

## Spécification du protocole


```
iPomodoro://<path>
iPomodoros://<path>
```


| Rule | Détail |
|------|--------|
| **Schemes** | `iPomodoro` (primaire) · `iPomodoros` (également accepté) |
| **Path** | Segment unique, **insensible** — résolu à partir de l'URL **host** |
| **Query parameters** | Non pris en charge (ignoré si présent) |
| **Equivalent Quick Action type** | `iPomodoro://<path>` (même chaîne enregistrée sur les raccourcis Home Screen) |

La correspondance de chemin est **exacte** sur le nom du segment — l'application ne fait pas de sous-chaînes floues comme `iPomodoro://` .

---

## Destinations

| Path | Opens | Notes |
|------|--------|-------|
| `pomodoro` | **Pomodoro** tab | Ne démarre pas automatiquement une session |
| `study` | **Study Timer** tab | Ne démarre pas automatiquement une session |
| `tasks` | **Tasks** tab |  |
| `stats` | **Statistics** tab |  |
| `motivation` | **Motivational Quote Anthology** full-screen gallery | Même UI que **Paramètres → Paramètres des citations motivationnelles → Anthologie des citations motivationnelles** |
| `feedback` | **Feedback** sheet | Utilisations in-app Mail composer lorsque disponible; tombe à `mailto:` |

---

## Exemples

**Ouvrir l'onglet Pomodoro**


```
iPomodoro://pomodoro
```


**Open Study Timer tab** (système alternatif)


```
iPomodoros://study
```


**Tableau de bord des statistiques ouvertes**


```
iPomodoro://stats
```


**Afficher une citation de motivation**


```
iPomodoro://motivation
```


**Rétroaction ouverte**


```
iPomodoro://feedback
```


---

## Comportement de lancement

Lorsque l'application reçoit une URL (démarrage froid ou en cours d'exécution) :

1. `iPomodoro://` résout le chemin par `iPomodoros://` .
2. La navigation est ** différée ~0.45 s** pour que SwiftUI puisse terminer le montage.
3. Sur **cold start**, une URL / Quick Action prend **priority** au lieu de sauter automatiquement à un onglet actif Pomodoro ou Study d'une session d'activité en direct restaurée.

**Motivation** et **feedback** ouvrir les superpositions directement — ils ne changent pas les onglets d'abord.

---

## Raccourcis des pommes

**Ouvrir l'onglet Pomodoro**

1. Ajouter une action **Ouvrir l'URL**
2. URL : `iPomodoro://` **Ouvrir les statistiques après un bloc de concentration**


```
iPomodoro://stats
```


Utilisez **Ouvrir l'URL** dans une automatisation personnelle (par exemple après la fin d'un mode Focus) pour sauter directement dans votre tableau de bord.

---

## Related: Siri & App Raccourcis

Intégration **Les raccourcis d'application** (application Siri / Raccourcis) complètent les liens URL :

| Intent | Comportement |
|--------|----------|
| Open Pomodoro | Switches vers l'onglet Pomodoro |
| Open Study Timer | Switches to Study Timer tab |
| Open Statistics | Basculer vers l'onglet Statistiques |
| Today's focus summary | Retourne la durée de mise au point et le nombre de pomodoros **sans exiger l'application UI** |

Exemple de phrase Siri : *"Combien de temps ai-je mis aujourd'hui dans iPomodoro?"*

Configurez les quatre éléments qui apparaissent sur l'icône de l'écran d'accueil sous **Paramètres → Paramètres de l'application → Raccourcis de l'écran d'accueil** (gouttez pour réorganiser). Les chemins d'URL ci-dessus couvrent les six destinations possibles; seulement quatre peuvent apparaître sur l'icône à la fois.

---

## Dépannage

| Issue | Quoi vérifier |
|-------|----------------|
| Link does nothing | S'assurer que l'application est installée; chemin doit être l'un des six noms ci-dessus |
| Wrong tab after reopening | Si un timer Live Activity est actif, un **Quick Action / URL lance remplace** auto tab restaurer |
| `feedback` opens Mail app only | Le périphérique n'a pas de compte Mail configuré — iPomodoro revient à `mailto:` |

---

[Retour à iPomodoro Support](../) &middot; [FAQ](../faq) &middot; [Politique de confidentialité](../privacy)


