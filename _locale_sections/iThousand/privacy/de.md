**Zuletzt aktualisiert:** 18. August 2026

iHTC Studio („wir“) hat **iThousand** („爱千字文“ / „爱千字文“, Bundle-ID `com.iHTCboy.iThousand`) entwickelt. Diese Datenschutzerklärung erläutert, welche Daten bei der Nutzung verarbeitet werden (und welche nicht). **Apple App Review** und Nutzer können sich auf **diese Seite** als öffentliche Datenschutzerklärung stützen. Für App Store Connect öffnen Sie diese Seite im Browser und kopieren Sie die URL aus der Adressleiste (die Domain kann sich ändern).

## Zusammenfassung (Übereinstimmung mit dem Apple-Datenschutzetikett)

| Thema | Unsere Praxis |
|-------|----------------|
| Konto | **Nicht erforderlich** — keine Registrierung, kein E-Mail-Login oder Telefonnummer erforderlich |
| Datenerhebung durch iHTC Studio | **Keine Datenerhebung** — wir betreiben **keinen** Backend-Service, der Ihre persönlichen Daten empfängt |
| Netzwerk | Bibliothek, character cards, reading, recite, Primer Hall, Hunt, widgets, and daily notifications work **offline** after install funktionieren nach der Installation **offline** |
| Analysen / Werbung / Tracking | **Keine** — keine Analysen von Drittanbietern, Werbung oder Tracking-SDKs; keine Nutzung von App Tracking Transparency |
| Optionale Apple-Dienste | **iCloud** (your private KVS), **Photo Library (Add Only)** for share cards, **StoreKit** for optionales Trinkgeld, **local notifications**, optional **Live Activities**, optional **Spotlight** (off by default), optional **system speech / translation** |

## Datenerfassung

Wir erheben, verkaufen oder teilen **keine** persönlichen Informationen für Werbung oder Analysen.

- **Kein Konto** — Sie können alle Kernfunktionen nutzen, ohne ein Konto bei uns zu erstellen.
- **Keine Analysen oder Werbung** — Die App-Binärdatei integriert keine Analysen, Werbung oder Crash-Reporting-SDKs von Drittanbietern, die Daten an uns senden.
- **Kein Hochladen von Inhalten** — Ihre reading history, favorites, lists (千单), saved characters, notes, study progress, streaks, and preferences stay on your device (and optionally in **your** iCloud). They are never uploaded to iHTC Studio servers because **we do not run such servers for this app**.

## So funktioniert die App

- **Mitgelieferte Bibliothek** — Text-JSON, Umgangssprache/Englisch, Indizes und Lernhilfen liegen im App-/Widget-Bundle. Durchsuchen und Lernen erfordern kein Netzwerk.
- **Sprache auf dem Gerät** – Die Rezitation nutzt Apples System **AVSpeechSynthesizer** (TTS). Wir senden keine Passagentexte an iHTC Studio.
- **Systemübersetzung** — Apple-Funktionen auf dem Gerät; Apple OS.
- **Widgets und App Group** — Widgets und App teilen Einstellungen und leichten Zustand über die App Group `group.com.iHTCboy.iThousand` auf Ihrem Gerät.
- **Tägliche Benachrichtigungen** – Lokal geplant mit Benutzerbenachrichtigungen. Durch Tippen auf eine Benachrichtigung wird ein Deep-Link zu einer Durchgangs-ID auf dem Gerät geöffnet. Kein Server-Fanout.
- **Karten teilen** – Bilder werden auf dem Gerät gerendert. Beim Speichern wird **nur die Add-On-Fotobibliothek** verwendet, wenn Sie auf „Speichern“ tippen. Das System Share Sheet sendet das Bild möglicherweise an eine von Ihnen ausgewählte App. Es gelten dann die Datenschutzbestimmungen dieses Reiseziels.
- **Optionaler Tipp** — „Tip Developer“ (`com.iHTCboy.iThousand.6`), **StoreKit** via Apple.
- **Siri / Verknüpfungen / Kontrollzentrum** – Optionale Systemintegrationen öffnen Deep Links auf dem Gerät; Sie senden Ihre Bibliothek nicht an uns.
- **Optionales Spotlight** — standardmäßig aus. Passagen/Karten werden auf dem Gerät indiziert; kein Such-Backend.
- **Feedback-E-Mail** — kann Ihren Text und Geräte-/App-Diagnose (Version, OS, Sprache) nur zur Fehlerbehebung enthalten.

## Auf Ihrem Gerät gespeicherte Daten

