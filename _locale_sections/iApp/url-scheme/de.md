iApp unterstützt ** `iapp://` ** und ** `iappstore://` ** Shortcut Links. Verwenden Sie sie in **Shortcuts**, Safari-Lesezeichen oder von **Home Screen Widgets** und **Live Activity**, um ** eine App-Detailseite** zu öffnen, **zurück zu einer gefilterten Rankings-Ansicht**, **Tabs** zu wechseln oder **zu sekundären Seiten** zu springen (Entwicklerfavoriten, Browserverlauf, Rangverfolgung und mehr).

> **Hinweis:** Long-Presse **Home Screen Quick Actions** verwenden den gleichen `iapp://` -Linktext, werden aber als Quick Actions gesendet – nicht durch den gleichen Pfad wie Safari / Shortcuts URLs analysiert, wenn sie nur aus dem Symbolmenü geöffnet werden.

## Linkformat


```
iapp://...
iappstore://...   (older alias, works the same)
```


Hosts sind **case-insensitive ** und normalisiert zu **kebab-case ** ( `iapp://` und `iappstore://` → `iapp://{host}` ). Legacy Aliase: `developer_favorites` → rank, `developer.favorites` → subscription, `developer-favorites` → review.

| What you want | Art der Verbindung |
|---------------|-----------|
| Open an app detail page | „iapp://app? |
| Open Rankings with filters | „iapp://rank? |
| Switch tabs or open settings pages | `iapp://{host}` (siehe Tabellen unten) |
| Tap an app in a widget | Öffnet die Detailseite |
| Tap the widget title / blank area | Öffnet die passende Rankings-Ansicht |
| Tap a rank **Live Activity** | Öffnet die passende Rankings-Ansicht |
| Tap a subscription **Live Activity** | Öffnet die App-Detailseite |

---

## Öffnen Sie eine App-Detailseite


```
iapp://app?id={APP_ID}&region={region}&country={cc}
```


| Parameter | Required | Beschreibung |
|-----------|----------|-------------|
| `id` | **Yes** | App Store ID |
| `region` | No | Regionscode, z. B. `cn`, `us`, `jp` (Standard: `us`) |
| `country` | No | Fakultativer Regionencode, wenn „Region weggelassen wird |

**Beispiel**


```
iapp://app?id=6446581591&region=cn
```


Verwendet von: **Mein Favoriten-Widget** (tippen Sie auf eine App), **Abonnement Live Activity** (tippen Sie auf die Aktivität) und **Shortcuts** / Lesezeichen.

---

## Offene Rankings mit Filtern

Wechselt zur Registerkarte **Rankings** und wendet das gewählte Diagramm, die Kategorie und die Region an.


```
iapp://rank?type={chart}&category={category}&region={region}
```


| Parameter | Beschreibung |
|-----------|-------------|
| `type` | Kartencode (siehe Tabelle unten) |
| `category` | Kategoriecode — Hauptkategorie oder Spielunterkategorie |
| `region` | Regionscode, z.B. `cn`, `us` |

Unerkannte Werte werden ignoriert; anerkannte Werte werden erinnert.

### Kartencodes ( `iapp://` ) — 12 Karten

| Code | Karte |
|------|-------|
| `topFreeApplications` | iPhone Top Free |
| `topPaidApplications` | iPhone Top bezahlt |
| `topGrossingApplications` | iPhone Top Grossing |
| `newApplications` | Neue Apps |
| `newFreeApplications` | Neu kostenlos |
| `newPaidApplications` | Neu bezahlt |
| `topFreeiPadApplications` | iPad Top Free |
| `topPaidiPadApplications` | iPad Top bezahlt |
| `topGrossingiPadApplications` | iPad Top Grossing |
| `topFreeMacApplications` | Mac Top Free |
| `topPaidMacApplications` | Mac Top bezahlt |
| `topGrossingMacApplications` | Mac Top-Brutto |

### Kategoriecodes ( `iapp://` )

| Code | Kategorie |
|------|----------|
| `0` | Alle Apps |
| `6014` | Spiele (alle Spiele) |
| `6005` | sozial |
| `6007` | Produktivität |
| `6002` | Versorgungsunternehmen |
| `6008` | Foto & Video |
| `6017` | Bildung |
| `6015` | Finanzen |
| … | 26 Hauptkategorien insgesamt |

**Spielunterkategorien: `iapp://` – `iappstore://` , `iapp://{host}` – `developer_favorites` (18 Genres). Beispiel: `developer.favorites` = Aktion.

### Beispiele


```
iapp://rank?type=topFreeApplications&category=6014&region=cn
iapp://rank?type=topFreeMacApplications&category=0&region=us
```


### Ältere Links im chinesischen Stil (immer noch unterstützt)


```
iapp://rank?type=热门免费榜&category=游戏&region=中国
```


Verwendet von: **Rankings-Widget** (Titel / leerer Bereich), **Rank Live Activity** (Tippen Sie die Aktivität) und **Shortcuts**.

---

## Widget Deep Links

Widgets verwenden kein separates URL-Format – sie erzeugen automatisch die gleichen `iapp://` und `iappstore://` -Links.

