**Zuletzt aktualisiert:** 29. Juli 2026

iHTC Studio („wir“, „uns“ oder „unser“) hat **iDeveloper** entwickelt (auch bekannt als „爱开发者“ / „愛開發者“, Bundle-ID `com.iHTCboy.iDeveloper`). Diese Datenschutzerklärung erläutert, welche Daten bei der Nutzung der App verarbeitet werden – und welche nicht. **Apple App Review** und Nutzer können sich auf diese Seite als öffentliche Datenschutz-URL stützen.

## Zusammenfassung (Abgleich mit Apples Datenschutz-Nährwertkennzeichnung)

| Thema | Unsere Praxis |
|-------|----------------|
| Konto | **Nicht erforderlich** |
| Datenerhebung durch iHTC Studio | **Daten werden nicht erfasst** – wir betreiben **kein** Backend, das deine Tool-Eingaben oder personenbezogenen Daten empfängt |
| Netzwerk | Tools und Spickzettel funktionieren standardmäßig **offline**. Netzwerkfähige Tools senden nur dann eine Anfrage, wenn **du** eine startest |
| Analyse / Werbung / Tracking | **Keine** – keine Analyse-, Werbe- oder Tracking-SDKs von Drittanbietern |
| Optionale Apple-Dienste | **iCloud** (dein privater KVS), **StoreKit**-Trinkgeld, von dir gewählte System-Teilen-Ziele, von Apple bereitgestellte Widgets / Live-Aktivitäten / Siri |

## Datenerhebung

Wir erheben, verkaufen oder teilen **keine** personenbezogenen Daten für Werbung oder Analyse. Deine Eingaben, Ausgaben, Favoriten, dein Verlauf und deine Snippets bleiben auf deinem Gerät (und optional in **deiner** iCloud). Sie werden nie auf Server von iHTC Studio hochgeladen, weil **wir für diese App keine solchen Server betreiben**.

## So funktioniert die App

- **Integrierte Tools und Referenzen** – Engines und Spickzettel-JSON sind in den Bundles von App, Widget und Teilen-Erweiterung enthalten.
- **Verarbeitung auf dem Gerät** – Formatierung, Kodierung, Krypto-Helfer, Regex und die meisten Werkzeuge laufen lokal.
- **Netzwerk nur auf Wunsch** – Braucht ein Tool das Internet, zeigt die Oberfläche einen Hinweis; die Anfrage wird nur durch deine Aktion ausgelöst und geht an den Zielhost dieses Tools – nicht über einen Proxy von iHTC Studio.
- **Teilen-Erweiterung** – Geteilter Text bzw. geteilte Inhalte werden auf deinem Gerät über die App Group `group.com.iHTCboy.iDeveloper` übergeben.
- **Widgets & Live-Aktivität** – Zeigen Momentaufnahmen von Inhalten, die du bereits geöffnet hast, oder von Timern, die du gestartet hast, über App Group / ActivityKit.
- **Optionales Trinkgeld** – Verbrauchbarer **StoreKit**-Kauf, der von Apple abgewickelt wird.

## Auf deinem Gerät gespeicherte Daten

| Daten | Zweck |
|-------|-------|
| Werkzeugkatalog und Referenzbibliothek | Offline-Tools und Spickzettel |
| Favoriten / zuletzt genutzte Tools | Schneller Zugriff |
| Aktionsverlauf | Frühere Ein- und Ausgaben wiederherstellen |
| Snippets | Von dir gespeicherte, wiederverwendbare Fragmente |
| Teilen-Eingangspuffer | Temporäre Übergabe aus Teilen / An Tool senden |
| Darstellung und Einstellungen | Design, Akzent, Sprache, Tabs, Widgets |
| Fokus- / Live-Aktivitätsstatus | Timer-Anzeige |
| Einführung und Bewertungsaufforderungen | Willkommens- / Bewertungsablauf |

## iCloud-Synchronisierung (optional)

Wenn aktiviert, können ausgewählte Einstellungen / Workflow-Zustände über Apples **`NSUbiquitousKeyValueStore`** synchronisiert werden, der an **deine Apple-ID** gebunden ist. Der Synchronisierungsverkehr geht an **Apple iCloud**, nicht an iHTC Studio.

## Berechtigungen

iDeveloper fragt Berechtigungen nur an, wenn eine Funktion sie braucht (zum Beispiel die Fotomediathek, wenn ein Tool ein von dir exportiertes Bild speichert, oder das Netzwerk, wenn du ein Netzwerk-Tool ausführst). Wir fragen **kein** Tracking, keine Kontakte und keinen genauen Standort für Analysezwecke an.

## Kontakt

[AppleOSer@gmail.com](mailto:AppleOSer@gmail.com)
