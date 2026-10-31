iWool ist ein datenschutzorientierter lokaler Tracker, der zum Erfassen von Geschäften, Verfolgen von Aktivitäten und Zählen von Einnahmen auf **iPhone und iPad** entwickelt wurde. **`iwool://`-Deep-Links** öffnen Startseite, Kalender, Statistiken, Einstellungen, In-App-Aktionen (neue Aktivität, schneller Countdown, Scanner, Erinnerungen) oder eine bestimmte Aktivität – über Widgets, Verknüpfungen oder Schnellaktionen auf dem Startbildschirm. **Keine Anmeldung, kein Upload – Ihre Daten bleiben auf dem Gerät.**

Alle unterstützten Pfade und Aliase finden Sie in der vollständigen [**`iwool://` URL-Schema-Referenz**](url-scheme).

## Erste Schritte

1. Tap **+** on the home screen to create your first activity.
2. Geben Sie den Titel, die Plattform sowie die Start- und Endzeit ein. Fügen Sie bei Bedarf Erinnerungen hinzu.
3. Tippen Sie auf **Speichern**. Die Aktivität erscheint in Ihrer Liste, gruppiert nach Status.
4. Wenn sich der Deal auszahlt, tippen Sie auf die Detailseite und dann auf **Einnahmen verzeichnen**.
5. Überprüfen Sie jederzeit **Statistiken**, um Ihre Gesamtzahlen, Trends und das Plattform-Ranking anzuzeigen.
6. Fügen Sie ein Startbildschirm- oder Sperrbildschirm-Widget hinzu, damit Sie die App nie öffnen müssen, um auf dem Laufenden zu bleiben.

## Funktionen

### Startbildschirm

- **Sieben Statusübersichtskarten** – Aktiv, Demnächst, Alle, Abgelaufen, Abgeschlossen, Abgebrochen, Angehalten. Tippen Sie auf eine beliebige Karte, um sofort zu filtern. Tippen Sie erneut, um zu „Heute“ zurückzukehren.
- **Pausieren oder kündigen Sie mit einem Gültigkeitsdatum** – verstecken Sie sich vor „Heute“/Kalender und stoppen Sie Erinnerungen, während Sie den Verdienstverlauf behalten.
- **Aktivitätsfreigabeexport** – Exportieren Sie ein Freigabepaket, das Freunde importieren können, um es mitzuverfolgen (getrennt von der vollständigen Sicherung).
- **Volltextsuche** – Suche nach Titel, Notizen, Plattform, Anforderungen und Regeln.
- **Aktionen durch langes Drücken** – als abgeschlossen markieren, pausieren/fortsetzen, abbrechen/wiederherstellen, archivieren, als neu duplizieren oder löschen.
- Bei wiederkehrenden Aktivitäten wird immer das **heutige Ereignis** angezeigt, sodass Status und Zeit mit Ihrem tatsächlichen Zeitplan übereinstimmen.

### Kalender

- Wechseln Sie zwischen **Monatsansicht** und **Wochenzeitleiste** – Ihre Präferenz wird gespeichert.
- Tippen Sie auf ein beliebiges Datum, um die Aktivitäten dieses Tages anzuzeigen. Punkte und Farben des linken Balkens folgen der Plattformfarbe.
- Drücken Sie lange auf eine beliebige Listenzeile, um die gleichen Schnellaktionen wie auf dem Startbildschirm zu erhalten.
- Zum Aktualisieren jederzeit ziehen.

### Aktivitätsdetails

- **Startet den Countdown** – zeigt die Zeit bis zum aktuellen oder nächsten Ereignis an; Hervorhebungen in Orange, wenn weniger als 24 Stunden vergangen sind.
- **Nächstes Ereignisdatum** wird für wiederkehrende Aktivitäten angezeigt; „Kein nächstes Vorkommen“, wenn die Serie endet.
- Aktivitäts-URL, Anforderungen, Regeln und Hinweise – alle Render-Links. **Einmaliges Tippen** öffnet sich in Safari (http/https) oder der zugehörigen App; Durch **langes Drücken** wird das native iOS-Linkmenü aufgerufen, einschließlich „In [App] öffnen“, „In Safari öffnen“, „Link kopieren“ und „Teilen“.

### Rekordgewinn

- Halbblattformular mit Betrag, optionaler Notiz und **Stichtag**.
- Mehrere Einträge pro Aktivität, jeweils unabhängig voneinander bearbeitbar oder löschbar.
- Einnahmen werden nur dann in der Statistik angezeigt, wenn sie hier erfasst werden. Die geschätzten Einnahmen dienen nur der Anzeige.

### Statistiken

