**Letzte Aktualisierung:** 6. September 2026 

iHTC Studio („wir“, „uns“ oder „unser“) hat **iBrowser** erstellt (auch bekannt als „全屏浏览器“ / „全螢幕瀏覽器“, Bundle-ID `full.screen.browser`). Diese Datenschutzrichtlinie erläutert, welche Daten bei der Nutzung der App verarbeitet werden (und welche nicht). **Apple App Review** und Benutzer können sich auf diese Seite als öffentliche Datenschutz-URL verlassen. Öffnen Sie für App Store Connect diese Seite mit den Datenschutzbestimmungen (../privacy) und kopieren Sie die Adresse aus der Adressleiste des Browsers. 

## Zusammenfassung (Ausrichtung des Apple Privacy Nutrition Label) 

| Thema | Unsere Praxis | 
|-------|----------------| 
| Konto | **Nicht erforderlich** – keine Registrierung oder Anmeldung bei iHTC Studio | 
| Datenerfassung durch iHTC Studio | **Daten werden nicht erfasst** – wir betreiben **kein** Backend, das Ihre Lesezeichen oder Einstellungen empfängt | 
| Werbung | **Keine** – keine Werbung, kein Anzeigen-SDK, keine Aufforderung zur App-Tracking-Transparenz für Anzeigen | 
| Inhalte durchsuchen | Von Ihnen geöffnete Seiten werden **direkt von WebKit** von diesen Websites geladen; Wir betreiben keinen Browsing-Proxy | 
| Optionale Apple-Synchronisierung | **iCloud Key-Value Storage** – standardmäßig deaktiviert; nur, wenn Sie es unter Einstellungen | aktivieren 

## Datenerfassung

- **Kein Konto** – Sie können die App nutzen, ohne ein Konto bei uns zu erstellen. 
- **Keine Werbung oder Analyse-SDK** – Die App zeigt iHTC Studio keine Werbung oder Phone-Home-Analysen an. 
- **Kein iHTC Studio-Backend für Ihre Lesezeichen** – Einstellungen bleiben auf Ihrem Gerät (und optional in **Ihrer** Apple iCloud). Wir hosten keinen Server, der Ihre Lesezeichenliste empfängt. 

### Surfen im Internet 

Wenn Sie zu einer Website navigieren oder eine Suchmaschine verwenden: 

- Ihr Gerät kontaktiert **diese Website** (oder diesen Suchanbieter) über das Netzwerk, wie bei jedem Browser. 
- Diese Dritten sehen möglicherweise Standardanfrage-Metadaten (IP-Adresse, Benutzeragent, von ihnen gesetzte Cookies, von Ihnen angeforderte Seiteninhalte). Es gelten deren Datenschutzrichtlinien. 
– Durch die Auswahl einer integrierten oder benutzerdefinierten **Suchmaschine** wird nur ein Such-URL-Präfix auf dem Gerät festgelegt. 

### Widgets, Verknüpfungen und Deep Links 

Startbildschirm-/Sperrbildschirm-Widgets, Siri, Verknüpfungen, Schnellaktionen auf dem Startbildschirm und `ibrowser://`-Links öffnen Ziele **auf Ihrem Gerät**. Sie senden Ihren Browserverlauf nicht an iHTC Studio. 

## Auf Ihrem Gerät gespeicherte Daten

| Daten | Wo | Zweck | 
|------|-------|---------| 
| Homepage-URL | UserDefaults (+ App-Gruppen-Snapshot) | Startseite; Widget-Anzeige | 
| Suchmaschinenpräfix | Benutzerstandards | Suche in der Adressleiste | 
| Lesezeichen | UserDefaults (JSON) (+ App-Gruppen-Snapshot) | Lokale Favoriten; Lesezeichen-Widgets | 
| Kindersicherung / Force-Hide-Chrom | UserDefaults (+ App-Gruppe) | Immersive & Kinder-/Kiosk-Modi | 
| Floatball ein/aus & Menüreihenfolge | Benutzerstandards | Abkürzungsangebot | 
| Schwimmerball **Position** | UserDefaults (nur Gerät) | Wo Sie den Ball gelassen haben – **nicht** mit iCloud synchronisiert | 
| Letzte erfolgreich geladene Seite | UserDefaults (+ App-Gruppe) | „Zuletzt fortfahren“ – **nur Gerät**, nicht iCloud | 
| Einstellungen Passwort | **Schlüsselanhänger** (`WhenUnlockedThisDeviceOnly`) | Optionale Einstellungssperre – **nicht** in UserDefaults, App Group oder iCloud | 
| Browserränder | Benutzerstandards | Inhaltseinfügungen | 
| Aussehen / Sprache | UserDefaults (nur Gerät) | Design und UI-Sprache – **nicht** iCloud | 
| Schnellauftrag auf dem Startbildschirm | UserDefaults (nur Gerät) | Menü lange drücken – **nicht** iCloud | 
| Erstausgabe-Leitfaden und Begriffsflaggen | UserDefaults (nur Gerät) | Onboarding | 
| Widget-Schnappschüsse | App-Gruppe `group.full.screen.browser` | Schreibgeschützte Anzeige für die Widget-Erweiterung |

Durch die Deinstallation der App werden ihre Sandbox- und App-Gruppendaten entfernt (abhängig vom iOS-Verhalten). Optionale iCloud-Kopien bleiben in **Ihrer** iCloud, bis Sie sie löschen oder die Synchronisierung an anderer Stelle deaktivieren. 

