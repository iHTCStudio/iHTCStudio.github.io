**Zuletzt aktualisiert:** 23. Juli 2026

iHTC Studio („wir“, „uns“ oder „unser“) hat **iVirtue** entwickelt (auch bekannt als „爱弟子规“ / „愛弟子規“, Bundle-ID `com.iHTCboy.iVirtue`). Diese Datenschutzerklärung erläutert, welche Daten bei der Nutzung der App verarbeitet werden (und welche nicht). **Apple App Review** und Nutzer können sich auf diese Seite als öffentliche Datenschutz-URL stützen.

## Zusammenfassung (Abgleich mit Apples Datenschutz-Nährwertkennzeichnung)

| Thema | Unsere Praxis |
|-------|----------------|
| Konto | **Nicht erforderlich** — keine Registrierung, keine Anmeldung per E-Mail, keine Telefonnummer |
| Datenerhebung durch iHTC Studio | **Keine Daten erhoben** — wir betreiben **kein** Backend, das Ihre personenbezogenen Daten empfängt |
| Netzwerk | Virtue-Bibliothek, Lesen, Rezitieren, Lernen, Widgets und tägliche Benachrichtigungen funktionieren nach der Installation **offline** |
| Analyse / Werbung / Tracking | **Keine** — keine Analyse-, Werbe- oder Tracking-SDKs von Drittanbietern; keine Nutzung von App Tracking Transparency |
| Optionale Apple-Dienste | **iCloud** (Ihr privater KVS), **Fotomediathek (nur Hinzufügen)** für Teilen-Karten, **StoreKit** für optionales Trinkgeld, **lokale Benachrichtigungen**, optionale **Live-Aktivitäten** |

## Datenerhebung

Wir erheben, verkaufen oder teilen **keine** personenbezogenen Daten für Werbung oder Analyse.

- **Kein Konto** — Sie können alle Kernfunktionen nutzen, ohne bei uns ein Konto anzulegen.
- **Keine Analyse oder Werbung** — Die App enthält keine SDKs von Drittanbietern für Analyse, Werbung oder Absturzberichte, die Daten an uns senden.
- **Kein Hochladen von Virtue-Inhalten** — Ihr Leseverlauf, Ihre Favoriten, Ihr Lernfortschritt und Ihre Einstellungen bleiben auf Ihrem Gerät (und optional in **Ihrem** iCloud). Sie werden nie auf Server von iHTC Studio hochgeladen, da **wir für diese App keine solchen Server betreiben**.

## Wie die App funktioniert

- **Mitgelieferte Bibliothek** — Virtue-JSON und Indizes sind im App-/Widget-Bundle enthalten. Stöbern und Lernen erfordern keine Netzwerkanfrage.
- **Sprachausgabe auf dem Gerät** — Die Rezitation nutzt Apples geräteinterne System-**AVSpeechSynthesizer** (TTS). Wir senden keinen Virtue-Text an iHTC Studio.
- **Widgets und App Group** — Widgets und App teilen Einstellungen und leichten Zustand über die App Group `group.com.iHTCboy.iVirtue` auf Ihrem Gerät.
- **Tägliche Benachrichtigungen** — Lokal mit User Notifications geplant. Tippen auf eine Benachrichtigung öffnet einen Deep-Link zu einer Virtue-ID auf dem Gerät; es gibt keinen Server-Versand.
- **Teilen-Karten** — Bilder werden auf dem Gerät erzeugt. Das Speichern nutzt **Fotomediathek (nur Hinzufügen)** ausschließlich, wenn Sie auf Speichern tippen. Das System-Share-Sheet kann das Bild an eine App senden, die **Sie** wählen; dann gilt die Datenschutzerklärung dieses Ziels.
- **Optionales Trinkgeld** — „Entwickler unterstützen“ ist ein verbrauchbarer **StoreKit**-Kauf, der von Apple abgewickelt wird. Wir erhalten Ihre Zahlungskartendaten nicht.

## Auf Ihrem Gerät gespeicherte Daten