- Gesamtwerte für heute, diese Woche, diesen Monat und dieses Jahr.
- **Monatliches Trenddiagramm** – tippen Sie auf einen beliebigen Balken (wenn der Betrag > 0), um alle Einnahmeneinträge in diesem Zeitraum anzuzeigen.
- **Plattform-Ranking** – unabhängige Zeitbereichsauswahl (Jahr/Monat/Woche); Tippen Sie auf eine Plattformzeile, um die Details pro Eingang anzuzeigen.
- **Aktivitätsübersicht** – Tippen Sie auf eine Statuszeile oder die Gesamtzeile, um die entsprechende Aktivitätsliste anzuzeigen.
- Die Einnahmenrichtlinie für wiederkehrende Aktivitäten (streng oder mild) kann in den Einstellungen konfiguriert werden.

### Erinnerungen

- Mehrere Erinnerungen pro Aktivität – zu Beginn, vor Beginn, vor Ablauf der Frist oder zu einer täglich festgelegten Zeit.
- Lokale Systembenachrichtigungen. Erinnerungspläne werden bei jedem Öffnen der App aufgeräumt.
- Abgebrochene Aktivitäten klingeln automatisch nicht mehr.
- In den Listenzeilen „Startseite“ und „Kalender“ wird ein **kleines Erinnerungssymbol** angezeigt, sodass Sie auf einen Blick sehen können, was geplant ist.

### Teilen Sie Bildkarten

Teilen Sie eine **Aktivität** oder Ihr **Statistik-Dashboard** als **gebrandete PNG-Bildkarte** über das Share Sheet des Systems – Hintergrund mit Farbverlauf, QR-Code aus dem App Store und optionales Wasserzeichen. Schalten Sie in den Einstellungen um, ob Einnahmen auf geteilten Karten angezeigt werden (**standardmäßig deaktiviert**). Bilder werden auf dem Gerät gerendert; Es wird nichts hochgeladen. „In Fotos speichern“ kann den Zugriff auf die Fotobibliothek anfordern.

### Schnellaktionen auf dem Startbildschirm

Drücken Sie lange auf das iWool-Symbol unter iOS, um bis zu **4** Verknüpfungen zu starten. Wählen Sie aus **9** Voreinstellungen in **Einstellungen → Extras → Startbildschirm-Verknüpfungen**:

Startseite · Kalender · Statistiken · **Schneller Countdown** · Neue Aktivität · Geplante Erinnerungen · Scanner · App bewerten · Feedback

Default: **Home, Calendar, Statistics, Quick Countdown**. Each action uses an `iwool://` URL (same router as widgets and Shortcuts).

### Dynamische Insel- und Live-Aktivitäten

Zwei Live-Aktivitätstypen auf unterstützten iPhone-Modellen:

**1. Ereignis-Countdown** (iOS 16.1+)

- An Wollaktivitäten gebunden – aktivieren Sie diese Funktion unter **Einstellungen → Benachrichtigungen → Live-Aktivität**.
- Passen Sie die **Vorlaufzeit** an (1–480 Minuten vor dem Start). Mehrere Aktivitäten im Fenster können jeweils eine Insel anzeigen oder rotieren.
- Drücken Sie lange auf eine geeignete Aktivität auf der Startseite oder im Kalender → **Zu Dynamic Island hinzufügen**.

**2. Schneller Countdown** (iOS 16.2+)

- **Eigenständiger** Insel-/Sperrbildschirm-Countdown – **nicht gespeichert** in Ihrer Aktivitätsdatenbank.
- Create from **Settings → Island Reminder** or `iwool://island` / Home Screen Quick Action.
- Dauer **1 Sekunde bis 8 Stunden** – voreingestellte Chips (30 s, 1–480 min) oder wählen Sie eine Frist; optionale Anzeige von Titel, Notiz, Akzentfarbe und Sekunden.
- Endet automatisch, wenn die Zeit abgelaufen ist; Ideal für Flash-Verkäufe, Anmeldefenster oder Ad-hoc-Timer.

### Widgets für den Startbildschirm und den Sperrbildschirm

**Insgesamt 12 Widget-Familien** (8 Startbildschirm- und 4 Sperrbildschirm-Zubehörstile):

| Widget | Beschreibung |
|--------|-------------|
| Heute aktiv | Die heutigen Aktivitäten sind derzeit im Gange |
| Heute Alle | Alle heutigen Aktivitäten |
| Heute Demnächst | Die heutigen, noch nicht begonnenen Aktivitäten |
| Alle Veranstaltungen | Vollständige Listenvorschau, sortiert nach Status |
| Statistikübersicht | Aktiv / Demnächst / Alle Zählungen – Große Anzeigen. Abgelaufen / Abgeschlossen / Abgebrochen |
| Ergebnis | Heute, diese Woche, diesen Monat und dieses Jahr |
| Blick | Aktivitätsanzahl + Einnahmen + Aktivanzahl auf einen Blick |
| Top-Plattformen | Das diesjährige Gewinnranking nach Plattform |
| Sperrbildschirm (4 Stile) | Rundes, rechteckiges und Inline-Zubehör – iOS 16+ |

