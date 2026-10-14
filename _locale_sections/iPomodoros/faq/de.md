### Warum sollte ich iPomodoro anderen Pomodoro-Apps vorziehen?

iPomodoro ist eine **native SwiftUI**-App, die für Apple-Plattformen entwickelt wurde — kein verpackter Web-Timer. Du erhältst **fünf integrierte Tabs** (Pomodoro, Study Timer, Aufgaben, Statistik, Einstellungen), **doppelte Live-Aktivitäten**, **fünf Widget-Familien**, **9 Erfolgsabzeichen**, **über 1000 Zitate auf dem Gerät**, **Siri- & URL-Kurzbefehle** sowie **optionale iCloud-Synchronisation** — das alles mit **null Analysen** und **ohne erforderliches Konto**. Eine ruhige App, die Fokus, Deadlines und Fortschrittsverfolgung von Anfang bis Ende abdeckt.

### Wo befinden sich die Timer- und Aufgabeneinstellungen?

Timer-Dauern, Sounds, Live-Aktivität, Seitenhintergrundfarben, optional **Fokus-Modus-Erinnerung** und (nur Pomodoro) optionale **Phase-Abschluss-Bestätigung** befinden sich unter dem **Zahnrad-Symbol** jeder Registerkarte (Pomodoro, Lern-Timer, Aufgaben oder **Statistiken**). Die globale **Einstellungen**-Registerkarte enthält Erscheinungsbild, Sprache, **Startbildschirm-Verknüpfungen**, **App-Anleitung**, Benachrichtigungsberechtigung, motivierende Zitate (einschließlich **täglicher Motivationsbenachrichtigung**), Widget-Anleitung, Feedback und Informationen — nicht die Modi-spezifischen Dauern. **Statistiken**-Einstellungen (Seitenhintergrund, Ziele, optionale iCloud-Synchronisierung, Erfolge, Zählregeln, CSV, Aufbewahrung) befinden sich unter **Statistik-Registerkarte → Zahnrad**.

### Wie funktionieren Startbildschirm-Verknüpfungen und Siri?

**Drücken Sie lange auf das App-Symbol**, um schnelle Aktionen auszuführen – Pomodoro, Lerntimer, Aufgaben, Statistiken, ein Motivationszitat oder Feedback zu öffnen. Passen Sie an, welche vier unter **Einstellungen → App-Einstellungen → Startbildschirm-Verknüpfungen** angezeigt werden (zum Neuordnen ziehen). Sie können dieselben Ziele auch über **`iPomodoro://`** URLs öffnen (`pomodoro`, `study`, `tasks`, `stats`, `motivation`, `feedback`; `iPomodoros://` funktioniert auch). Sehen Sie sich die vollständige [URL-Schema-Referenz](../url-scheme) an. **Siri / Shortcuts-App** kann über integrierte App-Shortcuts Tabs öffnen oder antworten: „Wie lange habe ich mich heute in iPomodoro konzentriert?“*. 

### Was ist der In-App-App-Guide? 

**Einstellungen → App-Einstellungen → App-Leitfaden** – ein zusammenklappbares Tutorial, das alle fünf Registerkarten, Widgets, Verknüpfungen, iCloud und FAQ abdeckt (ähnlicher Stil wie der Widget-Leitfaden). 

### Kann iPomodoro den Fokusmodus für mich aktivieren? 

Nein – iOS erlaubt es Drittanbieter-Apps nicht, Focus direkt zu aktivieren. Die optionale **Fokusmodus-Erinnerung** (Pomodoro- oder Lerntimer-Zahnradeinstellungen) prüft, ob der Fokus ausgeschaltet ist, wenn Sie einen Timer starten, und zeigt eine Warnung an; Sie können **Einstellungen** über die Benachrichtigung öffnen, müssen den Fokus jedoch selbst aktivieren. 

### Kann ich für jede Countdown-Aufgabe eine Farbe auswählen?

