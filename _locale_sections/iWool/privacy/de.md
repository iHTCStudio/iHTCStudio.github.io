iHTC Studio („wir“, „uns“ oder „unser“) hat iWool (auch bekannt als „爱羊毛“) entwickelt. Auf dieser Seite informieren wir Sie über unsere Richtlinien zur Erhebung, Nutzung und Offenlegung personenbezogener Daten bei der Nutzung unserer App.

## Zusammenfassung

**iWool erhebt, speichert oder übermittelt keine personenbezogenen Daten.** Die App läuft vollständig auf Ihrem lokalen Gerät und erfordert kein Konto, keine Internetverbindung und keine Cloud-Dienste.

## Datenerfassung

Wir erheben keine Daten. Konkret:

- **Es werden keine persönlichen Daten** erfasst (kein Name, E-Mail, Telefonnummer oder Konto).
- **Es werden keine Nutzungsdaten** oder Analysen erfasst.
- **Keine Aktivitäten, Einnahmen oder Inhalte**, die Sie in der App erstellen, sind für uns zugänglich.
- **Es werden keine Cookies oder Tracking-Technologien** verwendet.
- **Es sind keine Dienste Dritter** (Werbung, Analysen, Absturzberichte) integriert.

## So funktioniert die App

iWool speichert alle Daten – Aktivitäten, Erinnerungen, Verdienstaufzeichnungen, Wiederholungsstatus und Vorlagen – in einer lokalen SQLite-Datenbank auf Ihrem Gerät:

- Die Daten verlassen niemals Ihr Gerät, es sei denn, Sie exportieren ausdrücklich ein Backup und entscheiden sich dafür, es selbst zu teilen.
- Für keine der Kernfunktionen der App ist eine Internetverbindung erforderlich.
- Das Öffnen von http/https-Links aus der App heraus (in der integrierten Safari-Ansicht) folgt dem standardmäßigen iOS-Netzwerkverhalten; Die verlinkte Seite wird von Ihrem Gerät direkt von seinem Host geladen, nicht über einen iHTC Studio-Server.

## Berechtigungen

iWool fordert die folgenden Geräteberechtigungen nur bei Bedarf an:

| Erlaubnis | Zweck |
|------------|---------|
| Benachrichtigungen | Planen und versenden Sie lokale Erinnerungen für Ihre Aktivitäten |
| Kamera | Scannen Sie QR-Codes und Barcodes mit dem integrierten Scanner-Tool |
| Fotobibliothek (Lesen) | Wählen Sie Bilder für die QR-/Barcode-Erkennung aus |
| Live-Aktivitäten | Zeigen Sie die dynamische Insel- und Sperrbildschirm-Liveaktivität für bevorstehende Aktivitäten an (iOS 16.1+) |

Diese Berechtigungen werden ausschließlich für die angegebenen Zwecke verwendet. Es werden keine Daten, auf die über diese Berechtigungen zugegriffen wird, an einen externen Server oder Dritte übertragen.

## Datenspeicherung

- **Activity data** (activities, reminders, earnings records, recurrence completion states, templates) is stored locally in a SQLite database file (`iWool.sqlite`) in the app's support directory on your device.
- **App-Einstellungen** (Thema, Sprache, Währung, Badge-Strategie, Erinnerungseinstellungen usw.) werden lokal mithilfe von UserDefaults auf Ihrem Gerät gespeichert.
- **Widget snapshot** — a lightweight JSON summary of your current activities and earnings — is written to an App Group container (`group.com.iHTCboy.iWool`) shared between the main app and the widget extension. This data never leaves your device.
- Es werden keine Daten auf externen Servern oder Cloud-Diensten gespeichert.

## Dateien sichern und Bilder teilen

Wenn Sie **Einstellungen → Daten → Vollständige Sicherung exportieren** verwenden, generiert iWool eine CSV-Datei auf Ihrem Gerät. Die Datei enthält Ihre Aktivitäten, Erinnerungen, Verdienstaufzeichnungen, Wiederholungsstatus und Vorlagen. Diese Datei wird lokal erstellt und nur freigegeben, wenn Sie sich ausdrücklich dafür entscheiden (z. B. Speichern in Dateien oder Senden per AirDrop oder E-Mail). Wir haben keinen Zugriff auf diese Datei.

**Bildkarten zum Teilen** (PNG) werden vollständig auf Ihrem Gerät gerendert, wenn Sie in einer Aktivitäts- oder Statistikansicht auf „Teilen“ tippen. iWool lädt diese Bilder nicht hoch.

## Privatsphäre von Kindern

iWool erhebt wissentlich keine personenbezogenen Daten von irgendjemandem, auch nicht von Kindern unter 13 Jahren. Da wir überhaupt keine Daten erfassen, sind keine besonderen Bestimmungen erforderlich.

## Änderungen an dieser Richtlinie

Wir können diese Datenschutzrichtlinie von Zeit zu Zeit aktualisieren. Alle Änderungen werden mit aktualisiertem Datum auf dieser Seite veröffentlicht. Wir empfehlen Ihnen, diese Seite regelmäßig zu überprüfen.

## Kontaktieren Sie uns

Wenn Sie Fragen zu dieser Datenschutzrichtlinie haben, kontaktieren Sie uns bitte:

- **E-Mail:** [AppleOSer@gmail.com](mailto:AppleOSer@gmail.com)