## Optionale iCloud-Synchronisierung 

Wenn Sie **iCloud Sync** in den Einstellungen aktivieren (standardmäßig **aus**), werden ausgewählte Einstellungen über Apples **`NSUbiquitousKeyValueStore`** gespiegelt, das an **Ihre Apple-ID** gebunden ist: 

**Kann synchronisiert werden:** Lesezeichen, Startseite, Suchmaschine, Ränder, Adressleisten-/Symbolleisten-Anzeigesperren, Float-Ball ein/aus, Float-Ball-Menüreihenfolge. 

**Wird nicht synchronisiert:** Einstellungen Passwort, letzte Seite („Letzte Seite fortsetzen“), Float-Ball-Position, Aussehen, Sprache, Schnellaktionsreihenfolge auf dem Startbildschirm, Markierungen für Anleitungen/Begriffe. 

Der Synchronisierungsverkehr geht an **Apple iCloud**, nicht an iHTC Studio. Sie können die Synchronisierung deaktivieren oder in den Einstellungen auf **Jetzt synchronisieren** tippen. Wir können Ihre iCloud-Inhalte nicht lesen. 

## Berechtigungen 

Abhängig von der Website können Webseiten über WebKit Gerätefunktionen anfordern (z. B. Kamera, Mikrofon oder Standort). Systemaufforderungen werden nur angezeigt, wenn eine Seite danach fragt. Die App deklariert außerdem Funktionszeichenfolgen, die Webinhalte möglicherweise benötigen. Wir verwenden diese Berechtigungen nicht für eine separate native soziale oder Werbefunktion.

| Bereich | Hinweise |
|--------|---------|
| Netzwerk | Wird benötigt, um Websites zu laden und zu suchen |
| Bewegung (Schütteln) | Wird auf dem **iPhone** verwendet, um den Float-Ball/Chrome wiederherzustellen – die Verarbeitung erfolgt lokal; **iPad** verwendet stattdessen Tippen-nahe-oben |
| iCloud | Nur, wenn Sie die Synchronisierung aktivieren |
| Mail / Teilen-Menü | Optionale Rückmeldungen oder Freigabeaktionen, die Sie initiieren |
| StoreKit (optionales Trinkgeld) | Verbrauchbares Trinkgeld, das von Apple verarbeitet wird; schaltet keine Funktionen frei |

## Datenschutz von Kindern

Die Kindersicherung ist eine **lokale UI-Beschränkung** (Adressleiste ausblenden / optionales Einstellungs-Passwort). Solange sie aktiviert ist, öffnen Widgets, Kurzbefehle und nicht-Haupt-Lesezeichen stattdessen **Startseite**. Sie erstellt **kein** Kinderkonto bei uns. Wir fordern wissentlich keine persönlichen Informationen von Kindern für Marketingzwecke an. Eltern sollten überwachen, welche Websites geöffnet werden.

## Was wir nicht tun

- Wir benötigen **kein** ein iHTC Studio-Konto. 
- Wir zeigen **keine** In-App-Werbung oder Interstitial-Werbe-Popups an (abgesehen von den erforderlichen Erstauflagen). 
- Wir betreiben **keine** eigenen Cloud-Synchronisierungsserver für diese App (für die optionale Synchronisierung wird nur **Ihre** Apple iCloud verwendet). 
- Wir verkaufen Ihre Daten **nicht**. 
- Wir speichern das Einstellungskennwort **nicht** in einfachen Benutzerstandards (es verwendet den Schlüsselbund auf dem Gerät). 

## Dritte 

| Party | Rolle | 
|-------|------| 
| **Apfel** | App-Store-Vertrieb; optionales iCloud KVS; Widgets / Siri / Verknüpfungen; Mail, Share Sheet, Safari View Controller; optionaler StoreKit-Tipp | 
| **Websites und Suchmaschinen, die Sie öffnen** | Erhalten Sie normalen Browserverkehr für die von Ihnen besuchten Seiten | 

## Aufbewahrung und Löschung 

Lokale Einstellungen und Lesezeichen bleiben erhalten, bis Sie sie ändern oder löschen oder die App deinstallieren. Optionale iCloud-Daten unterliegen weiterhin den Richtlinien von Apple, bis Sie die Synchronisierung deaktivieren und/oder sie über die Tools von Apple löschen. Da wir auf unseren Servern keine personenbezogenen Daten erfassen, gibt es keinen Kontodatensatz, den wir über die Beantwortung Ihrer E-Mail hinaus löschen könnten. 

## Änderungen an dieser Richtlinie

Wir können diese Seite von Zeit zu Zeit aktualisieren. Das oben angezeigte Datum „Zuletzt aktualisiert“ wird sich ändern, wenn wir dies tun. Die fortgesetzte Nutzung nach Änderungen bedeutet, dass Sie die aktualisierte Richtlinie akzeptieren.

## Kontaktieren Sie uns

- **E-Mail:** [AppleOSer@gmail.com](mailto:AppleOSer@gmail.com)

Öffnen Sie diese [Datenschutzerklärung](../privacy) Seite in einem Browser und kopieren Sie die Adressleiste-URL, wenn Sie den öffentlichen Link für App Store Connect benötigen.
