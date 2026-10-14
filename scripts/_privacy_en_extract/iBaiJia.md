**Last updated:** August 18, 2026

iHTC Studio ("we", "us" or "our") built **iBaiJia** (also known as "爱百家姓" / "愛百家姓", Bundle ID `com.iHTCboy.iBaiJia`). This Privacy Policy explains what data is (and is not) handled when you use the app. **Apple App Review** and users may rely on **this page** as the public privacy policy for the app. For App Store Connect, open this Privacy Policy in your browser and copy the address from the address bar (the public site domain may change over time).

## Summary (Apple Privacy Nutrition Label alignment)

| Topic | Our practice |
|-------|----------------|
| Account | **Not required** — no registration, email sign-in, or phone number |
| Data collection by iHTC Studio | **Data Not Collected** — we do **not** operate a backend that receives your personal data |
| Network | Surname library, detail reading, recite, Study Hall, naming inspiration, widgets, and daily notifications work **offline** after install |
| Analytics / ads / tracking | **None** — no third-party analytics, advertising, or tracking SDKs; no App Tracking Transparency use |
| Optional Apple services | **iCloud** (your private KVS), **Photo Library (Add Only)** for share cards, **StoreKit** for optional tipping, **local notifications**, optional **Live Activities**, optional **Spotlight** (off by default), optional **system speech / translation** |

## Data Collection

We do **not** collect, sell, or share personal information for advertising or analytics.

- **No account** — You can use all core features without creating an account with us.
- **No analytics or ads** — The app binary does not integrate third-party analytics, advertising, or crash-reporting SDKs that phone home to us.
- **No content upload** — Your favorites, surname lists, notes, reading history, study progress, streaks, naming preferences, and settings stay on your device (and optionally in **your** iCloud). They are never uploaded to iHTC Studio servers because **we do not run such servers for this app**.

## How the App Works

- **Bundled library** — Surname JSON, English glosses, stroke-order glyphs, and indexes ship inside the app / widget bundle. Browsing and study do not require a network request.
- **On-device speech** — Reading and recitation use Apple’s system **AVSpeechSynthesizer** (TTS). We do not send surname text to iHTC Studio.
- **Optional system translation** — If you long-press detail text and use Apple’s system Translation (iOS 17.4 / macOS 14.4+), processing stays with Apple’s OS. We do not operate a translation backend.
- **Naming inspiration** — Generated entirely on device from bundled data. No names or preferences are uploaded.
- **Widgets & App Group** — Widgets and the app share preferences and lightweight state via App Group `group.com.iHTCboy.iBaiJia` on your device.
- **Daily notifications** — Scheduled locally with User Notifications. Tapping a notification opens a deep link on device; no server fan-out.
- **Share cards** — Images are rendered on device. Saving uses **Photo Library add-only** only when you tap save. System Share Sheet may send the image to an app **you** choose; that destination’s privacy policy then applies.
- **Optional tip** — “Tip Developer” (`com.iHTCboy.iBaiJia.6`) is a consumable **StoreKit** purchase processed by Apple. We do not receive your payment card details.
- **Siri / Shortcuts / Control Center** — Optional system integrations open on-device deep links; they do not send your library to us.
- **Optional Spotlight** — Off by default. If you enable indexing, surnames are indexed by the system on device for local search; we do not operate a search backend.
- **Feedback email** — If you send Feedback, the message may include text you write plus device / app diagnostics (version, OS, language) solely for troubleshooting.

## Data Stored on Your Device

| Data | Where | Purpose |
|------|-------|---------|
| Surname database & stroke glyphs | App bundle | Offline reading, tracing & study |
| Favorites & surname lists | App Group UserDefaults | Starred surnames and user lists |
| Notes | App Group UserDefaults | Surname notes you write |
| My Surname | App Group UserDefaults | Personalized home & widgets |
| Reading history / last read | App Group UserDefaults | Continue browsing, history UI |
| Study progress & high scores | App Group UserDefaults | Study Hall state |
| Check-in streak | App Group UserDefaults | Daily habit |
| Appearance & reading prefs | App Group UserDefaults | Theme, accent, language, layout, TTS, tabs, widgets |
| Daily Surname cache & notification prefs | App Group UserDefaults | Today’s ID, schedule time |
| Share-card preferences | App Group UserDefaults | Last style choices |
| Onboarding & TipKit state | Standard UserDefaults (device) | Welcome guide / discovery tips |
| Home Screen quick actions | System + local prefs | Shortcuts you configure |
| Widget / Live Activity snapshots | App Group / ActivityKit | Display text you already opened |

Uninstalling the app removes sandbox and App Group data associated with the app (subject to iOS/macOS behavior). Optional iCloud copies remain in **your** iCloud until you clear them or turn sync off and delete elsewhere.

## iCloud Sync (Optional)

If you enable **iCloud Sync** in Settings, the app mirrors selected user data through Apple’s **`NSUbiquitousKeyValueStore`** tied to **your Apple ID**:

- Favorites
- Surname lists
- Notes
- Reading history
- Study progress / high scores
- Check-in streaks
- Related preferences

Sync traffic goes to **Apple iCloud**, not to iHTC Studio. You can disable sync in Settings. We cannot read your iCloud contents.

## Permissions

iBaiJia requests permissions only when a feature needs them:

| Permission | When | Why |
|------------|------|-----|
| Notifications | You enable Daily Surname reminders | Local scheduling |
| Photo Library (Add Only) | You save a share card | Write the rendered image |
| iCloud | You enable sync | Sync favorites / lists / history / progress / streaks / notes |
| Live Activities (iOS) | You enable Reading Live Activity | Lock Screen / Dynamic Island |
| Background audio (iOS) | You enable background recitation | Continue TTS in background |

We do **not** request Contacts, precise Location, Camera, Microphone (beyond system TTS playback), or Tracking.

## Children’s Privacy

iBaiJia is a cultural learning app for a general audience and is **not** in the Kids Category. We do not knowingly collect personal information from children. The app does not require an account. Families may use reading and study features offline on their own devices.

## Third Parties

The only third-party services involved in normal use are **Apple** (App Store, iCloud, StoreKit, system TTS, optional system translation, notifications, Live Activities, Spotlight). Surname datasets include open-licensed English glosses (CC BY 4.0) and stroke-order glyphs (LGPL / Arphic Public License) — see the in-app About page for attribution. Cultural commentary in the app is original study material marked for reference.

## Data Retention & Deletion

- **On device:** You can clear study progress, history, or notes in the app. Settings supports export/import for backup. Delete the app to remove local sandbox and App Group data (subject to system behavior).
- **iCloud:** Disable sync in Settings; you may also manage iCloud storage in system Settings.
- **We do not retain copies** of your reading, notes, or favorites on iHTC Studio servers.

## Changes to This Policy

We may update this page for legal, product, or App Store compliance reasons. The “Last updated” date will change. Continued use after an update means you accept the revised policy.

## Contact

Questions about privacy: [AppleOSer@gmail.com](mailto:AppleOSer@gmail.com)

</section>
