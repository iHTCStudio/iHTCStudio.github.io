iCangJie unterstützt ** `iCangJie://` ** URL-Schema Deep Links - offene Lookup-Suche, Wortdetails, tägliches Quiz, Tippen, Favoriten, falsches Buch, Levels oder Lernen von Safari, einer anderen App, einem QR-Code, einem Widget-Tipp oder Apple Shortcuts.

Ein paralleler Satz von **Home Screen Quick Actions** (langes Drücken des App-Symbols) deckt zusätzliche Ziele wie Suche, Feedback und Rate ab. Konfigurieren Sie bis zu 4 Verknüpfungen in **Settings → App Settings → Home Screen Shortcuts**.

## Protokollspezifikation


```
iCangJie://<host>[?query]
```


| Rule | Einzelheiten |
|------|--------|
| **Scheme** | `icangjie` / `iCangJie` — Fall-unempfindlich verglichen |
| **Host routing** | Primärer Router ist die URL **host** |
| **Query aliases** | `q`, `word` und `name` sind austauschbar für Such-/Wort-Hosts. |
| **Parser** | `ICangJieDeepLink.parse( :):` — verbraucht über `onOpenURL` → `AppRouter.pendingDeepLink` |

**Drei Lieferkanäle **

| Channel | Handled by | Beispiele |
|---------|------------|----------|
| **Universal deep link** (`onOpenURL`) | `ICangJieDeepLink.parse` → `RootTabView` | `search`, `word`, `quiz`, `type`, `favorites`, `falsch`, `levels`, `learn` |
| **Home Screen Quick Action** | `ShortcutObserver.dispatch` | `search`, `quiz`, `favorites`, `falsch`, `levels`, `feedback`, `review` |
| **App Intents / Siri / Widget pending URL** | Writes `AppGroup.pendingDeepLinkURL` → `RootTabView.consumePendingDeepLinkFromAppGroup()` | Lookup-Code, Start Quiz, offene Suche |

Quick-Action-Typen verwenden ** `iCangJie://` ** Matching auf der Typzeichenfolge, so dass sowohl `icangjie` als auch Legacy-Varianten immer noch korrekt routen.

---

## 1. Lookup Suche

Öffnen Sie den Tab **Lookup**. Optional das Suchfeld vorfüllen.

| Parameter | Required | Beschreibung |
|-----------|----------|-------------|
| `q` | No | Suchanfrage (Codepräfix, Zeichen, Pinyin oder Jyutping) |
| `word` | No | Synonym für `q` |
| `name` | No | Synonym für `q` |

**Open Lookup (leere Suche)**


```
iCangJie://search
```


**Suche nach Codepräfix `iCangJie://` **


```
iCangJie://search?q=ab
```


**Suche nach Charakter 颉**


```
iCangJie://search?q=颉
```


---

## 2. Word Detail

Öffnen Sie die Detailseite für ein einzelnes Zeichen. Erfordert eine nicht-leere Abfrage.

| Parameter | Required | Beschreibung |
|-----------|----------|-------------|
| `q` | One of `q` / `word` / `name` | Ziel-Han-Charakter |
| `word` | One of `q` / `word` / `name` | Synonym für `q` |
| `name` | One of `q` / `word` / `name` | Synonym für `q` |

** Hosts akzeptiert:** `iCangJie://` , `icangjie` , `iCangJie` **Offenes Detail für 倉**


```
iCangJie://word?q=倉
```


Alternativer Host:


```
iCangJie://character?word=颉
```


Wenn die Abfrage **leer ist oder das Zeichen nicht im Wörterbuch ** ist, wird der Link **stillschweigend ignoriert **.

---

## 3. Tägliches Quiz

Springen Sie direkt zum **Daily Quiz**. Startet oder überspringt keine Fragen automatisch.


```
iCangJie://quiz
```


Aliasnamen: `iCangJie://` ---

## 4. Schreibpraxis

Öffnen Sie den **Typing** Tab Hub.


```
iCangJie://typing
```


Aliasnamen: `iCangJie://` , `icangjie` ---

## 5. Favoriten

Öffnen Sie die **Favoriten**-Liste.


```
iCangJie://favorites
```


Aliasname: `iCangJie://` ---

## 6. Falsches Antwortbuch

