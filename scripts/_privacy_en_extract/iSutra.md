**Last updated:** August 18, 2026

iHTC Studio ("we", "us" or "our") built **iSutra** (also known as "爱佛经" / "愛佛經", Bundle ID `com.iHTCboy.iSutra`). This Privacy Policy explains what data is (and is not) handled when you use the app. **Apple App Review** and users may rely on **this page** as the public privacy policy for the app. For App Store Connect, open this Privacy Policy in your browser and copy the address from the address bar (the public site domain may change over time).

## Summary (Apple Privacy Nutrition Label alignment)

| Topic | Our practice |
|-------|----------------|
| Account | **Not required** — no registration, email sign-in, or phone number |
| Data collection by iHTC Studio | **Data Not Collected** — we do **not** operate a backend that receives your personal data |
| Network | Library, reading, recite, Study Hall, Hunt, chant, practice, widgets, and daily notifications work **offline** after install |
| Analytics / ads / tracking | **None** — no third-party analytics, advertising, or tracking SDKs; no App Tracking Transparency use |
| Optional Apple services | **iCloud** (your private KVS), **Photo Library (Add Only)** for Dharma cards / exports, **StoreKit** for optional tipping, **local notifications**, optional **Live Activities**, optional **Spotlight** (off by default) |

## Data Collection

We do **not** collect, sell, or share personal information for advertising or analytics.

- **No account** — You can use all core features without creating an account with us.
- **No analytics or ads** — The app binary does not integrate third-party analytics, advertising, or crash-reporting SDKs that phone home to us.
- **No content upload** — Your reading history, favorites, lists, notes, mastery, streaks, chant counts, practice checklists, and preferences stay on your device (and optionally in **your** iCloud). They are never uploaded to iHTC Studio servers because **we do not run such servers for this app**.

## How the App Works

- **Bundled library** — Sutra JSON indexes, shards, large volumes, vernacular, English, famous lines, and indexes ship inside the app / widget bundle. Browsing and study do not require a network request.
- **On-device speech** — Recitation uses Apple’s system **AVSpeechSynthesizer** (TTS). We do not send sutra text to iHTC Studio.
- **Widgets & App Group** — Widgets and the app share preferences and lightweight state via App Group `group.com.iHTCboy.iSutra` on your device.
- **Daily notifications** — Scheduled locally with User Notifications. Tapping a notification opens a deep link to a passage ID on device; no server fan-out.
- **Dharma cards / exports** — Images and PDFs are rendered on device. Saving uses **Photo Library add-only** only when you tap save. System Share Sheet may send the file to an app **you** choose; that destination’s privacy policy then applies.
- **Copy-sutra (iOS)** — PencilKit strokes are stored under Application Support on the device (`CopySutra/…`) for drafts and export. They are **not** placed in the App Group and are **not** synced to iCloud.
- **Optional tip** — “Tip Developer” is a consumable **StoreKit** purchase processed by Apple. We do not receive your payment card details.
- **Siri / Shortcuts / Control Center** — Optional system integrations open on-device deep links; they do not send your library to us.
- **Optional Spotlight** — Off by default. If you enable indexing, content is indexed by the system on device for local search; we do not operate a search backend.

## Data Stored on Your Device

| Data | Where | Purpose |
|------|-------|---------|
| Sutra database (indexes, shards, large volumes) | App / Widget bundle | Offline reading & study |
| Favorites & lists (经单) | App Group UserDefaults | Starred passages and user lists |
| Reading history / last read | App Group UserDefaults | Continue reading, history UI |
| Study progress & mastery | App Group UserDefaults | Study Hall state, quiz / Hunt progress |
| Notes | App Group UserDefaults | Passage notes you write |
| Practice streak / check-in | App Group UserDefaults | Daily habit |
| Chant counts & sound prefs | App Group UserDefaults | Wooden-fish totals, goals, tones |
| Morning / evening practice & dedication | App Group UserDefaults | Daily liturgy checklist |
| Appearance & reading prefs | App Group UserDefaults | Theme, accent, language, layout, TTS, tabs, widgets |
| Daily Sutra cache & notification prefs | App Group UserDefaults | Today’s ID, schedule time |
| Share-card preferences | App Group UserDefaults | Last style / ratio choices |
| Copy-sutra drawings (iOS) | Application Support (`CopySutra/`) | Per-line tracing drafts |
| Onboarding & TipKit state | Standard UserDefaults (device) | Welcome guide / discovery tips |
| Home Screen quick actions | System + local prefs | Shortcuts you configure |
| Widget / Live Activity snapshots | App Group / ActivityKit | Display text / chant state you already opened |

