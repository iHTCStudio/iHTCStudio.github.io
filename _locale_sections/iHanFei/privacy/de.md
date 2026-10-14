**Zuletzt aktualisiert:** 5. September 2026

iHTC Studio („wir“) hat **iHanFei** („爱韩非子 / 愛韓非子“, Bundle-ID `com.iHTCboy.iHanFei`) entwickelt. Diese Datenschutzerklärung erläutert, welche Daten bei der Nutzung verarbeitet werden (und welche nicht). **Apple App Review** und Nutzer können sich auf **diese Seite** als öffentliche Datenschutzerklärung stützen. Für App Store Connect öffnen Sie diese Seite im Browser und kopieren Sie die URL aus der Adressleiste (die Domain kann sich ändern).

## Zusammenfassung (Übereinstimmung mit dem Apple-Datenschutzetikett)

| Thema | Unsere Praxis |
|-------|----------------|
| Konto | **Nicht erforderlich** — keine Registrierung, kein E-Mail-Login oder Telefonnummer erforderlich |
| Datenerhebung durch iHTC Studio | **Keine Datenerhebung** — wir betreiben **keinen** Backend-Service, der Ihre persönlichen Daten empfängt |
| Netzwerk | Bibliothek, Lesen, Rezitieren, Lernen, Hunt, Widgets und tägliche Benachrichtigungen funktionieren **offline** nach der Installation |
| Analysen / Werbung / Tracking | **Keine** — keine Analysen von Drittanbietern, Werbung oder Tracking-SDKs; keine Nutzung von App Tracking Transparency |
| Optionale Apple-Dienste | **iCloud** (privater KVS), **Fotomediathek (nur Hinzufügen)** für 孟-Karten, **StoreKit** für optionales Trinkgeld, **lokale Benachrichtigungen**, optionale **Live-Aktivitäten**, optionale **Handschrift** auf dem Gerät (Vision) |

## Datenerfassung

Wir erheben, verkaufen oder teilen **keine** persönlichen Informationen für Werbung oder Analysen.

- **Kein Konto** — Sie können alle Kernfunktionen nutzen, ohne ein Konto bei uns zu erstellen.
- **Keine Analysen oder Werbung** — Die App-Binärdatei integriert keine Analysen, Werbung oder Crash-Reporting-SDKs von Drittanbietern, die Daten an uns senden.
- **Kein Hochladen von Inhalten** — Leseverlauf, Favoriten, Listen, Notizen, Lernfortschritt und Einstellungen bleiben auf dem Gerät (optional in **Ihrem** iCloud). Sie werden nicht auf iHTC Studio-Server hochgeladen, da **wir für diese App keine solchen Server betreiben**.

## So funktioniert die App

- **Mitgelieferte Bibliothek** — Text-JSON, Umgangssprache/Englisch, Indizes und Lernhilfen liegen im App-/Widget-Bundle. Durchsuchen und Lernen erfordern kein Netzwerk.
- **Sprache auf dem Gerät** – Die Rezitation nutzt Apples System **AVSpeechSynthesizer** (TTS). Wir senden keine Passagentexte an iHTC Studio.
- **Widgets und App Group** — Widgets und App teilen Einstellungen und leichten Zustand über die App Group `group.com.iHTCboy.iHanFei` auf Ihrem Gerät.
- **Tägliche Benachrichtigungen** – Lokal geplant mit Benutzerbenachrichtigungen. Durch Tippen auf eine Benachrichtigung wird ein Deep-Link zu einer Durchgangs-ID auf dem Gerät geöffnet. Kein Server-Fanout.
- **法-Karten** — Bilder werden auf dem Gerät erzeugt. Speichern nutzt **Fotomediathek (nur Hinzufügen)** nur beim Tippen auf Speichern. Das Share Sheet kann das Bild an eine App senden, **die Sie wählen**; dann gilt deren Datenschutzerklärung.
- **Handschriftsuche (iOS)** – Die optionale Zeichenerkennung verwendet Apple **Vision** auf dem Gerät. Striche werden nicht hochgeladen.
- **Optionaler Tipp** – „Tip Developer“ ist ein verbrauchbarer **StoreKit**-Kauf, der von Apple abgewickelt wird. Wir erhalten Ihre Zahlungskartendaten nicht.
- **Siri / Verknüpfungen / Kontrollzentrum** – Optionale Systemintegrationen öffnen Deep Links auf dem Gerät; Sie senden Ihre Bibliothek nicht an uns.
- **Optionales Spotlight** – Wenn Sie die Indizierung aktivieren, werden Inhalte vom System auf dem Gerät für die lokale Suche indiziert; Wir betreiben kein Such-Backend.

## Auf Ihrem Gerät gespeicherte Daten

| Daten | Wo | Zweck |
|------|-------|---------|
| Han Feizi-Datenbank | App-/Widget-Bundle | Offline-Lesen und -Lernen |
| Favoriten und Listen (简册 lists) | UserDefaults der App Group | Markierte Abschnitte und Nutzerlisten |
| Leseverlauf / zuletzt gelesen | Benutzerstandards der App-Gruppe | Lesen Sie weiter, Verlauf der Benutzeroberfläche |
| Notizen | Benutzerstandards der App-Gruppe | Lesen von Notizen, die Sie schreiben |
| Studienfortschritt & Beherrschung | Benutzerstandards der App-Gruppe | Unterrichtszustand, Quiz/Jagdfortschritt |
| Übungssträhne / Check-in | Benutzerstandards der App-Gruppe | Tägliche Gewohnheit |
| Einstellungen der Teilen-Karten | UserDefaults der App Group | Zuletzt gewählter Stil / zuletzt gewähltes Seitenverhältnis |
| Daily Stratagem cache & notification prefs | UserDefaults der App Group | Heutige ID, schedule time, contextual toggle |
| Karten-Einstellungen | UserDefaults der App Group | Letzter Stil/Verhältnis |
| Onboarding- und TipKit-Status | Standard UserDefaults (Gerät) | Willkommensführer / Entdeckungstipps |
| Letzte Suchen | Standard UserDefaults (device) | Suchverlauf Ihrer Eingaben |
| Schnellaktionen auf dem Startbildschirm | System + lokale Einstellungen | Von Ihnen konfigurierte Verknüpfungen |
| Widget-/Live-Aktivitäts-Schnappschüsse | App-Gruppe / ActivityKit | Text anzeigen, den Sie bereits geöffnet haben |

