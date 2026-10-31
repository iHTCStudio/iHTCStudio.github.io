**Last updated:** September 19, 2026

iHTC Studio ("we", "us" or "our") built **iZengZi** (also known as "爱曾子 / 愛曾子", Bundle ID `com.iHTCboy.iZengZi`). This Privacy Policy explains what data is (and is not) handled when you use the app. **Apple App Review** and users may rely on **this page** as the public privacy policy. For App Store Connect, open this Privacy Policy in your browser and copy the address from the address bar (the public site domain may change over time).

## Summary (Apple Privacy Nutrition Label alignment)

| Topic | Our practice |
|-------|----------------|
| Account | **Not required** — no registration, email sign-in, or phone number |
| Data collection by iHTC Studio | **Data Not Collected** — we do **not** operate a backend that receives your personal data |
| Network | Library, reading, recite, Cultivation Hall, widgets, and daily notifications work **offline** after install |
| Analytics / ads / tracking | **None** — no third-party analytics, advertising, or tracking SDKs; no App Tracking Transparency use |
| Optional Apple services | **iCloud** (your private KVS), **Photo Library (Add Only)** for study cards, **StoreKit** for optional tipping, **local notifications**, optional **Live Activities**, optional on-device **handwriting** (Vision), optional **HealthKit** mood write (off by default) |

## Data Collection

We do **not** collect, sell, or share personal information for advertising or analytics.

- **No account** — You can use all core features without creating an account with us.
- **No analytics or ads** — The app binary does not integrate third-party analytics, advertising, or crash-reporting SDKs that phone home to us.
- **No content upload** — Your reading history, favorites, lists, notes, study progress, and preferences stay on your device (and optionally in **your** iCloud). They are never uploaded to iHTC Studio servers because **we do not run such servers for this app**.

The **three-question journal** is a private cultivation note on this device. Optional **HealthKit** mood write (iOS 18+) is **off by default**, asked only from journal settings, writes only to **your** Health app, and is **not** a mental-health product or diagnosis.

## How the App Works

- **Bundled library** — Text JSON, vernacular/English, indexes, and study aids ship inside the app / widget bundle.
- **On-device speech** — Recitation uses Apple’s system **AVSpeechSynthesizer** (TTS). We do not send passage text to iHTC Studio.
- **Widgets & App Group** — Widgets and the app share preferences via App Group `group.com.iHTCboy.iZengZi` on your device.
- **Daily notifications** — Scheduled locally. Tapping a notification opens a deep link on device.
- **Study cards** — Images are rendered on device. Saving uses **Photo Library add-only** only when you tap save.
- **Handwriting search (iOS)** — Optional character recognition uses Apple **Vision** on device. Strokes are not uploaded.
- **Optional tip** — “Tip Developer” is a consumable **StoreKit** purchase processed by Apple.
- **Siri / Shortcuts / Control Center** — Optional system integrations open on-device deep links.
- **Optional Spotlight** — If you enable indexing, the system indexes content on device.

## Data Stored on Your Device

| Data | Where | Purpose |
|------|-------|---------|
| Zengzi-line library | App / Widget bundle | Offline reading & study |
| Favorites & lists | App Group UserDefaults | Starred items and user lists |
| Reading history / last read | App Group UserDefaults | Continue reading |
| Notes | App Group UserDefaults | Reading notes you write |
| Study progress & mastery | App Group UserDefaults | Classroom / Hunt progress |
| Streak / check-in | App Group UserDefaults | Daily habit |
| Appearance & reading prefs | App Group UserDefaults | Theme, language, TTS, widgets |
| Daily Reflection cache & notification prefs | App Group UserDefaults | Today’s ID and schedule |
| Card preferences | App Group UserDefaults | Last style / ratio |
| Onboarding & TipKit state | Standard UserDefaults | Welcome guide |
| Widget / Live Activity snapshots | App Group / ActivityKit | Display text you already opened |

Uninstalling the app removes sandbox and App Group data (subject to OS behavior). Optional iCloud copies remain in **your** iCloud until you clear them.

## iCloud Sync (Optional)

If you enable **iCloud Sync** in Settings, the app mirrors selected user data through Apple’s **`NSUbiquitousKeyValueStore`** tied to **your Apple ID**:

- Favorites
- Lists
- Reading history
- Study progress / mastery
- Practice streaks
- Notes
- Three-question journal entries

Sync traffic goes to **Apple iCloud**, not to iHTC Studio. We cannot read your iCloud contents.

## Permissions

iZengZi requests permissions only when a feature needs them:

| Permission | When | Why |
|------------|------|-----|
| Notifications | You enable Daily Reflection reminders | Local scheduling |
| Photo Library (Add Only) | You save a card | Write the rendered image |
| iCloud | You enable sync | Sync favorites / lists / history / progress / notes |
| Live Activities (iOS) | You enable Reading Live Activity | Show the passage on Lock Screen / Dynamic Island |
| Background audio (capability) | You enable background recitation | Continue TTS in background |
| Health (Mood) | You enable journal sync in Settings | Write today’s three-axis mark to **your** Health app; never on first launch |

We do **not** request Contacts, precise Location, Camera, Microphone (beyond system TTS playback), or Tracking.
- Optional HealthKit mood write is **off by default** and never requested at first launch.

## What We Do Not Do

- We do **not** sell personal data.
- We do **not** build advertising profiles.
- We do **not** require an account or social login.
- We do **not** embed third-party ad, analytics, or social SDKs for data collection.
- We do **not** access your Photo Library beyond **add-only** when you choose to save a card.
- We do **not** receive StoreKit payment card numbers (Apple processes payments).

## Children’s Privacy

iZengZi is an educational literacy app for a general audience and is **not** in the Kids Category. We do not knowingly collect personal information from children. Families may use reading and study features offline on their own devices.

## Third Parties

- **Apple** — App Store distribution, optional StoreKit, optional iCloud KVS, system TTS, Share Sheet destinations you pick, and OS-level notification / Live Activity / Siri / Shortcuts / Vision / HealthKit delivery.
- **No other third-party SDKs** for ads, analytics, or social login are included for data collection.

## International Users

The app is designed to function offline on your device. Optional Apple services follow Apple’s terms and regional availability.

## Data Retention & Deletion

- **On device** — Delete the app to remove local sandbox and App Group data (subject to OS behavior).
- **iCloud** — Turn off sync and clear related keys from your iCloud account as needed; we cannot erase your iCloud for you.
- **We retain nothing** on iHTC Studio servers for this app because we do not collect it.

## Policy Changes

We may update this Privacy Policy. The “Last updated” date at the top will change. Continued use after an update means you accept the revised policy.

## Contact

Questions about privacy: [AppleOSer@gmail.com](mailto:AppleOSer@gmail.com)

</section>
