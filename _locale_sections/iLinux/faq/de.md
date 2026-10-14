### Benötigt iLinux ein Konto oder eine Internetverbindung?

Nein. iLinux funktioniert für Befehlsbibliotheken vollständig offline. Alle Befehlsdaten (JSON-Zusammenfassungen und Markdown-Dokumentation) sind in der App gebündelt. Es ist keine Anmeldung erforderlich, um die Dokumentation zu durchsuchen, zu lesen oder an Tests teilzunehmen. Die optionale **iCloud-Synchronisierung** verwendet Ihre Apple-ID, um Favoriten und Fortschritte geräteübergreifend abzugleichen – es werden keine Befehlsinhalte hochgeladen.

### Unterstützt iLinux Mac?

Ja. iLinux ist eine **native macOS-App** (macOS **13.0+**, nicht Mac Catalyst) mit einem **Seitenleisten-Desktop-Layout**, einem skalierbaren Fenster und erweiterten Tastaturkürzeln (**⌘,**, **⌘[**, **Esc**, **⌘←/→**, Quiztasten **1–4** / **⌘R** / **Return**). Alle Kernfunktionen – drei Shell-Bibliotheken, Äquivalente, Quiz, Deep Links und Themes – funktionieren auf dem Mac.

**Nicht auf Mac:** Startbildschirm-Widgets, Startbildschirm-Schnellaktionen und alternative App-Symbole sind **nur für iPhone/iPad**. Widgets unter iOS konfigurieren; Mac zeigt einen In-App-Hinweis an.

### Wie funktioniert die iCloud-Synchronisierung?

Wenn Sie mit derselben Apple-ID bei **iCloud** angemeldet sind, aktivieren Sie **iCloud Sync** unter **Einstellungen → Lernstatistiken**. iLinux synchronisiert **Favoriten**, **Quizfortschritt**, **Thema** und **Anzeigeeinstellungen** (Sprache, Shell-Plattform, Favoritenbereich, Liste/Raster) über **iPhone, iPad und Mac** über iCloud Key-Value Storage. Konflikte werden automatisch zusammengeführt (z. B. Favoritenzusammenführung). Sie können die **Synchronisierung auf einem Gerät deaktivieren**, ohne dass dies Auswirkungen auf andere hat. Befehlsbibliotheken bleiben vollständig offline; Nur Ihr persönlicher Fortschritt wird synchronisiert.

### Führt iLinux Befehle auf einem echten Linux-Terminal aus?

Nein. iLinux ist nur ein **Referenz- und Lerntool**. Es stellt keine Shell, keinen SSH-Client oder keine Remote-Ausführungsumgebung bereit. Befehle werden zum Lernen dokumentiert – Sie üben sie auf Ihrem eigenen Linux-Rechner, Windows-PC, Server oder Cloud-Instanz.

### Welche Shell-Plattformen unterstützt iLinux?

iLinux liefert drei Offline-Befehlsbibliotheken pro Inhaltssprache:

- **Linux** – 1050 Befehle in 14 Kategorien
- **Windows CMD / Batch** – 300 Befehle in 10 Kategorien
- **PowerShell** – 300 Befehle in 10 Kategorien

**insgesamt über 1650 Befehle** pro Sprache (Englisch, vereinfachtes Chinesisch, traditionelles Chinesisch). Wechseln Sie zwischen den Bibliotheken im Shell-Menü der Symbolleiste auf **Befehle**, **Kategorien** oder **Tägliches Quiz**.

### Wie wechsle ich zwischen Linux, CMD und PowerShell?

Tippen Sie in der Symbolleiste auf der Registerkarte „Befehle“, „Kategorien“ oder „Tägliches Quiz“ auf das Menü **Shell-Plattform** (Terminalsymbol). Ihre Auswahl bleibt bestehen und umfasst die Suche, Kategorien, Quizfragen und Lernstatistiken für diese Plattform.

Unter **Einstellungen → Home-Schnellzugriff** können Sie auch eine Standard-Shell-Plattform, einen **Favoritenbereich** (alle Plattformen vs. nur aktuelle Plattform) und die **Widget-Befehlsbibliothek** für Daily Command- und Category Spotlight-Widgets festlegen.

### Was sind plattformübergreifende äquivalente Befehle?

**100+ equivalent groups** link commands that accomplish the same task across Linux, CMD and PowerShell — for example `ls`, `dir` and `Get-ChildItem`. On a command detail page, the **Equivalents** bar shows related entries; tap one to jump to that platform's documentation instantly.

### Wie viele Befehle sind enthalten?

Jede Inhaltssprache umfasst **1650+** Befehle in drei Shell-Bibliotheken:

| Plattform | Befehle | Kategorien |
|----------|----------|------------|
| Linux | 1050 | 14 |
| CMD / Stapel | 300 | 10 |
| PowerShell | 300 | 10 |

Die gesamte Dokumentation ist offline in Englisch, vereinfachtem Chinesisch und traditionellem Chinesisch verfügbar.

### Wie suche ich nach einem Befehl?

Tippen Sie auf der Registerkarte „Befehle“ auf das Lupensymbol oder drücken Sie **⌘F** auf einer Hardwaretastatur. Geben Sie einen Befehlsnamen, ein Schlüsselwort oder einen Teil einer Beschreibung ein. Die Ergebnisse werden während der Eingabe in Echtzeit aktualisiert.

### Wie wechsle ich zwischen Listen- und Rasteransicht?

Öffnen Sie auf der Registerkarte **Befehle** oder **Kategorien** das Filtermenü der Symbolleiste (Trichtersymbol). Wählen Sie unter **Ansichtsmodus** die Option **Liste** oder **Raster**. Verwenden Sie im Rastermodus die Tasten **+ / −**, um Spalten pro Zeile festzulegen (**1–6 auf dem iPhone**, **1–8 auf iPad und Mac**). Sie können die Standardeinstellung auch unter **Einstellungen → Anzeige** ändern.

### Wie verfolge ich meinen Lernfortschritt?

Open a command's detail page and set its status to **Unlearned**, **Learned** or **Mastered**. In list view, swipe a row for quick status and favourite actions. In grid view, use the star button to favourite and the context menu for status. Filter to **Unlearned** from the toolbar menu to focus on commands you haven't studied yet.

### Welche Sprachen sind verfügbar?

iLinux unterstützt drei Sprachen sowohl für die App-Oberfläche als auch für die Befehlsdokumentation:

- **Englisch**
- **Vereinfachtes Chinesisch (简体中文)**
- **Traditionelles Chinesisch (繁體中文)**

Sie können auch **System** auswählen, um dem Gebietsschema Ihres Geräts zu folgen. Ändern Sie die Sprache unter **Einstellungen → Sprache**. Die gesamte App – einschließlich Widgets – wird sofort aktualisiert.

### Wie funktioniert das tägliche Quiz?

Jeden Tag wird ein neuer Satz von Quizfragen mithilfe eines datumsbasierten Startwerts generiert, der **auf die aktive Shell-Plattform beschränkt ist** (Linux, CMD oder PowerShell). Jeder, der iLinux am selben Tag nutzt, erhält das gleiche Basis-Quizset für diese Plattform. Es erscheinen zwei Fragetypen:

- **Übereinstimmungszusammenfassung** – Sie sehen eine kurze Beschreibung und müssen den richtigen Befehlsnamen auswählen.
- **Match Option Meaning** — you see a flag's description (e.g. `-r: recursive`) and must identify which command it belongs to.

Tap the **refresh button** (circular arrow) in the toolbar to get a different randomised set at any time. **Perfect streak** days (consecutive days with a perfect score) are tracked per platform and shown in the quiz screen and Quiz Glance widget. Generic help flags like `-h` and `--version` are excluded to keep questions unambiguous.

### Meine falschen Antworten werden nicht gespeichert. Was soll ich tun?

Falsche Antworten werden automatisch gespeichert, nachdem Sie eine Quizsitzung abgeschlossen haben. Stellen Sie sicher, dass Sie die gesamte Quizrunde abgeschlossen haben (beantworten Sie alle Fragen und gelangen Sie zum Ergebnisbildschirm). Teilweise abgeschlossene Sitzungen werden nicht gespeichert.

Sie können alle gespeicherten falschen Antworten unter **Einstellungen → Falsche Antworten** überprüfen.

### Wie füge ich einen Befehl zu den Favoriten hinzu?

Öffnen Sie die Detailseite eines beliebigen Befehls und tippen Sie auf das **Sternsymbol** in der oberen rechten Ecke. Tippen Sie in der **Rasteransicht** direkt auf den Stern in der Befehlszelle. Greifen Sie auf alle Favoriten über **Einstellungen → Favoriten** oder den Schnellfilter **Favoriten** zu.

### Wie richte ich Startbildschirm-Widgets ein?

1. Long-press an empty area of your Home Screen and tap the **+** button in the top corner.
2. Suchen Sie in der Widget-Galerie nach **iLinux**.
3. Wählen Sie einen Widget-Stil und tippen Sie auf **Widget hinzufügen**.

Eine schrittweise **Widget-Anleitung** ist auch unter **Einstellungen → Widget-Anleitung** verfügbar. Damit die Widget-Hintergründe dem Farbverlauf Ihres App-Designs folgen, aktivieren Sie die Option unter **Einstellungen → Widgets**.

**Widget-Befehlsbibliothek:** Wählen Sie unter **Einstellungen → Widgets** aus, welche Shell-Bibliothek (Linux / CMD / PowerShell) die Daily Command- und Category Spotlight-Widgets speist. Dies ist unabhängig vom In-App-Shell-Schalter – nützlich, wenn Sie möchten, dass Widgets Windows-Befehle anzeigen, während Sie in der App Linux durchsuchen.

### Das Widget „Täglicher Befehl“ zeigt jeden Tag denselben Befehl an. Wie ändere ich es?

Tippen Sie auf die **kreisförmige Pfeilschaltfläche (Shuffle)** in der oberen rechten Ecke des Daily Command-Widgets, um sofort einen anderen Befehl zu laden. Für diese Funktion ist **iOS 17 oder höher** erforderlich.

Unter iOS 16 zeigt das Widget „Täglicher Befehl“ einen festen Befehl für jeden Tag an und enthält keine Zufallsschaltfläche.

### Wie konfiguriere ich Schnellaktionen auf dem Startbildschirm?

Drücken Sie lange auf das iLinux-App-Symbol, um bis zu **4** Schnellaktionen anzuzeigen. Wählen Sie aus, welche Aktionen unter **Einstellungen → Startbildschirm-Verknüpfungen** angezeigt werden. Es stehen sieben Optionen zur Verfügung: **Suche**, **Tägliches Quiz**, **Favoriten**, **Buch mit falschen Antworten**, **Kategorien**, **Feedback senden** und **App bewerten**. Sie können auf demselben Bildschirm die Reihenfolge ändern und auf die Standardeinstellungen zurücksetzen.

### Wie verwende ich iLinux mit der Shortcuts-App?

iLinux supports the `ilinux://` URL scheme. Use an **Open URLs** action in the Shortcuts app. Examples:

- `ilinux://command?name=grep` – öffnet den Linux-Befehl `grep` (`cmd=` funktioniert auch)
- `ilinux://command?cmd=dir&platform=cmd` — opens CMD command `dir`
- `ilinux://command?cmd=Get-ChildItem&platform=powershell` — opens PowerShell command
- `ilinux://quiz` — opens the Daily Quiz tab
- `ilinux://favorites` — opens your Favourites list
- `ilinux://wrong` or `ilinux://mistakes` — opens the Wrong Answer Book

**Platform parameter:** `platform=linux` (default), `cmd` (aliases: `batch`, `bat`), or `powershell` (aliases: `ps`, `pwsh`). Omit for Linux commands.

Hinweis: **Suche** und **Kategorien** sind als Schnellaktionen auf dem Startbildschirm verfügbar, aber nicht als universelle Deep-Link-Hosts registriert. Sehen Sie sich die vollständige [URL-Schema-Referenz](../url-scheme) an.

### Wie teile ich einen Befehl?

Tippen Sie auf einer beliebigen Befehlsdetailseite in der Symbolleiste auf **Teilen**. Sie können den Befehl als **Markdown-Datei** exportieren oder eine **im PNG-Format gestaltete Freigabekarte** (mit App Store-QR-Code) erstellen, um sie über das Freigabeblatt des Systems zu senden. Beim Speichern von Bildern in Fotos kann der Zugriff auf die Fotobibliothek erforderlich sein.

### Wie ändere ich die Designfarbe?

Gehen Sie zu **Einstellungen → Thema**. Scrollen Sie durch 15 integrierte Farbvoreinstellungen oder tippen Sie auf die Zeile **Benutzerdefinierte Farbe**, um mit der Systemfarbauswahl eine beliebige Farbe auszuwählen. Die Akzentfarbe, die Farbverläufe und der Widget-Spiegel werden alle sofort aktualisiert.

### Kann ich das App-Symbol ändern?

Ja. Gehen Sie zu **Einstellungen → App-Symbol**, um aus **6 Symbolen** auszuwählen (Standard plus 5 Alternativen). Die Einstellung wird sofort übernommen, ohne dass die App neu gestartet werden muss.

### Die Widget-Farbe passt nicht zu meinem Thema. Wie kann ich das Problem beheben?

Widgets synchronisieren ihre Designfarbe über eine App-Gruppe, die von der Haupt-App und der Widget-Erweiterung gemeinsam genutzt wird. Wenn das Widget veraltet aussieht:

1. Öffnen Sie iLinux einmal – dies erzwingt eine Aktualisierung der App-Gruppendaten.
2. Wenn das Widget immer noch nicht aktualisiert wird, drücken Sie lange auf das Widget und tippen Sie auf **Widget bearbeiten** (oder entfernen Sie es und fügen Sie es erneut hinzu), um ein Neuladen der Zeitleiste auszulösen.

Stellen Sie sicher, dass die **iLinux Widget**-Erweiterung und die Haupt-App beide auf dem neuesten Stand sind (gleiche Version).

### Unterstützt iLinux das iPad?

Ja. iLinux läuft nativ auf dem iPad mit adaptiven Layouts. Der Rastermodus unterstützt bis zu **8 Spalten**. Widgets, alternative Symbole, Startbildschirm-Verknüpfungen und Haptik werden auf dem iPad vollständig unterstützt.

### Wie ändere ich die Sprache auf dem Mac?

Die In-App-**Sprachauswahl** befindet sich unter **Einstellungen → Sprache** auf **iPhone und iPad**. Auf **Mac** erfolgt die Spracheinstellung normalerweise über **iCloud-Synchronisierung** von einem anderen Gerät oder folgt beim ersten Start Ihren gespeicherten Einstellungen/Systemgebietsschemas. Aktivieren Sie die iCloud-Synchronisierung, um die Sprache auf allen Geräten anzugleichen.

### Brauchen Sie noch Hilfe?

Kontaktieren Sie uns unter [AppleOSer@gmail.com](mailto:AppleOSer@gmail.com) oder nutzen Sie die In-App-Option **Einstellungen → Feedback senden**. Wir antworten in der Regel innerhalb von 48 Stunden.
