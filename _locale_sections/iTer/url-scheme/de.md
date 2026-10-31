iTer unterstützt das URL-Schema ** `iTer://` ** auf **iPhone und iPad**. Verwenden sie es in shortcuts, safari, widgets oder anderen apps, um eine frage, das tägliche quiz, favoriten oder das falsche antwortbuch zu öffnen.

** Quick Actions** (langes Drücken des App-Symbols) verwenden die gleichen `iTer://` -Strings wieder. Wählen Sie bis zu **4** aus **7** Optionen in **Einstellungen → Home Screen Shortcuts **.

> **Hinweis:** Deep Links **navigate** innerhalb der App. Sie ändern keine Quizeinstellungen oder markieren Fragen aus der Ferne. **Mac** registriert keine Quick Actions für den Startbildschirm; Widgets und In-App-Navigation funktionieren weiterhin auf dem Mac.

## Protokoll


```
iTer://<host>[?query]
```


| Rule | Einzelheiten |
|------|--------|
| **Scheme** | "iTer" (fallunempfindlich) |
| **Question detail** | Host `question` — abfrage **`id=<questionID>`** oder **`q=<questionID>`** (erforderlich) |
| **Daily Quiz** | Host "Quiz" |
| **Favourites** | Host `Favoriten` → Einstellungen → Favoritenliste |
| **Wrong book** | Host `falsch`, `Fehler` oder `falsche Fragen` — optional **`record=<UUID>`** öffnet einen Fehler |
| **Search** | Host `search` — Quick Action / Shortcut only (öffnet globale Such-Tab) |
| **Categories** | Host `categories` — Quick Action / shortcut only (öffnet die Registerkarte Kategorien) |
| **Feedback** | Host `Feedback` — Quick Action only (mail compose oder `mailto:` fallback) |
| **Rate app** | Host `review` — Quick Action only (StoreKit in-app review). Legacy-Typen, die "Sterne" enthalten, funktionieren ebenfalls. |

Pfade wie `iTer://` werden akzeptiert, wenn der Host leer ist und das Pfadsegment übereinstimmt.

## Beispiele


```
iTer://question?id=94c34bb2bdef11e6a0e100163e0021c8
iTer://quiz
iTer://favorites
iTer://wrong
iTer://wrong?record=550E8400-E29B-41D4-A716-446655440000
```


## Home Bildschirm Schnelle Aktionen

| Type | Typische Verwendung |
|------|-------------|
| `iTer://search` | Globale Suche |
| `iTer://quiz` | Täglicher Quiz Tab |
| `iTer://favorites` | Favoritenliste |
| `iTer://wrong` | Falsches Antwortbuch |
| `iTer://categories` | Tab Kategorien |
| `iTer://feedback` | Feedback senden |
| `iTer://review` | Bewerten Sie die App (StoreKit) |

Standardauswahl: Suche, Quiz, Favoriten, Feedback. Bestellen oder ersetzen Sie in ** Einstellungen → Home Screen Shortcuts ** (max 4). Die App passt die Verknüpfung `iTer://` Strings mit **enthält **, so dass Legacy-Varianten, die diese Pfade enthalten, immer noch korrekt routen.

## Widget Deep Links

| Widget | Typische URL |
|--------|-------------|
| Daily Question | „iTer://question?id=... |
| Quiz Glance | „iTer://quiz |
| Favourites Glance | „iTer://favorites |
| Wrong Book Glance | `iTer://wrong` oder `iTer://wrong?record=<UUID>` |

---

[Zurück zu iTer Support](../) · [FAQ](../faq) · [Privacy Policy](../Privacy)


