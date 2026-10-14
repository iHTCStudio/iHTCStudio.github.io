**Last updated:** August 18, 2026

iHTC Studio ("we", "us" or "our") built **iThousand** (also known as "爱千字文" / "愛千字文", Bundle ID `com.iHTCboy.iThousand`). This Privacy Policy explains what data is (and is not) handled when you use the app. **Apple App Review** and users may rely on **this page** as the public privacy policy for the app. For App Store Connect, open this Privacy Policy in your browser and copy the address from the address bar (the public site domain may change over time).

## Summary (Apple Privacy Nutrition Label alignment)

| Topic | Our practice |
|-------|----------------|
| Account | **Not required** — no registration, email sign-in, or phone number |
| Data collection by iHTC Studio | **Data Not Collected** — we do **not** operate a backend that receives your personal data |
| Network | Library, character cards, reading, recite, Primer Hall, Hunt, widgets, and daily notifications work **offline** after install |
| Analytics / ads / tracking | **None** — no third-party analytics, advertising, or tracking SDKs; no App Tracking Transparency use |
| Optional Apple services | **iCloud** (your private KVS), **Photo Library (Add Only)** for share cards, **StoreKit** for optional tipping, **local notifications**, optional **Live Activities**, optional **Spotlight** (off by default), optional **system speech / translation** |

## Data Collection

We do **not** collect, sell, or share personal information for advertising or analytics.

- **No account** — You can use all core features without creating an account with us.
- **No analytics or ads** — The app binary does not integrate third-party analytics, advertising, or crash-reporting SDKs that phone home to us.
- **No content upload** — Your reading history, favorites, lists (千单), saved characters, notes, study progress, streaks, and preferences stay on your device (and optionally in **your** iCloud). They are never uploaded to iHTC Studio servers because **we do not run such servers for this app**.

## How the App Works

- **Bundled library** — Passage JSON, vernacular/English, pinyin, character cards, stroke-order data, and indexes ship inside the app / widget bundle (curated from public web sources). Browsing and study do not require a network request.
- **On-device speech** — Recitation uses Apple’s system **AVSpeechSynthesizer** (TTS). We do not send passage text to iHTC Studio.
- **Optional system translation** — If you use Apple’s on-device / system translation features, processing stays with Apple’s OS. We do not operate a translation backend.
- **Widgets & App Group** — Widgets and the app share preferences and lightweight state via App Group `group.com.iHTCboy.iThousand` on your device.
- **Daily notifications** — Scheduled locally with User Notifications. Tapping a notification opens a deep link to a passage ID on device; no server fan-out.
- **Share cards** — Images are rendered on device. Saving uses **Photo Library add-only** only when you tap save. System Share Sheet may send the image to an app **you** choose; that destination’s privacy policy then applies.
- **Optional tip** — “Tip Developer” (`com.iHTCboy.iThousand.6`) is a consumable **StoreKit** purchase processed by Apple. We do not receive your payment card details.
- **Siri / Shortcuts / Control Center** — Optional system integrations open on-device deep links; they do not send your library to us.
- **Optional Spotlight** — Off by default. If you enable indexing, passages and character cards are indexed by the system on device for local search; we do not operate a search backend.
- **Feedback email** — If you send Feedback, the message may include text you write plus device / app diagnostics (version, OS, language) solely for troubleshooting.

## Data Stored on Your Device

| Data | Where | Purpose |
|------|-------|---------|
| Passage & character database | App / Widget bundle | Offline reading, literacy cards & study |
| Favorites & lists (千单) | App Group UserDefaults | Starred passages and user lists |
| Saved characters & famous-line favorites | App Group UserDefaults | Hard-character bookmarks, starred lines |
| Reading history / last read | App Group UserDefaults | Continue reading, history UI |
| Study progress & mastery | App Group UserDefaults | Primer Hall state, quiz / Hunt progress |
| Notes | App Group UserDefaults | Passage notes you write |
| Study streak / check-in | App Group UserDefaults | Daily habit |
| Appearance & reading prefs | App Group UserDefaults | Theme, accent, language, layout, TTS, tabs, widgets, font scale |
| Daily Line cache & notification prefs | App Group UserDefaults | Today’s ID, schedule time, contextual toggle |
| Share-card preferences | App Group UserDefaults | Last style / ratio choices |
| Onboarding & TipKit state | Standard UserDefaults (device) | Welcome guide / discovery tips |
| Home Screen quick actions | System + local prefs | Shortcuts you configure |
| Widget / Live Activity snapshots | App Group / ActivityKit | Display text you already opened |

Uninstalling the app removes sandbox and App Group data associated with the app (subject to iOS/macOS behavior). Optional iCloud copies remain in **your** iCloud until you clear them or turn sync off and delete elsewhere.

## iCloud Sync (Optional)

If you enable **iCloud Sync** in Settings, the app mirrors selected user data through Apple’s **`NSUbiquitousKeyValueStore`** tied to **your Apple ID**:

- Favorites
- Lists (千单)
- Saved characters / famous-line favorites
- Reading history
- Study progress / mastery
- Study streaks
- Notes

Sync traffic goes to **Apple iCloud**, not to iHTC Studio. You can disable sync in Settings. We cannot read your iCloud contents.

## Permissions

iThousand requests permissions only when a feature needs them:

| Permission | When | Why |
|------------|------|-----|
| Notifications | You enable Daily Line reminders | Local scheduling |
| Photo Library (Add Only) | You save a share card or character image | Write the rendered image |
| iCloud | You enable sync | Sync favorites / lists / history / progress / streaks / notes / saved characters |
| Live Activities (iOS) | You enable Reading Live Activity | Lock Screen / Dynamic Island |
| Background audio | You enable background recitation | Continue TTS in background |

We do **not** request Contacts, precise Location, Camera, Microphone (beyond system TTS playback), or Tracking.

## Children’s Privacy

iThousand is an educational literacy app for a general audience and is **not** in the Kids Category. We do not knowingly collect personal information from children. The app does not require an account. Families may use reading and character-card features offline on their own devices.

## Third Parties

The only third-party services involved in normal use are **Apple** (App Store, iCloud, StoreKit, system TTS, optional system translation, notifications, Live Activities, Spotlight).

## Data Retention & Deletion

- **On device:** You can clear study progress, history, or notes in the app. Delete the app to remove local sandbox and App Group data (subject to system behavior).
- **iCloud:** Disable sync in Settings; you may also manage iCloud storage in system Settings.
- **We do not retain copies** of your reading, notes, or character bookmarks on iHTC Studio servers.

## Changes to This Policy

We may update this page for legal, product, or App Store compliance reasons. The “Last updated” date will change. Continued use after an update means you accept the revised policy.

## Contact

Questions about privacy: [AppleOSer@gmail.com](mailto:AppleOSer@gmail.com)

</section>
