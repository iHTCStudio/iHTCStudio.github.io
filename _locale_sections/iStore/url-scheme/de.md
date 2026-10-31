iStore unterstützt ** `istore://` ** Shortcut Links. Verwenden Sie sie in **Shortcuts **, Safari-Lesezeichen oder von **Widgets **, **Control Center **, **Spotlight ** und der **Share Extension **, um ** eine Region zu wechseln **, ** Ihre letzte Region zu wechseln **, ** einen Tab zu öffnen ** oder ** zu einem Guide zu springen **.

## Linkformat


```
istore://{host}?{params}
```


Hosts sind **case-insensitive **. Regionscodes verwenden Standardwerte **Alpha-2** ( `istore://` , `us` , `cn` , `jp` , `hk` , ...).

| What you want | Link |
|---------------|------|
| Switch to a region | „istore://switch?region={code} |
| Switch to your last region | „istore://switch-last |
| Open the Store / Favorites / Settings tab | `istore://store` · `istore://favorites` · `istore://settings` |
| Open App Availability | „istore://availability |

---

## Wechsel zu einer Region

Fordert einen Wechsel in die angegebene Region an (durch die In-App-Bestätigung geleitet, falls aktiviert).


```
istore://switch?region={code}
```


| Parameter | Required | Beschreibung |
|-----------|----------|-------------|
| `region` | **Yes** | Regionscode, z.B. `us`, `cn`, `jp`, `hk`, `tw` |

**Beispiel**


```
istore://switch?region=us
```


Verwendet von: **interaktive Widgets**, **Spotlight** Ergebnisse und **Shortcuts / Siri**.

---

## Wechseln Sie zu Ihrer letzten Region


```
istore://switch-last
```


Lies dein letztes Switch-Ziel und wechsele erneut zu ihm. Betreibt die **Switch Last** Control Center-Steuerung (iOS 18+) und die passende Shortcut / Siri-Aktion.

---

## Tabs & Seiten (keine Abfrage)

| URL | Öffnet |
|-----|-------|
| `istore://store` | Speichertipp |
| `istore://favorites` | Favoriten-Tab |
| `istore://settings` | Tab Einstellungen |
| `istore://availability` | Einstellungen → App-Verfügbarkeit (auch von der Share Extension verwendet) |
| `istore://switch-history` | Switch History |
| `istore://quick-regions` | Quick Regions Einstellungen |
| `istore://feature-guide` | Funktionsübersicht |
| `istore://widget-guide` | Widget-Anleitung |
| `istore://shortcuts-guide` | Kurzbefehle-Anleitung |
| `istore://usage-guide` | Nutzungsanleitung |
| `istore://feedback` | Feedback-E-Mail |
| `istore://in-app-review` | App-Store-Bewertung in der App |

---

## Widgets, Kontrollzentrum & Spotlight

Diese erzeugen automatisch `istore://` -Links, wenn Sie tippen:

| Source | Tap target | Wirkung |
|--------|------------|--------|
| **Quick Regions / Recent / Custom widget** | A region tile | „istore://switch?region=... |
| **Switch Last control** (iOS 18+) | The control | „istore://switch-last |
| **Spotlight** | A region result | „istore://switch?region=... |

Interaktiver Wechsel von Widgets und Control Center öffnet die App, um die offizielle Umleitung des App Store abzuschließen.

---

## Aktienverlängerung

Teilen Sie einen beliebigen **App Store Link** in iStore. Die Share Extension prüft die Verfügbarkeit in beliebten Regionen und kann dann die App über `istore://` öffnen, damit Sie das Ergebnis überprüfen und wechseln können.

---

## Siri & Shortcuts

Finden Sie integrierte Aktionen in der **Shortcuts** App oder fragen Sie **Siri**. Titel und Phrasen sind auf Englisch lokalisiert / 简体中� / 繁體中�.

| Action | What you can set | Wirkung |
|--------|------------------|--------|
| Switch region | Region | Wechsel in diese Region |
| Switch last region | — | Wechsel zu Ihrem letzten Ziel |
| Switch favorite region | A favorite | Wechsel zu einer bevorzugten Region |
| Open store | — | Öffnet iStore |
| Check availability | App link or ID | Prüft, wo die App verfügbar ist |

---

## Regionscodes in Links

Deep Links und widgetgenerierte URLs verwenden immer stabile **Regionalcodes** ( `istore://` , `us` , `cn` , `jp` , ...) — keine lokalisierten Anzeigenamen.

**Beispiele**


```
istore://switch?region=jp
istore://switch?region=hk
```


[Zurück zur Übersicht](..) · [FAQ](../faq) · [Privacy](../privacy]


