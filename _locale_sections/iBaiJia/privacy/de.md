**Zuletzt aktualisiert:** 18. August 2026

iHTC Studio („wir“) hat **iBaiJia** („爱百家姓“ / „爱百家姓“, Bundle-ID `com.iHTCboy.iBaiJia`) entwickelt. Diese Datenschutzerklärung erläutert, welche Daten bei der Nutzung verarbeitet werden (und welche nicht). **Apple App Review** und Nutzer können sich auf **diese Seite** als öffentliche Datenschutzerklärung stützen. Für App Store Connect öffnen Sie diese Seite im Browser und kopieren Sie die URL aus der Adressleiste (die Domain kann sich ändern).

## Zusammenfassung (Übereinstimmung mit dem Apple-Datenschutzetikett)

| Thema | Unsere Praxis |
|-------|----------------|
| Konto | **Nicht erforderlich** — keine Registrierung, kein E-Mail-Login oder Telefonnummer erforderlich |
| Datenerhebung durch iHTC Studio | **Keine Datenerhebung** — wir betreiben **keinen** Backend-Service, der Ihre persönlichen Daten empfängt |
| Netzwerk | Surname library, detail reading, recite, Study Hall, naming inspiration, widgets, and daily notifications work **offline** after install |
| Analysen / Werbung / Tracking | **Keine** — keine Analysen von Drittanbietern, Werbung oder Tracking-SDKs; keine Nutzung von App Tracking Transparency |
| Optionale Apple-Dienste | **iCloud** (your private KVS), **Photo Library (Add Only)** for share cards, **StoreKit** for optionales Trinkgeld, **local notifications**, optional **Live Activities**, optional **Spotlight** (off by default), optional **system speech / translation** |

## Datenerfassung

Wir erheben, verkaufen oder teilen **keine** persönlichen Informationen für Werbung oder Analysen.

- **Kein Konto** — Sie können alle Kernfunktionen nutzen, ohne ein Konto bei uns zu erstellen.
- **Keine Analysen oder Werbung** — Die App-Binärdatei integriert keine Analysen, Werbung oder Crash-Reporting-SDKs von Drittanbietern, die Daten an uns senden.
- **Kein Hochladen von Inhalten** — Ihre favorites, surname lists, notes, reading history, study progress, streaks, naming preferences, and settings stay on your device (and optionally in **your** iCloud). They are never uploaded to iHTC Studio servers because **we do not run such servers for this app**.

## So funktioniert die App

- **Mitgelieferte Bibliothek** — Text-JSON, Umgangssprache/Englisch, Indizes und Lernhilfen liegen im App-/Widget-Bundle. Durchsuchen und Lernen erfordern kein Netzwerk.
- **Sprache auf dem Gerät** — Lesen/Rezitation via **AVSpeechSynthesizer**. Kein Familientext an iHTC Studio.
- **Optionale Systemübersetzung** — Apple Translation; Verarbeitung in Apple OS.
- **Namensinspiration** — vollständig auf dem Gerät aus gebündelten Daten. Kein Upload von Namen oder Einstellungen.
- **Widgets und App Group** — Widgets und App teilen Einstellungen und leichten Zustand über die App Group `group.com.iHTCboy.iBaiJia` auf Ihrem Gerät.
- **Tägliche Benachrichtigungen** — lokal mit User Notifications. Tipp öffnet Deep Link; kein Server.
- **Karten teilen** – Bilder werden auf dem Gerät gerendert. Beim Speichern wird **nur die Add-On-Fotobibliothek** verwendet, wenn Sie auf „Speichern“ tippen. Das System Share Sheet sendet das Bild möglicherweise an eine von Ihnen ausgewählte App. Es gelten dann die Datenschutzbestimmungen dieses Reiseziels.
- **Optionaler Tipp** — „Tip Developer“ (`com.iHTCboy.iBaiJia.6`), **StoreKit** via Apple.
- **Siri / Verknüpfungen / Kontrollzentrum** – Optionale Systemintegrationen öffnen Deep Links auf dem Gerät; Sie senden Ihre Bibliothek nicht an uns.
- **Optionales Spotlight** — Familiennamen werden auf dem Gerät indiziert.
- **Feedback-E-Mail** — kann Ihren Text und Geräte-/App-Diagnose (Version, OS, Sprache) nur zur Fehlerbehebung enthalten.

## Auf Ihrem Gerät gespeicherte Daten

