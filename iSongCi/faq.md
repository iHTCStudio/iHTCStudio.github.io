---
layout: doc
title: iSongCi — FAQ
app_id: iSongCi
doc_title_en: Frequently Asked Questions
doc_title_zh_cn: 常见问题
doc_title_zh_tw: 常見問題
description: Comprehensive FAQ for iSongCi — offline Song Ci, daily ci, reading, widgets, Siri and iCloud.
---

<section lang="en" markdown="1">

### Is the app fully offline?

Yes. All **21,592 Song Ci works** are bundled. After install the app makes **zero outbound network requests** — no account, no ads, no analytics. Optional iCloud uses Apple's service only when you enable it.

### How is this different from Tang poetry / generic poetry apps?

iSongCi is **vertical to Song Ci (宋词)** — not a mixed Tang/Song/Yuan poetry catalog. It adds **1,461 cipai** knowledge, **plain translation & modern commentary**, **immersive vertical reading** with pinyin, daily ci, share cards, widgets, Control Center, Siri, and optional iCloud.

### How much content is included?

| Item | Count |
|------|-------|
| Ci works (total) | 21,592 |
| Authors | 1,509 |
| Cipai (tune patterns) | 1,461 |
| Featured cipai with intro | 60 |
| Plain translations | 11,029 |
| Modern commentary | All works |
| Collections | 12 (Haofang 363 · Wanyue 520 · 10 theme sets) |
| Dynasties | Five Dynasties, Northern Song, Southern Song |

### What are plain translation, classical notes, and modern commentary?

Three separate layers on the detail page — toggle each section independently:

- **Plain translation (白话译文)** — modern Chinese rendering of the full text (~11,029 works)
- **Classical notes (注释)** — traditional scholarly annotations where available
- **Modern commentary (白话赏析)** — auto-generated background, gist, and reading tips for every work (for reference, not academic citation)

### Do all works have translations?

No. **11,029** works include a full plain translation; the rest show original text plus modern commentary. Classical notes appear only when source data includes them. The app is a reading & discovery studio, not a full academic edition of every ci.

### How does Today's Ci work?

A piece is chosen **deterministically from the featured pool** (Haofang + Wanyue masterpieces) using the **calendar day as seed** — everyone sees the **same ci on the same date**. It rolls over at **local midnight**. Open from **Home** or `isongci://daily`.

### What is Serendipity?

**邂逅一词** draws a **random** piece from the featured pool — different each tap. Use **Home → Serendipity**, `isongci://random`, the **Random Ci** widget, or Siri.

### How accurate is pinyin?

Pinyin is **auto-generated** per segment. It works well for most lines but **may misread polyphonic characters** (多音字). Use it as a reading aid, not a pronunciation authority.

### Traditional Chinese display?

UI has dedicated **繁體中文** strings. Corpus text is stored in simplified Chinese and **converted at display time** (character-level s2t table) for Traditional mode — you don't need two copies of the database.

### How do vertical reading and pinyin work?

Turn on globally in **Settings → Reading** (vertical layout, pinyin, calligraphy font). In any work detail you can open **Immersive Reading** for a full-screen vertical (right-to-left) or horizontal page with xuan-paper background and independent font scaling.

### What is Immersive Reading?

**Detail → More → Immersive Reading** opens a chrome-free page — ideal for reciting or presenting on iPad or a large screen. Switch vertical/horizontal and calligraphy inside the reader.

### How do I change font size?

**Settings → Reading** slider, or **Detail → More → Font size**. Scales body text independently of system Dynamic Type; syncs via iCloud if enabled.

### How does read-aloud (TTS) work?

Tap the **speaker** icon on the detail toolbar. Uses on-device Mandarin speech synthesis. Pause and resume with the same button.

### How do favorites, notes, and iCloud work?

**Favorites** — tap ♥ on any work. **Private notes** — per-poem annotations only you can see (detail page). Optional **iCloud Sync** mirrors favorites, notes, appearance, font scale, tab visibility, and reading streak across devices. **Ci text is never uploaded** — it always stays in the app bundle.

### What are the reading streak rules?

Open **any ci** in the app to count for that calendar day. **Consecutive days** increment your streak; **skip more than one day** and the streak resets to zero on next open. **Total read count** tracks lifetime pieces opened. Streak appears on Home and the **Reading Streak** widget.

### What share card styles exist?

**13 styles:** Classic, Ink Wash, Cinnabar Seal, Silk Scroll, Scroll Long, Ochre Gold, Winter Snow, Green Landscape, Bamboo Slips, Moonlit Silver, Minimal, Dark Minimal, Vertical Script. Choose full text or excerpt; optionally include commentary; export PNG at 3× resolution.

### Which widgets are available?

| Widget | Purpose |
|--------|---------|
| Today's Ci | Today's highlighted piece |
| Serendipity | Random featured ci (refreshes hourly) |
| Favorite Ci | Latest starred work |
| Reading Streak | Consecutive days + total read count |
| Control Center | One-tap open Today's Ci (iOS 18+) |

Sizes: Small / Medium / Large on Home Screen; Lock Screen circular, inline, or rectangular. Supports **StandBy**. Widget language follows **in-app language**, not system language.

### Widget shows wrong or empty text?

1. Open the app once after install
2. Pull to refresh on Home to rewrite widget cache
3. After changing language, open the app briefly to refresh
4. **Favorite Ci** needs at least one starred work
5. **Reading Streak** needs you to open a work inside the app first
6. Ensure widgets are allowed for iSongCi in system settings

### What is the Control Center widget (iOS 18+)?

Add **Today's Ci** from **Settings → Control Center** (or system Control Center editor). Requires **iOS 18.0+**. Tapping opens the app directly to today's piece.

### What Siri shortcuts exist?

Three App Intents ship with the app:

| Intent | Example phrase |
|--------|----------------|
| Open Today's Ci | "Today's ci in iSongCi" |
| Random Ci | "Serendipity in iSongCi" |
| Search Ci | "Search in iSongCi" (with keyword) |

Configure up to **4 Home Screen quick actions** in Settings. Full deep-link list in [Shortcut Links](url-scheme).

### What are Spotlight limitations?

Spotlight indexes the **featured pool plus your favorites** — up to **~1,000** entries. Rare works won't appear in system search; use **in-app deep full-text search** instead (lazy-loads the full corpus). Tap a Spotlight result to open that ci directly.

### Can I hide tabs?

Yes. **Settings → Tab Bar** — toggle **Categories** and/or **Favorites** tabs. Hidden tabs remain reachable via detail actions, long-press menus, widgets, and `isongci://` links.




|---------|---------------|------------------|
| Home Screen quick actions | ✅ | ❌ |
| Widgets & Control Center | ✅ (iOS 18+ CC) | Widgets primarily on iPhone/iPad |
| Haptic feedback | ✅ | ❌ |
| Dedicated Search tab | iOS 26+ | Search via button / sheet |
| Core reading, favorites, iCloud | ✅ | ✅ |

### Is the app free? What is the tip jar?

**Completely free** — all 21,592 works and every feature, no subscription, no ads. An **optional tip jar** (`com.iHTCboy.iSongCi.6`) lets you support development via Apple In-App Purchase; it unlocks nothing extra.

### System requirements

| Platform | Minimum |
|----------|---------|
| iPhone / iPad | iOS 17.0+ |
| Mac | macOS 13.0+ |
| Control Center widget | iOS 18.0+ |
| System translation panel | iOS 17.4+ / macOS 14.4+ |

### How do I get the app?

