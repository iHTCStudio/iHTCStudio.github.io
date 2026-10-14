iAppManager unterstützt ** `iappmanager://` ** Links für Shortcuts, Widgets, App Intents und Home Screen Aktionen.

## Linkformat


```
iappmanager://{host}[/…]
```


## Apps & Module

| URL | Öffnet |
|-----|-------|
| `iappmanager://apps` | Meine Apps |
| `iappmanager://apps/{appleId}` | Spezifische App (Übersicht) |
| `iappmanager://apps/{appleId}/{tab}` | App-Detailmodul | `iappmanager://` ist die numerische App Store Connect / App Store App ID. `iappmanager://apps` Beispiele:

| Tab | Modul |
|-----|--------|
| `overview` | Übersicht |
| `versions` | Fassungen |
| `builds` | Bauten |
| `backgroundAssets` | Hintergrund-Assets |
| `encryption` | Verschlüsselung |
| `submissions` | Überprüfungsvorschläge |
| `reviewDetail` | Details zur Überprüfung |
| `metadata` | Metadaten |
| `media` | Screenshots & Previews |
| `productPages` | Kundenspezifische Produktseiten |
| `appEvents` | In-App-Events |
| `appClips` | App Clips |
| `experiments` | Lagerversuche |
| `nominations` | Mit Nominierungen |
| `availability` | Verfügbarkeit |
| `pricing` | Preisgestaltung |
| `ageRating` | Altersbewertung |
| `accessibility` | Zugänglichkeit |
| `appTags` | App Tags |
| `iap` | In-App Käufe |
| `gameCenter` | Game Center |
| `testflight` | Prüfflug |
| `reviews` | Kundenbewertungen |
| `privacy` | Privatsphäre (Ernährungshinweis) |
| `promoCodes` | Promo-Codes |
| `webhooks` | Webhooks |

Beispiel: `iappmanager://` ## Sidebar & Tools

| URL | Öffnet |
|-----|-------|
| `iappmanager://certificates` | Zertifikate und Kennungen |
| `iappmanager://users` | Nutzer & Access |
| `iappmanager://reports` | Berichte |
| `iappmanager://settings` | Einstellungen |
| `iappmanager://add-account` | API Key Account hinzufügen |
| `iappmanager://about` | Über |
| `iappmanager://feedback` | Feedback-E-Mail |
| `iappmanager://in-app-review` | Rate prompt |

## In-App Guides

| URL | Guide |
|-----|-------|
| `iappmanager://feature-guide` | Feature Tour |
| `iappmanager://usage-guide` | Nutzungsanleitung |
| `iappmanager://widget-guide` | Widget-Anleitung |
| `iappmanager://shortcuts-guide` | Kurzbefehle-Anleitung |
| `iappmanager://release-guide` | Freigabebereitschaft |
| `iappmanager://iap-guide` | IAP & Abonnements |
| `iappmanager://testflight-guide` | Prüfflug |
| `iappmanager://reports-guide` | Berichte |

Kalte und warme Starts puffern kurze tiefe Links, damit das Onboarding zuerst beendet werden kann. App Intents kann auch eine verwaltete App mit einem optionalen Modul öffnen.


