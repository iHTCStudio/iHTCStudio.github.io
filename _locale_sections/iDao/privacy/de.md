**Zuletzt aktualisiert:** 3. August 2026

iHTC Studio („wir“, „uns“ oder „unser“) hat **iDao** (auch bekannt als „爱道德经“ / „愛道德經“, Bundle-ID `com.iHTCboy.iDao`) entwickelt. Diese Datenschutzrichtlinie erklärt, welche Daten beim Nutzen der App verarbeitet werden (und welche nicht). **Apple App Review** und Nutzer können sich auf **diese Seite** als die öffentliche Datenschutzrichtlinie der App verlassen. Für App Store Connect öffnen Sie diese Datenschutzrichtlinie in Ihrem Browser und kopieren Sie die Adresse aus der Adressleiste (die öffentliche Domain der Seite kann sich im Laufe der Zeit ändern).

## Zusammenfassung (Übereinstimmung mit dem Apple-Datenschutzetikett)

| Thema | Unsere Praxis |
|-------|----------------|
| Konto | **Nicht erforderlich** — keine Registrierung, kein E-Mail-Login oder Telefonnummer |
| Datenerfassung durch iHTC Studio | **Keine Datenerfassung** — wir betreiben **kein** Backend, das Ihre persönlichen Daten empfängt |
| Netzwerk | Bibliothek, Lesen, Rezitieren, Studierhalle, Den Dao suchen, Widgets und tägliche Benachrichtigungen funktionieren **offline** nach der Installation |
| Analysen / Werbung / Tracking | **Keine** — keine Analytik, Werbung oder Tracking-SDKs von Drittanbietern; keine Nutzung von App Tracking Transparency |
| Optionale Apple-Dienste | **iCloud** (Ihr privates KVS, bidirektionale Zusammenführung), **Fotobibliothek (Nur Hinzufügen)** für Dao-Karten, **StoreKit** für freiwillige Trinkgelder, **lokale Benachrichtigungen**, optionale **Live-Aktivitäten** |

## Datenerfassung

Wir erfassen, verkaufen oder teilen **keine** persönlichen Informationen für Werbung oder Analysen.

- **Kein Konto** — Sie können alle Hauptfunktionen nutzen, ohne ein Konto bei uns zu erstellen.
- **Keine Analyse oder Werbung** — Die App-Binärdatei integriert keine Drittanbieter-Analyse-, Werbe- oder Absturzbericht-SDKs, die Daten an uns zurücksenden.
- **Kein Hochladen von Inhalten** — Ihr Leseverlauf, Favoriten, Listen, Notizen, Beherrschungen, Serien und Einstellungen bleiben auf Ihrem Gerät (und optional in **Ihrem** iCloud). Sie werden niemals auf iHTC Studio-Server hochgeladen, da **wir für diese App keine solchen Server betreiben**.

## So funktioniert die App

- **Gebündelte Bibliothek** – Kapitel JSON, Umgangssprache, Pinyin, Kommentare, englische Ausgaben, berühmte Zeilen und Indizes sind im App-/Widget-Paket enthalten. Zum Durchsuchen und Studieren ist keine Netzwerkanfrage erforderlich. 
- **Sprache auf dem Gerät** – Die Rezitation nutzt Apples System **AVSpeechSynthesizer** (TTS). Wir senden keinen Kapiteltext an iHTC Studio. 
- **Widgets & App-Gruppe** – Widgets und die App teilen ihre Präferenzen und ihren Lightweight-Status über die App-Gruppe `group.com.iHTCboy.iDao` auf Ihrem Gerät. 
- **Tägliche Benachrichtigungen** – Lokal geplant mit Benutzerbenachrichtigungen. Durch Tippen auf eine Benachrichtigung wird ein Deep-Link zu einer Kapitel-ID auf dem Gerät geöffnet. Kein Server-Fanout. 
- **Dao-Karten** – Bilder werden auf dem Gerät gerendert. Beim Speichern wird **nur die Add-On-Fotobibliothek** verwendet, wenn Sie auf „Speichern“ tippen. Das System Share Sheet sendet das Bild möglicherweise an eine von Ihnen ausgewählte App. Es gelten dann die Datenschutzbestimmungen dieses Reiseziels. 
- **Optionaler Tipp** – „Tip Developer“ ist ein verbrauchbarer **StoreKit**-Kauf, der von Apple abgewickelt wird. Wir erhalten Ihre Zahlungskartendaten nicht. 
- **Siri / Verknüpfungen / Kontrollzentrum** – Optionale Systemintegrationen öffnen Deep Links auf dem Gerät; Sie senden Ihre Bibliothek nicht an uns. 
- **Optionales Spotlight** – standardmäßig deaktiviert. Wenn Sie die Indizierung aktivieren, wird der Inhalt vom System auf dem Gerät für die lokale Suche indiziert; Wir betreiben kein Such-Backend.

## Auf Ihrem Gerät gespeicherte Daten 

