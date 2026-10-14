TwinPolarCam unterstützt ** `twinpolarcam://` ** Verknüpfungen. Verwenden Sie sie in **Safari-Lesezeichen **, der **Shortcuts ** App oder von **Home Screen Quick Actions ** und **Spotlight **, um direkt in Guides und Keyscreens zu springen.

## Linkformat


```
twinpolarcam://{host}
```


Es gibt keine Pfad- oder Abfragekomponente - das Routing ist nur **Hostname ** (fallunempfindlich).

---

## Leitfäden

| URL | Öffnet |
|-----|-------|
| `twinpolarcam://usage-guide` | **Wie man ** Anleitung verwendet |
| `twinpolarcam://recording-guide` | **Aufzeichnung & Zuverlässigkeit ** Leitfaden |
| `twinpolarcam://export-guide` | **Export & Pending** Guidesheet |
| `twinpolarcam://feature-guide` | **Feature Tour** (6-seitige Onboarding-Wiedergabe) |

Gleiche Ziele wie **App-Einstellungen → Hilfe**.

---

## App-Bildschirme

| URL | Öffnet |
|-----|-------|
| `twinpolarcam://settings` | App Settings Panel |
| `twinpolarcam://pending` | Manager für ausstehende Ausfuhren |
| `twinpolarcam://feedback` | Send Feedback (Mail Composer) |
| `twinpolarcam://recording` | Haupt-App (Live Activity / Dynamic Island Return) |

---

## Home Bildschirm Schnelle Aktionen

** Langes Drücken des TwinPolarCam-Symbols** – vier feste Verknüpfungen (gleiche Hosts wie oben):

| Quick action | URL |
|--------------|-----|
| Usage Guide | `twinpolarcam://usage-guide` |
| Recording Tips | „twinpolarcam://recording-guide |
| Export Guide | „twinpolarcam://export-guide |
| Feature Tour | `twinpolarcam://feature-guide` |

Schnelle Aktionen funktionieren am **kalten Start** und wenn die App bereits läuft. Wenn das Onboarding noch nicht abgeschlossen ist, wird der Link ** in die Warteschlange ** und geliefert, nachdem Sie den Willkommensführer abgeschlossen haben.

---

## Spotlight

TwinPolarCam indexes guide-Seiten in **Spotlight**. Suche nach:

- TwinPolarCam
- Usage Guide / Recording & Zuverlässigkeit / Export & Pending / Feature Tour

Durch Tippen auf ein Ergebnis wird das passende Leitblech geöffnet.

---

## Notizen

- **Unsupported devices** can still open guide links from the unsupported screen — nützlich für das Lesen der Anforderungen vor der Rückerstattung.
- Unbekannte Hosts werden **sicher ignoriert** (kein Absturz).
- Guides erfordern, dass die Hauptoberfläche bereit ist; Kaltstart-URLs werden gepuffert, bis die Initialisierung abgeschlossen ist.

[User Guide](index) · [FAQ](../faq) · [Privacy Policy](../privacy)


