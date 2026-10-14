iHTC Studio („wir") hat iAppManager (爱应用者 / 愛應用者) entwickelt.

## Kurzfassung

**iHTC Studio betreibt kein Backend für deine App-Store-Connect-Daten.** Du meldest dich mit einem **API Key** an; der Schlüssel liegt in der **Geräte-Keychain**. Geschäftsanfragen gehen **direkt zu Apple** (`api.appstoreconnect.apple.com`). **Kein iHTC-Studio-Konto. Keine Werbung. Kein Analytics-/Crash-SDK.** Optionale StoreKit-Trinkgelder verarbeitet **Apple**.

## Auf dem Gerät gespeicherte Daten

| Daten | Zweck |
|------|---------|
| API-Key-Konten (Issuer ID, Key ID, `.p8` PEM) | App Store Connect API-Auth — Keychain |
| Kontenindex / aktuelles Konto / Einstellungen | Multi-Account, Erscheinungsbild, Sprache, Akzent |
| Remote-Bildcache | App-Icons & Medien-Thumbnails (in Einstellungen löschbar) |
| Review-Antwortvorlagen, Report-Presets / Sterne | Lokale Produktivitätshilfen pro Konto |
| App-Group-Widget-Snapshot | Pipeline-Zähler, Theme/Sprache — **nur auf dem Gerät** |

## Netzwerk

| Ziel | Warum |
|-------------|-----|
| `api.appstoreconnect.apple.com` | Gesamte ASC-Verwaltung (JWT auf dem Gerät signiert) |
| Apple iTunes Lookup (mehrere Regionen) | Optionale Icon-Anreicherung |
| Apple CDN / vorab signierte Upload-URLs | Screenshots, Previews, IPA/PKG-Chunk-Uploads (PUT ohne Bearer) |
| `apps.apple.com` / App Store | Produktseiten öffnen (System / extern) |
| Mail-Client | Feedback, das du selbst sendest |

iHTC Studio erhält **nicht** deinen API-Private-Key, App-Metadaten, IPA-Inhalte, Verkaufsberichte oder Kundenreviews.

## Berechtigungen & Plattform

| Fähigkeit | Wann | Warum |
|------------|------|-----|
| Ausgehender Netzwerkverkehr | Bei ASC-Funktionen | Apple-APIs |
| Vom Nutzer gewählte Dateien | IPA/Screenshots hochladen, Reports exportieren | Du wählst Dateien |
| Keychain | API Key speichern / entfernen | Sichere lokale Speicherung |
| App Group | Widgets | Nur lokale Zusammenfassungen |
| Fotos / Share Sheet (vom OS) | Wenn du exportierst / speicherst | Nutzerinitiiert |

**Installation von Zertifikaten in die System-Keychain** ist für **macOS** gedacht. iOS: Liste / Download / Teilen.

## Was wir nicht tun

- Kein iHTC-Studio-Cloud-Konto für ASC-Daten
- Keine Werbung oder Drittanbieter-Tracker
- Kein Verkauf personenbezogener Daten
- Widgets rufen ASC nicht selbst auf

## Kontakt

[AppleOSer@gmail.com](mailto:AppleOSer@gmail.com)
