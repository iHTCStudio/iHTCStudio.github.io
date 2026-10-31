**Zuletzt aktualisiert:** 9. September 2026

iHTC Studio („wir", „uns" oder „unser") hat **iMusic** (auch „爱音乐" / „愛音樂", Bundle ID `com.iHTCboy.iMusic`) entwickelt. Diese Seite erklärt, welche Daten bei der Nutzung der App (und der Widget-Erweiterung) verarbeitet werden — und welche nicht. **Apple App Review** und Nutzer können diese Seite als öffentliche Datenschutzerklärung heranziehen. Für App Store Connect: [Privacy Policy](../privacy) im Browser öffnen und die URL aus der Adressleiste kopieren (die öffentliche Domain kann sich ändern).

## Überblick (Apple Privacy Nutrition Label)

| Thema | Unser Vorgehen |
|-------|----------------|
| Konto | **Nicht erforderlich** — keine Registrierung, E-Mail oder Telefonnummer |
| Datenerfassung durch iHTC Studio | **Data Not Collected** — wir betreiben **kein** Backend, das personenbezogene Daten empfängt |
| Netzwerk | **Guides** nach Installation **offline** lesbar; **Wiedergabe** und **Song-ID** nutzen nach Freigabe Apple-Dienste |
| Analyse / Werbung / Tracking | **Keine** — keine Drittanbieter-Analytics, Werbung oder Tracking-SDKs; kein App Tracking Transparency |
| Optionale Apple-Dienste | **Apple Music / MusicKit**, **ShazamKit**, **iCloud** (private KVS), **Fotos (nur hinzufügen)** für Share Cards, optional **StoreKit**-Trinkgeld, **lokale Mitteilungen**, optionale **Live Activities** |

## Datenerfassung

Wir sammeln, verkaufen oder teilen **keine** personenbezogenen Daten zu Werbe- oder Analysezwecken.

- **Kein Konto** — alle mitgelieferten Guides ohne iHTC Studio-Konto nutzbar.
- **Keine Analyse oder Werbung** — keine Drittanbieter-Analytics-, Werbe- oder Crash-SDKs, die uns anrufen.
- **Kein Upload Ihrer Guides** — Favoriten, Listen, Später hören, Notizen, Verlauf und Einstellungen bleiben auf dem Gerät (optional **Ihre** iCloud); nichts geht an iHTC Studio-Server (**wir betreiben kein solches Backend für diese App**).
- **Kein Hosting von Musik** — keine Vollaudio-Dateien im Bundle. Abspielbare Treffer liefert **Apple Music**. Ohne Abo ggf. bis **30 s Katalog-Vorschau** lokal gecacht.

## Funktionsweise der App

- **Mitgelieferte Bibliothek** — Titelindex, Guides, Künstlernotizen, Kategorien, Sammlungen, Zitate, Tageskalender im App-/Widget-Bundle; Guides offline lesbar.
- **Apple Music (MusicKit)** — Nach Freigabe Abgleich mit kuratierter Katalogliste (ISRC zuerst, dann Künstler + Titel) und Wiedergabe über Apple Player. Abostatus bei Apple; Timeout = **unbekannt** (kein „nicht abonniert"-Hardcode). Artwork-URLs ggf. für Cover. Keine Apple-ID-/Zahlungsdaten bei uns.
- **30-Sekunden-Vorschau** — ohne Abo kann Apple-Vorschau in `Caches` landen (LRU, kein Volltrack). Kein Prefetch der nächsten Vorschau bei Mobilfunk/Niedrigenergie/Datensparmodus. Artwork- und Vorschau-Cache in Einstellungen löschbar, ohne Favoriten/Listen anzutasten.
- **Song-ID (ShazamKit)** — nur beim Öffnen von Recognize; Mikrofon verarbeitet **Apple**; keine Aufzeichnungsarchive. Treffer öffnet On-Device-Guide.
- **On-Device-Sprache** — Guide-Vorlesen via **AVSpeechSynthesizer**; Text nicht an iHTC Studio.
- **Widget & App Group** — `group.com.iHTCboy.iMusic` teilt Einstellungen; Live-Activity-Artwork kleines JPEG + Token.
- **Tägliche Mitteilungen** — lokal geplant; Tap → Deep Link zur Titel-ID.
- **Share Cards** — On-Device-Rendering; **Fotos nur hinzufügen** beim Speichern.
- **Optionales Trinkgeld** — **StoreKit**-Verbrauchsartikel.
- **Optionales Spotlight** — **standardmäßig aus**; wenn an, indexiert das System On-Device.

## Auf dem Gerät gespeicherte Daten

| Daten | Ort | Zweck |
|------|-------|---------|
| Guide-Bibliothek (Index + Shards) | App-/Widget-Bundle | Offline-Lesen |
| Favoriten, Listen, Später hören | App Group UserDefaults | Ihre Listen |
| Notizen, Verlauf, Vorlese-Fortschritt | App Group UserDefaults | Fortsetzen |
| Streak / Check-in | App Group UserDefaults | Tägliche Gewohnheit |
| Erscheinungsbild, Sprache, Tabs | App Group UserDefaults | Einstellungen |
| Daily Piece Cache & Mitteilungen | App Group UserDefaults | Heutige ID & Plan |
| Share-Card-Einstellungen | App Group UserDefaults | Letzter Stil |
| Artwork-URLs & decodierte Bilder | App Group + Cache | Cover; Prefetch nach MusicKit-Freigabe |
| 30-S-Vorschaudateien | App Caches | Offline nach erstem Treffer |
| Live-Activity-Thumbnail | App Group JPEG + Token | Lock Screen / Dynamic Island beim **Vorlesen** |
| MusicKit / Shazam-Freigabe | System | Merken Ihrer Wahl |
| Onboarding & Bewertungs-Prompt | Gerät UserDefaults | Willkommen / Review |

Deinstallation entfernt Sandbox und App Group (iOS/macOS-Regeln). Optionale iCloud-Kopien bleiben in **Ihrer** iCloud. Apple-Music-Bibliothek und Abo bleiben bei Apple.

## iCloud-Sync (optional)

Mit **iCloud Sync** in Einstellungen spiegelt **`NSUbiquitousKeyValueStore`** unter **Ihrer Apple-ID**:

- Favoriten, Listen, Später hören, Notizen, Hör-/Leseverlauf, Vorlese-Fortschritt, Streaks

Guide-Texte sind bereits im App-Bundle. Artwork-Dateien und Vorschau-Audio **nicht** per KVS. Traffic nur zu **Apple iCloud**, nicht über iHTC Studio. Abschaltbar; wir lesen Ihre iCloud nicht.

## Berechtigungen

| Berechtigung | Wann | Warum |
|------------|------|-----|
| **Apple Music / Mediathek** | MusicKit-Erklärung oder Wiedergabe-Tap | Abgleich & Play; Cover |
| **Mikrofon** | Song-ID öffnen | Umgebungsmusik erkennen |
| **Mitteilungen** | Daily-Piece-Erinnerung | Lokal geplant |
| **Fotos (nur hinzufügen)** | Musik-Karte speichern | Gerendertes Bild; keine Volllibrary-Lese |
| **iCloud** | Sync aktivieren | Listen/Notizen/Verlauf/Streaks |
| **Live Activities (iOS)** | Reading Live Activity (Standard an) | Guide beim **Vorlesen** auf Sperrbildschirm |
| **Hintergrundaudio** | Option an | MusicKit/Vorschau/TTS im Hintergrund |

Keine Kontakte, präzise Ortung, Kamera oder Tracking. Kein **Lesen** der Fotomediathek.

## Was wir nicht tun

- Kein Verkauf personenbezogener Daten oder Werbeprofile
- Kein erzwungenes Konto oder Social Login
- Keine werbe-/analyseorientierten Drittanbieter-SDKs
- Keine Volltracks auf Gerät oder unseren Servern
- Keine Speicherung von Shazam-Mikrofonpuffern nach Erkennung
- Keine Custom Dynamic Island für **Musikwiedergabe** — nur Guide-Vorlesen (wenn aktiv)
- Keine StoreKit-Kartennummern bei uns

## Datenschutz von Kindern

Keine absichtliche Erhebung bei Kindern unter 13 (oder lokalem Alter). Kein Datensammel-Backend → keine Kinderprofile bei uns. Apple Music & Shazam unterliegen Apples Regeln.

## Drittanbieter

- **Apple** — App Store, MusicKit, ShazamKit, StoreKit, iCloud KVS, TTS, Teilen, Mitteilungen, Live Activities, Siri/Shortcuts
- **Keine** weiteren datensammelnden Drittanbieter-SDKs

## Internationale Nutzer

Guides offline auf dem Gerät. Apple Music, Shazam, iCloud unterliegen Apples Bedingungen und Regionalverfügbarkeit. Katalog-Abgleich hängt von der Storefront der angemeldeten Apple-ID ab.

## Aufbewahrung & Löschung

- **Gerät** — Artwork/Vorschau-Cache unter **Einstellungen → Speicher**; Deinstallation löscht Sandbox/App Group.
- **iCloud (optional)** — bleibt in **Ihrer** iCloud bis Sie Sync aus oder Apple-Tools nutzen.
- **iHTC Studio** — kein serverseitiges Konto zum Löschen.

## Änderungen

Wir können diese Richtlinie aktualisieren; „Zuletzt aktualisiert" oben ändert sich.

## Kontakt

- **E-Mail:** [AppleOSer@gmail.com](mailto:AppleOSer@gmail.com)

Antwort in der Regel innerhalb von 48 Stunden.