| Widget | Tap target | Offen |
|--------|------------|-------|
| **Rankings · iApp** | An app row | „iapp://app?id=...&region=... |
| **Rankings · iApp** | Title or blank area | `iapp://rank?type=...&category=...&region=...` |
| **My Favorites · iApp** | An app row | „iapp://app?id=...&region=... |

Angeheftete Favoriten erscheinen zuerst im Widget Meine Favoriten. Widget-Thema und -Sprache folgen **Einstellungen → Widgets** und Ihrer App-Sprache (alle 18 Sprachen). Beim Konfigurieren von Widget-Regionen zeigt HK / TW / MO klarere Anzeigenamen in der Liste und vereinheitlichte Suche (z.B. „China“, „HK“); gespeicherte Region **codes** in Links bleiben `iapp://` , `iappstore://` , `iapp://{host}` .

---

## Browserverlauf (kein URL-Link)

**App Browse History** wird unter **Einstellungen → Daten → App Browse History** verwaltet. Wenn Sie auf einen Eintrag tippen, wird die Detailseite in der iApp erneut geöffnet - sie verwendet **nicht ** eine `iapp://` URL, die Sie extern kopieren oder teilen können.

---

## Live Activity Deep Links

| Live Activity type | Tap behavior | Geschaffene Verbindung |
|--------------------|--------------|----------------|
| **Rankings** (tracking preset) | Opens filtered Rankings | „iapp://rank? |
| **Subscriptions** (per subscription) | Opens app detail | „iapp://app?id=...&region=... |

Aktivieren Sie die Live-Aktivität des Rangs pro Tracking-Voreinstellung in **Einstellungen → Erweitert**. Aktivieren Sie die Live-Aktivität des Abonnements in **Einstellungen → Erweitert → Live-Aktivität** (getrennt vom Rang Live-Aktivität); dann pro Abonnement beim Hinzufügen oder Bearbeiten. Preis-Drop-Monitore zeigen Baseline vs aktuellen Preis auf dem Sperrbildschirm.

---

## Tab & Action Links (keine Abfrage)

Diese öffnen einen Tab oder lösen eine In-App-Aktion aus. Funktioniert von **Shortcuts **, Safari und **Home Screen Quick Actions **.

### Hauptregisterkarten

| URL | Öffnet |
|-----|--------|
| `iapp://search` | Suchtab + Fokus Suchfeld |
| `iapp://rank` | Rankings Tab (keine Filteränderung, wenn keine Abfrage) |
| `iapp://favorites` | **Favoriten-Tab** wenn aktiviert in **Einstellungen → App-Einstellungen**; ansonsten **Einstellungen → App-Favoriten** |
| `iapp://subscription` | Registerkarte Abonnements, falls sichtbar; ansonsten **Einstellungen → Abonnements** |
| `iapp://settings` | Tab Einstellungen |
| `iapp://feedback` | Feedback-E-Mail |
| `iapp://review` | In-App App Store Rating (alias `iapp://rate`) |

### Sekundärseiten

Öffnet zuerst die Registerkarte **Einstellungen ** und drückt dann die Zielseite. Wenn eine passende Registerkarte vorhanden ist (z. B. Entwicklerfavoriten), öffnet diese Registerkarte stattdessen.

| URL | Öffnet |
|-----|--------|
| `iapp://developer-favorites` | Tab Entwicklerfavoriten oder **Einstellungen → Entwicklerfavoriten** |
| `iapp://browse-history` | **Einstellungen → Daten → App Browse History** |
| `iapp://favorite-groups` | **Einstellungen → Daten → Lieblingsgruppen** |
| `iapp://rank-tracking` | **Einstellungen → Erweitert → Rank Tracking** |
| `iapp://live-activity` | **Einstellungen → Fortgeschrittene → Live-Aktivität** |
| `iapp://apple-services` | **Einstellungen → Drittanbieter → Apple Services** |
| `iapp://region-switch` | **Einstellungen → Drittanbieter → App Store Region** |
| `iapp://usage-guide` | **Einstellungen → Hilfe → Gebrauchsanweisungen** |
| `iapp://widget-guide` | **Einstellungen → Widgets → Widget Guide** (nur iOS 17+; URL funktioniert, aber nicht im Quick Actions Picker aufgeführt) |

---

## Home Bildschirm Schnelle Aktionen

Langes Drücken des App-Icons. Passen Sie bis zu **4** von **15** Optionen in **Settings → Home Screen Long Press → Customize Shortcuts** an.

Standardauswahl: Suche, Rang, Favoriten, Feedback.

Jede Option verwendet `iapp://` dieselben URLs wie oben. Schnelle Aktionen werden über das Icon-Menü gesendet; externe Shortcuts / Safari verwenden den einheitlichen `iappstore://` Pfad.

