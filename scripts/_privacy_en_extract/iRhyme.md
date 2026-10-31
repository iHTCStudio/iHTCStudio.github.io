**Last updated:** September 3, 2026

iHTC Studio ("we", "us" or "our") built **iRhyme** (also known as "爱声律启蒙 / 愛聲律啟蒙", Bundle ID `com.iHTCboy.iRhyme`). This Privacy Policy explains what data is (and is not) handled when you use the app. **Apple App Review** and users may rely on **this page** as the public privacy policy for the app. For App Store Connect, open this Privacy Policy in your browser and copy the address from the address bar (the public site domain may change over time).

## Summary (Apple Privacy Nutrition Label alignment)

| Topic | Our practice |
|-------|----------------|
| Account | **Not required** — no registration, email sign-in, or phone number |
| Data collection by iHTC Studio | **Data Not Collected** — we do **not** operate a backend that receives your personal data |
| Network | Library, reading, recite, Rhyme Academy, widgets, and daily notifications work **offline** after install |
| Analytics / ads / tracking | **None** — no third-party analytics, advertising, or tracking SDKs; no App Tracking Transparency use |
| Optional Apple services | **iCloud** (your private KVS), **Photo Library (Add Only)** for rhyme cards, **StoreKit** for optional tipping, **local notifications**, optional **Live Activities**, optional **on-device handwriting** (Vision) |

## Data Collection

We do **not** collect, sell, or share personal information for advertising or analytics.

- **No account** — You can use all core features without creating an account with us.
- **No analytics or ads** — The app binary does not integrate third-party analytics, advertising, or crash-reporting SDKs that phone home to us.
- **No content upload** — Your reading history, favorites, lists, notes, study progress, and preferences stay on your device (and optionally in **your** iCloud). They are never uploaded to iHTC Studio servers because **we do not run such servers for this app**.

## How the App Works

- **Bundled library** — Text JSON, vernacular/English, indexes, and study aids ship inside the app / widget bundle. Browsing and study do not require a network request.
- **On-device speech** — Recitation uses Apple’s system **AVSpeechSynthesizer** (TTS). We do not send passage text to iHTC Studio.
- **Widgets & App Group** — Widgets and the app share preferences and lightweight state via App Group `group.com.iHTCboy.iRhyme` on your device.
- **Daily notifications** — Scheduled locally with User Notifications. Tapping a notification opens a deep link to a passage ID on device; no server fan-out.
- **Rhyme cards** — Images are rendered on device. Saving uses **Photo Library add-only** only when you tap save. System Share Sheet may send the image to an app **you** choose; that destination’s privacy policy then applies.
- **Handwriting search (iOS)** — Optional character recognition uses Apple **Vision** on device. Strokes are not uploaded.
- **Optional tip** — “Tip Developer” is a consumable **StoreKit** purchase processed by Apple. We do not receive your payment card details.
- **Siri / Shortcuts / Control Center** — Optional system integrations open on-device deep links; they do not send your library to us.
- **Optional Spotlight** — If you enable indexing, content is indexed by the system on device for local search; we do not operate a search backend.

## Data Stored on Your Device

| Data | Where | Purpose |
|------|-------|---------|
| Rhyme database | App / Widget bundle | Offline reading & study |
| Favorites & lists (韵单) | App Group UserDefaults | Starred passages and user lists |
| Reading history / last read | App Group UserDefaults | Continue reading, history UI |
| Notes | App Group UserDefaults | Reading notes you write |
| Study progress & mastery | App Group UserDefaults | Rhyme Academy state, quiz / Hunt progress |
| Practice streak / check-in | App Group UserDefaults | Daily habit |
| Appearance & reading prefs | App Group UserDefaults | Theme, accent, language, layout, TTS, tabs, widgets, font scale |
| Today’s Rhyme cache & notification prefs | App Group UserDefaults | Today’s ID, schedule time, contextual toggle |
| Card preferences | App Group UserDefaults | Last style / ratio choices |
| Onboarding & TipKit state | Standard UserDefaults (device) | Welcome guide / discovery tips |
| Recent searches | Standard UserDefaults (device) | Search history you typed |
| Home Screen quick actions | System + local prefs | Shortcuts you configure |
| Widget / Live Activity snapshots | App Group / ActivityKit | Display text you already opened |

Uninstalling the app removes sandbox and App Group data associated with the app (subject to iOS/macOS behavior). Optional iCloud copies remain in **your** iCloud until you clear them or turn sync off and delete elsewhere.

## iCloud Sync (Optional)

If you enable **iCloud Sync** in Settings, the app mirrors selected user data through Apple’s **`NSUbiquitousKeyValueStore`** tied to **your Apple ID**:

- Favorites
- Lists (韵单)
- Reading history
- Study progress / mastery
- Practice streaks
- Notes

Sync traffic goes to **Apple iCloud**, not to iHTC Studio. You can disable sync in Settings. We cannot read your iCloud contents.

## Permissions

iRhyme requests permissions only when a feature needs them:

| Permission | When | Why |
|------------|------|-----|
| Notifications | You enable Today’s Rhyme reminders | Local scheduling of reminder notifications |
| Photo Library (Add Only) | You save a card | Write the rendered image; we do not need full library read access |
| iCloud | You enable sync | Sync favorites / lists / history / progress / streaks / notes |
| Live Activities (iOS) | You enable Reading Live Activity | Show the passage you are reading on Lock Screen / Dynamic Island |
| Background audio (capability) | You enable background recitation | Continue TTS when the app is not foreground |

We do **not** request Contacts, precise Location, Camera, Microphone (beyond system TTS playback), or Tracking. Handwriting search uses on-device Vision and does not require a network permission prompt.

## What We Do Not Do

- We do **not** sell personal data.
- We do **not** build advertising profiles.
- We do **not** require an account or social login.
- We do **not** embed third-party ad, analytics, or social SDKs for data collection.
- We do **not** access your Photo Library beyond **add-only** when you choose to save a card.
- We do **not** receive StoreKit payment card numbers (Apple processes payments).
- We do **not** upload handwriting strokes or passage text to iHTC Studio.

## Children’s Privacy

iRhyme is an educational literacy app for a general audience and is **not** in the Kids Category. We do not knowingly collect personal information from children. The app does not require an account. Families may use reading and study features offline on their own devices.

## Third Parties

- **Apple** — App Store distribution, optional StoreKit purchases, optional iCloud KVS, system TTS, Share Sheet destinations you pick, and OS-level notification / Live Activity / Siri / Shortcuts / Vision delivery.
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
