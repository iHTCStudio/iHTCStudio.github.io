iHTC Studio („wir“, „uns“ oder „unser“) hat **iPomodoro** (auch bekannt als „爱番茄“ / „愛番茄“) als Produktivitäts-App für iPhone und iPad entwickelt. Auf dieser Seite wird erläutert, wie wir mit Informationen umgehen, wenn Sie die App nutzen. 

## Zusammenfassung 

**iPomodoro erhebt, speichert oder übermittelt keine personenbezogenen Daten an unsere Server.** Timer, Lernstatistiken, Einstellungen und Motivationsinhalte funktionieren auf Ihrem Gerät. Die optionale **iCloud-Synchronisierung** für Aufgaben und/oder Studienstatistiken nutzt Apple CloudKit unter Ihrer Apple-ID – wir betreiben diesen Cloud-Dienst nicht. 

## Daten, die wir nicht sammeln 

- Kein Name, keine E-Mail-Adresse, keine Telefonnummer oder kein Benutzerkonto (es sei denn, Sie senden uns freiwillig eine E-Mail für den Support). 
- Keine Nutzungsanalysen, Absturzberichts-SDKs oder Werbekennungen. 
- Keine Standortverfolgung. 
- Kein Hochladen von Timer-Sitzungen oder Studienstatistiken auf **unsere Server** (optionale iCloud-Synchronisierung speichert Daten in Ihrem Apple iCloud-Konto). 
- Aufgabenlisten werden **nicht** auf uns hochgeladen – die optionale iCloud-Synchronisierung erfolgt direkt zwischen Ihren Geräten über Apple CloudKit, wenn Sie sie aktivieren. 

## Auf Ihrem Gerät gespeicherte Daten 

Folgendes bleibt **lokal** auf Ihrem iPhone oder iPad:

| Daten | Lagerung | Zweck | 
|------|---------|---------| 
| Pomodoro- und Lerntimer-Einstellungen | Benutzerstandards | Dauer, Töne, Themen, Benachrichtigungseinstellungen, optional **Phasenabschluss bestätigen** (Pomodoro) | 
| Countdown-Aufgaben (Titel, Datum, Notizen, Erinnerungsflagge, Pin, Reihenfolge, **Akzentfarbe**) | SQLite-Datenbank | Aufgabenliste, Fälligkeitserinnerungen, Widget-Farben | 
| Geschichte der Studiensitzung | SQLite-Datenbank | Registerkarte „Statistik“ (Fokuszeit, Diagramme, Aufgabenaufschlüsselung) | 
| Einstellungen für die Statistikanzeige | Benutzerstandards | Standardfilter, **benutzerdefinierter Datumsbereich**, Zählregeln, Themenfarben für die Registerkarte „Statistik“ | 
| Ziel- und Leistungspräferenzen fokussieren | Benutzerstandards | Tägliche/wöchentliche Ziele, freigeschaltete Abzeichen | 
| Startbildschirm-Verknüpfungseinstellungen | Benutzerstandards | Welche Schnellaktionen erscheinen, wenn Sie lange auf das App-Symbol drücken (bis zu 4) | 
| Fokusmodus-Erinnerung schaltet um | Benutzerstandards | Optionale Eingabeaufforderung beim Starten eines Timers ohne aktivierten Fokus | 
| Täglicher Motivationsbenachrichtigungsplan | Benutzerstandards | Optionale wiederholte lokale Benachrichtigungszeit | 
| Statistiken heute Fortschrittsschnappschuss | Benutzerstandards der App-Gruppe | Heutiges Statistik-Widget | 
| Korpus Motivationszitate (Dialog/Täglich + Benachrichtigung) | App-Bundle JSON | Angebotspools auf dem Gerät (**1000+** Dialoge/Tag kombiniert); Benachrichtigungspool ist separat | 
| Themen- und Spracheinstellungen | Benutzerstandards | Aussehen und Lokalisierung | 
| Index der täglichen Motivationszitate | Benutzerstandards der App-Gruppe | Motivations-Widget und Live-Aktivitätshinweis-Synchronisierung | 
| Sprachfilter für Motivationszitat | Benutzerstandards der App-Gruppe | Widget-Zitatpool entspricht In-App-Einstellungen | 
| Globaler Theme-Spiegel für Widgets | Benutzerstandards der App-Gruppe | Widget-Akzentfarben und optionaler Hintergrund mit Farbverlauf | 
| Pomodoro-Timer-Schnappschuss | Gemeinsamer App-Gruppencontainer | Pomodoro-Widget und Live-Aktivität | 
| Lern-Timer-Schnappschuss | Gemeinsamer App-Gruppencontainer | Lerntimer-Widget und Live-Aktivität | 
| Snapshot des Aufgaben-Widgets | Gemeinsamer App-Gruppencontainer | Countdown-Aufgaben-Widget |

