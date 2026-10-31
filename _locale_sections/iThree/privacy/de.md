**Zuletzt aktualisiert:** 31. Juli 2026

iHTC Studio („wir“, „uns“ oder „unser“) hat **iThree** (auch bekannt als „爱三字经“ / „愛三字經“, Bundle-ID `com.iHTCboy.iThree`) entwickelt. Diese Datenschutzrichtlinie erklärt, welche Daten beim Nutzen der App verarbeitet werden (und welche nicht). **Apple App Review** und Nutzer können sich auf **diese Seite** als die öffentliche Datenschutzrichtlinie der App verlassen. Für App Store Connect öffnen Sie diese Datenschutzrichtlinie in Ihrem Browser und kopieren Sie die Adresse aus der Adressleiste (die öffentliche Domain der Seite kann sich im Laufe der Zeit ändern).

## Zusammenfassung (Übereinstimmung mit dem Apple-Datenschutzetikett)

| Thema | Unsere Praxis |
|-------|----------------|
| Konto | **Nicht erforderlich** — keine Registrierung, kein E-Mail-Login oder Telefonnummer erforderlich |
| Datenerhebung durch iHTC Studio | **Keine Datenerhebung** — wir betreiben **keinen** Backend-Service, der Ihre persönlichen Daten empfängt |
| Netzwerk | Bibliothek, Lesen, Rezitieren, Lernen, Hunt, Widgets und tägliche Benachrichtigungen funktionieren **offline** nach der Installation |
| Analysen / Werbung / Tracking | **Keine** — keine Analysen von Drittanbietern, Werbung oder Tracking-SDKs; keine Nutzung von App Tracking Transparency |
| Optionale Apple-Dienste | **iCloud** (Ihr privates KVS), **Fotobibliothek (Nur Hinzufügen)** für geteilte Karten, **StoreKit** für optionale Trinkgelder, **lokale Benachrichtigungen**, optionale **Live-Aktivitäten** |

## Datenerhebung

Wir erheben, verkaufen oder teilen **keine** persönlichen Informationen für Werbung oder Analysen.

- **Kein Konto** — Sie können alle Kernfunktionen nutzen, ohne ein Konto bei uns zu erstellen.
- **Keine Analysen oder Werbung** — Die App-Binärdatei integriert keine Analysen, Werbung oder Crash-Reporting-SDKs von Drittanbietern, die Daten an uns senden.
- **Kein Hochladen von Inhalten** — Ihr Leseverlauf, Favoriten (einschließlich Story-Favoriten), Listen von Zeilen, Lernfortschritt, Serien und Einstellungen bleiben auf Ihrem Gerät (und optional in **Ihrem** iCloud-Konto). Sie werden niemals auf iHTC Studio-Server hochgeladen, da **wir solche Server für diese App nicht betreiben**.

## So funktioniert die App

- **Gebündelte Bibliothek** – Passage JSON, Zeichen-Pinyin, Umgangssprache/Englisch, Geschichten, klassische Indizes und Dynastien werden im App-/Widget-Bundle geliefert. Zum Durchsuchen und Studieren ist keine Netzwerkanfrage erforderlich. 
- **Sprache auf dem Gerät** – Die Rezitation nutzt Apples System **AVSpeechSynthesizer** (TTS). Wir senden keine Passagentexte an iHTC Studio. 
- **Widgets & App-Gruppe** – Widgets und die App teilen ihre Präferenzen und ihren Lightweight-Status über die App-Gruppe `group.com.iHTCboy.iThree` auf Ihrem Gerät. 
- **Tägliche Benachrichtigungen** – Lokal geplant mit Benutzerbenachrichtigungen. Durch Tippen auf eine Benachrichtigung wird ein Deep-Link zu einer Durchgangs-ID auf dem Gerät geöffnet. Kein Server-Fanout. 
- **Karten teilen** – Bilder werden auf dem Gerät gerendert. Beim Speichern wird **nur die Add-On-Fotobibliothek** verwendet, wenn Sie auf „Speichern“ tippen. Das System Share Sheet sendet das Bild möglicherweise an eine von Ihnen ausgewählte App. Es gelten dann die Datenschutzbestimmungen dieses Reiseziels. 
- **Optionaler Tipp** – „Tip Developer“ ist ein verbrauchbarer **StoreKit**-Kauf, der von Apple abgewickelt wird. Wir erhalten Ihre Zahlungskartendaten nicht. 
- **Siri / Verknüpfungen / Kontrollzentrum** – Optionale Systemintegrationen öffnen Deep Links auf dem Gerät; Sie senden Ihre Bibliothek nicht an uns. 
- **Optionales Spotlight** – Wenn Sie die Indizierung aktivieren, werden Inhalte vom System auf dem Gerät für die lokale Suche indiziert; Wir betreiben kein Such-Backend.

## Auf Ihrem Gerät gespeicherte Daten 

