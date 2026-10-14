**Zuletzt aktualisiert:** 5. August 2026

iHTC Studio („wir“, „uns“ oder „unser“) hat **iYijing** (auch bekannt als „爱周易“ / „愛周易“, Bundle-ID `com.iHTCboy.iYiJing`) erstellt. Diese Datenschutzrichtlinie erklärt, welche Daten beim Verwenden der App verarbeitet werden (und welche nicht). **Apple App Review** und Benutzer können sich auf **diese Seite** als öffentliche Datenschutzrichtlinie der App verlassen. Für App Store Connect öffnen Sie diese Datenschutzrichtlinie in Ihrem Browser und kopieren die Adresse aus der Adressleiste (die öffentliche Domain kann sich im Laufe der Zeit ändern).

## Zusammenfassung (Ausrichtung am Apple-Datenschutz-Nährwertetikett)

| Thema | Unsere Praxis |
|-------|----------------|
| Konto | **Nicht erforderlich** — keine Registrierung, kein E-Mail-Anmeldung oder Telefonnummer |
| Datenerhebung durch iHTC Studio | **Daten werden nicht erhoben** — wir betreiben **kein** Backend, das Ihre persönlichen Daten empfängt |
| Netzwerk | Bibliothek, Lesen, Rezitieren, kulturelle Wiedergabe, Study Hall, Widgets und tägliche Benachrichtigungen funktionieren **offline** nach der Installation |
| Analysen / Werbung / Tracking | **Keine** — keine Analytik, Werbung oder Tracking-SDKs von Drittanbietern; keine Nutzung von App Tracking Transparency |
| Optionale Apple-Dienste | **iCloud** (Ihr privates KVS, Zusammenführen), **Fotobibliothek (Nur Hinzufügen)** für Lernkarten, **StoreKit** für optionale Trinkgelder, **lokale Benachrichtigungen**, optionale **Live-Aktivitäten** |

## Datenerhebung

Wir erfassen, verkaufen oder teilen keine persönlichen Informationen für Werbung oder Analysen.

- **Kein Konto** — Sie können alle Kernfunktionen nutzen, ohne ein Konto bei uns zu erstellen.
- **Keine Analysen oder Werbung** — Die App-Binärdatei integriert keine Drittanbieter-Analyse-, Werbe- oder Absturzbericht-SDKs, die Daten an uns senden.
- **Kein Hochladen von Inhalten** — Ihr Leseverlauf, Favoriten, Listen, Notizen, Casting-Aufzeichnungen, falsche Bücher, Meisterschaft, Serien und Einstellungen bleiben auf Ihrem Gerät (und optional in **Ihrem** iCloud). Sie werden niemals auf die Server von iHTC Studio hochgeladen, da **wir für diese App keine solchen Server betreiben**.

## Wie die App funktioniert

- **Gebündelte Bibliothek** – Hexagramm JSON, Ten Wings, Trigramme, berühmte Linien und Indizes werden im App-/Widget-Bundle geliefert. Zum Durchsuchen und Studieren ist keine Netzwerkanfrage erforderlich. 
- **Sprache auf dem Gerät** – Die Rezitation nutzt Apples System **AVSpeechSynthesizer** (TTS). Wir senden keinen Hexagrammtext an iHTC Studio. 
- **Kulturguss** – Münz- und Schafgarbenverfahren laufen ausschließlich auf der Grundlage pädagogischer Symbolik; Datensätze, die Sie speichern möchten, bleiben lokal (und optional in Ihrer iCloud). 
- **Widgets & App-Gruppe** – Widgets und die App teilen ihre Präferenzen und ihren Lightweight-Status über die App-Gruppe `group.com.iHTCboy.iYiJing` auf Ihrem Gerät. 
- **Tägliche Benachrichtigungen** – Lokal geplant mit Benutzerbenachrichtigungen. Durch Antippen wird ein Deep-Link zu einer Hexagramm-ID auf dem Gerät geöffnet. Kein Server-Fanout. 
- **Lernkarten** – Bilder werden auf dem Gerät gerendert. Beim Speichern wird **nur die Add-On-Fotobibliothek** verwendet, wenn Sie auf „Speichern“ tippen. Das System Share Sheet sendet das Bild möglicherweise an eine von Ihnen ausgewählte App. Es gelten dann die Datenschutzbestimmungen dieses Reiseziels. 
- **Optionaler Tipp** – „Tip Developer“ ist ein verbrauchbarer **StoreKit**-Kauf, der von Apple abgewickelt wird. Wir erhalten Ihre Zahlungskartendaten nicht. 
- **Siri / Verknüpfungen / Kontrollzentrum** – Optionale Systemintegrationen öffnen Deep Links auf dem Gerät; Sie senden Ihre Bibliothek nicht an uns. 
- **Optionales Spotlight** – Wenn Sie die Indizierung aktivieren, werden Inhalte vom System auf dem Gerät für die lokale Suche indiziert; Wir betreiben kein Such-Backend. 
- **Optionale Live-Aktivität** – standardmäßig deaktiviert; Wenn diese Option aktiviert ist, wird das Hexagramm, das Sie gerade lesen, auf dem Sperrbildschirm/Dynamic Island angezeigt.