Unter iOS 17 und höher unterstützen Listen-Widgets **Tippen pro Zeile**, um die passende Aktivität direkt zu öffnen.

Eine integrierte **Widget-Anleitung** in den Einstellungen führt Sie Schritt für Schritt durch das Hinzufügen von Widgets, mit einer Widget-Galerie und FAQ.

### Extras zum Aktivitätsformular

- **Beliebte App-Links** – mit einem Fingertipp ausfüllen für gängige URL-Schemata für Bezahl-, Bank- und Shopping-Apps.
- **Scannen oder aus Album auswählen** – scannen Sie einen QR-Code oder wählen Sie ein Bild aus, um die Aktivitäts-URL automatisch auszufüllen.

### QR-/Barcode-Scanner

Ein eigenständiger Scanner unter **Einstellungen → Extras**:

- Echtzeit-Kamerascan mit Taschenlampenunterstützung.
- Wählen Sie aus einem Fotoalbum mit visueller Erkennung.
- Ergebnisliste mit One-Tap-Kopierung, In-App-Safari für http/https-Links und Export über Share Sheet.

### Aussehen und Sprache

- Über 8 Themenfarben (Gold, Ozeanblau, Waldgrün, Rosenrosa, Lavendel, Sonnenuntergangsorange, Mint, Kirschrot …)
- Hell-/Dunkel-/System-Erscheinungsbild – mit haptischer Rückmeldung beim Schalter.
- **20 alternative Startbildschirm-App-Symbole.**
- 13 Anzeigesprachen: Englisch, vereinfachtes Chinesisch, traditionelles Chinesisch, Japanisch, Koreanisch, Thailändisch, Hindi, Spanisch, Französisch, Deutsch, brasilianisches Portugiesisch, Russisch, Arabisch – unabhängig von der Systemsprache umschaltbar.
- Mehrere Währungen (ISO 4217); anpassbare **Dezimalstellen** für allgemeine Beträge (Standard 2) und Diagrammbeschriftungen (Standard 0).
- Konfigurierbare **App-Badge-Strategie** (aus/heutige Zählung/Gesamtzahl ausstehend).
- **Weitere Empfehlungen** – Link zur App Store-Seite des Entwicklers unter Einstellungen → Info.

### Daten & Datenschutz

- **Vollständiges Backup exportieren** – CSV-Datei mit allen Aktivitäten, Erinnerungen, Einnahmen, Wiederholungsstatus und Vorlagen.
- **Sicherung importieren** – Ersetzen Sie die gesamte Bibliothek oder führen Sie sie nur durch Anhängen zusammen (behält vorhandene Daten bei).
- **Archivieren mit nur einem Fingertipp** – Archivieren Sie alle abgeschlossenen/abgelaufenen/abgebrochenen einmaligen Aktivitäten auf einmal.
- Das Archiv kann jederzeit über die Einstellungen wiederhergestellt werden.
- Beim Teilen einer Aktivität wird Text in die Zwischenablage kopiert. Durch den Umschalter **Teilen-inklusive-Erträge** (standardmäßig deaktiviert) bleiben Ihre Verdienstbeträge privat.

## Wiederholungsregeln

| Typ | Optionen |
|------|---------|
| Täglich | Alle N Tage |
| Wöchentlich | Jede Kombination von Wochentagen |
| Monatlich | Einzelner Tag, bis zum Enddatum oder bis zum Monatsende |
| Jährlich | Ein Tag, bis zum Enddatum oder bis zum 31. Dezember |
| Benutzerdefiniert | Benutzerdefiniertes Intervall in Tagen |

Endbedingungen: ein bestimmtes Enddatum oder eine maximale Anzahl von Vorkommen.

## Systemanforderungen

| Funktion | Mindestens |
|---------|---------|
| iPhone/iPad | iOS 15.0+ |
| Sperrbildschirm-Widgets | iOS 16.0+ |
| Dynamic Island – Event-Countdown | iOS 16.1+ (unterstützte Hardware) |
| Schnelle Countdown-Live-Aktivität | iOS 16.2+ |
| Tippen Sie auf das Widget pro Zeile | iOS 17.0+ |

## Kontaktieren Sie uns

Fragen, Feedback oder benötigen Sie Hilfe? Erreichen Sie uns unter:

- **In-App:** Einstellungen → Feedback senden
- **E-Mail:** [AppleOSer@gmail.com](mailto:AppleOSer@gmail.com)

Wir antworten in der Regel innerhalb von 48 Stunden.

[FAQ](faq) · [URL-Schema](url-scheme) · [Datenschutzerklärung](privacy)
