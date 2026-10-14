iHTC Studio („wir“, „uns“ oder „unser“) hat iLinux (auch bekannt als „爱 Linux“) entwickelt. Auf dieser Seite informieren wir Sie über unsere Richtlinien zur Erhebung, Nutzung und Offenlegung personenbezogener Daten bei der Nutzung unserer App.

## Zusammenfassung

**iLinux sammelt keine Analysen und verkauft keine persönlichen Daten.** Befehlsbibliotheken laufen vollständig offline auf Ihrem Gerät. Die optionale **iCloud-Synchronisierung** (sofern aktiviert und bei iCloud angemeldet) speichert Favoriten, Quizfortschritt, Design und Anzeigeeinstellungen in **Ihrem** iCloud-Schlüsselwertspeicher unter Ihrer Apple-ID – iHTC Studio betreibt keinen Backend-Server für diese Daten.

## Datenerfassung

Wir betreiben keine Analysen, Werbung oder Tracking. Konkret:

- **Keine persönlichen Daten** werden von iHTC Studio erfasst (kein Name, E-Mail, Telefonnummer oder iHTC Studio-Konto).
- **Es sind keine Nutzungsanalysen** oder Absturzberichts-SDKs integriert.
- **Ihre Lerndaten** (Favoriten, Quizergebnisse, falsche Antworten) bleiben auf Ihren Geräten und, wenn Sie die Synchronisierung aktivieren, in **Apple iCloud** – nicht auf iHTC Studio-Servern.
- **Keine Cookies oder Tracker von Drittanbietern** in der App.

## So funktioniert die App

iLinux speichert alle vom Benutzer generierten Daten – Favoriten, aktuelle Ansichten, Quizsitzungsergebnisse, Datensätze zu falschen Antworten, Shell-Plattformpräferenz, Favoritenbereich, Widget-Befehlsbibliothek und App-Präferenzen – lokal auf Ihrem Gerät:

- Alle Befehlsdaten (JSON-Zusammenfassungen und Markdown-Dokumentation für **Linux, CMD und PowerShell**) werden in der App gebündelt und niemals von einem externen Server abgerufen.
- Zum Durchsuchen von Befehlen oder zum Durchführen von Tests ist keine Internetverbindung erforderlich.
- Die optionale **iCloud-Synchronisierung** verwendet Apples **NSUbiquitousKeyValueStore**, wenn Sie bei iCloud angemeldet sind und die Synchronisierung aktiviert lassen. Sie können es in den Einstellungen für jedes Gerät deaktivieren.
- Beim Öffnen externer Links innerhalb der App (z. B. durch Tippen auf eine URL im Abschnitt „Feedback“) wird das standardmäßige iOS-Netzwerkverhalten verwendet. Die verlinkte Seite wird von Ihrem Gerät direkt von seinem Host geladen, nicht über einen iHTC Studio-Server.
- The optional **App Store version check** (`AppStoreVersionChecker`) makes a single read-only request to the public iTunes Lookup API to compare the installed version with the latest release. No personal data is sent in this request.

## Berechtigungen

iLinux fordert den Zugriff auf die **Fotobibliothek** nur dann an, wenn Sie sich für das **Speichern einer Freigabekarte oder eines Befehls-Screenshots** in Fotos entscheiden. Es ist kein Zugriff auf Kamera, Mikrofon, Standort oder Kontakte erforderlich.

## Datenspeicherung

| Daten | Speicherort |
|------|-----------------|
| Favoriten, aktuelle Ansichten, Datensätze mit falschen Antworten, Lernstatus (pro Plattform) | Lokale Benutzereinstellungen/App-Gruppe auf Ihrem Gerät |
| Quizfortschritt und tägliche Sitzungsergebnisse (verschlüsselt nach Datum und Shell-Plattform) | Lokale App-Sandbox auf Ihrem Gerät |
| Thema, Sprache, Listen-/Rasterlayout, Shell-Plattform, Favoritenbereich, Widget-Bibliothek | Lokale Benutzereinstellungen/App-Gruppe auf Ihrem Gerät |
| iCloud-Synchronisierungsspiegel (optional) | Apple iCloud Key-Value Storage (`crossSync.*` keys) — favourites, quiz progress, theme, app preferences |
| Widget-Snapshot (nur iOS/iPad) | App Group container (`group.com.iHTCboy.iLinuxs`) |

