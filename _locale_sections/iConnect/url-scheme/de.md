iConnect unterstützt ** `iconnect://` ** URL-Schema Deep Links - Öffnen Sie einen Tab, eine Einstellungsseite oder ein In-App-Blatt von Safari, einer anderen App, einem Lesezeichen oder Apple Shortcuts. Diese URLs spiegeln die verfügbaren Ziele als **Home Screen Quick Actions** auf iPhone und iPad wider (langes Drücken des App-Symbols).

> **Hinweis:** URL-Links nur **navigieren innerhalb von iConnect**. Sie verbinden sich nicht mit einem peer, starten eine Übertragung oder öffnen einen bestimmten chat-thread.

## Protokollspezifikation


```
iconnect://<host>
iconnect://<host>?refresh=1
```


| Rule | Einzelheiten |
|------|--------|
| **Scheme** | „iconnect |
| **Host / path** | Ein einzelnes Segment, **case-unsensitive ** - aufgelöst von URL **host ** oder erstem **path ** Segment |
| **Aliases** | Mehrere Hosts akzeptieren Synonyme (siehe Tabelle unten) |
| **Query** | Nur `refresh=1` / `refresh=true` auf **Devices** löst eine Discovery-Aktualisierung aus |

Beispiele für gleichwertige Formulare:


```
iconnect://devices
iconnect://open/devices
```


---

## Tab Destinationen

| URL | Öffnet |
|-----|--------|---------|
| `iconnect://devices` | **Devices** tab (radar / discovery) | "Gerät" |
| `iconnect://devices?refresh=1` | **Devices** tab and **refreshes** nearby discovery | — |
| `iconnect://chat` | **Chats** tab | "Botschaften" |
| `iconnect://transfers` | **Transfers** tab | „Übertragung |
| `iconnect://history` | **History** tab (transfer log) | — |
| `iconnect://settings` | **Settings** tab | "Setzen" |

**Refresh Discovery**


```
iconnect://devices?refresh=1
iconnect://devices/refresh
```


---

## Einstellungen Unterseiten

Diese Links wechseln zu **Settings** und öffnen dann die passende Seite:

| URL | Öffnet |
|-----|--------|---------|
| `iconnect://about` | About | — |
| `iconnect://usage` | Usage Guide | `guide`, `help`, `usageguide` |
| `iconnect://shortcuts` | Home Screen shortcuts picker (iOS) | „Homeshortcuts |
| `iconnect://debug` | Debug / diagnostics info | „Debuginfo |

---

## In-App-Aktionen

| URL | Öffnet |
|-----|--------|
| `iconnect://share` | Teilen Sie iConnect Blatt (App Store Link + Empfehlungstext) |
| `iconnect://feedback` | Feedback E-Mail compose (fällt zurück zu `mailto:`, wenn Mail nicht verfügbar ist) |
| `iconnect://review` | In-App App Aufforderung zur Abgabe von Speicherbewertungen |

**Review Aliase:** `iconnect://` , `iconnect` ---

## Beispiele

** Chats öffnen Tab**


```
iconnect://chat
```


**Offener Transfer-Tab**


```
iconnect://transfers
```


**Refresh Device Discovery**


```
iconnect://devices?refresh=1
```


**Open Usage Guide**


```
iconnect://usage
```


** Teilen Sie die App**


```
iconnect://share
```


---

## Startseite Bildschirm Quick Actions (iOS)

Langes Drücken des iConnect-Icons. Passen Sie bis zu **4** Shortcuts in **Settings → Home Screen Shortcuts ** an (drag to reorder).

| Quick Action | URL |
|--------------|-----|
| Devices | „iconnect://devices |
| Chats | „iconnect://chat |
| Transfers | „iconnect://transfers |
| History | „iconnect://history |
| Share | „iconnect://share |
| Feedback | „iconnect://feedback |
| Rate | „iconnect://review |
| About | „iconnect://about |

Standardmäßig aktiviert: **Geräte**, **Chats**, **Share**, **Feedback**.

Quick-Action-Typen verwenden die gleichen `iconnect://` -Strings und werden durch denselben Parser wie externe URLs geleitet.

---

## Apple Shortcuts

**Offener Transfer-Tab**

1. Aktion hinzufügen **Offene URL**
2. URL: `iconnect://` **Refresh in der Nähe Geräte nach dem Beitritt Wi‐Fi**


```
iconnect://devices?refresh=1
```


Verwenden Sie **Offene URL** in einer persönlichen Automatisierung (z. B. wenn Wi-Fi verbunden ist), um zum Suchen und Scannen zu springen.

---

## Startverhalten

Wenn iConnect eine URL erhält (Kaltstart oder während des Laufens):

1. Der Link wird durch `iconnect://` analysiert.
2. Tab-Schalter animieren sofort; **share**, **feedback** und **review** öffnen sich nach kurzer Verzögerung (~0,4 s auf iOS), damit die Benutzeroberfläche das Montieren beenden kann.
3. **Feedback** verwendet, wenn verfügbar, In-App-Mail; ansonsten wird der Standard-Mail-Client über `iconnect://` geöffnet.
**Share** auf dem Mac verwendet den System-Share-Picker; auf iOS präsentiert er ein Sharesheet.

---

## Fehlerbehebung

| Issue | Was zu überprüfen ist |
|-------|----------------|
| Link does nothing | Stellen Sie sicher, dass iConnect installiert ist; Host muss mit einem unterstützten Namen übereinstimmen |
| `feedback` opens Mail only | Kein auf dem Gerät konfiguriertes Mail-Konto — erwarteter Fallback |
| `shortcuts` has no effect on Mac | Home Screen Shortcut Anpassung ist ** iOS nur ** |
| URL does not connect to a device | Deep Links navigieren nur - Verwenden Sie die Registerkarte Geräte, um Peers manuell zu entdecken |

---

[Zurück zum iConnect Support](..) · [FAQ](../faq) · [Privacy Policy](../Privacy)


