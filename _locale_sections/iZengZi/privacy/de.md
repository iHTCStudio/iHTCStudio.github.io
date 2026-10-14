**Zuletzt aktualisiert:** 19. September 2026

iHTC Studio ("wir", "uns" oder "unser") hat **iLiezi** (auch bekannt als "爱列子 / 愛列子", Bundle-ID `com.iHTCboy.iLiezi`) entwickelt. Diese Datenschutzerklärung erklärt, welche Daten beim Verwenden der App verarbeitet werden (und welche nicht). **Apple App Review** und Benutzer können sich auf **diese Seite** als die öffentliche Datenschutzerklärung verlassen. Für App Store Connect öffnen Sie diese Datenschutzerklärung in Ihrem Browser und kopieren die Adresse aus der Adressleiste (die Domain der öffentlichen Seite kann sich im Laufe der Zeit ändern).

## Zusammenfassung (Übereinstimmung mit dem Apple-Datenschutzetikett)

| Thema | Unsere Praxis |
|-------|----------------|
| Konto | **Nicht erforderlich** — keine Registrierung, kein E-Mail-Login oder Telefonnummer erforderlich |
| Datenerhebung durch iHTC Studio | **Keine Datenerhebung** — wir betreiben **keinen** Backend-Service, der Ihre persönlichen Daten empfängt |
| Netzwerk | Bibliothek, Lesen, Rezitieren, Lernen, Hunt, Widgets und tägliche Benachrichtigungen funktionieren **offline** nach der Installation |
| Analysen / Werbung / Tracking | **Keine** — keine Analysen von Drittanbietern, Werbung oder Tracking-SDKs; keine Nutzung von App Tracking Transparency |
| Optionale Apple-Dienste | **iCloud** (your private KVS), **Photo Library (Add Only)** for study cards, **StoreKit** for optionales Trinkgeld, **local notifications**, optional **Live Activities**, optional on-device **handwriting** (Vision), optional **HealthKit** mood write (off by default) |

## Datenerfassung

Wir erheben, verkaufen oder teilen **keine** persönlichen Informationen für Werbung oder Analysen.

- **Kein Konto** — Sie können alle Kernfunktionen nutzen, ohne ein Konto bei uns zu erstellen.
- **Keine Analysen oder Werbung** — Die App-Binärdatei integriert keine Analysen, Werbung oder Crash-Reporting-SDKs von Drittanbietern, die Daten an uns senden.
- **Kein Hochladen von Inhalten** — Leseverlauf, Favoriten, Listen, Notizen, Lernfortschritt und Einstellungen bleiben auf dem Gerät (optional in **Ihrem** iCloud). Sie werden nicht auf iHTC Studio-Server hochgeladen, da **wir für diese App keine solchen Server betreiben**.

**Drei-Fragen-Tagebuch** privat auf dem Gerät. **HealthKit** **aus**, nur aus Journal-Einstellungen, nur **Health**, **keine** Diagnose.

## So funktioniert die App

- **Gebündelte Bibliothek** – JSON-Text, Umgangssprache/Englisch, Indizes und Lernhilfen sind im App-/Widget-Paket enthalten.
- **Sprache auf dem Gerät** – Die Rezitation nutzt Apples System **AVSpeechSynthesizer** (TTS). Wir senden keine Passagentexte an iHTC Studio.
- **Widgets & App-Gruppe** – Widgets und die App-Freigabeeinstellungen über die App-Gruppe `group.com.iHTCboy.iLiezi` auf Ihrem Gerät.
- **Tägliche Benachrichtigungen** – Lokal geplant. Durch Tippen auf eine Benachrichtigung wird ein Deep-Link auf dem Gerät geöffnet.
- **Lernkarten** – Bilder werden auf dem Gerät gerendert. Beim Speichern wird **nur die Add-On-Fotobibliothek** verwendet, wenn Sie auf „Speichern“ tippen.
- **Handschriftsuche (iOS)** – Die optionale Zeichenerkennung verwendet Apple **Vision** auf dem Gerät. Striche werden nicht hochgeladen.
- **Optionaler Tipp** – „Tip Developer“ ist ein verbrauchbarer **StoreKit**-Kauf, der von Apple abgewickelt wird.
- **Siri / Verknüpfungen / Kontrollzentrum** – Optionale Systemintegrationen öffnen Deep Links auf dem Gerät.
- **Optionales Spotlight** – Wenn Sie die Indizierung aktivieren, indiziert das System Inhalte auf dem Gerät.

## Auf Ihrem Gerät gespeicherte Daten

| Daten | Wo | Zweck |
|------|-------|---------|
| Zengzi-Linien-Bibliothek | App-/Widget-Bundle | Offline-Lesen und -Lernen |
| Favoriten & Listen | Benutzerstandards der App-Gruppe | Markierte Elemente und Benutzerlisten |
| Leseverlauf / zuletzt gelesen | Benutzerstandards der App-Gruppe | Weiterlesen |
| Notizen | Benutzerstandards der App-Gruppe | Lesen von Notizen, die Sie schreiben |
| Studienfortschritt & Beherrschung | Benutzerstandards der App-Gruppe | Unterrichts-/Jagdfortschritt |
| Streak / Check-in | Benutzerstandards der App-Gruppe | Tägliche Gewohnheit |
| Aussehen & Lesepräferenzen | Benutzerstandards der App-Gruppe | Thema, Sprache, TTS, Widgets |
| Daily Reflection cache & notification prefs | UserDefaults der App Group | Heutige ID and schedule |
| Karteneinstellungen | Benutzerstandards der App-Gruppe | Letzter Stil / Verhältnis |
| Onboarding- und TipKit-Status | Standardbenutzerstandards | Willkommensführer |
| Widget-/Live-Aktivitäts-Schnappschüsse | App-Gruppe / ActivityKit | Text anzeigen, den Sie bereits geöffnet haben |