Auf keinem von iHTC Studio betriebenen Server werden Daten gespeichert. Optionale iCloud-Daten unterliegen den iCloud-Bedingungen von Apple.

## iCloud-Synchronisierung (optional)

Wenn **iCloud Sync** aktiviert ist und Sie bei iCloud angemeldet sind:

- Synchronisierte Daten: **Lernfortschritt** (Favoriten, Aktuelles, Lernstatus, Quizergebnisse, Datensätze zu falschen Antworten), **Thema** und **App-Einstellungen** (Sprache, Shell-Plattform, Favoritenbereich, Listen-/Rastereinstellungen).
- Speicher: Apple **iCloud Key-Value Storage**, verknüpft mit Ihrer Apple-ID.
- Zusammenführen: In Konflikt stehende Aktualisierungen werden auf dem Gerät zusammengeführt (z. B. Favoritenvereinigung, neueste Zeitstempel).
- Opt-out: in **Einstellungen → iCloud Sync** auf jedem Gerät deaktivieren; Dieses Gerät stoppt das Hochladen und Zusammenführen, behält aber lokale Daten.
- iHTC Studio kann Ihren iCloud-Container nicht lesen.

## App-Gruppe (Widget-Erweiterung – nur iOS/iPad)

iLinux uses an App Group (`group.com.iHTCboy.iLinuxs`) to share a small amount of data with its Home Screen widget extension. This data includes:

- The selected content language code (e.g. `en`, `zh-Hans`)
- Eine Momentaufnahme der Themenfarbe (Akzent-Hex-Werte und Farbverlaufswerte)
- Eine Zusammenfassung Ihres Lernfortschritts (Anzahl der Favoriten, Quizstatistiken) zur Widget-Anzeige
- Die ausgewählte **Widget-Befehlsbibliothek** (Linux / CMD / PowerShell)
- Der Shuffle-Zähler des Daily Command-Widgets (eine einfache Ganzzahl, die zur Auswahl des nächsten vorgestellten Befehls verwendet wird)

Diese Daten werden nur in einen gemeinsamen Container auf Ihrem Gerät geschrieben und niemals irgendwohin übertragen.

## Was iLinux nicht ist

iLinux führt keine Shell-Befehle aus, öffnet keine SSH-Sitzungen und greift nicht auf Remote-Systeme zu. Diese App erfasst keine Befehlszeileneingaben, die Sie möglicherweise an anderer Stelle eingeben.

## In-App-Kauf

iLinux beinhaltet eine optionale Trinkgeld-/Kaufoption. Sämtliche Zahlungsvorgänge werden ausschließlich über **Apples StoreKit-Framework** abgewickelt. iHTC Studio empfängt, verarbeitet oder speichert keine Zahlungskarteninformationen oder Rechnungsdetails.

## Privatsphäre von Kindern

iLinux sammelt wissentlich keine personenbezogenen Daten von irgendjemandem, auch nicht von Kindern unter 13 Jahren. Da wir überhaupt keine Daten sammeln, sind keine besonderen Bestimmungen erforderlich.

## Änderungen an dieser Richtlinie

Wir können diese Datenschutzrichtlinie von Zeit zu Zeit aktualisieren. Alle Änderungen werden mit aktualisiertem Datum auf dieser Seite veröffentlicht. Wir empfehlen Ihnen, diese Seite regelmäßig zu überprüfen.

## Kontaktieren Sie uns

Wenn Sie Fragen zu dieser Datenschutzrichtlinie haben, kontaktieren Sie uns bitte:

- **E-Mail:** [AppleOSer@gmail.com](mailto:AppleOSer@gmail.com)