Ja. Beim Hinzufügen oder Bearbeiten einer Aufgabe wählen Sie eine von **9 Akzentfarben**. Die Liste und das **Countdown-Aufgaben**-Widget verwenden diese Farbe pro Zeile. Die Farben werden über iCloud synchronisiert, wenn die Aufgaben-Synchronisation aktiviert ist.

### Kann ich Statistiken nach einem benutzerdefinierten Datumsbereich filtern?

Ja. Auf der Registerkarte Statistiken (oder im Periodenbericht) wählen Sie **Benutzerdefiniert** in der Periodenleiste und legen dann Start- und Enddatum fest. Der Bereich wird gespeichert, wenn **Filter merken** in den Statistik-Einstellungen aktiviert ist.

### Kann ich eine tägliche Motivationsbenachrichtigung erhalten?

Ja. **Einstellungen → Motivationszitat-Einstellungen** enthält eine optionale **tägliche Motivationsbenachrichtigung** — wählen Sie eine Uhrzeit und iPomodoro plant eine wiederholte **lokale Benachrichtigung** mit einer zufälligen Zeile aus dem auf dem Gerät gespeicherten Benachrichtigungs-Zitate-Pool (kein Netzwerk). Getrennt von Timer-Abschlusswarnungen.

### Was ist der Unterschied zwischen täglichen Zitaten und Benachrichtigungszitaten?

**Dialog-/tägliche Zitate** (**1000+** zusammen, wenn der Filter auf Alle steht — vereinfachtes Chinesisch + Englisch) versorgen das Start-Popup, die Einstellungen-Browse, den Live-Aktivitäts-Hinweis und das Motivation-Widget. **Benachrichtigungszitate** sind ein separater, geräteinterner Pool (**365 allgemeine Zeilen pro Sprache**), der nur für Hintergrund-Timer-Abschlussbenachrichtigungen verwendet wird. Beide respektieren Ihren Zitat-Sprachfilter in den Einstellungen.  

### Was ist die Pomodoro-Technik?  

Die Pomodoro-Technik ist eine Methode des Zeitmanagements: arbeite in fokussierten Intervallen (klassisch 25 Minuten) und mache dann eine kurze Pause. Nach mehreren Zyklen, mache eine längere Pause. iPomodoro automatisiert diesen Rhythmus, damit du dich auf die Arbeit und nicht auf die Uhr konzentrieren kannst.  

### Wie unterscheidet sich iPomodoro von der alten Flutter-Version?  

Dies ist eine **vollständige SwiftUI-Neuschreibung** für Apple-Plattformen. Gleiche Kernideen — Pomodoro, Lern-Timer, Countdown-Aufgaben — aber mit nativer Leistung, Live-Aktivität, modernen Widgets und engerer iOS-Integration.  

### Brauche ich ein Konto oder eine Internetverbindung?

Es ist kein iPomodoro-Konto erforderlich. Timer, Studienstatistiken, Themen und Widgets laufen **vollständig offline** auf Ihrem Gerät. **Optional:** aktivieren Sie **Aufgaben mit iCloud synchronisieren** (Aufgaben → Zahnrad) und/oder **Studienstatistiken mit iCloud synchronisieren** (Statistik → Zahnrad), um Daten über Geräte hinweg zusammenzuführen, die bei derselben Apple-ID angemeldet sind – dies verwendet Apple CloudKit, nicht unsere Server. Das Internet wird auch für App-Store-Updates oder Feedback-E-Mails genutzt. 

### Wie funktioniert die Studienstatistik? 

Öffnen Sie die Registerkarte **Statistiken**. Filtern Sie nach Alle / Pomodoro / Lerntimer und nach Heute / Woche / Monat / Jahr / Alle Zeiten / **Benutzerdefinierter Datumsbereich**. Das Dashboard zeigt **die heutige Übersicht**, **Zielfortschritt**, einen Wochenvergleich, eine **monatliche Heatmap**, **Erfolge**, Wochentags-/Tageszeitdiagramme und **Aufschlüsselung nach verknüpften Aufgaben**. Tippen Sie auf das **Zahnradsymbol** für Ziele, optionale **iCloud-Synchronisierung**, Zählregeln, **CSV-Export/Import** und Datenaufbewahrung. Statistiken werden **niemals auf unsere Server hochgeladen** (optional nutzt iCloud Apple CloudKit unter Ihrer Apple-ID). 

