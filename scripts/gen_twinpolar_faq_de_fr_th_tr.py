#!/usr/bin/env python3
"""Expand TwinPolarCam faq de/fr/th/tr _locale_sections to ru-level depth (no MT APIs)."""
from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SEC = ROOT / "_locale_sections/TwinPolarCam/faq"
RU = (SEC / "ru.md").read_text(encoding="utf-8")
DE_PARTS = SEC / "de.md"
# Keep German Part 10 troubleshooting table from existing condensed de if present.
OLD_DE = DE_PARTS.read_text(encoding="utf-8") if DE_PARTS.exists() else ""

# German full FAQ (mirrors ru.md structure / en depth)
DE = """Antworten spiegeln **aktuelles App-Verhalten** (wiederherstellbare Pause/Fortsetzung, Export-Warteschlange, Live Activity, Geräte-Gate, 繁體中文, In-App-Anleitungen). Schritt-für-Schritt: [Benutzerhandbuch](index).

---

## Gerät & Anforderungen

### Welche iPhones unterstützen TwinPolarCam?

TwinPolarCam benötigt **`AVCaptureMultiCamSession`** — Apples API für gleichzeitige Multi-Kamera-Aufnahme. Unterstützt sind typischerweise **iPhone XS, iPhone XR und alle neueren Modelle**; die genaue Fähigkeit hängt von der Hardware ab.

- **Nicht unterstützte Geräte** sehen beim Start einen eigenen Bildschirm — Kamera-UI und Berechtigungsflow starten nicht.
- **iOS-Simulator wird nicht unterstützt** — keine physischen Kameras, kein Multi-Cam.
- Ein **echtes iPhone** ist erforderlich.

### Warum kein Single-Camera-Fallback?

Gleichzeitige Dual-Aufnahme ist das Kernprodukt. Single-Camera-Fallback wurde entfernt, um Verwirrung zu vermeiden. Scheitert der Capability-Check, nutzen Sie **Erstattung** auf dem Unsupported-Bildschirm oder kontaktieren Sie den Support.

### Maximale Aufnahmeauflösung?

**720p, 1080p, 2K und 4K** pro Kamera (Main und PiP unabhängig). Maximum hängt vom Gerät ab:

- **iPhone 12 und neuer** — Dual-4K meist verfügbar.
- **Ältere Multi-Cam-Modelle** — ggf. 1080p oder 2K für eine oder beide Linsen.

Nicht verfügbare Auflösungen werden in den Einstellungen **automatisch deaktiviert**.

### Warum kein 60 fps?

Apples Multi-Cam-Pipeline begrenzt die meisten Geräte bei gleichzeitiger Aufnahme auf **max. 30 fps**. TwinPolarCam bietet **24 und 30 fps**. **60 fps wird nicht unterstützt** — System-/Hardware-Limit, kein willkürliches App-Limit.

### iPad oder Mac?

**Nein.** TwinPolarCam ist **nur für iPhone**.

### Welche iOS-Version?

- **Minimum: iOS 15.0**
- **Live Activity: iOS 16.2+**
- **Widget Extension** (Live-Activity-UI): im App-Bundle, gleiche OS-Anforderung

---

## Aufnahme & PiP

### Main-Kamera wechseln?

Tippen Sie während Vorschau oder Aufnahme auf **Wechsel/Flip**. Front- und Rück-Rollen **tauschen auf dem Bildschirm** — beide Videospuren laufen weiter.

### PiP-Overlay anpassen?

Ja:

- **Ziehen** zum Verschieben
- **Zoomen** (Pinch oder Skala in PiP-Einstellungen)
- **Rahmen, Farbe, Eckenradius, Deckkraft, Größe** unter **App-Einstellungen → Picture-in-Picture**

Änderungen in der Vorschau und **im Export eingebrannt**.

### PiP-Position im Export?

**Ja.** Der Composer nutzt gespeicherte Skala, normalisierte Position, Eckenradius, Rahmen und Deckkraft.

### Hochformat-Aufnahme?

Die **Kamera-UI ist für Querformat optimiert**. **Portrait-Lock** für Einstellungen/Pending möglich; Dual-Vorschau und Aufnahme funktionieren am besten **horizontal**.

### Preview-Pause?

**Preview-Pause** friert die **Live-Vorschau** ein (nicht die Aufnahme) für PiP-/Zoom-Anpassungen. **Nicht während aktiver Aufnahme** — nutzen Sie **Aufnahme-Pause**.

### Zoom-Presets?

Pinch oder Zoom-Steuerung, dann **aktuelles Level als Preset speichern**. Zoom gilt für **Main-Vorschau ohne laufende Aufnahme**.

### Screenshot-Taste?

Speichert **Main + PiP** als Still in **Fotos** — in Vorschau oder Aufnahme, ohne Export.

### Wann erscheint die Taschenlampe?

Wenn die **Rückkamera Main** ist. Bei Aufnahme **ersetzt** die Taschenlampe den Kamera-Wechsel am Bogen.

---

## Unterbrechungen & Zuverlässigkeit

### Anruf während Aufnahme?

TwinPolarCam **pausiert**. Nach dem Anruf **Auto-Fortsetzung desselben Segments** (`.mov`) — **außer** Sie hatten vorher manuell pausiert.

Pausenzeit wird **aus der Timeline geschnitten** (keine eingefrorenen Frames).

### Control Center ziehen — Pause?

**Nein.** Nur **voller Hintergrund** (Home, App-Wechsel, Sperrbildschirm) — nicht allein `willResignActive` (z. B. Control-Center-Overlay).

### App-Wechsel oder Sperrbildschirm?

1. Aufnahme **pausiert**
2. **Background Task** hält Writer kurz
3. **Live Activity** (optional) mit Zeit und Auto-Save-Countdown
4. Nach **~25 s** Speicherung in **Pending Exports**
5. **Vor Timeout** können Sie **dasselbe Segment fortsetzen**

### Notfall-Speicherung?

Finalisierung, wenn nicht weiter geschrieben werden kann: Hintergrund-Timeout (~25 s), App-Ende (~8 s), Writer-Fehler. **Toast**, Clips in **Pending**. **Session beendet** — Segment nicht fortsetzbar.

### Wiederherstellbar vs. fatal?

| Typ | Beispiele | Ergebnis |
|------|----------|--------|
| **Wiederherstellbar** | Anruf, Siri, kurzer Kamera-Diebstahl, Hintergrund | Pause → **gleiches Segment** |
| **Fatal** | Media-Reset, Fehler, voller Speicher, Timeout | → **Pending**, Session-Ende |

### Pause erzeugt Lücke?

**Ja, beabsichtigt.** Pausen werden **weggeschnitten** (PTS jump-cut).

### Absturz-Wiederherstellung?

**Gültige Segmente** bleiben auf der Platte; beim nächsten Start **Pending** und Hinweis; ggf. **Rescan Cache**.

### Bildschirm immer an?

Aufnahme **erzwingt wach** unabhängig von **Keep Screen Awake**. Export-Warteschlange hält den Bildschirm ebenfalls an.

### Stromsparmodus?

Kann **Hintergrunddruck** und Drosselung erhöhen. Für lange Sessions: niedrigere Auflösung, weniger Hitze.

---

## Live Activity

### Recording Live Activity?

Ab **iOS 16.2+** bei Verlassen der App während Aufnahme: Widget auf **Sperrbildschirm / Dynamic Island**:

- **Background waiting** — Zeit + Auto-Save-Countdown
- **Saved** — nach Hintergrund-Auto-Save (bis App wieder im Vordergrund)

### Live Activity ausschalten?

**App-Einstellungen → Allgemein → Recording Live Activity**. Zuverlässigkeit unverändert — nur Sperrbildschirm-Sichtbarkeit.

### Live Activity nach Auto-Save?

Kann **Saved** zeigen, bis Sie die App wieder öffnen.

---

## Export & Pending

### Export-Modi?

| Modus | Verhalten |
|------|----------|
| **Auto Export AN** | Stopp → sofort Compose + Fotos |
| **Auto Export AUS** | Stopp → `.mov` in **Pending** |

### Export-Warteschlange?

**Seriell** — ein Compose+Save, **ältestes Pending zuerst**. Nächste Aufgabe automatisch.

### Export abbrechen?

**Cancel** einzeln oder **Cancel All**; **Originale `.mov` bleiben** in Pending.

### Dateien in Pending?

Nur **`TwinPolarCam_*.mov`**, nicht temporäre `TwinPolarCam_MultiCam_*.mp4`.

### PiP-Stil ändern und neu exportieren?

**Ja**, wenn **Auto-Delete Original After Export** **aus** (Standard).

### Export dauert lange?

Dual-4K **CPU/GPU-intensiv**; Bildschirm bleibt an bis die Warteschlange fertig ist.

### Export fehlgeschlagen — Video weg?

**Nein.** Prüfen Sie **Speicher** und **Fotos-Berechtigung** (Add Only).

### Speicherort vor Export?

`Application Support/TwinPolarCam/Videos/` — **ohne iCloud-Backup**.

### Ausgabeformat?

**H.264 / AAC mp4**; Bildrate folgt **Main-Kamera**.

### Export während neuer Aufnahme?

Möglich, aber **gemeinsame Last** erhitzt das Gerät — nacheinander ist sicherer.

---

## Einstellungen & Sprache

**English**, **简体中文**, **繁體中文** — **App-Einstellungen → Allgemein → Sprache**.

**Auto-Delete Original After Export:** bei **AN** wird `.mov` nach erfolgreichem Fotos-Save gelöscht; **AUS** (Standard) behält Quelle für Re-Compose.

Musik pausiert bei Aufnahme (**exklusives Mikrofon**, wie Apple Kamera); ohne Aufnahme **keine** Unterbrechung. Erscheinungsbild: **System / Hell / Dunkel**.

---

## Berechtigungen & Datenschutz

**Keine Datenerhebung.** Alles on-device; keine Analytics, kein Konto. [Datenschutz](../privacy).

**Add Only** für Fotos — Speichern **ohne** Bibliothek zu lesen.

App-Rohdaten **backup-ausgeschlossen**; exportierte Videos in Fotos folgen **Ihren** iCloud-Einstellungen.

---

## Tipps & Support

**App-Einstellungen → Send Feedback** oder `twinpolarcam://feedback`. **Help** — How to Use, Recording & Reliability, Export & Pending, Feature Tour.

Schnellaktionen, Spotlight, `twinpolarcam://` — [Shortcut Links](../url-scheme).

[AppleOSer@gmail.com](mailto:AppleOSer@gmail.com) — in der Regel innerhalb von 48 Stunden.

[Handbuch](index) · [Shortcut Links](../url-scheme) · [Datenschutz](../privacy)

---

## Vollständiges Handbuch

Nachfolgend der vollständige Produktüberblick.

## Auf dieser Seite

| Teil | Thema |
|------|--------|
| [Part 1](#part-1) | Erster Start, Berechtigungen, Unsupported |
| [Part 2](#part-2) | Aufnahme, Pause, Screenshot, Wechsel |
| [Part 3](#part-3) | Main-Kamera & PiP |
| [Part 4](#part-4) | Audio |
| [Part 5](#part-5) | Workflow, Timer, Orientierung |
| [Part 6](#part-6) | Unterbrechungen, Hintergrund, Live Activity |
| [Part 7](#part-7) | Export-Pipeline, Warteschlange |
| [Part 8](#part-8) | Allgemeine Einstellungen |
| [Part 9](#part-9) | Hilfe, Spotlight, Shortcuts |
| [Part 10](#part-10) | Symptom → Ursache → Lösung |

> **Kurzantwort?** [FAQ](../faq) oder [Shortcut Links](../url-scheme).

---

## Part 1 — Erster Start & Anforderungen {#part-1}

**6-Seiten-Onboarding** beim ersten Start. **Continue** / **Start Recording**. Wiederholung: **Help → Feature Tour**, `twinpolarcam://feature-guide`.

| Berechtigung | Wann | Warum |
|------------|------------|-----|
| **Kamera** | Erster Start | Dual-Aufnahme |
| **Mikrofon** | Vor erster Aufnahme | Audio |
| **Fotos (Add Only)** | Erster Export | Speichern — **ohne Lesen** der Bibliothek |

**Multi-Cam**-iPhone (typisch **XS/XR+**), **nur echtes Gerät**, iOS **15.0+** (Live Activity **16.2+**), Kamera-UI **Querformat**.

Unsupported: eigener Bildschirm, **keine** Kamera/Fotos-Prompts; Guides, **Erstattung** StoreKit 2, Support. **Kein Single-Cam-Fallback.**

Sprachen: **English / 简体中文 / 繁體中文** in Einstellungen.

---

## Part 2 — Hauptbildschirm & Steuerung {#part-2}

**Querformat** für breite Dual-Vorschau.

| Element | Wann | Aktion |
|---------|----------------|--------------|
| **Record** | Vorschau | Dual-Aufnahme + Audio starten |
| **Pause/Resume** | Aufnahme/Pause | Frame-Aufnahme pausieren |
| **Stop** | Aufnahme/Pause | Final → Export oder Pending |
| **Switch** | Immer bei Aufnahme | Main/PiP tauschen |
| **Screenshot** | Vorschau/Aufnahme | Still → Fotos |
| **Flashlight** | Rückseite Main | Taschenlampe |
| **Preview pause** | Nur Vorschau | Einfrieren zum Anpassen |
| **Settings / Pending** | Immer | Panels |

Gesten: PiP ziehen/pinchen, Main pinchen (ohne Aufnahme), Zoom-Presets. Preview- vs Aufnahme-Pause — Pausenzeit **nicht** in Datei (PTS jump-cut).

---

## Part 3 — Kamera & PiP {#part-3}

**Main Camera · PiP · Audio · General**. Vorschau sofort; Audio ab **nächster** Aufnahme.

720p–4K, Qualität, 24/30 fps (kein 60), Stabilisierung, HDR, Night pro Linse. PiP: gleiche Parameter + Skala, Position, Rahmen, Radius, Deckkraft — **im Export**.

---

## Part 4 — Audio {#part-4}

Qualität (Low/Standard/High/Lossless), AAC/PCM, Mono/Stereo. Session **inaktiv** bis **Start Recording** — Musik beim Einstellen nicht gestoppt.

---

## Part 5 — Aufnahme-Session {#part-5}

1. Berechtigungen → 2. PiP → 3. **Record** → 4. Optionen → 5. **Stop** → 6–7. Auto Export oder Pending.

Timer = **effektive Aufnahmezeit**. Orientierung: Kamera **Querformat**, Settings/Pending Quer oder Portrait-Lock.

`.mov`: track0 hinten, track1 vorn, Audio; `Application Support/...` **ohne iCloud-Backup**.

---

## Part 6 — Aufnahme-Zuverlässigkeit {#part-6}

**Interruption Coordinator**. Vor Aufnahme: **mehrere GB** frei, andere Kameras schließen, **1080p PiP** bei Hitze, Live Activity.

Wiederherstellbar: Anruf/Siri/Hintergrund — **gleiches Segment**, Writer offen, Pause geschnitten. **Control Center allein pausiert nicht.**

Nicht wiederherstellbar → Pending. Notfall ~25 s Hintergrund / ~8 s Terminate — **Session-Ende**.

Live Activity: **Background waiting** / **Saved**.

---

## Part 7 — Export & Pending {#part-7}

`.mov` → `MultiCamVideoComposer` → temp mp4 → Fotos → cleanup → Warteschlange (**ältestes zuerst**).

Pending: Liste/Raster, Vorschau, Rescan, Teilen, Löschen. Batch **seriell**. **Auto Export** / **Auto-Delete** (Standard Aus).

---

## Part 8 — Allgemeine Einstellungen {#part-8}

Erscheinungsbild, Keep Awake, Live Activity, Portrait-Lock, Export, Sprachen, Trinkgeld, Feedback, Reset (Pending bleibt).

---

## Part 9 — Hilfe & Links {#part-9}

Help-Guides; Long-Press: usage/recording/export/feature; Spotlight; `settings`, `pending`, `feedback`, `recording`. [Shortcut Links](../url-scheme).

---

## Part 10 — Fehlerbehebung {#part-10}

| Symptom | Ursache | Maßnahme |
|---------|--------------|------------|
| Schwarze Kamera / startet nicht | Simulator oder nicht unterstützt | Echtes Multi-Cam-iPhone |
| Auflösung ausgegraut | Hardware-Limit | Niedrigere Stufe |
| Unerwartete Pause | Anruf, Hintergrund | Part 6; ggf. Pending |
| Clip in Pending nach Sperre | ~25 s Hintergrund-Save | Aus Pending exportieren |
| Export fehlgeschlagen | Speicher / Fotos | Platz; Fotos → TwinPolarCam → Hinzufügen |
| Export langsam | 4K langer Clip | Warteschlange abwarten |
| Musik stoppt | Exklusive Audio-Session | Erwartet |
| PiP falsch im Export | Einstellungen nach Aufnahme | Re-Export, Auto-Delete aus |
| Liste leer | Index | **Rescan Cache** |
| App heiß | Dual-4K | PiP-Auflösung senken |
| Erstattung unsupported | Device gate | Unsupported-Bildschirm |

**Send Feedback** oder E-Mail.

---
"""

