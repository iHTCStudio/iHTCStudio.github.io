**Zuletzt aktualisiert:** 18. August 2026

iHTC Studio („wir“) hat **iPrimer** („爱小学“ / „爱小学“, Bundle-ID `com.iHTCboy.iPrimer`) entwickelt. Diese Datenschutzerklärung erläutert, welche Daten bei der Nutzung verarbeitet werden (und welche nicht). **Apple App Review** und Nutzer können sich auf **diese Seite** als öffentliche Datenschutzerklärung stützen. Für App Store Connect öffnen Sie diese Seite im Browser und kopieren Sie die URL aus der Adressleiste (die Domain kann sich ändern).

## Zusammenfassung (Übereinstimmung mit dem Apple-Datenschutzetikett)

| Thema | Unsere Praxis |
|-------|----------------|
| Konto | **Nicht erforderlich** — keine Registrierung, kein E-Mail-Login oder Telefonnummer erforderlich |
| Datenerhebung durch iHTC Studio | **Keine Datenerhebung** — wir betreiben **keinen** Backend-Service, der Ihre persönlichen Daten empfängt |
| Netzwerk | Bibliothek, reading, recite, Character Study, meditation, Life Guidance, widgets, and daily notifications work **offline** after install funktionieren nach der Installation **offline** |
| Analysen / Werbung / Tracking | **Keine** — keine Analysen von Drittanbietern, Werbung oder Tracking-SDKs; keine Nutzung von App Tracking Transparency |
| Optionale Apple-Dienste | **iCloud** (Ihr privates KVS), **Fotobibliothek (Nur Hinzufügen)** für geteilte Karten, **StoreKit** für optionale Trinkgelder, **lokale Benachrichtigungen**, optionale **Live-Aktivitäten** |

## Datenerfassung

Wir erheben, verkaufen oder teilen **keine** persönlichen Informationen für Werbung oder Analysen.

- **Kein Konto** — Sie können alle Kernfunktionen nutzen, ohne ein Konto bei uns zu erstellen.
- **Keine Analysen oder Werbung** — Die App-Binärdatei integriert keine Analysen, Werbung oder Crash-Reporting-SDKs von Drittanbietern, die Daten an uns senden.
- **Kein Hochladen von Inhalten** — Ihre reading history, favorites, study lists, reflection journal entries, habit check-ins, meditation streaks, study progress, and preferences stay on your device (and optionally in **your** iCloud). They are never uploaded to iHTC Studio servers because **we do not run such servers for this app**.

## So funktioniert die App

- **Mitgelieferte Bibliothek** — Text-JSON, Umgangssprache/Englisch, Indizes und Lernhilfen liegen im App-/Widget-Bundle. Durchsuchen und Lernen erfordern kein Netzwerk.
- **Sprache auf dem Gerät** – Die Rezitation nutzt Apples System **AVSpeechSynthesizer** (TTS). Wir senden keinen Kapiteltext an iHTC Studio.
- **Widgets und App Group** — Widgets und App teilen Einstellungen und leichten Zustand über die App Group `group.com.iHTCboy.iPrimer` auf Ihrem Gerät.
- **Tägliche Benachrichtigungen** – Lokal geplant mit Benutzerbenachrichtigungen. Durch Tippen auf eine Benachrichtigung wird ein Deep-Link zu einer Kapitel-ID auf dem Gerät geöffnet. Kein Server-Fanout.
- **Karten teilen** – Bilder werden auf dem Gerät gerendert. Beim Speichern wird **nur die Add-On-Fotobibliothek** verwendet, wenn Sie auf „Speichern“ tippen. Das System Share Sheet sendet das Bild möglicherweise an eine von Ihnen ausgewählte App. Es gelten dann die Datenschutzbestimmungen dieses Reiseziels.
- **Optionaler Tipp** — „Tip Developer“ (`com.iHTCboy.iPrimer.6`), **StoreKit** via Apple.
- **Siri / Verknüpfungen / Kontrollzentrum** – Optionale Systemintegrationen öffnen Deep Links auf dem Gerät; Sie senden Ihre Bibliothek nicht an uns.
- **Optionales Spotlight** – Wenn Sie die Indizierung aktivieren, werden Inhalte vom System auf dem Gerät für die lokale Suche indiziert; Wir betreiben kein Such-Backend.

## Auf Ihrem Gerät gespeicherte Daten