### Kann ich Studienstatistiken exportieren oder importieren?

Ja. **Registerkarte „Statistik“ → Zahnrad → Exportieren** gibt eine CSV-Datei über das Systemfreigabeblatt frei. **Importieren** akzeptiert das gleiche Format (`kind,started_at,ended_at,duration_seconds,outcome` plus optional `task_id,task_title,cloud_id`) – wählen Sie **zusammenführen** (Duplikate überspringen) oder **alle ersetzen**. Nützlich für Backups oder manuelle Migration. Aktivieren Sie für die automatische geräteübergreifende Synchronisierung stattdessen **Studienstatistiken mit iCloud synchronisieren**. 

### Kann ich meine Statistiken als Bild teilen? 

Ja. iPomodoro kann **Marken-Snapshot-Karten** (Fokusmetriken + App Store-QR-Code) für das **Statistik-Dashboard** (Symbolleistenfreigabe), **Zeitraumberichte**, **Jahresrückblick**-Zusammenfassungen und **Erfolge** (vollständige Liste oder einzelnes Abzeichen) rendern. Statistik-Freigabekarten verwenden die Farben Ihres **Registerkartenthemas „Statistik“**. Sie können eine **App-Werbekarte** auch über Einstellungen → App teilen teilen. 

### Kann ich Studienstatistiken mit iCloud synchronisieren? 

Ja – **Registerkarte „Statistik“ → Zahnrad → Studienstatistiken mit iCloud synchronisieren**. Dies ist **getrennt** von der Aufgabe der iCloud-Synchronisierung. Sitzungen werden nach `cloudId` auf Ihren Apple-ID-Geräten über den CloudKit-Eintragstyp `StudySession` zusammengeführt. **Tageszieleinstellungen** (`StatsGoals`) und **Erfolgs-Freischalt-/Feierstatus** (`StatsAchievements`) werden bei Aktivierung unter demselben Schalter synchronisiert.

### Wie funktionieren tägliche Fokusziele? 

**Statistiken → Ausrüstung → Ziele**: Legen Sie die tägliche Pomodoro-Anzahl, die täglichen Fokusminuten und die wöchentlichen Fokusminuten fest. Der Fortschritt wird im Statistik-Dashboard und im Widget „Heutige Statistiken“ angezeigt, sofern aktiviert. 

### Wie verknüpfe ich eine Countdown-Aufgabe mit einer Fokussitzung? 

Tippen Sie im Pomodoro- oder Study-Timer-Bildschirm auf **Aufgabe verknüpfen** und wählen Sie eine Aufgabe aus. Oder drücken Sie in **Aufgaben** lange auf eine Aufgabe → **Fokus mit Pomodoro** oder **Fokus mit Lerntimer**. Abgeschlossene Sitzungen speichern den Aufgabentitel für die **Aufschlüsselung nach Aufgabe** in der Statistik. 

### Wie kann ich Aufgaben anpinnen oder neu anordnen? 

Wischen Sie auf der Registerkarte **Aufgaben** über eine Zeile zu **Anheften** oder verwenden Sie das Sortiermenü in der Navigationsleiste. Wechseln Sie in den Neuordnungsmodus, um Aufgaben zu **ziehen** – die Sortierung wechselt automatisch zur benutzerdefinierten Reihenfolge. Angeheftete Aufgaben werden oben in einem eigenen Abschnitt angezeigt. 

### Wie funktioniert die iCloud-Aufgabensynchronisierung? 

Registerkarte „Aufgaben“ → Zahnrad → Umschalten zwischen **Aufgaben mit iCloud synchronisieren**. Aufgaben werden nach dem Zeitpunkt der letzten Änderung auf Ihren Apple-ID-Geräten zusammengeführt. Pomodoro / Lerntimer bleiben vor Ort. **Studienstatistiken** können optional separat synchronisiert werden (Statistiken → Zahnrad). Sie müssen in den iOS-Einstellungen bei iCloud angemeldet sein. Die Synchronisierung wird auch ausgeführt, wenn Sie zur App zurückkehren.