| Daten | Wo | Zweck |
|------|-------|---------|
| Virtue-Datenbank | App-/Widget-Bundle | Offline lesen und lernen |
| Favoriten und Virtue-Listen | UserDefaults der App Group | Mit Stern markierte Werke und Nutzerlisten |
| Leseverlauf / zuletzt gelesen | UserDefaults der App Group | Weiterlesen, Verlaufsanzeige |
| Lernfortschritt und Beherrschung | UserDefaults der App Group | 4 Beherrschungsstufen, Quizstatus |
| Serie / Check-in | UserDefaults der App Group | Lernserien |
| Darstellungs- und Leseeinstellungen | UserDefaults der App Group | Design, Akzent, Sprache, Layout, TTS, Tabs, Widgets |
| Cache des Tages-Virtues und Benachrichtigungseinstellungen | UserDefaults der App Group | ID von heute, Uhrzeit, Schalter für kontextbezogene Auswahl |
| Einstellungen der Teilen-Karten | UserDefaults der App Group | Zuletzt gewählter Stil / zuletzt gewähltes Seitenverhältnis |
| Onboarding- und TipKit-Status | Standard-UserDefaults (Gerät) | Willkommensanleitung / Entdeckungstipps |
| Home-Bildschirm-Schnellaktionen | System + lokale Einstellungen | Bis zu 4 von Ihnen konfigurierte Kurzbefehle |
| Widget-/Live-Aktivität-Snapshots | App Group / ActivityKit | Anzeigetext, den Sie bereits geöffnet haben |

Das Deinstallieren der App entfernt die zugehörigen Sandbox- und App-Group-Daten (abhängig vom Verhalten von iOS/macOS). Optionale iCloud-Kopien verbleiben in **Ihrem** iCloud, bis Sie sie löschen oder die Synchronisierung ausschalten und anderswo löschen.

## iCloud-Synchronisierung (optional)

Wenn Sie in den Einstellungen die **iCloud-Synchronisierung** aktivieren, spiegelt die App ausgewählte Nutzerdaten über Apples **`NSUbiquitousKeyValueStore`**, der an **Ihre Apple-ID** gebunden ist:

- Favoriten
- Virtue-Listen
- Leseverlauf
- Lernfortschritt / Beherrschung
- Serientage

Der Synchronisierungsverkehr geht an **Apple iCloud**, nicht an iHTC Studio. Sie können die Synchronisierung in den Einstellungen deaktivieren. Wir können den Inhalt Ihres iCloud nicht lesen.

## Berechtigungen

iVirtue fordert Berechtigungen nur an, wenn eine Funktion sie benötigt:

| Berechtigung | Wann | Warum |
|------------|------|-----|
| Mitteilungen | Sie aktivieren die Erinnerungen für das Tages-Virtue | Lokale Planung von Erinnerungsbenachrichtigungen |
| Fotomediathek (nur Hinzufügen) | Sie speichern eine Teilen-Karte | Das erzeugte Bild schreiben; wir benötigen keinen vollen Lesezugriff auf die Mediathek |
| iCloud | Sie aktivieren die Synchronisierung | Favoriten / Listen / Verlauf / Fortschritt / Serien synchronisieren |
| Live-Aktivitäten (iOS) | Sie aktivieren die Lese-Live-Aktivität | Das gerade gelesene Virtue auf dem Sperrbildschirm / in der Dynamic Island anzeigen |
| Hintergrundaudio (Capability) | Sie aktivieren die Hintergrundrezitation | TTS fortsetzen, wenn die App nicht im Vordergrund ist |

Wir fordern **keinen** Zugriff auf Kontakte, genauen Standort, Kamera, Mikrofon (über die Wiedergabe der System-TTS hinaus) oder Tracking an.

## Datenschutz für Kinder

iVirtue erhebt wissentlich von niemandem personenbezogene Daten, auch nicht von Kindern unter 13 Jahren (oder dem entsprechenden Alter in Ihrer Region). Da wir kein Backend zur Datenerhebung betreiben, wird bei uns kein Kinderprofil gespeichert.

## Drittanbieter

- **Apple** — Vertrieb über den App Store, optionale StoreKit-Käufe, optionaler iCloud-KVS, System-TTS, von Ihnen gewählte Ziele im Share Sheet sowie die Zustellung von Benachrichtigungen / Live-Aktivitäten auf Betriebssystemebene.
- **Keine weiteren SDKs von Drittanbietern** für Werbung, Analyse oder Social-Login zur Datenerhebung sind enthalten.

## Internationale Nutzer

Die App ist darauf ausgelegt, offline auf Ihrem Gerät zu funktionieren. Optionale Apple-Dienste unterliegen den Bedingungen von Apple und der regionalen Verfügbarkeit.

## Änderungen dieser Richtlinie

Wir können diese Datenschutzerklärung von Zeit zu Zeit aktualisieren. Das Datum „Zuletzt aktualisiert“ oben ändert sich, und die überarbeitete Erklärung wird auf dieser Datenschutzseite veröffentlicht.

## Kontakt

- **E-Mail:** [AppleOSer@gmail.com](mailto:AppleOSer@gmail.com)
