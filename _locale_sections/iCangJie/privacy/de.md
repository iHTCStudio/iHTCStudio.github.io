iHTC Studio („wir“, „uns“ oder „unser“) hat iCangJie (auch bekannt als „爱仓颉“ / „愛倉頡“) entwickelt. Diese Seite beschreibt unsere Richtlinien zur Erhebung, Nutzung und Offenlegung von Daten bei der Nutzung unserer App.

## Zusammenfassung

**iCangJie erhebt, speichert oder überträgt keinerlei personenbezogene Daten.** Alle Zeichensuchen, Quizze, das Tippen-Training und der Lernfortschritt werden ausschließlich auf Ihrem Gerät verarbeitet. Es ist kein Konto erforderlich, und für keine Kernfunktion wird eine Internetverbindung benötigt.

## Datenerhebung

Wir erheben keinerlei Daten. Im Einzelnen:

- Es werden **keine personenbezogenen Informationen** erhoben (kein Name, keine E-Mail-Adresse, keine Telefonnummer, kein Konto).
- Es werden **keine Nutzungsdaten** und keine Analysen erhoben.
- Es sind **keine SDKs von Drittanbietern** für Werbung, Analyse oder Absturzberichte eingebunden.
- Es werden **keine Cookies oder Tracking-Technologien** verwendet.

## iCloud-Synchronisierung

iCangJie bietet eine optionale iCloud-Synchronisierung (in den Einstellungen umschaltbar). Wenn sie aktiviert ist, werden die folgenden Daten über den **iCloud-Schlüssel-Wert-Speicher (iCloud KVS)** synchronisiert, einen vollständig von Apple bereitgestellten und verwalteten Dienst:

| Synchronisierte Daten | Zweck |
|-------------|---------|
| Favoriten | Ihre mit Lesezeichen versehenen Zeichen |
| Lernstatus | Fortschrittsstufe für jedes Zeichen |
| Fehlerheft | Falsch beantwortete Quizfragen |
| Quizergebnisse und Serie | Ihre täglichen Quizleistungen |
| Tippstatistik | Genauigkeit, Serie und Sitzungsanzahl aus dem Tippen-Training |
| Tägliche Tippaufzeichnungen | Zeichenanzahl pro Tag und Histogramme der Codelängen (ca. 120 Tage) |
| Fortschritt in integrierten Texten | Fortsetzungsposition in den integrierten Tipptexten |

Diese Daten werden direkt zwischen Ihren Geräten über Apples iCloud-Infrastruktur übertragen. iHTC Studio betreibt keinen Server und hat keinen Zugriff auf Ihre iCloud-Daten. Für den Umgang von Apple mit iCloud-Daten gilt [Apples Datenschutzrichtlinie](https://www.apple.com/privacy/).

Sie können die iCloud-Synchronisierung jederzeit in den Einstellungen deaktivieren. Wenn sie deaktiviert ist, bleiben alle Daten lokal auf dem jeweiligen Gerät.

Einstellungen der Tipp-Oberfläche (Beibehaltung falscher Tasten, Text-Pinyin) werden lokal auf jedem Gerät gespeichert und **nicht** über iCloud synchronisiert.

## Lokal auf Ihrem Gerät gespeicherte Daten

Alle von iCangJie erzeugten Daten bleiben auf Ihrem Gerät:

| Daten | Speicherung | Kontrolle durch den Nutzer |
|------|---------|--------------|
| Favoriten | Lokal (UserDefaults / App Group) | Einzelne Einträge in der App entfernen oder alle löschen |
| Lernstatus | Lokal (UserDefaults) | In den App-Einstellungen zurücksetzen |
| Fehlerheft | Lokal (UserDefaults) | In der App löschen |
| Quizergebnisse und Serie | Lokal (UserDefaults) | In den App-Einstellungen zurücksetzen |
| Tippstatistik und tägliche Aufzeichnungen | Lokal (UserDefaults / App Group); optional iCloud KVS | Wird beim Zurücksetzen der Lerndaten gelöscht |
| Textfortschritt | Lokal (UserDefaults / App Group); optional iCloud KVS | Wird beim Zurücksetzen der Lerndaten gelöscht |
| Einstellungen der Tipp-Oberfläche | Lokal (UserDefaults) | Unter Einstellungen → Tippen ändern |
| Onboarding- und Einsteigerpfad-Markierungen | Lokal (UserDefaults) | Wird nur erneut angezeigt, wenn Sie die App-Daten zurücksetzen |
| Quiz-Einstellungen | Lokal (UserDefaults) | In den Quiz-Einstellungen ändern |
| Einstellung zur Spotlight-Indizierung | Lokal (UserDefaults) | Unter Einstellungen → Home-Bildschirm-Kurzbefehle umschalten |
| App-Einstellungen und Design | Lokal (UserDefaults) | Durch Löschen der App zurücksetzen |

Widgets nutzen einen **App-Group**-Container, um Daten zwischen der Haupt-App und den Widget-Erweiterungen auszutauschen. Dieser Container bleibt auf Ihrem Gerät und ist für Dritte nicht zugänglich.

### JSON-Sicherung (vom Nutzer ausgelöst)

Sie können eine JSON-Sicherungsdatei (`.icangjie-backup`) mit Lerndaten **exportieren**. Die Datei wird an einem Ort geschrieben, den **Sie wählen** (Dateien, AirDrop usw.). Beim **Import** wird eine von Ihnen ausgewählte Datei gelesen. iHTC Studio lädt Sicherungsdateien weder hoch noch hostet oder öffnet es sie.

### Spotlight-Indizierung (iOS, optional)

Wenn aktiviert, indiziert iCangJie bis zu **80** Favoriten und zuletzt angesehene Zeichen im iOS-Spotlight-Index **auf dem Gerät** (Domain `com.iHTCboy.iCangJie.words`). Einträge laufen nach 30 Tagen ab. Diese Daten verlassen Ihr Gerät nicht, außer über Apples Spotlight-System auf Ihrem iPhone/iPad. Sie können sie jederzeit in den Einstellungen deaktivieren.

## Berechtigungen

iCangJie fordert **nur eine optionale Berechtigung** an:

| Berechtigung | Wann angefordert | Zweck |
|------------|----------------|---------|
| **Fotomediathek (nur Hinzufügen)** | Wenn Sie in einem Tutorial bei einem Wurzeldiagramm-Bild auf **In Fotos sichern** tippen | Das Bild in Ihrer Fotomediathek speichern |

iCangJie liest Ihre vorhandenen Fotos **nicht**. Für die Kernfunktionen gibt es keinen Zugriff auf Kamera, Mikrofon, Kontakte, Standort oder das lokale Netzwerk.

Optionale Funktionen, die externe Websites öffnen (Youdao-Online-Suche, Tutorial-Links), nutzen den System-Browser und gewähren iCangJie keinen Zugriff auf Ihren Browserverlauf.

## Datenschutz für Kinder

iCangJie erhebt wissentlich von niemandem personenbezogene Daten, auch nicht von Kindern unter 13 Jahren. Da überhaupt keine Daten erhoben werden, sind keine besonderen Vorkehrungen erforderlich.

## Änderungen dieser Richtlinie

Wir können diese Datenschutzerklärung von Zeit zu Zeit aktualisieren. Änderungen werden mit aktualisiertem Datum auf dieser Seite veröffentlicht. Wir empfehlen, diese Seite regelmäßig zu prüfen.

## Kontakt

Wenn Sie Fragen zu dieser Datenschutzerklärung haben, kontaktieren Sie uns bitte:

- **E-Mail:** [AppleOSer@gmail.com](mailto:AppleOSer@gmail.com)
