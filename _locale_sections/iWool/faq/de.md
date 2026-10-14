### Funktioniert iWool auf dem iPad?

Ja. iWool ist eine universelle App für **iPhone und iPad** (iOS 15.0+). Das Layout passt sich den Bildschirmgrößen des iPad an. Widgets und Live-Aktivitäten folgen denselben Regeln wie auf dem iPhone.

### Benötigt iWool ein Konto oder eine Internetverbindung?

Nein. iWool funktioniert vollständig offline. Alle Daten werden mithilfe von SQLite lokal auf Ihrem Gerät gespeichert. Für die Nutzung einer Funktion sind kein Konto, keine Anmeldung und keine Netzwerkverbindung erforderlich (außer dem Öffnen von http/https-Links innerhalb der App).

### Wo werden meine Daten gespeichert? Ist es sicher?

Alle Daten – Aktivitäten, Erinnerungen, Verdienstaufzeichnungen, Wiederholungsstatus – werden in einer lokalen SQLite-Datenbank auf Ihrem Gerät gespeichert. Es wird nichts auf einen Server hochgeladen. Wenn Sie die App deinstallieren, werden Ihre Daten gelöscht. Sichern Sie regelmäßig mit **Einstellungen → Daten → Vollständige Sicherung exportieren**.

### Wie kann ich meine Daten sichern und wiederherstellen?

Gehen Sie zu **Einstellungen → Daten → Vollständige Sicherung exportieren**, um eine CSV-Datei zu generieren. Speichern Sie es in Dateien, übertragen Sie es per AirDrop auf Ihren Mac oder senden Sie es per E-Mail.

Gehen Sie zum Wiederherstellen zu **Einstellungen → Daten → Backup importieren** und wählen Sie Ihre Datei aus. Sie werden aufgefordert, zwischen Folgendem zu wählen:

- **Alle Daten ersetzen** – löscht alles und stellt die Daten aus dem Backup wieder her. Verwenden Sie dies, wenn Sie Geräte wechseln oder eine Neuinstallation durchführen.
- **Nur anhängen (bestehendes beibehalten)** – Fügt Sicherungsaktivitäten als neue Datensätze ein, ohne etwas auf Ihrem Gerät zu löschen. Verwenden Sie dies, um Daten von einem anderen Gerät zusammenzuführen.

### Wie funktionieren wiederkehrende Aktivitäten?

Wenn Sie eine Wiederholungsregel festlegen (täglich, wöchentlich, monatlich, jährlich oder ein benutzerdefiniertes Intervall), speichert iWool einen Stammdatensatz und erweitert ihn virtuell in einzelne Vorkommnisse an jedem Tag. In der Liste und im Kalender wird für eine wiederkehrende Serie immer das heutige Ereignis angezeigt.

Um das Vorkommen eines bestimmten Tages als abgeschlossen zu markieren, verwenden Sie das Menü durch langes Drücken oder die Symbolleiste unten auf der Detailseite. Das markiert nur diesen Tag; Die Serie geht weiter.

### Warum wird eine Erinnerung nicht angezeigt?

iOS beschränkt jede App auf etwa 64 ausstehende lokale Benachrichtigungen gleichzeitig. iWool priorisiert einmalige Aktivitäten und plant bis zu 120 Tage zukünftiger Ereignisse für wiederkehrende Aktivitäten, aber sehr große Sammlungen wiederkehrender Erinnerungen können gekürzt werden.

Überprüfen Sie **Einstellungen → Benachrichtigungen → Geplante lokale Erinnerungen**, um genau zu sehen, welche Erinnerungen derzeit registriert sind.

Überprüfen Sie außerdem:

- Die Benachrichtigungsberechtigung wird erteilt (iOS-Einstellungen → iWool → Benachrichtigungen).
- Die Aktivität wird nicht storniert (bei stornierten Aktivitäten werden die Erinnerungen automatisch gelöscht).
- Der Erinnerungszeitpunkt liegt in der Zukunft.

### Was ist der Unterschied zwischen „geschätztem Verdienst“ und „erfasstem Verdienst“?

- **Geschätzter Verdienst** – im Aktivitätsformular eingegeben. Wird auf der Aktivitätskarte angezeigt. Zählt nicht in der Statistik.
- **Erfasste Einnahmen** – werden auf der Aktivitätsdetailseite über das Einkommensformular eingegeben. Dies sind die tatsächlichen Beträge, die in allen Statistiksummen, Trenddiagrammen und Plattformrankings gezählt werden.

### Wie erfasse ich Einnahmen für einen bestimmten Tag einer wiederkehrenden Aktivität?