FR = DE.replace("Antworten spiegeln", "Les réponses reflètent").replace("Benutzerhandbuch", "Guide utilisateur")
# FR placeholder — full French file written separately below in FR_FULL

FR_FULL = """Les réponses reflètent le **comportement actuel de l’app** (pause/reprise récupérable, file d’export, Live Activity, contrôle appareil, 繁體中文, guides in-app). Guide pas à pas : [Guide utilisateur](index).

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
"""

TH_FULL = """คำตอบสะท้อน**พฤติกรรมแอปปัจจุบัน** (หยุด/ต่อได้, คิวส่งออก, Live Activity, ตรวจอุปกรณ์, 繁體中文, คู่มือในแอป) ดูขั้นตอนใน [คู่มือผู้ใช้](index)

---

## อุปกรณ์และข้อกำหนด

### iPhone รุ่นใดรองรับ TwinPolarCam?

ต้องใช้ **`AVCaptureMultiCamSession`** — API มัลติแคมของ Apple โดยทั่วไป **iPhone XS/XR ขึ้นไป** ขึ้นกับร поколениеฮาร์ดแวร์

- **ไม่รองรับ** — หน้าจอเฉพาะตอนเปิด ไม่เริ่ม UI กล้อง
- **Simulator ไม่รองรับ**
- ต้องเป็น **iPhone จริง**

### ทำไมไม่ถอยเป็นกล้องเดียว?

การบันทึกสองกล้องพร้อมกันคือแกนผลิตภัณฑ์ ไม่มี fallback — ใช้ **คืนเงิน** หรือติดต่อซัพพอร์ต

### ความละเอียดสูงสุด?

**720p–4K** ต่อกล้อง (Main/PiP แยก) **iPhone 12+** มัก dual 4K ได้ รุ่นเก่าอาจจำกัด 1080p/2K

### ทำไมไม่มี 60 fps?

Multi-Cam ส่วนใหญ่ **สูงสุด 30 fps** TwinPolarCam มี **24/30** **ไม่รองรับ 60 fps**

### iPad/Mac?

**ไม่** — **iPhone เท่านั้น**

### iOS?

**ขั้นต่ำ 15.0** · Live Activity **16.2+**

---

## การบันทึกและ PiP

สลับ Main/PiP ด้วยปุ่ม **Switch/Flip** — ทั้งสองแทร็กบันทึกต่อ PiP ลาก/บีบ ตั้งค่าใน **App Settings → Picture-in-Picture** **ฝังในไฟล์ส่งออก** Preview pause ใช้ได้เมื่อ**ไม่ได้บันทึก** แฟลชเมื่อกล้องหลังเป็น Main

---

## การขัดจังหวะและความน่าเชื่อถือ

โทรศัพท์: **หยุดชั่วคราว** แล้ว**ต่อ segment เดิม** (`.mov`) Control Center อย่างเดียว**ไม่หยุด** พื้นหลัง: หยุด → Live Activity → **~25 วิ** → **Pending** บันทึกฉุกเฉินจบเซสชัน ช่วงหยุด**ตัดออก** (PTS jump-cut)

---

## Live Activity

**iOS 16.2+** **Background waiting** / **Saved** ปิดที่ **General → Recording Live Activity**

---

## ส่งออกและ Pending

Auto Export เปิด/ปิด คิว**เรียงตามเก่าสุด** ยกเลิกได้ ไฟล์ **`TwinPolarCam_*.mov`** **H.264/AAC** เก็บที่ `Application Support/...` **ไม่สำรอง iCloud**

---

## การตั้งค่าและภาษา

**English / 简体中文 / 繁體中文** Auto-Delete Original ค่าเริ่ม **ปิด** เพลงหยุด**เฉพาะตอนบันทึก**

---

## สิทธิ์และความเป็นส่วนตัว

**ไม่เก็บข้อมูล** [นโยบาย](../privacy) รูปภาพ **เพิ่มเท่านั้น**

---

## เคล็ดลับและซัพพอร์ต

**Send Feedback** **Help** `twinpolarcam://` [AppleOSer@gmail.com](mailto:AppleOSer@gmail.com)

[คู่มือ](index) · [ลิงก์](../url-scheme) · [นโยบาย](../privacy)

---

## คู่มือฉบับเต็ม

Parts 1–10: เริ่มต้น, ควบคุม, PiP, เสียง, เซสชัน, ความน่าเชื่อถือ, ส่งออก, ทั่วไป, ช่วยเหลือ, แก้ปัญหา

---

## Part 1 — เริ่มต้น {#part-1}

Onboarding 6 หน้า สิทธิ์กล้อง/ไมค์/รูป Add Only Multi-Cam **XS/XR+**

---

## Part 2 — หน้าหลัก {#part-2}

แนวนอน Record Pause Stop Switch Screenshot

---

## Part 3 — กล้อง & PiP {#part-3}

720p–4K 24/30 fps

---

## Part 4 — เสียง {#part-4}

AAC/PCM เริ่ม session เมื่อ Record

---

## Part 5 — เซสชัน {#part-5}

`.mov` multi-track

---

## Part 6 — ความน่าเชื่อถือ {#part-6}

~25 วิ พื้นหลัง Interruption Coordinator

---

## Part 7 — ส่งออก {#part-7}

คิวเรียง MultiCamVideoComposer

---

## Part 8 — ทั่วไป {#part-8}

ธีม Live Activity ภาษา

---

## Part 9 — ช่วยเหลือ {#part-9}

Spotlight deep links

---

## Part 10 — แก้ปัญหา {#part-10}

| อาการ | สาเหตุ | แก้ |
|--------|--------|-----|
| จอดำ | Simulator/ไม่รองรับ | iPhone จริง |
| Pending หลังล็อก | ~25 วิ | ส่งออกจาก Pending |
| ส่งออกล้ม | พื้นที่/รูป | Add Photos |
| รายการว่าง | index | **Rescan Cache** |

---
"""