### Was beinhaltet das Bild zum Teilen des Statistik-Dashboards?

Tippen Sie auf **Teilen** in der Symbolleiste des Statistik-Tabs. Die lange Karte spiegelt Ihre **aktuellen Filter für Umfang und Zeitraum** wider – der heutige Held, Zielerreichung, Heatmap, Wochentags-/Stunden-Diagramme, Aufgabenaufteilung, Trendbalken und aktuelle Sitzungen – sowie Branding und einen App Store QR-Code. Die Farben entsprechen Ihrem **Seiten-Theme des Statistik-Tabs**.

### Kann ich das Theme des Statistik-Tabs anpassen?

Ja. **Statistik-Tab → Zahnrad → Theme** — die gleichen Titelbalken- und Hintergrundverlaufs-Steuerungen wie bei Pomodoro, Study Timer und Aufgaben. Standard ist Fokus-Rot (`#E53935` / `#EF9A9A`). Die Tönung des Statistik-Tabs, die Navigationsleiste und **Statistik-Share-Karten** folgen alle diesen Seiten-Theme-Farben.

### Wie funktionieren Erfolge?

Neun lokale Abzeichen werden freigeschaltet, wenn Sie Meilensteine ​​erreichen – erster Pomodoro, Streaks, gesamte Pomodoros, Fokusstunden, tägliche Zielerreichung und mehr. Wenn Sie ein neues Abzeichen freischalten, wird auf der Registerkarte „Statistiken“ eine **Vollbild-Feier** angezeigt (tippen Sie zum Schließen auf **Weiter**). Öffnen Sie **Statistik → Ausrüstung → Erfolge**, um das Raster zu durchsuchen. **Tippen Sie auf ein Abzeichen**, um ein Detailblatt anzuzeigen. Teilen Sie die **vollständige Liste** über die Erfolgssymbolleiste oder ein **einzelnes Abzeichen** über den Detailbildschirm. Abzeichen werden auf dem Gerät gespeichert; Wenn die iCloud-Synchronisierung aktiviert ist, werden der Entsperr- und Speicherstatus über CloudKit auf Ihren Geräten zusammengeführt – nicht auf unsere Server hochgeladen. 

### Wie durchsuche ich vergangene Monate auf der Fokus-Heatmap? 

Verwenden Sie im Statistik-Dashboard die Pfeile **Vorheriger/Nächster Monat** auf der Heatmap-Karte, tippen Sie auf den **Monatstitel**, um ein Blatt **Jahr + Monatsauswahl** zu öffnen, oder tippen Sie auf **Diesen Monat**, um zum aktuellen Monat zurückzukehren. 

### Warum sehen zukünftige Daten auf der Heatmap anders aus? 

Tage nach dem heutigen Tag im aktuellen Monat werden als **Platzhalter mit gestricheltem Umriss** und einer helleren Füllung angezeigt – sie werden nicht als Fokustage gezählt. Vergangene Tage und heute verwenden die Farben normaler Intensität. 

### Wie füge ich das Widget „Heutige Statistiken“ hinzu?

Drücken Sie lange auf den Startbildschirm → **+** → suchen Sie nach **iPomodoro** → fügen Sie **Heutige Statistiken** hinzu (Klein, **Mittel, Groß** oder Sperrbildschirm rechteckig/inline). Es zeigt den heutigen Fokus, den Pomodoro und den **wöchentlichen** Zielfortschritt sowie die Serie. 

### Wie füge ich das Aufgaben-Widget hinzu? 

Drücken Sie lange auf den Startbildschirm → **+** → **iPomodoro** suchen → **Countdown-Aufgaben** hinzufügen (Klein / Mittel / Groß). Es zeigt anstehende angeheftete Aufgaben und die verbleibenden Tage an. Öffnen Sie die App, nachdem Sie Aufgaben bearbeitet haben, um eine schnellere Aktualisierung zu gewährleisten. 