Diese Daten sind für uns nicht zugänglich. Durch die Deinstallation der App wird der lokale Speicher entfernt (mit Ausnahme der iOS-Systemsicherungen, die Sie möglicherweise aktiviert haben). 

## Optionale iCloud-Synchronisierung (Aufgaben und Studienstatistiken) 

**Aufgaben:** Wenn Sie **Aufgaben mit iCloud synchronisieren** aktivieren, werden Countdown-Aufgaben über CloudKit (`iCloud.com.iHTCboy.iPomodoros`) synchronisiert. 

**Studienstatistiken:** Wenn Sie **Studienstatistiken mit iCloud synchronisieren** (Statistikeinstellungen) aktivieren, werden Fokussitzungsdatensätze als CloudKit-Datensätze vom Typ `StudySession` synchronisiert – einschließlich optionalem Titel/ID der verknüpften Aufgabe und eines `cloudId` für die Zusammenführung. **Tageszieleinstellungen** (`StatsGoals`) und **Erfolgs-Freischalt-/Feierstatus** (`StatsAchievements`) werden unter demselben Schalter synchronisiert. Sync verwendet inkrementelle CloudKit-Änderungstokens nach dem ersten vollständigen Pull. Dies ist **unabhängig** von der Aufgabensynchronisierung. 

In beiden Fällen verbleiben die Daten über die Infrastruktur von Apple in **Ihrem privaten iCloud-Konto** – nicht auf iHTC Studio-Servern. Deaktivieren Sie jederzeit einen der beiden Schalter. Lokale Kopien verbleiben auf jedem Gerät. 

## Benachrichtigungen 

Wenn Sie die Benachrichtigungsberechtigung erteilen, plant iPomodoro **lokale Benachrichtigungen** auf Ihrem Gerät für:

- Timer-Abschluss- und Hintergrundlernerinnerungen (sofern in den Einstellungen aktiviert) – der Nachrichtentext wird aus einem gebündelten Angebotspool für Benachrichtigungen auf dem Gerät ausgewählt; kein Netzwerkabruf 
- **Tägliche Motivationsbenachrichtigung** (optional, Einstellungen) – wiederholte lokale Benachrichtigung zu der von Ihnen gewählten Zeit 
- Erinnerungen an das Fälligkeitsdatum einer Aufgabe (sofern pro Aufgabe aktiviert) 

Diese Benachrichtigungen werden von iOS auf dem Gerät erstellt und übermittelt. Wir betreiben keinen Push-Benachrichtigungsserver und laden keine Angebotstexte von unseren Servern herunter. 

## App-Gruppe (Widgets und Live-Aktivitäten) 

Die Haupt-App und die Widget-Erweiterung teilen minimale Timer-, Motivations-, Thema-, **Aufgaben**- und **Heutige-Statistik-Fortschritts-Snapshots** über Apples App Group (`group.com.iHTCboy.iPomodoros`). Pomodoro und Study Timer verwenden **separate** Snapshot-Tasten auf dem Gerät, sodass beide Widgets nebeneinander existieren können. Dieser Container verbleibt auf Ihrem Gerät und wird nur zur Anzeige von Widgets und Live-Aktivitäten verwendet – nicht für den Zugriff Dritter. 

## In-App-Kauf 

Ein optionaler In-App-Supportkauf wird vollständig über **Apple StoreKit** abgewickelt. Wir erhalten über Apple nur Standard-App-Store-Kaufbelege; Wir erfassen Zahlungsdaten nicht direkt. 

## Dienste von Drittanbietern

iPomodoro integriert **nicht** Drittanbieter-Analytics, Werbung oder Social-Login-SDKs.

Wenn Sie auf **Feedback** tippen, kann die App Ihren Mail-Client mit einer vorausgefüllten Vorlage öffnen, die Geräte-Modell und App-Version enthält — Sie entscheiden, ob Sie sie senden.

## Datenschutz von Kindern

Wir sammeln wissentlich keine persönlichen Informationen von Kindern. Da wir keine personenbezogenen Daten über die App sammeln, gelten keine speziellen kindgerechten Bestimmungen über die standardmäßigen App-Store-Altersfreigaben hinaus.

## Änderungen dieser Richtlinie

Wir können diese Datenschutzrichtlinie von Zeit zu Zeit aktualisieren. Änderungen werden auf dieser Seite veröffentlicht.

## Kontaktieren Sie uns

Fragen zum Datenschutz?

- **E-Mail:** [AppleOSer@gmail.com](mailto:AppleOSer@gmail.com)
