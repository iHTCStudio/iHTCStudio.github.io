iHTC Studio („wir“; früher iHTCTeam) entwickelt **iVeil** (爱修图 / 愛修圖; frühere Versionen hießen iPhoto). Diese Richtlinie erklärt, was mit Ihren Daten geschieht, wenn Sie die App und ihre Teilen-Erweiterung, die Fotos-Bearbeitungserweiterung, Widgets, Kontrollzentrum-Steuerungen und die Kamera auf dem Sperrbildschirm verwenden.

*Zuletzt aktualisiert: 18. Oktober 2026*

## Kurzfassung

- **Kein Account, keine Werbung, keine Analyse, kein Tracking.** iVeil enthält keine SDKs von Drittanbietern für Analyse, Werbung oder Tracking.
- **Ihre Fotos und Videos verlassen Ihr Gerät über iVeil nicht.** Erkennung, Bearbeitung und Export laufen auf dem Gerät. Wir betreiben keine Server, die Ihre Inhalte empfangen.
- **Sie entscheiden, was geteilt wird.** iVeil erzeugt neue Kopien. Originale in Fotos ändern sich nur, wenn Sie eine Bearbeitung mit der Fotos-Bearbeitungserweiterung sichern, und diese Bearbeitung lässt sich in Fotos zurücksetzen.

## Welche Daten iVeil auf Ihrem Gerät verarbeitet

| Daten | Zweck | Was bleibt |
|------|-----|--------------|
| Fotos und Videos, die Sie auswählen (Fotos, das Teilen-Menü, Dateien oder die Kamera) | Zum Prüfen, Verbergen und Bearbeiten | Im App-Sandbox gespeichert, bis Sie sie löschen. Fotos aus der Teilen-Erweiterung durchlaufen kurz den App-Group-Container und werden dann in die App verschoben. |
| Gesichter und Personen (Apple Vision) | Gesichter finden und verbergen, gewählte Personen behalten, einen Emoji-Schleier an die Kopfneigung anpassen, eine behaltene Person freistellen und optional ein Porträt retuschieren | Rechtecke oder Umrisse, die zum erneuten Zeichnen Ihrer Abdeckungen nötig sind, werden mit dem Projekt gespeichert. Gesichtsmerkmale bleiben nur im Arbeitsspeicher. |
| Text in Bildern (Vision-Texterkennung und Apple-Datendetektoren) | Telefonnummern, E-Mails, Adressen, Karten- und Ausweisnummern, Passzeilen, Bestellnummern, Konto-IDs und Links finden | Gespeichert werden nur Bereich und Art. Der erkannte Text selbst wird nicht gespeichert. |
| QR-Codes und Strichcodes | Sie verbergen und mit „Was im Code steckt“ anzeigen, welche Art von Information sie enthalten | Nur Kategorie und Feldnamen (zum Beispiel „Bordkarte: Sitz“) werden gespeichert, niemals der Inhalt. |
| Dateidetails (Ort, Aufnahmezeit, Kamera, Objektiv, Seriennummern) | Zeigen, was eine Datei verrät, und es aus den Kopien entfernen, die Sie teilen | Aus Ihrer Datei gelesen. Kopien behalten nur, was Sie auswählen; Seriennummern und Besitzernamen werden immer entfernt. |
| Möglicherweise sensible Bilder (Apple Sensitive Content Analysis) | Nacktheit oder drastische Inhalte vor dem Teilen weichzeichnen, nur wenn Sie in den Einstellungen die Warnung zu sensiblen Inhalten oder die Kommunikationssicherheit aktiviert haben | Die Analyse läuft auf dem Gerät innerhalb von Apples Framework. Ergebnisse werden weder gespeichert noch gesendet. |
| Apple Intelligence (optional, iOS 26) | „Mit Apple Intelligence erneut prüfen“ und „Einen Look beschreiben“ | Läuft auf Apples On-Device-Modell. Es erhält nur erkannte Textzeilen und Anzahlen oder den Satz, den Sie eingeben, niemals Bilder oder Gesichtsdaten. |
| Unsichtbare Markierung (optional) | Später nachsehen, an wen Sie ein Foto gesendet haben | Ein 32-Bit-Code wird in der Bildhelligkeit verborgen. Die Empfängernamen, die Sie eingeben, bleiben in einer Liste auf Ihrem Gerät (bis zu 500 Einträge), die Sie unter Einstellungen → Unsichtbare Markierung bearbeiten oder leeren können. |
| Freistellungen und Genmoji-Schleier | Ausgeschnittene Personen und eigene Emoji erneut verwenden | Als Bilder im App-Group-Container auf Ihrem Gerät gespeichert, bis Sie sie entfernen. |
| Zuletzt gelöscht | Eine Löschung rückgängig machen | Gelöschte Projekte bleiben 30 Tage und werden danach dauerhaft entfernt. |
| Einstellungen | Sprache, Erscheinungsbild, Aufnahme- und Exportoptionen | Im App-Group-Container auf Ihrem Gerät gespeichert. |