| Daten | Wo | Zweck |
|------|-------|---------|
| Passagen- & Zeichendatenbank | App-/Widget-Bundle | Offline, Literacy-Karten |
| Favoriten und Listen (千单) | UserDefaults der App Group | Markierte Abschnitte und Nutzerlisten |
| Gespeicherte Zeichen & Zeilen | UserDefaults der App Group | Schwierige Zeichen, markierte Zeilen |
| Leseverlauf / zuletzt gelesen | Benutzerstandards der App-Gruppe | Lesen Sie weiter, Verlauf der Benutzeroberfläche |
| Lernfortschritt und Beherrschung | UserDefaults der App Group | Primer Hall state, quiz / Hunt progress |
| Notizen | UserDefaults der App Group | Passagen-Notizen |
| Lernserie / Check-in | UserDefaults der App Group | Tägliche Gewohnheit |
| Einstellungen der Teilen-Karten | UserDefaults der App Group | Zuletzt gewählter Stil / zuletzt gewähltes Seitenverhältnis |
| Daily Line-Cache- und Benachrichtigungseinstellungen | Benutzerstandards der App-Gruppe | Heutige ID, Zeitplanzeit, kontextbezogenes Umschalten |
| Share-Card-Einstellungen | Benutzerstandards der App-Gruppe | Letzte Stil-/Verhältnisauswahl |
| Onboarding- und TipKit-Status | Standard UserDefaults (Gerät) | Willkommensführer / Entdeckungstipps |
| Schnellaktionen auf dem Startbildschirm | System + lokale Einstellungen | Von Ihnen konfigurierte Verknüpfungen |
| Widget-/Live-Aktivitäts-Schnappschüsse | App-Gruppe / ActivityKit | Text anzeigen, den Sie bereits geöffnet haben |

Die Deinstallation der App entfernt Sandbox- und App-Gruppendaten, die mit der App verbunden sind (abhängig vom Verhalten von iOS/macOS). Optionale iCloud-Kopien bleiben in **deiner** iCloud, bis du sie löschst oder die Synchronisierung ausschaltest und anderswo löschst.

## iCloud-Synchronisierung (optional)

Wenn du **iCloud-Synchronisierung** in den Einstellungen aktivierst, spiegelt die App ausgewählte Benutzerdaten über Apples **`NSUbiquitousKeyValueStore`**, die mit **deiner Apple-ID** verknüpft ist:

- Favoriten
- Listen (千单)
- Gespeicherte Zeichen / Lieblingszeilen
- Leseverlauf
- Lernfortschritt / Kenntnisse
- Lernserien
- Notizen

Der Synchronisationsverkehr geht an **Apple iCloud**, nicht an iHTC Studio. Du kannst die Synchronisierung in den Einstellungen deaktivieren. Wir können deine iCloud-Inhalte nicht lesen.

## Berechtigungen

iLiezi fordert Berechtigungen nur an, wenn eine Funktion diese benötigt:

| Erlaubnis | Wann | Warum |
|------------|------|-----|
| Benachrichtigungen | Sie aktivieren Daily Line reminders | Lokale Planung |
| Fotomediathek (nur Hinzufügen) | Share-Karte/Zeichenbild | Write the rendered image |
| iCloud | Sync aktivieren | Favoriten/Listen/Verlauf/Fortschritt/Serien/Notizen/gespeicherte Zeichen |
| Live-Aktivitäten (iOS) | Sie aktivieren Lese-Live-Aktivität | Sperrbildschirm / Dynamic Island |
| Hintergrundaudio | Hintergrundrezitation aktivieren | TTS im Hintergrund |

Wir fordern **keine** Kontakte, den genauen Standort, die Kamera, das Mikrofon (über die System-TTS-Wiedergabe hinaus) oder die Nachverfolgung an.

## Privatsphäre von Kindern

iThousand — Bildungs-App, **nicht** Kids Category.

## Dritte Parteien

Drittanbieter: **Apple** (…Systemübersetzung, Spotlight).

## Datenaufbewahrung & Löschung

- **Auf dem Gerät:** Fortschritt/Verlauf/Notizen löschen. App löschen entfernt Sandbox/App Group.
- **iCloud:** Sync in Einstellungen deaktivieren; iCloud-Speicher in Systemeinstellungen verwalten.
- **Keine Kopien** von Lesen, Notizen, Zeichen-Lesezeichen.

## Änderungen an dieser Richtlinie

Wir können diese Seite aus rechtlichen Gründen, produktbedingt oder wegen App-Store-Compliance aktualisieren. Das Datum „Zuletzt aktualisiert“ ändert sich. Fortgesetzte Nutzung nach einer Aktualisierung gilt als Zustimmung zur überarbeiteten Richtlinie.

## Kontakt

Fragen zum Datenschutz: [AppleOSer@gmail.com](mailto:AppleOSer@gmail.com)
