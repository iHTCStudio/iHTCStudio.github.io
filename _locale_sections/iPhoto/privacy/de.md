iHTC Studio („wir“, „uns“ oder „unser“) hat iPhoto (auch bekannt als „爱修图“ / „愛修圖“) erstellt. Auf dieser Seite werden unsere Richtlinien in Bezug auf Daten beschrieben, wenn Sie die App nutzen.

## Zusammenfassung

**iPhoto erfordert kein Konto und lädt Ihre Fotos nicht auf iHTC Studio-Server hoch.** Aufnahme, Schönheit, Filter und Export laufen auf Ihrem Gerät. Die optionale **iCloud-Synchronisierung** deckt nur Einstellungen ab – niemals Fotodateien.

## Datenerfassung

Wir betreiben kein Backend, das Ihre persönlichen Daten sammelt:

- **Kein Konto** – Es ist keine Registrierung, E-Mail-Adresse oder Telefonnummer erforderlich.
- **Keine Analysen oder Werbung** – Keine Analysen, Werbung oder Tracking-SDKs von Drittanbietern.
- **Kein Foto-Upload zur Analyse** – Gesichtspunkte und Renderings bleiben auf dem Gerät.

## So funktioniert die App

- **Speicher** – Projekte (Original/Miniaturansicht/Bearbeitungsstatus) leben in der App-Sandbox. Widget-Miniaturansichten verwenden den App-Gruppencontainer.
- **Gesichtsschönheit** – Siehe unten **Gesichtsdaten und Schönheitsverarbeitung auf dem Gerät**.
- **Fotobibliothek** – Der Zugriff ist auf die von Ihnen ausgewählten Importe beschränkt und optionale Exportspeicherungen, die Sie starten.
- **Metadatenstreifen** – Entfernt optional EXIF-/GPS-/Gerätefelder aus den von Ihnen erstellten Exporten.

## Gesichtsdaten und Schönheitsverarbeitung auf dem Gerät

When you use beauty features (Capture live preview, shutter bake, or the editor Beauty tool), iPhoto analyzes faces **only on your device** using Apple’s Vision framework (`VNDetectFaceLandmarksRequest`). This is **not** face recognition, identity matching, biometrics enrollment, or authentication.

### Welche Gesichtsdaten werden verarbeitet?

- **Vorübergehende Orientierungspunkte (nur Speicher):** Gesichtsbegrenzungsrahmen, Gesichtskontur, Augen, Augenbrauen, äußere/innere Lippen, Pupillen und zugehörige Geometrie zum Erstellen von Masken für optionale kosmetische Bearbeitungen (glätten, aufhellen, schlank, Augen, Zähne, Rouge, Lippenstift).
- **Persisted with a project (optional):** a **normalized face bounding rectangle** plus your chosen **beauty strength / color parameters** (`FaceBeautyEdit`), so per-face settings can be restored when you reopen the project. **Full landmark coordinates are not written to disk.**

### Benutzen

Face geometry is used solely to apply the beauty adjustments **you** enable during capture preview, photo capture, editor preview, thumbnail refresh, and export/share. It is not used for advertising, profiling, or identification.

### Teilen

**Gesichtsdaten werden niemals an Dritte weitergegeben.** Sie werden nicht auf iHTC Studio-Server oder eine Cloud-Analyse-API hochgeladen. Die optionale iCloud-Schlüsselwertsynchronisierung deckt **nur Einstellungen** ab (z. B. Sprache, Thema, Umschalten zwischen Beauty-Rezepten) und **synchronisiert keine Fotos oder Gesichtspunkte**.

### Speicherort

- Fotos und Projektbearbeitungsdateien: **App-Sandbox auf Ihrem Gerät**
- Vorübergehende Orientierungspunkte: **Nur RAM** (wird gelöscht, wenn Sie den Editor verlassen / Analyse-Cache leeren)
- Widget-Miniaturansichten: App-Gruppe auf Ihrem Gerät (gerenderte Bilder, keine Orientierungsdatensätze)

### Aufbewahrung und Löschung

- Vorübergehende Orientierungspunkte sind nur während der Verarbeitung vorhanden und werden anschließend verworfen.
- Behaltene Gesichtsfelder und Schönheitsparameter bleiben **nur so lange erhalten, wie Sie das zugehörige Fotoprojekt behalten**.
- **Löschen** Sie ein Projekt, **setzen** Sie Änderungen zurück oder **deinstallieren** Sie die App, um zugehörige Gesichtsmetadaten und lokale Fotos zu entfernen.

### Dritte

Keine. Für alle Gesichtsanalysen und -darstellungen werden Apple Vision und Core Image auf dem Gerät verwendet.

## Auf Ihrem Gerät gespeicherte Daten

| Daten | Wo | Zweck |
|------|-------|---------|
| Fotoprojekte | App-Dokumente | Originale, Daumen, Bearbeitungsstand |
| Metadaten zur Gesichtsschönheit bearbeiten | Projektbearbeitungsstatus (Sandbox) | Nur normalisierte Gesichtsbox + Beauty-Parameter |
| Präferenzen | Benutzerstandards für App-Gruppen | Sprache, Thema, Aufnahme-/Exportoptionen |
| Widget-Schnappschüsse | App-Gruppe | Aktuelle Projekte/Statistiken für Widgets |
| Erfassen Sie das Schönheitsrezept | App-Gruppe (optional merken) | Kraft- und Schönheitsparameter |
| iCloud-Einstellungen | Ihr privates iCloud KVS | Optionale Präferenzsynchronisierung |

## iCloud-Synchronisierung

Optional sync uses Apple's `NSUbiquitousKeyValueStore` for lightweight preferences (appearance, language, export defaults, capture beauty settings, and similar). **Photo files and face landmarks are not synced.** Sync can be turned off in Settings.

## Berechtigungen

| Erlaubnis | Zweck |
|------------|---------|
| Kamera | Registerkarte „Erfassen“. |
| Fotobibliothek (lesen) | Importieren |
| Fotobibliothek (nur hinzufügen) | Optionaler Export in Fotos |
| Mikrofon | Optionaler Ton bei Videoaufnahme mit Ton; Für die Fotoaufnahme ist dies nicht erforderlich |

## In-App-Käufe

Der optionale **Tip Developer** ist ein verbrauchbarer StoreKit-Kauf. Es werden keine Funktionen freigeschaltet und es ist kein separates App-Konto erforderlich.

## Privatsphäre von Kindern

iPhoto erfasst wissentlich keine personenbezogenen Daten von Kindern. Die Kernverarbeitung bleibt auf dem Gerät, ohne iHTC Studio-Datenerfassungs-Backend.

## Haftungsausschluss

iPhoto ist **nicht mit Apple Inc. verbunden**

## Änderungen

Wir können diese Richtlinie auf dieser Seite aktualisieren. Bitte überprüfen Sie es regelmäßig.

## Kontakt

- **E-Mail:** [AppleOSer@gmail.com](mailto:AppleOSer@gmail.com)