## Auf Ihrem Gerät gespeicherte Daten 

| Daten | Wo | Zweck | 
|------|-------|---------| 
| Hexagramm-/Flügel-/Trigramm-Datenbank | App-/Widget-Bundle | Offline-Lesen und Lernen | 
| Favoriten- und Hexagrammlisten | Benutzerstandards der App-Gruppe | Markierte Werke und Benutzerlisten | 
| Leseverlauf / zuletzt gelesen | Benutzerstandards der App-Gruppe | Lesen Sie weiter, Verlauf der Benutzeroberfläche | 
| Studienfortschritt, Meisterschaft und falsches Buch | Benutzerstandards der App-Gruppe | Studiensaal Zustand | 
| Casting-Aufzeichnungen | Benutzerstandards der App-Gruppe | Kulturelle Casting-Geschichte, die Sie retten | 
| Notizen | Benutzerstandards der App-Gruppe | Notizen, die Sie schreiben | 
| Streak / Check-in | Benutzerstandards der App-Gruppe | Tägliche Gewohnheit | 
| Aussehen & Lesepräferenzen | Benutzerstandards der App-Gruppe | Thema, Akzent, Sprache, Layout, TTS, Tabs, Widgets | 
| Täglicher Hexagramm-Cache und Benachrichtigungseinstellungen | Benutzerstandards der App-Gruppe | Heutiger Ausweis, geplante Uhrzeit | 
| Share-Card-Einstellungen | Benutzerstandards der App-Gruppe | Letzte Stil-/Verhältnisauswahl | 
| Onboarding-Status | Standard UserDefaults (Gerät) | Willkommensführer | 
| Widget-/Live-Aktivitäts-Schnappschüsse | App-Gruppe / ActivityKit | Text anzeigen, den Sie bereits geöffnet haben |

Die Deinstallation der App entfernt Sandbox- und App-Gruppen-Daten, die mit der App verbunden sind (abhängig vom Verhalten von iOS/macOS). Optionale iCloud-Kopien bleiben in **deinem** iCloud, bis du sie löschst oder die Synchronisierung ausschaltest und sie anderweitig löscht.

## iCloud-Synchronisierung (Optional)

Wenn du die **iCloud-Synchronisierung** in den Einstellungen aktivierst, spiegelt die App ausgewählte Benutzerdaten über **Apple’s `NSUbiquitousKeyValueStore`**, die mit **deiner Apple-ID** verknüpft ist, unter Verwendung von Zusammenführungsregeln für Favoriten, Listen, Verlauf, Meisterschaft, Notizen, Casting-Aufzeichnungen, Falschbuch und Serien.

Synchronisierungsverkehr geht zu **Apple iCloud**, nicht zu iHTC Studio. Du kannst die Synchronisierung in den Einstellungen deaktivieren. Wir können deine iCloud-Inhalte nicht einsehen.

## Berechtigungen

iYijing fordert Berechtigungen nur an, wenn eine Funktion sie benötigt:

| Berechtigung | Wann | Warum |
|------------|------|-----|
| Benachrichtigungen | Wenn Sie tägliche Hexagramm-Erinnerungen aktivieren | Lokale Planung von Erinnerungsbenachrichtigungen |
| Foto-Bibliothek (nur hinzufügen) | Wenn Sie eine Lernkarte speichern | Das gerenderte Bild speichern; wir benötigen keinen vollen Zugriff auf die Bibliothek |
| iCloud | Wenn Sie die Synchronisation aktivieren | Favoriten / Listen / Verlauf / Beherrschung / Notizen / Ziehen / Falsches Buch / Serien synchronisieren |
| Live-Aktivitäten (iOS) | Wenn Sie die Leselige Live-Aktivität aktivieren | Zeigt das Hexagramm, das Sie lesen, auf dem Sperrbildschirm / Dynamic Island an |
| Hintergrund-Audio (Funktion) | Wenn Sie Hintergrundrezitation aktivieren | Text-to-Speech fortsetzen, wenn die App nicht im Vordergrund ist |

Wir fordern **nicht** Kontakte, exakte Standortdaten, Kamera, Mikrofon (außer für systeminterne TTS-Wiedergabe) oder Tracking an.

## Was wir nicht tun

- Wir verkaufen **keine** personenbezogene Daten. 
- Wir erstellen **keine** Werbeprofile. 
- Wir benötigen **kein** Konto oder Social-Login. 
- Wir betten zur Datenerfassung **keine** Werbung, Analysen oder soziale SDKs von Drittanbietern ein. 
- Wir greifen über die Option „Nur hinzufügen“ hinaus **nicht** auf Ihre Fotobibliothek zu, wenn Sie sich für das Speichern einer Karte entscheiden. 
- Wir erhalten **keine** Nummern von StoreKit-Zahlungskarten (Apple verarbeitet Zahlungen). 
- Wir senden **keine** Casting-Fragen oder Ergebnisse an einen Server. 

## Privatsphäre von Kindern 

iYijing erfasst wissentlich keine personenbezogenen Daten von irgendjemandem, auch nicht von Kindern unter 13 Jahren (oder dem entsprechenden Alter in Ihrer Region). Da wir kein Datenerfassungs-Backend betreiben, wird bei uns kein Kinderprofil gespeichert. Familien können die Lese- und Lernfunktionen offline auf ihren eigenen Geräten nutzen. 

## Dritte 

- **Apple** – App Store-Verteilung, optionale StoreKit-Käufe, optionales iCloud KVS, System-TTS, von Ihnen ausgewählte Share Sheet-Ziele und Benachrichtigungen auf Betriebssystemebene/Live-Aktivität/Siri/Shortcuts-Bereitstellung. 
- **Für die Datenerfassung sind keine weiteren SDKs von Drittanbietern** für Anzeigen, Analysen oder Social-Login enthalten. 

## Internationale Benutzer

Die App ist so konzipiert, dass sie offline auf Ihrem Gerät funktioniert. Optionale Apple-Dienste unterliegen den Geschäftsbedingungen und der regionalen Verfügbarkeit von Apple. 

## Datenaufbewahrung und -löschung 

- **Auf dem Gerät** – Lokale Einstellungen und Fortschritte bleiben erhalten, bis Sie sie in der App löschen (sofern verfügbar), das Gerät zurücksetzen oder die App deinstallieren. 
- **iCloud (optional)** – Die von Ihnen synchronisierten Daten verbleiben gemäß den Richtlinien von Apple in **Ihrem** iCloud-Konto, bis Sie die Synchronisierung deaktivieren und/oder sie über die Tools von Apple löschen. 
- **iHTC Studio** – Da wir auf unseren Servern keine personenbezogenen Daten erfassen, gibt es keinen Kontodatensatz, den wir auf Anfrage über die Beantwortung Ihrer E-Mail-Fragen hinaus löschen können. 

## Änderungen an dieser Richtlinie 

Wir können diese Datenschutzrichtlinie von Zeit zu Zeit aktualisieren. Das Datum „Letzte Aktualisierung“ oben ändert sich und die überarbeitete Richtlinie wird auf dieser Seite mit den Datenschutzrichtlinien veröffentlicht. 

## Kontaktieren Sie uns 

Wenn Sie Fragen zu dieser Datenschutzrichtlinie oder den Datenschutzpraktiken haben: 

- **E-Mail:** [AppleOSer@gmail.com](mailto:AppleOSer@gmail.com) 

Wir antworten in der Regel innerhalb von 48 Stunden.