### Kann ich das Motivations-Widget-Zitat aktualisieren? 

Tippen Sie unter **iOS 17+** auf die Schaltfläche **Aktualisieren** im Widget „Tägliche Motivation“, um sofort ein anderes Zitat auszuwählen, ohne die App zu öffnen. 

### Warum funktionieren Benachrichtigungen nicht? 

Überprüfen Sie **Registerkarte „Einstellungen“ → Benachrichtigungen** auf Ihren aktuellen iOS-Berechtigungsstatus. Timer- und Aufgabenerinnerungen erfordern Benachrichtigungszugriff. Öffnen Sie die Systemeinstellungen, wenn die Berechtigung verweigert wurde. 

### Wie kann ich die Arbeits- und Pausendauer anpassen? 

Tippen Sie auf das **Zahnradsymbol** auf der Registerkarte „Pomodoro“ → passen Sie die Stepperreihen an oder **tippen Sie auf die großen Timer-Ziffern** auf dem Hauptbildschirm, um eine Dauerauswahl zu öffnen. Ein langes Pausenintervall (alle N Pomodoros) ist ebenfalls konfigurierbar. 

### Was ist der Abschluss der Phase bestätigen?

**Pomodoro-Tab → Zahnrad → Phase als abgeschlossen bestätigen**. Wenn **ein**, zeigt iPomodoro nach jedem Arbeits- oder Pausenabschnitt einen Dialog, bevor die nächste Phase beginnt. Wenn **aus** (Standard), startet die nächste Phase automatisch nach dem Abschlussalarm — klassischer, freihändiger Pomodoro-Ablauf.

### Wie funktionieren Live-Aktivität und Dynamic Island?

Aktivieren Sie **Live-Aktivität** separat in den Pomodoro- und Study-Timer-Einstellungen (Zahnradsymbol). Jeder Modus erhält seinen **eigenen** Sperrbildschirm- und Dynamic-Island-Countdown — sie überschreiben sich niemals gegenseitig. Während einer Sitzung sehen Sie einen Live-Countdown; wenn sie abgeschlossen ist, erscheint eine kurze Feieranzeige für 10 Sekunden. Wenn iOS die App beendet, während Ihr Timer noch auf dem Sperrbildschirm angezeigt wird, stellt das erneute Öffnen von iPomodoro die Sitzung **wieder her** und springt zum aktiven Tab — **es sei denn**, Sie haben die App über eine **Home-Bildschirm-Schnellaktion** gestartet, die Priorität hat.

### Wie füge ich Widgets hinzu?

Langes Drücken des Startbildschirms → **+** → Suche nach **iPomodoro** (oder 爱番茄 / 愛番茄). Wähle **iPomodoro · Pomodoro** oder **iPomodoro · Study Timer** für Timer-Countdowns (sie sind separate Widgets), **Today's Stats** für den täglichen Fortschritt beim Fokus, **Countdown Tasks** für Fristen oder **Daily Motivational Quote** für das tägliche Zitat. Für Schritt-für-Schritt-Hilfe öffne **Einstellungen → Widgets → Anleitung**.

### Warum aktualisiert sich mein Timer-Widget nicht?

Pomodoro und Study Timer sind **separate Widgets**. Starte oder pausiere eine Sitzung im **entsprechenden Tab** und stelle sicher, dass du das richtige Widget hinzugefügt hast. iOS kann die Aktualisierung verzögern, um Akku zu sparen — öffne die App einmal, um schneller zu synchronisieren.

### Wo ist das alte Timer-Widget?

Timer sind jetzt **iPomodoro · Pomodoro** und **iPomodoro · Study Timer**. Entferne alle alten Timer-Widgets und füge die neuen aus der Widget-Galerie hinzu.

### Wie funktioniert das tägliche Motivationszitat?