## Gesichtsdaten

iVeil nutzt Apples Vision-Framework auf Ihrem Gerät, um Gesichter und Personen zu **lokalisieren**. Das ist **keine** Gesichtserkennung: iVeil erkennt nicht, wer jemand ist, vergleicht keine Gesichter und erstellt keine biometrischen Vorlagen.

- **Verwendung:** Gesichter verbergen, die Personen behalten, die Sie auswählen, Emoji-Schleier ausrichten, eine behaltene Person freistellen und optional ein Porträt retuschieren.
- **Speicherung:** Normalisierte Gesichtsrechtecke, Personenkonturen und Ihre Retusche-Einstellungen werden im Projekt in der App-Sandbox gespeichert. Vollständige Gesichtsmerkmale werden nie auf die Festplatte geschrieben.
- **Weitergabe:** Gesichtsdaten werden nie hochgeladen, nie an uns oder Dritte weitergegeben und nicht mit iCloud synchronisiert.
- **Aufbewahrung:** Gesichtsdaten bleiben nur so lange wie das Projekt. Das Löschen eines Projekts (nach 30 Tagen in Zuletzt gelöscht) oder das Entfernen der App löscht sie.

## Netzwerk

iVeil hat keine eigenen Server. Die einzigen Netzwerkanfragen stammen von Apple-Diensten:

- **Karten.** Hat ein Foto einen Ort, zeigt iVeil ihn auf einer Apple-Karte, die Kartenkacheln für dieses Gebiet von Apple lädt. Bei **Straßenblock** wird der Ortsname bei Apple anhand der Mitte einer etwa 5 km großen Rasterzelle abgefragt, nicht anhand der genauen Koordinaten. Es werden keine Bildinhalte gesendet. Apple verarbeitet diese Anfragen gemäß [Apples Datenschutzrichtlinie](https://www.apple.com/de/legal/privacy/).
- **Optionales Trinkgeld.** „Entwickler unterstützen“ ist ein Verbrauchskauf in der App, den Apple über StoreKit abwickelt. Er schaltet nichts frei, und wir erhalten keine persönlichen Daten.
- **Optionale iCloud-Synchronisierung (standardmäßig aus).** Wenn Sie sie einschalten, werden wenige Einstellungen (etwa Sprache, Erscheinungsbild und Aufnahme- oder Exportoptionen) über Ihren privaten iCloud-Schlüsselwertspeicher synchronisiert. Fotos, Videos, Gesichtsdaten und die Liste der unsichtbaren Markierung werden nie synchronisiert.

## Berechtigungen

| Berechtigung | Zweck |
|------------|---------|
| Fotos | Die ausgewählten Fotos öffnen und Ort sowie Kameradaten anzeigen |
| Fotos (nur hinzufügen) | Die exportierten Kopien sichern |
| Kamera | Aufnahmetab, Live-Schleier und die Schleier-Kamera auf dem Sperrbildschirm |

iVeil fordert keine Berechtigung für Mikrofon, Ort, Kontakte oder Tracking an. Der Video-Schleier verwendet den Ton, der bereits im ausgewählten Video enthalten ist, und kann ihn entfernen.

## Hintergrundarbeit und Live Activities

Stapel von Sicher teilen und Exporte des Video-Schleiers, die **Sie starten**, können kurz im Hintergrund weiterlaufen. Eine Live Activity kann Titel und Fortschritt auf dem Sperrbildschirm anzeigen. Sie zeigt niemals Bildinhalte.

## Kinder

iVeil erhebt wissentlich keine personenbezogenen Daten von irgendjemandem, auch nicht von Kindern, weil Inhalte auf dem Gerät verarbeitet werden und wir kein Backend zur Datenerhebung betreiben.

## Hinweis

iVeil ist eine unabhängige App und **nicht mit Apple Inc. verbunden.** Die automatische Erkennung ist ein erster Durchgang, keine Garantie. Bitte prüfen Sie ein Foto, bevor Sie es teilen.

## Änderungen

Wenn sich unsere Praxis ändert, aktualisieren wir diese Seite und das Datum oben.

## Kontakt

- **E-Mail:** [AppleOSer@gmail.com](mailto:AppleOSer@gmail.com)