Durch die Deinstallation der App werden Sandbox- und App-Gruppendaten entfernt (je nach Betriebssystemverhalten). Optionale iCloud-Kopien bleiben in **Ihrer** iCloud, bis Sie sie löschen.

## iCloud-Synchronisierung (optional)

Wenn du **iCloud-Synchronisierung** in den Einstellungen aktivierst, spiegelt die App ausgewählte Benutzerdaten über Apples **`NSUbiquitousKeyValueStore`**, die mit **deiner Apple-ID** verknüpft ist:

- Favoriten
- Listen
- Leseverlauf
- Lernfortschritt / Kenntnisse
- Übungsserien
- Notizen
- Drei-Fragen-Tagebuch

Der Synchronisierungsverkehr geht an **Apple iCloud**, nicht an iHTC Studio. Wir können Ihre iCloud-Inhalte nicht lesen.

## Berechtigungen

iLiezi fordert Berechtigungen nur an, wenn eine Funktion diese benötigt:

| Erlaubnis | Wann | Warum |
|------------|------|-----|
| Benachrichtigungen | Sie aktivieren Daily Reflection reminders | Lokale Planung |
| Fotobibliothek (Nur hinzufügen) | Sie speichern eine Karte | Schreiben Sie das gerenderte Bild |
| iCloud | Sie aktivieren die Synchronisierung | Favoriten/Listen/Verlauf/Fortschritt/Notizen synchronisieren |
| Live-Aktivitäten (iOS) | Sie aktivieren die Lese-Live-Aktivität | Zeigen Sie die Passage auf dem Sperrbildschirm / Dynamic Island | an
| Hintergrundaudio (Fähigkeit) | Sie aktivieren die Hintergrundrezitation | TTS im Hintergrund fortsetzen |
| Health (Stimmung) | Journal-Sync in Einstellungen | Dreier-Achsen-Mark ins **Health**; nicht beim Erststart |

Wir fordern **keine** Kontakte, den genauen Standort, die Kamera, das Mikrofon (über die System-TTS-Wiedergabe hinaus) oder die Nachverfolgung an.
- HealthKit-Stimmungsschreiben **standardmäßig aus**, nicht beim Erststart.

## Was wir nicht tun

- Wir verkaufen **keine** personenbezogene Daten.
- Wir erstellen **keine** Werbeprofile.
- Wir benötigen **kein** Konto oder Social-Login.
- Wir betten zur Datenerfassung **keine** Werbung, Analysen oder soziale SDKs von Drittanbietern ein.
- Wir greifen über die Option „Nur hinzufügen“ hinaus **nicht** auf Ihre Fotobibliothek zu, wenn Sie sich für das Speichern einer Karte entscheiden.
- Wir erhalten **keine** Nummern von StoreKit-Zahlungskarten (Apple verarbeitet Zahlungen).

## Privatsphäre von Kindern

iLiezi ist eine Bildungs- und Lesekompetenz-App für ein allgemeines Publikum und gehört **nicht** zur Kategorie „Kinder“. Wir erfassen wissentlich keine personenbezogenen Daten von Kindern. Familien können Lese- und Lernfunktionen offline auf ihren eigenen Geräten nutzen.

## Dritte Parteien

- **Apple** — App Store, StoreKit, iCloud KVS, TTS, Share Sheet, Benachrichtigungen/Live Activity/Siri/Shortcuts/Vision/HealthKit
- **Keine weiteren Drittanbieter-SDKs** für Werbung, Analysen oder Social-Login sind zur Datenerfassung enthalten.

## Internationale Nutzer

Die App ist darauf ausgelegt, offline auf Ihrem Gerät zu funktionieren. Optionale Apple-Dienste unterliegen den Bedingungen von Apple und der regionalen Verfügbarkeit.

## Datenaufbewahrung & Löschung

- **Auf dem Gerät** — Löschen Sie die App, um lokale Sandbox- und App-Gruppendaten zu entfernen (abhängig vom Verhalten des Betriebssystems).
- **iCloud** — Deaktivieren Sie die Synchronisierung und löschen Sie bei Bedarf die zugehörigen Schlüssel aus Ihrem iCloud-Konto; wir können Ihr iCloud-Konto nicht für Sie löschen.
- **Wir speichern nichts** auf den iHTC Studio-Servern für diese App, da wir keine Daten sammeln.

## Richtlinienänderungen

Wir können diese Datenschutzerklärung aktualisieren. Das Datum „Zuletzt aktualisiert“ oben wird sich ändern. Die weitere Nutzung nach einer Aktualisierung bedeutet, dass Sie die überarbeitete Richtlinie akzeptieren.

## Kontakt

Fragen zum Datenschutz: [AppleOSer@gmail.com](mailto:AppleOSer@gmail.com)