Öffnen Sie die Aktivitätsdetails für das Ereignis an diesem Tag (tippen Sie in der Liste oder im Kalender auf die Aktivität an diesem Tag). Tippen Sie auf der Detailseite im Abschnitt „Einnahmen“ auf **Aufzeichnen**. Als Aufnahmedatum wird standardmäßig das Ereignisdatum dieses Tages verwendet.

### Kann ich einen einzelnen Einnahmeneintrag löschen, ohne dass sich dies auf die Aktivität auswirkt?

Ja. Öffnen Sie die Aktivitätsdetails, tippen Sie auf die Verdienstzeile, die Sie bearbeiten möchten, und scrollen Sie im Bearbeitungsformular nach unten. Tippen Sie auf **Diesen Verdienstdatensatz löschen** und bestätigen Sie. Nur dieser eine Eintrag wird entfernt; die Aktivität und alle anderen Aufzeichnungen bleiben davon unberührt.

### Das Statistikdiagramm zeigt falsche Beträge für japanische Yen (JPY) / koreanische Won (KRW).

Diese Währungen haben standardmäßig keine Dezimalstellen, was dazu führen konnte, dass Beträge in älteren Versionen als ganze Zahlen angezeigt wurden. In der aktuellen Version können Sie die Anzahl der Nachkommastellen unabhängig konfigurieren:

- Gehen Sie zu **Einstellungen → Darstellung und Sprache → Betragsdezimalstellen**, um die Anzahl der Dezimalstellen für alle Betragsanzeigen festzulegen (Standard: 2).
- Gehen Sie zu **Einstellungen → Darstellung und Sprache → Dezimalstellen für Diagrammanzahl**, um die Dezimalstellen für Diagrammbalkenbeschriftungen speziell festzulegen (Standard: 0).

### Wie verwende ich die Funktion „Dynamische Insel/Live-Aktivität“?

**Ereignis-Countdown** (iOS 16.1+, unterstütztes iPhone): aktivieren Sie in **Einstellungen → Benachrichtigungen → Live-Aktivität**. Legen Sie die Vorlaufzeit fest (1–480 Minuten). Aktivitäten im Fenster werden automatisch ausgewählt; Drücken Sie lange auf „Startseite“ oder „Kalender“ → **Zur dynamischen Insel hinzufügen**.

**Quick Countdown** (iOS 16.2+): a **standalone** island timer **not tied to your activity database**. Open **Settings → Island Reminder**, use a Home Screen Quick Action, or `iwool://island`. Duration **1 second to 8 hours**; optional title, note and accent colour. When it ends, the Live Activity dismisses — nothing is saved unless you create a wool activity separately.

### Was ist Quick Countdown im Vergleich zu Event-Live-Aktivität?

|  | Countdown zum Ereignis | Schneller Countdown |
|---|-----------------|-----------------|
| Mit Aktivität verknüpft | Ja | Nein |
| In der App bestehen geblieben | Ja | Nein |
| Mindestens iOS | 16.1 | 16.2 |
| Wie fange ich an? | Automatische oder lange Betätigung | Einstellungen / Verknüpfung / `iwool://island` |

### Wie funktionieren Schnellaktionen auf dem Startbildschirm?

Long-press the iWool icon (iOS). Choose up to **4** from **9** presets in **Settings → Tools → Home Screen Shortcuts**: Home, Calendar, Statistics, Quick Countdown, New Activity, Scheduled Reminders, Scanner, Rate, Feedback. Default: Home, Calendar, Statistics, Quick Countdown. Each uses an `iwool://` URL.

### How do `iwool://` deep links work?

iWool unterstützt **`iwool://`** für Registerkarten, Aktionen und Ereignisdetails – verwendet von Widgets, Verknüpfungen und Schnellaktionen. Beispiele:

- `iwool://home`, `iwool://calendar`, `iwool://stats`, `iwool://settings`
- `iwool://new`, `iwool://island`, `iwool://scanner`, `iwool://reminders`
- `iwool://event/42`, `iwool://event/42?day=189345600` (recurring occurrence)

Unbekannte Pfade werden ignoriert (keine stille Weiterleitung zur Startseite). Sehen Sie sich die vollständige [**URL-Schema-Referenz**](../url-scheme) an.

### Wie teile ich eine Aktivität oder Statistiken als Bild?

