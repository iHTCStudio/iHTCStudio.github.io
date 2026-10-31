Antworten spiegeln **aktuelles App-Verhalten** (wiederherstellbare Pause/Fortsetzung, Export-Warteschlange, Live Activity, Geräte-Gate, 繁體中文, In-App-Anleitungen). Schritt-für-Schritt: [Benutzerhandbuch](index).

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
