**Zuletzt aktualisiert:** 18. August 2026

iHTC Studio („wir“) hat **iSutra** („爱佛经“ / „爱佛经“, Bundle-ID `com.iHTCboy.iSutra`) entwickelt. Diese Datenschutzerklärung erläutert, welche Daten bei der Nutzung verarbeitet werden (und welche nicht). **Apple App Review** und Nutzer können sich auf **diese Seite** als öffentliche Datenschutzerklärung stützen. Für App Store Connect öffnen Sie diese Seite im Browser und kopieren Sie die URL aus der Adressleiste (die Domain kann sich ändern).

## Zusammenfassung (Übereinstimmung mit dem Apple-Datenschutzetikett)

| Thema | Unsere Praxis |
|-------|----------------|
| Konto | **Nicht erforderlich** — keine Registrierung, kein E-Mail-Login oder Telefonnummer erforderlich |
| Datenerhebung durch iHTC Studio | **Keine Datenerhebung** — wir betreiben **keinen** Backend-Service, der Ihre persönlichen Daten empfängt |
| Netzwerk | Bibliothek, reading, recite, Study Hall, Hunt, chant, practice, widgets, and daily notifications work **offline** after install funktionieren nach der Installation **offline** |
| Analysen / Werbung / Tracking | **Keine** — keine Analysen von Drittanbietern, Werbung oder Tracking-SDKs; keine Nutzung von App Tracking Transparency |
| Optionale Apple-Dienste | **iCloud** (your private KVS), **Photo Library (Add Only)** for Dharma cards / exports, **StoreKit** for optionales Trinkgeld, **local notifications**, optional **Live Activities**, optional **Spotlight** (off by default) |

## Datenerfassung

Wir erheben, verkaufen oder teilen **keine** persönlichen Informationen für Werbung oder Analysen.

- **Kein Konto** — Sie können alle Kernfunktionen nutzen, ohne ein Konto bei uns zu erstellen.
- **Keine Analysen oder Werbung** — Die App-Binärdatei integriert keine Analysen, Werbung oder Crash-Reporting-SDKs von Drittanbietern, die Daten an uns senden.
- **Kein Hochladen von Inhalten** — Ihre reading history, favorites, lists, notes, mastery, streaks, chant counts, practice checklists, and preferences stay on your device (and optionally in **your** iCloud). They are never uploaded to iHTC Studio servers because **we do not run such servers for this app**.

## So funktioniert die App

- **Mitgelieferte Bibliothek** — Text-JSON, Umgangssprache/Englisch, Indizes und Lernhilfen liegen im App-/Widget-Bundle. Durchsuchen und Lernen erfordern kein Netzwerk.
- **Sprache auf dem Gerät** — **AVSpeechSynthesizer**. Kein Sutra-Text an iHTC Studio.
- **Widgets und App Group** — Widgets und App teilen Einstellungen und leichten Zustand über die App Group `group.com.iHTCboy.iSutra` auf Ihrem Gerät.
- **Tägliche Benachrichtigungen** – Lokal geplant mit Benutzerbenachrichtigungen. Durch Tippen auf eine Benachrichtigung wird ein Deep-Link zu einer Durchgangs-ID auf dem Gerät geöffnet. Kein Server-Fanout.
- **Dharma-Karten / Export** — Bilder/PDF auf dem Gerät. **Fotomediathek (nur Hinzufügen)** beim Speichern.
- **Sutra abschreiben (iOS)** — PencilKit-Striche in Application Support (`CopySutra/…`). **Nicht** in App Group, **keine** iCloud-Sync.
- **Optionaler Tipp** – „Tip Developer“ ist ein verbrauchbarer **StoreKit**-Kauf, der von Apple abgewickelt wird. Wir erhalten Ihre Zahlungskartendaten nicht.
- **Siri / Verknüpfungen / Kontrollzentrum** – Optionale Systemintegrationen öffnen Deep Links auf dem Gerät; Sie senden Ihre Bibliothek nicht an uns.
- **Optionales Spotlight** – standardmäßig deaktiviert. Wenn Sie die Indizierung aktivieren, wird der Inhalt vom System auf dem Gerät für die lokale Suche indiziert; Wir betreiben kein Such-Backend.

## Auf Ihrem Gerät gespeicherte Daten

| Daten | Wo | Zweck |
|------|-------|---------|
| Sutra-Datenbank (Indizes, Shards) | App-/Widget-Bundle | Offline-Lesen und -Lernen |
| Favoriten und Listen (经单) | UserDefaults der App Group | Markierte Abschnitte und Nutzerlisten |
| Leseverlauf / zuletzt gelesen | Benutzerstandards der App-Gruppe | Lesen Sie weiter, Verlauf der Benutzeroberfläche |
| Lernfortschritt und Beherrschung | UserDefaults der App Group | Study Hall state, quiz / Hunt progress |
| Notizen | UserDefaults der App Group | Passagen-Notizen |
| Übungssträhne / Check-in | Benutzerstandards der App-Gruppe | Tägliche Gewohnheit |
| Chant-Zähler & Ton | UserDefaults der App Group | Wooden-fish, Ziele, Töne |
| Morgen/Abend-Praxis | UserDefaults der App Group | Tägliche Liturgie-Checkliste |
| Aussehen & Lesepräferenzen | Benutzerstandards der App-Gruppe | Thema, Akzent, Sprache, Layout, TTS, Tabs, Widgets |
| Daily Sutra cache & notification prefs | UserDefaults der App Group | Heutige ID, schedule time |
| Share-Card-Einstellungen | Benutzerstandards der App-Gruppe | Letzte Stil-/Verhältnisauswahl |
| Copy-sutra-Zeichnungen (iOS) | Application Support (`CopySutra/`) | Entwürfe pro Zeile |
| Onboarding- und TipKit-Status | Standard UserDefaults (Gerät) | Willkommensführer / Entdeckungstipps |
| Schnellaktionen auf dem Startbildschirm | System + lokale Einstellungen | Von Ihnen konfigurierte Verknüpfungen |
| Widget-/Live-Activity-Schnappschüsse | App Group / ActivityKit | Anzeige geöffneter Text/Chant |

