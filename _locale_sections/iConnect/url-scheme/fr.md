iConnect prend en charge ** `iconnect://` ** Les liens profonds du schéma URL — ouvrez un onglet, une page Paramètres, ou une feuille d'application de Safari, une autre application, un signet ou des raccourcis Apple. Ces URL reflètent les destinations disponibles sous la forme de **Home Screen Quick Actions** sur iPhone et iPad (long-press l'icône de l'application).

> **Note:** Liens URL uniquement **navigate inside iConnect**. Ils ne se connectent pas à un pair, démarrent un transfert ou ouvrent un fil de discussion spécifique.

## Spécification du protocole


```
iconnect://<host>
iconnect://<host>?refresh=1
```


| Rule | Détail |
|------|--------|
| **Scheme** | `connecter` |
| **Host / path** | Un seul segment, **insensible aux cas** — résolu à partir de l'URL **host** ou du premier segment **path** |
| **Aliases** | Plusieurs hôtes acceptent les synonymes (voir tableau ci-dessous) |
| **Query** | Seulement `refresh=1` / `refresh=true` sur **Dispositifs** déclenche un rafraîchissement découverte |

Exemples de formulaires équivalents:


```
iconnect://devices
iconnect://open/devices
```


---

## Destinations des onglets

| URL | Ouvre |
|-----|--------|---------|
| `iconnect://devices` | **Devices** tab (radar / discovery) | "dispositif" |
| `iconnect://devices?refresh=1` | **Devices** tab and **refreshes** nearby discovery | — |
| `iconnect://chat` | **Chats** tab | "messages" |
| `iconnect://transfers` | **Transfers** tab | "transfert" |
| `iconnect://history` | **History** tab (transfer log) | — |
| `iconnect://settings` | **Settings** tab | «réglage» |

**Découverte nouvelle**


```
iconnect://devices?refresh=1
iconnect://devices/refresh
```


---

## Paramètres des sous-pages

Ces liens passent à **Paramètres**, puis ouvrez la page correspondante:

| URL | Ouvre |
|-----|--------|---------|
| `iconnect://about` | About | — |
| `iconnect://usage` | Usage Guide | «guide», «aide», «guide d'usage» |
| `iconnect://shortcuts` | Home Screen shortcuts picker (iOS) | "shortcuts à domicile" |
| `iconnect://debug` | Debug / diagnostics info | `debuginfo` |

---

## Actions en cours

| URL | Ouvre |
|-----|--------|
| `iconnect://share` | Partager la feuille iConnect (Lien de l'App Store + texte de recommandation) |
| `iconnect://feedback` | E-mail de rétroaction composer (reste à `mailto:` si le courrier n'est pas disponible) |
| `iconnect://review` | App dans l'application Note de magasin rapide |

**Alias de l'examen :** `iconnect://` , `iconnect` ---

## Exemples

**Ouvrir l'onglet Chats**


```
iconnect://chat
```


**Ouvrir l'onglet Transferts**


```
iconnect://transfers
```


**Découverte de l'appareil neuf**


```
iconnect://devices?refresh=1
```


**Guide d'utilisation ouvert**


```
iconnect://usage
```


**Partagez l'application**


```
iconnect://share
```


---

## Actions rapides d'écran d'accueil (iOS)

Appuyez sur l'icône iConnect. Personnalisez jusqu'à **4** raccourcis dans **Paramètres → raccourcis d'écran d'accueil** (gouttez pour réorganiser).

| Quick Action | URL |
|--------------|-----|
| Devices | `iconnect://devices` |
| Chats | "iconnect://chat" |
| Transfers | "iconnect://transferts" |
| History | "iconnect://histoire" |
| Share | `iconnect://share` |
| Feedback | `iconnect://feedback` |
| Rate | `iconnect://review` |
| About | `iconnect://about` |

Par défaut activé : **Dispositifs**, **Chats**, **Share**, **Feedback**.

Les types d'action rapide utilisent les mêmes chaînes `iconnect://` et sont acheminés par le même analyseur que les URL externes.

---

## Raccourcis des pommes

**Ouvrir l'onglet Transferts**

1. Ajouter une action **Ouvrir l'URL**
2. URL : `iconnect://` **Rénover les appareils à proximité après avoir joint le Wi-Fi**


```
iconnect://devices?refresh=1
```


Utilisez **Ouvrir l'URL** dans une automatisation personnelle (p. ex. quand Wi‐Fi se connecte) pour sauter à la découverte et à la recherche.

---

## Comportement de lancement

Lorsque iConnect reçoit une URL (démarrage froid ou en cours d'exécution):

1. Le lien est analysé par `iconnect://` .
2. L'onglet s'allume immédiatement; **share**, **feedback** et **review** s'ouvre après un court délai (~0,4 s sur iOS) pour que l'interface utilisateur puisse terminer le montage.
3. **Feedback** utilise le courrier dans l'application lorsque disponible; sinon ouvre le client de messagerie par défaut via `iconnect://` .
4. **Share** sur Mac utilise le sélecteur de partage système; sur iOS il présente une feuille de partage.

---

## Dépannage

| Issue | Quoi vérifier |
|-------|----------------|
| Link does nothing | Assurez-vous que iConnect est installé; l'hôte doit correspondre à un nom supporté ci-dessus |
| `feedback` opens Mail only | Aucun compte Mail configuré sur l'appareil — retour prévu |
| `shortcuts` has no effect on Mac | Home Screen raccourci personnalisation est **iOS-seulement** |
| URL does not connect to a device | Les liens profonds ne naviguent que — utilisez l'onglet Appareils pour découvrir les pairs manuellement |

---

[Retour à iConnect Support](..) · [FAQ](../faq) · [Politique de confidentialité](../privacy)


