**Zuletzt aktualisiert:** 19. September 2026

iHTC Studio („wir“, „uns“ oder „unser“) hat **iBianQue** (auch bekannt als „爱扁鹊 / 愛扁鵲“, Bundle-ID `com.iHTCboy.iBianQue`) entwickelt. Diese Datenschutzrichtlinie erklärt, welche Daten beim Verwenden der App verarbeitet werden (und welche nicht). **Apple App Review** und Nutzer können sich auf **diese Seite** als öffentliche Datenschutzrichtlinie verlassen. Für App Store Connect öffnen Sie diese Datenschutzrichtlinie in Ihrem Browser und kopieren die Adresse aus der Adressleiste (die Domain der öffentlichen Seite kann sich im Laufe der Zeit ändern).

## Zusammenfassung (Übereinstimmung mit dem Apple-Datenschutzetikett)

| Thema | Unsere Praxis |
|-------|----------------|
| Konto | **Nicht erforderlich** — keine Registrierung, kein Anmelden per E-Mail oder Telefonnummer |
| Datenerhebung durch iHTC Studio | **Keine Daten gesammelt** — wir betreiben kein Backend, das Ihre persönlichen Daten empfängt |
| Netzwerk | Bibliothek, Lesen, Rezitieren, Que Study, Widgets und tägliche Benachrichtigungen funktionieren **offline** nach der Installation |
| Analysen / Werbung / Tracking | **Keine** — keine Analyse-, Werbe- oder Tracking-SDKs von Drittanbietern; keine Nutzung von App Tracking Transparency |
| Optionale Apple-Dienste | **iCloud** (Ihr privates KVS), **Fotomediathek (Nur hinzufügen)** für Lernkarten, **StoreKit** für optionales Trinkgeld, **lokale Benachrichtigungen**, optionale **Live-Aktivitäten**, optional **handschriftliche Eingabe** auf dem Gerät (Vision) |

## Datenerhebung

Wir sammeln, verkaufen oder teilen **keine** persönlichen Informationen für Werbung oder Analysen.

- **Kein Konto** — Sie können alle Kernfunktionen nutzen, ohne ein Konto bei uns zu erstellen.
- **Keine Analysen oder Werbung** — Die App-Binärdatei integriert keine Analyse-, Werbe- oder Absturzbericht-SDKs von Drittanbietern, die Daten an uns senden.
- **Kein Hochladen von Inhalten** — Ihr Leseverlauf, Favoriten, Listen, Notizen, Lernfortschritt und Einstellungen bleiben auf Ihrem Gerät (und optional in **Ihrem** iCloud-Konto). Sie werden niemals auf iHTC Studio Server hochgeladen, da **wir solche Server für diese App nicht betreiben**.

Vier Untersuchungs-Szenen, Meridian-Atlas-Taps und die Zungenskizze auf dem Gerät bleiben lokal. Sie sind kulturelle Diagramme. Sie sind **keine** Diagnose, Verschreibung oder HealthKit-Integration.

## So funktioniert die App

- **Gebündelte Bibliothek** – JSON-Text, Umgangssprache/Englisch, Indizes und Lernhilfen sind im App-/Widget-Paket enthalten. 
- **Sprache auf dem Gerät** – Die Rezitation nutzt Apples System **AVSpeechSynthesizer** (TTS). Wir senden keine Passagentexte an iHTC Studio. 
- **Widgets & App-Gruppe** – Widgets und die App-Freigabeeinstellungen über die App-Gruppe `group.com.iHTCboy.iBianQue` auf Ihrem Gerät. 
- **Tägliche Benachrichtigungen** – Lokal geplant. Durch Tippen auf eine Benachrichtigung wird ein Deep-Link auf dem Gerät geöffnet. 
- **Lernkarten** – Bilder werden auf dem Gerät gerendert. Beim Speichern wird **nur die Add-On-Fotobibliothek** verwendet, wenn Sie auf „Speichern“ tippen. 
- **Handschriftsuche (iOS)** – Die optionale Zeichenerkennung verwendet Apple **Vision** auf dem Gerät. Striche werden nicht hochgeladen. 
- **Optionaler Tipp** – „Tip Developer“ ist ein verbrauchbarer **StoreKit**-Kauf, der von Apple abgewickelt wird. 
- **Siri / Verknüpfungen / Kontrollzentrum** – Optionale Systemintegrationen öffnen Deep Links auf dem Gerät. 
- **Optionales Spotlight** – Wenn Sie die Indizierung aktivieren, indiziert das System Inhalte auf dem Gerät. 

## Auf Ihrem Gerät gespeicherte Daten

| Daten | Wo | Zweck | 
|------|-------|---------| 
| Bian Que / Nan Jing-Bibliothek | App-/Widget-Bundle | Offline-Lesen und Lernen | 
| Favoriten & Listen | Benutzerstandards der App-Gruppe | Markierte Elemente und Benutzerlisten | 
| Leseverlauf / zuletzt gelesen | Benutzerstandards der App-Gruppe | Weiterlesen | 
| Notizen | Benutzerstandards der App-Gruppe | Lesen von Notizen, die Sie schreiben | 
| Studienfortschritt & Beherrschung | Benutzerstandards der App-Gruppe | Unterrichts-/Jagdfortschritt | 
| Streak / Check-in | Benutzerstandards der App-Gruppe | Tägliche Gewohnheit | 
| Aussehen & Lesepräferenzen | Benutzerstandards der App-Gruppe | Thema, Sprache, TTS, Widgets | 
| Tägliche Kunst-Cache- und Benachrichtigungseinstellungen | Benutzerstandards der App-Gruppe | Heutiger Ausweis und Zeitplan | 
| Karteneinstellungen | Benutzerstandards der App-Gruppe | Letzter Stil / Verhältnis | 
| Onboarding- und TipKit-Status | Standardbenutzerstandards | Willkommensführer | 
| Widget-/Live-Aktivitäts-Schnappschüsse | App-Gruppe / ActivityKit | Text anzeigen, den Sie bereits geöffnet haben | 