Die Deinstallation der App entfernt Sandbox- und App-Gruppendaten, die mit der App verbunden sind (abhängig vom Verhalten von iOS/macOS). Optionale iCloud-Kopien bleiben in **deiner** iCloud, bis du sie löschst oder die Synchronisierung ausschaltest und anderswo löschst.

## iCloud-Synchronisierung (optional)

Mit **iCloud Sync** Spiegelung über **`NSUbiquitousKeyValueStore`**. Traffic zu **Apple iCloud**. Copy-sutra **nicht** enthalten.

## Berechtigungen

iLiezi fordert Berechtigungen nur an, wenn eine Funktion diese benötigt:

| Erlaubnis | Wann | Warum |
|------------|------|-----|
| Benachrichtigungen | Sie aktivieren Daily Sutra reminders | Lokale Planung of reminder notifications |
| Fotomediathek (nur Hinzufügen) | Dharma-Karte speichern/exportieren | Gerendetes Bild/PDF; kein Vollzugriff |
| iCloud | Sync aktivieren | Favoriten/Listen/Verlauf/Mastery/Notizen/Chant |
| Live Activities (iOS) | Reading/Chant Live Activity | Lesen/Chant auf Sperrbildschirm |
| Hintergrundaudio (Fähigkeit) | Sie aktivieren die Hintergrundrezitation | TTS fortsetzen, wenn die App nicht im Vordergrund ist |

Wir fordern **keine** Kontakte, den genauen Standort, die Kamera, das Mikrofon (über die System-TTS-Wiedergabe hinaus) oder die Nachverfolgung an.

## Was wir nicht tun

- Wir verkaufen **keine** personenbezogene Daten.
- Wir erstellen **keine** Werbeprofile.
- Wir benötigen **kein** Konto oder Social-Login.
- Wir betten zur Datenerfassung **keine** Werbung, Analysen oder soziale SDKs von Drittanbietern ein.
- **Kein** Zugriff auf Fotomediathek über **nur Hinzufügen** hinaus beim Speichern.
- Wir erhalten **keine** Nummern von StoreKit-Zahlungskarten (Apple verarbeitet Zahlungen).
- **Keine** Wahrsagerei oder bezahlte Segens-Commerce aus religiösen Inhalten.

## Privatsphäre von Kindern

iSutra erhebt wissentlich keine Daten, auch nicht von Kindern unter 13. Kein Backend, kein Kinderprofil.

## Dritte Parteien

- **Apple** — App Store-Verteilung, optionale StoreKit-Käufe, optionales iCloud-KVS, System-TTS, von Ihnen ausgewählte Share Sheet-Ziele, und Betriebssystem-gestützte Zustellung für Benachrichtigungen / Live-Aktivitäten / Siri / Kurzbefehle.
- **Keine weiteren Drittanbieter-SDKs** für Werbung, Analysen oder Social-Login sind zur Datenerfassung enthalten.

## Internationale Nutzer

Die App ist darauf ausgelegt, offline auf Ihrem Gerät zu funktionieren. Optionale Apple-Dienste unterliegen den Bedingungen von Apple und der regionalen Verfügbarkeit.

## Datenaufbewahrung & Löschung

- **Auf dem Gerät** — Lokale Einstellungen und Fortschritte bleiben erhalten, bis Sie sie in der App löschen (falls verfügbar), das Gerät zurücksetzen oder die App deinstallieren.
- **iCloud (optional)** — Daten, die Sie synchronisiert haben, bleiben in **Ihrem** iCloud-Konto gemäß den Richtlinien von Apple, bis Sie die Synchronisation deaktivieren und/oder sie über Apples Tools löschen.
- **iHTC Studio** — Da wir keine persönlichen Daten auf unseren Servern sammeln, gibt es keinen Kontodatensatz, den wir auf Anfrage löschen könnten, abgesehen davon, Ihre E-Mail-Fragen zu beantworten.

## Änderungen an dieser Richtlinie

Wir können diese Datenschutzrichtlinie von Zeit zu Zeit aktualisieren. Das Datum „Zuletzt aktualisiert“ oben wird sich ändern, und die überarbeitete Richtlinie wird auf dieser Seite der Datenschutzrichtlinie veröffentlicht.

## Kontaktieren Sie uns

Wenn Sie Fragen zu dieser Datenschutzrichtlinie oder zu Datenschutzpraktiken haben:

- **E-Mail:** [AppleOSer@gmail.com](mailto:AppleOSer@gmail.com)

Wir antworten normalerweise innerhalb von 48 Stunden.
