iWool prend en charge ** `iwool://` ** Des liens profonds du schéma d'URL – ouvrez un onglet, lancez une action dans l'application, ou sautez à une activité spécifique de Safari, de raccourcis Apple, d'un widget ou d'une action rapide d'écran d'accueil (cliquez sur l'icône de l'application).

> **Important:** Liens profonds seulement **naviggate à l'intérieur iWool**. Ils ne créent pas de connexions de serveur ni ne synchronisent les données vers le cloud.

## Spécification du protocole


```
iwool://<path>[?query]
```


| Rule | Détail |
|------|--------|
| **Scheme** | "iwool" (insensible au cas par cas) |
| **Routing** | Le premier segment de chemin (hôte ou chemin) sélectionne la destination |
| **Empty URL** | `iwool://` sans chemin → **Accueil** |
| **Unknown paths** | **Ignoré** (pas de retour silencieux à la maison) |
| **Parser** | `IWoolDeepLink.parse( :)` → `ContentView.applyDeepLink` |

---

## 1. Destinations des onglets

| URL | Ouvre |
|-----|--------|---------|
| `iwool://home` | **Home** tab | — |
| `iwool://calendar` | **Calendar** tab | «cal» |
| `iwool://stats` | **Statistics** tab | «statistique», «stat» |
| `iwool://settings` | **Settings** tab | `réglage`, `préférences` |

---

## 2. Actions en cours

Ces itinéraires correspondent à **Actions rapides de l'écran d'accueil** et feuilles ou sous-pages ouvertes:

| URL | Ouvre |
|-----|--------|---------|
| `iwool://new` | **Create activity** sheet | `create`, `add`, `new-event`, `new-event` |
| `iwool://island` | **Quick Countdown** (Dynamic Island reminder) sheet | < < Island-Reminer > > , < < Island-Reminer > > , < < Compte à rebours > > , < < Compte à rebours > > , < < Compte à rebours > > |
| `iwool://reminders` | **Scheduled local reminders** list (Settings) | `reminders programmés`, `reminders programmés`, `reminders programmés`, `reminders de notification` |
| `iwool://scanner` | **QR / barcode scanner** (Settings → Tools) | `scan`, `qrcode`, `barcode` |
| `iwool://rate` | In-app **App Store rating** prompt | « rating », « review », «rate-in-app », «rateinapp » |
| `iwool://feedback` | **Feedback** email compose | `mail`, `support`, `contact` |

**Les chemins de paramètres nestés** (même actions):


```
iwool://settings/scanner
iwool://settings/reminders
iwool://settings/rate
iwool://settings/feedback
```


---

## 3. Détail des activités

Ouvrez une seule activité de laine par ID de base de données.

| Parameter | Required | Désignation des marchandises |
|-----------|----------|-------------|
| Path `event/{id}` | One of path / query | Identification de l'activité (entier positif) |
| Query `id={id}` | One of path / query | Comme le chemin |
| Query `day={seconds}` | No | Pour **activités récurrentes** - début de la journée naturelle comme «tempsIntervalDepuis1970» (la nuit du même jour) |

**Ouverture de l'activité 42**


```
iwool://event/42
iwool://event?id=42
```


**Événement récurrent à un jour donné**


```
iwool://event/42?day=189345600
```


Lors de la construction de liens pour les séries récurrentes, iWool peut dériver `iwool://` de la même logique que la liste d'origine ( `iwool` ).

---

## 4. Actions rapides de l'écran d'accueil (iOS)

Appuyez longuement sur l'icône iWool → jusqu'à **4** actions. Personnaliser dans **Paramètres → Outils → Raccourcis d'écran d'accueil** (9 options, glisser pour réorganiser, réinitialiser aux valeurs par défaut).

| Option | URL |
|--------|-----|
| Home | "iwool://home" |
| Calendar | "iwool://calendar" |
| Statistics | 'iwool://stats' |
| Quick Countdown | 'iwool://island' |
| New Activity | "iwool://new" |
| Scheduled Reminders | 'iwool://reminders' |
| Scanner | 'iwool://scanner' |
| Rate App | "iwool://rate" |
| Feedback | "iwool://feedback" |

**Défaut lors de la première installation :** Accueil · Calendrier · Statistiques · Compte à rebours rapide.

Action rapide `iwool://` ---

## 5. Widget liens profonds

Les touches Widget utilisent les mêmes URLs :

| Widget | Tap target | URL |
|--------|------------|-----|
| Today Active / Today All / Today Upcoming / All Events | Home | "iwool://home" |
| Stats Overview / Earnings / Top Platforms | Statistics | 'iwool://stats' |
| Glance | First event or Home | "iwool://event/{id}" ou "iwool://home" |
| Lock Screen accessories | First event or Home | "iwool://event/{id}" ou "iwool://home" |
| List row (iOS 17+) | Activity detail | `iwool://event/{id}` |

Quick Countdown Live Activities utilise l'interface utilisateur dans l'application uniquement — **pas d'URL séparée** pour lancer un compte à rebours à partir de l'extérieur de l'application (utilisez `iwool://` pour ouvrir la feuille de création).

---

## Exemples de raccourcis pour Apple

** Statistiques ouvertes**


```
iwool://stats
```


**Créer une nouvelle activité**


```
iwool://new
```


**Ouvrir la feuille de compte à rebours**


```
iwool://island
```


**Ouvrir l'activité après avoir copié l'ID**


```
iwool://event?id=42
```


---

## Comportement de lancement

| Scenario | Débit |
|----------|------|
| **Widget / Shortcuts `onOpenURL`** | `AppRouter` → `applyDeep Lien |
| **Cold start — Quick Action** | `SceneSceneDelegate` → `PendingShortcutBuffer` → `ScetcutObserver` |
| **Warm start — Quick Action** | Callback de scène → notification → `ShortcutObserver` |
| **Feedback / Rate (cold start)** | Court délai donc la feuille mail / StoreKit a une scène de fenêtre active |
| **Invalid event ID** | Lien ignoré — pas d'alerte |

---

## Dépannage

| Issue | Quoi vérifier |
|-------|----------------|
| Link opens app but nothing happens | Path doit correspondre à une route supportée; les chemins inconnus ne sont pas redirigés vers Home |
| `event` link shows wrong occurrence | Ajouter `?day=` pour les activités récurrentes |
| Quick Action does nothing on cold launch | Attendez ~0.4 s ou réessayez; Feedback/taux besoin temps de montage de l'interface utilisateur |
| `iwool://island` does not start countdown automatically | Ouvre la feuille de création **** — confirmer la durée et appuyez sur Démarrer dans l'application |
| Quick Countdown requires iOS 16.2+ | Les activités de l'événement en direct ont besoin d'iOS 16.1+; compte à rebours île autonome a besoin de 16.2+ |

---

[Retour à iWool Support](..) · [FAQ](../faq) · [Politique de confidentialité](../privacy)