Verwenden Sie auf einer Aktivitätsdetailseite oder in der Symbolleiste der Registerkarte **Statistik** **Teilen**, um eine gebrandete **PNG-Bildkarte** zu rendern (Farbverlauf, QR-Code, optionale Einnahmen, falls in den Einstellungen aktiviert). Das Bild wird auf dem Gerät generiert; Beim Speichern in „Fotos“ kann der Zugriff auf die Fotobibliothek erforderlich sein.

### Wie viele Widgets enthält iWool?

**12 Widget-Familien** – acht Startbildschirm-Widgets (Heute aktiv, Heute alle, Heute demnächst, Alle Ereignisse, Statistikübersicht, Einnahmen, Überblick, Top-Plattformen) plus vier Sperrbildschirm-Zubehörstile (iOS 16+).

### Wie füge ich Widgets zu meinem Startbildschirm oder Sperrbildschirm hinzu?

Detaillierte Schritt-für-Schritt-Anleitungen finden Sie unter **Einstellungen → Widgets → Widget-Anleitung** in der App. Kurz gesagt:

1. Long-press an empty area of your Home Screen and tap the **+** button.
2. Suchen Sie in der Widget-Galerie nach **iWool**.
3. Wählen Sie einen Widget-Stil und eine Widget-Größe und tippen Sie dann auf **Widget hinzufügen**.

Für Sperrbildschirm-Widgets (iOS 16+): Drücken Sie lange auf den Sperrbildschirm und tippen Sie auf **Anpassen**. Fügen Sie dann iWool-Widgets zur Zeile mit den Sperrbildschirm-Widgets hinzu.

### Warum zeigt das Widget veraltete Daten an?

Widgets werden aktualisiert, wenn Sie die App öffnen oder wenn sich Daten ändern. iOS aktualisiert die Widget-Zeitleisten außerdem regelmäßig im Hintergrund (bestenfalls etwa alle 15 Minuten). Wenn das Widget veraltet ist, öffnen Sie iWool einmal, um eine Aktualisierung zu erzwingen.

### Wie ändere ich die Anzeigesprache?

Gehen Sie zu **Einstellungen → Darstellung und Sprache → Anzeigesprache**. Sie können unabhängig von der Systemsprache Ihres Geräts aus 13 Sprachen wählen:

Englisch, vereinfachtes Chinesisch, traditionelles Chinesisch, Japanisch, Koreanisch, Thailändisch, Hindi, Spanisch, Französisch, Deutsch, brasilianisches Portugiesisch, Russisch, Arabisch.

Die Änderung wird sofort in der gesamten App wirksam.

### Kann ich eine Aktivität teilen, ohne meine Verdienstbeträge zu teilen?

Ja. Standardmäßig werden beim Kopieren oder Teilen einer Aktivität Ihre Verdienstdaten nicht berücksichtigt. Wenn Sie sie einbeziehen möchten, gehen Sie zu **Einstellungen → Erscheinungsbild und Sprache** und aktivieren Sie **Einnahmen beim Teilen berücksichtigen**.

### Wie scanne ich einen QR-Code oder Barcode?

Gehen Sie zu **Einstellungen → Extras → QR-/Barcode-Scanner**. Richten Sie Ihre Kamera auf einen Code oder tippen Sie auf das Albumsymbol, um ein Bild auszuwählen. Die Ergebnisse werden in einer Liste angezeigt, die Sie kopieren oder in Safari öffnen können.

Sie können auch direkt vom Aktivitätsformular aus scannen: Tippen Sie beim Ausfüllen des Aktivitäts-URL-Felds auf das Scan-Symbol daneben, um einen Code zu scannen und die URL automatisch auszufüllen.

### Was bedeutet „Archiv“? Ist es dasselbe wie löschen?

Nein. Durch die Archivierung wird eine Aktivität aus der Hauptliste ausgeblendet, ohne sie zu löschen. Archivierte Aktivitäten können unter **Einstellungen → Aktivitätsverwaltung → Archivierte Aktivitäten** angezeigt, wiederhergestellt oder gelöscht werden.

Drücken Sie lange auf eine abgeschlossene, abgelaufene oder abgebrochene Aktivität, um die Option „Archivieren“ anzuzeigen. Um alle abgeschlossenen, abgelaufenen und stornierten einmaligen Aktivitäten auf einmal zu archivieren, verwenden Sie **Einstellungen → Aktivitätsverwaltung → Alle abgeschlossenen archivieren**.

### Brauchen Sie noch Hilfe?

Kontaktieren Sie uns unter [AppleOSer@gmail.com](mailto:AppleOSer@gmail.com) oder nutzen Sie die In-App-Option **Einstellungen → Feedback senden**. Wir antworten in der Regel innerhalb von 48 Stunden.
