**Zuletzt aktualisiert:** 29. Juli 2026

iHTC Studio („wir“, „uns“ oder „unser“) hat **iLunYu** entwickelt (auch bekannt als „爱论语“ / „愛論語“, Bundle-ID `com.iHTCboy.iLunYu`). Diese Datenschutzerklärung erläutert, welche Daten bei der Nutzung der App verarbeitet werden (und welche nicht). **Apple App Review** und Nutzer können sich auf diese Seite als öffentliche Datenschutz-URL stützen.

## Zusammenfassung (Abgleich mit Apples Datenschutz-Nährwertkennzeichnung)

| Thema | Unsere Praxis |
|-------|----------------|
| Konto | **Nicht erforderlich** |
| Datenerhebung durch iHTC Studio | **Keine Daten erhoben** — wir betreiben **kein** Backend, das Ihre personenbezogenen Daten empfängt |
| Netzwerk | Bibliothek, Lesen, Rezitieren, Lernen, Widgets und tägliche Benachrichtigungen funktionieren nach der Installation **offline** |
| Analyse / Werbung / Tracking | **Keine** |
| Optionale Apple-Dienste | **iCloud** (Ihr privater KVS), **Fotomediathek (nur Hinzufügen)** für Teilen-Karten, **StoreKit**-Trinkgeld, **lokale Benachrichtigungen**, optionale **Live-Aktivitäten** |

## Datenerhebung

Wir erheben, verkaufen oder teilen **keine** personenbezogenen Daten für Werbung oder Analyse. Ihr Leseverlauf, Favoriten, Listen und Einstellungen bleiben auf Ihrem Gerät (und optional in **Ihrem** iCloud). Sie werden nie auf Server von iHTC Studio hochgeladen.

## Wie die App funktioniert

- **Mitgelieferte Bibliothek** — Kapitel-JSON und Indizes sind im App-/Widget-Bundle enthalten.
- **Sprachausgabe auf dem Gerät** — Rezitation nutzt Apples System-**AVSpeechSynthesizer**. Wir senden keinen Text an iHTC Studio.
- **Widgets & App Group** — Gemeinsame Nutzung über App Group `group.com.iHTCboy.iLunYu` auf Ihrem Gerät.
- **Tägliche Benachrichtigungen** — Lokal geplant. Tippen öffnet einen Deep-Link zu einer Kapitel-ID auf dem Gerät.
- **Teilen-Karten** — Auf dem Gerät gerendert. Speichern nutzt **Fotomediathek (nur Hinzufügen)**, wenn Sie auf Speichern tippen.
- **Optionales Trinkgeld** — Verbrauchbarer **StoreKit**-Kauf, der von Apple abgewickelt wird.

## Auf Ihrem Gerät gespeicherte Daten

| Daten | Zweck |
|------|-------|
| Kapiteldatenbank | Offline-Lesen & Lernen |
| Favoriten & Leselisten | Markierte Werke und Benutzerlisten |
| Leseverlauf | Weiterlesen |
| Lernfortschritt & Meisterschaft | Klassenzustand |
| Serie / Check-in | Lernserien |
| Darstellung & Leseeinstellungen | Design, Sprache, TTS, Tabs, Widgets |
| Tageskapitel-Cache & Benachrichtigungen | Heutige ID und Zeitplan |
| Onboarding-Status | Willkommensführung |

## iCloud-Synchronisierung (optional)

Wenn aktiviert, spiegelt die App Favoriten, Leselisten, Leseverlauf, Lernfortschritt und Serien über Apples **`NSUbiquitousKeyValueStore`**, gebunden an **Ihre Apple-ID**. Sync-Verkehr geht an **Apple iCloud**, nicht an iHTC Studio.

## Berechtigungen

| Berechtigung | Wann | Warum |
|------------|------|-----|
| Benachrichtigungen | Sie aktivieren Tageskapitel-Erinnerungen | Lokale Planung |
| Fotomediathek (nur Hinzufügen) | Sie speichern eine Teilen-Karte | Gerendertes Bild schreiben |
| iCloud | Sie aktivieren Sync | Favoriten / Listen / Verlauf / Fortschritt / Serien |
| Live-Aktivitäten (iOS) | Sie aktivieren Lese-Live-Aktivität | Sperrbildschirm / Dynamic Island |
| Hintergrundaudio | Sie aktivieren Hintergrund-Rezitation | TTS im Hintergrund fortsetzen |

Wir fordern **keine** Kontakte, genaue Standortdaten, Kamera, Mikrofon (über System-TTS hinaus) oder Tracking an.

## Kontakt

[AppleOSer@gmail.com](mailto:AppleOSer@gmail.com)