Uninstalling the app removes sandbox and App Group data associated with the app (subject to iOS/macOS behavior). Optional iCloud copies remain in **your** iCloud until you clear them or turn sync off and delete elsewhere.

## iCloud Sync (Optional)

If you enable **iCloud Sync** in Settings, the app mirrors selected user data through Apple’s **`NSUbiquitousKeyValueStore`** tied to **your Apple ID** (favorites, lists, history, mastery, notes, chant preferences, practice configuration, and related progress). Sync traffic goes to **Apple iCloud**, not to iHTC Studio. Copy-sutra drawings are **not** included. You can disable sync in Settings. We cannot read your iCloud contents.

## Permissions

iSutra requests permissions only when a feature needs them:

| Permission | When | Why |
|------------|------|-----|
| Notifications | You enable Daily Sutra reminders | Local scheduling of reminder notifications |
| Photo Library (Add Only) | You save a Dharma card or export | Write the rendered image / PDF; we do not need full library read access |
| iCloud | You enable sync | Sync favorites / lists / history / mastery / notes / chant & practice prefs |
| Live Activities (iOS) | You enable Reading or Chant Live Activity | Show reading / chant progress on Lock Screen / Dynamic Island |
| Background audio (capability) | You enable background recitation | Continue TTS when the app is not foreground |

We do **not** request Contacts, precise Location, Camera, Microphone (beyond system TTS playback), or Tracking.

## What We Do Not Do

- We do **not** sell personal data.
- We do **not** build advertising profiles.
- We do **not** require an account or social login.
- We do **not** embed third-party ad, analytics, or social SDKs for data collection.
- We do **not** access your Photo Library beyond **add-only** when you choose to save.
- We do **not** receive StoreKit payment card numbers (Apple processes payments).
- We do **not** turn religious content into fortune-telling or paid blessing commerce.

## Children’s Privacy

iSutra does not knowingly collect personal data from anyone, including children under 13 (or the equivalent age in your region). Because we do not operate a data-collection backend, there is no child profile stored with us. Families may use the reading and practice features offline on their own devices.

## Third Parties

- **Apple** — App Store distribution, optional StoreKit purchases, optional iCloud KVS, system TTS, Share Sheet destinations you pick, and OS-level notification / Live Activity / Siri / Shortcuts delivery.
- **No other third-party SDKs** for ads, analytics, or social login are included for data collection.

## International Users

The app is designed to function offline on your device. Optional Apple services follow Apple’s terms and regional availability.

## Data Retention & Deletion

- **On device** — Local preferences and progress remain until you clear them in-app (where available), reset the device, or uninstall the app.
- **iCloud (optional)** — Data you synced remains in **your** iCloud account under Apple’s policies until you disable sync and/or clear it through Apple’s tools.
- **iHTC Studio** — Because we do not collect personal data on our servers, there is no account dataset for us to delete on request beyond answering your email questions.

## Changes to This Policy

We may update this Privacy Policy from time to time. The “Last updated” date at the top will change, and the revised policy will be posted on this Privacy Policy page.

## Contact Us

If you have questions about this Privacy Policy or privacy practices:

- **Email:** [AppleOSer@gmail.com](mailto:AppleOSer@gmail.com)

We typically respond within 48 hours.

</section>