Die Deinstallation der App entfernt Sandbox- und App-Gruppendaten, die mit der App verbunden sind (abhängig vom Verhalten von iOS/macOS). Optionale iCloud-Kopien bleiben in **deiner** iCloud, bis du sie löschst oder die Synchronisierung ausschaltest und anderswo löschst.

## iCloud-Synchronisierung (optional)

Wenn du **iCloud-Synchronisierung** in den Einstellungen aktivierst, spiegelt die App ausgewählte Benutzerdaten über Apples **`NSUbiquitousKeyValueStore`**, die mit **deiner Apple-ID** verknüpft ist:

- Favoriten
- Listen (简册 lists)
- Leseverlauf
- Lernfortschritt / Kenntnisse
- Übungsserien
- Notizen

Der Synchronisationsverkehr geht an **Apple iCloud**, nicht an iHTC Studio. Du kannst die Synchronisierung in den Einstellungen deaktivieren. Wir können deine iCloud-Inhalte nicht lesen.

## Berechtigungen

iLiezi fordert Berechtigungen nur an, wenn eine Funktion diese benötigt:

| Erlaubnis | Wann | Warum |
|------------|------|-----|
| Benachrichtigungen | Sie aktivieren Daily Stratagem reminders | Lokale Planung of reminder notifications |
| Fotomediathek (nur Hinzufügen) | Karte speichern | Gerendetes Bild schreiben |
| iCloud | Sync aktivieren | Favoriten/Listen/Verlauf/Fortschritt/Serien/Notizen |
| Live-Aktivitäten (iOS) | Sie aktivieren die Lese-Live-Aktivität | Zeigen Sie die Passage, die Sie gerade lesen, auf dem Sperrbildschirm/Dynamic Island | an
| Hintergrundaudio (Fähigkeit) | Sie aktivieren die Hintergrundrezitation | TTS fortsetzen, wenn die App nicht im Vordergrund ist |

**Keine** Kontakte, Standort, Kamera, Mikrofon (außer TTS), Tracking. Handschrift — Vision auf dem Gerät.

## Was wir nicht tun

- Wir verkaufen **keine** personenbezogene Daten.
- Wir erstellen **keine** Werbeprofile.
- Wir benötigen **kein** Konto oder Social-Login.
- Wir betten zur Datenerfassung **keine** Werbung, Analysen oder soziale SDKs von Drittanbietern ein.
- Wir greifen über die Option „Nur hinzufügen“ hinaus **nicht** auf Ihre Fotobibliothek zu, wenn Sie sich für das Speichern einer Karte entscheiden.
- Wir erhalten **keine** Nummern von StoreKit-Zahlungskarten (Apple verarbeitet Zahlungen).
- **Kein** Upload von Handschrift/Passagentext an iHTC Studio.

## Privatsphäre von Kindern

iHanFei ist eine Bildungs- und Lese-App für ein allgemeines Publikum und **nicht** in der Kids Category. Wir erheben wissentlich keine personenbezogenen Daten von Kindern. Die App erfordert kein Konto. Familien können Lese- und Lernfunktionen offline auf eigenen Geräten nutzen.

## Dritte Parteien

- **Apple** — App Store-Vertrieb, optionale StoreKit-Käufe, optionales iCloud-KVS, System-TTS, von Ihnen gewählte Share-Sheet-Ziele sowie Benachrichtigungen/Live-Aktivitäten/Siri/Kurzbefehle/Vision auf OS-Ebene.
- **Keine weiteren Drittanbieter-SDKs** für Werbung, Analysen oder Social-Login sind zur Datenerfassung enthalten.

## Internationale Nutzer

Die App ist darauf ausgelegt, offline auf Ihrem Gerät zu funktionieren. Optionale Apple-Dienste unterliegen den Bedingungen von Apple und der regionalen Verfügbarkeit.

## Datenaufbewahrung & Löschung

- **Auf dem Gerät** — Löschen Sie die App, um lokale Sandbox- und App-Gruppendaten zu entfernen (abhängig vom Verhalten des Betriebssystems).
- **iCloud** — Deaktivieren Sie die Synchronisierung und löschen Sie bei Bedarf zugehörige Schlüssel aus Ihrem iCloud-Konto / Ihren Geräten; wir können Ihr iCloud nicht für Sie löschen.
- **Wir speichern nichts** auf den iHTC Studio-Servern für diese App, da wir keine Daten sammeln.

## Richtlinienänderungen

Wir können diese Datenschutzerklärung aktualisieren. Das Datum „Zuletzt aktualisiert“ oben ändert sich. Fortgesetzte Nutzung nach einer Aktualisierung gilt als Zustimmung zur überarbeiteten Richtlinie. Wesentliche Änderungen können gegebenenfalls auch im App Store unter „Was ist neu“ vermerkt werden.

## Kontakt

Fragen zum Datenschutz: [AppleOSer@gmail.com](mailto:AppleOSer@gmail.com)