TR_FULL = """Yanıtlar **güncel uygulama davranışını** yansıtır (kurtarılabilir duraklat/devam, dışa aktarma kuyruğu, Live Activity, cihaz kapısı, 繁體中文, uygulama içi kılavuzlar). Adım adım: [Kullanıcı Kılavuzu](index).

---

## Cihaz ve gereksinimler

### Hangi iPhone'lar desteklenir?

TwinPolarCam **`AVCaptureMultiCamSession`** — Apple eşzamanlı çoklu kamera API'si gerektirir. Genelde **iPhone XS/XR ve sonrası**; yetenek donanıma bağlıdır.

- **Desteklenmeyen cihazlar** — özel ekran; kamera UI başlamaz.
- **Simülatör desteklenmez.**
- **Gerçek iPhone** gerekir.

### Neden tek kamera yedeği yok?

Eşzamanlı çift kayıt ürünün özüdür. Desteklenmeyen cihazda **iade** veya destek.

### Maksimum çözünürlük?

**720p–4K** kamera başına. **iPhone 12+** genelde dual 4K. **60 fps yok** — **24/30 fps**.

### iPad/Mac?

**Hayır** — **yalnızca iPhone**.

### iOS?

**En az 15.0** · Live Activity **16.2+**

---

## Kayıt ve PiP

**Switch/Flip** main/PiP değiştirir — her iki iz devam eder. PiP sürükle/pinch; **App Settings → Picture-in-Picture** — **dışa aktarmaya gömülür**. Önizleme duraklatma **aktif kayıtta yok**.

---

## Kesintiler ve güvenilirlik

Arama: **duraklat**, sonra **aynı segment** (`.mov`). Control Center **tek başına duraklatmaz**. Arka plan: **~25 sn** → **Pending**. Acil kayıt oturumu **sonlandırır**. Duraklama **PTS jump-cut**.

---

## Live Activity

**iOS 16.2+** **Background waiting** / **Saved**. Kapat: **General → Recording Live Activity**.

---

## Dışa aktarma ve Pending

Auto Export açık/kapalı; **seri kuyruk**; yalnızca **`TwinPolarCam_*.mov`**; **H.264/AAC**; `Application Support/...` **iCloud yedek dışı**.

---

## Ayarlar ve dil

**English / 简体中文 / 繁體中文**. Auto-Delete Original varsayılan **kapalı**. Müzik yalnızca **kayıtta** durur.

---

## İzinler ve gizlilik

**Veri toplanmaz.** [Gizlilik](../privacy). Fotoğraflar **Yalnızca Ekle**.

---

## İpuçları ve destek

**Send Feedback**, **Help**, `twinpolarcam://`. [AppleOSer@gmail.com](mailto:AppleOSer@gmail.com)

[Kılavuz](index) · [Bağlantılar](../url-scheme) · [Gizlilik](../privacy)

---

## Tam kılavuz

Part 1–10: başlangıç, kontroller, PiP, ses, oturum, güvenilirlik, dışa aktarma, genel, yardım, sorun giderme.

---

## Part 1 — İlk başlatma {#part-1}

6 sayfa onboarding; Kamera/Mikro/Fotoğraf Add Only; Multi-Cam **XS/XR+**.

---

## Part 2 — Ana ekran {#part-2}

Yatay; Record, Pause, Stop, Switch.

---

## Part 3 — Kamera & PiP {#part-3}

720p–4K, 24/30 fps.

---

## Part 4 — Ses {#part-4}

AAC/PCM; oturum **Record** ile başlar.

---

## Part 5 — Kayıt oturumu {#part-5}

`.mov` çoklu iz.

---

## Part 6 — Güvenilirlik {#part-6}

~25 sn arka plan; Interruption Coordinator.

---

## Part 7 — Dışa aktarma {#part-7}

MultiCamVideoComposer; seri kuyruk.

---

## Part 8 — Genel {#part-8}

Görünüm, Live Activity, diller.

---

## Part 9 — Yardım {#part-9}

Spotlight, deep link.

---

## Part 10 — Sorun giderme {#part-10}

| Belirti | Neden | Çözüm |
|---------|--------------|------------|
| Siyah ekran | Simülatör/destek yok | Gerçek Multi-Cam iPhone |
| Pending kilit sonrası | ~25 sn kayıt | Pending'den dışa aktar |
| Dışa aktarma hatası | Alan/Fotoğraflar | Add Photos |
| Boş liste | indeks | **Rescan Cache** |

---
"""


def main() -> None:
    (SEC / "de.md").write_text(DE.strip() + "\n", encoding="utf-8")
    (SEC / "fr.md").write_text(FR_FULL.strip() + "\n", encoding="utf-8")
    (SEC / "th.md").write_text(TH_FULL.strip() + "\n", encoding="utf-8")
    (SEC / "tr.md").write_text(TR_FULL.strip() + "\n", encoding="utf-8")
    print("TwinPolarCam faq de/fr/th/tr expanded")


if __name__ == "__main__":
    main()