Durch die Deinstallation der App werden Sandbox- und App-Gruppendaten entfernt (je nach Betriebssystemverhalten). Optionale iCloud-Kopien bleiben in **Ihrer** iCloud, bis Sie sie löschen. 

## iCloud-Synchronisierung (optional)

Wenn Sie **iCloud Sync** in den Einstellungen aktivieren, spiegelt die App ausgewählte Benutzerdaten über Apples **`NSUbiquitousKeyValueStore`**, das an **Ihre Apple-ID** gebunden ist: 

- Favoriten 
- Listen 
- Geschichte lesen 
- Studienfortschritt / Beherrschung 
- Übungssträhnen 
- Notizen 

Der Synchronisierungsverkehr geht an **Apple iCloud**, nicht an iHTC Studio. Wir können Ihre iCloud-Inhalte nicht lesen. 

## Berechtigungen 

iBianQue fordert Berechtigungen nur an, wenn eine Funktion diese benötigt: 

| Erlaubnis | Wann | Warum | 
|------------|------|-----| 
| Benachrichtigungen | Sie aktivieren tägliche Kunsterinnerungen | Lokale Planung | 
| Fotobibliothek (Nur hinzufügen) | Sie speichern eine Karte | Schreiben Sie das gerenderte Bild | 
| iCloud | Sie aktivieren die Synchronisierung | Favoriten/Listen/Verlauf/Fortschritt/Notizen synchronisieren | 
| Live-Aktivitäten (iOS) | Sie aktivieren die Lese-Live-Aktivität | Zeigen Sie die Passage auf dem Sperrbildschirm / Dynamic Island | an 
| Hintergrundaudio (Fähigkeit) | Sie aktivieren die Hintergrundrezitation | TTS im Hintergrund fortsetzen | 

Wir fordern **keine** Kontakte, den genauen Standort, die Kamera, das Mikrofon (über die System-TTS-Wiedergabe hinaus) oder die Nachverfolgung an. 

## Was wir nicht tun

- Wir verkaufen **keine** personenbezogene Daten. 
- Wir erstellen **keine** Werbeprofile. 
- Wir benötigen **kein** Konto oder Social-Login. 
- Wir betten zur Datenerfassung **keine** Werbung, Analysen oder soziale SDKs von Drittanbietern ein. 
- Wir greifen über die Option „Nur hinzufügen“ hinaus **nicht** auf Ihre Fotobibliothek zu, wenn Sie sich für das Speichern einer Karte entscheiden. 
- Wir erhalten **keine** Nummern von StoreKit-Zahlungskarten (Apple verarbeitet Zahlungen). 

## Privatsphäre von Kindern 

iBianQue ist eine Bildungs- und Lesekompetenz-App für ein allgemeines Publikum und gehört **nicht** zur Kategorie „Kinder“. Wir erfassen wissentlich keine personenbezogenen Daten von Kindern. Familien können Lese- und Lernfunktionen offline auf ihren eigenen Geräten nutzen. 

## Dritte 

- **Apple** – App Store-Verteilung, optionales StoreKit, optionales iCloud KVS, System-TTS, von Ihnen ausgewählte Share Sheet-Ziele und Benachrichtigung auf Betriebssystemebene/Live-Aktivität/Siri/Verknüpfungen/Vision-Bereitstellung. 
- **Für die Datenerfassung sind keine weiteren SDKs von Drittanbietern** für Anzeigen, Analysen oder Social-Login enthalten. 

## Internationale Benutzer 

Die App ist so konzipiert, dass sie offline auf Ihrem Gerät funktioniert. Optionale Apple-Dienste unterliegen den Geschäftsbedingungen und der regionalen Verfügbarkeit von Apple. 

## Datenaufbewahrung und -löschung

- **Auf dem Gerät** — Löschen Sie die App, um lokale Sandbox- und App-Gruppendaten zu entfernen (abhängig vom Verhalten des Betriebssystems).
- **iCloud** — Deaktivieren Sie die Synchronisierung und löschen Sie bei Bedarf die zugehörigen Schlüssel aus Ihrem iCloud-Konto; wir können Ihr iCloud-Konto nicht für Sie löschen.
- **Wir speichern nichts** auf den iHTC Studio-Servern für diese App, da wir keine Daten sammeln.

## Richtlinienänderungen

Wir können diese Datenschutzerklärung aktualisieren. Das Datum „Zuletzt aktualisiert“ oben wird sich ändern. Die weitere Nutzung nach einer Aktualisierung bedeutet, dass Sie die überarbeitete Richtlinie akzeptieren.

## Kontakt

Fragen zum Datenschutz: [AppleOSer@gmail.com](mailto:AppleOSer@gmail.com)