Mit `(year × 400 + dayOfYear) % total` wird jeden Tag ein Angebot deterministisch ausgewählt. Filtern Sie die Zitatsprache unter **Einstellungen → Einstellungen für motivierende Zitate → Sprachen für motivierende Zitate** (Alle / Vereinfacht / Traditionell / Englisch). Das gleiche Zitat erscheint bis Mitternacht im Motivations-Widget und im Live-Aktivitätshinweis. Durchsuchen Sie zufällige Zitate unter **Einstellungen → Einstellungen für motivierende Zitate → Anthologie mit motivierenden Zitaten** (Vollbild, einzeln). 

### Können Widget-Hintergründe meinem Thema folgen? 

Ja. **Einstellungen → Widgets → Widget-Hintergrund folgt Thema** spiegelt Ihren globalen Akzentverlauf auf Start- und Sperrbildschirm-Widgets wider. Schalten Sie es aus, um einen sauberen weißen (hellen) oder systemdunklen Hintergrund zu erhalten, während die Akzentfarben auf den Titeln beibehalten werden. 

### Wie funktionieren Erinnerungen an fällige Aufgaben? 

Aktivieren Sie beim Erstellen oder Bearbeiten einer Aufgabe die **Erinnerung an Fälligkeitstermine** und legen Sie ein zukünftiges Zieldatum/eine zukünftige Zielzeit fest. Genau in diesem Moment wird eine lokale Benachrichtigung ausgelöst. Verwalten Sie ausstehende Erinnerungen unter **Registerkarte „Aufgaben“ → „Zahnrad“ → „Erinnerungen an fällige Aufgaben“ – tippen Sie unten auf dem Bearbeitungsblatt auf eine Zeile, um die Aufgabe zu bearbeiten oder zu **löschen**. Auch das Wischen zum Löschen in der Aufgabenliste funktioniert weiterhin. 

### Wie lösche ich eine Aufgabe während der Bearbeitung?

Öffnen Sie eine Aufgabe aus der Liste oder aus **Erinnerungen an fällige Aufgaben**, scrollen Sie dann zum Ende des Bearbeitungsblatts und tippen Sie auf **Löschen**. Bestätigen Sie in der Benachrichtigung. Bei neuen Aufgaben (Flow erstellen) wird keine Schaltfläche zum Löschen angezeigt. 

### Warum kann ich eine Erinnerung für ein vergangenes Datum nicht aktivieren? 

Wenn das Zieldatum/Uhrzeit bereits verstrichen ist, wird der Erinnerungsschalter ausgeblendet und alle vorhandenen Erinnerungen werden automatisch deaktiviert – es gibt nichts Sinnvolles mehr zu planen. 

### Kann ich eine andere Sprache als mein System verwenden? 

Ja. Gehen Sie zur **Registerkarte „Einstellungen“ → „Sprache“** und wählen Sie Englisch, vereinfachtes Chinesisch oder traditionelles Chinesisch aus. Der App-Name auf Ihrem Startbildschirm richtet sich nach der Systemsprache. Die In-App-Benutzeroberfläche folgt Ihrer In-App-Auswahl. 

### Sammelt die App meine Daten? 

Keine Analyse, kein Tracking. Timer und Studienstatistiken bleiben standardmäßig auf Ihrem Gerät. Aufgaben und Lernsitzungen werden nur dann mit **Ihrer iCloud** synchronisiert, wenn Sie die separaten Schalter aktivieren. Wir empfangen Ihre Aufgaben- oder Timerdaten nicht auf unseren Servern. Ausführliche Informationen finden Sie in unserer [Datenschutzerklärung](../privacy). 

### Wird macOS unterstützt? 

macOS-Unterstützung ist geplant. Das Xcode-Projekt enthält bereits die macOS SDK-Konfiguration; Bleiben Sie auf dem Laufenden für Updates im App Store. 

### Brauchen Sie noch Hilfe?

Kontaktieren Sie uns unter [AppleOSer@gmail.com](mailto:AppleOSer@gmail.com). Wir antworten normaler weise innerhalb von 48 Stunden.

&lt;/Abschnitt&gt;
