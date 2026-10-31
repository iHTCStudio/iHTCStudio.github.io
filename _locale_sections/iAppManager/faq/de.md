### Was ist iAppManager?

Eine **native App-Store-Connect-Arbeitsstation** für iPhone, iPad und Mac. Anmeldung mit **API Key**, Verwaltung von Versionen, Screenshots, IAP, TestFlight, Zertifikaten, Berichten und Reviews — Traffic **direkt zu Apple**. Kein iHTC-Studio-Konto nötig.

### Wie erhalte ich einen API Key?

1. [App Store Connect](https://appstoreconnect.apple.com) → **Users and Access** → **Integrations** → **App Store Connect API**
2. Schlüssel erstellen (Admin oder App Manager empfohlen)
3. `.p8` **einmal** herunterladen, **Issuer ID** und **Key ID** notieren
4. In iAppManager einfügen (oder Datei wählen). Die In-App-Anleitung mit Screenshots führt dich durch.

### Wird meine `.p8` zu iHTC Studio hochgeladen?

**Nein.** Der private Schlüssel bleibt in der **Geräte-Keychain**. Anfragen werden lokal signiert und an `api.appstoreconnect.apple.com` gesendet. Konto entfernen löscht den lokalen Schlüssel.

### Brauche ich im App das Apple-ID-Passwort?

**Nein.** Authentifizierung **nur per API Key** (Issuer ID + Key ID + `.p8`). Fehlt eine öffentliche API (z. B. Privacy Nutrition Labels, Gratis-App-Promocodes), öffnet die App Apples Website — dort nutzt du Apple ID in Safari/ASC.

### IPA / PKG ohne Transporter hochladen?

**Ja.** iAppManager nutzt Apples **Build Upload REST** (WWDC25). Große Dateien lieber am **Mac**; iOS unterstützt dieselbe API, große Uploads sind dort unbequem.

### Was bedeutet „on sale" in Filtern / Widgets?

**In mindestens einem App-Store-Territorium verfügbar.** Pipeline-Buckets (waiting / in review / rejected / pending developer release) werden getrennt geführt. Widget **Needs attention** = waiting + in review + rejected + pending release (lokale Summe, kein ASC-Feld).

### Hard vs. Soft Checks vor dem Submit?

**Hard blockers** stoppen den Submit (z. B. Build nicht bereit, Demo-Konto nötig aber fehlt). **Soft checks** warnen (Haupt-Screenshot-Größe, Copyright, Altersfreigabe usw.) — nach Bestätigung weiter. Siehe Overview / Versions / Submissions `?` oder `iappmanager://release-guide`.

### Welche Sprachen?

**English · 简体中文 · 繁體中文** — System folgen oder in den Einstellungen erzwingen. Hot-Swap der Sprache **ohne** Root neu zu mounten (Navigation und Entwürfe bleiben).

### Warum zeigen Widgets keine Live-ASC-Zahlen?

Widgets **rufen ASC nicht auf**. Die Haupt-App scannt und schreibt einen Snapshot (~10 Min. TTL, gleiche Buckets wie My Apps). App öffnen und Liste aktualisieren (oder Status erzwingen).

### macOS vs. iOS?

Beide: Store, Monetarisierung, TestFlight, Game Center, Nutzer, Berichte, Reviews, Webhooks. **Große IPAs** und Zertifikate in die System-Keychain — **Mac** bevorzugen. Alternative App-Icons **nur iOS**.

### Privacy-Policy-URL für App Store Connect?

Öffne die [Privacy Policy](../privacy) dieser Site und kopiere die URL aus der Browser-Adressleiste.

### Systemanforderungen?

iPhone / iPad **iOS 17.0+**, Mac **macOS 14.0+**.

### Support kontaktieren?

[AppleOSer@gmail.com](mailto:AppleOSer@gmail.com) — in der Regel innerhalb von 48 Stunden.