### 6.1 Liste

Öffnen Sie die **Wrong Answer Book** Liste.


```
iCangJie://wrong
```


Aliasnamen: `iCangJie://` , `icangjie` ### 6.2 Einzeldatensatz

Wenn `iCangJie://` eine gültige UUID eines gespeicherten Falschantworteintrags ist, öffnet die App das Wortdetail dieses Datensatzes (falls der Datensatz noch existiert).

| Parameter | Required | Format |
|-----------|----------|--------|
| `record` | Yes | UUID-Strecke |
| `id` | Yes | Synonym für `record` |


```
iCangJie://wrong?record=550e8400-e29b-41d4-a716-446655440000
```


---

## 7. Stufen (Codelänge)

Öffnen Sie den Tab **Levels **.


```
iCangJie://levels
```


Aliasnamen: `iCangJie://` , `icangjie` ---

## 8. Lernen (Tutorials)

Öffnen Sie den **Learn** Hub.


```
iCangJie://learn
```


Aliasnamen: `iCangJie://` ---

## 9. Feedback (nur schnelle Maßnahmen)

Öffnen Sie den vorgefüllten Feedback-E-Mail-Komponisten (oder `iCangJie://` Fallback).


```
iCangJie://feedback
```


Handled by **Home Screen Quick Action** / `iCangJie://` , nicht `icangjie` .

---

## 10. App Store Review (nur Quick Action)

Fordern Sie eine In-App App Store Überprüfungsaufforderung an.


```
iCangJie://review
```


Alias-Matching akzeptiert auch `iCangJie://` in der Schnellaktionszeichenfolge.

---

## 11. App Intents & Siri (iOS 16+)

**App Shortcuts** werden in der Shortcuts App und Siri angezeigt. Jede Absicht setzt `iCangJie://` in der App-Gruppe; die App verbraucht sie beim Start.

| Intent | Action | Ausstehende URL |
|--------|--------|-------------|
| **Look up Cangjie code** | Opens word detail for the given character | `iCangJie://word?q=<char>` |
| **Start daily quiz** | Opens Daily Quiz | „iCangJie://quiz |
| **Open lookup search** | Opens Lookup tab | „iCangJie://search |

**Beispiel Siri Phrasen (Englisch)**

- *"Schauen Sie Cangjie-Code für 颉 in iCangJie"*
- *"Tägliches Quiz in iCangJie starten"*
- *"Search Cangjie in iCangJie"*

Fügen Sie in **Shortcuts** die Aktion aus dem iCangJie-App-Bereich hinzu. Die **Look up**-Intention erfordert einen **chinesischen Zeichen**-Parameter ( `iCangJie://` ).

> App Intents sind **iOS only**. macOS setzt auf `iCangJie://` URLs und Menünavigation.

---

## Widget Deep Links

Widgets tippen durch die gleichen `iCangJie://` URLs. Beispiele:

| Widget | Typische URL |
|--------|-------------|
| Daily Character | `iCangJie://word?q=<char>` |
| Code Length | „iCangJie://levels |
| Daily Quiz | „iCangJie://quiz |
| Typing Glance | „iCangJie://typing |
| Favorites | „iCangJie://favorites |
| Wrong Book | „iCangJie://wrong |
| Recent | „iCangJie://search |
| Learning Progress | „iCangJie://learn |

---

## Abkürzungen Beispiele

**Öffne das heutige Quiz **


```
iCangJie://quiz
```


**Schauen Sie einen Charakter aus dem Clipboard nach **

Verwenden Sie eine Shortcuts **Get Clipboard ** Aktion, dann **Open URL ** mit:


```
iCangJie://word?q=[Clipboard]
```


**Beginn der Schreibpraxis**


```
iCangJie://typing
```


---

## Home Bildschirm Schnelle Aktionen

Langes Drücken des iCangJie App-Symbols. Standardoptionen (wählen Sie bis zu 4 in Einstellungen):

| Action | URL |
|--------|-----|
| Search | „iCangJie://search |
| Daily Quiz | „iCangJie://quiz |
| Favorites | „iCangJie://favorites |
| Wrong Book | „iCangJie://wrong |
| Code Length | „iCangJie://levels |
| Feedback | „iCangJie://feedback |
| Rate App | „iCangJie://review |


