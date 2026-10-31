Les réponses reflètent le **comportement actuel de l’app** (pause/reprise récupérable, file d’export, Live Activity, contrôle appareil, 繁體中文, guides in-app). Guide pas à pas : [Guide utilisateur](index).

---

## Appareil et exigences

### Quels iPhone prennent en charge TwinPolarCam ?

TwinPolarCam requiert **`AVCaptureMultiCamSession`** — l’API Apple multi-caméra simultanée. Prise en charge typique : **iPhone XS, iPhone XR et modèles ultérieurs** ; les capacités exactes dépendent du matériel.

- **Appareils non pris en charge** : écran dédié au lancement — pas d’UI caméra ni de flux de permissions.
- **Simulateur iOS non pris en charge** — pas de caméras physiques ni Multi-Cam.
- **iPhone réel** requis.

### Pourquoi pas de repli mono-caméra ?

L’enregistrement dual simultané est le cœur du produit. Le repli mono a été retiré pour éviter la confusion. Échec du test : **remboursement** sur l’écran non pris en charge ou support.

### Résolution maximale ?

**720p, 1080p, 2K et 4K** par caméra (main et PiP indépendamment). Maximum selon l’appareil :

- **iPhone 12 et plus** — dual 4K en général disponible.
- **Anciens Multi-Cam** — plafond 1080p ou 2K sur une ou deux lentilles.

Résolutions indisponibles **désactivées automatiquement** dans les réglages.

### Pourquoi pas 60 fps ?

Le pipeline Multi-Cam Apple limite souvent à **30 fps max** en enregistrement simultané. TwinPolarCam propose **24 et 30 fps**. **60 fps non pris en charge** — contrainte système/matériel.

### iPad ou Mac ?

**Non.** TwinPolarCam est **iPhone uniquement**.

### Version iOS ?

- **Minimum : iOS 15.0**
- **Live Activity : iOS 16.2+**
- **Extension widget** (UI Live Activity) : incluse, mêmes exigences OS

---

## Enregistrement et PiP

### Changer la caméra principale ?

Appuyez sur **basculer/retourner** en prévisualisation ou enregistrement. Les rôles avant/arrière **s’échangent à l’écran** — les deux pistes continuent.

### Personnaliser le PiP ?

Oui : **glisser**, **pincer**, réglages **App → Picture-in-Picture** (bordure, couleur, coins, opacité, taille). **Gravé à l’export**.

### Position PiP à l’export ?

**Oui** — échelle, position normalisée, coins, bordure, opacité sauvegardés.

### Portrait ?

UI **optimisée paysage** ; verrou portrait pour Réglages/Pending possible ; dual preview/enregistrement **horizontal** de préférence.

### Pause aperçu ?

Gèle la **prévisualisation live** (pas l’enregistrement). **Indisponible pendant enregistrement actif** — utilisez **pause enregistrement**.

### Presets zoom ?

Pincer puis **enregistrer le niveau** ; zoom sur **main hors enregistrement**.

### Bouton capture ?

**Main + PiP** → **Photos**, prévisualisation ou enregistrement.

### Lampe torche ?

Quand **arrière = main** ; en enregistrement **remplace** le bouton bascule.

---

## Interruptions et fiabilité

### Appel pendant enregistrement ?

**Pause** ; fin d’appel **reprise du même segment** (`.mov`) sauf pause manuelle avant l’appel. Temps de pause **coupé** de la timeline.

### Centre de contrôle ?

**Non** — seulement **arrière-plan complet** (Accueil, changement d’app, verrouillage).

### Changement d’app ou verrouillage ?

1. **Pause** 2. Tâche arrière-plan 3. **Live Activity** optionnelle 4. **~25 s** → **Pending** 5. **Avant timeout** : **reprise même segment**.

### Sauvegarde d’urgence ?

Finalisation si écriture impossible (~25 s fond, ~8 s fin app, erreur writer). **Toast**, clips **Pending**, **session terminée**.

### Récupérable vs fatal ?

| Type | Exemples | Résultat |
|------|----------|--------|
| **Récupérable** | Appel, Siri, vol caméra bref, fond | Pause → **même segment** |
| **Fatal** | Reset média, erreur, disque plein | **Pending**, fin session |

### Pause = trou dans la vidéo ?