| Daten | Wo | Zweck | 
|------|-------|---------| 
| Passage-Datenbank (inkl. Pinyin) | App-/Widget-Bundle | Offline-Lesen und Lernen | 
| Favoriten & Leitungslisten | Benutzerstandards der App-Gruppe | Markierte Passagen/Geschichten und Benutzerlisten | 
| Leseverlauf / zuletzt gelesen | Benutzerstandards der App-Gruppe | Lesen Sie weiter, Verlauf der Benutzeroberfläche | 
| Studienfortschritt & Beherrschung | Benutzerstandards der App-Gruppe | Unterrichtszustand, Quiz/Jagdfortschritt | 
| Übungssträhne / Check-in | Benutzerstandards der App-Gruppe | Tägliche Gewohnheit | 
| Aussehen & Lesepräferenzen | Benutzerstandards der App-Gruppe | Thema, Akzent, Sprache, Layout, TTS, Tabs, Widgets | 
| Daily Line-Cache- und Benachrichtigungseinstellungen | Benutzerstandards der App-Gruppe | Heutige ID, Zeitplanzeit, kontextbezogenes Umschalten | 
| Share-Card-Einstellungen | Benutzerstandards der App-Gruppe | Letzte Stil-/Verhältnisauswahl | 
| Onboarding- und TipKit-Status | Standard UserDefaults (Gerät) | Willkommensführer / Entdeckungstipps | 
| Schnellaktionen auf dem Startbildschirm | System + lokale Einstellungen | Von Ihnen konfigurierte Verknüpfungen | 
| Widget-/Live-Aktivitäts-Schnappschüsse | App-Gruppe / ActivityKit | Text anzeigen, den Sie bereits geöffnet haben |

Die Deinstallation der App entfernt Sandbox- und App-Gruppendaten, die mit der App verbunden sind (abhängig vom Verhalten von iOS/macOS). Optionale iCloud-Kopien bleiben in **deiner** iCloud, bis du sie löschst oder die Synchronisierung ausschaltest und anderswo löschst.

## iCloud-Synchronisierung (optional)

Wenn du **iCloud-Synchronisierung** in den Einstellungen aktivierst, spiegelt die App ausgewählte Benutzerdaten über Apples **`NSUbiquitousKeyValueStore`**, die mit **deiner Apple-ID** verknüpft ist:

- Passage-Favoriten
- Story-Favoriten
- Linienlisten
- Leseverlauf
- Lernfortschritt / Kenntnisse
- Übungsserien

Der Synchronisationsverkehr geht an **Apple iCloud**, nicht an iHTC Studio. Du kannst die Synchronisierung in den Einstellungen deaktivieren. Wir können deine iCloud-Inhalte nicht lesen.

## Berechtigungen

iThree fordert Berechtigungen nur an, wenn eine Funktion diese benötigt:

| Erlaubnis | Wann | Warum | 
|------------|------|-----| 
| Benachrichtigungen | Sie aktivieren Daily Line-Erinnerungen | Lokale Planung von Erinnerungsbenachrichtigungen | 
| Fotobibliothek (Nur hinzufügen) | Sie speichern eine Share-Karte | Schreiben Sie das gerenderte Bild. Wir benötigen keinen vollständigen Lesezugriff auf die Bibliothek | 
| iCloud | Sie aktivieren die Synchronisierung | Favoriten/Listen/Verlauf/Fortschritt/Streaks synchronisieren | 
| Live-Aktivitäten (iOS) | Sie aktivieren die Lese-Live-Aktivität | Zeigen Sie die Passage, die Sie gerade lesen, auf dem Sperrbildschirm/Dynamic Island | an 
| Hintergrundaudio (Fähigkeit) | Sie aktivieren die Hintergrundrezitation | TTS fortsetzen, wenn die App nicht im Vordergrund ist | 

Wir fordern **keine** Kontakte, den genauen Standort, die Kamera, das Mikrofon (über die System-TTS-Wiedergabe hinaus) oder die Nachverfolgung an. 

## Was wir nicht tun 

- Wir verkaufen **keine** personenbezogene Daten. 
- Wir erstellen **keine** Werbeprofile. 
- Wir benötigen **kein** Konto oder Social-Login. 
- Wir betten zur Datenerfassung **keine** Werbung, Analysen oder soziale SDKs von Drittanbietern ein. 
- Wir greifen über die Option „Nur hinzufügen“ hinaus **nicht** auf Ihre Fotobibliothek zu, wenn Sie sich für das Speichern einer Karte entscheiden. 
- Wir erhalten **keine** Nummern von StoreKit-Zahlungskarten (Apple verarbeitet Zahlungen). 

## Privatsphäre von Kindern

iThree sammelt wissentlich keine persönlichen Daten von irgendjemandem, einschließlich Kindern unter 13 Jahren (oder dem entsprechenden Alter in Ihrer Region). Da wir keine Daten-Sammel-Backend betreiben, wird kein Kinderprofil bei uns gespeichert. Familien können die Lese- und Studienfunktionen offline auf ihren eigenen Geräten nutzen.

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
