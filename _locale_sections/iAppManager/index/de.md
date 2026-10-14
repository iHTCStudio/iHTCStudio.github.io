**Schneller veröffentlichen. Raus aus dem Browser-Labyrinth.**

iAppManager (爱应用者) ist eine **native App-Store-Connect-Arbeitsstation** für iPhone, iPad und Mac. Melden Sie sich mit einem **API Key** an, speichern Sie Zugangsdaten in der **Keychain** und sprechen Sie **direkt mit Apple** — Versionen, Screenshots, IAP, TestFlight, Zertifikate, Umsatzberichte und Kundenrezensionen an einem Ort. **Kein iHTC-Studio-Konto. Keine Werbung. Kein Analytics-SDK. Kein Drittanbieter-Backend für Ihre ASC-Daten.**

**Auf einen Blick:** Multi-Account-API-Key-Login · App-Liste mit Plattform- und Pipeline-Filtern · Overview-Bereitschafts-Checkliste · Versionen & Review-Einreichungen · Build Upload REST (IPA/PKG) · Metadaten & Medien mit Cross-Locale-Kopie · Custom Product Pages · In-App Events · App Clips · Store-Experimente · Featuring-Nominierungen · Verfügbarkeit & Preise · Altersfreigabe · Barrierefreiheit · App Tags · IAP & Abos · Game Center · TestFlight · Kundenrezensionen · Zertifikate & Geräte · Benutzer & Rollen · Sales-/Finance-/Analytics-Berichte · Webhooks · Widgets & `iappmanager://`-Deep-Links · English / 简体 / 繁體

> Für Indie-Entwickler und kleine Teams, die jede Woche in App Store Connect leben — und einen Schreibtisch wollen, der sich wie eine Mac-App anfühlt, nicht wie ein Tab-Chaos.

## Erste Schritte