**Oui** — intervalles **omis** (jump-cut PTS).

### Récupération après crash ?

Segments valides sur disque ; au relancement **Pending** + alerte ; **Rescan Cache** si besoin.

### Écran toujours allumé ?

Enregistrement **force éveil** ; file d’export aussi.

### Mode économie d’énergie ?

Peut augmenter pression arrière-plan et throttling.

---

## Live Activity

### Recording Live Activity ?

**iOS 16.2+** : widget **écran verrouillé / Dynamic Island** — **Background waiting** / **Saved**.

### Désactiver ?

**Réglages app → Général → Recording Live Activity**.

### Reste après auto-save ?

Peut afficher **Saved** jusqu’au retour au premier plan.

---

## Export et Pending

| Mode | Comportement |
|------|----------|
| **Auto Export ON** | Stop → Photos immédiat |
| **OFF** | `.mov` dans **Pending** |

File **sérieille**, plus ancien d’abord. **Annulation** possible ; **`.mov` conservés**. Seulement **`TwinPolarCam_*.mov`**. Re-export PiP si **Auto-Delete Original** **off**. 4K dual = lent ; échec export → clip **pas perdu**. Stockage : `Application Support/...` **hors backup iCloud**. **H.264/AAC mp4**.

---

## Réglages et langue

**English / 简体中文 / 繁體中文**. **Auto-Delete Original** : ON supprime `.mov` après succès ; OFF (défaut) garde la source. Musique pausée **uniquement** à l’enregistrement. Apparence **System / Light / Dark**.

---

## Autorisations et confidentialité

**Aucune collecte.** [Confidentialité](../privacy). Photos **Ajout uniquement**. Originaux app **hors sauvegarde** ; Photos selon **votre** iCloud.

---

## Astuces et support

**Send Feedback**, **Help**, `twinpolarcam://`, [Shortcut Links](../url-scheme). [AppleOSer@gmail.com](mailto:AppleOSer@gmail.com).

[Guide](index) · [Liens](../url-scheme) · [Confidentialité](../privacy)

---

## Guide complet

| Partie | Sujet |
|------|--------|
| [Part 1](#part-1) | Premier lancement, permissions |
| [Part 2](#part-2) | Contrôles |
| [Part 3](#part-3) | Caméra & PiP |
| [Part 4](#part-4) | Audio |
| [Part 5](#part-5) | Session |
| [Part 6](#part-6) | Fiabilité |
| [Part 7](#part-7) | Export |
| [Part 8](#part-8) | Général |
| [Part 9](#part-9) | Aide |
| [Part 10](#part-10) | Dépannage |

---

## Part 1 — Premier lancement {#part-1}

Onboarding 6 pages ; permissions Caméra / Micro / Photos Add Only ; Multi-Cam **XS/XR+** ; iOS **15.0+** ; pas de repli mono-caméra.

---

## Part 2 — Écran principal {#part-2}

Paysage ; Record, Pause, Stop, Switch, Screenshot, Flashlight, Preview pause, Settings/Pending.

---

## Part 3 — Caméra & PiP {#part-3}

720p–4K, 24/30 fps, PiP stylé **dans l’export**.

---

## Part 4 — Audio {#part-4}

Qualité, AAC/PCM ; session active au **Record** seulement.

---

## Part 5 — Session {#part-5}

Workflow ; timer = temps effectif ; `.mov` multi-piste.

---

## Part 6 — Fiabilité {#part-6}

Interruption Coordinator ; ~25 s fond ; Live Activity.

---

## Part 7 — Export {#part-7}

`MultiCamVideoComposer` ; file sérieille ; Pending.

---

## Part 8 — Général {#part-8}

Apparence, Live Activity, langues, reset.

---

## Part 9 — Aide {#part-9}

Guides, Spotlight, deep links.

---

## Part 10 — Dépannage {#part-10}

| Symptôme | Cause | Action |
|---------|--------------|------------|
| Écran noir | Simulateur / non pris en charge | iPhone Multi-Cam réel |
| Export échoué | Stockage / Photos | Espace ; permission Ajout |
| Pending après verrou | ~25 s save | Exporter depuis Pending |
| PiP incorrect | Réglages après prise | Re-export, Auto-Delete off |
| Liste vide | Index | **Rescan Cache** |

**Send Feedback** ou e-mail.

---