| Daten | Wo | Zweck |
|------|-------|---------|
| Familiennamen-DB & Striche | App-Bundle | Offline, Nachzeichnen, Lernen |
| Favoriten & Familienlisten | UserDefaults der App Group | Markierte Familiennamen |
| Notizen | UserDefaults der App Group | Familien-Notizen |
| Mein Familienname | UserDefaults der App Group | Personalisierte Startseite & Widgets |
| Leseverlauf / zuletzt gelesen | UserDefaults der App Group | Weiterstöbern, Verlaufs-UI |
| Lernfortschritt & Highscores | UserDefaults der App Group | Study-Hall-Status |
| Check-in-Serie | UserDefaults der App Group | Tägliche Gewohnheit |
| Aussehen & Lesepräferenzen | Benutzerstandards der App-Gruppe | Thema, Akzent, Sprache, Layout, TTS, Tabs, Widgets |
| Daily Surname cache & notification prefs | UserDefaults der App Group | Heutige ID, schedule time |
| Share-Karten-Einstellungen | UserDefaults der App Group | Last style choices |
| Onboarding- und TipKit-Status | Standard UserDefaults (Gerät) | Willkommensführer / Entdeckungstipps |
| Schnellaktionen auf dem Startbildschirm | System + lokale Einstellungen | Von Ihnen konfigurierte Verknüpfungen |
| Widget-/Live-Aktivitäts-Schnappschüsse | App-Gruppe / ActivityKit | Text anzeigen, den Sie bereits geöffnet haben |

Die Deinstallation der App entfernt Sandbox- und App-Gruppendaten, die mit der App verbunden sind (abhängig vom Verhalten von iOS/macOS). Optionale iCloud-Kopien bleiben in **deiner** iCloud, bis du sie löschst oder die Synchronisierung ausschaltest und anderswo löschst.

## iCloud-Synchronisierung (optional)

Wenn du **iCloud-Synchronisierung** in den Einstellungen aktivierst, spiegelt die App ausgewählte Benutzerdaten über Apples **`NSUbiquitousKeyValueStore`**, die mit **deiner Apple-ID** verknüpft ist:

- Favoriten
- Familienlisten
- Notizen
- Leseverlauf
- Lernfortschritt / Highscores
- Check-in-Serien
- Zugehörige Einstellungen

Der Synchronisationsverkehr geht an **Apple iCloud**, nicht an iHTC Studio. Du kannst die Synchronisierung in den Einstellungen deaktivieren. Wir können deine iCloud-Inhalte nicht lesen.

## Berechtigungen

iLiezi fordert Berechtigungen nur an, wenn eine Funktion diese benötigt:

| Erlaubnis | Wann | Warum |
|------------|------|-----|
| Benachrichtigungen | Sie aktivieren Daily Surname reminders | Lokale Planung |
| Fotomediathek (nur Hinzufügen) | Sie speichern eine Teilen-Karte | Gerendertes Bild schreiben |
| iCloud | Sync aktivieren | Favoriten/Listen/Verlauf/Fortschritt/Serien/Notizen |
| Live-Aktivitäten (iOS) | Sie aktivieren Lese-Live-Aktivität | Sperrbildschirm / Dynamic Island |
| Hintergrundaudio (iOS) | Hintergrundrezitation aktivieren | TTS im Hintergrund |

Wir fordern **keine** Kontakte, den genauen Standort, die Kamera, das Mikrofon (über die System-TTS-Wiedergabe hinaus) oder die Nachverfolgung an.

## Privatsphäre von Kindern

iBaiJia ist eine Kultur-Lern-App für ein allgemeines Publikum und **nicht** in der Kids Category. Wir erheben wissentlich keine personenbezogenen Daten von Kindern. Die App erfordert kein Konto. Familien können Lese- und Lernfunktionen offline auf eigenen Geräten nutzen.

## Dritte Parteien

Drittanbieter: **Apple**. Familiendaten: CC BY 4.0, LGPL/Arphic (About).

## Datenaufbewahrung & Löschung

- **Auf dem Gerät:** löschen, Export/Import in Einstellungen. App löschen.
- **iCloud:** Sync in Einstellungen deaktivieren; iCloud-Speicher in Systemeinstellungen verwalten.
- **Keine Kopien** von Lesen, Notizen, Favoriten.

## Änderungen an dieser Richtlinie

Wir können diese Seite aus rechtlichen Gründen, produktbedingt oder wegen App-Store-Compliance aktualisieren. Das Datum „Zuletzt aktualisiert“ ändert sich. Fortgesetzte Nutzung nach einer Aktualisierung gilt als Zustimmung zur überarbeiteten Richtlinie.

## Kontakt

Fragen zum Datenschutz: [AppleOSer@gmail.com](mailto:AppleOSer@gmail.com)