| Daten | Wo | Zweck |
|------|-------|---------|
| Chapter-Datenbank | App-/Widget-Bundle | Offline-Lesen und -Lernen |
| Favoriten & Lernlisten | UserDefaults der App Group | Markierte Werke & Listen |
| Leseverlauf / zuletzt gelesen | Benutzerstandards der App-Gruppe | Lesen Sie weiter, Verlauf der Benutzeroberfläche |
| Lernfortschritt und Beherrschung | UserDefaults der App Group | Character Study state, quiz / Hunt progress |
| Lernserie / Check-in | UserDefaults der App Group | Daily-Study-Gewohnheit |
| Reflexionstagebuch | UserDefaults der App Group | Life-Guidance-Tagebuch |
| Gewohnheits-Check-ins (洒扫应对) | UserDefaults der App Group | Life-Guidance-Gewohnheiten |
| Meditations-Serie & Sitzungen | UserDefaults der App Group | Meditationskontinuität |
| Einstellungen der Teilen-Karten | UserDefaults der App Group | Zuletzt gewählter Stil / zuletzt gewähltes Seitenverhältnis |
| Daily Study cache & notification prefs | UserDefaults der App Group | Heutige ID, schedule time, contextual toggle |
| Share-Card-Einstellungen | Benutzerstandards der App-Gruppe | Letzte Stil-/Verhältnisauswahl |
| Onboarding- und TipKit-Status | Standard UserDefaults (Gerät) | Willkommensführer / Entdeckungstipps |
| Schnellaktionen auf dem Startbildschirm | System + lokale Einstellungen | Von Ihnen konfigurierte Verknüpfungen |
| Widget-/Live-Aktivitäts-Schnappschüsse | App-Gruppe / ActivityKit | Text anzeigen, den Sie bereits geöffnet haben |

Die Deinstallation der App entfernt Sandbox- und App-Gruppendaten, die mit der App verbunden sind (abhängig vom Verhalten von iOS/macOS). Optionale iCloud-Kopien bleiben in **deiner** iCloud, bis du sie löschst oder die Synchronisierung ausschaltest und anderswo löschst.

## iCloud-Synchronisierung (optional)

Wenn du **iCloud-Synchronisierung** in den Einstellungen aktivierst, spiegelt die App ausgewählte Benutzerdaten über Apples **`NSUbiquitousKeyValueStore`**, die mit **deiner Apple-ID** verknüpft ist:

- Favoriten
- Lernlisten
- Leseverlauf
- Lernfortschritt / Kenntnisse
- Lernserien
- Reflexionstagebuch
- Gewohnheits-Check-ins

Der Synchronisationsverkehr geht an **Apple iCloud**, nicht an iHTC Studio. Du kannst die Synchronisierung in den Einstellungen deaktivieren. Wir können deine iCloud-Inhalte nicht lesen.

## Berechtigungen

iLiezi fordert Berechtigungen nur an, wenn eine Funktion diese benötigt:

| Erlaubnis | Wann | Warum |
|------------|------|-----|
| Benachrichtigungen | Sie aktivieren Daily Study or meditation reminders | Lokale Planung |
| Fotomediathek (nur Hinzufügen) | Sie speichern eine Teilen-Karte | Gerendertes Bild schreiben |
| iCloud | Sync aktivieren | Favoriten/Listen/Verlauf/Fortschritt/Serien/Journal/Gewohnheiten |
| Live Activities (iOS) | Reading/Meditation Live Activity | Sperrbildschirm / Dynamic Island |
| Hintergrundaudio | Hintergrundrezitation aktivieren | TTS im Hintergrund |

Wir fordern **keine** Kontakte, den genauen Standort, die Kamera, das Mikrofon (über die System-TTS-Wiedergabe hinaus) oder die Nachverfolgung an.

## Privatsphäre von Kindern

iPrimer **12+**, **nicht** Kids Category. Keine bewusste Datenerhebung von Kindern.

## Dritte Parteien

Drittanbieter: nur **Apple** (App Store, iCloud, StoreKit, TTS, Benachrichtigungen, Live Activities).

## Datenaufbewahrung & Löschung

- **Auf dem Gerät:** App löschen entfernt Sandbox und App Group (systemabhängig).
- **iCloud:** Sync in Einstellungen deaktivieren; iCloud-Speicher in Systemeinstellungen verwalten.
- **Wir speichern keine Kopien** von Lese-, Journal- und Gewohnheitsdaten auf iHTC Studio-Servern.

## Änderungen an dieser Richtlinie

Wir können diese Seite aus rechtlichen Gründen, produktbedingt oder wegen App-Store-Compliance aktualisieren. Das Datum „Zuletzt aktualisiert“ ändert sich. Fortgesetzte Nutzung nach einer Aktualisierung gilt als Zustimmung zur überarbeiteten Richtlinie.

## Kontakt

Fragen zum Datenschutz: [AppleOSer@gmail.com](mailto:AppleOSer@gmail.com)