| Daten | Wo | Zweck | 
|------|-------|---------| 
| Kapiteldatenbank (inkl. Pinyin-/Notizenausgaben) | App-/Widget-Bundle | Offline-Lesen und Lernen | 
| Favoriten & Listen (道单) | Benutzerstandards der App-Gruppe | Markierte Kapitel und Benutzerlisten | 
| Leseverlauf / zuletzt gelesen | Benutzerstandards der App-Gruppe | Lesen Sie weiter, Verlauf der Benutzeroberfläche | 
| Studienfortschritt & Beherrschung | Benutzerstandards der App-Gruppe | Study Hall Zustand, Quiz / Suche nach dem Tao-Fortschritt | 
| Notizen | Benutzerstandards der App-Gruppe | Kapitelnotizen, die Sie schreiben | 
| Übungssträhne / Check-in | Benutzerstandards der App-Gruppe | Tägliche Gewohnheit | 
| Aussehen & Lesepräferenzen | Benutzerstandards der App-Gruppe | Thema, Akzent, Sprache, Layout, TTS, Tabs, Widgets | 
| Täglicher Kapitel-Cache und Benachrichtigungseinstellungen | Benutzerstandards der App-Gruppe | Heutige ID, Zeitplanzeit, kontextbezogenes Umschalten | 
| Share-Card-Einstellungen | Benutzerstandards der App-Gruppe | Letzte Stil-/Verhältnisauswahl | 
| Onboarding- und TipKit-Status | Standard UserDefaults (Gerät) | Willkommensführer / Entdeckungstipps | 
| Schnellaktionen auf dem Startbildschirm | System + lokale Einstellungen | Von Ihnen konfigurierte Verknüpfungen | 
| Widget-/Live-Aktivitäts-Schnappschüsse | App-Gruppe / ActivityKit | Text anzeigen, den Sie bereits geöffnet haben |

Das Deinstallieren der App entfernt Sandbox- und App-Gruppendaten, die mit der App verbunden sind (abhängig vom Verhalten von iOS/macOS). Optionale iCloud-Kopien bleiben in **deiner** iCloud, bis du sie löschst oder die Synchronisierung ausschaltest und anderswo löschst.

## iCloud-Synchronisierung (Optional)

Wenn du die **iCloud-Synchronisierung** in den Einstellungen aktivierst, spiegeln die ausgewählten Benutzerdaten der App Apples **`NSUbiquitousKeyValueStore`** wider, die mit **deiner Apple-ID** verbunden ist, unter Verwendung der **bidirektionalen Zusammenführung** (Favoriten, Listen, Verlauf, Meisterung, Notizen, Streaks), sodass Cloud- und Geräte-Updates kombiniert werden, anstatt einfach überschrieben zu werden.

Der Synchronisationsverkehr geht zu **Apple iCloud**, nicht zu iHTC Studio. Du kannst die Synchronisierung in den Einstellungen deaktivieren. Wir können deine iCloud-Inhalte nicht lesen.

## Berechtigungen

iDao fordert Berechtigungen nur an, wenn eine Funktion sie benötigt:

| Erlaubnis | Wann | Warum | 
|------------|------|-----| 
| Benachrichtigungen | Sie aktivieren tägliche Kapitelerinnerungen | Lokale Planung von Erinnerungsbenachrichtigungen | 
| Fotobibliothek (Nur hinzufügen) | Sie speichern eine Dao-Karte | Schreiben Sie das gerenderte Bild. Wir benötigen keinen vollständigen Lesezugriff auf die Bibliothek | 
| iCloud | Sie aktivieren die Synchronisierung | Favoriten / Listen / Verlauf / Meisterschaft / Notizen / Streifen | synchronisieren 
| Live-Aktivitäten (iOS) | Sie aktivieren die Lese-Live-Aktivität | Zeigen Sie das Kapitel, das Sie gerade lesen, auf dem Sperrbildschirm/Dynamic Island | an 
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

iDao sammelt wissentlich keine persönlichen Daten von irgendjemandem, einschließlich Kindern unter 13 Jahren (oder dem entsprechenden Alter in Ihrer Region). Da wir kein Backend zur Datenerfassung betreiben, wird bei uns kein Kinderprofil gespeichert. Familien können die Lese- und Lernfunktionen offline auf ihren eigenen Geräten nutzen.

## Dritte Parteien

- **Apple** — App Store-Verteilung, optionale StoreKit-Käufe, optionales iCloud KVS, systemweite TTS, von Ihnen ausgewählte Share Sheet-Ziele sowie OS-Ebene-Benachrichtigungen / Live-Aktivitäten / Siri / Kurzbefehle.
- **Keine anderen Drittanbieter-SDKs** für Werbung, Analysen oder soziale Anmeldung sind für die Datenerfassung enthalten.

## Internationale Nutzer

Die App ist so konzipiert, dass sie offline auf Ihrem Gerät funktioniert. Optionale Apple-Dienste unterliegen den Nutzungsbedingungen von Apple und der regionalen Verfügbarkeit.

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