| Link | Öffnet |
|------|--------|
| `iapp://search` | Such-Tab + Fokus |
| `iapp://rank` | Tab Rankings |
| `iapp://favorites` | Favoriten Tab oder Einstellungen → App Favoriten |
| `iapp://developer-favorites` | Tab Developer Favorites oder Einstellungen → Developer Favorites |
| `iapp://subscription` | Tab Abonnements oder Einstellungen → Abonnements |
| `iapp://browse-history` | App Browse History |
| `iapp://favorite-groups` | Lieblingsgruppeneinstellungen |
| `iapp://rank-tracking` | Rangverfolgung |
| `iapp://live-activity` | Einstellungen für Live-Aktivitäten |
| `iapp://apple-services` | Apple Services Links |
| `iapp://region-switch` | App Store Region Switch |
| `iapp://usage-guide` | Gebrauchsanweisung |
| `iapp://settings` | Tab Einstellungen |
| `iapp://feedback` | Feedback-E-Mail |
| `iapp://review` | In-App-Rating | `iapp://` wird als externe URL unterstützt, aber **not** ist im Quick Actions Picker verfügbar.

---

## Siri & Shortcuts (iOS 16+)

Finden Sie integrierte Aktionen in der **Shortcuts** App oder fragen Sie **Siri**. Alle Intent-Titel, Parameter-Beschriftungen und Siri-Phrasen sind in jeder App-Sprache **voll lokalisiert ** - sie werden aktualisiert, wenn Sie ** Einstellungen → Aussehen → Sprache ** ändern.

| Action | What you can set | Wirkung |
|--------|------------------|--------|
| Search apps | Keyword and region | Öffnet Such-Tab mit Abfrage |
| Open charts | Chart, category, and region | Öffnet Rankings mit Filtern (gleich wie `iapp://rank`) |
| Add favorite | App ID and region | Addiert zu Favoriten schweigend |

**Beispiel Siri Phrasen (englische Benutzeroberfläche): *"Suchen Sie Apps in iApp"*, *"Öffnen Sie Diagramme in iApp"*, *"Favorit in iApp hinzufügen"*. In 简体中� erscheinen Phrasen auf Chinesisch; dasselbe für alle 18 Sprachen.

---

## Mac Keyboard Shortcuts

Verwenden Sie auf dem Mac **⌘1** bis **⌘N**, um die Registerkarten zu wechseln. Zahlen werden **dynamisch ** zugewiesen, basierend darauf, welche Tabs sichtbar sind:

| When visible | Typische Abkürzung |
|--------------|------------------|
| Rankings | ⌘1 |
| Search | ⌘2 |
| Subscriptions (if shown) | Nächste Nummer |
| Favorites (if tab enabled) | Nächste Nummer |
| Developer Favorites (if tab enabled) | Nächste Nummer |
| Settings | Letzte Nummer |

Beispiel mit allen optionalen Registerkarten auf: ⌘1 Rankings · ⌘2 Suche · ⌘3 Abonnements · ⌘4 Favoriten · ⌘5 Entwicklerfavoriten · ⌘6 Einstellungen.

Wenn ein Tab ausgeblendet wird, werden die verbleibenden Tabs automatisch neu nummeriert.

---

## Regionscodes in Links

Deep Links und widgetgenerierte URLs verwenden immer stabile **Regionalcodes** ( `iapp://` , `iappstore://` , `iapp://{host}` , `developer_favorites` , `developer.favorites` , ...) — keine lokalisierten Anzeigenamen. Region Picker und Suche können klarere Etiketten zeigen, aber gespeicherte Codes bleiben gleich.

**Beispiele**


```
iapp://app?id=6446581591&region=hk
iapp://rank?type=topFreeApplications&category=0&region=tw
```


---

## In-App-Suche (nicht URL-Links)

Diese funktionieren in iApp, sind aber **nicht `iapp://` URLs:

| Action | Wie |
|--------|-----|
| **Single App ID search** | Geben Sie eine numerische ID (6-12 Ziffern, kein Komma) in der Suche ein |
| **Batch App ID search** | Bis zu 50 Komma-getrennte IDs |
| **Add Subscription** | Lange drücken Sie jede App-Reihe |
| **Save Developer** | Long-Press → **Developer** Untermenü oder Detail **Mehr ** Menü |
| **Open by-ranking view** | Kontextmenü → Entwickler-Apps oder Entwicklerfavoriten |
| **Pause / resume subscription** | Long-Press auf einer Subscription-Reihe |
| **Reopen from browse history** | **Einstellungen → Daten → App Browse History** → Tap-Eintrag |

Verwenden Sie ** `iapp://` ** Links oder **Siri / Shortcuts**, wenn Sie iApp von außerhalb der App öffnen müssen.

---

## Tipps

- Link codes work in any app language — Sie ändern sich nicht, wenn Sie die UI-Sprache wechseln.
- Widgets und **Live Activity** erzeugen diese Links automatisch, wenn Sie tippen.
- Widget-Diagrammdaten für einige Mac / iPad bezahlt und Hochrechnung Charts können leicht von der Haupt-App abweichen.
- **Add favorite** via Shortcuts does not open the app UI — Es schreibt direkt in Ihre Favoritenliste.
- **Content compare** mode in all-region info cannot export share images — Wechseln Sie zuerst zur Listen- oder Rasteransicht.

[Zurück zur Übersicht](..) · [FAQ](../faq) · [Privacy](../privacy]