1. Erstellen Sie einen **App Store Connect API Key** (Admin oder App Manager empfohlen): App Store Connect → **Users and Access** → **Integrations** → **App Store Connect API** → Key anlegen, **`.p8` einmal** herunterladen, **Issuer ID** + **Key ID** notieren.
2. iAppManager öffnen → Issuer ID / Key ID / PEM einfügen (oder `.p8` wählen) → verifizieren (`GET /v1/apps`). Keys werden in der **Keychain** dieses Geräts gespeichert.
3. Kurzes **Onboarding** abschließen (Zertifikate · Berichte · Widgets · Datenschutz). Guides jederzeit unter **Einstellungen → Hilfe** wiederholen.
4. Unter **My Apps**: **Liste / Raster / Karten**, Favoriten anheften, nach **Plattform** (iOS / macOS / tvOS / visionOS) oder **Status** filtern (im Verkauf · nicht im Verkauf · wartend · in Review · abgelehnt · ausstehende Entwicklerfreigabe).
5. App öffnen → starten in **Overview** (neueste Version/Build, Shortcuts, weiche Checkliste, kürzliche Einreichungen).
6. Release-Pfad: **Versions** → **Build** anhängen → **Metadata / Media** → **Review Detail** → über **Review Submissions** einreichen (oder „sofort senden").
7. **Home-Screen-Widgets** hinzufügen (Account Hub, Apps Pulse, Review Desk, Quick Actions) und `iappmanager://` aus Kurzbefehlen testen.

> In-App-Guides **Release / IAP / TestFlight / Reports** sind einen Tipp entfernt (auch per Deep Link unten).

## Warum Sie es herunterladen sollten

- **Ein nativer Schreibtisch für den gesamten Release** — kein Hin und Her zwischen ASC-Web-Tabs für Versionen, Assets, IAP, TestFlight, Zerts und Berichte.
- **API Key, kein weiteres Passwort-Ritual** — Issuer ID + Key ID + `.p8` in der Keychain; Multi-Account; Konto entfernen löscht den lokalen Key.
- **Builds ohne Transporter hochladen** — WWDC25 **Build Upload REST** für IPA/PKG; dieselbe Pipeline auf iOS (große Dateien weiterhin am liebsten am Mac).
- **Ausführliche Guides in der App** — Release-Bereitschaft, IAP, TestFlight und Berichte erklären harte vs. weiche Checks, bevor Sie einen Review-Zyklus verbrennen.
- **Pipeline auf dem Sperrbildschirm** — Widgets spiegeln im Verkauf / wartend / in Review / abgelehnt / ausstehende Freigabe (gleiche Buckets wie My Apps).
- **Datenschutz durch Architektur** — ASC-Traffic geht an `api.appstoreconnect.apple.com`; iHTC Studio hostet Ihre Apps, Keys oder Berichte nicht.

## Funktionen

### Anmeldung & Konten

- **Nur API Key** (Issuer ID / Key ID / `.p8`) — kein Apple-ID-OAuth in der App
- Keychain-Speicher; **Multi-Account**; Abmelden / Entfernen löscht das lokale Geheimnis
- In-App-Guide **„So erhalten Sie einen API Key"** mit Abbildungen

### My Apps

- **Liste / Raster / Karten** (Standard Liste) mit Spaltensteuerung
- **Anheften** pro Konto; **Plattform-** und **Status-**Filter mit ~10‑Minuten-Katalog-Cache (Force Refresh mit Fortschritt)
- **Im Verkauf = in mindestens einem Territory verfügbar**; Pipeline-Buckets unabhängig vom Storefront
- Kontextmenü: anheften, zu Modulen springen, Name / Bundle ID / Apple ID / SKU / Store · ASC · Deep Links / Zusammenfassung kopieren; App Store oder ASC öffnen
- Icons: ASC-Build-Artwork → iTunes Lookup → Monogramm, disk-cached

### Overview & Release-Bereitschaft

- Neueste Version/Build, Modul-Shortcuts, kürzliche Review-Einreichungen
- **Weiche Checkliste** (primäre Screenshot-Größe, Copyright, Altersfreigabe u. a.)
- Versions / Submissions wenden **harte Blocker** an (Build-Status, Demo-Zugangsdaten wenn nötig)
- Guide: `iappmanager://release-guide`

### Versionen, Builds & Einreichungen

- Versionen anlegen, Builds anhängen, einreichen / abbrechen, Release-Modi (manuell / auto / geplant), gestaffeltes Release, **Release Now** bei ausstehender Entwicklerfreigabe
- **Build Upload REST** für IPA/PKG; Build-Größe; Diagnose; Beta App Clip; Export-Compliance
- **Background Assets** (`.aar`) erstellen / Chunk-Upload / External Beta & App-Store-Review-Pfade
- **Verschlüsselungserklärungen** mit Dokument-Upload; aus Overview weich geprüft
- **Review Submissions** Entwurf / Items hinzufügen / einreichen; „sofort" oder „zum Entwurf"
- **Review Detail** — Kontakt, Demo-Konto, Notizen, Anhänge, Routing App Coverage

### Store-Eintrag & Wachstum

- **Metadata** — App Info vs. Version Listing; Kategorien, Copyright, EULA, Primärlocale; Android-Mapping; Multi-Locale mit ★ Primary; **Cross-Locale-Kopie**
- **Screenshots & Previews** — nach Version / Locale / Gerätegröße; Reservierungs-Upload; Cross-Locale; Poster-Frame-Zeitcode; Abdeckung durch echte Assets
- **Batch-Assets-Workstation** — Screenshots/Previews über Locales × Größen in einem Desk
- **Download-Size-Workbench** — Build-Downloadgrößen mit weichen Limit-Hinweisen
- **SKU-Suche** in My Apps; adaptive Aktionsleisten auf schmalen Screens
- **Custom Product Pages** — Sichtbarkeit, Deep Links, Promo-Text, Search Keywords, Medien, einreichen
- **In-App Events**, **App Clips**, **Store-Experimente** (Traffic getrennt von Review), **Featuring-Nominierungen**
- **Availability**, **Pricing** (Preispunkt wählen und anwenden — inkl. Equalization-Vorschau), **Altersfreigabe**, **Barrierefreiheit**, **App Tags**
- Häufige Formulare: **⌘S** speichern am Mac

### Monetarisierung & Game Center

- IAP / Abo-Gruppen, Lokalisierungen, Review-Screenshots/Notizen, territoriale Verfügbarkeit, Preispunkte
- Intro / Promo / Win-back; **Offer Codes**; Promo-Bilder; Grace Period; Server-Notification-URLs; CSV Import/Export; einreichen (inkl. Abo-Gruppen)
- Guide: `iappmanager://iap-guide`
- **Game Center** — Achievements, Leaderboards / Sets, Challenges / Activities, Multiplayer, Matchmaking

### TestFlight

- Gruppen, öffentliche Links, Rekrutierungskriterien, Metriken, Einladungen, individuelle Tester, Builds, What to Test, Beta-Lizenz / Review
- Feedback-Posteingang und CSV + **Vollgrößen-Screenshots / Crash-Logs Bulk-Export** (Mac-Ordner / iOS-Zip + Manifest)
- Guide: `iappmanager://testflight-guide`

### Zertifikate, Benutzer, Berichte, Rezensionen

- Zertifikate (CSR in der App / Import) · Profile · Bundle IDs & Capabilities · Merchant / Pass Type · Geräte (**macOS**: Keychain-Installation)
- Benutzereinladungen, Rollen, App-Sichtbarkeit, Provisioning; Sandbox-Tester
- **Reports** — Sales / Finance / Analytics, Szenarien, Custom Presets, **breite TSV-Vorschau** (Spalten, Suche, Vollbild quer) und **leichte Summary-Charts**; `iappmanager://reports-guide`
- Kundenrezensionen — Filter, Suche, antworten / löschen, **Antwort-Vorlagen** (max. 20 pro Konto)
- **Webhooks** — anlegen / bearbeiten / ping / Zustellung (wir hosten keine öffentlichen Callbacks)

### Widgets, Shortcuts, Feinschliff

- Widgets: **Account Hub**, **Apps Pulse** (S/M/L), **Review Desk**, **Quick Actions**
- `iappmanager://` + App Intents — [Shortcut Links](url-scheme)
- Erscheinungsbild, Akzent, EN / 简 / 繁 (Hot-Swap ohne Navigationsverlust)
- iOS **Alternative App-Icons** (IconStyle1–7); StoreKit-Trinkgeld; Feedback-E-Mail

### Datenschutz

- API-Geheimnisse in der **Geräte-Keychain**; Business-API nur an **Apple**
- Optionale Icons via iTunes Lookup; Thumbnail-Cache in Einstellungen löschen
- App Group nur **lokale** Widget-Snapshots — kein Upload an iHTC Studio
- Details: [Privacy Policy](privacy)

## App beziehen

| Kanal | Link |
|-------|------|
| App Store | [Download on the App Store](https://apps.apple.com/app/id6794497110) |

## Systemanforderungen

| Komponente | Minimum |
|------------|---------|
| iPhone / iPad | iOS 17.0+ |
| Mac | macOS 14.0+ |
| Widgets | iOS 17.0+ |
| Große IPAs | **Mac** empfohlen |

## Kontakt

- **E-Mail:** [AppleOSer@gmail.com](mailto:AppleOSer@gmail.com)

Wir antworten in der Regel innerhalb von 48 Stunden.

[FAQ](faq) · [Shortcut Links](url-scheme) · [Privacy Policy](privacy)