[Download on the App Store](https://apps.apple.com/app/id6788433450) (App ID **6788433450**).

### How do I contact support?

[AppleOSer@gmail.com](mailto:AppleOSer@gmail.com) — we typically reply within 48 hours.

---

### How does continuous reading work?

Enable **continuous reading** in Settings → Reading. After a work finishes TTS, a bottom bar appears; if you do nothing for a few seconds, the next item in the current queue (browse / playlist / favorites / daily) starts automatically. You can also pick lines when generating share cards.

### How do daily reminders work?

Optional **local notifications** remind you to read today's ci. Tap the notification to open the matching work via deep link. Disabling notifications does not clear your reading streak.

## Complete User Guide

The sections below are the full product walkthrough previously on the support page. Quick Q&A items remain above (if any).

---

## Part 1 — First Launch & Interface

### Welcome guide

On first launch, a **multi-page welcome guide** introduces the app — library scale, daily ci, immersive reading, favorites, widgets, and privacy. Swipe through each page, then tap **Get Started**. Replay anytime: **Settings → Help → Usage Guide** or deep link `isongci://feature-guide`.

### Tab bar overview

| Tab | What it does |
|-----|----------------|
| **Home** | Today's Ci, Serendipity, Continue Reading, reading streak, themed previews |
| **Browse** | Authors, cipai, dynasties, genres, theme collections, full catalog |
| **Favorites** | Starred works with list / grid / card layouts and grouping |
| **Settings** | Appearance, reading, data, tabs, widgets, shortcuts, help |
| **Search** | Instant metadata search + lazy full-text deep search (dedicated tab on **iOS 26+**) |

> **Tip:** Hide the **Browse** or **Favorites** tab in **Settings → Tab Bar**. If you close the tab you're on, the app returns to Home automatically. Tab visibility syncs via optional iCloud.

### Platforms

| Platform | Minimum |
|----------|---------|
| iPhone / iPad | iOS 17.0+ |
| Mac | macOS 13.0+ |

Dedicated **Search tab** requires **iOS 26+**. On earlier iOS versions, search is available from the Browse page or via Spotlight / Siri.

### Privacy at install

- **No sign-up · no ads · no analytics SDK**
- Corpus ships inside the app bundle — no CDN, no telemetry
- Optional iCloud uses **your private iCloud** only; ci text is never uploaded

---

## Part 2 — Home

The **Home** tab is your daily entry point — curated discovery without hunting through 21,592 works.

### Today's Ci (每日一词)

A **deterministic daily pick** — the same ci for everyone on the same calendar date, chosen from the full library by a date-based algorithm. Tap the card to open the full detail page.

- Refreshes automatically at **local midnight**
- Written to **App Group** storage when the app launches so **Daily Ci** widgets stay in sync
- Deep link: `isongci://daily`
- Siri: *"Today's ci in iSongCi"*

### Serendipity (邂逅一词)

Tap **Serendipity** for a **random curated ci** — great when you want surprise rather than today's fixed pick. Each tap draws a new piece from the offline library.

- Deep link: `isongci://random`
- Siri: *"Serendipity in iSongCi"*

### Continue Reading

If you recently opened a work, **Continue Reading** appears on Home with the title and author. One tap resumes where you left off.

- Deep link: `isongci://continue-reading`
- Also available as a Home Screen quick action

### Reading streak

Home shows your **reading streak** — consecutive days you've read at least one ci, plus a cumulative read count. Opening any work detail counts toward today's streak.

- Synced via optional **iCloud KVS**
- **Streak** widget shows streak on Home Screen and Lock Screen

### Themed previews

Scroll down for quick entry cards — **featured cipai**, **theme collections**, **豪放 / 婉约** genres, and **dynasty** highlights. Tap **View All** to jump into Browse at that section.

### Home Screen quick actions

Long-press the app icon for shortcuts like **Today's Ci**, **Serendipity**, **Continue Reading**, **Favorites**, and **Search**. Customize up to **4** items in **Settings → Shortcuts → Home Screen Quick Actions** (15 actions available — see Part 10).

---

## Part 3 — Browse

Open the **Browse** tab. Multiple sections let you explore the library from different angles:

### 1. Authors (名家)

**1,509 Song Ci poets** with biographies. Tap an author for their profile and full work list.

- Switch layout via **⋯**: **List**, **Grid**, or **Cards**
- Grid column count (2–4) remembered separately on iPhone and iPad
- Deep link: `isongci://author?id=12`

### 2. Cipai (词牌)

**1,461 cipai** tune patterns in the full index. **60 featured cipai** include introductory essays explaining form, rhythm, and representative mood — learn the pattern, then browse works written to that tune.

Examples: 水调歌头, 念奴娇, 满江红, 蝶恋花, 浣溪沙.

### 3. Dynasties (朝代)

Browse by historical period:

| Dynasty | Coverage |
|---------|----------|
| **五代** | Early *ci* tradition before the Song |
| **北宋** | Northern Song masters |
| **南宋** | Southern Song lyricists |

### 4. Genres (流派)

| Genre | Count | Character |
|-------|-------|-----------|
| **豪放** | 363 | Bold, expansive, heroic tone |
| **婉约** | 520 | Delicate, lyrical, intimate tone |

Works may appear in one or both groupings where applicable.

### 5. Theme collections (主题)

**10 curated theme collections** — love, parting, nostalgia, nature, patriotism, philosophy, festivals, and more. Each collection groups ci that share a motif.

### 6. Full catalog (全集)

The complete **21,592-work** index. Use when you want everything in one scrollable list with sort and filter options.

### Layout & section options

Tap **⋯** on Browse or Author pages:

| Option | What it does |
|--------|----------------|
| **Layout** | List / Grid / Cards |
| **Section visibility** | Show or hide any browse section |
| **Section order** | Reorder how sections appear |
| **Grid columns** | 2–4 on iPhone, 2–4 on iPad (remembered separately) |

### Search entry (pre–iOS 26)

On iOS 17–25, open search from the **search field** at the top of Browse or via Spotlight / Siri. On **iOS 26+**, use the dedicated **Search** tab (Part 7).

---

## Part 4 — Detail Reading

Tap any ci to open **Work Detail** — the core reading experience.

### Toolbar (top right)

| Button | Action |
|--------|--------|
| **♥** | Add or remove from Favorites (uses your accent color when starred) |
| **Speaker** | Start **TTS read-aloud**; tap again to pause / resume |
| **⋯ More** | Opens the action menu (see below) |

### Content sections

Not every work has every layer. Sections appear only when content exists:

| Section | Coverage | What you see |
|---------|----------|--------------|
| **Original text** | All 21,592 | Full ci with optional pinyin |
| **Classical notes** | Where available | Traditional scholarly annotations |
| **Plain translation** | **11,029 works** | Modern vernacular rendering |
| **Modern commentary** | Curated subset | Appreciation and literary context |
| **Cipai intro** | Featured & linked cipai | Tune pattern explanation |
| **Author bio** | 1,509 authors | Poet biography |
| **Related works** | Smart links | Same author, cipai, or theme |

Toggle each section on or off while reading. **Private notes** appear at the bottom — your personal annotations, visible only to you (synced via iCloud when enabled).

### More menu (⋯)

| Item | What it does |
|------|----------------|
| **Font size** | Opens scaling panel (50%–300%, default base 22 pt) |
| **Immersive reading** | Full-screen, distraction-free view (Part 5) |
| **Pinyin** | Per-work override of global pinyin setting |
| **Vertical layout** | Per-work override of reading direction |
| **Copy full text** | Copies entire ci to clipboard |
| **Share text** | System share sheet with plain text |
| **Generate share card** | Opens 13-style image card editor (Part 11) |
| **Private note** | Add or edit your personal note for this work |

### Reading options

- **Pinyin** — global default in Settings; override per work in detail
- **Vertical layout** — classical top-to-bottom reading; override per work
- **Center original text** — on by default; aligns the main text block
- **System translation** (iOS 17.4+) — Apple's translation panel for selected text
- **Section toggles** — show/hide Translation, Notes, Commentary, Cipai intro, Author bio

### TTS read-aloud

Tap the **speaker** icon for on-device text-to-speech. Uses system voices — no network. Ideal for listening while commuting or studying pronunciation with pinyin visible.

### Long-press on list rows

In any work list, **long-press** a row for quick actions: **Favorite**, **Read aloud**, **Share**, or **Remove from history** (in history views).

### Deep link

Open a specific work by catalog ID: `isongci://poem?id=42`

---

## Part 5 — Immersive Reading

From detail **More → Immersive Reading**, enter a clean full-screen page designed for recitation, presentation, and focused study.

### Layout

- **Vertical** — classical scroll-style top-to-bottom flow (default for immersive)
- **Horizontal** — modern left-to-right flow
- Switch anytime inside immersive mode; preference can follow global Settings

### Typography & atmosphere

- **Calligraphy-inspired font** for the main text — evokes brush-written Song Ci
- **Xuan paper (宣纸) background** — warm, textured literary feel
- Adapts to your **light / dark / system** theme and **accent color**

### Controls

- Pinch or use the **font scale** control (50%–300%)
- Tap to show/hide chrome (toolbar, section toggles)
- **TTS** available without leaving immersive mode
- Swipe or use arrows to move to **previous / next** work in the current list context

### Best for

- iPad presentation or desk reading
- Memorization and recitation practice
- Screenshots and share-card preparation

---

## Part 6 — Favorites

### Starring works

Tap **♥** on any work detail, or long-press a list row → **Favorite**. Favorited rows use your **accent color** for the star.

### Favorites tab layouts

Open the **Favorites** tab. Tap **⋯** to switch:

| Layout | Best for |
|--------|----------|
| **List** | Dense scanning with title, author, cipai |
| **Grid** | Visual browsing with adjustable columns |
| **Cards** | Large preview cards with excerpt |

### Grouping

Organize your collection by:

| Group by | Behavior |
|----------|----------|
| **Author** | Clusters works under each poet |
| **Dynasty** | 五代 / 北宋 / 南宋 sections |
| **Cipai** | Groups by tune pattern |

### Batch editing

Tap **Edit** on the Favorites page:

- **Multi-select** works with checkmarks
- **Select all / Deselect all**
- **Batch remove** from favorites (with confirmation)

Swipe left on a row for a quick **Remove** action.

### Favorite Ci widget

The **Favorite Ci** home-screen widget rotates through your starred works — a personal daily pick from your own collection.

### Export

**Settings → Data → Export favorites** — share your collection as a file for backup or migration.

---

## Part 7 — Search

iSongCi offers **two-tier offline search** — fast metadata first, deep full-text when needed.

### Tier 1 — Instant metadata search

As you type, the app instantly matches against bundled metadata:

- **Titles** (ci names)
- **Author names**
- **Cipai names**
- **Tags and categories**

No loading spinner — results appear on every keystroke.

### Tier 2 — Lazy full-text deep search

For line-level matches inside ci bodies, the app lazily loads **`fulltext.json`** from the bundle on first deep-search use. After the one-time load, full-text search runs entirely on-device.

- Matches **any line** in the 21,592-work corpus
- Slightly slower on first launch of deep search; cached thereafter
- **Zero network** — file ships with the app

### Dedicated Search tab (iOS 26+)

On **iOS 26 and later**, Search has its own tab in the tab bar. On earlier versions, use the search field in **Browse** or system integrations below.

### Spotlight

The app indexes up to **~1,000 works** for system Spotlight search. Tap a Spotlight result to open that work directly in iSongCi.

### Siri & deep links

- Siri: *"Search in iSongCi"* (with keyword)
- Deep link: `isongci://search?q=明月`

### Search tips

| Tip | Why |
|-----|-----|
| Search author + keyword | Narrows large result sets |
| Try cipai name | Finds all works in a tune pattern |
| Use a famous line | Triggers full-text tier for line match |
| Search in Traditional Chinese | UI converts; corpus matches simplified source |

---

## Part 8 — Themes & Appearance

Open **Settings → Appearance**.

### Theme mode

| Mode | Behavior |
|------|----------|
| **Light** | Paper-bright reading background |
| **Dark** | Ink-dark night reading |
| **System** | Follows iOS / macOS appearance |

### Accent color — 15 presets + custom

Choose from **15 theme presets** inspired by Song-dynasty aesthetics:

| # | Preset | Mood |
|---|--------|------|
| 1 | 水墨 Ink | Neutral literary gray |
| 2 | 胭脂 Rouge | Warm crimson accent |
| 3 | 朱砂 Cinnabar | Classic seal-red |
| 4 | 青瓷 Celadon | Cool green glaze |
| 5 | 松绿 Pine | Deep forest green |
| 6 | 黛蓝 Indigo | Scholar's blue-black |
| 7 | 群青 Azure | Bright mineral blue |
| 8 | 青莲 Lotus | Purple-blue blossom |
| 9 | 琥珀 Amber | Golden warm tone |
| 10 | 赭金 Ochre | Earthy gold-brown |
| 11 | 月白 Moon | Pale silver-white |
| 12 | 竹青 Bamboo | Fresh bamboo green |
| 13 | 藕荷 Lotus root | Soft pink-lavender |
| 14 | 玄色 Ebony | Deep black accent |
| 15 | 缃色 Silk | Aged manuscript yellow |

Tap any swatch — selected ring + checkmark. Or pick **Custom** to choose any color from the system color picker.

Accent color applies to: favorite stars, buttons, highlights, share-card accents, and widget tint (when **Follow app theme** is on).

### Language

**English / 简体中文 / 繁體中文** — UI switches instantly. Corpus text is stored in simplified Chinese; Traditional display uses on-device conversion.

### iCloud sync

**Appearance** (light/dark/system), **accent preset**, and **font scale** sync via optional iCloud KVS.

---

## Part 9 — Widgets

### Add a Home Screen widget

1. Long-press the Home Screen → **Edit Home Screen** → tap **+**
2. Search **iSongCi** / **爱宋词**
3. Pick a widget type and size → **Add Widget**

### Widget types

| Widget | Sizes | Behavior |
|--------|-------|----------|
| **Daily Ci** | Small / Medium / Large + Lock Screen | Today's deterministic ci; tap opens detail |
| **Random Ci** | Small / Medium / Large + Lock Screen | Serendipity pick; refreshes on timeline |
| **Favorite Ci** | Small / Medium | Rotates through your favorites |
| **Streak** | Small / Circular (Lock Screen) | Reading streak count and flame icon |

### Lock Screen widgets

When adding widgets, switch to the **Lock Screen** customization page and choose iSongCi rectangular, circular, or inline accessories.

### Widget theme

**Settings → Widgets → Follow app theme** — widgets match your light/dark/accent choice.

### Control Center (iOS 18+)

Add controls for **Today's Ci**, **Serendipity**, and **Search** from **Settings → Control Center** on iOS 18 and later.

### Troubleshooting widgets

- Open the app once after install so daily ci cache is written to App Group
- If text looks wrong after a language change, open the app briefly — it refreshes widget caches automatically
- Daily Ci widget updates at local midnight
- Random Ci widget timeline refreshes periodically for variety

### Widget guide in app

**Settings → Widgets → Widget Guide** or `isongci://widget-guide` for per-widget screenshots and tips.

---

## Part 10 — Siri, Shortcuts & Home Screen Actions

### Siri intents (3)

| Intent | Example phrase |
|--------|----------------|
| **Today's Ci** | "Today's ci in iSongCi" |
| **Serendipity** | "Serendipity in iSongCi" |
| **Search Ci** | "Search in iSongCi" (with keyword) |

Add these in the **Shortcuts** app for automations — e.g. open `isongci://daily` every morning.

### Home Screen quick actions (15 available, max 4 enabled)

Long-press the app icon. Customize in **Settings → Shortcuts → Home Screen Quick Actions**:

| # | Action | Opens |
|---|--------|-------|
| 1 | Today's Ci | `isongci://daily` |
| 2 | Serendipity | `isongci://random` |
| 3 | Continue Reading | `isongci://continue-reading` |
| 4 | Favorites | `isongci://favorites` |
| 5 | Search | `isongci://search` |
| 6 | Browse | `isongci://category` |
| 7 | Home | `isongci://home` |
| 8 | Settings | `isongci://settings` |
| 9 | Usage Guide | `isongci://usage-guide` |
| 10 | Widget Guide | `isongci://widget-guide` |
| 11 | Shortcuts Guide | `isongci://shortcuts-guide` |
| 12 | Feature Guide | `isongci://feature-guide` |
| 13 | Feedback | `isongci://feedback` |
| 14 | In-App Review | `isongci://in-app-review` |
| 15 | Home Shortcuts Settings | `isongci://home-shortcuts` |

Only **4** appear on the icon menu at once — pick your most-used four.

### Deep links (`isongci://`)

Full reference: [Shortcut Links](url-scheme). Common URLs:

| URL | Opens |
|-----|-------|
| `isongci://poem?id=42` | Ci detail by catalog ID |
| `isongci://author?id=12` | Author profile |
| `isongci://daily` | Today's Ci |
| `isongci://random` | Serendipity |
| `isongci://continue-reading` | Continue Reading |
| `isongci://search?q=明月` | Search for 明月 |
| `isongci://favorites` | Favorites tab |

Use in Shortcuts, Notes, Safari, or MDM configuration profiles.

### Shortcuts guide in app

**Settings → Shortcuts → Shortcuts Guide** or `isongci://shortcuts-guide` — one-tap copy buttons for every URL.

---

## Part 11 — Share Cards (13 Styles)

From detail **More → Generate share card**:

| Style | Mood |
|-------|------|
| Classic | Clean literary layout |
| Ink | Brush-and-wash aesthetic |
| Minimal | Typography-focused |
| Vertical | Classical top-to-bottom |
| Cinnabar | Seal-red accent |
| Dark | Night ink background |
| Celadon | Cool ceramic green |
| Ochre-gold | Warm gold tone |
| Snow white | Bright paper white |
| Scroll | Horizontal scroll motif |
| Moon white | Pale moonlit palette |
| Bamboo shadow | Green bamboo texture |
| Xuan paper | Textured 宣纸 background |

### Export options

- **Full text** vs **excerpt** — remembered for next time
- **3× resolution** PNG — sharp on Retina displays and social media
- **Export PNG** — save to Photos or share via any app
- Style preference saved automatically

Requires **Photo Library (Add)** permission only when saving to Photos — write-only, no read access.

---

## Part 12 — iCloud Sync

Optional sync through **iCloud Key-Value Store** — no iHTC Studio server.

| Synced | Not synced |
|--------|------------|
| Favorites | Home Screen quick action choices |
| Private notes | Onboarding / welcome-guide flags |
| Appearance (light/dark/system) | Widget shuffle state |
| Accent color & font scale | Ci text (always in app bundle) |
| Browse / Favorites tab visibility | Search fulltext cache |
| Reading streak | Custom accent picker hue (re-pick on new device) |

Turn on: **Settings → Data → iCloud Sync**. Requires iCloud sign-in on the device. **Ci text is never uploaded** — only your personal data and preferences.

---

## Part 13 — Notifications

### Daily Ci reminder

Optional **local notification** reminds you to read today's ci.

| Setting | Location |
|---------|----------|
| Enable / disable | **Settings → Notifications** |
| Reminder time | Pick your preferred hour and minute |
| Permission | iOS asks on first enable — no server involved |

Notifications are **scheduled entirely on-device**. No push server, no tracking pixel, no remote payload.

### Tips

- If reminders stop after an iOS update, open the app once to reschedule
- Disabling notifications does not affect reading streak logic
- Streak counts when you open any work detail — notification is optional encouragement only

---

## Part 14 — Settings & Guides

Open **Settings**. Sections, top to bottom:

### Appearance

- **Theme** — Light / Dark / System
- **Accent color** — 15 presets + custom (Part 8)
- **Language** — English / 简体中文 / 繁體中文

### Reading

- **Font size slider** — 50%–300% continuous scale (also in detail More menu)
- **Vertical reading** — global toggle
- **Pinyin** — on by default
- **Center original text** — on by default
- **Calligraphy font** — immersive & detail typography

### Data

- **Reading streak** — view streak stats
- **iCloud Sync** — optional (Part 12)
- **Export favorites** — share collection as file

### Tab Bar

- Toggle **Browse** tab visibility (default on)
- Toggle **Favorites** tab visibility (default on)

### Widgets

- **Widget Guide** — per-widget instructions
- **Follow app theme** toggle

### Shortcuts

- **Home Screen Quick Actions** — pick up to 4 from 15
- **Shortcuts Guide** — deep link reference with copy buttons

### Notifications

- **Daily Ci reminder** — enable, time, permission status

### Help

- **Usage Guide** — replay feature tour
- **Feature Guide** — deeper feature cards (`isongci://feature-guide`)
- **Send Feedback** — opens email (`isongci://feedback`)

### About

- Version number
- **Tip jar** — optional in-app purchase `com.iHTCboy.iSongCi.6` (handled by Apple StoreKit)
- App Store link
- Replay welcome onboarding

---

## Part 15 — Get the App

| Channel | Link |
|---------|------|
| App Store | [Download on the App Store](https://apps.apple.com/app/id6788433450) |

### System requirements

| Platform | Minimum |
|----------|---------|
| iPhone / iPad | iOS 17.0+ (Search tab: iOS 26.0+) |
| Mac | macOS 13.0+ |

### Contact

- **Email:** [AppleOSer@gmail.com](mailto:AppleOSer@gmail.com) — we typically reply within 48 hours.

### Optional tip jar

If you enjoy iSongCi, consider the optional tip via **Settings → About**. Product ID: `com.iHTCboy.iSongCi.6`. Payment is processed entirely by Apple.

[FAQ](faq) · [Shortcut Links](url-scheme) · [Privacy Policy](privacy)

</section>

<section lang="zh-CN" markdown="1">

### 应用是完全离线的吗？

是的。全部 **21,592 首词作**内置。安装后**零外发网络请求**——无账号、无广告、无分析。开启 iCloud 后仅通过 Apple 服务同步你主动启用的数据。

### 和唐诗/泛诗词 App 有什么不同？

爱宋词**垂直深耕宋词**——不是唐诗宋词元曲混合目录。提供 **1,461 个词牌**知识、**白话译文与现代赏析**、**沉浸竖排阅读**与拼音、今日一词、词卡分享、小组件、控制中心、Siri 与可选 iCloud。

### 收录多少内容？

| 项目 | 数量 |
|------|------|
| 词作总数 | 21,592 |
| 词人 | 1,509 |
| 词牌 | 1,461 |
| 精选词牌（含简介） | 60 |
| 白话译文 | 11,029 |
| 白话赏析 | 全部词作 |
| 合集 | 12（豪放 363 · 婉约 520 · 10 个主题） |
| 朝代 | 五代、北宋、南宋 |

### 白话译文、古典注释、白话赏析有什么区别？

详情页三个独立区块，可分别展开/收起：

- **白话译文** — 全篇现代汉语翻译（约 11,029 首）
- **注释** — 传统笺注类注释（有则显示）
- **白话赏析** — 构建时自动生成的背景、大意与读法提示（仅供参考，非学术引证）

### 所有词作都有译文吗？

不是。**11,029** 首含完整白话译文，其余为原文 + 白话赏析；古典注释视数据源而定。App 定位为品读与检索工作台，而非全库学术注本。

### 今日一词怎么选？

从**精选池**（豪放 + 婉约名作）中，以**自然日为种子确定性**选取——**同一天所有用户看到同一首**，本地**午夜**切换。可从**首页**或 `isongci://daily` 打开。

### 邂逅一词是什么？

**邂逅一词**从精选池**随机**打开一首，每次可能不同。入口：**首页 → 邂逅一词**、`isongci://random`、**邂逅一词**小组件或 Siri。

### 拼音准确吗？

拼音为**自动生成**、按段注音。多数情况可用，但**多音字可能读错**。请作阅读辅助，不作权威注音。

### 繁体中文怎么显示？

界面有独立**繁體中文**文案；资料正文存简体，繁体模式下**运行时逐字转换**（s2t 字表），无需双份数据库。

### 竖排和拼音怎么用？

在 **设置 → 阅读** 全局开关（竖排、拼音、楷体书法）。任意词作详情可进入**沉浸阅读**，全屏竖排（右→左）或横排，宣纸背景，独立字号缩放。

### 沉浸阅读是什么？

**详情 → 更多 → 沉浸阅读**进入全屏无干扰页面，适合背诵或大屏展示。阅读器内可切换竖排/横排与书法字体。

### 如何调节字号？

**设置 → 阅读**滑块，或**详情 → 更多 → 字号**。独立于系统动态字体；开启 iCloud 时可同步。

### 语音朗读怎么用？

详情工具栏点**喇叭**，使用设备本地普通话 TTS，同一按钮暂停/继续。

### 收藏、笔记与 iCloud 怎么用？

**收藏** — 点 ♥ 加星标。**私人笔记** — 每首词仅自己可见的批注（详情页）。可选 **iCloud 同步**收藏、笔记、外观、字号、Tab 显隐、阅读打卡。**词作正文从不上传**——始终保留在安装包内。

### 阅读打卡规则是什么？

在 App 内**打开任意一首词**即计当日打卡。**连续自然日**累加 streak；**中断超过一天**则下次打开 streak 归零显示。**累计品读**统计终身打开篇数。首页与**阅读打卡**小组件同步展示。

### 有哪些分享卡片风格？

**13 种：**经典书香、水墨意境、朱砂印泥、绢帛卷轴、卷轴长图、赭金、雪景、青绿山水、竹简、月夜银灰、简约留白、暗色极简、竖排书法。可选全文/摘录、是否附带赏析；3× 分辨率导出 PNG。

### 有哪些小组件？

| 组件 | 用途 |
|------|------|
| 今日一词 | 当日推荐 |
| 邂逅一词 | 随机精选（约每小时轮换） |
| 收藏词句 | 最新收藏一首 |
| 阅读打卡 | 连续天数 + 累计品读 |
| 控制中心 | 一键打开今日一词（iOS 18+） |

主屏小/中/大，锁屏圆形/行内/矩形；支持 **StandBy**。小组件语言跟随 **App 内语言**，非系统语言。

### 小组件空白或文案不对？

1. 安装后至少打开 App 一次
2. 首页下拉刷新以重写小组件缓存
3. 切换语言后打开 App 刷新
4. **收藏词句**需先收藏至少一首
5. **阅读打卡**需先在 App 内打开词作
6. 检查系统是否允许爱宋词小组件

### 控制中心控件是什么（iOS 18+）？

在 **设置 → 控制中心**（或系统控制中心编辑）添加**今日一词**。需 **iOS 18.0+**。点击直接打开 App 并进入今日一词。

### 有哪些 Siri 能力？

内置 3 个 App Intent：

| 意图 | 示例短语 |
|------|----------|
| 打开今日一词 | 「iSongCi 今日一词」 |
| 邂逅一词 | 「iSongCi 邂逅一词」 |
| 搜索宋词 | 「在 iSongCi 搜索」（可带关键词） |

可在设置中配置主屏快捷操作（最多 4 项）。完整深链见[快捷链接说明](url-scheme)。

### Spotlight 有什么限制？

仅索引**精选池 + 你的收藏**，上限约 **1,000** 条。冷门词作不会出现在系统搜索中，请用 App 内**深度全文搜索**（懒加载全库）。点击 Spotlight 结果直达该词详情。

### 能隐藏标签吗？

可以。**设置 → 标签栏** 关闭**分类**和/或**收藏**标签。隐藏后仍可从详情、长按菜单、小组件与 `isongci://` 链接进入。




|------|---------------|------------------|
| 主屏快捷操作 | ✅ | ❌ |
| 小组件与控制中心 | ✅（iOS 18+ 控制中心） | 小组件主要在 iPhone/iPad |
| 触感反馈 | ✅ | ❌ |
| 独立搜索 Tab | iOS 26+ | 通过按钮 / Sheet 搜索 |
| 核心阅读、收藏、iCloud | ✅ | ✅ |

### 免费吗？打赏是什么？

**完全免费**——21,592 首词与全部功能，无订阅、无广告。可选**打赏**（`com.iHTCboy.iSongCi.6`）通过 Apple 内购支持开发，**不解锁任何额外功能**。

### 系统要求

| 平台 | 最低版本 |
|------|----------|
| iPhone / iPad | iOS 17.0+ |
| Mac | macOS 13.0+ |
| 控制中心控件 | iOS 18.0+ |
| 系统翻译面板 | iOS 17.4+ / macOS 14.4+ |

### 如何下载？

[在 App Store 下载](https://apps.apple.com/app/id6788433450)（App ID **6788433450**）。

### 如何联系支持？

[AppleOSer@gmail.com](mailto:AppleOSer@gmail.com) — 通常 48 小时内回复。

---

### 连续朗读怎么用？

在 **设置 → 阅读** 开启**连续朗读**。整首读完后会出现底部提示条；数秒无操作则自动续读当前队列中的下一首（浏览 / 词单 / 收藏 / 今日一词等带入的队列）。生成词卡时也可勾选要上卡的句子。

### 每日提醒怎么用？

可选**本地通知**提醒阅读今日一词；点击通知会深链打开对应词作。关闭通知不影响打卡连续记录。

## 完整使用手册

以下为原支持页的完整分步说明（内容完整保留）。上方保留常见问答（如有）。

---

## 第一部分 — 首次启动与界面

### 欢迎引导

首次打开会显示**多页欢迎引导**——介绍书库规模、今日一词、沉浸阅读、收藏、小组件与隐私。左右滑动浏览，最后点**开始使用**。随时可重看：**设置 → 帮助 → 使用指南**，或深链 `isongci://feature-guide`。

### 底部标签栏

| 标签 | 作用 |
|------|------|
| **首页** | 今日一词、邂逅一词、继续阅读、阅读打卡、主题预览 |
| **分类** | 词人、词牌、朝代、流派、主题合集、全集 |
| **收藏** | 已加星标的词作，支持列表/网格/卡片与分组 |
| **设置** | 外观、阅读、数据、标签栏、小组件、快捷指令、帮助 |
| **搜索** | 即时元数据搜索 + 懒加载全文深度搜索（**iOS 26+** 为独立搜索标签） |

> **提示：** 可在 **设置 → 标签栏** 关闭「分类」或「收藏」标签。若关闭当前所在标签，会自动回到首页。标签显隐可通过 iCloud 同步。

### 支持平台

| 平台 | 最低版本 |
|------|----------|
| iPhone / iPad | iOS 17.0+ |
| Mac | macOS 13.0+ |

独立**搜索标签**需 **iOS 26+**。更早版本请从分类页搜索框、Spotlight 或 Siri 进入搜索。

### 安装即隐私

- **无账号 · 无广告 · 无分析 SDK**
- 词库内置于安装包——无 CDN、无遥测
- 可选 iCloud 仅用**你的私有 iCloud**；词作正文从不上传

---

## 第二部分 — 首页

**首页**是每日入口——不必在 21,592 首中盲目翻找。

### 今日一词

**按日期确定性推荐**——同一公历日期，所有用户看到同一首词，由日期算法从全库中选出。点击卡片进入完整详情。

- **本地零点**自动换新
- App 启动时写入 **App Group**，供**今日一词**小组件读取
- 深链：`isongci://daily`
- Siri：「爱宋词今日一词」

### 邂逅一词

点 **邂逅一词** 随机邂逅一首——想要惊喜而非固定推荐时使用。每次点击从离线库中重新抽取。

- 深链：`isongci://random`
- Siri：「爱宋词邂逅一词」

### 继续阅读

若你最近打开过词作，首页显示 **继续阅读** 卡片（标题与作者）。一点即回到上次阅读。

- 深链：`isongci://continue-reading`
- 也可设为主屏快捷操作

### 阅读打卡

首页展示**连续阅读天数**与累计阅读篇数。打开任意词作详情即计入当日打卡。

- 可通过 **iCloud 键值存储**同步
- **打卡**小组件在主屏/锁屏展示连续天数

### 主题预览

向下滚动可见快捷入口——**精选词牌**、**主题合集**、**豪放/婉约**、**朝代**亮点。点 **查看全部** 跳转分类并定位到对应分区。

### 主屏快捷操作

长按 App 图标可见 **今日一词**、**邂逅一词**、**继续阅读**、**收藏**、**搜索** 等。在 **设置 → 快捷指令 → 主屏快捷操作** 中自定义（共 15 项可选，最多启用 4 项，见第十部分）。

---

## 第三部分 — 分类浏览

打开 **分类** 标签，多分区从不同角度探索书库：

### 1. 词人（名家）

**1,509 位宋词作者**，含传记。点词人进入作者页与作品列表。

- 点 **⋯** 切换 **列表 / 网格 / 卡片**
- iPhone 与 iPad 网格列数（2–4）分别记忆
- 深链：`isongci://author?id=12`

### 2. 词牌

全库 **1,461 个词牌**。**60 个精选词牌**附有导读——介绍格律、节奏与典型意境，先学词牌再读同牌作品。

示例：水调歌头、念奴娇、满江红、蝶恋花、浣溪沙。

### 3. 朝代

| 朝代 | 范围 |
|------|------|
| **五代** | 宋词前身，花间与传统 |
| **北宋** | 北宋名家 |
| **南宋** | 南宋词人 |

### 4. 流派

| 流派 | 数量 | 特点 |
|------|------|------|
| **豪放** | 363 首 | 旷达雄浑、慷慨激昂 |
| **婉约** | 520 首 | 含蓄细腻、婉转多情 |

同一作品在适用时可能归入多个分组。

### 5. 主题合集

**10 组主题合集**——爱情、离别、怀古、山水、爱国、哲理、节令等。按意境聚合相关词作。

### 6. 全集

完整 **21,592 首**索引，支持排序与筛选，适合一览全库。

### 布局与分区选项

在分类页或词人页点 **⋯**：

| 选项 | 作用 |
|------|------|
| **布局** | 列表 / 网格 / 卡片 |
| **分区显隐** | 显示或隐藏任意浏览分区 |
| **分区排序** | 调整分区出现顺序 |
| **网格列数** | iPhone / iPad 分别 2–4 列 |

### 搜索入口（iOS 26 之前）

iOS 17–25 请用分类页顶部**搜索框**，或 Spotlight / Siri。 **iOS 26+** 请用独立 **搜索** 标签（第七部分）。

---

## 第四部分 — 详情阅读

点任意词作进入**详情页**——核心阅读体验。

### 顶部工具栏

| 按钮 | 功能 |
|------|------|
| **♥** | 收藏 / 取消收藏（收藏后使用主题色） |
| **喇叭** | **语音朗读**；再次点击暂停 / 继续 |
| **⋯ 更多** | 打开操作菜单 |

### 内容分区

并非每首都有全部解读层，有内容才显示：

| 分区 | 覆盖 | 内容 |
|------|------|------|
| **原文** | 全部 21,592 首 | 正文，可开拼音 |
| **古典注释** | 有则显示 | 传统注疏 |
| **白话译文** | **11,029 首** | 现代语翻译 |
| **白话赏析** | 精选篇目 | 鉴赏与背景 |
| **词牌介绍** | 精选/关联词牌 | 格律与典故 |
| **作者生平** | 1,509 位词人 | 传记 |
| **相关作品** | 智能推荐 | 同作者、同词牌、同主题 |

阅读时可单独开关各分区。**私人笔记**在底部——仅自己可见（开启 iCloud 时同步）。

### 更多菜单（⋯）

| 项目 | 作用 |
|------|------|
| **字号** | 缩放面板（50%–300%，基准 22 pt） |
| **沉浸阅读** | 全屏无干扰（第五部分） |
| **拼音** | 单篇覆盖全局拼音设置 |
| **竖排** | 单篇覆盖阅读方向 |
| **复制全文** | 复制整首到剪贴板 |
| **分享文本** | 系统分享纯文本 |
| **生成词卡** | 13 种风格图片编辑器（第十一部分） |
| **私人笔记** | 添加或编辑本篇批注 |

### 阅读选项

- **拼音** — 设置页全局默认；详情可临时覆盖
- **竖排** — 古典竖排；详情可临时覆盖
- **原文居中** — 默认开启
- **系统翻译**（iOS 17.4+）— 选中文字使用 Apple 翻译
- **分区开关** — 译文、注释、赏析、词牌、作者等

### 语音朗读

点 **喇叭** 使用设备本地 TTS，无需联网。适合通勤听读，或对照拼音练发音。

### 列表长按

任意列表**长按**一行：**收藏**、**朗读**、**分享**、**从浏览记录移除**（历史视图中）。

### 深链

按目录 ID 打开：`isongci://poem?id=42`

---

## 第五部分 — 沉浸阅读

详情 **更多 → 沉浸阅读**，进入全屏专注页面，适合背诵、展示与深度品读。

### 排版

- **竖排** — 古典从上到下（沉浸模式默认）
- **横排** — 现代从左到右
- 沉浸模式内可随时切换；也可跟随全局设置

### 字体与氛围

- **书法风格字体**——贴近毛笔写就的词意
- **宣纸背景**——温润纸感
- 随 **浅/深/系统** 主题与**强调色**自适应

### 操作

- 双指缩放或 **字号** 滑块（50%–300%）
- 点击显示/隐藏工具栏与分区开关
- 沉浸模式内可 **朗读**
- 左右切换当前列表中的 **上一首 / 下一首**

### 适用场景

- iPad 展示、案头诵读
- 背诵练习
- 截图与词卡制作

---

## 第六部分 — 收藏

### 加星收藏

详情点 **♥**，或长按 → **收藏**。已收藏星标使用你的**强调色**。

### 收藏页布局

打开 **收藏** 标签，点 **⋯** 切换：

| 布局 | 适合 |
|------|------|
| **列表** | 密集浏览标题、作者、词牌 |
| **网格** | 可调列数的视觉浏览 |
| **卡片** | 大卡片摘要预览 |

### 分组

| 分组方式 | 行为 |
|----------|------|
| **按词人** | 同一作者下聚合 |
| **按朝代** | 五代 / 北宋 / 南宋 |
| **按词牌** | 同一词牌下聚合 |

### 批量编辑

收藏页点 **编辑**：

- **多选**词作
- **全选 / 取消全选**
- **批量取消收藏**（有确认）

左滑单行可快速**移除**。

### 收藏一词小组件

**收藏一词**小组件轮播你收藏的词作——从自己的书单里每日邂逅。

### 导出

**设置 → 数据 → 导出收藏** — 以文件形式分享，便于备份或迁移。

---

## 第七部分 — 搜索

爱宋词提供**双层离线搜索**——先快后深，全程无网。

### 第一层 — 即时元数据搜索

输入即搜，匹配内置元数据：

- **标题**（词题）
- **作者**
- **词牌**
- **标签与分类**

无需等待加载，逐字即时出结果。

### 第二层 — 懒加载全文深度搜索

要在正文中搜名句，首次深度搜索时懒加载包内 **`fulltext.json`**。一次性加载后，全文检索在本地完成。

- 可匹配 21,592 首中的**任意字句**
- 首次略慢，之后缓存加速
- **零网络**——文件随 App 安装

### 独立搜索标签（iOS 26+）

**iOS 26 及以上**在标签栏有独立 **搜索** 标签。更早版本用分类页搜索框或下方系统入口。

### Spotlight

为最多约 **1,000 首**建立系统搜索索引，点结果直达详情。

### Siri 与深链

- Siri：「爱宋词搜索」（带关键词）
- 深链：`isongci://search?q=明月`

### 搜索技巧

| 技巧 | 原因 |
|------|------|
| 作者名 + 关键词 | 缩小结果集 |
| 搜词牌名 | 找出同牌全部作品 |
| 搜名句 | 触发全文检索层 |
| 繁体输入 | 界面转换；语料以简体匹配 |

---

## 第八部分 — 主题与外观

打开 **设置 → 外观**。

### 主题模式

| 模式 | 效果 |
|------|------|
| **浅色** | 明亮纸面阅读 |
| **深色** | 墨色夜读 |
| **跟随系统** | 随 iOS / macOS 外观 |

### 强调色 — 15 款预设 + 自定义

**15 款**宋词意象预设：

| # | 预设 | 意境 |
|---|------|------|
| 1 | 水墨 | 中性书卷灰 |
| 2 | 胭脂 | 暖红 |
| 3 | 朱砂 | 经典印红 |
| 4 | 青瓷 | 冷釉绿 |
| 5 | 松绿 | 深松绿 |
| 6 | 黛蓝 | 学者蓝黑 |
| 7 | 群青 | 明亮石青 |
| 8 | 青莲 | 紫蓝花色 |
| 9 | 琥珀 | 暖金 |
| 10 | 赭金 | 土金褐 |
| 11 | 月白 | 淡银白 |
| 12 | 竹青 | 新竹绿 |
| 13 | 藕荷 | 淡粉紫 |
| 14 | 玄色 | 深黑 |
| 15 | 缃色 | 古绢黄 |

点色块选中（外圈 + 对勾）。或选 **自定义** 用系统取色器任选颜色。

强调色用于：收藏星标、按钮、高亮、词卡点缀、小组件色调（开启「跟随 App 主题」时）。

### 语言

**English / 简体中文 / 繁體中文** — 界面即时切换。语料为简体，繁体界面运行时转换显示。

### iCloud

**外观**、**强调色**、**字号**可通过 iCloud 同步。

---

## 第九部分 — 小组件

### 添加到主屏幕

1. 长按主屏幕 → **编辑主屏幕** → 点 **+**
2. 搜索 **爱宋词** / **iSongCi**
3. 选择类型与尺寸 → **添加小组件**

### 组件类型

| 组件 | 尺寸 | 行为 |
|------|------|------|
| **今日一词** | 小 / 中 / 大 + 锁屏 | 当日确定性推荐；点击进详情 |
| **邂逅一词** | 小 / 中 / 大 + 锁屏 | 随机邂逅；时间线刷新 |
| **收藏一词** | 小 / 中 | 轮播收藏 |
| **阅读打卡** | 小 / 圆形（锁屏） | 连续天数与火焰图标 |

### 锁屏小组件

添加时切换到**锁屏**页，可选矩形、圆形或行内样式。

### 跟随 App 主题

**设置 → 小组件 → 跟随 App 主题**。

### 控制中心（iOS 18+）

在 **设置 → 控制中心** 添加 **今日一词**、**邂逅一词**、**搜索** 控件。

### 常见问题

- 安装后**至少打开 App 一次**，写入今日一词缓存
- 切换语言后文案不对，打开 App 片刻即可刷新
- 今日一词每天**本地零点**更新
- 邂逅一词按时间线周期性换词

### App 内教程

**设置 → 小组件 → 小组件教程**，或 `isongci://widget-guide`。

---

## 第十部分 — Siri、快捷指令与主屏快捷操作

### Siri 意图（3 个）

| 意图 | 示例说法 |
|------|----------|
| **今日一词** | 「爱宋词今日一词」 |
| **邂逅一词** | 「爱宋词邂逅一词」 |
| **搜索** | 「爱宋词搜索」（带关键词） |

可在**快捷指令**中自动化，例如每天定时打开 `isongci://daily`。

### 主屏快捷操作（15 项可选，最多 4 项启用）

长按图标。在 **设置 → 快捷指令 → 主屏快捷操作** 配置：

| # | 操作 | 打开 |
|---|------|------|
| 1 | 今日一词 | `isongci://daily` |
| 2 | 邂逅一词 | `isongci://random` |
| 3 | 继续阅读 | `isongci://continue-reading` |
| 4 | 收藏 | `isongci://favorites` |
| 5 | 搜索 | `isongci://search` |
| 6 | 分类 | `isongci://category` |
| 7 | 首页 | `isongci://home` |
| 8 | 设置 | `isongci://settings` |
| 9 | 使用教程 | `isongci://usage-guide` |
| 10 | 小组件教程 | `isongci://widget-guide` |
| 11 | 快捷指令教程 | `isongci://shortcuts-guide` |
| 12 | 功能引导 | `isongci://feature-guide` |
| 13 | 意见反馈 | `isongci://feedback` |
| 14 | 应用内评分 | `isongci://in-app-review` |
| 15 | 快捷操作设置 | `isongci://home-shortcuts` |

图标菜单**同时只显示 4 项**——选最常用的四个。

### 深链（`isongci://`）

完整列表：[快捷链接](url-scheme)。常用：

| 链接 | 打开 |
|------|------|
| `isongci://poem?id=42` | 按 ID 打开词作 |
| `isongci://author?id=12` | 词人详情 |
| `isongci://daily` | 今日一词 |
| `isongci://random` | 邂逅一词 |
| `isongci://continue-reading` | 继续阅读 |
| `isongci://search?q=明月` | 搜索「明月」 |
| `isongci://favorites` | 收藏标签 |

可用于快捷指令、备忘录、Safari。

### App 内教程

**设置 → 快捷指令 → 快捷指令教程**，或 `isongci://shortcuts-guide`——一键复制各链接。

---

## 第十一部分 — 分享词卡（13 种风格）

详情 **更多 → 生成词卡**：

| 风格 | 特点 |
|------|------|
| 经典 | 简洁文学版式 |
| 水墨 | 笔墨意境 |
| 极简 | 以字体为主 |
| 竖排 | 古典直排 |
| 朱砂 | 印红点缀 |
| 暗色 | 墨色夜景 |
| 青瓷 | 冷釉绿 |
| 赭金 | 暖金设色 |
| 雪白 | 明亮纸白 |
| 卷轴 | 横卷意象 |
| 月白 | 月华淡色 |
| 竹影 | 竹纹绿意 |
| 宣纸 | 纸纹质感 |

### 导出选项

- **全文 / 摘录**（下次记住）
- **3 倍分辨率** PNG——视网膜屏与社交平台清晰
- **导出 PNG** 存相册或系统分享
- 风格偏好自动保存

保存到相册时需 **相册（仅写入）** 权限——只写不读。

---

## 第十二部分 — iCloud 同步

可选 **iCloud 键值存储**同步——不经 iHTC Studio 服务器。

| 会同步 | 不同步 |
|--------|--------|
| 收藏 | 主屏快捷操作配置 |
| 私人笔记 | 引导完成标记 |
| 外观（浅/深/系统） | 小组件随机状态 |
| 强调色与字号 | 词作正文（始终在安装包内） |
| 分类/收藏 Tab 显隐 | 全文搜索缓存 |
| 阅读打卡 | 自定义取色色相（新设备需重选） |

开启：**设置 → 数据 → iCloud 同步**。需设备登录 iCloud。**词作正文从不上传**。

---

## 第十三部分 — 通知

### 每日一词提醒

可选**本地通知**提醒阅读今日一词。

| 设置 | 位置 |
|------|------|
| 开关 | **设置 → 通知** |
| 提醒时间 | 自选时分 |
| 权限 | 首次开启时系统询问——无服务器 |

通知**完全在设备本地调度**。无推送服务器、无追踪。

### 提示

- iOS 大版本升级后若提醒失效，打开 App 一次即可重新调度
- 关闭通知不影响打卡统计
- 打开任意详情即计打卡——通知只是可选提醒

---

## 第十四部分 — 设置与教程

打开 **设置**，自上而下：

### 外观

- **主题** — 浅色 / 深色 / 跟随系统
- **强调色** — 15 预设 + 自定义（第八部分）
- **语言** — English / 简体中文 / 繁體中文

### 阅读

- **正文字号** — 50%–300%（详情更多菜单也可调）
- **竖排阅读** — 全局开关
- **拼音标注** — 默认开启
- **原文居中** — 默认开启
- **书法字体** — 沉浸与详情排版

### 数据

- **阅读打卡** — 查看统计
- **iCloud 同步** — 可选（第十二部分）
- **导出收藏** — 分享为文件

### 标签栏

- **分类** 标签显隐（默认显示）
- **收藏** 标签显隐（默认显示）

### 小组件

- **小组件教程**
- **跟随 App 主题**

### 快捷指令

- **主屏快捷操作** — 15 选 4
- **快捷指令教程** — 深链列表与复制

### 通知

- **每日一词提醒** — 开关、时间、权限状态

### 帮助

- **使用指南** — 重看功能导览
- **功能教程** — 更深功能卡片（`isongci://feature-guide`）
- **发送反馈** — 邮件（`isongci://feedback`）

### 关于

- 版本号
- **打赏** — 可选内购 `com.iHTCboy.iSongCi.6`（Apple StoreKit）
- App Store 链接
- 重播欢迎引导

---

## 第十五部分 — 获取应用

| 渠道 | 链接 |
|------|------|
| App Store | [在 App Store 下载](https://apps.apple.com/app/id6788433450) |

### 系统要求

| 平台 | 最低版本 |
|------|----------|
| iPhone / iPad | iOS 17.0+（搜索标签：iOS 26.0+） |
| Mac | macOS 13.0+ |

### 联系我们

- **邮箱：** [AppleOSer@gmail.com](mailto:AppleOSer@gmail.com) — 通常 48 小时内回复。

### 可选打赏

喜欢爱宋词可在 **设置 → 关于** 打赏。产品 ID：`com.iHTCboy.iSongCi.6`。支付由 Apple 处理。

[常见问题](faq) · [快捷链接](url-scheme) · [隐私政策](privacy)

</section>

<section lang="zh-TW" markdown="1">

### 應用是完全離線的嗎？

是的。全部 **21,592 首詞作**內建。安裝後**零外發網路請求**——無帳號、無廣告、無分析。開啟 iCloud 後僅透過 Apple 服務同步你主動啟用的資料。

### 和唐詩/泛詩詞 App 有什麼不同？

愛宋詞**垂直深耕宋詞**——不是唐詩宋詞元曲混合目錄。提供 **1,461 個詞牌**知識、**白話譯文與現代賞析**、**沉浸直排閱讀**與拼音、今日一詞、詞卡分享、小工具、控制中心、Siri 與可選 iCloud。

### 收錄多少內容？

| 項目 | 數量 |
|------|------|
| 詞作總數 | 21,592 |
| 詞人 | 1,509 |
| 詞牌 | 1,461 |
| 精選詞牌（含簡介） | 60 |
| 白話譯文 | 11,029 |
| 白話賞析 | 全部詞作 |
| 合集 | 12（豪放 363 · 婉約 520 · 10 個主題） |
| 朝代 | 五代、北宋、南宋 |

### 白話譯文、古典註釋、白話賞析有什麼區別？

詳情頁三個獨立區塊，可分別展開/收起：

- **白話譯文** — 全篇現代漢語翻譯（約 11,029 首）
- **註釋** — 傳統箋註類註釋（有則顯示）
- **白話賞析** — 建置時自動產生的背景、大意與讀法提示（僅供參考，非學術引證）

### 所有詞作都有譯文嗎？

不是。**11,029** 首含完整白話譯文，其餘為原文 + 白話賞析；古典註釋視資料來源而定。App 定位為品讀與檢索工作台，而非全庫學術注本。

### 今日一詞怎麼選？

從**精選池**（豪放 + 婉約名作）中，以**自然日為種子確定性**選取——**同一天所有使用者看到同一首**，本地**午夜**切換。可從**首頁**或 `isongci://daily` 開啟。

### 邂逅一詞是什麼？

**邂逅一詞**從精選池**隨機**開啟一首，每次可能不同。入口：**首頁 → 邂逅一詞**、`isongci://random`、**邂逅一詞**小工具或 Siri。

### 拼音準確嗎？

拼音為**自動產生**、依段注音。多數情況可用，但**多音字可能讀錯**。請作閱讀輔助，不作權威注音。

### 繁體中文怎麼顯示？

介面有獨立**繁體中文**文案；資料正文存簡體，繁體模式下**執行時逐字轉換**（s2t 字表），無需雙份資料庫。

### 直排和拼音怎麼用？

在 **設定 → 閱讀** 全域開關（直排、拼音、楷體書法）。任意詞作詳情可進入**沉浸閱讀**，全螢幕直排（右→左）或橫排，宣紙背景，獨立字號縮放。

### 沉浸閱讀是什麼？

**詳情 → 更多 → 沉浸閱讀**進入全螢幕無干擾頁面，適合背誦或大螢幕展示。閱讀器內可切換直排/橫排與書法字體。

### 如何調節字號？

**設定 → 閱讀**滑桿，或**詳情 → 更多 → 字號**。獨立於系統動態字體；開啟 iCloud 時可同步。

### 語音朗讀怎麼用？

詳情工具列點**喇叭**，使用裝置本地普通話 TTS，同一按鈕暫停/繼續。

### 收藏、筆記與 iCloud 怎麼用？

**收藏** — 點 ♥ 加星號。**私人筆記** — 每首詞僅自己可見的批註（詳情頁）。可選 **iCloud 同步**收藏、筆記、外觀、字號、Tab 顯隱、閱讀打卡。**詞作正文從不上傳**——始終保留在安裝包內。

### 閱讀打卡規則是什麼？

在 App 內**開啟任意一首詞**即計當日打卡。**連續自然日**累加 streak；**中斷超過一天**則下次開啟 streak 歸零顯示。**累計品讀**統計終身開啟篇數。首頁與**閱讀打卡**小工具同步展示。

### 有哪些分享卡片風格？

**13 種：**經典書香、水墨意境、朱砂印泥、絹帛卷軸、卷軸長圖、赭金、雪景、青綠山水、竹簡、月夜銀灰、簡約留白、暗色極簡、直排書法。可選全文/摘錄、是否附帶賞析；3× 解析度匯出 PNG。

### 有哪些小工具？

| 元件 | 用途 |
|------|------|
| 今日一詞 | 當日推薦 |
| 邂逅一詞 | 隨機精選（約每小時輪換） |
| 收藏詞句 | 最新收藏一首 |
| 閱讀打卡 | 連續天數 + 累計品讀 |
| 控制中心 | 一鍵開啟今日一詞（iOS 18+） |

主畫面小/中/大，鎖定畫面圓形/行內/矩形；支援 **StandBy**。小工具語言跟隨 **App 內語言**，非系統語言。

### 小工具空白或文案不對？

1. 安裝後至少開啟 App 一次
2. 首頁下拉刷新以重寫小工具快取
3. 切換語言後開啟 App 刷新
4. **收藏詞句**需先收藏至少一首
5. **閱讀打卡**需先在 App 內開啟詞作
6. 檢查系統是否允許愛宋詞小工具

### 控制中心控制項是什麼（iOS 18+）？

在 **設定 → 控制中心**（或系統控制中心編輯）新增**今日一詞**。需 **iOS 18.0+**。點擊直接開啟 App 並進入今日一詞。

### 有哪些 Siri 能力？

內建 3 個 App Intent：

| 意圖 | 範例短語 |
|------|----------|
| 開啟今日一詞 | 「iSongCi 今日一詞」 |
| 邂逅一詞 | 「iSongCi 邂逅一詞」 |
| 搜尋宋詞 | 「在 iSongCi 搜尋」（可帶關鍵字） |

可在設定中設定主畫面快速操作（最多 4 項）。完整深鏈見[快捷連結說明](url-scheme)。

### Spotlight 有什麼限制？

僅索引**精選池 + 你的收藏**，上限約 **1,000** 條。冷門詞作不會出現在系統搜尋中，請用 App 內**深度全文搜尋**（懶載入全庫）。點擊 Spotlight 結果直達該詞詳情。

### 能隱藏標籤嗎？

可以。**設定 → 標籤列** 關閉**分類**和/或**收藏**標籤。隱藏後仍可從詳情、長按選單、小工具與 `isongci://` 連結進入。




|------|---------------|------------------|
| 主畫面快速操作 | ✅ | ❌ |
| 小工具與控制中心 | ✅（iOS 18+ 控制中心） | 小工具主要在 iPhone/iPad |
| 觸感回饋 | ✅ | ❌ |
| 獨立搜尋 Tab | iOS 26+ | 透過按鈕 / Sheet 搜尋 |
| 核心閱讀、收藏、iCloud | ✅ | ✅ |

### 免費嗎？打賞是什麼？

**完全免費**——21,592 首詞與全部功能，無訂閱、無廣告。可選**打賞**（`com.iHTCboy.iSongCi.6`）透過 Apple 內購支持開發，**不解鎖任何額外功能**。

### 系統要求

| 平台 | 最低版本 |
|------|----------|
| iPhone / iPad | iOS 17.0+ |
| Mac | macOS 13.0+ |
| 控制中心控制項 | iOS 18.0+ |
| 系統翻譯面板 | iOS 17.4+ / macOS 14.4+ |

### 如何下載？

[在 App Store 下載](https://apps.apple.com/app/id6788433450)（App ID **6788433450**）。

### 如何聯絡支援？

[AppleOSer@gmail.com](mailto:AppleOSer@gmail.com) — 通常 48 小時內回覆。

---

### 連續朗讀怎麼用？

在 **設定 → 閱讀** 開啟**連續朗讀**。整首讀完後會出現底部提示條；數秒無操作則自動續讀目前佇列中的下一首（瀏覽 / 詞單 / 收藏 / 今日一詞等帶入的佇列）。產生詞卡時也可勾選要上卡的句子。

### 每日提醒怎麼用？

可選**本地通知**提醒閱讀今日一詞；點擊通知會深鏈開啟對應詞作。關閉通知不影響打卡連續紀錄。

## 完整使用手冊

以下為原支援頁的完整分步說明（內容完整保留）。上方保留常見問答（如有）。

---

## 第一部分 — 首次啟動與介面

### 歡迎引導

首次開啟會顯示**多頁歡迎引導**——介紹書庫規模、今日一詞、沉浸閱讀、收藏、小工具與隱私。左右滑動瀏覽，最後點**開始使用**。隨時可重看：**設定 → 幫助 → 使用指南**，或深鏈 `isongci://feature-guide`。

### 底部標籤列

| 標籤 | 作用 |
|------|------|
| **首頁** | 今日一詞、邂逅一詞、繼續閱讀、閱讀打卡、主題預覽 |
| **分類** | 詞人、詞牌、朝代、流派、主題合集、全集 |
| **收藏** | 已加星標的詞作，支援列表/網格/卡片與分組 |
| **設定** | 外觀、閱讀、資料、標籤列、小工具、捷徑、幫助 |
| **搜尋** | 即時中繼資料搜尋 + 懶載入全文深度搜尋（**iOS 26+** 為獨立搜尋標籤） |

> **提示：** 可在 **設定 → 標籤列** 關閉「分類」或「收藏」標籤。若關閉目前所在標籤，會自動回到首頁。標籤顯隱可透過 iCloud 同步。

### 支援平台

| 平台 | 最低版本 |
|------|----------|
| iPhone / iPad | iOS 17.0+ |
| Mac | macOS 13.0+ |

獨立**搜尋標籤**需 **iOS 26+**。較早版本請從分類頁搜尋框、Spotlight 或 Siri 進入搜尋。

### 安裝即隱私

- **無帳號 · 無廣告 · 無分析 SDK**
- 詞庫內建於安裝包——無 CDN、無遙測
- 可選 iCloud 僅用**你的私有 iCloud**；詞作正文從不上傳

---

## 第二部分 — 首頁

**首頁**是每日入口——不必在 21,592 首中盲目翻找。

### 今日一詞

**依日期確定性推薦**——同一公曆日期，所有使用者看到同一首詞，由日期演算法從全庫中選出。點擊卡片進入完整詳情。

- **本地零點**自動換新
- App 啟動時寫入 **App Group**，供**今日一詞**小工具讀取
- 深鏈：`isongci://daily`
- Siri：「愛宋詞今日一詞」

### 邂逅一詞

點 **邂逅一詞** 隨機邂逅一首——想要驚喜而非固定推薦時使用。每次點擊從離線庫中重新抽取。

- 深鏈：`isongci://random`
- Siri：「愛宋詞邂逅一詞」

### 繼續閱讀

若你最近開啟過詞作，首頁顯示 **繼續閱讀** 卡片（標題與作者）。一點即回到上次閱讀。

- 深鏈：`isongci://continue-reading`
- 也可設為主畫面快捷操作

### 閱讀打卡

首頁展示**連續閱讀天數**與累計閱讀篇數。開啟任意詞作詳情即計入當日打卡。

- 可透過 **iCloud 鍵值儲存**同步
- **打卡**小工具在主畫面/鎖定畫面展示連續天數

### 主題預覽

向下捲動可見快捷入口——**精選詞牌**、**主題合集**、**豪放/婉約**、**朝代**亮點。點 **查看全部** 跳轉分類並定位到對應分區。

### 主畫面快捷操作

長按 App 圖示可見 **今日一詞**、**邂逅一詞**、**繼續閱讀**、**收藏**、**搜尋** 等。在 **設定 → 捷徑 → 主畫面快捷操作** 中自訂（共 15 項可選，最多啟用 4 項，見第十部分）。

---

## 第三部分 — 分類瀏覽

開啟 **分類** 標籤，多分區從不同角度探索書庫：

### 1. 詞人（名家）

**1,509 位宋詞作者**，含傳記。點詞人進入作者頁與作品列表。

- 點 **⋯** 切換 **列表 / 網格 / 卡片**
- iPhone 與 iPad 網格欄數（2–4）分別記憶
- 深鏈：`isongci://author?id=12`

### 2. 詞牌

全庫 **1,461 個詞牌**。**60 個精選詞牌**附有導讀——介紹格律、節奏與典型意境，先學詞牌再讀同牌作品。

範例：水調歌頭、念奴嬌、滿江紅、蝶戀花、浣溪沙。

### 3. 朝代

| 朝代 | 範圍 |
|------|------|
| **五代** | 宋詞前身，花間與傳統 |
| **北宋** | 北宋名家 |
| **南宋** | 南宋詞人 |

### 4. 流派

| 流派 | 數量 | 特點 |
|------|------|------|
| **豪放** | 363 首 | 曠達雄渾、慷慨激昂 |
| **婉約** | 520 首 | 含蓄細膩、婉轉多情 |

同一作品在適用時可能歸入多個分組。

### 5. 主題合集

**10 組主題合集**——愛情、離別、懷古、山水、愛國、哲理、節令等。依意境聚合相關詞作。

### 6. 全集

完整 **21,592 首**索引，支援排序與篩選，適合一覽全庫。

### 版面與分區選項

在分類頁或詞人頁點 **⋯**：

| 選項 | 作用 |
|------|------|
| **版面** | 列表 / 網格 / 卡片 |
| **分區顯隱** | 顯示或隱藏任意瀏覽分區 |
| **分區排序** | 調整分區出現順序 |
| **網格欄數** | iPhone / iPad 分別 2–4 欄 |

### 搜尋入口（iOS 26 之前）

iOS 17–25 請用分類頁頂部**搜尋框**，或 Spotlight / Siri。 **iOS 26+** 請用獨立 **搜尋** 標籤（第七部分）。

---

## 第四部分 — 詳情閱讀

點任意詞作進入**詳情頁**——核心閱讀體驗。

### 頂部工具列

| 按鈕 | 功能 |
|------|------|
| **♥** | 收藏 / 取消收藏（收藏後使用主題色） |
| **喇叭** | **語音朗讀**；再次點擊暫停 / 繼續 |
| **⋯ 更多** | 開啟操作選單 |

### 內容分區

並非每首都有全部解讀層，有內容才顯示：

| 分區 | 覆蓋 | 內容 |
|------|------|------|
| **原文** | 全部 21,592 首 | 正文，可開拼音 |
| **古典註釋** | 有則顯示 | 傳統注疏 |
| **白話譯文** | **11,029 首** | 現代語翻譯 |
| **白話賞析** | 精選篇目 | 鑑賞與背景 |
| **詞牌介紹** | 精選/關聯詞牌 | 格律與典故 |
| **作者生平** | 1,509 位詞人 | 傳記 |
| **相關作品** | 智慧推薦 | 同作者、同詞牌、同主題 |

閱讀時可單獨開關各分區。**私人筆記**在底部——僅自己可見（開啟 iCloud 時同步）。

### 更多選單（⋯）

| 項目 | 作用 |
|------|------|
| **字號** | 縮放面板（50%–300%，基準 22 pt） |
| **沉浸閱讀** | 全螢幕無干擾（第五部分） |
| **拼音** | 單篇覆蓋全域拼音設定 |
| **直排** | 單篇覆蓋閱讀方向 |
| **複製全文** | 複製整首到剪貼簿 |
| **分享文字** | 系統分享純文字 |
| **生成詞卡** | 13 種風格圖片編輯器（第十一部分） |
| **私人筆記** | 新增或編輯本篇批註 |

### 閱讀選項

- **拼音** — 設定頁全域預設；詳情可臨時覆蓋
- **直排** — 古典直排；詳情可臨時覆蓋
- **原文置中** — 預設開啟
- **系統翻譯**（iOS 17.4+）— 選取文字使用 Apple 翻譯
- **分區開關** — 譯文、註釋、賞析、詞牌、作者等

### 語音朗讀

點 **喇叭** 使用裝置本地 TTS，無需連網。適合通勤聽讀，或對照拼音練發音。

### 列表長按

任意列表**長按**一行：**收藏**、**朗讀**、**分享**、**從瀏覽記錄移除**（歷史檢視中）。

### 深鏈

依目錄 ID 開啟：`isongci://poem?id=42`

---

## 第五部分 — 沉浸閱讀

詳情 **更多 → 沉浸閱讀**，進入全螢幕專注頁面，適合背誦、展示與深度品讀。

### 排版

- **直排** — 古典從上到下（沉浸模式預設）
- **橫排** — 現代從左到右
- 沉浸模式內可隨時切換；也可跟隨全域設定

### 字體與氛圍

- **書法風格字體**——貼近毛筆寫就的詞意
- **宣紙背景**——溫潤紙感
- 隨 **淺/深/系統** 主題與**強調色**自適應

### 操作

- 雙指縮放或 **字號** 滑桿（50%–300%）
- 點擊顯示/隱藏工具列與分區開關
- 沉浸模式內可 **朗讀**
- 左右切換目前列表中的 **上一首 / 下一首**

### 適用場景

- iPad 展示、案頭誦讀
- 背誦練習
- 截圖與詞卡製作

---

## 第六部分 — 收藏

### 加星收藏

詳情點 **♥**，或長按 → **收藏**。已收藏星標使用你的**強調色**。

### 收藏頁版面

開啟 **收藏** 標籤，點 **⋯** 切換：

| 版面 | 適合 |
|------|------|
| **列表** | 密集瀏覽標題、作者、詞牌 |
| **網格** | 可調欄數的視覺瀏覽 |
| **卡片** | 大卡片摘要預覽 |

### 分組

| 分組方式 | 行為 |
|----------|------|
| **依詞人** | 同一作者下聚合 |
| **依朝代** | 五代 / 北宋 / 南宋 |
| **依詞牌** | 同一詞牌下聚合 |

### 批次編輯

收藏頁點 **編輯**：

- **多選**詞作
- **全選 / 取消全選**
- **批次取消收藏**（有確認）

左滑單行可快速**移除**。

### 收藏一詞小工具

**收藏一詞**小工具輪播你收藏的詞作——從自己的書單裡每日邂逅。

### 匯出

**設定 → 資料 → 匯出收藏** — 以檔案形式分享，便於備份或遷移。

---

## 第七部分 — 搜尋

愛宋詞提供**雙層離線搜尋**——先快後深，全程無網。

### 第一層 — 即時中繼資料搜尋

輸入即搜，比對內建中繼資料：

- **標題**（詞題）
- **作者**
- **詞牌**
- **標籤與分類**

無需等待載入，逐字即時出結果。

### 第二層 — 懶載入全文深度搜尋

要在正文中搜名句，首次深度搜尋時懶載入包內 **`fulltext.json`**。一次性載入後，全文檢索在本地完成。

- 可比對 21,592 首中的**任意字句**
- 首次略慢，之後快取加速
- **零網路**——檔案隨 App 安裝

### 獨立搜尋標籤（iOS 26+）

**iOS 26 及以上**在標籤列有獨立 **搜尋** 標籤。較早版本用分類頁搜尋框或下方系統入口。

### Spotlight

為最多約 **1,000 首**建立系統搜尋索引，點結果直達詳情。

### Siri 與深鏈

- Siri：「愛宋詞搜尋」（帶關鍵字）
- 深鏈：`isongci://search?q=明月`

### 搜尋技巧

| 技巧 | 原因 |
|------|------|
| 作者名 + 關鍵字 | 縮小結果集 |
| 搜詞牌名 | 找出同牌全部作品 |
| 搜名句 | 觸發全文檢索層 |
| 繁體輸入 | 介面轉換；語料以簡體比對 |

---

## 第八部分 — 主題與外觀

開啟 **設定 → 外觀**。

### 主題模式

| 模式 | 效果 |
|------|------|
| **淺色** | 明亮紙面閱讀 |
| **深色** | 墨色夜讀 |
| **跟隨系統** | 隨 iOS / macOS 外觀 |

### 強調色 — 15 款預設 + 自訂

**15 款**宋詞意象預設：

| # | 預設 | 意境 |
|---|------|------|
| 1 | 水墨 | 中性書卷灰 |
| 2 | 胭脂 | 暖紅 |
| 3 | 朱砂 | 經典印紅 |
| 4 | 青瓷 | 冷釉綠 |
| 5 | 松綠 | 深松綠 |
| 6 | 黛藍 | 學者藍黑 |
| 7 | 群青 | 明亮石青 |
| 8 | 青蓮 | 紫藍花色 |
| 9 | 琥珀 | 暖金 |
| 10 | 赭金 | 土金褐 |
| 11 | 月白 | 淡銀白 |
| 12 | 竹青 | 新竹綠 |
| 13 | 藕荷 | 淡粉紫 |
| 14 | 玄色 | 深黑 |
| 15 | 缃色 | 古絹黃 |

點色塊選中（外圈 + 勾選）。或選 **自訂** 用系統取色器任選顏色。

強調色用於：收藏星標、按鈕、高亮、詞卡點綴、小工具色調（開啟「跟隨 App 主題」時）。

### 語言

**English / 简体中文 / 繁體中文** — 介面即時切換。語料為簡體，繁體介面執行時轉換顯示。

### iCloud

**外觀**、**強調色**、**字號**可透過 iCloud 同步。

---

## 第九部分 — 小工具

### 新增到主畫面

1. 長按主畫面 → **編輯主畫面** → 點 **+**
2. 搜尋 **愛宋詞** / **iSongCi**
3. 選擇類型與尺寸 → **加入小工具**

### 元件類型

| 元件 | 尺寸 | 行為 |
|------|------|------|
| **今日一詞** | 小 / 中 / 大 + 鎖定畫面 | 當日確定性推薦；點擊進詳情 |
| **邂逅一詞** | 小 / 中 / 大 + 鎖定畫面 | 隨機邂逅；時間軸重新整理 |
| **收藏一詞** | 小 / 中 | 輪播收藏 |
| **閱讀打卡** | 小 / 圓形（鎖定畫面） | 連續天數與火焰圖示 |

### 鎖定畫面小工具

新增時切換到**鎖定畫面**頁，可選矩形、圓形或行內樣式。

### 跟隨 App 主題

**設定 → 小工具 → 跟隨 App 主題**。

### 控制中心（iOS 18+）

在 **設定 → 控制中心** 新增 **今日一詞**、**邂逅一詞**、**搜尋** 控制項。

### 常見問題

- 安裝後**至少開啟 App 一次**，寫入今日一詞快取
- 切換語言後文案不對，開啟 App 片刻即可重新整理
- 今日一詞每天**本地零點**更新
- 邂逅一詞依時間軸週期性換詞

### App 內教學

**設定 → 小工具 → 小工具教學**，或 `isongci://widget-guide`。

---

## 第十部分 — Siri、捷徑與主畫面快捷操作

### Siri 意圖（3 個）

| 意圖 | 範例說法 |
|------|----------|
| **今日一詞** | 「愛宋詞今日一詞」 |
| **邂逅一詞** | 「愛宋詞邂逅一詞」 |
| **搜尋** | 「愛宋詞搜尋」（帶關鍵字） |

可在**捷徑**中自動化，例如每天定時開啟 `isongci://daily`。

### 主畫面快捷操作（15 項可選，最多 4 項啟用）

長按圖示。在 **設定 → 捷徑 → 主畫面快捷操作** 設定：

| # | 操作 | 開啟 |
|---|------|------|
| 1 | 今日一詞 | `isongci://daily` |
| 2 | 邂逅一詞 | `isongci://random` |
| 3 | 繼續閱讀 | `isongci://continue-reading` |
| 4 | 收藏 | `isongci://favorites` |
| 5 | 搜尋 | `isongci://search` |
| 6 | 分類 | `isongci://category` |
| 7 | 首頁 | `isongci://home` |
| 8 | 設定 | `isongci://settings` |
| 9 | 使用教學 | `isongci://usage-guide` |
| 10 | 小工具教學 | `isongci://widget-guide` |
| 11 | 捷徑教學 | `isongci://shortcuts-guide` |
| 12 | 功能引導 | `isongci://feature-guide` |
| 13 | 意見回饋 | `isongci://feedback` |
| 14 | 應用內評分 | `isongci://in-app-review` |
| 15 | 快捷操作設定 | `isongci://home-shortcuts` |

圖示選單**同時只顯示 4 項**——選最常用的四個。

### 深鏈（`isongci://`）

完整列表：[快捷連結](url-scheme)。常用：

| 連結 | 開啟 |
|------|------|
| `isongci://poem?id=42` | 依 ID 開啟詞作 |
| `isongci://author?id=12` | 詞人詳情 |
| `isongci://daily` | 今日一詞 |
| `isongci://random` | 邂逅一詞 |
| `isongci://continue-reading` | 繼續閱讀 |
| `isongci://search?q=明月` | 搜尋「明月」 |
| `isongci://favorites` | 收藏標籤 |

可用於捷徑、備忘錄、Safari。

### App 內教學

**設定 → 捷徑 → 捷徑教學**，或 `isongci://shortcuts-guide`——一鍵複製各連結。

---

## 第十一部分 — 分享詞卡（13 種風格）

詳情 **更多 → 生成詞卡**：

| 風格 | 特點 |
|------|------|
| 經典 | 簡潔文學版面 |
| 水墨 | 筆墨意境 |
| 極簡 | 以字體為主 |
| 直排 | 古典直排 |
| 朱砂 | 印紅點綴 |
| 暗色 | 墨色夜景 |
| 青瓷 | 冷釉綠 |
| 赭金 | 暖金設色 |
| 雪白 | 明亮紙白 |
| 卷軸 | 橫卷意象 |
| 月白 | 月華淡色 |
| 竹影 | 竹紋綠意 |
| 宣紙 | 紙紋質感 |

### 匯出選項

- **全文 / 摘錄**（下次記住）
- **3 倍解析度** PNG——Retina 螢幕與社群平台清晰
- **匯出 PNG** 存相簿或系統分享
- 風格偏好自動儲存

儲存到相簿時需 **相簿（僅寫入）** 權限——只寫不讀。

---

## 第十二部分 — iCloud 同步

可選 **iCloud 鍵值儲存**同步——不經 iHTC Studio 伺服器。

| 會同步 | 不同步 |
|--------|--------|
| 收藏 | 主畫面快捷操作設定 |
| 私人筆記 | 引導完成標記 |
| 外觀（淺/深/系統） | 小工具隨機狀態 |
| 強調色與字號 | 詞作正文（始終在安裝包內） |
| 分類/收藏 Tab 顯隱 | 全文搜尋快取 |
| 閱讀打卡 | 自訂取色色相（新裝置需重選） |

開啟：**設定 → 資料 → iCloud 同步**。需裝置登入 iCloud。**詞作正文從不上傳**。

---

## 第十三部分 — 通知

### 每日一詞提醒

可選**本地通知**提醒閱讀今日一詞。

| 設定 | 位置 |
|------|------|
| 開關 | **設定 → 通知** |
| 提醒時間 | 自選時分 |
| 權限 | 首次開啟時系統詢問——無伺服器 |

通知**完全在裝置本地排程**。無推送伺服器、無追蹤。

### 提示

- iOS 大版本升級後若提醒失效，開啟 App 一次即可重新排程
- 關閉通知不影響打卡統計
- 開啟任意詳情即計打卡——通知只是可選提醒

---

## 第十四部分 — 設定與教學

開啟 **設定**，自上而下：

### 外觀

- **主題** — 淺色 / 深色 / 跟隨系統
- **強調色** — 15 預設 + 自訂（第八部分）
- **語言** — English / 简体中文 / 繁體中文

### 閱讀

- **正文字號** — 50%–300%（詳情更多選單也可調）
- **直排閱讀** — 全域開關
- **拼音標註** — 預設開啟
- **原文置中** — 預設開啟
- **書法字體** — 沉浸與詳情排版

### 資料

- **閱讀打卡** — 檢視統計
- **iCloud 同步** — 可選（第十二部分）
- **匯出收藏** — 分享為檔案

### 標籤列

- **分類** 標籤顯隱（預設顯示）
- **收藏** 標籤顯隱（預設顯示）

### 小工具

- **小工具教學**
- **跟隨 App 主題**

### 捷徑

- **主畫面快捷操作** — 15 選 4
- **捷徑教學** — 深鏈列表與複製

### 通知

- **每日一詞提醒** — 開關、時間、權限狀態

### 幫助

- **使用指南** — 重看功能導覽
- **功能教學** — 更深功能卡片（`isongci://feature-guide`）
- **傳送回饋** — 郵件（`isongci://feedback`）

### 關於

- 版本號
- **打賞** — 可選內購 `com.iHTCboy.iSongCi.6`（Apple StoreKit）
- App Store 連結
- 重播歡迎引導

---

## 第十五部分 — 取得應用

| 管道 | 連結 |
|------|------|
| App Store | [在 App Store 下載](https://apps.apple.com/app/id6788433450) |

### 系統需求

| 平台 | 最低版本 |
|------|----------|
| iPhone / iPad | iOS 17.0+（搜尋標籤：iOS 26.0+） |
| Mac | macOS 13.0+ |

### 聯絡我們

- **信箱：** [AppleOSer@gmail.com](mailto:AppleOSer@gmail.com) — 通常 48 小時內回覆。

### 可選打賞

喜歡愛宋詞可在 **設定 → 關於** 打賞。產品 ID：`com.iHTCboy.iSongCi.6`。付款由 Apple 處理。

[常見問題](faq) · [快捷連結](url-scheme) · [隱私政策](privacy)

</section>
