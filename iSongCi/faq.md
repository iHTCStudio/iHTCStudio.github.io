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

Configure up to **4 Home Screen quick actions** in Settings. Full deep-link list in [Shortcut Links](../url-scheme).

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

On iOS, open **handwriting lyric search** from the control beside Home search when you prefer drawing characters over typing pinyin.

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

Full reference: [Shortcut Links](../url-scheme). Common URLs:

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

[FAQ](../faq) · [Shortcut Links](../url-scheme) · [Privacy Policy](../privacy)

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

可在设置中配置主屏快捷操作（最多 4 项）。完整深链见[快捷链接说明](../url-scheme)。

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

在 iOS 上，可从首页搜索旁的入口打开**手写寻词**，用书写代替拼音输入。

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

完整列表：[快捷链接](../url-scheme)。常用：

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

[常见问题](../faq) · [快捷链接](../url-scheme) · [隐私政策](../privacy)

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

可在設定中設定主畫面快速操作（最多 4 項）。完整深鏈見[快捷連結說明](../url-scheme)。

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

在 iOS 上，可從首頁搜尋旁的入口打開**手寫尋詞**，用書寫代替拼音輸入。

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

完整列表：[快捷連結](../url-scheme)。常用：

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

[常見問題](../faq) · [快捷連結](../url-scheme) · [隱私政策](../privacy)

</section>
<section lang="ja" markdown="1">

### アプリは完全にオフラインですか?

 はい。 **21,592 件の Song Ci 作品**がすべてバンドルされています。 インストール後、アプリは **アウトバウンド ネットワーク リクエストを一切行いません**。アカウント、広告、分析はありません。 オプションの iCloud は、有効にした場合にのみ Apple のサービスを使用します。 

### これは唐詩や一般的な詩アプリとどう違うのですか?

 iSongCi は **Song Ci (宋词)** に垂直であり、唐/宋/元の混合詩カタログではありません。 **1,461 cipai** の知識、**平易な翻訳と現代語の解説**、ピンイン付きの **没入型縦読み**、毎日の ci、共有カード、ウィジェット、コントロール センター、Siri、およびオプションの iCloud が追加されます。 

### どれくらいのコンテンツが含まれていますか?

 | アイテム | カウント |
 |------|------|
 | Ci作品（合計） | 21,592 |
 | 著者 | 1,509 |
 | Cipai (曲パターン) | 1,461 |
 | イントロ付きの注目の cipai | 60 |
 | 平易な翻訳 | 11,029 |
 | 現代の解説 | すべての作品 |
 | コレクション | 12 (Haofang 363 · Wanyue 520 · 10 テーマセット) |
 | 王朝 | 五代、北宋、南宋 |

 ### 平訳・古典注・現代注釈とは何ですか？ 

詳細ページ上の 3 つの個別のレイヤー — 各セクションを個別に切り替えます。

- **平訳 (白话译文)** — 全文の現代中国語訳 (~11,029 作品)
 - **古典的な注釈 (注释)** — 利用可能な場合は伝統的な学術注釈
 - **現代の解説 (白话赏分析)** — 各作品の背景、要点、および読み方のヒントが自動生成されます (学術的な引用ではなく参考用)

 ### すべての作品に翻訳はありますか?

 No. **11,029** 作品には全文平訳が含まれています。 残りは原文と現代の解説を示します。 クラシックノートは、ソースデータにクラシックノートが含まれている場合にのみ表示されます。 このアプリは読書と発見のスタジオであり、すべての CI の完全な学術版ではありません。 

### 今日の Ci はどのように機能しますか?

 作品は、**カレンダーの日をシード**として使用し、**注目のプール** (Haofang + Wanyue の傑作) から決定的に選択されます。つまり、誰もが **同じ日付の同じ CI を見ることになります**。 **現地の真夜中**にロールオーバーします。 **自宅**または`isongci://daily`から開きます。 

### セレンディピティとは何ですか?

 **邂逅一词** は、タップごとに異なる、注目のプールから **ランダム** の部分を描画します。 **Home → Serendipity**、`isongci://random`、**Random Ci** ウィジェット、または Siri を使用します。 

### ピンインはどのくらい正確ですか?

ピンインはセグメントごとに**自動生成**されます。 ほとんどの行ではうまく機能しますが、**多音文字** (多音文字) を読み間違える可能性があります。 発音の専門家としてではなく、読書補助として使用してください。 

### 繁体字中国語表示?

 UI には専用の **繁體中文** 文字列があります。 コーパス テキストは簡体字中国語で保存され、繁体字モードでは **表示時に変換** (文字レベルの s2t テーブル) されます。データベースのコピーを 2 つ必要ありません。 

### 縦読みとピンインはどのように機能しますか?

 **[設定] → [読み取り]** でグローバルにオンにします (縦書きレイアウト、ピンイン、カリグラフィー フォント)。 どのような作業の詳細でも、玄紙の背景と独立したフォント スケーリングを備えた縦方向 (右から左) または横方向のページを全画面で表示する **イマーシブ リーディング** を開くことができます。 

### 没入型読書とは何ですか?

 **詳細 → 詳細 → 没入型読書** を選択すると、クロムフリーのページが開きます。iPad または大画面での朗読やプレゼンテーションに最適です。 リーダー内で縦横切り替えとカリグラフィーを切り替えます。 

### フォント サイズを変更するにはどうすればよいですか?

 **[設定] → [読み取り]** スライダー、または **[詳細] → [詳細] → [フォント サイズ]**。 システムのダイナミック タイプとは独立して本文テキストをスケーリングします。 有効になっている場合は、iCloud 経由で同期します。 

### 読み上げ (TTS) はどのように機能しますか?

詳細ツールバーの **スピーカー** アイコンをタップします。 デバイス上の中国語音声合成を使用します。 同じボタンで一時停止と再開ができます。 

### お気に入り、メモ、iCloud はどのように機能しますか?

 **お気に入り** — 作品の ♥ をタップします。 **プライベートノート** — あなただけが見ることができる詩ごとの注釈 (詳細ページ)。 オプションの **iCloud Sync** は、お気に入り、メモ、外観、フォント スケール、タブの表示状態、読書回数をデバイス間でミラーリングします。 **Ci テキストは決してアップロードされません** - 常にアプリ バンドル内に残ります。 

### 連続読書ルールとは何ですか?

 アプリで **任意の ci** を開き、その暦日をカウントします。 **連続日数**により、連続記録が増加します。 **1 日以上スキップすると**、次回開くと連続記録がゼロにリセットされます。 **合計読み取り数** は、開かれた生涯のピースを追跡します。 Streak は、ホームと **Reading Streak** ウィジェットに表示されます。 

### どのようなシェア カード スタイルがありますか?

 **13 スタイル:** クラシック、インクウォッシュ、辰砂シール、シルクスクロール、スクロールロング、オークルゴールド、ウィンタースノー、グリーンランドスケープ、バンブースリップ、ムーンリットシルバー、ミニマル、ダークミニマル、縦書き。 全文または抜粋を選択します。 オプションでコメントを含めることもできます。 3 倍の解像度で PNG をエクスポートします。 

### どのウィジェットが利用可能ですか?

| ウィジェット | 目的 |
 |--------|--------|
 | 今日のCi | 今日の注目作品 |
 | セレンディピティ | ランダムな注目の ci (1 時間ごとに更新) |
 | お気に入りの Ci | 最新の主演作品 |
 | 連続読書 | 連続日数 + 合計読み取り数 |
 | コントロールセンター | ワンタップで今日の Ci を開きます (iOS 18 以降) |

 サイズ: ホーム画面で小 / 中 / 大。 ロック画面は円形、インライン、または長方形です。 **スタンバイ**をサポートします。 ウィジェット言語はシステム言語ではなく**アプリ内言語**に従います。 

### ウィジェットに間違ったテキストまたは空のテキストが表示されますか?

 1. インストール後にアプリを一度開きます
 2. ホームでプルして更新し、ウィジェットのキャッシュを書き換えます
 3. 言語を変更した後、アプリを短時間開いて更新します
 4. **お気に入りの Ci** には、少なくとも 1 つのスター付き作品が必要です
 5. **Reading Streak** では、まずアプリ内で作品を開く必要があります
 6. システム設定で iSongCi に対してウィジェットが許可されていることを確認します

 ### コントロール センター ウィジェット (iOS 18 以降) とは何ですか?

 **[設定] → [コントロール センター]** (またはシステム コントロール センター エディター) から **今日の Ci** を追加します。 **iOS 18.0+** が必要です。 タップするとアプリが開き、今日の作品が直接表示されます。 

### どのような Siri ショートカットが存在しますか?

 アプリには 3 つのアプリ インテントが付属しています。

| 意図 | フレーズ例 |
 |------|----------------|
 | 今日のCiを開く | 「iSongCiの今日のci」 |
 | ランダム Ci | 「iSongCi のセレンディピティ」 |
 | 検索C | 「iSongCiで検索」（キーワードあり） |

 [設定] で最大 **4 つのホーム画面のクイック アクション**を構成します。 [ショートカット リンク](../url-scheme) の完全なディープリンク リスト。 

### Spotlight の制限とは何ですか?

 Spotlight は、**注目のプールとお気に入り** (最大 **~1,000** エントリ) にインデックスを付けます。 レアな作品はシステム検索では表示されません。 代わりに **アプリ内の詳細な全文検索** を使用してください (完全なコーパスを遅延読み込みします)。 Spotlight の結果をタップして、その ci を直接開きます。 

### タブを非表示にすることはできますか?

 はい。 **[設定] → [タブ バー]** — **カテゴリ** タブや **お気に入り** タブを切り替えます。 非表示のタブには、詳細アクション、長押しメニュー、ウィジェット、`isongci://` リンクを介して引き続きアクセスできます。 




|----------|---------------|------|
 | ホーム画面のクイックアクション | ✅ | ❌ |
 | ウィジェットとコントロールセンター | ✅ (iOS 18+ CC) | 主に iPhone/iPad のウィジェット |
 | 触覚フィードバック | ✅ | ❌ |
 | 専用の検索タブ | iOS 26+ | ボタン/シートから検索 |
 | 主要な読書、お気に入り、iCloud | ✅ | ✅ |

 ### アプリは無料ですか? チップジャーとは何ですか？

**完全に無料** — 21,592 作品すべてとすべての機能を利用でき、購読や広告はありません。 **オプションのヒント ジャー** (`com.iHTCboy.iSongCi.6`) を使用すると、Apple アプリ内購入を通じて開発をサポートできます。 余分なものは何もロック解除されません。 

### システム要件

 | プラットフォーム | 最小 |
 |----------|-----------|
 | iPhone / iPad | iOS 17.0以降 |
 | マック | macOS 13.0+ |
 | コントロールセンターウィジェット | iOS 18.0以降 |
 | システム翻訳パネル | iOS 17.4以降 / macOS 14.4以降 |

 ### アプリを入手するにはどうすればよいですか?

 [App Store でダウンロード](https://apps.apple.com/app/id6788433450) (アプリ ID **6788433450**)。 

### サポートに連絡するにはどうすればよいですか?

 [AppleOSer@gmail.com](mailto:AppleOSer@gmail.com) — 通常、48 時間以内に返信します。 

---

 ### 連続読み取りはどのように機能しますか?

 [設定] → [読み取り] で **連続読み取り** を有効にします。 作業が TTS を終了すると、下部のバーが表示されます。 数秒間何もしないと、現在のキュー内の次の項目 (ブラウズ / プレイリスト / お気に入り / 毎日) が自動的に開始されます。 共有カードを生成するときに行を選択することもできます。 

### 毎日のリマインダーはどのように機能しますか?

オプションの **ローカル通知** は、今日の CI を読むよう通知します。 通知をタップすると、ディープリンク経由でマッチング作品が開きます。 通知を無効にしても、連続読書は解消されません。 

## 完全なユーザー ガイド

 以下のセクションは、サポート ページに以前に掲載されていた完全な製品ウォークスルーです。 簡単な Q&A 項目は (存在する場合) 上に残ります。 

---

 ## パート 1 — 最初の起動とインターフェイス

 ### ウェルカムガイド

 最初の起動時には、**複数ページのウェルカム ガイド**で、ライブラリの規模、毎日の CI、没入型読書、お気に入り、ウィジェット、プライバシーなどについてアプリが紹介されます。 各ページをスワイプして、**開始する** をタップします。 いつでも再生: **[設定] → [ヘルプ] → [使用ガイド]** またはディープリンク `isongci://feature-guide`。 

### タブバーの概要

 | タブ | 何をするのか |
 |-----|----------------|
 | **ホーム** | 今日の Ci、セレンディピティ、続きを読む、連続読書、テーマ別プレビュー |
 | **閲覧** | 著者、cipai、王朝、ジャンル、テーマコレクション、完全なカタログ |
 | **お気に入り** | スター付きはリスト/グリッド/カードのレイアウトとグループ化に対応します。 
| **設定** | 外観、読み取り、データ、タブ、ウィジェット、ショートカット、ヘルプ |
 | **検索** | インスタントメタデータ検索 + 遅延全文詳細検索 (**iOS 26+** の専用タブ) |

> **ヒント:** **[設定] → [タブ バー]** で [**参照**] または [**お気に入り**] タブを非表示にします。 表示中のタブを閉じると、アプリは自動的にホームに戻ります。 タブの表示設定はオプションの iCloud 経由で同期されます。 

### プラットフォーム

 | プラットフォーム | 最小 |
 |----------|-----------|
 | iPhone / iPad | iOS 17.0以降 |
 | マック | macOS 13.0+ |

 専用の**検索タブ**には**iOS 26以降**が必要です。 以前の iOS バージョンでは、検索は [参照] ページまたは Spotlight / Siri 経由で利用できます。 

### インストール時のプライバシー

 - **サインアップなし、広告なし、分析 SDK なし**
 - コーパスはアプリ バンドル内に同梱されます - CDN やテレメトリはありません
 - オプションの iCloud は **プライベート iCloud** のみを使用します。 ci テキストは決してアップロードされません

 ---

 ## パート 2 — ホーム

 **ホーム** タブは、毎日のエントリ ポイントです。21,592 作品を探し回らなくても、厳選された発見が得られます。 

### 今日の Ci (每日一词)

 **決定的な毎日の選択** — 日付ベースのアルゴリズムによって完全なライブラリから選択された、同じ暦日の全員に同じ CI が選択されます。 カードをタップして詳細ページを開きます。 

- **現地の午前0時**に自動的に更新されます
 - アプリの起動時に **アプリ グループ** ストレージに書き込まれるため、**Daily Ci** ウィジェットは同期を維持します
 - ディープリンク: `isongci://daily`
 - Siri: *「iSongCi の今日の ci」*

### セレンディピティ (邂逅一词)

 [**セレンディピティ**] をタップすると、**ランダムに厳選された CI** が表示されます。今日の固定ピックではなく、驚きが欲しい場合に最適です。 タップするたびに、オフライン ライブラリから新しい作品が描画されます。 

- ディープリンク: `isongci://random`
 - Siri: *「iSongCi のセレンディピティ」*

 ### 続きを読む

 最近作品を開いた場合は、[ホーム] に [**続きを読む**] とタイトルと作者が表示されます。 ワンタップで中断したところから再開します。 

- ディープリンク: `isongci://continue-reading`
 - ホーム画面のクイックアクションとしても利用可能

 ### 連続読書数

 ホームには、**連続読書数**、つまり少なくとも 1 つの CI を読んだ連続日数と累積読書数が表示されます。 仕事の詳細を開くと、今日の連続記録にカウントされます。 

- オプションの **iCloud KVS** 経由で同期
 - **ストリーク** ウィジェットはホーム画面とロック画面にストリークを表示します

 ### テーマ別プレビュー

 下にスクロールすると、クイック エントリー カードが表示されます — **注目の cipai**、**テーマ コレクション**、**豪放 / 婉约** ジャンル、**dynasty** ハイライト。 [**すべて表示**] をタップして、そのセクションの [参照] に移動します。 

### ホーム画面のクイックアクション

アプリのアイコンを長押しすると、**今日の Ci**、**セレンディピティ**、**続きを読む**、**お気に入り**、**検索**などのショートカットが表示されます。 **[設定] → [ショートカット] → [ホーム画面のクイック アクション]** で最大 **4** 項目をカスタマイズできます (15 のアクションが利用可能 — パート 10 を参照)。 

---

 ## パート 3 — 参照

 [**参照**] タブを開きます。 複数のセクションにより、さまざまな角度からライブラリを探索できます。 

### 1. 著者 (名家)

 **1,509 人の宋慈の詩人**と伝記。 著者をタップすると、プロフィールと全作品リストが表示されます。 

- **⋯** によるレイアウトの切り替え: **リスト**、**グリッド**、または **カード**
 - グリッド列数 (2 ～ 4) は iPhone と iPad で個別に記憶されます
 - ディープリンク: `isongci://author?id=12`

 ### 2. Cipai (词牌)

 **1,461 cipai** の曲パターンを完全なインデックスに収録。 **60 の注目の cipai** には、形式、リズム、代表的な雰囲気を説明する入門エッセイが含まれています。パターンを学び、その曲に合わせて書かれた作品を閲覧してください。 

例: 水调歌头、念奴娇、满江红、蝶恋花、浣溪沙。 

### 3. 王朝 (朝代)

 歴史的期間ごとに参照:

 | 王朝 | 取材範囲 |
 |----------|----------|
 | **五代** | 歌以前の初期の *ci* の伝統 |
 | **北宋** | 北宋の巨匠 |
 | **南宋** | 南宋の作詞家 |

 ### 4. ジャンル (流派)

| ジャンル | カウント | キャラクター |
 |------|------|-----------|
 | **豪放** | 363 | 大胆で広がりのある英雄的なトーン |
 | **婉约** | 520 | 繊細で叙情的で親密なトーン |

 作品は、該当する場合、一方または両方のグループに掲載される場合があります。 

### 5. テーマ集 (主题)

 **厳選された 10 のテーマ コレクション** — 愛、別れ、郷愁、自然、愛国心、哲学、祭りなど。 各コレクションは、モチーフを共有する ci をグループ化します。 

### 6. フルカタログ (全集)

 完全な **21,592 作品** のインデックス。 並べ替えとフィルターのオプションを備えた 1 つのスクロール可能なリストにすべてを含める場合に使用します。 

### レイアウトとセクションのオプション

 参照ページまたは作成ページで **⋯** をタップします。 

| オプション | 何をするのか |
 |------|----------------|
 | **レイアウト** | リスト/グリッド/カード |
 | **セクションの可視性** | 参照セクションを表示または非表示にする |
 | **セクションの順序** | セクションの表示順序を変更する |
 | **グリッド列** | iPhone では 2 ～ 4、iPad では 2 ～ 4 (個別に記憶) |

 ### 検索エントリ (iOS 26 より前)

 iOS 17 ～ 25 では、[ブラウズ] の上部にある **検索フィールド** から、または Spotlight / Siri 経由で検索を開きます。 **iOS 26+** では、専用の **検索** タブ (パート 7) を使用します。 

---

 ## パート 4 — 詳細な説明

 任意の ci をタップすると、核となる読書エクスペリエンスである **作品の詳細** が開きます。

### ツールバー (右上)

 | ボタン | アクション |
 |----------|----------|
 | ***♥** | お気に入りに追加または削除します (スターを付けたときにアクセント カラーを使用します) |
 | **スピーカー** | **TTS 読み上げ** を開始します。 もう一度タップして一時停止/再開 |
 | **⋯ 詳細** | アクション メニューを開きます (下記を参照)。 

### コンテンツセクション

 すべての作品にすべてのレイヤーがあるわけではありません。 セクションはコンテンツが存在する場合にのみ表示されます。 

| セクション | 取材範囲 | 目に見えるもの |
 |----------|----------|--------------|
 | **原文** | すべて 21,592 | 完全な ci (オプションのピンイン付き) |
 | **クラシックノート** | 利用可能な場合 | 伝統的な学術注釈 |
 | **平訳** | **11,029 作品** | 現代の日常的なレンダリング |
 | **現代の解説** | 厳選されたサブセット | 鑑賞と文学的背景 |
 | **Cipai の紹介** | 注目およびリンクされた cipai | チューンパターン解説｜
 | **著者略歴** | 1,509 人の著者 | 詩人の伝記 |
 | **関連作品** | スマートリンク | 同じ著者、cipai、またはテーマ |

 読書中に各セクションのオンとオフを切り替えます。 **プライベート メモ** が下部に表示されます。これは、自分だけが閲覧できる個人的な注釈です (有効にすると iCloud 経由で同期されます)。 

### その他のメニュー (⋯)

| アイテム | 何をするのか |
 |------|----------------|
 | **フォント サイズ** | スケーリング パネルを開きます (50% ～ 300%、デフォルトのベース 22 ポイント) |
 | **没入型読書** | フルスクリーンで気を散らすことのないビュー (パート 5) |
 | **ピンイン** | グローバル ピンイン設定の作業ごとのオーバーライド |
 | **縦型レイアウト** | 作業ごとの読み取り方向の上書き |
 | **全文をコピー** | ci 全体をクリップボードにコピーします。 
| **テキストを共有** | プレーンテキストのシステム共有シート |
 | **シェアカードを生成** | 13 スタイルのイメージ カード エディターを開きます (パート 11) |
 | **私的なメモ** | この作品に関する個人的なメモを追加または編集します |

 ### 読み取りオプション

 - **ピンイン** — 設定のグローバルデフォルト。 作業ごとに詳細にオーバーライドする
 - **縦型レイアウト** — 古典的な上から下への読み取り。 作業ごとに上書きする
 - **元のテキストを中央揃え** — デフォルトでオン。 メインテキストブロックを整列させます
 - **システム翻訳** (iOS 17.4+) — 選択したテキストに対する Apple の翻訳パネル
 - **セクションの切り替え** — 表示/非表示 翻訳、メモ、解説、Cipai イントロ、著者略歴

 ### TTS 読み上げ

 デバイス上でテキスト読み上げを行うには、**スピーカー** アイコンをタップします。 システム音声を使用します - ネットワークは使用しません。 通勤中のリスニングやピンインが見える発音の勉強に最適です。

### リストの行を長押しします

 どの作業リストでも、行を **長押し**すると、**お気に入り**、**読み上げ**、**共有**、**履歴から削除** (履歴ビュー内) のクイック アクションが実行されます。 

### ディープリンク

 カタログ ID: `isongci://poem?id=42` で特定の作品を開きます

 ---

 ## パート 5 — 没入型読書

 詳細 **[詳細] → [没入型読書]** から、朗読、プレゼンテーション、集中的な学習のために設計されたきれいな全画面ページに入ります。 

### レイアウト

 - **垂直** — 古典的なスクロール スタイルの上から下への流れ (没入型のデフォルト)
 - **水平** — モダンな左から右への流れ
 - イマーシブモードでいつでも切り替えることができます。 設定はグローバル設定に従うことができます

 ### タイポグラフィーと雰囲気

 - **書道にインスピレーションを得た本文のフォント** - 筆で書かれた Song Ci を彷彿とさせます
 - **宣紙（宣纸）の背景** — 温かみのある質感のある文学的な雰囲気
 - **ライト/ダーク/システム**のテーマと**アクセントカラー**に適応します

 ### コントロール

 - ピンチするか、**フォント スケール** コントロールを使用します (50% ～ 300%)
 - タップしてクロムを表示/非表示にします (ツールバー、セクションの切り替え)
 - **TTS** はイマーシブ モードを終了せずに利用可能
 - スワイプまたは矢印を使用して、現在のリスト コンテキストで **前/次** の作品に移動します

 ### こんな方に最適

- iPadでのプレゼンテーションまたは机上での読書
 - 暗記と暗唱の練習
 - スクリーンショットと共有カードの準備

 ---

 ## パート 6 — お気に入り

 ### 出演作品

 仕事の詳細で [**♥**] をタップするか、リストの行を長押し → [**お気に入り**] をタップします。 お気に入りの行では、星の**アクセントカラー**が使用されます。 

### [お気に入り] タブのレイアウト

 [**お気に入り**] タブを開きます。 **⋯** をタップして切り替えます:

 | レイアウト | こんな方に最適 |
 |----------|----------|
 | **リスト** | タイトル、著者、cipai を含む高密度のスキャン |
 | **グリッド** | 調整可能な列を使用した視覚的なブラウジング |
 | **カード** | 抜粋付きの大きなプレビュー カード |

 ### グループ化

 次の方法でコレクションを整理します。 

| グループ化 | 行動 |
 |----------|----------|
 | **著者** | クラスターは各詩人の下で活動します。 
| **王朝** | 五代 / 北宋 / 南宋 セクション |
 | **キパイ** | 曲のパターンごとにグループ化 |

 ### 一括編集

 [お気に入り] ページで [**編集**] をタップします。 

- **複数選択**はチェックマークで機能します
 - **すべて選択/すべて選択解除**
 - お気に入りから **一括削除** (確認付き)

 行を左にスワイプすると、**削除** アクションが簡単に実行できます。 

### お気に入りの Ci ウィジェット

 **お気に入り Ci** ホーム画面ウィジェットは、スター付きの作品、つまり自分のコレクションから毎日選択した作品を順番に表示します。 

＃＃＃ 輸出

**[設定] → [データ] → [お気に入りをエクスポート]** — コレクションをバックアップまたは移行用のファイルとして共有します。 

---

 ## パート 7 — 検索

 iOS では、ピンインを入力するよりも文字を描画したい場合は、ホーム検索の横にあるコントロールから **手書き歌詞検索** を開きます。 

iSongCi は **2 層のオフライン検索**を提供します。最初にメタデータが高速で、必要に応じて詳細なフルテキストが表示されます。 

### 階層 1 — 即時メタデータ検索

 入力すると、アプリはバンドルされたメタデータと即座に照合します。 

- **タイトル** (ci 名)
 - **著者名**
 - **Cipai の名前**
 - **タグとカテゴリ**

 読み込みスピナーなし - キーストロークごとに結果が表示されます。 

### Tier 2 — 遅延全文詳細検索

 ci ボディ内の行レベルの一致の場合、アプリは最初の詳細検索の使用時にバンドルから **`fulltext.json`** を遅延ロードします。 1 回の読み込み後、全文検索が完全にデバイス上で実行されます。 

- 21,592 作品のコーパス内の **任意の行** と一致します
 - ディープ検索の最初の起動がわずかに遅くなります。 その後キャッシュされる
 - **ゼロネットワーク** — ファイルはアプリに同梱されています

 ### 専用検索タブ (iOS 26 以降)

 **iOS 26 以降** では、検索のタブ バーに独自のタブが表示されます。 以前のバージョンでは、**参照** の検索フィールドまたは以下のシステム統合を使用してください。 

### スポットライト

アプリはシステムの Spotlight 検索用に最大 **約1,000 件の作品** をインデックス化します。Spotlight の結果をタップすると、その作品を iSongCi で直接開けます。

### Siri とディープリンク

- Siri: *"iSongCi で検索"*（キーワード付き）
- ディープリンク: `isongci://search?q=明月`

### 検索のコツ

| コツ | 理由 |
|-----|-----|
| 作者＋キーワードで検索 | 大量の結果を絞り込める |
| 詞牌名を試す | 同じ調の作品をすべて見つける |
| 有名な一節を使う | 行単位の一致で全文検索レベルを発動 |
| 繁体字で検索 | UI は変換される；コーパスは簡体字ソースに一致 |

---

## パート8 — テーマ & 外観

**設定 → 外観** を開きます。

### テーマモード

| モード | 説明 |
|------|----------|
| **ライト** | 紙のように明るい読書背景 |
| **ダーク** | 墨のように暗い夜間読書 |
| **システム** | iOS / macOS の外観に従う |

### アクセントカラー — 15 のプリセット + カスタム

宋代の美学にインスパイアされた **15 のテーマプリセット** から選択:

| # | プリセット | 気分 |
 |---|--------|------|
 | 1 | 水墨インク | ニュートラル文学グレー |
 | 2 | 胭脂ルージュ | 温かみのある深紅のアクセント |
 | 3 | 朱砂 辰砂 | クラシックシールレッド |
 | 4 | 青瓷青磁 | 涼しい緑色の釉薬 | 写真 クールな緑色の釉薬
 | 5 | 松绿パイン | 深い森の緑 | 写真
 | 6 | 黛蓝 インディゴ | 学者のブルーブラック |
 | 7 | 群青アズール | 明るいミネラルブルー |
 | 8 | 青莲ロータス | 紫青の花 | 写真 紫青の花
 | 9 | 琥珀 | ゴールデンウォームトーン |
 | 10 | 赭金黄土色 | 素朴なゴールドブラウン |
 | 11 | 月白ムーン | 淡い銀白色 |
 | 12 | 竹青 新鮮な竹の緑 | 写真
 | 13 | 藕荷レンコン | レンコン ソフトピンクラベンダー |
 | 14 | 玄色エボニー | ディープブラックアクセント |
 | 15 | 缃色シルク | 古い原稿黄色 |

 任意のスウォッチ — 選択したリング + チェックマークをタップします。 または、[**カスタム**] を選択して、システム カラー ピッカーから任意の色を選択します。 

アクセント カラーは、お気に入りのスター、ボタン、ハイライト、共有カードのアクセント、ウィジェットの色合いに適用されます (**アプリのテーマに従う** がオンの場合)。 

### 言語

 **English / 简体中文 / 繁體中文** — UI は瞬時に切り替わります。 コーパス テキストは簡体字中国語で保存されます。 従来の表示では、デバイス上の変換が使用されます。 

### iCloud同期

 **外観** (ライト/ダーク/システム)、**アクセント プリセット**、**フォント スケール** は、オプションの iCloud KVS 経由で同期します。 

---

 ## パート 9 — ウィジェット

### ホーム画面ウィジェットを追加する

 1. ホーム画面を長押し → **ホーム画面の編集** → **+**をタップ
 2. **iSongCi** / **愛情宋词** を検索します
 3. ウィジェットのタイプとサイズを選択 → **ウィジェットを追加**

 ### ウィジェットの種類

 | ウィジェット | サイズ | 行動 |
 |----------|------|----------|
 | **デイリー Ci** | 小 / 中 / 大 + ロック画面 | 今日の決定論的ci。 タップすると詳細が開きます |
 | **ランダム Ci** | 小 / 中 / 大 + ロック画面 | セレンディピティピック。 タイムラインの更新 |
 | **お気に入りの Ci** | 小 / 中 | お気に入りを順に表示します |
 | **ストリーク** | 小 / 円形 (ロック画面) | 連続読書数と炎のアイコン |

 ### ロック画面ウィジェット

 ウィジェットを追加するときは、**ロック画面** カスタマイズ ページに切り替えて、iSongCi の長方形、円形、またはインライン アクセサリを選択します。 

### ウィジェットのテーマ

 **設定 → ウィジェット → アプリのテーマに従う** — ウィジェットは、明るい/暗い/アクセントの選択に一致します。 

### コントロールセンター (iOS 18+)

 iOS 18 以降の **[設定] → [コントロール センター]** から **Today's Ci**、**Serendipity**、**Search** のコントロールを追加します。 

### トラブルシューティング ウィジェット

- インストール後、一度アプリを開き、日次 Ci キャッシュを App Group に書き込む  
- 言語変更後にテキストが正しく表示されない場合、アプリを短時間開く — ウィジェットキャッシュが自動で更新されます  
- 日次 Ci ウィジェットは現地の深夜に更新  
- ランダム Ci ウィジェットのタイムラインはバラエティのために定期的に更新されます  

### アプリ内ウィジェットガイド

**設定 → ウィジェット → ウィジェットガイド** または `isongci://widget-guide` で、ウィジェットごとのスクリーンショットとヒントを確認できます。

---

## パート10 — Siri、ショートカット & ホーム画面アクション

### Siri インテント (3)

| インテント | 例文 |
|------------|----------------|
| **今日の Ci** | 「iSongCi で今日の ci」 |
| **セレンディピティ** | 「iSongCi でセレンディピティ」 |
| **Ci を検索** | 「iSongCi で検索」 (キーワード付き) |

自動化のために **ショートカット** アプリに追加 — 例：毎朝 `isongci://daily` を開く。

### ホーム画面クイックアクション (15 個利用可能、最大 4 つ有効)

アプリアイコンを長押し。**設定 → ショートカット → ホーム画面クイックアクション** でカスタマイズ:

| # | アクション | 開く |
 |---|--------|------|
| 1 | 今日のCi | `isongci://daily` |
| 2 | セレンディピティ | `isongci://random` |
| 3 | 続きを読む | `isongci://continue-reading` |
| 4 | お気に入り | `isongci://favorites` |
| 5 | 検索 | `isongci://search` |
| 6 | 参照 | `isongci://category` |
| 7 | ホーム | `isongci://home` |
| 8 | 設定 | `isongci://settings` |
| 9 | ご利用ガイド | `isongci://usage-guide` |
| 10 | ウィジェットガイド | `isongci://widget-guide` |
| 11 | ショートカットガイド | `isongci://shortcuts-guide` |
| 12 | 機能ガイド | `isongci://feature-guide` |
| 13 | フィードバック | `isongci://feedback` |
| 14 | アプリ内レビュー | `isongci://in-app-review` |
| 15 | ホームショートカット設定 | `isongci://home-shortcuts` |

 アイコン メニューには一度に **4** のみが表示されます。最もよく使用される 4 つを選択してください。 

### ディープリンク (`isongci://`)

 完全な参照: [ショートカット リンク](../url-scheme)。 一般的な URL:

 | URL | 開く |
 |-----|------|
| `isongci://poem?id=42` | カタログ ID 別の Ci の詳細 |
| `isongci://author?id=12` | 著者プロフィール |
| `isongci://daily` | 今日のCi |
| `isongci://random` | セレンディピティ |
| `isongci://continue-reading` | 続きを読む |
| `isongci://search?q=明月` | 明月を検索 |
| `isongci://favorites` | お気に入りタブ |

 ショートカット、メモ、Safari、または MDM 構成プロファイルで使用します。 

### アプリ内のショートカット ガイド

**[設定] → [ショートカット] → [ショートカット ガイド]** または `isongci://shortcuts-guide` — すべての URL のコピー ボタンを 1 回タップします。 

---

 ## パート 11 — カードを共有する (13 スタイル)

 詳細 **詳細 → 共有カードの生成** から:

 | スタイル | 気分 |
 |------|------|
 | クラシック | きれいな文学的なレイアウト |
 | インク | ブラシ＆ウォッシュの美学 |
 | 最小限 | タイポグラフィー中心 |
 | 垂直 | 古典的な上から下へ |
 | 辰砂 | シールレッドのアクセント |
 | ダーク | 夜のインクの背景 | 写真 夜のインクの背景
 | 青磁 | クールなセラミックグリーン |
 | オーカーゴールド | 温かみのあるゴールドトーン |
 | 白雪姫 | 写真 明るい紙白 | 写真
 | スクロール | 横スクロールモチーフ | 横スクロールモチーフ
 | ムーンホワイト | 淡い月明かりに照らされたパレット |
 | 竹影 | 写真 竹影 緑の竹のテクスチャ | 写真 緑の竹のテクスチャ
 | 玄紙 | テクスチャ宣纸背景 | | テクスチャ宣纸背景

 ### エクスポートオプション

 - **全文** 対 **抜粋** — 次回のために覚えておきます
 - **解像度 3 倍** PNG — Retina ディスプレイやソーシャル メディアで鮮明に表示
 - **PNG をエクスポート** — 写真に保存するか、任意のアプリで共有
 - スタイル設定は自動的に保存されます

 写真に保存する場合のみ **写真ライブラリ (追加)** 権限が必要です。書き込み専用で読み取りアクセスはできません。 

---

 ## パート 12 — iCloud 同期

 **iCloud Key-Value ストア** を介したオプションの同期 - iHTC Studio サーバーは使用しません。

| 同期済み | 同期されていません |
 |----------|-----------|
 | お気に入り | ホーム画面のクイック アクションの選択 |
 | 個人的なメモ | オンボーディング / ウェルカム ガイド フラグ |
 | 外観(明/暗/系) | ウィジェットのシャッフル状態 |
 | アクセントカラーとフォントスケール | Ci テキスト (常にアプリバンドル内) |
 | 参照/お気に入りタブの表示/非表示 | フルテキスト キャッシュを検索 |
 | 連続読書 | カスタム アクセント ピッカーの色相 (新しいデバイスで再選択) |

 **「設定」→「データ」→「iCloud 同期」** をオンにします。 デバイスで iCloud サインインが必要です。 **Ci テキストは決してアップロードされません**。個人データと設定のみがアップロードされます。 

---

 ## パート 13 — 通知

 ### 毎日の Ci リマインダー

 オプションの **ローカル通知** により、今日の CI を読むよう通知されます。 

| 設定 | 場所 |
 |----------|----------|
 | 有効/無効 | **設定 → 通知** |
 | リマインダー時間 | ご希望の時間と分を選択してください |
 | 許可 | iOS は最初の有効化時に要求します — サーバーは関係しません |

 通知は **完全にデバイス上でスケジュール設定されます**。 プッシュサーバー、トラッキングピクセル、リモートペイロードはありません。 

### ヒント

- iOSのアップデート後にリマインダーが停止した場合は、一度アプリを開いてスケジュールを変更してください
 - 通知を無効にしても連続読み取りロジックには影響しません
 - 仕事の詳細を開いたときの連続カウント - 通知は任意の奨励のみです

 ---

 ## パート 14 — 設定とガイド

 **設定**を開きます。 セクション、上から下:

 ### 外観

 - **テーマ** — ライト / ダーク / システム
 - **アクセントカラー** — 15 プリセット + カスタム (パート 8)
 - **言語** — 英語 / 简体中文 / 繁體中文

 ### 読書

 - **フォント サイズ スライダー** — 50% ～ 300% の連続スケール ([詳細] メニューも詳細)
 - **垂直方向の読み取り** — グローバル切り替え
 - **ピンイン** — デフォルトでオン
 - **元のテキストを中央揃え** — デフォルトでオン
 - **カリグラフィー フォント** — 没入型で詳細なタイポグラフィー

 ### データ

 - **連続読み取り** — 連続読み取りの統計を表示します
 - **iCloud Sync** — オプション (パート 12)
 - **お気に入りのエクスポート** — コレクションをファイルとして共有

 ### タブバー

 - [**参照**] タブの表示/非表示を切り替えます (デフォルトはオン)
 - **お気に入り**タブの表示/非表示を切り替えます (デフォルトはオン)

 ### ウィジェット

 - **ウィジェット ガイド** — ウィジェットごとの説明
 - **アプリのテーマに従う** 切り替え

 ### ショートカット

 - **ホーム画面のクイックアクション** — 15 個から 4 個を選択
 - **ショートカット ガイド** — コピー ボタン付きのディープ リンク リファレンス

### 通知

 - **毎日の Ci リマインダー** — 有効化、時間、許可ステータス

 ### ヘルプ

 - **使用ガイド** — リプレイ機能ツアー
 - **機能ガイド** — より詳細な機能カード (`isongci://feature-guide`)
 - **フィードバックを送信** — メールを開きます (`isongci://feedback`)

 ###について

 - バージョン番号
 - **ヒント ジャー** — オプションのアプリ内購入 `com.iHTCboy.iSongCi.6` (Apple StoreKit によって処理されます)
 - App Storeへのリンク
 - リプレイ歓迎のオンボーディング

 ---

 ## パート 15 — アプリを入手する

 | チャンネル | リンク |
 |----------|------|
 | アプリストア | [App Storeでダウンロード](https://apps.apple.com/app/id6788433450) |

 ### システム要件

 | プラットフォーム | 最小 |
 |----------|-----------|
 | iPhone / iPad | iOS 17.0以降 (検索タブ: iOS 26.0以降) |
 | マック | macOS 13.0+ |

 ### 連絡先

 - **電子メール:** [AppleOSer@gmail.com](mailto:AppleOSer@gmail.com) — 通常、48 時間以内に返信します。 

### オプションのチップジャー

 iSongCi を楽しんでいる場合は、**[設定] → [バージョン情報]** からオプションのヒントを検討してください。 製品ID:`com.iHTCboy.iSongCi.6`。 支払いはすべて Apple によって処理されます。 

[よくある質問](../faq) · [ショートカット リンク](../url-scheme) · [プライバシー ポリシー](../privacy)

</section>
<section lang="ko" markdown="1">

### 앱이 완전히 오프라인 상태인가요? 

예. **21,592개의 송치 작품**을 모두 묶음으로 묶었습니다. 설치 후 앱은 **아웃바운드 네트워크 요청이 전혀 발생하지 않습니다**. 계정도, 광고도, 분석도 없습니다. 선택 사항인 iCloud는 활성화된 경우에만 Apple 서비스를 사용합니다. 

### 당시/일반시 앱과 어떻게 다른가요? 

iSongCi는 **송자(宋词)와 수직**입니다. 당/송/원 시가 혼합된 카탈로그가 아닙니다. **1,461 cipai** 지식, **평범한 번역 및 현대 해설**, 병음이 포함된 **몰입형 세로 읽기**, 일일 CI, 공유 카드, 위젯, 제어 센터, Siri 및 선택적인 iCloud를 추가합니다. 

### 얼마나 많은 콘텐츠가 포함되어 있나요? 

| 아이템 | 카운트 | 
|------|---------| 
| Ci 작품(전체) | 21,592 | 
| 저자 | 1,509 | 
| Cipai(조정 패턴) | 1,461 | 
| 소개가 포함된 주요 cipai | 60 | 
| 일반 번역 | 11,029 | 
| 현대 논평 | 모든 작품 | 
| 컬렉션 | 12 (호팡 363 · 완웨 520 · 테마 10세트) | 
| 왕조 | 오대, 북송, 남송 | 

### 평번역, 고전 주해, 현대 해설이란 무엇인가요? 

세부 정보 페이지의 세 가지 개별 레이어 - 각 섹션을 독립적으로 전환합니다.

- **일반 번역(白话译文)** — 전체 텍스트의 현대 중국어 번역(~11,029개 작품) 
- **고전 노트(注释)** — 가능한 경우 전통적인 학술 주석 
- **현대해설(白话赏析)** — 모든 작품에 대한 배경, 요점, 읽기 팁 자동 생성(학술 인용이 아닌 참고용) 

### 모든 작품에 번역이 있나요? 

번호 **11,029** 작품에는 전체 일반 번역이 포함되어 있습니다. 나머지는 원본 텍스트와 현대 해설을 보여줍니다. 클래식 메모는 소스 데이터에 포함된 경우에만 나타납니다. 이 앱은 모든 CI의 전체 학술 버전이 아닌 독서 및 발견 스튜디오입니다. 

### 오늘의 Ci는 어떻게 작동하나요? 

**달력 날짜를 씨앗**으로 사용하여 **특집 풀**(Haofang + Wanyue 걸작)에서 결정론적으로 작품이 선택됩니다. 모든 사람이 **같은 날짜에 같은 CI**를 볼 수 있습니다. **현지 자정**에 롤오버됩니다. **집** 또는 `isongci://daily`에서 엽니다. 

### 세렌디피티란 무엇인가요? 

**邂逅一词**는 탭할 때마다 다른 추천 풀에서 **무작위** 조각을 가져옵니다. **홈 → 세렌디피티**, `isongci://random`, **Random Ci** 위젯 또는 Siri를 사용하세요. 

### 병음은 얼마나 정확합니까?

병음은 세그먼트별로 **자동 생성**됩니다. 대부분의 줄에서 잘 작동하지만 **다음 문자를 잘못 읽을 수 있습니다**(多歌字). 발음 기관이 아닌 읽기 보조 도구로 사용하세요. 

### 중국어 번체 디스플레이? 

UI에는 전용 **繁體中文** 문자열이 있습니다. 말뭉치 텍스트는 중국어 간체로 저장되며 일반 모드의 경우 **표시 시 변환**(문자 수준 s2t 테이블)됩니다. 데이터베이스 사본 두 개가 필요하지 않습니다. 

### 세로 읽기와 병음은 어떻게 작동하나요? 

**설정 → 읽기**(세로 레이아웃, 병음, 캘리그래피 글꼴)에서 전체적으로 켜세요. 모든 작업 세부 사항에서 xuan-paper 배경과 독립적인 글꼴 크기 조정이 포함된 전체 화면 세로(오른쪽에서 왼쪽) 또는 가로 페이지에 대한 **몰입형 독서**를 열 수 있습니다. 

### 몰입형 독서란 무엇인가요? 

**세부 정보 → 더보기 → 몰입형 독서**는 크롬이 없는 페이지를 엽니다. iPad나 대형 화면에서 낭송하거나 발표하는 데 적합합니다. 리더 내부에서 세로/가로 및 캘리그래피를 전환할 수 있습니다. 

### 글꼴 크기는 어떻게 변경하나요? 

**설정 → 읽기** 슬라이더 또는 **세부정보 → 더보기 → 글꼴 크기**. 시스템 동적 유형과 관계없이 본문 텍스트의 크기를 조정합니다. 활성화된 경우 iCloud를 통해 동기화됩니다. 

### 소리내어 읽기(TTS)는 어떻게 작동하나요?

세부정보 도구 모음에서 **스피커** 아이콘을 탭하세요. 기기 내 중국어 음성 합성을 사용합니다. 동일한 버튼으로 일시 중지하고 다시 시작하세요. 

### 즐겨찾기, 메모, iCloud는 어떻게 작동하나요? 

**즐겨찾기** — 원하는 작품에서 ♥를 탭하세요. **비공개 메모** — 나만 볼 수 있는 시별 주석입니다(세부정보 페이지). 선택 사항인 **iCloud Sync**는 즐겨찾기, 메모, 모양, 글꼴 크기, 탭 가시성 및 여러 기기의 연속 읽기를 미러링합니다. **Ci 텍스트는 업로드되지 않습니다** — 항상 앱 번들에 유지됩니다. 

### 연속 읽기 규칙은 무엇인가요? 

해당 날짜를 계산하려면 앱에서 **모든 CI**를 엽니다. **연속적인 일수** 연속 기록이 늘어납니다. **하루 이상 건너뛰면** 다음 번 열 때 연속 기록이 0으로 재설정됩니다. **총 읽기 횟수**는 평생 동안 열어본 부분을 추적합니다. Streak는 홈과 **Reading Streak** 위젯에 나타납니다. 

### 어떤 공유 카드 스타일이 있나요? 

**13가지 스타일:** 클래식, 잉크 워시, 진사 봉인, 실크 스크롤, 긴 스크롤, 황토 금, 겨울 눈, 녹색 풍경, 대나무 전표, 달빛 은색, 최소, 어두운 최소, 수직 스크립트. 전문이나 발췌문을 선택하세요. 선택적으로 해설을 포함합니다. PNG를 3× 해상도로 내보냅니다. 

### 어떤 위젯을 사용할 수 있나요?

| 위젯 | 목적 | 
|---------|---------| 
| 오늘의 CI | 오늘의 하이라이트 | 
| 세렌디피티 | 무작위 추천 CI(매시간 새로 고침) | 
| 좋아하는 CI | 최신 별표 작품 | 
| 연속 읽기 | 연속 일수 + 총 읽기 횟수 | 
| 제어 센터 | 탭 한 번으로 오늘의 Ci 열기(iOS 18+) | 

크기: 홈 화면의 소형/중형/대형; 잠금 화면 원형, 인라인 또는 직사각형. **대기**를 지원합니다. 위젯 언어는 시스템 언어가 아닌 **인앱 언어**를 따릅니다. 

### 위젯에 잘못된 텍스트 또는 빈 텍스트가 표시됩니까? 

1. 설치 후 앱을 한 번 실행해 보세요. 
2. 위젯 캐시를 다시 작성하려면 홈에서 당겨서 새로고침하세요. 
3. 언어를 변경한 후 앱을 잠시 열어서 새로고침하세요. 
4. **Favorite Ci**에는 별표 표시된 작품이 하나 이상 필요합니다. 
5. **Reading Streak**에서는 먼저 앱 내에서 작품을 열어야 합니다. 
6. 시스템 설정에서 iSongCi에 위젯이 허용되는지 확인하세요. 

### 제어 센터 위젯(iOS 18+)이란 무엇인가요? 

**설정 → 제어 센터**(또는 시스템 제어 센터 편집기)에서 **오늘의 Ci**를 추가하세요. **iOS 18.0+**가 필요합니다. 탭하면 오늘의 작품으로 바로 앱이 열립니다. 

### 어떤 Siri 단축키가 있나요? 

세 가지 앱 인텐트가 앱과 함께 제공됩니다.

| 의도 | 예시 문구 | 
|---------|---| 
| 오늘의 Ci 열기 | "오늘의 CI in iSongCi" | 
| 랜덤 CI | "아이송치의 세렌디피티" | 
| CI 검색 | "iSongCi에서 검색"(키워드 포함) | 

설정에서 최대 **4개의 홈 화면 빠른 작업**을 구성하세요. [바로가기 링크](../url-scheme)의 전체 딥링크 목록입니다. 

### Spotlight 제한사항은 무엇인가요? 

Spotlight는 **추천 풀과 즐겨찾기**를 색인화합니다(최대 **~1,000** 항목). 희귀 작품은 시스템 검색에 나타나지 않습니다. 대신 **인앱 심층 전체 텍스트 검색**을 사용하세요(전체 자료를 지연 로드함). Spotlight 결과를 탭하여 해당 CI를 직접 엽니다. 

### 탭을 숨길 수 있나요? 

예. **설정 → 탭 표시줄** — **카테고리** 및/또는 **즐겨찾기** 탭을 전환합니다. 숨겨진 탭은 세부 작업, 길게 누르기 메뉴, 위젯 및 `isongci://` 링크를 통해 계속 접근할 수 있습니다. 




|---------|---------------|------| 
| 홈 화면 빠른 작업 | ✅ | ❌ | 
| 위젯 및 제어 센터 | ✅ (iOS 18+ CC) | 주로 iPhone/iPad에서 사용되는 위젯 | 
| 햅틱 피드백 | ✅ | ❌ | 
| 전용 검색 탭 | iOS 26 이상 | 버튼/시트를 통해 검색 | 
| 핵심 읽기, 즐겨찾기, iCloud | ✅ | ✅ | 

### 이 앱은 무료인가요? 팁병이란 무엇인가요?

**완전 무료** — 21,592개 작품과 모든 기능이 모두 포함되어 있으며 구독이나 광고가 없습니다. **선택적 팁 항아리**(`com.iHTCboy.iSongCi.6`)를 사용하면 Apple 인앱 구매를 통해 개발을 지원할 수 있습니다. 추가로 아무것도 잠금 해제되지 않습니다. 

### 시스템 요구사항 

| 플랫폼 | 최소 | 
|----------|---------| 
| 아이폰/아이패드 | iOS 17.0+ | 
| 맥 | 맥OS 13.0+ | 
| 제어 센터 위젯 | iOS 18.0 이상 | 
| 시스템 번역 패널 | iOS 17.4+ / macOS 14.4+ | 

### 앱을 다운로드하려면 어떻게 해야 하나요? 

[App Store에서 다운로드](https://apps.apple.com/app/id6788433450) (앱 ID **6788433450**). 

### 지원팀에 어떻게 문의하나요? 

[AppleOSer@gmail.com](mailto:AppleOSer@gmail.com) — 일반적으로 48시간 이내에 답변을 드립니다. 

--- 

### 연속 읽기는 어떻게 작동하나요? 

설정 → 읽기에서 **연속 읽기**를 활성화하세요. 작업이 TTS를 마치면 하단 표시줄이 나타납니다. 몇 초 동안 아무것도 하지 않으면 현재 대기열의 다음 항목(탐색/재생 목록/즐겨찾기/매일)이 자동으로 시작됩니다. 공유 카드를 생성할 때 라인을 선택할 수도 있습니다. 

### 일일 알림은 어떻게 작동하나요?

옵션 **지역 알림**은 오늘의 CI를 읽도록 상기시켜줍니다. 알림을 탭하면 딥링크를 통해 일치하는 작품이 열립니다. 알림을 비활성화해도 연속 읽기 기록은 지워지지 않습니다. 

## 전체 사용자 가이드 

아래 섹션은 이전에 지원 페이지에 있었던 전체 제품 연습입니다. 빠른 Q&A 항목은 위에 남아 있습니다(있는 경우). 

--- 

## 1부 — 첫 번째 실행 및 인터페이스 

### 환영 가이드 

처음 출시 시 **여러 페이지로 구성된 환영 가이드**에서는 도서관 규모, 일일 CI, 몰입형 독서, 즐겨찾기, 위젯, 개인 정보 보호 등 앱을 소개합니다. 각 페이지를 스와이프한 다음 **시작하기**를 탭하세요. 언제든지 재생: **설정 → 도움말 → 사용 가이드** 또는 딥링크 `isongci://feature-guide`. 

### 탭바 개요 

| 탭 | 그것이 하는 일 | 
|------|---| 
| **홈** | 오늘의 Ci, 세렌디피티, 계속 읽기, 연속 읽기, 테마 미리보기 | 
| **찾아보기** | 작가, cipai, 왕조, 장르, 테마 컬렉션, 전체 카탈로그 | 
| **즐겨찾기** | 목록/그리드/카드 레이아웃 및 그룹화를 사용한 별표 작품 | 
| **설정** | 모양, 읽기, 데이터, 탭, 위젯, 바로가기, 도움말 | 
| **검색** | 즉각적인 메타데이터 검색 + 게으른 전체 텍스트 심층 검색(**iOS 26+**의 전용 탭) |

> **팁:** **설정 → 탭 표시줄**에서 **찾아보기** 또는 **즐겨찾기** 탭을 숨기세요. 현재 사용 중인 탭을 닫으면 앱이 자동으로 홈으로 돌아갑니다. 옵션인 iCloud를 통해 탭 가시성이 동기화됩니다. 

### 플랫폼 

| 플랫폼 | 최소 | 
|----------|---------| 
| 아이폰/아이패드 | iOS 17.0+ | 
| 맥 | 맥OS 13.0+ | 

전용 **검색 탭**에는 **iOS 26+**이 필요합니다. 이전 iOS 버전에서는 찾아보기 페이지나 Spotlight/Siri를 통해 검색이 가능합니다. 

### 설치 시 개인정보 보호 

- **가입 없음 · 광고 없음 · 분석 SDK 없음** 
- Corpus는 앱 번들 내에 포함되어 있습니다. CDN도 없고 원격 측정도 없습니다. 
- 선택 사항인 iCloud는 **개인 iCloud**만 사용합니다. ci 텍스트는 업로드되지 않습니다 

--- 

## 2부 - 홈 

**홈** 탭은 매일의 시작 지점입니다. 21,592개의 작품을 탐색하지 않고도 선별된 검색이 가능합니다. 

### 오늘의 시(每日一词) 

**결정론적 일일 선택** — 날짜 기반 알고리즘에 의해 전체 라이브러리에서 선택된 동일한 달력 날짜의 모든 사람을 위한 동일한 CI입니다. 카드를 탭하면 전체 세부정보 페이지가 열립니다. 

- **현지 자정**에 자동으로 새로고침됩니다. 
- 앱이 실행될 때 **앱 그룹** 저장소에 기록되므로 **Daily Ci** 위젯이 동기화 상태로 유지됩니다. 
- 딥링크: `isongci://daily` 
- Siri: *"iSongCi의 오늘의 ci"*

### 세렌디피티(邂逅一词) 

**임의의 선별된 CI**를 보려면 **세렌디피티**를 탭하세요. 오늘의 고정 픽이 아닌 놀라움을 원할 때 좋습니다. 탭할 때마다 오프라인 라이브러리에서 새로운 작품이 그려집니다. 

- 딥링크: `isongci://random` 
- Siri: *"iSongCi의 뜻밖의 행운"* 

### 계속 읽기 

최근에 작품을 열었다면 제목 및 저자와 함께 **계속 읽기**가 홈에 나타납니다. 탭 한 번으로 중단한 부분부터 다시 시작됩니다. 

- 딥링크: `isongci://continue-reading` 
- 홈 화면의 빠른 작업으로도 사용 가능 

### 연속 읽기 

홈에는 귀하의 **연속 독서**가 표시됩니다. 연속 일수 동안 최소 하나의 CI를 읽었으며 누적 읽기 횟수도 표시됩니다. 작업 세부정보를 열면 오늘 연속 기록에 포함됩니다. 

- 옵션 **iCloud KVS**를 통해 동기화됨 
- **줄무늬** 위젯은 홈 화면과 잠금 화면에 줄무늬를 표시합니다. 

### 테마 미리보기 

아래로 스크롤하여 **추천 cipai**, **테마 컬렉션**, **豪放 / 婉约** 장르 및 **dynasty** 하이라이트 등의 빠른 입력 카드를 확인하세요. 해당 섹션의 찾아보기로 이동하려면 **모두 보기**를 탭하세요. 

### 홈 화면 빠른 작업

**오늘의 Ci**, **세렌디피티**, **계속 읽기**, **즐겨찾기**, **검색**과 같은 바로가기를 사용하려면 앱 아이콘을 길게 누르세요. **설정 → 바로가기 → 홈 화면 빠른 작업**에서 최대 **4** 항목을 사용자 정의하세요(15개 작업 사용 가능 - 10부 참조). 

--- 

## 3부 — 찾아보기 

**찾아보기** 탭을 엽니다. 여러 섹션을 통해 다양한 각도에서 라이브러리를 탐색할 수 있습니다. 

### 1. 저자(명가) 

**1,509명의 송자 시인** 전기 포함. 프로필과 전체 작품 목록을 보려면 작성자를 탭하세요. 

- **⋯**를 통해 레이아웃 전환: **목록**, **그리드** 또는 **카드** 
- iPhone 및 iPad에서 별도로 기억되는 그리드 열 수(2~4) 
- 딥링크: `isongci://author?id=12` 

2. 치파이(词牌) 

**1,461 cipai** 전체 인덱스의 패턴을 조정합니다. **60개의 특집 시파이**에는 형식, 리듬, 대표적인 분위기를 설명하는 입문 에세이가 포함되어 있습니다. 패턴을 배우고 해당 곡에 맞춰 작성된 작품을 찾아보세요. 

예: 水调歌头, 念奴娇, 满江红, 蝶恋꽃, 浣溪沙. 

### 3. 왕조(朝代) 

역사적 기간별로 찾아보기: 

| 왕조 | 적용 범위 | 
|---------|----------| 
| **오대** | 노래 이전의 초기 *ci* 전통 | 
| **북극** | 북송의 명인 | 
| **남부** | 남송 작사 | 

### 4. 장르(流派)

| 장르 | 카운트 | 캐릭터 | 
|-------|-------|-----------| 
| **豪放** | 363 | 대담하고 확장적이며 영웅적인 톤 | 
| **婉约** | 520 | 섬세하고 서정적이며 친밀한 톤 | 

해당되는 경우 작품은 하나 또는 두 그룹 모두에 나타날 수 있습니다. 

### 5. 테마 컬렉션(主题) 

**10가지 엄선된 테마 컬렉션** — 사랑, 이별, 향수, 자연, 애국심, 철학, 축제 등. 각 컬렉션은 모티브를 공유하는 ci를 그룹화합니다. 

### 6. 전체 카탈로그(전集) 

전체 **21,592개 작품** 지수. 정렬 및 필터 옵션을 사용하여 스크롤 가능한 하나의 목록에 모든 항목을 포함하려는 경우에 사용하세요. 

### 레이아웃 및 섹션 옵션 

찾아보기 또는 작성자 페이지에서 **⋯**를 탭하세요. 

| 옵션 | 그것이 하는 일 | 
|---------|---| 
| **레이아웃** | 목록/그리드/카드 | 
| **섹션 공개 상태** | 탐색 섹션 표시 또는 숨기기 | 
| **섹션 순서** | 섹션 표시 방식 재정렬 | 
| **그리드 열** | iPhone의 경우 2~4, iPad의 경우 2~4(별도 기억) | 

### 검색 항목(iOS 26 이전) 

iOS 17~25에서는 찾아보기 상단에 있는 **검색 필드**에서 또는 Spotlight/Siri를 통해 검색을 엽니다. **iOS 26+**에서는 전용 **검색** 탭(파트 7)을 사용하세요. 

--- 

## 4부 — 세부 내용 읽기 

CI를 탭하여 핵심 읽기 환경인 **작업 세부정보**를 엽니다.

### 툴바(오른쪽 상단) 

| 버튼 | 액션 | 
|---------|---------| 
| **♥** | 즐겨찾기에 추가 또는 제거(별표 표시 시 강조 색상 사용) | 
| **연사** | **TTS 소리내어 읽기**를 시작합니다. 다시 탭하여 일시중지/재개 | 
| **⋯ 더 보기** | 작업 메뉴 열기(아래 참조) | 

### 콘텐츠 섹션 

모든 작품에 모든 레이어가 있는 것은 아닙니다. 섹션은 콘텐츠가 있는 경우에만 나타납니다. 

| 섹션 | 적용 범위 | 당신이 보는 것 | 
|---------|----------|---------------| 
| **원문** | 전체 21,592 | 선택적 병음이 포함된 전체 ci | 
| **클래식 노트** | 가능한 경우 | 전통적인 학술 주석 | 
| **평범한 번역** | **11,029개 작품** | 현대 현지어 렌더링 | 
| **현대 논평** | 선별된 하위 집합 | 감상과 문학적 맥락 | 
| **Cipai 소개** | 추천 및 링크된 cipai | 튜닝 패턴 설명 | 
| **저자 약력** | 저자 1,509명 | 시인 전기 | 
| **관련 작품** | 스마트 링크 | 동일한 저자, cipai 또는 테마 | 

읽는 동안 각 섹션을 켜거나 끕니다. **비공개 메모**는 하단에 표시됩니다. 개인 주석은 본인에게만 표시됩니다(활성화된 경우 iCloud를 통해 동기화됨). 

### 추가 메뉴(⋯)

| 아이템 | 그것이 하는 일 | 
|------|---| 
| **글꼴 크기** | 스케일링 패널 열기(50%~300%, 기본 기본 22pt) | 
| **몰입형 독서** | 방해 없는 전체 화면 보기(5부) | 
| **병음** | 전역 병음 설정의 작업별 재정의 | 
| **수직 레이아웃** | 작품별 읽기 방향 재정의 | 
| **전문 복사** | 전체 CI를 클립보드에 복사합니다 | 
| **텍스트 공유** | 일반 텍스트가 포함된 시스템 공유 시트 | 
| **공유 카드 생성** | 13가지 스타일의 이미지 카드 편집기 열기(11부) | 
| **비공개 메모** | 이 작업에 대한 개인 메모 추가 또는 편집 | 

### 읽기 옵션 

- **병음** — 설정의 전역 기본값입니다. 세부적으로 작품별로 재정의 
- **수직 레이아웃** — 전통적인 위에서 아래로 읽기; 작업당 재정의 
- **원본 텍스트 중앙에** — 기본적으로 켜져 있습니다. 기본 텍스트 블록을 정렬합니다. 
- **시스템 번역**(iOS 17.4+) — 선택한 텍스트에 대한 Apple의 번역 패널 
- **섹션 토글** — 번역, 메모, 해설, Cipai 소개, 저자 약력 표시/숨기기 

### TTS 소리내어 읽기 

기기 내 텍스트 음성 변환 기능을 이용하려면 **스피커** 아이콘을 탭하세요. 시스템 음성을 사용합니다. 네트워크는 없습니다. 통근 중에 듣기에 적합하거나 병음이 표시되어 발음을 공부하는 데 적합합니다.

### 목록 행을 길게 누르기 

어떤 작업 목록에서든 행을 **길게 눌러** 빠른 작업을 수행할 수 있습니다. **즐겨찾기**, **소리내어 읽기**, **공유** 또는 **기록에서 제거**(기록 보기에서). 

### 딥링크 

카탈로그 ID: `isongci://poem?id=42`로 특정 작품을 엽니다. 

--- 

## 5부 - 몰입형 독서 

세부정보 **더보기 → 몰입형 독서**에서 암송, 발표, 집중 학습을 위해 설계된 깔끔한 전체 화면 페이지로 들어갑니다. 

### 레이아웃 

- **수직** — 클래식 스크롤 스타일의 위에서 아래로 흐름(몰입형의 경우 기본값) 
- **수평** — 현대적인 왼쪽에서 오른쪽 흐름 
- 몰입형 모드 내에서 언제든지 전환할 수 있습니다. 기본 설정은 전역 설정을 따를 수 있습니다. 

### 타이포그래피 및 분위기 

- **서예에서 영감을 받은 글꼴** 본문 - 붓으로 쓴 Song Ci를 연상시킵니다. 
- **선지(宣纸) 배경** — 따뜻하고 질감이 있는 문학적 느낌 
- **밝음/어두움/시스템** 테마 및 **악센트 색상**에 맞게 조정됩니다. 

### 컨트롤 

- **글꼴 크기** 컨트롤(50%~300%)을 핀치하거나 사용합니다. 
- 탭하여 크롬 표시/숨기기(도구 모음, 섹션 전환) 
- 몰입형 모드를 종료하지 않고도 **TTS** 사용 가능 
- 현재 목록 컨텍스트에서 **이전/다음** 작업으로 이동하려면 스와이프하거나 화살표를 사용하세요. 

### 다음에 가장 적합

- iPad 프레젠테이션 또는 책상 독서 
- 암기 및 암송 연습 
- 스크린샷 및 공유카드 준비 

--- 

## 파트 6 - 즐겨찾기 

### 주연 작품 

과제 세부정보에서 **♥**를 탭하거나 목록 행 → **즐겨찾기**를 길게 누르세요. 즐겨찾기 행은 별표에 **악센트 색상**을 사용합니다. 

### 즐겨찾기 탭 레이아웃 

**즐겨찾기** 탭을 엽니다. 전환하려면 **⋯**를 탭하세요. 

| 레이아웃 | | 
|---------|----------| 
| **목록** | 제목, 작성자, cipai를 사용한 정밀 스캐닝 | 
| **그리드** | 조정 가능한 열을 사용한 시각적 탐색 | 
| **카드** | 발췌문이 포함된 대형 미리보기 카드 | 

### 그룹화 

다음을 통해 컬렉션을 정리하세요: 

| 그룹화 기준 | 행동 | 
|----------|----------| 
| **저자** | 클러스터는 각 시인 아래에서 작동합니다 | 
| **왕조** | 五代 / 北宋 / 南宋 섹션 | 
| **시파이** | 튜닝 패턴별 그룹 | 

### 일괄 편집 

즐겨찾기 페이지에서 **수정**을 탭하세요. 

- **다중 선택**은 체크 표시와 함께 작동합니다. 
- **모두 선택 / 모두 선택 취소** 
- 즐겨찾기에서 **일괄 제거**(확인 후) 

빠른 **제거** 작업을 수행하려면 행을 왼쪽으로 스와이프하세요. 

### 즐겨찾는 Ci 위젯 

**Favorite Ci** 홈 화면 위젯은 별표 표시된 작품을 순환하며 귀하의 컬렉션에서 개인적으로 매일 선택한 작품입니다. 

### 내보내다

**설정 → 데이터 → 즐겨찾기 내보내기** — 백업 또는 마이그레이션을 위해 컬렉션을 파일로 공유하세요. 

--- 

## 7부 - 검색 

iOS에서 병음을 입력하는 것보다 문자를 그리는 것을 선호하는 경우 홈 검색 옆 컨트롤에서 **필기 가사 검색**을 엽니다. 

iSongCi는 **2계층 오프라인 검색**을 제공합니다. 빠른 메타데이터 우선, 필요할 경우 심층적인 전체 텍스트 제공입니다. 

### Tier 1 — 즉각적인 메타데이터 검색 

입력하는 동안 앱은 즉시 번들 메타데이터와 일치합니다. 

- **제목**(CI 이름) 
- **저자 이름** 
- **Cipai 이름** 
- **태그 및 카테고리** 

로딩 스피너 없음 - 키를 누를 때마다 결과가 표시됩니다. 

### Tier 2 — 게으른 전체 텍스트 심층 검색 

ci 본문 내부의 줄 수준 일치의 경우 앱은 첫 번째 심층 검색 사용 시 번들에서 **`fulltext.json`**을 느리게 로드합니다. 일회성 로드 후에는 전체 텍스트 검색이 장치 내에서 완전히 실행됩니다. 

- 21,592개 작품 모음의 **모든 줄**과 일치합니다. 
- 심층 검색을 처음 시작할 때 약간 느려집니다. 그 이후에는 캐시됨 
- **제로 네트워크** — 파일이 앱과 함께 제공됩니다. 

### 전용 검색 탭(iOS 26+) 

**iOS 26 이상**에서는 검색의 탭 표시줄에 자체 탭이 있습니다. 이전 버전에서는 **찾아보기** 또는 아래 시스템 통합의 검색 필드를 사용하세요. 

### 스포트라이트

앱은 시스템 Spotlight 검색을 위해 최대 **약 1,000편의 작품**을 색인합니다. Spotlight 결과를 탭하면 해당 작품을 iSongCi에서 바로 열 수 있습니다.

### Siri 및 딥 링크

- Siri: *"iSongCi에서 검색"* (키워드와 함께)
- 딥 링크: `isongci://search?q=明月`

### 검색 팁

| 팁 | 이유 |
|-----|-----|
| 저자 + 키워드 검색 | 대규모 검색 결과를 좁힘 |
| 사자 이름(cipai) 시도 | 특정 곡 패턴의 모든 작품 검색 |
| 유명 구절 사용 | 구절 일치 전체 텍스트 계층 트리거 |
| 번체 중국어로 검색 | UI는 변환; 말뭉치는 간체 소스와 매칭 |

---

## Part 8 — 테마 및 외관

**설정 → 외관**을 엽니다.

### 테마 모드

| 모드 | 동작 |
|------|----------|
| **라이트** | 종이처럼 밝은 읽기 배경 |
| **다크** | 먹색처럼 어두운 야간 읽기 |
| **시스템** | iOS / macOS 외관을 따름 |

### 강조 색상 — 15개 사전 설정 + 사용자 정의

송나라 미학에서 영감을 받은 **15개 테마 사전 설정** 중에서 선택:

| # | 프리셋 | 기분 | 
|---|---------|------| 
| 1 | 水墨 잉크 | 중립 문학 회색 | 
| 2 | 胭脂 루즈 | 따뜻한 진홍색 악센트 | 
| 3 | 朱砂 진사 | 클래식 씰-레드 | 
| 4 | 青瓷 청자 | 시원한 녹색 유약 | 
| 5 | 소나무 | 깊은 숲 녹색 | 
| 6 | 黛蓝 인디고 | 학자의 블루 블랙 | 
| 7 | 群青 Azure | 밝은 미네랄 블루 | 
| 8 | 青莲 연꽃 | 보라색 파란색 꽃 | 
| 9 | 琥珀 앰버 | 황금빛 따뜻한 톤 | 
| 10 | 赭金 황토 | 소박한 골드 브라운 | 
| 11 | 月白 문 | 창백한 은백색 | 
| 12 | 竹青 대나무 | 신선한 대나무 녹색 | 
| 13 | 藕荷 연근 | 소프트 핑크-라벤더 | 
| 14 | 玄color 에보니 | 딥 블랙 액센트 | 
| 15 | 缃color 실크 | 세 원고 노란색 | 

견본(선택한 링 + 체크 표시)을 탭합니다. 또는 **사용자 정의**를 선택하여 시스템 색상 선택기에서 원하는 색상을 선택하세요. 

강조 색상 적용 대상: 즐겨찾는 별표, 버튼, 강조 표시, 공유 카드 강조 및 위젯 색조(**앱 테마 따르기**가 켜져 있는 경우). 

### 언어 

**English / 简体中文 / 繁體中文** — UI가 즉시 전환됩니다. 코퍼스 텍스트는 중국어 간체로 저장됩니다. 기존 디스플레이는 기기 내 변환을 사용합니다. 

### iCloud 동기화 

**외관**(밝음/어두움/시스템), **악센트 사전 설정** 및 **글꼴 크기**는 옵션인 iCloud KVS를 통해 동기화됩니다. 

--- 

## 9부 - 위젯

### 홈 화면 위젯 추가 

1. 홈 화면 길게 누르기 → **홈 화면 편집** → **+** 누르기 
2. **iSongCi** / **爱宋词** 검색 
3. 위젯 유형 및 크기 선택 → **위젯 추가** 

### 위젯 유형 

| 위젯 | 크기 | 행동 | 
|---------|-------|----------| 
| **데일리시** | 소형 / 중형 / 대형 + 잠금화면 | 오늘날의 결정론적 CI; 탭하면 세부정보가 열립니다 | 
| **임의의 Ci** | 소형 / 중형 / 대형 + 잠금화면 | 세렌디피티 픽; 타임라인 새로고침 | 
| **좋아하는 CI** | 소형/중형 | 즐겨찾기를 통해 회전 | 
| **연속** | 소형/원형(잠금화면) | 연속 읽기 횟수와 불꽃 아이콘 | 

### 잠금 화면 위젯 

위젯을 추가할 때 **잠금 화면** 사용자 정의 페이지로 전환하고 iSongCi 직사각형, 원형 또는 인라인 액세서리를 선택하세요. 

### 위젯 테마 

**설정 → 위젯 → 앱 테마 따르기** — 위젯은 밝은/어두운/악센트 선택과 일치합니다. 

### 제어 센터(iOS 18+) 

iOS 18 이상에서는 **설정 → 제어 센터**에서 **오늘의 Ci**, **Serendipity** 및 **검색**에 대한 제어 기능을 추가합니다. 

### 위젯 문제 해결

- 설치 후 앱을 한 번 열어 일일 CI 캐시를 앱 그룹에 기록
- 언어 변경 후 텍스트가 이상해 보이면 앱을 잠시 열어 위젯 캐시가 자동으로 새로고침됩니다
- 지역 자정에 매일 Ci 위젯 업데이트
- 다양성을 위해 주기적으로 갱신되는 랜덤 Ci 위젯 타임라인

### 앱 내 위젯 가이드

**위젯별 스크린샷과 팁을 위한 위젯 가이드→ → 설정 또는 `isongci://widget-guide`. 

--- 

## 파트 10 — 시리, 단축키 및 홈 화면 동작

### 시리 의도 (3)

| 의도 | 예시 구문 |
|--------|----------------|
| **오늘의 시** | "오늘의 시인 아이송치" |
| **우연의 우연** | "이송지의 우연" |
| **검색 Ci** | "iSongCi에서 검색" (키워드 포함) |

이 기능을 자동화용 **단축키** 앱에 추가하세요 — 예: 매일 아침 `isongci://daily` 열어보세요. 

### 홈 화면 빠른 행동 (15개 사용 가능, 최대 4개 활성화)

앱 아이콘을 길게 누르세요. **설정 → 바로가기 → 홈 화면 빠른 동작**에서 사용자 지정

| # | 액션 | 열림 | 
|---|---------|-------| 
| 1 | 오늘의 CI | `isongci://daily` |
| 2 | 세렌디피티 | `isongci://random` |
| 3 | 계속 읽기 | `isongci://continue-reading` |
| 4 | 즐겨찾기 | `isongci://favorites` |
| 5 | 검색 | `isongci://search` |
| 6 | 찾아보기 | `isongci://category` |
| 7 | 홈 | `isongci://home` |
| 8 | 설정 | `isongci://settings` |
| 9 | 이용안내 | `isongci://usage-guide` |
| 10 | 위젯 가이드 | `isongci://widget-guide` |
| 11 | 바로가기 가이드 | `isongci://shortcuts-guide` |
| 12 | 기능 가이드 | `isongci://feature-guide` |
| 13 | 피드백 | `isongci://feedback` |
| 14 | 인앱 리뷰 | `isongci://in-app-review` |
| 15 | 홈 바로가기 설정 | `isongci://home-shortcuts` |

아이콘 메뉴에는 한 번에 **4**만 표시됩니다. 가장 많이 사용되는 4개를 선택하세요. 

### 딥 링크(`isongci://`) 

전체 참조: [바로가기 링크](../url-scheme). 일반 URL: 

| URL | 열림 | 
|------|---------| 
| `isongci://poem?id=42` | 카탈로그 ID별 Ci 세부정보 |
| `isongci://author?id=12` | 작성자 프로필 |
| `isongci://daily` | 오늘의 CI |
| `isongci://random` | 세렌디피티 |
| `isongci://continue-reading` | 계속 읽기 |
| `isongci://search?q=明月` | 명월을 검색하세요 |
| `isongci://favorites` | 즐겨찾기 탭 |

바로가기, 메모, Safari 또는 MDM 구성 프로필에서 사용하세요. 

### 앱 내 단축키 안내

**설정 → 바로가기 → 바로가기 가이드** 또는 `isongci://shortcuts-guide` — 모든 URL에 대한 원탭 복사 버튼. 

--- 

## 파트 11 - 공유 카드(13가지 스타일) 

세부정보 **더보기 → 공유 카드 생성**에서: 

| 스타일 | 기분 | 
|-------|------| 
| 클래식 | 깨끗한 문학적 레이아웃 | 
| 잉크 | 브러시 앤 워시 미학 | 
| 최소 | 타이포그래피 중심 | 
| 수직 | 위에서 아래로 클래식 | 
| 진사 | 씰 레드 액센트 | 
| 어둠 | 밤 잉크 배경 | 
| 청자 | 쿨 세라믹 그린 | 
| 황토색 | 따뜻한 골드 톤 | 
| 백설공주 | 밝은 종이 흰색 | 
| 스크롤 | 가로 스크롤 모티브 | 
| 문 화이트 | 창백한 달빛 팔레트 | 
| 대나무 그림자 | 녹색 대나무 질감 | 
| 법사 | 질감된 宣纸 배경 | 

### 내보내기 옵션 

- **전체 텍스트** 및 **발췌** — 다음에 기억됨 
- **3× 해상도** PNG — Retina 디스플레이 및 소셜 미디어에서 선명하게 표시 
- **PNG 내보내기** — 사진에 저장하거나 모든 앱을 통해 공유 
- 자동으로 저장되는 스타일 기본 설정 

사진에 저장할 때만 **사진 라이브러리(추가)** 권한이 필요합니다. 쓰기 전용이며 읽기 액세스는 불가능합니다. 

--- 

## 12부 — iCloud 동기화 

**iCloud Key-Value Store**를 통한 선택적 동기화 - iHTC Studio 서버가 없습니다.

| 동기화됨 | 동기화되지 않음 | 
|---------|------------| 
| 즐겨찾기 | 홈 화면 빠른 작업 선택 | 
| 비공개 메모 | 온보딩/환영 안내 플래그 | 
| 외관(밝음/어두움/계) | 위젯 셔플 상태 | 
| 악센트 색상 및 글꼴 크기 | Ci 텍스트(항상 앱 번들에 있음) | 
| 찾아보기/즐겨찾기 탭 가시성 | 전문 캐시 검색 | 
| 연속 독서 | 맞춤 악센트 선택기 색상(새 장치에서 다시 선택) | 

활성화: **설정 → 데이터 → iCloud 동기화**. 기기에 iCloud 로그인이 필요합니다. **Ci 텍스트는 절대 업로드되지 않습니다** — 개인 데이터와 기본 설정만 업로드됩니다. 

--- 

## 13부 — 알림 

### 일일 CI 알림 

옵션 **지역 알림**은 오늘의 CI를 읽도록 상기시켜줍니다. 

| 설정 | 위치 | 
|---------|----------| 
| 활성화 / 비활성화 | **설정 → 알림** | 
| 알림 시간 | 원하는 시간과 분을 선택하세요 | 
| 허가 | iOS는 첫 번째 활성화를 요청합니다. 서버는 관련되지 않습니다 | 

알림은 **완전히 기기 내에서 예약됩니다**. 푸시 서버도 없고, 추적 픽셀도 없고, 원격 페이로드도 없습니다. 

### 팁

- iOS 업데이트 후 알림이 중지되면 앱을 한 번 열어 일정을 변경하세요. 
- 알림을 비활성화해도 연속 읽기 로직에는 영향을 미치지 않습니다. 
- 작업 세부정보를 열면 연속 카운트됩니다. 알림은 선택 사항이며 권장 사항일 뿐입니다. 

--- 

## 14부 - 설정 및 가이드 

**설정**을 엽니다. 섹션(위에서 아래로): 

### 외관 

- **테마** — 밝음/어두움/시스템 
- **악센트 색상** — 15가지 사전 설정 + 사용자 정의(파트 8) 
- **언어** — 영어 / 简体中文 / 繁體中文 

### 읽기 

- **글꼴 크기 슬라이더** — 50%~300% 연속 비율(자세한 내용은 추가 메뉴에서도 확인 가능) 
- **세로 읽기** — 전역 토글 
- **병음** — 기본적으로 켜져 있음 
- **원본 텍스트 중앙에** — 기본적으로 켜져 있습니다. 
- **캘리그래피 글꼴** — 몰입감 있고 디테일한 타이포그래피 

### 데이터 

- **연속 읽기** — 연속 읽기 통계 보기 
- **iCloud 동기화** — 선택 사항(12부) 
- **즐겨찾기 내보내기** — 컬렉션을 파일로 공유 

### 탭바 

- **찾아보기** 탭 표시 여부 전환(기본값은 켜짐) 
- **즐겨찾기** 탭 표시 여부 전환(기본값은 켜짐) 

### 위젯 

- **위젯 가이드** — 위젯별 지침 
- **앱 테마 따르기** 토글 

### 단축키 

- **홈 화면 빠른 작업** — 15개 중 최대 4개 선택 
- **단축키 가이드** — 복사 버튼이 포함된 딥링크 참조

### 알림 

- **매일 Ci 알림** — 활성화, 시간, 권한 상태 

### 도움말 

- **사용 가이드** — 재생 기능 둘러보기 
- **기능 가이드** — 더 깊은 기능 카드(`isongci://feature-guide`) 
- **의견 보내기** — 이메일 열기(`isongci://feedback`) 

### 소개 

- 버전 번호 
- **팁 항아리** — 선택적 인앱 구매 `com.iHTCboy.iSongCi.6`(Apple StoreKit에서 처리) 
- 앱스토어 링크 
- 온보딩 환영 재생 재생 

--- 

## 15부 — 앱 다운로드 

| 채널 | 링크 | 
|---------|------| 
| 앱스토어 | [App Store에서 다운로드](https://apps.apple.com/app/id6788433450) | 

### 시스템 요구사항 

| 플랫폼 | 최소 | 
|----------|---------| 
| 아이폰/아이패드 | iOS 17.0+(검색 탭: iOS 26.0+) | 
| 맥 | 맥OS 13.0+ | 

### 연락처 

- **이메일:** [AppleOSer@gmail.com](mailto:AppleOSer@gmail.com) — 일반적으로 48시간 이내에 답변을 드립니다. 

### 팁 용기(옵션) 

iSongCi를 즐겨하신다면 **설정 → 정보**를 통해 선택적인 팁을 고려해 보세요. 제품 ID: `com.iHTCboy.iSongCi.6`. 결제는 전적으로 Apple에서 처리됩니다. 

[FAQ](../faq) · [바로가기 링크](../url-scheme) · [개인정보취급방침](../privacy)

</section>
<section lang="ru" markdown="1">

### Приложение полностью автономно? 

Да. Все **21 592 произведения Сон Ци** включены в комплект. После установки приложение не отправляет **нулевые исходящие сетевые запросы** — ни учетной записи, ни рекламы, ни аналитики. Дополнительный iCloud использует службу Apple только при ее включении. 

### Чем это отличается от поэзии Тан/универсальных поэтических приложений? 

iSongCi **вертикальен Сун Ци (宋词)**, а не смешанный поэтический каталог Тан, Сун и Юань. Он добавляет **1461 знание cipai**, **простой перевод и современные комментарии**, **захватывающее вертикальное чтение** с помощью пиньинь, ежедневную ci, карточки общего доступа, виджеты, Центр управления, Siri и дополнительный iCloud. 

### Сколько контента включено? 

| Товар | Граф | 
|------|-------| 
| Ci работ (всего) | 21 592 | 
| Авторы | 1509 | 
| Ципай (паттерны мелодии) | 1,461 | 
| Рекомендуемый ципай с вступлением | 60 | 
| Простые переводы | 11 029 | 
| Современный комментарий | Все работы | 
| Коллекции | 12 (Хаофан 363 · Ванюэ 520 · 10 наборов тем) | 
| Династии | Пять династий, Северная Сун, Южная Сун | 

### Что такое простой перевод, классические примечания и современные комментарии? 

Три отдельных слоя на странице сведений — переключайте каждый раздел независимо:

- **Простой перевод (白话译文)** — современный китайский перевод полного текста (~11 029 работ) 
- **Классические примечания (注释)** — традиционные научные аннотации, если таковые имеются. 
- **Современные комментарии (白话赏析)** — автоматически генерируемые предыстория, суть и советы по чтению для каждой работы (для справки, а не для академического цитирования). 

### У всех работ есть переводы? 

№ **11 029** произведений включают полный простой перевод; остальные показывают оригинальный текст плюс современные комментарии. Классические примечания появляются только в том случае, если их содержат исходные данные. Приложение представляет собой студию чтения и открытий, а не полное академическое издание всех книг. 

### Как работает Today's Ci? 

Произведение выбирается **детерминированно из избранного пула** (шедевры Хаофан + Ванюэ) с использованием **календарного дня в качестве исходного** — все видят **одну и ту же ци в один и тот же день**. Оно наступает в **полночь по местному времени**. Открыто из **Дома** или `isongci://daily`. 

### Что такое интуитивная прозорливость? 

**邂逅一词** извлекает **случайную** фигуру из избранного пула — разную при каждом нажатии. Используйте **Дом → Serendipity**, `isongci://random`, виджет **Случайный Ci** или Siri. 

### Насколько точна пиньинь?

Пиньинь **генерируется автоматически** для каждого сегмента. Он хорошо работает для большинства строк, но **может неправильно читать полифонические символы** (多音字). Используйте его как средство чтения, а не как справочник по произношению. 

### Традиционный китайский дисплей? 

Пользовательский интерфейс имеет выделенные строки **繁體中文**. Текст корпуса хранится на упрощенном китайском языке и **конвертируется во время отображения** (таблица s2t на уровне символов) для традиционного режима — вам не нужны две копии базы данных. 

### Как работают вертикальное чтение и пиньинь? 

Включите глобально в **Настройки → Чтение** (вертикальная раскладка, пиньинь, каллиграфический шрифт). В любой детали работы вы можете открыть **Иммерсивное чтение** для полноэкранной вертикальной (справа налево) или горизонтальной страницы с фоном из сюань-бумаги и независимым масштабированием шрифта. 

### Что такое иммерсивное чтение? 

**Подробнее → Дополнительно → Иммерсивное чтение** открывает страницу без Chrome — идеально подходит для чтения или презентации на iPad или большом экране. Переключайте вертикаль/горизонтальность и каллиграфию внутри ридера. 

### Как изменить размер шрифта? 

Ползунок **Настройки → Чтение** или **Детализация → Дополнительно → Размер шрифта**. Масштабирует основной текст независимо от системного динамического типа; синхронизируется через iCloud, если включено. 

### Как работает чтение вслух (TTS)?

Коснитесь значка **динамика** на панели инструментов подробностей. Использует встроенный в устройство синтез речи. Пауза и возобновление с помощью той же кнопки. 

### Как работают избранное, заметки и iCloud? 

**Избранное** — нажмите ♥ на любой работе. **Личные заметки** — аннотации к каждому стихотворению, которые можете видеть только вы (страница с подробностями). Дополнительная функция **iCloud Sync** отражает избранное, заметки, внешний вид, масштаб шрифта, видимость вкладок и полосу чтения на разных устройствах. **Текст Ci никогда не загружается** — он всегда остается в пакете приложения. 

### Каковы правила полосового чтения? 

Откройте **любой город** в приложении, чтобы подсчитать этот календарный день. **Дни подряд** увеличивают вашу серию; **пропустите более одного дня**, и при следующем открытии полоса обнулится. **Общее количество прочтений** отслеживает открытые фрагменты за все время. Streak появляется на главной странице и в виджете **Reading Streak**. 

### Какие стили карточек обмена существуют? 

**13 стилей:** Классический, Чернильная смывка, Киноварная печать, Шелковый свиток, Длинный свиток, Охра-золото, Зимний снег, Зеленый пейзаж, Бамбуковые полоски, Лунное серебро, Минимальный, Темный минималистичный, Вертикальный шрифт. Выберите полный текст или отрывок; при желании включить комментарий; экспортируйте PNG с разрешением 3×. 

### Какие виджеты доступны?

| Виджет | Цель | 
|--------|---------| 
| Сегодняшний Ки | Сегодняшний выделенный фрагмент | 
| Интуитивная прозорливость | Случайные избранные ci (обновляется каждый час) | 
| Любимый Ки | Последняя отмеченная работа | 
| полоса чтения | Дни подряд + общее количество прочтений | 
| Центр управления | Открытие Today's Ci одним касанием (iOS 18+) | 

Размеры: маленький/средний/большой на главном экране; Экран блокировки круглый, линейный или прямоугольный. Поддерживает **Режим ожидания**. Язык виджетов соответствует **языку приложения**, а не системному языку. 

### Виджет показывает неправильный или пустой текст? 

1. Откройте приложение один раз после установки. 
2. Потяните, чтобы обновить главную страницу, чтобы перезаписать кеш виджетов. 
3. После смены языка ненадолго откройте приложение, чтобы обновить его. 
4. Для **Любимого фильма** требуется хотя бы одна работа, отмеченная звездочкой. 
5. **Reading Streak** требует, чтобы вы сначала открыли произведение внутри приложения. 
6. Убедитесь, что виджеты разрешены для iSongCi в настройках системы. 

### Что такое виджет Центра управления (iOS 18+)? 

Добавьте **Сегодняшний Ci** из **Настройки → Центр управления** (или редактора Центра управления системой). Требуется **iOS 18.0+**. Нажатие открывает приложение непосредственно к сегодняшнему фрагменту. 

### Какие ярлыки Siri существуют? 

Вместе с приложением поставляются три намерения приложения:

| Намерение | Пример фразы | 
|--------|----------------| 
| Открыть сегодняшнюю Ci | «Сегодняшняя ци в iSongCi» | 
| Случайное Ci | «Интуиция в iSongCi» | 
| Поиск Ки | «Поиск в iSongCi» (с ключевым словом) | 

Настройте до **4 быстрых действий на главном экране** в настройках. Полный список глубоких ссылок в [Быстрые ссылки](../url-scheme). 

### Каковы ограничения Spotlight? 

Spotlight индексирует **избранное и избранное** — до **~1000** записей. Редкие работы не будут отображаться в системном поиске; вместо этого используйте **глубокий полнотекстовый поиск в приложении** (ленивая загрузка всего корпуса). Коснитесь результата Spotlight, чтобы открыть его напрямую. 

### Могу ли я скрыть вкладки? 

Да. **Настройки → Панель вкладок** — переключение вкладок **Категории** и/или **Избранное**. Скрытые вкладки по-прежнему доступны с помощью действий с подробными сведениями, меню длительного нажатия, виджетов и ссылок `isongci://`. 




|---------|---------------|------------------| 
| Быстрые действия на главном экране | ✅ | ❌ | 
| Виджеты и Центр управления | ✅ (iOS 18+ CC) | Виджеты в основном на iPhone/iPad | 
| Тактильная обратная связь | ✅ | ❌ | 
| Вкладка «Выделенный поиск» | iOS 26+ | Поиск по кнопке/листу | 
| Основное чтение, избранное, iCloud | ✅ | ✅ | 

### Приложение бесплатное? Что такое баночка для наконечников?

**Совершенно бесплатно** — работают все 21 592 приложения и все функции, без подписки и без рекламы. **Дополнительный банк с советами** (`com.iHTCboy.iSongCi.6`) позволяет поддерживать разработку через Apple In-App Purchase; он не открывает ничего лишнего. 

### Системные требования 

| Платформа | Минимум | 
|----------|---------| 
| iPhone/iPad | iOS 17.0+ | 
| Мак | macOS 13.0+ | 
| Виджет Центра управления | iOS 18.0+ | 
| Панель перевода системы | iOS 17.4+ / macOS 14.4+ | 

### Как мне получить приложение? 

[Загрузить в App Store](https://apps.apple.com/app/id6788433450) (идентификатор приложения **6788433450**). 

### Как мне связаться со службой поддержки? 

[AppleOSer@gmail.com](mailto:AppleOSer@gmail.com) — обычно мы отвечаем в течение 48 часов. 

--- 

### Как работает непрерывное чтение? 

Включите **непрерывное чтение** в меню «Настройки» → «Чтение». После завершения работы TTS появляется нижняя полоса; если вы ничего не делаете в течение нескольких секунд, следующий элемент в текущей очереди (просмотр/плейлист/избранное/ежедневно) запускается автоматически. Вы также можете выбирать строки при создании карт акций. 

### Как работают ежедневные напоминания?

Дополнительные **локальные уведомления** напоминают вам о необходимости прочитать сегодняшнюю ci. Коснитесь уведомления, чтобы открыть подходящую работу по глубокой ссылке. Отключение уведомлений не очищает вашу полосу чтения. 

## Полное руководство пользователя 

В разделах ниже представлено полное описание продукта, ранее представленное на странице поддержки. Элементы быстрых вопросов и ответов остаются выше (если есть). 

--- 

## Часть 1 — Первый запуск и интерфейс 

### Приветственное руководство 

При первом запуске приложение представлено в **многостраничном приветственном руководстве**: масштаб библиотеки, ежедневный доступ к контенту, иммерсивное чтение, избранное, виджеты и конфиденциальность. Пролистните каждую страницу, затем нажмите **Начать**. Воспроизвести в любое время: **Настройки → Справка → Руководство по использованию** или глубокая ссылка `isongci://feature-guide`. 

### Обзор панели вкладок 

| Вкладка | Что он делает | 
|-----|----------------| 
| **Главная** | Сегодняшний Ci, Serendipity, Продолжить чтение, полоса чтения, тематические превью | 
| **Просмотр** | Авторы, ципаи, династии, жанры, тематические сборники, полный каталог | 
| **Избранное** | Помеченные работают со списком/сеткой/карточками и группировкой | 
| **Настройки** | Внешний вид, чтение, данные, вкладки, виджеты, ярлыки, справка | 
| **Поиск** | Мгновенный поиск по метаданным + ленивый полнотекстовый глубокий поиск (специальная вкладка на **iOS 26+**) |

> **Совет.** Скройте вкладку **Обзор** или **Избранное** в меню **Настройки → Панель вкладок**. Если вы закроете вкладку, на которой находитесь, приложение автоматически вернется на главную страницу. Видимость вкладок синхронизируется через дополнительный iCloud. 

### Платформы 

| Платформа | Минимум | 
|----------|---------| 
| iPhone/iPad | iOS 17.0+ | 
| Мак | macOS 13.0+ | 

Для выделенной **вкладки «Поиск**» требуется **iOS 26+**. В более ранних версиях iOS поиск доступен на странице «Обзор» или через Spotlight/Siri. 

### Конфиденциальность при установке 

- **Без регистрации · без рекламы · без аналитического SDK** 
- Корпус поставляется внутри пакета приложения — без CDN, без телеметрии. 
- Дополнительный iCloud использует только **ваш личный iCloud**; текст ci никогда не загружается 

--- 

## Часть 2 — Дом 

Вкладка **Главная** — это ваша ежедневная точка входа: кураторское открытие без поиска среди 21 592 работ. 

### Сегодняшняя Ци (每日一词) 

**Детерминированный ежедневный выбор** — один и тот же ci для всех на одну и ту же календарную дату, выбранный из полной библиотеки с помощью алгоритма, основанного на дате. Коснитесь карточки, чтобы открыть страницу с полной информацией. 

- Обновляется автоматически в **полночь по местному времени**. 
– Записывается в хранилище **группы приложений** при запуске приложения, поэтому виджеты **Daily Ci** остаются синхронизированными. 
– Глубокая ссылка: `isongci://daily`. 
- Siri: *"Сегодняшняя ci в iSongCi"*

### Интуиция (邂逅一词) 

Нажмите **Serendipity**, чтобы получить **случайно выбранную CI** — отлично, если вам нужен сюрприз, а не фиксированный выбор на сегодняшний день. Каждое нажатие извлекает новый фрагмент из автономной библиотеки. 

– Глубокая ссылка: `isongci://random`. 
- Сири: *"Интуиция в iSongCi"* 

### Продолжить чтение 

Если вы недавно открыли произведение, на главной странице появится надпись **Продолжить чтение** с названием и автором. Одним касанием возобновляется с того места, на котором вы остановились. 

- Глубокая ссылка: `isongci://continue-reading`. 
- Также доступно в качестве быстрого действия на главном экране. 

### полоса чтения 

На главной странице отображается ваша **серия чтения** – в течение нескольких дней подряд вы читали хотя бы одно ci, а также общее количество прочитанных книг. Открытие любой детали работы засчитывается в сегодняшнюю серию. 

- Синхронизируется через дополнительный **iCloud KVS**. 
- Виджет **Полоса** показывает полосу на главном экране и экране блокировки. 

### Тематические превью 

Прокрутите вниз, чтобы просмотреть карточки быстрого входа — **рекомендуемые сипай**, **коллекции тем**, жанры **豪放/婉约** и **основные моменты династии**. Нажмите **Просмотреть все**, чтобы перейти к обзору этого раздела. 

### Быстрые действия на главном экране

Нажмите и удерживайте значок приложения, чтобы открыть такие ярлыки, как **Today's Ci**, **Serendipity**, **Продолжить чтение**, **Избранное** и **Поиск**. Настройте до **4** элементов в разделе **Настройки → Ярлыки → Быстрые действия на главном экране** (доступно 15 действий — см. часть 10). 

--- 

## Часть 3 — Обзор 

Откройте вкладку **Обзор**. Несколько разделов позволяют изучить библиотеку с разных сторон: 

### 1. Авторы (名家) 

**1509 поэтов Сун Ци** с биографиями. Нажмите на автора, чтобы просмотреть его профиль и полный список работ. 

- Переключение макета с помощью **⋯**: **Список**, **Сетка** или **Карточки**. 
- Количество столбцов сетки (2–4) запоминается отдельно на iPhone и iPad. 
– Глубокая ссылка: `isongci://author?id=12`. 

### 2. Сипай (词牌) 

**1461 шаблон настройки cipai** в полном указателе. **60 избранных ципай** включают в себя вводные эссе, объясняющие форму, ритм и репрезентативное настроение. Изучите образец, а затем просмотрите произведения, написанные на эту мелодию. 

Примеры: 水调歌头, 念奴娇, 满江红, 蝶恋花, 浣溪沙. 

### 3. Династии (朝代) 

Просмотр по историческому периоду: 

| Династия | Покрытие | 
|---------|----------| 
| **五代** | Ранняя традиция *ci* до песни | 
| **北宋** | Мастера Северной песни | 
| **南宋** | Авторы текста Южной песни | 

### 4. Жанры (流派)

| Жанр | Граф | Персонаж | 
|-------|-------|-----------| 
| **豪放** | 363 | Смелый, экспансивный, героический тон | 
| **婉约** | 520 | Нежный, лирический, интимный тон | 

Работы могут включаться в одну или обе группы, где это применимо. 

### 5. Коллекции тем (主题) 

**10 тщательно подобранных тематических коллекций** — любовь, расставание, ностальгия, природа, патриотизм, философия, фестивали и многое другое. В каждой коллекции группируются ci, имеющие общий мотив. 

### 6. Полный каталог (全集) 

Полный индекс из **21 592 работ**. Используйте, если вы хотите, чтобы все было в одном прокручиваемом списке с параметрами сортировки и фильтрации. 

### Макет и параметры разделов 

Нажмите **⋯** на страницах «Обзор» или «Автор»: 

| Вариант | Что он делает | 
|--------|----------------| 
| **Макет** | Список/Сетка/Карточки | 
| **Видимость раздела** | Показать или скрыть любой раздел просмотра | 
| **Порядок разделов** | Изменение порядка отображения разделов | 
| **Столбцы сетки** | 2–4 на iPhone, 2–4 на iPad (запоминается отдельно) | 

### Запись поиска (до iOS 26) 

В iOS 17–25 откройте поиск в **поле поиска** в верхней части окна «Обзор» или с помощью Spotlight/Siri. В **iOS 26+** используйте специальную вкладку **Поиск** (часть 7). 

--- 

## Часть 4. Подробное чтение 

Коснитесь любого изображения, чтобы открыть **Подробности работы** — основной интерфейс чтения.

### Панель инструментов (вверху справа) 

| Кнопка | Действие | 
|--------|--------| 
| **♥** | Добавить или удалить из избранного (при пометке используется цвет акцента) | 
| **Спикер** | Запустите **чтение TTS вслух**; нажмите еще раз, чтобы приостановить/возобновить | 
| **⋯ Еще** | Открывает меню действий (см. ниже) | 

### Разделы контента 

Не каждая работа имеет каждый слой. Разделы появляются только тогда, когда контент существует: 

| Раздел | Покрытие | Что вы видите | 
|---------|----------|--------------| 
| **Исходный текст** | Все 21 592 | Полная ци с возможностью использования пиньинь | 
| **Классические ноты** | Где доступно | Традиционные научные аннотации | 
| **Простой перевод** | **11 029 работ** | Современный народный рендеринг | 
| **Современный комментарий** | Кураторское подмножество | Признание и литературный контекст | 
| **Введение в Сипай** | Рекомендуемые и связанные cipai | Объяснение шаблона настройки | 
| **Биография автора** | 1509 авторов | Биография поэта | 
| **Работы по теме** | Умные ссылки | Тот же автор, сипай или тема | 

Включайте и выключайте каждый раздел во время чтения. **Личные заметки** отображаются внизу — ваши личные аннотации, видимые только вам (синхронизируются через iCloud, если они включены). 

### Еще меню (⋯)

| Товар | Что он делает | 
|------|----------------| 
| **Размер шрифта** | Открывает панель масштабирования (50%–300%, базовый размер по умолчанию 22 пт) | 
| **Захватывающее чтение** | Полноэкранный просмотр без отвлекающих факторов (Часть 5) | 
| **Пиньинь** | Переопределение глобальной настройки пиньинь для каждой работы | 
| **Вертикальная компоновка** | Индивидуальное переопределение направления чтения | 
| **Скопировать полный текст** | Копирует все данные в буфер обмена | 
| **Поделиться текстом** | Системный общий лист с обычным текстом | 
| **Создать карту акций** | Открывает редактор карточек изображений в стиле 13 (Часть 11) | 
| **Личное сообщение** | Добавьте или отредактируйте свою личную заметку к этой работе | 

### Параметры чтения 

- **Пиньинь** — глобальное значение по умолчанию в настройках; переопределение для каждой работы подробно 
- **Вертикальная раскладка** — классическое чтение сверху вниз; переопределить за работу 
- **Центрировать исходный текст** — включено по умолчанию; выравнивает основной текстовый блок 
- **Системный перевод** (iOS 17.4+) — панель перевода Apple для выделенного текста. 
- **Переключение разделов** — показать/скрыть перевод, заметки, комментарии, вступление Cipai, биографию автора. 

### TTS, чтение вслух 

Коснитесь значка **динамика**, чтобы озвучить текст на устройстве. Использует системные голоса — нет сети. Идеально подходит для прослушивания во время поездок на работу или изучения произношения с видимой пиньинь.

### Длительное нажатие на строки списка 

В любом рабочем списке **удерживайте** строку, чтобы выполнить быстрые действия: **Избранное**, **Читать вслух**, **Поделиться** или **Удалить из истории** (в режиме просмотра истории). 

### Глубокая ссылка 

Открыть конкретную работу по идентификатору каталога: `isongci://poem?id=42` 

--- 

## Часть 5. Иммерсивное чтение 

Из подробностей **Дополнительно → Иммерсивное чтение** откройте чистую полноэкранную страницу, предназначенную для чтения, презентации и целенаправленного изучения. 

### Макет 

- **Вертикально** — классическая прокрутка сверху вниз (по умолчанию для погружения). 
- **Горизонтальное** — современный поток слева направо. 
- Переключение в любое время в режиме погружения; предпочтение может следовать глобальным настройкам 

### Типографика и атмосфера 

- **Шрифт в стиле каллиграфии** для основного текста — напоминает написанную кистью Сун Ци. 
- **Фон из бумаги Сюань (宣纸)** — теплая, фактурная литературная атмосфера. 
- Адаптируется к вашей **светлой/темной/системной теме** и **акцентному цвету** 

### Элементы управления 

– Сведите пальцы или используйте элемент управления **Масштаб шрифта** (50–300%). 
- Нажмите, чтобы показать/скрыть Chrome (панель инструментов, переключатели разделов). 
- **TTS** доступен, не выходя из режима погружения. 
- Проведите пальцем по экрану или используйте стрелки для перехода к **предыдущей/следующей** работе в контексте текущего списка. 

### Лучше всего для

- Презентация iPad или настольное чтение 
- Практика запоминания и декламации. 
- Скриншоты и подготовка карты обмена 

--- 

## Часть 6 — Избранное 

### Актерские работы 

Нажмите **♥** на любой детали работы или нажмите и удерживайте строку списка → **Избранное**. В избранных строках в качестве звездочки используется ваш **акцентный цвет**. 

### Макеты вкладок «Избранное» 

Откройте вкладку **Избранное**. Нажмите **⋯**, чтобы переключиться: 

| Макет | Лучшее для | 
|--------|----------| 
| **Список** | Плотное сканирование с указанием названия, автора, cipai | 
| **Сетка** | Визуальный просмотр с регулируемыми колонками | 
| **Карты** | Большие карточки предварительного просмотра с отрывком | 

### Группировка 

Организуйте свою коллекцию следующим образом: 

| Группировать по | Поведение | 
|----------|----------| 
| **Автор** | Кластеры произведений под каждого поэта | 
| **Династия** | 五代 / 北宋 / 南宋 разделы | 
| **Сипай** | Группы по шаблону мелодии | 

### Пакетное редактирование 

Нажмите **Изменить** на странице «Избранное»: 

- **Множественный выбор** работает с галочками. 
- **Выбрать все/Отменить выбор** 
- **Пакетное удаление** из избранного (с подтверждением) 

Проведите по строке влево, чтобы выполнить быстрое действие **Удалить**. 

### Любимый виджет Ci 

Виджет **Favorite Ci** на главном экране позволяет просматривать отмеченные вами работы — персональный ежедневный выбор из вашей собственной коллекции. 

### Экспорт

**Настройки → Данные → Экспортировать избранное** — поделитесь своей коллекцией в виде файла для резервного копирования или переноса. 

--- 

## Часть 7 — Поиск 

Если вы предпочитаете рисовать символы, а не вводить пиньинь, в iOS откройте **поиск текстов по рукописному вводу** с помощью элемента управления рядом с главным поиском. 

iSongCi предлагает **двухуровневый автономный поиск** — сначала быстрые метаданные, а при необходимости — глубокий полнотекстовый поиск. 

### Уровень 1 — Мгновенный поиск метаданных 

По мере ввода приложение мгновенно сопоставляет связанные метаданные: 

- **Титулы** (имена ci) 
- **Имена авторов** 
- **Имена сипаев** 
- **Теги и категории** 

Нет счетчика загрузки — результаты появляются при каждом нажатии клавиши. 

### Уровень 2 — Ленивый полнотекстовый глубокий поиск 

Для совпадений на уровне строки внутри тел ci приложение лениво загружает **`fulltext.json`** из пакета при первом использовании глубокого поиска. После однократной загрузки полнотекстовый поиск выполняется полностью на устройстве. 

– Соответствует **любой строке** в корпусе из 21 592 работ. 
- Чуть медленнее при первом запуске глубокого поиска; кэшируется после этого 
- **Нулевая сеть** — файл поставляется вместе с приложением. 

### Вкладка «Выделенный поиск» (iOS 26+) 

В **iOS 26 и более поздних версиях** функция «Поиск» имеет собственную вкладку на панели вкладок. В более ранних версиях используйте поле поиска в разделе **Обзор** или системной интеграции ниже. 

### Прожектор

Приложение индексирует до **~1,000 произведений** для системного поиска Spotlight. Нажмите на результат Spotlight, чтобы открыть это произведение напрямую в iSongCi.

### Siri и глубокие ссылки

- Siri: *"Поиск в iSongCi"* (с ключевым словом)
- Глубокая ссылка: `isongci://search?q=明月`

### Советы по поиску

| Совет | Почему |
|-------|-------|
| Ищите автора + ключевое слово | Сужает большой набор результатов |
| Попробуйте название ципая | Находит все произведения в данной тональности |
| Используйте известную строку | Активирует полнотекстовый уровень для совпадения строки |
| Ищите на традиционном китайском | UI конвертирует; корпус соответствует упрощенному исходнику |

---

## Часть 8 — Темы и внешний вид

Откройте **Настройки → Внешний вид**.

### Режим темы

| Режим | Поведение |
|-------|----------|
| **Светлый** | Фон для чтения яркий как бумага |
| **Темный** | Фон для чтения тёмный как чернила ночью |
| **Системный** | Следует за внешним видом iOS / macOS |

### Акцентный цвет — 15 предустановок + собственный

Выберите из **15 предустановок темы**, вдохновленных эстетикой династии Сун:

| # | Предустановленные | Настроение | 
|---|--------|------| 
| 1 | 水墨 Чернила | Нейтральный литературный серый | 
| 2 | 胭脂 Руж | Теплый малиновый акцент | 
| 3 | 朱砂 Киноварь | Классический тюлень-красный | 
| 4 | 青瓷 Селадон | Прохладная зеленая глазурь | 
| 5 | 松绿 Сосна | Глубокий зеленый лес | 
| 6 | 黛蓝 Индиго | Ученый сине-черный | 
| 7 | 群青 Лазурный | Яркий минеральный синий | 
| 8 | 青莲 Лотос | Фиолетово-синий цветок | 
| 9 | 琥珀 Янтарь | Золотой теплый тон | 
| 10 | 赭金 Охра | Земляной золотисто-коричневый | 
| 11 | 月白 Луна | Бледно-серебристо-белый | 
| 12 | 竹青 Бамбук | Свежий зеленый бамбук | 
| 13 | 藕荷 Корень лотоса | Нежный розово-лавандовый | 
| 14 | 玄色 Ebony | Глубокий черный акцент | 
| 15 | 缃色 Шелк | Старая рукопись желтого цвета | 

Тапните любой образец — выбранное кольцо + галочка. Или выберите **Пользовательский**, чтобы выбрать любой цвет из системной палитры цветов. 

Цвет акцента применяется к избранным звездочкам, кнопкам, выделениям, акцентам на карточках и оттенку виджета (когда включен параметр **Следовать за темой приложения**). 

### Язык 

**Английский / 简体中文 / 繁體中文** — пользовательский интерфейс переключается мгновенно. Текст корпуса хранится на упрощенном китайском языке; Традиционный дисплей использует преобразование на устройстве. 

### синхронизация с iCloud 

**Внешний вид** (светлый/темный/системный), **настройка акцентов** и **масштаб шрифта** синхронизируются через дополнительный iCloud KVS. 

--- 

## Часть 9 — Виджеты

### Добавьте виджет на главный экран 

1. Нажмите и удерживайте главный экран → **Редактировать главный экран** → нажмите **+**. 
2. Найдите **iSongCi** / **爱宋词** 
3. Выберите тип и размер виджета → **Добавить виджет**. 

### Типы виджетов 

| Виджет | Размеры | Поведение | 
|--------|-------|----------| 
| **Дейли Си** | Маленький/Средний/Большой + Экран блокировки | Сегодняшняя детерминированная ci; кран открывает подробно | 
| **Случайное число** | Маленький/Средний/Большой + Экран блокировки | Выбор по счастливой случайности; обновление на временной шкале | 
| **Любимый Ки** | Малый/Средний | Перелистывает избранное | 
| **Полоса** | Маленький/круглый (экран блокировки) | Чтение количества полос и значок пламени | 

### Виджеты экрана блокировки 

При добавлении виджетов переключитесь на страницу настройки **Экран блокировки** и выберите прямоугольные, круглые или встроенные аксессуары iSongCi. 

### Тема виджета 

**Настройки → Виджеты → Следовать теме приложения** — виджеты соответствуют вашему выбору: светлый/темный/акцентный. 

### Центр управления (iOS 18+) 

Добавьте элементы управления для **Today's Ci**, **Serendipity** и **Поиска** из **Настройки → Центр управления** на iOS 18 и более поздних версиях. 

### Устранение неполадок виджетов

- Откройте приложение один раз после установки, чтобы ежедневный кеш ci записался в App Group
- Если текст выглядит неправильно после смены языка, просто откройте приложение — это автоматически обновит кеши виджетов
- Ежедневный виджет Ci обновляется в полночь по местному времени
- Виджет Random Ci обновляет таймлайн периодически для разнообразия

### Руководство по виджетам в приложении

**Настройки → Виджеты → Руководство по виджетам** или `isongci://widget-guide` для скриншотов и советов по каждому виджету.

---

## Часть 10 — Siri, команды и действия на главном экране

### Siri intents (3)

| Команда | Пример фразы |
|--------|----------------|
| **Сегодняшний Ci** | "Сегодняшний ci в iSongCi" |
| **Случайность** | "Случайность в iSongCi" |
| **Поиск Ci** | "Поиск в iSongCi" (с ключевым словом) |

Добавьте их в приложение **Команды** для автоматизаций — например, открыть `isongci://daily` каждое утро.

### Быстрые действия на главном экране (15 доступны, максимум 4 можно включить)

Длительное нажатие на иконку приложения. Настройте в **Настройки → Команды → Быстрые действия на главном экране**:

| # | Действие | Открывается | 
|---|--------|-------| 
| 1 | Сегодняшний Ки | `isongci://daily` | 
| 2 | Интуитивная прозорливость | `isongci://random` | 
| 3 | Продолжить чтение | `isongci://continue-reading` | 
| 4 | Избранное | `isongci://favorites` | 
| 5 | Поиск | `isongci://search` | 
| 6 | Обзор | `isongci://category` | 
| 7 | Главная | `isongci://home` | 
| 8 | Настройки | `isongci://settings` | 
| 9 | Руководство по использованию | `isongci://usage-guide` | 
| 10 | Руководство по виджетам | `isongci://widget-guide` | 
| 11 | Руководство по ярлыкам | `isongci://shortcuts-guide` | 
| 12 | Руководство по функциям | `isongci://feature-guide` | 
| 13 | Обратная связь | `isongci://feedback` | 
| 14 | Обзор в приложении | `isongci://in-app-review` | 
| 15 | Главная Настройки ярлыков | `isongci://home-shortcuts` | 

В меню значков одновременно отображаются только **4** — выберите четыре наиболее часто используемых. 

### Глубокие ссылки (`isongci://`) 

Полная ссылка: [Ярлыки ссылок](../url-scheme). Общие URL-адреса: 

| URL-адрес | Открывается | 
|-----|-------| 
| `isongci://poem?id=42` | Детализация Ci по ID каталога | 
| `isongci://author?id=12` | Профиль автора | 
| `isongci://daily` | Сегодняшний Ки | 
| `isongci://random` | Интуитивная прозорливость | 
| `isongci://continue-reading` | Продолжить чтение | 
| `isongci://search?q=明月` | Искать 明月 | 
| `isongci://favorites` | Вкладка «Избранное» | 

Используйте в профилях конфигурации «Ярлыки», «Заметки», Safari или MDM. 

### Руководство по сочетаниям клавиш в приложении

**Настройки → Ярлыки → Руководство по ярлыкам** или `isongci://shortcuts-guide` — кнопки копирования одним нажатием для каждого URL-адреса. 

--- 

## Часть 11 — Общие карты (13 стилей) 

Из подробностей **Подробнее → Создать карту акций**: 

| Стиль | Настроение | 
|-------|------| 
| Классический | Чистый литературный макет | 
| Чернила | Эстетика чистки и мытья | 
| Минимальный | Ориентирован на типографику | 
| Вертикальный | Классический сверху вниз | 
| Киноварь | Тюленево-красный акцент | 
| Темный | Ночной фон чернил | 
| Селадон | Прохладный керамический зеленый | 
| Охра-золото | Теплый золотой тон | 
| Белоснежка | Яркая белая бумага | 
| Прокрутка | Горизонтальный мотив прокрутки | 
| Луна белая | Бледная лунная палитра | 
| Бамбуковая тень | Зеленая текстура бамбука | 
| Сюань бумага | Текстурированный фон 宣纸 | 

### Параметры экспорта 

- **Полный текст** или **отрывок** – запомнить на следующий раз. 
- **Разрешение 3×** PNG — четкость на дисплеях Retina и в социальных сетях. 
- **Экспортировать PNG** – сохранить в фотографиях или поделиться через любое приложение. 
- Предпочтения стиля сохраняются автоматически. 

Разрешение **Библиотека фотографий (Добавить)** требуется только при сохранении в «Фото» — только запись, без доступа для чтения. 

--- 

## Часть 12 — Синхронизация с iCloud 

Дополнительная синхронизация через **iCloud Key-Value Store** — без сервера iHTC Studio.

| Синхронизировано | Не синхронизировано | 
|--------|------------| 
| Избранное | Выбор быстрых действий на главном экране | 
| Личные заметки | Флажки регистрации/приветствия | 
| Внешний вид (светлый/темный/системный) | Состояние виджета в случайном порядке | 
| Цвет акцента и масштаб шрифта | Ci-текст (всегда в комплекте приложения) | 
| Видимость вкладки «Обзор/Избранное» | Полнотекстовый поиск в кэше | 
| Полоса чтения | Пользовательский оттенок выбора акцента (повторный выбор на новом устройстве) | 

Включите: **Настройки → Данные → Синхронизация с iCloud**. Требуется вход в iCloud на устройстве. **Текст Ci никогда не загружается** — только ваши личные данные и предпочтения. 

--- 

## Часть 13. Уведомления 

### Ежедневное напоминание о Ci 

Дополнительное **локальное уведомление** напоминает вам о необходимости прочитать сегодняшнюю ci. 

| Настройка | Расположение | 
|---------|----------| 
| Включить/отключить | **Настройки → Уведомления** | 
| Время напоминания | Выберите предпочитаемый час и минуту | 
| Разрешение | iOS запрашивает при первом включении — сервер не задействован | 

Уведомления **планируются исключительно на устройстве**. Никакого push-сервера, никакого пикселя отслеживания, никакой удаленной полезной нагрузки. 

### Советы

- Если напоминания прекращаются после обновления iOS, откройте приложение один раз, чтобы перенести расписание. 
- Отключение уведомлений не влияет на логику полос чтения. 
- Полосы засчитываются, когда вы открываете любую информацию о работе — уведомление является необязательным и является лишь дополнительным поощрением. 

--- 

## Часть 14 — Настройки и руководства 

Откройте **Настройки**. Разделы сверху вниз: 

### Внешний вид 

- **Тема** — Светлая/Тёмная/Системная. 
- **Акцентный цвет** — 15 пресетов + собственный (часть 8) 
- **Язык** — английский / 简体中文 / 繁體中文 

### Чтение 

- **Ползунок размера шрифта** — непрерывный масштаб 50–300 % (также подробно в меню «Дополнительно») 
- **Вертикальное чтение** — глобальный переключатель. 
- **Пиньинь** — включено по умолчанию. 
- **Центрировать исходный текст** — включено по умолчанию. 
- **Шрифт «Каллиграфия»** — эффектная и детализированная типографика. 

### Данные 

- **Reading streak** — просмотр статистики серий. 
- **Синхронизация с iCloud** — необязательно (часть 12) 
- **Экспортировать избранное** — поделиться коллекцией в виде файла. 

### Панель вкладок 

– Переключить видимость вкладки **Обзор** (по умолчанию включено). 
– Переключить видимость вкладки **Избранное** (по умолчанию включено). 

### Виджеты 

- **Руководство по виджетам** — инструкции для каждого виджета. 
- Переключатель **Следовать за темой приложения**. 

### Ярлыки 

- **Быстрые действия на главном экране** — выберите до 4 из 15. 
- **Руководство по ярлыкам** — справочник по глубоким ссылкам с кнопками копирования.

### Уведомления 

- **Ежедневное напоминание о Ci** — включение, время, статус разрешения. 

### Помощь 

- **Руководство по использованию** — обзор функций воспроизведения. 
- **Руководство по функциям** — карточки с более глубокими функциями (`isongci://feature-guide`). 
- **Отправить отзыв** — открывает электронное письмо (`isongci://feedback`). 

### О нас 

- Номер версии 
- **Банка с советами** — дополнительная покупка в приложении `com.iHTCboy.iSongCi.6` (обслуживается Apple StoreKit) 
- Ссылка на магазин приложений 
- Повтор приветствия при регистрации 

--- 

## Часть 15. Загрузите приложение 

| Канал | Ссылка | 
|---------|------| 
| Магазин приложений | [Загрузить в App Store](https://apps.apple.com/app/id6788433450) | 

### Системные требования 

| Платформа | Минимум | 
|----------|---------| 
| iPhone/iPad | iOS 17.0+ (вкладка «Поиск»: iOS 26.0+) | 
| Мак | macOS 13.0+ | 

### Контакт 

- **Электронная почта:** [AppleOSer@gmail.com](mailto:AppleOSer@gmail.com) — обычно мы отвечаем в течение 48 часов. 

### Дополнительный контейнер для наконечников 

Если вам нравится iSongCi, воспользуйтесь дополнительным советом в разделе **Настройки → О программе**. Идентификатор продукта: `com.iHTCboy.iSongCi.6`. Платеж полностью обрабатывается Apple. 

[Часто задаваемые вопросы](../faq) · [Быстрые ссылки](../url-scheme) · [Политика конфиденциальности](../privacy)

</section>
<section lang="th" markdown="1">

### แอปออฟไลน์โดยสมบูรณ์หรือไม่ 

ใช่. ผลงาน **21,592 Song Ci** ทั้งหมดรวมอยู่ในชุดเดียวกัน หลังจากติดตั้งแอปแล้ว **คำขอเครือข่ายขาออกเป็นศูนย์** — ไม่มีบัญชี ไม่มีโฆษณา ไม่มีการวิเคราะห์ iCloud เสริมจะใช้บริการของ Apple เฉพาะเมื่อคุณเปิดใช้งานเท่านั้น 

### สิ่งนี้แตกต่างจากแอปบทกวี Tang / บทกวีทั่วไปอย่างไร 

iSongCi เป็น **แนวตั้งสำหรับ Song Ci (宋词)** — ไม่ใช่แคตตาล็อกบทกวี Tang/Song/Yuan แบบผสม เพิ่มความรู้ **1,461 cipai**, **การแปลแบบธรรมดาและคำอธิบายสมัยใหม่**, **การอ่านแนวตั้งที่สมจริง** ด้วยพินอิน, CI รายวัน, การ์ดแชร์, วิดเจ็ต, ศูนย์ควบคุม, Siri และ iCloud เสริม 

### รวมเนื้อหาเท่าไหร่? 

| รายการ | นับ | 
|-|-------| 
| งาน Ci (ทั้งหมด) | 21,592 | 
| ผู้เขียน | 1,509 | 
| Cipai (รูปแบบการปรับแต่ง) | 1,461 | 
| cipai ที่โดดเด่นพร้อมอินโทร | 60 | 
| แปลธรรมดา | 11,029 | 
| ความเห็นสมัยใหม่ | ผลงานทั้งหมด | 
| คอลเลกชัน | 12 (Haofang 363 · Wanyue 520 · 10 ธีมชุด) | 
| ราชวงศ์ | ห้าราชวงศ์ ซ่งเหนือ ซ่งใต้ | 

### คำแปลธรรมดา บันทึกคลาสสิก และคำอธิบายสมัยใหม่คืออะไร 

สามเลเยอร์แยกกันในหน้ารายละเอียด — สลับแต่ละส่วนแยกกัน:

- **การแปลธรรมดา (白话译文)** — การแสดงข้อความฉบับเต็มในภาษาจีนสมัยใหม่ (~ 11,029 งาน) 
- **บันทึกคลาสสิก (注释)** — คำอธิบายประกอบทางวิชาการแบบดั้งเดิม หากมี 
- **คำอธิบายสมัยใหม่ (白话赏析)** — พื้นหลัง สาระสำคัญ และเคล็ดลับการอ่านที่สร้างขึ้นโดยอัตโนมัติสำหรับงานทุกชิ้น (สำหรับการอ้างอิง ไม่ใช่การอ้างอิงทางวิชาการ) 

### งานทั้งหมดมีการแปลมั้ย? 

ลำดับที่ งาน **11,029** มีการแปลธรรมดาฉบับเต็ม; ส่วนที่เหลือแสดงข้อความต้นฉบับพร้อมคำอธิบายสมัยใหม่ บันทึกย่อแบบคลาสสิกจะปรากฏเฉพาะเมื่อมีข้อมูลต้นฉบับเท่านั้น แอปนี้เป็นสตูดิโอการอ่านและการค้นพบ ไม่ใช่ฉบับวิชาการฉบับเต็มของทุกฉบับ 

### Ci ของวันนี้ทำงานอย่างไร? 

ผลงานชิ้นหนึ่งจะถูกเลือก **ตามที่กำหนดจากกลุ่มผลงานเด่น** (ผลงานชิ้นเอกของฮ่าวฟาง + ว่านเยว่) โดยใช้ **วันตามปฏิทินเป็นเมล็ดพันธุ์** — ทุกคนจะเห็น **CI เดียวกันในวันเดียวกัน** โดยจะทบยอดในเวลา **เที่ยงคืนของท้องถิ่น** เปิดจาก **บ้าน** หรือ `isongci://daily` 

### Serendipity คืออะไร? 

**邂逅一词** ดึงชิ้นส่วน **สุ่ม** จากกลุ่มที่แนะนำ — การแตะแต่ละครั้งจะแตกต่างกัน ใช้ **หน้าแรก → Serendipity**, `isongci://random`, วิดเจ็ต **Random Ci** หรือ Siri 

### พินอินแม่นยำแค่ไหน?

พินอิน **สร้างขึ้นอัตโนมัติ** ต่อเซ็กเมนต์ ใช้งานได้ดีกับบรรทัดส่วนใหญ่ แต่ **อาจอ่านอักขระโพลีโฟนิกผิด** (多音字) ใช้เป็นเครื่องช่วยอ่าน ไม่ใช่ผู้มีอำนาจในการออกเสียง 

### การแสดงแบบจีนดั้งเดิม? 

UI ได้เฉพาะสตริง **繁體中文** ข้อความคอร์ปัสจะถูกจัดเก็บเป็นภาษาจีนตัวย่อและ **แปลง ณ เวลาที่แสดง** (ตาราง s2t ระดับอักขระ) สำหรับโหมดดั้งเดิม คุณไม่จำเป็นต้องมีสำเนาฐานข้อมูลสองชุด 

### การอ่านแนวตั้งและพินอินทำงานอย่างไร 

เปิดทั่วโลกใน **การตั้งค่า → การอ่าน** (รูปแบบแนวตั้ง พินอิน แบบอักษรประดิษฐ์ตัวอักษร) ในรายละเอียดงานใดๆ คุณสามารถเปิด **การอ่านแบบสมจริง** สำหรับหน้าแนวตั้ง (ขวาไปซ้าย) หรือแนวนอนแบบเต็มหน้าจอที่มีพื้นหลังแบบกระดาษซวนและการปรับขนาดแบบอักษรที่เป็นอิสระ 

### การอ่านอย่างดื่มด่ำคืออะไร? 

**รายละเอียด → เพิ่มเติม → การอ่านแบบดื่มด่ำ** เปิดหน้าที่ไม่มีโครเมียม — เหมาะสำหรับการท่องหรือนำเสนอบน iPad หรือหน้าจอขนาดใหญ่ สลับแนวตั้ง/แนวนอนและการประดิษฐ์ตัวอักษรภายในเครื่องอ่าน 

### ฉันจะเปลี่ยนขนาดตัวอักษรได้อย่างไร? 

แถบเลื่อน **การตั้งค่า → การอ่าน** หรือ **รายละเอียด → เพิ่มเติม → ขนาดตัวอักษร** ปรับขนาดข้อความเนื้อหาโดยไม่ขึ้นอยู่กับประเภทไดนามิกของระบบ ซิงค์ผ่าน iCloud หากเปิดใช้งาน 

### การอ่านออกเสียง (TTS) ทำงานอย่างไร

แตะไอคอน **ลำโพง** บนแถบเครื่องมือรายละเอียด ใช้การสังเคราะห์เสียงพูดภาษาจีนกลางบนอุปกรณ์ หยุดชั่วคราวและเล่นต่อด้วยปุ่มเดียวกัน 

### รายการโปรด โน้ต และ iCloud ทำงานอย่างไร 

**รายการโปรด** — แตะ ♥ ในงานใดก็ได้ **บันทึกส่วนตัว** — คำอธิบายประกอบต่อบทกวีที่คุณเห็นเท่านั้น (หน้ารายละเอียด) ตัวเลือก **iCloud Sync** จะสะท้อนรายการโปรด บันทึก ลักษณะ ขนาดแบบอักษร การมองเห็นแท็บ และแนวการอ่านบนอุปกรณ์ต่างๆ **ข้อความ Ci ไม่เคยอัปโหลด** — ข้อความจะยังคงอยู่ใน App Bundle เสมอ 

### กฎแนวการอ่านคืออะไร? 

เปิด **ใด ๆ ci** ในแอปเพื่อนับวันตามปฏิทินนั้น **วันติดต่อกัน** เพิ่มสตรีคของคุณ **ข้ามมากกว่าหนึ่งวัน** และสตรีคจะรีเซ็ตเป็นศูนย์ในการเปิดครั้งถัดไป **จำนวนการอ่านทั้งหมด** ติดตามจำนวนชิ้นที่เปิดตลอดอายุการใช้งาน Streak ปรากฏบนหน้าแรกและวิดเจ็ต **Reading Streak** 

### มีรูปแบบบัตรแชร์อะไรบ้าง? 

**13 สไตล์:** คลาสสิก, Ink Wash, Cinnabar Seal, Silk Scroll, Scroll Long, ทองคำสีเหลืองสด, หิมะฤดูหนาว, ภูมิทัศน์สีเขียว, ใบไผ่, สีเงินแสงจันทร์, มินิมอล, ดาร์กมินิมอล, สคริปต์แนวตั้ง เลือกข้อความเต็มหรือข้อความที่ตัดตอนมา เลือกที่จะรวมความเห็น; ส่งออก PNG ที่ความละเอียด 3 × 

### มีวิดเจ็ตอะไรบ้าง?

| วิดเจ็ต | วัตถุประสงค์ | 
|--------|---------| 
| ซีวันนี้ | ผลงานไฮไลท์ประจำวันนี้ | 
| เซเรนดิพิตี้ | สุ่มแนะนำ ci (รีเฟรชทุกชั่วโมง) | 
| Ci ที่ชื่นชอบ | ผลงานที่ติดดาวล่าสุด | 
| การอ่านสตรีค | จำนวนวันติดต่อกัน + จำนวนการอ่านทั้งหมด | 
| ศูนย์ควบคุม | แตะเพียงครั้งเดียวเปิด Ci ของวันนี้ (iOS 18+) | 

ขนาด: เล็ก / กลาง / ใหญ่บนหน้าจอหลัก; ล็อคหน้าจอเป็นวงกลม อินไลน์ หรือสี่เหลี่ยม รองรับ **สแตนด์บาย** ภาษาวิดเจ็ตเป็นไปตาม **ภาษาในแอป** ไม่ใช่ภาษาของระบบ 

### วิดเจ็ตแสดงข้อความผิดหรือว่างเปล่า? 

1. เปิดแอปหนึ่งครั้งหลังจากติดตั้ง 
2. ดึงเพื่อรีเฟรชบนหน้าแรกเพื่อเขียนแคชวิดเจ็ตใหม่ 
3. หลังจากเปลี่ยนภาษาแล้ว ให้เปิดแอปสั้นๆ เพื่อรีเฟรช 
4. **Ci ที่ชื่นชอบ** ต้องมีงานที่ติดดาวอย่างน้อยหนึ่งงาน 
5. **Reading Streak** ต้องการให้คุณเปิดงานในแอปก่อน 
6. ตรวจสอบให้แน่ใจว่าวิดเจ็ตได้รับอนุญาตสำหรับ iSongCi ในการตั้งค่าระบบ 

### วิดเจ็ตศูนย์ควบคุม (iOS 18+) คืออะไร? 

เพิ่ม **Ci ของวันนี้** จาก **การตั้งค่า → ศูนย์ควบคุม** (หรือตัวแก้ไขศูนย์ควบคุมระบบ) ต้องใช้ **iOS 18.0+** การแตะจะเปิดแอปโดยตรงไปยังชิ้นส่วนของวันนี้ 

### มีทางลัด Siri อะไรบ้าง? 

App Intents สามรายการมาพร้อมกับแอป:

| เจตนา | ตัวอย่างวลี | 
|--------|----------------| 
| เปิด Ci ของวันนี้ | “วันนี้ใน iSongCi” | 
| สุ่ม Ci | "ความบังเอิญใน iSongCi" | 
| ค้นหา C | "ค้นหาใน iSongCi" (พร้อมคำสำคัญ) | 

กำหนดค่าการดำเนินการด่วนสูงสุด **4 รายการบนหน้าจอหลัก** ในการตั้งค่า รายการลิงก์ในรายละเอียดแบบเต็มใน [ลิงก์ทางลัด](../url-scheme) 

### ข้อจำกัดของ Spotlight คืออะไร 

Spotlight จัดทำดัชนี **กลุ่มรายการเด่นบวกรายการโปรดของคุณ** — มากถึง **~1,000** รายการ ผลงานหายากจะไม่ปรากฏในการค้นหาระบบ ใช้ **การค้นหาข้อความแบบเต็มเชิงลึกในแอป** แทน (ขี้เกียจโหลดคลังข้อมูลทั้งหมด) แตะผลลัพธ์ Spotlight เพื่อเปิด ci นั้นโดยตรง 

### ฉันสามารถซ่อนแท็บได้หรือไม่ 

ใช่. **การตั้งค่า → แถบแท็บ** — สลับแท็บ **หมวดหมู่** และ/หรือ **รายการโปรด** แท็บที่ซ่อนไว้ยังคงสามารถเข้าถึงได้ผ่านการดำเนินการโดยละเอียด เมนูแบบกดยาว วิดเจ็ต และลิงก์ `isongci://` 




|---------|---------------|------------------| 
| การดำเนินการด่วนบนหน้าจอหลัก | ✅ | ❌ | 
| วิดเจ็ตและศูนย์ควบคุม | ✅ (iOS 18+ CC) | วิดเจ็ตบน iPhone/iPad เป็นหลัก | 
| การตอบสนองแบบสัมผัส | ✅ | ❌ | 
| แท็บค้นหาเฉพาะ | iOS 26+ | ค้นหาด้วยปุ่ม / แผ่น | 
| การอ่านหลัก, รายการโปรด, iCloud | ✅ | ✅ | 

### แอพฟรีหรือเปล่า? ขวดทิปคืออะไร?

**ฟรีโดยสมบูรณ์** — ผลงานทั้งหมด 21,592 รายการและทุกฟีเจอร์ ไม่ต้องสมัครสมาชิก ไม่มีโฆษณา **ขวดทิปเสริม** (`com.iHTCboy.iSongCi.6`) ช่วยให้คุณสนับสนุนการพัฒนาผ่านการซื้อในแอปของ Apple มันปลดล็อคไม่มีอะไรพิเศษ 

### ความต้องการของระบบ 

| แพลตฟอร์ม | ขั้นต่ำ | 
|----------|---------| 
| ไอโฟน/ไอแพด | iOS 17.0+ | 
| แม็ค | macOS 13.0+ | 
| วิดเจ็ตศูนย์ควบคุม | iOS 18.0+ | 
| แผงการแปลระบบ | iOS 17.4+ / macOS 14.4+ | 

### ฉันจะรับแอปได้อย่างไร 

[ดาวน์โหลดบน App Store](https://apps.apple.com/app/id6788433450) (รหัสแอป **6788433450**) 

### ฉันจะติดต่อฝ่ายสนับสนุนได้อย่างไร 

[AppleOSer@gmail.com](mailto:AppleOSer@gmail.com) — โดยทั่วไปเราจะตอบกลับภายใน 48 ชั่วโมง 

--- 

### การอ่านต่อเนื่องทำงานอย่างไร? 

เปิดใช้งาน **การอ่านต่อเนื่อง** ในการตั้งค่า → การอ่าน หลังจากที่งานเสร็จสิ้น TTS แถบด้านล่างจะปรากฏขึ้น ถ้าคุณไม่ทำอะไรเลยสักสองสามวินาที รายการถัดไปในคิวปัจจุบัน (เรียกดู / เพลย์ลิสต์ / รายการโปรด / รายวัน) จะเริ่มทำงานโดยอัตโนมัติ คุณยังสามารถเลือกบรรทัดเมื่อสร้างการ์ดแชร์ได้ 

### การแจ้งเตือนรายวันทำงานอย่างไร

ตัวเลือก **การแจ้งเตือนในท้องถิ่น** เตือนให้คุณอ่าน Ci ของวันนี้ แตะการแจ้งเตือนเพื่อเปิดงานที่ตรงกันผ่านลิงก์ในรายละเอียด การปิดใช้งานการแจ้งเตือนไม่ได้ช่วยล้างแนวการอ่านของคุณ 

## คู่มือการใช้งานฉบับสมบูรณ์ 

ส่วนด้านล่างนี้คือคำแนะนำผลิตภัณฑ์ฉบับเต็มก่อนหน้านี้ในหน้าสนับสนุน รายการถามตอบด่วนยังคงอยู่ด้านบน (ถ้ามี) 

--- 

## ส่วนที่ 1 — การเปิดตัวครั้งแรกและอินเทอร์เฟซ 

### ยินดีต้อนรับคำแนะนำ 

ในการเปิดตัวครั้งแรก **คู่มือต้อนรับแบบหลายหน้า** จะแนะนำแอป — ขนาดห้องสมุด, Ci รายวัน, การอ่านแบบดื่มด่ำ, รายการโปรด, วิดเจ็ต และความเป็นส่วนตัว ปัดผ่านแต่ละหน้า จากนั้นแตะ **เริ่มต้น** เล่นซ้ำได้ทุกเมื่อ: **การตั้งค่า → ความช่วยเหลือ → คู่มือการใช้งาน** หรือลิงก์ในรายละเอียด `isongci://feature-guide` 

### ภาพรวมแถบแท็บ 

| แท็บ | มันทำอะไร | 
|-----|----------------| 
| **บ้าน** | Ci ของวันนี้ Serendipity อ่านต่อ แนวการอ่าน ตัวอย่างธีม | 
| **เรียกดู** | ผู้แต่ง, cipai, ราชวงศ์, ประเภท, คอลเลกชันธีม, แคตตาล็อกฉบับเต็ม | 
| **รายการโปรด** | ผลงานที่ติดดาวกับรายการ / ตาราง / เค้าโครงการ์ดและการจัดกลุ่ม | 
| **การตั้งค่า** | ลักษณะที่ปรากฏ, การอ่าน, ข้อมูล, แท็บ, วิดเจ็ต, ทางลัด, วิธีใช้ | 
| **ค้นหา** | ค้นหาข้อมูลเมตาทันที + การค้นหาเชิงลึกแบบข้อความเต็มแบบ Lazy (แท็บเฉพาะบน **iOS 26+**) |

> **เคล็ดลับ:** ซ่อนแท็บ **เรียกดู** หรือ **รายการโปรด** ใน **การตั้งค่า → แถบแท็บ** หากคุณปิดแท็บที่คุณเปิดอยู่ แอปจะกลับสู่หน้าแรกโดยอัตโนมัติ การเปิดเผยแท็บจะซิงค์ผ่าน iCloud เสริม 

### แพลตฟอร์ม 

| แพลตฟอร์ม | ขั้นต่ำ | 
|----------|---------| 
| ไอโฟน/ไอแพด | iOS 17.0+ | 
| แม็ค | macOS 13.0+ | 

เฉพาะ **แท็บค้นหา** ต้องใช้ **iOS 26+** ใน iOS เวอร์ชันก่อนหน้า การค้นหาสามารถทำได้จากหน้าเลือกหาหรือผ่าน Spotlight / Siri 

### ความเป็นส่วนตัวเมื่อติดตั้ง 

- ** ไม่ต้องสมัคร · ไม่มีโฆษณา · ไม่มี SDK การวิเคราะห์ ** 
- Corpus จัดส่งภายใน App Bundle — ไม่มี CDN ไม่มีการวัดและส่งข้อมูลทางไกล 
- iCloud เสริมจะใช้ **iCloud ส่วนตัวของคุณ** เท่านั้น ข้อความ ci ไม่เคยถูกอัปโหลด 

--- 

## ตอนที่ 2 — บ้าน 

แท็บ **หน้าแรก** เป็นจุดเริ่มต้นรายวันของคุณ — การค้นพบที่คัดสรรมาโดยไม่ต้องค้นหาผลงานถึง 21,592 ชิ้น 

### Ci วันนี้ (每日一词) 

**การเลือกรายวันตามที่กำหนด** — ci เดียวกันสำหรับทุกคนในวันที่ปฏิทินเดียวกัน เลือกจากไลบรารีทั้งหมดโดยใช้อัลกอริธึมตามวันที่ แตะการ์ดเพื่อเปิดหน้ารายละเอียดทั้งหมด 

- รีเฟรชอัตโนมัติเวลา **เที่ยงคืนท้องถิ่น** 
- เขียนไปยังพื้นที่เก็บข้อมูล **กลุ่มแอป** เมื่อแอปเปิดตัว ดังนั้นวิดเจ็ต **Daily Ci** จึงซิงค์กัน 
- ลิงก์ในรายละเอียด: `isongci://daily` 
- Siri: *"ci วันนี้ใน iSongCi"*

### Serendipity (邂逅一词) 

แตะ **Serendipity** เพื่อ **สุ่มคัดสรร** — เหมาะมากเมื่อคุณต้องการเซอร์ไพรส์มากกว่าตัวเลือกคงที่ของวันนี้ การแตะแต่ละครั้งจะดึงชิ้นส่วนใหม่จากห้องสมุดออฟไลน์ 

- ลิงก์ในรายละเอียด: `isongci://random` 
- Siri: *"ความบังเอิญใน iSongCi"* 

### อ่านต่อครับ 

หากคุณเพิ่งเปิดผลงาน **อ่านต่อ** จะปรากฏบนหน้าแรกพร้อมชื่อเรื่องและผู้แต่ง แตะครั้งเดียวจะดำเนินการต่อจากจุดที่คุณค้างไว้ 

- ลิงก์ในรายละเอียด: `isongci://continue-reading` 
- มีให้ใช้งานในรูปแบบการดำเนินการด่วนบนหน้าจอหลักด้วย 

### การอ่านแนว 

หน้าแรกแสดง **แนวการอ่าน** ของคุณ — วันติดต่อกันที่คุณอ่านอย่างน้อย 1 CI บวกด้วยจำนวนการอ่านสะสม การเปิดรายละเอียดงานใดๆ จะนับรวมต่อกระแสของวันนี้ 

- ซิงค์ผ่านอุปกรณ์เสริม **iCloud KVS** 
- วิดเจ็ต **ริ้ว** แสดงริ้วบนหน้าจอหลักและหน้าจอล็อค 

### ตัวอย่างธีม 

เลื่อนลงเพื่อดูการ์ดรายการด่วน — **แนะนำ cipai**, **คอลเลกชันธีม**, **豪放 / 婉约** ประเภท และไฮไลท์ **dynasty** แตะ **ดูทั้งหมด** เพื่อข้ามไปยังเรียกดูที่ส่วนนั้น 

### การดำเนินการด่วนบนหน้าจอหลัก

กดไอคอนแอปค้างไว้เพื่อดูทางลัด เช่น **Today's Ci**, **Serendipity**, **Continue Reading**, **Favorites** และ **Search** ปรับแต่งรายการได้สูงสุด **4** ใน **การตั้งค่า → ทางลัด → การดำเนินการด่วนบนหน้าจอหลัก** (มี 15 การดำเนินการ — ดูส่วนที่ 10) 

--- 

## ตอนที่ 3 — เรียกดู 

เปิดแท็บ **เรียกดู** หลายส่วนช่วยให้คุณสำรวจห้องสมุดจากมุมที่ต่างกัน: 

### 1. ผู้แต่ง (名家) 

**กวีซ่งซี 1,509 คน** พร้อมชีวประวัติ แตะผู้เขียนเพื่อดูโปรไฟล์และรายการงานทั้งหมด 

- สลับเค้าโครงผ่าน **⋯**: **รายการ**, **ตาราง** หรือ **การ์ด** 
- จำนวนคอลัมน์กริด (2–4) จดจำแยกกันบน iPhone และ iPad 
- ลิงก์ในรายละเอียด: `isongci://author?id=12` 

### 2. ชิไป (词牌) 

**1,461 cipai** ปรับแต่งรูปแบบในดัชนีเต็ม **บทความเด่น 60 บทความ** ประกอบด้วยบทความเบื้องต้นที่อธิบายรูปแบบ จังหวะ และอารมณ์ที่เป็นตัวแทน เรียนรู้รูปแบบ จากนั้นอ่านผลงานที่เขียนในทำนองนั้น 

ตัวอย่าง: 水调歌头, 念奴娇, 满江红, 蝶恋花, 浣溪沙 

### 3. ราชวงศ์ (朝代) 

เรียกดูตามช่วงเวลาทางประวัติศาสตร์: 

| ราชวงศ์ | ความคุ้มครอง | 
|---------|----------| 
| **五代** | ประเพณี *ci* ยุคแรกก่อนเพลง | 
| **北宋** | ปรมาจารย์เพลงเหนือ | 
| **南宋** | ผู้แต่งเพลงใต้ | 

### 4. ประเภท (流派)

| ประเภท | นับ | ตัวละคร | 
|-------|-------|-----------| 
| **豪放** | 363 | โทนที่กล้าหาญ กว้างขวาง และกล้าหาญ | 
| **婉约** | 520 | น้ำเสียงที่ละเอียดอ่อน โคลงสั้น ๆ และใกล้ชิด | 

ผลงานอาจปรากฏในกลุ่มเดียวหรือทั้งสองกลุ่มตามความเหมาะสม 

### 5. คอลเลกชันธีม (主题) 

**คอลเลกชั่นธีมที่คัดสรรมาแล้ว 10 คอลเลกชั่น** — ความรัก การพรากจากกัน ความคิดถึง ธรรมชาติ ความรักชาติ ปรัชญา เทศกาล และอื่นๆ แต่ละคอลเลกชันจะจัดกลุ่มที่มีแนวคิดร่วมกัน 

### 6. แคตตาล็อกฉบับเต็ม (全集) 

ดัชนี **21,592 งาน** ที่สมบูรณ์ ใช้เมื่อคุณต้องการทุกอย่างในรายการแบบเลื่อนได้รายการเดียวพร้อมตัวเลือกการเรียงลำดับและตัวกรอง 

### ตัวเลือกเค้าโครงและส่วนต่างๆ 

แตะ **⋯** บนหน้าเรียกดูหรือผู้แต่ง: 

| ตัวเลือก | มันทำอะไร | 
|--------|----------------| 
| **เค้าโครง** | รายการ / ตาราง / การ์ด | 
| **การเปิดเผยส่วน** | แสดงหรือซ่อนส่วนการเรียกดู | 
| **ลำดับส่วน** | จัดลำดับวิธีการแสดงส่วนต่างๆ ใหม่ | 
| **คอลัมน์ตาราง** | 2–4 บน iPhone, 2–4 บน iPad (จำแยกกัน) | 

### รายการค้นหา (ก่อน iOS 26) 

บน iOS 17–25 ให้เปิดการค้นหาจาก **ช่องค้นหา** ที่ด้านบนของเรียกดูหรือผ่าน Spotlight / Siri บน **iOS 26+** ให้ใช้แท็บ **ค้นหา** โดยเฉพาะ (ตอนที่ 7) 

--- 

## ตอนที่ 4 — การอ่านรายละเอียด 

แตะจุดใดก็ได้เพื่อเปิด **รายละเอียดงาน** — ประสบการณ์การอ่านหลัก

### แถบเครื่องมือ (ขวาบน) 

| ปุ่ม | การกระทำ | 
|--------|--------| 
| **♥** | เพิ่มหรือลบออกจากรายการโปรด (ใช้สีเฉพาะจุดของคุณเมื่อติดดาว) | 
| **วิทยากร** | เริ่ม **TTS อ่านออกเสียง**; แตะอีกครั้งเพื่อหยุดชั่วคราว / เล่นต่อ | 
| **... เพิ่มเติม** | เปิดเมนูการทำงาน (ดูด้านล่าง) | 

### ส่วนเนื้อหา 

ไม่ใช่ทุกงานจะมีทุกชั้น ส่วนต่างๆ จะปรากฏเมื่อมีเนื้อหาอยู่เท่านั้น: 

| มาตรา | ความคุ้มครอง | สิ่งที่คุณเห็น | 
|---------|----------|--------------| 
| **ข้อความต้นฉบับ** | ทั้งหมด 21,592 | ci แบบเต็มพร้อมพินอินเสริม | 
| **โน้ตคลาสสิก** | ถ้ามี | คำอธิบายประกอบทางวิชาการแบบดั้งเดิม | 
| **แปลธรรมดา** | **11,029 ผลงาน** | การเรนเดอร์ภาษาท้องถิ่นสมัยใหม่ | 
| **ความเห็นสมัยใหม่** | เซ็ตย่อยที่ดูแลจัดการ | ความชื่นชมและบริบทวรรณกรรม | 
| **แนะนำ Cipai** | cipai ที่โดดเด่นและเชื่อมโยง | ปรับแต่งคำอธิบายรูปแบบ | 
| **ประวัติผู้เขียน** | ผู้เขียน 1,509 คน | ชีวประวัติกวี | 
| **ผลงานที่เกี่ยวข้อง** | ลิงค์อัจฉริยะ | ผู้แต่ง คนเดียวกัน cipai หรือธีม | 

สลับเปิดหรือปิดแต่ละส่วนขณะอ่าน **บันทึกส่วนตัว** จะปรากฏที่ด้านล่าง — คำอธิบายประกอบส่วนตัวของคุณ ซึ่งมองเห็นได้เฉพาะคุณเท่านั้น (ซิงค์ผ่าน iCloud เมื่อเปิดใช้งาน) 

### เมนูเพิ่มเติม (⋯)

| รายการ | มันทำอะไร | 
|-----------------------| 
| **ขนาดตัวอักษร** | เปิดแผงมาตราส่วน (50%–300% ฐานเริ่มต้น 22 pt) | 
| **การอ่านอย่างดื่มด่ำ** | มุมมองแบบเต็มจอ ไร้สิ่งกวนใจ (ตอนที่ 5) | 
| **พินอิน** | การแทนที่การตั้งค่าพินอินส่วนกลางต่องาน | 
| **เค้าโครงแนวตั้ง** | การแทนที่ทิศทางการอ่านต่องาน | 
| **คัดลอกข้อความฉบับเต็ม** | คัดลอก ci ทั้งหมดไปยังคลิปบอร์ด | 
| **แชร์ข้อความ** | แผ่นแบ่งปันระบบพร้อมข้อความธรรมดา | 
| **สร้างบัตรแชร์** | เปิดตัวแก้ไขการ์ดรูปภาพ 13 สไตล์ (ตอนที่ 11) | 
| **หมายเหตุส่วนตัว** | เพิ่มหรือแก้ไขบันทึกส่วนตัวของคุณสำหรับงานนี้ | 

### ตัวเลือกการอ่าน 

- **พินอิน** — ค่าเริ่มต้นส่วนกลางในการตั้งค่า แทนที่แต่ละงานโดยละเอียด 
- **รูปแบบแนวตั้ง** — การอ่านจากบนลงล่างแบบคลาสสิก แทนที่ต่องาน 
- **ข้อความต้นฉบับตรงกลาง** — เปิดตามค่าเริ่มต้น จัดแนวบล็อกข้อความหลัก 
- **การแปลโดยระบบ** (iOS 17.4+) — แผงการแปลของ Apple สำหรับข้อความที่เลือก 
- **การสลับส่วน** — แสดง/ซ่อนคำแปล หมายเหตุ ความเห็น คำนำ Cipai ประวัติผู้แต่ง 

### TTS อ่านออกเสียง 

แตะไอคอน **ลำโพง** สำหรับการอ่านออกเสียงข้อความบนอุปกรณ์ ใช้เสียงของระบบ — ไม่มีเครือข่าย เหมาะสำหรับการฟังขณะเดินทางหรือเรียนการออกเสียงด้วยพินอินที่มองเห็นได้

### กดค้างที่แถวรายการ 

ในรายการงานใดๆ **กดค้างไว้** แถวเพื่อดำเนินการด่วน: **รายการโปรด**, **อ่านออกเสียง**, **แชร์** หรือ **ลบออกจากประวัติ** (ในมุมมองประวัติ) 

### ลิงค์ลึก 

เปิดงานเฉพาะตามรหัสแค็ตตาล็อก: `isongci://poem?id=42` 

--- 

## ตอนที่ 5 — การอ่านที่ดื่มด่ำ 

จากรายละเอียด **เพิ่มเติม → การอ่านแบบดื่มด่ำ** เข้าสู่หน้าเต็มหน้าจอที่สะอาดหมดจดซึ่งออกแบบมาเพื่อการท่องจำ การนำเสนอ และการศึกษาแบบเน้นเนื้อหา 

### เค้าโครง 

- **แนวตั้ง** — การไหลจากบนลงล่างสไตล์การเลื่อนแบบคลาสสิก (ค่าเริ่มต้นสำหรับการดื่มด่ำ) 
- **แนวนอน** — การไหลจากซ้ายไปขวาที่ทันสมัย 
- สลับได้ตลอดเวลาในโหมดดื่มด่ำ การตั้งค่าสามารถติดตามการตั้งค่าส่วนกลางได้ 

### การพิมพ์และบรรยากาศ 

- **แบบอักษรที่ได้รับแรงบันดาลใจจากการประดิษฐ์ตัวอักษร** สำหรับข้อความหลัก — ชวนให้นึกถึง Song Ci ที่เขียนด้วยพู่กัน 
- **พื้นหลังกระดาษ Xuan (宣纸)** — ให้ความรู้สึกอบอุ่นและมีพื้นผิวทางวรรณกรรม 
- ปรับให้เข้ากับธีม **สว่าง / มืด / ระบบ** และ **สีเฉพาะจุด** 

### การควบคุม 

- บีบนิ้วหรือใช้ตัวควบคุม **ขนาดตัวอักษร** (50%–300%) 
- แตะเพื่อแสดง/ซ่อน Chrome (แถบเครื่องมือ สลับส่วน) 
- **TTS** ใช้งานได้โดยไม่ต้องออกจากโหมดดื่มด่ำ 
- ปัดหรือใช้ลูกศรเพื่อเลื่อนไปยังงาน **ก่อนหน้า / ถัดไป** ในบริบทรายการปัจจุบัน 

### ดีที่สุดสำหรับ

- การนำเสนอด้วย iPad หรือการอ่านหนังสือบนโต๊ะ 
- การฝึกท่องจำและท่องจำ 
- ภาพหน้าจอและการเตรียมการ์ดแชร์ 

--- 

## ตอนที่ 6 — รายการโปรด 

###ผลงานนำแสดง 

แตะ **♥** บนรายละเอียดงานใดๆ หรือกดแถวรายการค้างไว้ → **รายการโปรด** แถวรายการโปรดใช้ **สีเฉพาะจุด** ของคุณในการติดดาว 

### รูปแบบแท็บรายการโปรด 

เปิดแท็บ **รายการโปรด** แตะ **⋯** เพื่อเปลี่ยน: 

| เค้าโครง | ดีที่สุดสำหรับ | 
|--------|----------| 
| **รายการ** | การสแกนหนาแน่นด้วยชื่อเรื่อง ผู้แต่ง cipai | 
| **กริด** | การเรียกดูภาพด้วยคอลัมน์ที่ปรับได้ | 
| **การ์ด** | การ์ดแสดงตัวอย่างขนาดใหญ่พร้อมข้อความที่ตัดตอนมา | 

### การจัดกลุ่ม 

จัดระเบียบคอลเลกชันของคุณโดย: 

| จัดกลุ่มตาม | พฤติกรรม | 
|----------|----------| 
| **ผู้เขียน** | คลัสเตอร์ทำงานภายใต้กวีแต่ละคน | 
| **ราชวงศ์** | 五代 / 北宋 / 南宋 ส่วน | 
| **ชิไป** | จัดกลุ่มตามรูปแบบการปรับแต่ง | 

### การแก้ไขเป็นกลุ่ม 

แตะ **แก้ไข** บนหน้ารายการโปรด: 

- **เลือกได้หลายรายการ** ใช้งานได้โดยมีเครื่องหมายถูก 
- **เลือกทั้งหมด / ยกเลิกการเลือกทั้งหมด** 
- **ลบแบทช์** ออกจากรายการโปรด (พร้อมการยืนยัน) 

ปัดไปทางซ้ายบนแถวเพื่อดำเนินการ **ลบ** อย่างรวดเร็ว 

### วิดเจ็ต Ci ที่ชื่นชอบ 

วิดเจ็ตบนหน้าจอหลัก **Favorite Ci** หมุนเวียนไปตามผลงานที่ติดดาวของคุณ ซึ่งเป็นตัวเลือกรายวันส่วนตัวจากคอลเลกชันของคุณเอง 

### ส่งออก

**การตั้งค่า → ข้อมูล → ส่งออกรายการโปรด** — แชร์คอลเลกชันของคุณเป็นไฟล์สำหรับการสำรองข้อมูลหรือการย้ายข้อมูล 

--- 

## ตอนที่ 7 — ค้นหา 

บน iOS ให้เปิด **การค้นหาเนื้อเพลงด้วยลายมือ** จากส่วนควบคุมข้างการค้นหาหน้าแรก เมื่อคุณต้องการวาดอักขระมากกว่าการพิมพ์พินอิน 

iSongCi เสนอ **การค้นหาออฟไลน์สองชั้น** — เมตาดาต้ารวดเร็วก่อน ข้อความแบบเต็มลึกเมื่อจำเป็น 

### ระดับ 1 — ค้นหาข้อมูลเมตาทันที 

ขณะที่คุณพิมพ์ แอปจะจับคู่กับข้อมูลเมตาที่รวมไว้ทันที: 

- **ชื่อเรื่อง** (ชื่อ) 
- **ชื่อผู้แต่ง** 
- **ชื่อชิไป** 
- **แท็กและหมวดหมู่** 

ไม่มีตัวหมุนโหลด — ผลลัพธ์จะปรากฏทุกครั้งที่กดแป้นพิมพ์ 

### ระดับ 2 — การค้นหาข้อความแบบเต็มแบบ Lazy 

สำหรับการจับคู่ระดับบรรทัดภายในเนื้อหา ci แอปจะโหลด **`fulltext.json`** จากบันเดิลเมื่อใช้การค้นหาเชิงลึกครั้งแรก หลังจากโหลดครั้งเดียว การค้นหาข้อความแบบเต็มจะทำงานบนอุปกรณ์ทั้งหมด 

- จับคู่ **บรรทัดใดก็ได้** ในคลังข้อมูล 21,592 งาน 
- ช้าลงเล็กน้อยในการเปิดตัวการค้นหาเชิงลึกครั้งแรก แคชไว้หลังจากนั้น 
- **ไม่มีเครือข่าย** — ไฟล์มาพร้อมกับแอป 

### แท็บค้นหาเฉพาะ (iOS 26+) 

บน **iOS 26 และใหม่กว่า** การค้นหาจะมีแท็บของตัวเองในแถบแท็บ ในเวอร์ชันก่อนหน้า ให้ใช้ช่องค้นหาใน **เรียกดู** หรือการรวมระบบด้านล่าง 

### สปอตไลท์

แอปจะจัดทำดัชนีได้สูงสุด **~1,000 ผลงาน** สำหรับการค้นหาใน Spotlight ของระบบ แตะผลลัพธ์ใน Spotlight เพื่อเปิดผลงานนั้นโดยตรงใน iSongCi

### Siri & ลิงก์ลึก

- Siri: *"ค้นหาใน iSongCi"* (พร้อมคำสำคัญ)
- ลิงก์ลึก: `isongci://search?q=明月`

### เคล็ดลับการค้นหา

| เคล็ดลับ | เหตุผล |
|-----------|--------|
| ค้นหาผู้แต่ง + คำสำคัญ | ช่วยจำกัดชุดผลลัพธ์ขนาดใหญ่ |
| ลองใช้ชื่อฉีไพ | ค้นหาผลงานทั้งหมดในแพทเทิร์นทำนองเดียวกัน |
| ใช้บทที่มีชื่อเสียง | เรียกใช้งานโหมดข้อความเต็มสำหรับจับคู่บรรทัด |
| ค้นหาเป็นภาษาจีนตัวเต็ม | UI แปลง; คลังข้อมูลจับคู่กับแหล่งภาษาจีนตัวย่อ |

---

## ส่วนที่ 8 — ธีม & การแสดงผล

เปิด **การตั้งค่า → การแสดงผล**

### โหมดธีม

| โหมด | พฤติกรรม |
|------|----------|
| **สว่าง** | พื้นหลังอ่านเหมือนกระดาษสว่าง |
| **มืด** | อ่านยามค่ำแบบหมึกเข้ม |
| **ระบบ** | ปรับตามการแสดงผลของ iOS / macOS |

### สีเน้น — 15 แบบตั้งต้น + กำหนดเอง

เลือกจาก **ธีมตั้งต้น 15 แบบ** ได้แรงบันดาลใจจากความงามสมัยราชวงศ์ซ่ง:

| # | ตั้งค่าล่วงหน้า | อารมณ์ | 
|---|--------|------| 
| 1 | 水墨 Ink | สีเทาวรรณกรรมกลาง | 
| 2 | 胭脂 Rouge | สำเนียงสีแดงเข้มอบอุ่น | 
| 3 | 朱砂 Cinnabar | คลาสสิคซีล-แดง | 
| 4 | 青瓷 ศิลาดล | เคลือบเขียวเย็น | 
| 5 | 松绿 ต้นสน | ป่าลึกสีเขียว | 
| 6 | 黛蓝 สีคราม | นักวิชาการสีน้ำเงิน-ดำ | 
| 7 | 群青 Azure | สีฟ้าแร่สดใส | 
| 8 | 青莲 โลตัส | ดอกสีม่วงฟ้า | 
| 9 | 琥珀 อำพัน | โทนสีอบอุ่นสีทอง | 
| 10 | 赭金 Ocher | สีน้ำตาลทองเอิร์ธโทน | 
| 11 | 月白 ดวงจันทร์ | สีขาวเงินซีด | 
| 12 | 竹青 ไม้ไผ่ | ไผ่เขียวสด | 
| 13 | 藕荷 รากบัว | สีชมพูอ่อน-ลาเวนเดอร์ | 
| 14 | 玄色 ไม้มะเกลือ | เน้นสีดำเข้ม | 
| 15 | 缃色 ผ้าไหม | ต้นฉบับอายุ สีเหลือง | 

แตะตัวอย่างใดก็ได้ — แหวนที่เลือก + เครื่องหมายถูก หรือเลือก **กำหนดเอง** เพื่อเลือกสีใดก็ได้จากเครื่องมือเลือกสีของระบบ 

สีเฉพาะจุดใช้กับ: ดาวโปรด ปุ่ม ไฮไลต์ ส่วนเน้นการ์ดแชร์ และสีวิดเจ็ต (เมื่อ **ติดตามธีมแอป** เปิดอยู่) 

### ภาษา 

**ภาษาอังกฤษ / 简体中文 / 繁體中文** — UI สลับทันที ข้อความ Corpus ถูกจัดเก็บเป็นภาษาจีนตัวย่อ จอแสดงผลแบบดั้งเดิมใช้การแปลงบนอุปกรณ์ 

### การซิงค์ iCloud 

**รูปลักษณ์** (สว่าง/มืด/ระบบ) **ตั้งค่าสำเนียงล่วงหน้า** และ **ขนาดแบบอักษร** ซิงค์ผ่านตัวเลือก iCloud KVS 

--- 

## ตอนที่ 9 — วิดเจ็ต

### เพิ่มวิดเจ็ตหน้าจอหลัก 

1. กดหน้าจอหลักค้างไว้ → **แก้ไขหน้าจอหลัก** → แตะ **+** 
2. ค้นหา **iSongCi** / **爱宋词** 
3. เลือกประเภทและขนาดวิดเจ็ต → **เพิ่มวิดเจ็ต** 

### ประเภทวิดเจ็ต 

| วิดเจ็ต | ขนาด | พฤติกรรม | 
|--------|-------|----------| 
| **รายวัน** | เล็ก / กลาง / ใหญ่ + ล็อคหน้าจอ | ci ที่กำหนดขึ้นของวันนี้; แตะเปิดรายละเอียด | 
| **สุ่ม Ci** | เล็ก / กลาง / ใหญ่ + ล็อคหน้าจอ | เลือก Serendipity; รีเฟรชบนไทม์ไลน์ | 
| **Ci ที่ชื่นชอบ** | เล็ก / กลาง | หมุนเวียนไปตามรายการโปรดของคุณ | 
| **สตรีค** | เล็ก / วงกลม (ล็อคหน้าจอ) | การอ่านจำนวนแนวและไอคอนเปลวไฟ | 

### วิดเจ็ตล็อคหน้าจอ 

เมื่อเพิ่มวิดเจ็ต ให้สลับไปที่หน้าการปรับแต่ง **หน้าจอล็อค** และเลือกอุปกรณ์เสริม iSongCi เป็นรูปสี่เหลี่ยมผืนผ้า วงกลม หรือแบบอินไลน์ 

### ธีมวิดเจ็ต 

**การตั้งค่า → วิดเจ็ต → ติดตามธีมของแอป** — วิดเจ็ตตรงกับตัวเลือกสีอ่อน/เข้ม/สำเนียงของคุณ 

### ศูนย์ควบคุม (iOS 18+) 

เพิ่มการควบคุมสำหรับ **Ci วันนี้**, **Serendipity** และ **ค้นหา** จาก **การตั้งค่า → ศูนย์ควบคุม** บน iOS 18 และใหม่กว่า 

### วิดเจ็ตการแก้ไขปัญหา

- เปิดแอปหนึ่งครั้งหลังติดตั้ง เพื่อให้แคช CI รายวันถูกเขียนลงใน App Group
- หากข้อความดูผิดปกติหลังจากเปลี่ยนภาษา ให้เปิดแอปสั้น ๆ — แอปจะรีเฟรชแคชวิดเจ็ตโดยอัตโนมัติ
- อัปเดตวิดเจ็ต Ci รายวันในเวลาเที่ยงคืนท้องถิ่น
- ไทม์ไลน์วิดเจ็ต Random Ci รีเฟรชเป็นระยะเพื่อความหลากหลาย

### คู่มือวิดเจ็ตในแอป

**การตั้งค่า→วิดเจ็ต→คู่มือวิดเจ็ต** หรือ `isongci://widget-guide` สําหรับภาพหน้าจอและคําแนะนําต่อวิดเจ็ตแต่ละชิ้น 

--- 

## ตอนที่ 10 — Siri, ทางลัด & การกระทําบนหน้าจอหลัก

### ความตั้งใจของ Siri (3)

|เจตนา |ตัวอย่างวลี |
|--------|----------------|
|** Ci** วันนี้ |"cis วันนี้ใน iSongCi" |
|**ความบังเอิญ** |"ความบังเอิญใน iSongCi" |
|**ค้นหา Ci** |"ค้นหาใน iSongCi" (พร้อมคําสําคัญ) |

เพิ่มสิ่งเหล่านี้ในแอป **Shortcuts** สําหรับระบบอัตโนมัติ — เช่น เปิด`isongci://daily`ทุกเช้า 

### การกระทําด่วนบนหน้าจอหลัก (มีให้เลือก 15 รายการ, เปิดใช้งานสูงสุด 4 รายการ)

กดปุ่มค้างที่ไอคอนแอปปรับแต่งใน **การตั้งค่า→ทางลัด→การดําเนินการด่วนบนหน้าจอหลัก**:

| # | การกระทำ | เปิด | 
|---|--------|-------| 
| 1 | ซีวันนี้ | `isongci://daily` | 
| 2 | เซเรนดิพิตี้ | `isongci://random` | 
| 3 | อ่านต่อ | `isongci://continue-reading` | 
| 4 | รายการโปรด | `isongci://favorites` | 
| 5 | ค้นหา | `isongci://search` | 
| 6 | เรียกดู | `isongci://category` | 
| 7 | หน้าแรก | `isongci://home` | 
| 8 | การตั้งค่า | `isongci://settings` | 
| 9 | คู่มือการใช้งาน | `isongci://usage-guide` | 
| 10 | คู่มือวิดเจ็ต | `isongci://widget-guide` | 
| 11 | คู่มือทางลัด | `isongci://shortcuts-guide` | 
| 12 | คู่มือคุณสมบัติ | `isongci://feature-guide` | 
| 13 | คำติชม | `isongci://feedback` | 
| 14 | รีวิวในแอป | `isongci://in-app-review` | 
| 15 | การตั้งค่าทางลัดหน้าแรก | `isongci://home-shortcuts` | 

มีเพียง **4** เท่านั้นที่ปรากฏบนเมนูไอคอนพร้อมกัน เลือกสี่รายการที่คุณใช้บ่อยที่สุด 

### ลิงก์ในรายละเอียด (`isongci://`) 

ข้อมูลอ้างอิงฉบับเต็ม: [ลิงก์ทางลัด](../url-scheme) URL ทั่วไป: 

| URL | เปิด | 
|-----|-------| 
| `isongci://poem?id=42` | รายละเอียด Ci ตามแค็ตตาล็อก ID | 
| `isongci://author?id=12` | โปรไฟล์ผู้เขียน | 
| `isongci://daily` | ซีวันนี้ | 
| `isongci://random` | เซเรนดิพิตี้ | 
| `isongci://continue-reading` | อ่านต่อ | 
| `isongci://search?q=明月` | ค้นหา 明月 | 
| `isongci://favorites` | แท็บรายการโปรด | 

ใช้ในโปรไฟล์การกำหนดค่าคำสั่งลัด, Notes, Safari หรือ MDM 

### คำแนะนำทางลัดในแอป

**การตั้งค่า → ทางลัด → คำแนะนำทางลัด** หรือ `isongci://shortcuts-guide` — ปุ่มคัดลอกด้วยการแตะเพียงครั้งเดียวสำหรับทุก URL 

--- 

## ตอนที่ 11 — แชร์การ์ด (13 สไตล์) 

จากรายละเอียด **เพิ่มเติม → สร้างการ์ดแชร์**: 

| สไตล์ | อารมณ์ | 
|-------|-| 
| คลาสสิค | รูปแบบวรรณกรรมที่สะอาดตา | 
| หมึก | ความงามแบบแปรงแล้วล้าง | 
| น้อยที่สุด | เน้นการพิมพ์ | 
| แนวตั้ง | คลาสสิกจากบนลงล่าง | 
| ชาด | ประทับตราสำเนียงสีแดง | 
| มืด | พื้นหลังหมึกกลางคืน | 
| ศิลาดล | เซรามิค โทนเย็น สีเขียว | 
| สีออเกอร์-ทอง | โทนสีทองอบอุ่น | 
| สโนว์ไวท์ | กระดาษขาวสว่าง | 
| เลื่อน | แม่ลายเลื่อนแนวนอน | 
| มูนไวท์ | พาเลทท์แสงจันทร์นวล | 
| เงาไม้ไผ่ | เนื้อไผ่เขียว | 
| กระดาษซวน | พื้นผิว 宣纸 พื้นหลัง | 

### ตัวเลือกการส่งออก 

- **ข้อความเต็ม** กับ **ข้อความที่ตัดตอนมา** — จำไว้ใช้ครั้งต่อไป 
- **ความละเอียด 3×** PNG — คมชัดบนจอภาพ Retina และโซเชียลมีเดีย 
- **ส่งออก PNG** — บันทึกลงในรูปภาพหรือแชร์ผ่านแอปใดก็ได้ 
- การตั้งค่าสไตล์จะถูกบันทึกโดยอัตโนมัติ 

ต้องได้รับอนุญาต **คลังรูปภาพ (เพิ่ม)** เมื่อบันทึกลงในรูปภาพเท่านั้น — เขียนอย่างเดียว ไม่มีสิทธิ์ในการอ่าน 

--- 

## ตอนที่ 12 — การซิงค์ iCloud 

ตัวเลือกการซิงค์ผ่าน **iCloud Key-Value Store** — ไม่มีเซิร์ฟเวอร์ iHTC Studio

| ซิงค์แล้ว | ไม่ซิงค์ | 
|--------|------------| 
| รายการโปรด | ตัวเลือกการดำเนินการด่วนบนหน้าจอหลัก | 
| บันทึกส่วนตัว | การเริ่มต้นใช้งาน / แฟล็กคำแนะนำการต้อนรับ | 
| ลักษณะที่ปรากฏ (สว่าง/มืด/ระบบ) | สถานะการสุ่มวิดเจ็ต | 
| สีเน้นเสียงและขนาดตัวอักษร | ข้อความ Ci (อยู่ในชุดแอปเสมอ) | 
| เรียกดู / การมองเห็นแท็บรายการโปรด | ค้นหาแคชข้อความแบบเต็ม | 
| การอ่านแนว | เฉดสีตัวเลือกสำเนียงแบบกำหนดเอง (เลือกใหม่บนอุปกรณ์ใหม่) | 

เปิด: **การตั้งค่า → ข้อมูล → ซิงค์ iCloud** จำเป็นต้องลงชื่อเข้าใช้ iCloud บนอุปกรณ์ **ไม่เคยอัปโหลดข้อความ Ci** — เฉพาะข้อมูลส่วนบุคคลและการตั้งค่าของคุณเท่านั้น 

--- 

## ตอนที่ 13 — การแจ้งเตือน 

### การแจ้งเตือน Ci รายวัน 

ตัวเลือก **การแจ้งเตือนในท้องถิ่น** เตือนให้คุณอ่าน Ci ของวันนี้ 

| การตั้งค่า | ที่ตั้ง | 
|---------|----------| 
| เปิด / ปิด | **การตั้งค่า → การแจ้งเตือน** | 
| เวลาเตือนความจำ | เลือกชั่วโมงและนาทีที่คุณต้องการ | 
| การอนุญาต | iOS ถามเมื่อเปิดใช้งานครั้งแรก — ไม่มีเซิร์ฟเวอร์ที่เกี่ยวข้อง | 

การแจ้งเตือน **กำหนดเวลาไว้บนอุปกรณ์ทั้งหมด** ไม่มีพุชเซิร์ฟเวอร์ ไม่มีพิกเซลการติดตาม ไม่มีเพย์โหลดระยะไกล 

### เคล็ดลับ

- หากการเตือนหยุดลงหลังจากอัปเดต iOS ให้เปิดแอปหนึ่งครั้งเพื่อกำหนดเวลาใหม่ 
- การปิดใช้งานการแจ้งเตือนไม่ส่งผลต่อตรรกะการอ่านต่อเนื่อง 
- นับจำนวนสตรีคเมื่อคุณเปิดรายละเอียดงานใดๆ — การแจ้งเตือนเป็นเพียงการให้กำลังใจเท่านั้น 

--- 

## ตอนที่ 14 — การตั้งค่าและคำแนะนำ 

เปิด **การตั้งค่า** ส่วนต่างๆ จากบนลงล่าง: 

### รูปร่างหน้าตา 

- **ธีม** — สว่าง / มืด / ระบบ 
- **สีเน้นเสียง** — 15 ค่าที่ตั้งล่วงหน้า + กำหนดเอง (ตอนที่ 8) 
- **ภาษา** — อังกฤษ / 简体中文 / 繁體中文 

### การอ่าน 

- **แถบเลื่อนขนาดตัวอักษร** — มาตราส่วนต่อเนื่อง 50%–300% (รวมถึงรายละเอียดเมนูเพิ่มเติมด้วย) 
- **การอ่านแนวตั้ง** — สลับทั่วโลก 
- **พินอิน** — เปิดตามค่าเริ่มต้น 
- **ข้อความต้นฉบับตรงกลาง** — เปิดตามค่าเริ่มต้น 
- **แบบอักษรการประดิษฐ์ตัวอักษร** — แบบอักษรที่สมจริงและมีรายละเอียด 

### ข้อมูล 

- **แนวการอ่าน** — ดูสถิติแนวการอ่าน 
- **iCloud Sync** — ตัวเลือกเสริม (ตอนที่ 12) 
- **ส่งออกรายการโปรด** — แชร์คอลเลกชันเป็นไฟล์ 

### แถบแท็บ 

- สลับการมองเห็นแท็บ ** เรียกดู ** (ค่าเริ่มต้นเปิด) 
- สลับการมองเห็นแท็บ **รายการโปรด** (ค่าเริ่มต้นเปิด) 

### วิดเจ็ต 

- **คำแนะนำวิดเจ็ต** — คำแนะนำต่อวิดเจ็ต 
- **ติดตามธีมของแอป** สลับ 

### ทางลัด 

- **การดำเนินการด่วนบนหน้าจอหลัก** — เลือกได้สูงสุด 4 รายการจาก 15 รายการ 
- **คำแนะนำทางลัด** — การอ้างอิงลิงก์ในรายละเอียดพร้อมปุ่มคัดลอก

### การแจ้งเตือน 

- **การแจ้งเตือน Ci รายวัน** — เปิดใช้งาน เวลา สถานะการอนุญาต 

### ช่วยด้วย 

- **คู่มือการใช้งาน** — ทัวร์ชมฟีเจอร์การเล่นซ้ำ 
- **คำแนะนำคุณลักษณะ** — การ์ดคุณลักษณะเชิงลึก (`isongci://feature-guide`) 
- **ส่งคำติชม** — เปิดอีเมล (`isongci://feedback`) 

### เกี่ยวกับ 

- หมายเลขเวอร์ชัน 
- **ขวดทิป** — ตัวเลือกการซื้อในแอป `com.iHTCboy.iSongCi.6` (จัดการโดย Apple StoreKit) 
- ลิงค์ App Store 
- เล่นซ้ำยินดีต้อนรับสู่การเริ่มต้นใช้งาน 

--- 

## ตอนที่ 15 — รับแอป 

| ช่อง | ลิงค์ | 
|---------|-| 
| แอพสโตร์ | [ดาวน์โหลดได้ที่ App Store](https://apps.apple.com/app/id6788433450) | 

### ความต้องการของระบบ 

| แพลตฟอร์ม | ขั้นต่ำ | 
|----------|---------| 
| ไอโฟน/ไอแพด | iOS 17.0+ (แท็บค้นหา: iOS 26.0+) | 
| แม็ค | macOS 13.0+ | 

### ติดต่อ 

- **อีเมล:** [AppleOSer@gmail.com](mailto:AppleOSer@gmail.com) — โดยทั่วไปเราจะตอบกลับภายใน 48 ชั่วโมง 

### โถทิปเสริม 

หากคุณชอบ iSongCi โปรดพิจารณาเคล็ดลับเสริมผ่าน **การตั้งค่า → เกี่ยวกับ** รหัสผลิตภัณฑ์: `com.iHTCboy.iSongCi.6`. การชำระเงินจะดำเนินการโดย Apple ทั้งหมด 

[คำถามที่พบบ่อย](../faq) · [ลิงก์ทางลัด](../url-scheme) · [นโยบายความเป็นส่วนตัว](../privacy)

</section>
<section lang="de" markdown="1">

### Ist die App vollständig offline? 

Ja. Alle **21.592 Song Ci-Werke** sind gebündelt. Nach der Installation sendet die App **keine ausgehenden Netzwerkanfragen** – kein Konto, keine Werbung, keine Analysen. Optional: iCloud nutzt den Dienst von Apple nur, wenn Sie ihn aktivieren. 

### Wie unterscheidet sich das von Tang-Poesie-/allgemeinen Poesie-Apps? 

iSongCi ist **senkrecht zu Song Ci (宋词)** – kein gemischter Tang/Song/Yuan-Gedichtkatalog. Es bietet **1.461 Cipai**-Wissen, **einfache Übersetzung und moderne Kommentare**, **immersives vertikales Lesen** mit Pinyin, täglichem CI, Share-Karten, Widgets, Control Center, Siri und optionaler iCloud. 

### Wie viel Inhalt ist enthalten? 

| Artikel | Zählen | 
|------|-------| 
| Ci arbeitet (gesamt) | 21.592 | 
| Autoren | 1.509 | 
| Cipai (Stimmmuster) | 1.461 | 
| Empfohlenes Cipai mit Intro | 60 | 
| Einfache Übersetzungen | 11.029 | 
| Moderner Kommentar | Alle Werke | 
| Sammlungen | 12 (Haofang 363 · Wanyue 520 · 10 Themensets) | 
| Dynastien | Fünf Dynastien, Nordlied, Südlied | 

### Was sind einfache Übersetzungen, klassische Notizen und moderne Kommentare? 

Drei separate Ebenen auf der Detailseite – jeden Abschnitt können Sie einzeln umschalten:

- **Einfache Übersetzung (白话译文)** – moderne chinesische Wiedergabe des Volltextes (~11.029 Werke) 
- **Klassische Anmerkungen (注释)** – traditionelle wissenschaftliche Anmerkungen, sofern verfügbar 
- **Moderner Kommentar (白话赏析)** – automatisch generierter Hintergrund, Kerninhalte und Lesetipps für jedes Werk (als Referenz, nicht als akademisches Zitat) 

### Gibt es für alle Werke Übersetzungen? 

Nein. **11.029** Werke enthalten eine vollständige einfache Übersetzung; der Rest zeigt Originaltext plus moderne Kommentare. Klassische Notizen werden nur angezeigt, wenn sie in den Quelldaten enthalten sind. Die App ist ein Lese- und Entdeckungsstudio, keine vollständige akademische Ausgabe aller Ci. 

### Wie funktioniert Today's Ci? 

Ein Stück wird **deterministisch aus dem vorgestellten Pool** (Haofang + Wanyue-Meisterwerke) ausgewählt, wobei der **Kalendertag als Startwert** verwendet wird – jeder sieht das **gleiche CI am selben Datum**. Es überschlägt sich um **lokale Mitternacht**. Öffnen von **Zu Hause** oder `isongci://daily`. 

### Was ist Serendipity? 

**邂逅一词** zieht ein **zufälliges** Stück aus dem vorgestellten Pool – bei jedem Tippen ein anderes. Verwenden Sie **Home → Serendipity**, `isongci://random`, das **Random Ci**-Widget oder Siri. 

### Wie genau ist Pinyin?

Pinyin wird pro Segment **automatisch generiert**. Es funktioniert gut für die meisten Zeilen, **kann aber dazu führen, dass polyphone Zeichen falsch interpretiert werden** (多音字). Benutzen Sie es als Lesehilfe, nicht als Autorität für die Aussprache. 

### Traditionelle chinesische Anzeige? 

Die Benutzeroberfläche verfügt über dedizierte **繁體中文**-Strings. Korpustext wird in vereinfachtem Chinesisch gespeichert und **zum Zeitpunkt der Anzeige konvertiert** (S2T-Tabelle auf Zeichenebene) für den traditionellen Modus – Sie benötigen keine zwei Kopien der Datenbank. 

### Wie funktionieren vertikales Lesen und Pinyin? 

Global unter **Einstellungen → Lesen** aktivieren (vertikales Layout, Pinyin, Kalligraphieschrift). In jedem Arbeitsdetail können Sie **Immersive Reading** für eine vertikale (von rechts nach links) oder horizontale Vollbildseite mit Xuan-Papierhintergrund und unabhängiger Schriftskalierung öffnen. 

### Was ist immersives Lesen? 

**Detail → Mehr → Immersive Reading** öffnet eine chromfreie Seite – ideal zum Rezitieren oder Präsentieren auf dem iPad oder einem großen Bildschirm. Wechseln Sie im Lesegerät zwischen Vertikal/Horizontal und Kalligraphie. 

### Wie ändere ich die Schriftgröße? 

Schieberegler **Einstellungen → Lesen** oder **Detail → Mehr → Schriftgröße**. Skaliert den Textkörper unabhängig vom dynamischen Typ des Systems; Synchronisiert über iCloud, wenn aktiviert. 

### Wie funktioniert das Vorlesen (TTS)?

Tippen Sie in der Detailsymbolleiste auf das Symbol **Lautsprecher**. Verwendet die Mandarin-Sprachsynthese auf dem Gerät. Mit derselben Taste pausieren und fortfahren. 

### Wie funktionieren Favoriten, Notizen und iCloud? 

**Favoriten** – tippen Sie bei einem beliebigen Werk auf ♥. **Private Notizen** – Anmerkungen pro Gedicht, die nur Sie sehen können (Detailseite). Die optionale **iCloud-Synchronisierung** spiegelt Favoriten, Notizen, Erscheinungsbild, Schriftskalierung, Tab-Sichtbarkeit und Lesestreifen auf allen Geräten wider. **Ci-Text wird nie hochgeladen** – er bleibt immer im App-Bundle. 

### Was sind die Lesestreak-Regeln? 

Öffnen Sie **ein beliebiges Ci** in der App, um diesen Kalendertag zu zählen. **Aufeinanderfolgende Tage** verlängern deinen Streak; **Überspringen Sie mehr als einen Tag** und der Streak wird beim nächsten Öffnen auf Null zurückgesetzt. **Gesamtanzahl der Lesezugriffe** erfasst die geöffneten lebenslangen Teile. Streak wird auf der Startseite und im **Reading Streak**-Widget angezeigt. 

### Welche Share-Card-Stile gibt es? 

**13 Stile:** Klassisch, Ink Wash, Cinnabar Seal, Silk Scroll, Scroll Long, Ockergold, Winter Snow, Green Landscape, Bamboo Slips, Moonlit Silver, Minimal, Dark Minimal, Vertical Script. Wählen Sie Volltext oder Auszug; optional einen Kommentar hinzufügen; Exportieren Sie PNG mit 3-facher Auflösung. 

### Welche Widgets sind verfügbar?

| Widget | Zweck | 
|--------|---------| 
| Das heutige Ci | Das heute hervorgehobene Stück | 
| Zufall | Zufällig vorgestelltes CI (stündlich aktualisiert) | 
| Lieblings-Ci | Neueste markierte Arbeit | 
| Lesesträhne | Aufeinanderfolgende Tage + Gesamtanzahl der Lesevorgänge | 
| Kontrollzentrum | Öffnen Sie „Today's Ci“ mit nur einem Fingertipp (iOS 18+) | 

Größen: Klein / Mittel / Groß auf dem Startbildschirm; Sperrbildschirm kreisförmig, inline oder rechteckig. Unterstützt **StandBy**. Die Widget-Sprache folgt der **In-App-Sprache**, nicht der Systemsprache. 

### Widget zeigt falschen oder leeren Text an? 

1. Öffnen Sie die App nach der Installation einmal 
2. Ziehen Sie zum Aktualisieren auf die Startseite, um den Widget-Cache neu zu schreiben 
3. Öffnen Sie nach dem Ändern der Sprache kurz die App, um sie zu aktualisieren 
4. **Lieblings-Ci** benötigt mindestens ein mit einem Stern ausgezeichnetes Werk 
5. **Reading Streak** erfordert, dass Sie zuerst ein Werk in der App öffnen 
6. Stellen Sie sicher, dass Widgets für iSongCi in den Systemeinstellungen zulässig sind 

### Was ist das Control Center-Widget (iOS 18+)? 

Fügen Sie **Heutiges Ci** über **Einstellungen → Kontrollzentrum** (oder den System-Kontrollzentrum-Editor) hinzu. Erfordert **iOS 18.0+**. Durch Antippen öffnet sich die App direkt zum heutigen Stück. 

### Welche Siri-Verknüpfungen gibt es? 

Im Lieferumfang der App sind drei App Intents enthalten:

| Absicht | Beispielsatz | 
|--------|----------------| 
| Öffnen Sie das heutige Ci | „Heutiges ci in iSongCi“ | 
| Zufälliges Ci | „Serendipity in iSongCi“ | 
| Suche Ci | „Suche in iSongCi“ (mit Schlüsselwort) | 

Konfigurieren Sie in den Einstellungen bis zu **4 Schnellaktionen für den Startbildschirm**. Vollständige Deep-Link-Liste in [Shortcut-Links](../url-scheme). 

### Was sind Spotlight-Einschränkungen? 

Spotlight indiziert den **vorgestellten Pool sowie Ihre Favoriten** – bis zu **~1.000** Einträge. Seltene Werke werden nicht in der Systemsuche angezeigt; Verwenden Sie stattdessen die **tiefe In-App-Volltextsuche** (lädt den gesamten Korpus verzögert). Tippen Sie auf ein Spotlight-Ergebnis, um dieses CI direkt zu öffnen. 

### Kann ich Tabs ausblenden? 

Ja. **Einstellungen → Tab-Leiste** – schalten Sie die Registerkarten **Kategorien** und/oder **Favoriten** um. Ausgeblendete Registerkarten bleiben über Detailaktionen, Menüs mit langem Drücken, Widgets und `isongci://`-Links erreichbar. 




|---------|---------------|----| 
| Schnellaktionen auf dem Startbildschirm | ✅ | ❌ | 
| Widgets und Kontrollzentrum | ✅ (iOS 18+ CC) | Widgets hauptsächlich auf iPhone/iPad | 
| Haptisches Feedback | ✅ | ❌ | 
| Registerkarte „Spezielle Suche“ | iOS 26+ | Suche über Button / Blatt | 
| Kernlektüre, Favoriten, iCloud | ✅ | ✅ | 

### Ist die App kostenlos? Was ist das Trinkgeldglas?

**Völlig kostenlos** – alle 21.592 Werke und alle Funktionen, kein Abonnement, keine Werbung. Mit einem **optionalen Trinkgeldglas** (`com.iHTCboy.iSongCi.6`) können Sie die Entwicklung über Apple In-App Purchase unterstützen; es schaltet nichts zusätzliches frei. 

### Systemanforderungen 

| Plattform | Minimum | 
|----------|---------| 
| iPhone / iPad | iOS 17.0+ | 
| Mac | macOS 13.0+ | 
| Kontrollzentrum-Widget | iOS 18.0+ | 
| Systemübersetzungspanel | iOS 17.4+ / macOS 14.4+ | 

### Wie bekomme ich die App? 

[Im App Store herunterladen](https://apps.apple.com/app/id6788433450) (App-ID **6788433450**). 

### Wie kontaktiere ich den Support? 

[AppleOSer@gmail.com](mailto:AppleOSer@gmail.com) – wir antworten normalerweise innerhalb von 48 Stunden. 

--- 

### Wie funktioniert kontinuierliches Lesen? 

Aktivieren Sie **kontinuierliches Lesen** unter Einstellungen → Lesen. Nachdem eine Arbeit TTS abgeschlossen hat, erscheint eine untere Leiste; Wenn Sie einige Sekunden lang nichts tun, wird automatisch das nächste Element in der aktuellen Warteschlange (Durchsuchen / Wiedergabeliste / Favoriten / Täglich) gestartet. Sie können bei der Generierung von Aktienkarten auch Zeilen auswählen. 

### Wie funktionieren tägliche Erinnerungen?

Optionale **lokale Benachrichtigungen** erinnern Sie daran, die heutige Ci zu lesen. Tippen Sie auf die Benachrichtigung, um das passende Werk per Deeplink zu öffnen. Durch das Deaktivieren von Benachrichtigungen wird Ihre Lesesträhne nicht gelöscht. 

## Vollständiges Benutzerhandbuch 

Die folgenden Abschnitte enthalten die vollständige Produktanleitung, die zuvor auf der Support-Seite verfügbar war. Kurze Fragen und Antworten bleiben oben (falls vorhanden). 

--- 

## Teil 1 – Erster Start und Schnittstelle 

### Willkommensführer 

Beim ersten Start stellt ein **mehrseitiger Willkommensleitfaden** die App vor – Bibliotheksskala, tägliches CI, immersives Lesen, Favoriten, Widgets und Datenschutz. Wischen Sie durch jede Seite und tippen Sie dann auf **Erste Schritte**. Jederzeit wiedergeben: **Einstellungen → Hilfe → Nutzungsanleitung** oder Deep-Link `isongci://feature-guide`. 

### Übersicht über die Tab-Leiste 

| Tab | Was es tut | 
|-----|----------------| 
| **Zuhause** | Heutiges Ci, Serendipity, Weiterlesen, Lesesträhne, thematische Vorschauen | 
| **Durchsuchen** | Autoren, Titel, Dynastien, Genres, Themensammlungen, Gesamtkatalog | 
| **Favoriten** | Starred funktioniert mit Listen-/Raster-/Kartenlayouts und Gruppierungen | 
| **Einstellungen** | Aussehen, Lesen, Daten, Registerkarten, Widgets, Verknüpfungen, Hilfe | 
| **Suchen** | Sofortige Metadatensuche + verzögerte Volltext-Tiefensuche (eigene Registerkarte unter **iOS 26+**) |

> **Tipp:** Blenden Sie die Registerkarte **Durchsuchen** oder **Favoriten** in **Einstellungen → Registerkartenleiste** aus. Wenn Sie den Tab schließen, auf dem Sie sich befinden, kehrt die App automatisch zur Startseite zurück. Die Tab-Sichtbarkeit wird über optionale iCloud synchronisiert. 

### Plattformen 

| Plattform | Minimum | 
|----------|---------| 
| iPhone / iPad | iOS 17.0+ | 
| Mac | macOS 13.0+ | 

Für die dedizierte **Suchregisterkarte** ist **iOS 26+** erforderlich. In früheren iOS-Versionen ist die Suche über die Seite „Durchsuchen“ oder über Spotlight/Siri verfügbar. 

### Datenschutz bei der Installation 

- **Keine Anmeldung · keine Werbung · kein Analyse-SDK** 
- Corpus wird im App-Bundle geliefert – kein CDN, keine Telemetrie 
- Optionale iCloud verwendet nur **Ihre private iCloud**; CI-Text wird nie hochgeladen 

--- 

## Teil 2 – Zuhause 

Die Registerkarte **Home** ist Ihr täglicher Einstiegspunkt – kuratierte Entdeckung, ohne 21.592 Werke durchsuchen zu müssen. 

### Heutiges Ci (每日一词) 

Eine **deterministische tägliche Auswahl** – das gleiche CI für alle am selben Kalenderdatum, ausgewählt aus der gesamten Bibliothek durch einen datumsbasierten Algorithmus. Tippen Sie auf die Karte, um die vollständige Detailseite zu öffnen. 

- Aktualisiert sich automatisch um **lokale Mitternacht** 
- Wird beim Start der App in den **App Group**-Speicher geschrieben, damit **Daily Ci**-Widgets synchron bleiben 
- Deeplink: `isongci://daily` 
- Siri: *"Heutiges ci in iSongCi"*

### Serendipity (邂逅一词) 

Tippen Sie auf **Serendipity**, um eine **zufällig kuratierte Ci** zu erhalten – ideal, wenn Sie lieber eine Überraschung als die heutige feste Auswahl wünschen. Bei jedem Tippen wird ein neues Stück aus der Offline-Bibliothek gezogen. 

- Deeplink: `isongci://random` 
- Siri: *"Serendipity in iSongCi"* 

### Weiterlesen 

Wenn Sie kürzlich ein Werk geöffnet haben, wird auf der Startseite **Weiterlesen** mit dem Titel und dem Autor angezeigt. Durch einmaliges Tippen wird dort fortgesetzt, wo Sie aufgehört haben. 

- Deeplink: `isongci://continue-reading` 
- Auch als Schnellaktion auf dem Startbildschirm verfügbar 

### Lesesträhne 

Auf der Startseite wird Ihre **Leseserie** angezeigt – an aufeinanderfolgenden Tagen, an denen Sie mindestens ein Ci gelesen haben, plus einer kumulativen Leseanzahl. Das Öffnen eines Arbeitsdetails zählt für den heutigen Streak. 

- Synchronisierung über optionales **iCloud KVS** 
- Das **Streak**-Widget zeigt Streak auf dem Startbildschirm und dem Sperrbildschirm an 

### Themenvorschauen 

Scrollen Sie nach unten, um Schnellzugangskarten zu erhalten – **ausgewählte Cipai**, **Themensammlungen**, **豪放 / 婉约**-Genres und **Dynastie**-Highlights. Tippen Sie auf **Alle anzeigen**, um in diesem Abschnitt zum Durchsuchen zu springen. 

### Schnelle Aktionen auf dem Startbildschirm

Drücken Sie lange auf das App-Symbol, um Verknüpfungen wie **Today's Ci**, **Serendipity**, **Weiterlesen**, **Favoriten** und **Suchen** aufzurufen. Passen Sie bis zu **4** Elemente unter **Einstellungen → Verknüpfungen → Schnellaktionen auf dem Startbildschirm** an (15 Aktionen verfügbar – siehe Teil 10). 

--- 

## Teil 3 – Durchsuchen 

Öffnen Sie die Registerkarte **Durchsuchen**. In mehreren Abschnitten können Sie die Bibliothek aus verschiedenen Blickwinkeln erkunden: 

### 1. Autoren (名家) 

**1.509 Song Ci-Dichter** mit Biografien. Tippen Sie auf einen Autor, um dessen Profil und die vollständige Werkliste anzuzeigen. 

- Wechseln Sie das Layout über **⋯**: **Liste**, **Raster** oder **Karten** 
- Die Anzahl der Rasterspalten (2–4) wird auf iPhone und iPad separat gespeichert 
- Deep-Link: `isongci://author?id=12` 

### 2. Cipai (词牌) 

**1.461 Cipai** Melodiemuster im vollständigen Index. **60 vorgestellte Cipai** enthalten einführende Essays, in denen Form, Rhythmus und repräsentative Stimmung erläutert werden – lernen Sie das Muster und stöbern Sie dann in Werken, die zu dieser Melodie geschrieben wurden. 

Beispiele: 水调歌头, 念奴娇, 满江红, 蝶恋花, 浣溪沙. 

### 3. Dynastien (朝代) 

Nach historischem Zeitraum durchsuchen: 

| Dynastie | Abdeckung | 
|---------|----------| 
| **五代** | Frühe *ci*-Tradition vor dem Lied | 
| **北宋** | Northern Song-Meister | 
| **南宋** | Southern Song-Texter | 

### 4. Genres (流派)

| Genre | Zählen | Charakter | 
|-------|-------|-----------| 
| **豪放** | 363 | Kühner, expansiver, heroischer Ton | 
| **婉约** | 520 | Zarter, lyrischer, intimer Ton | 

Gegebenenfalls können Werke in einer oder beiden Gruppierungen erscheinen. 

### 5. Themensammlungen (主题) 

**10 kuratierte Themensammlungen** – Liebe, Abschied, Nostalgie, Natur, Patriotismus, Philosophie, Feste und mehr. Jede Sammlung umfasst Ci, die ein gemeinsames Motiv haben. 

### 6. Vollständiger Katalog (全集) 

Der vollständige **21.592-Werke**-Index. Verwenden Sie diese Option, wenn Sie alles in einer scrollbaren Liste mit Sortier- und Filteroptionen haben möchten. 

### Layout- und Abschnittsoptionen 

Tippen Sie auf **⋯** auf den Seiten „Durchsuchen“ oder „Autoren“: 

| Option | Was es tut | 
|--------|----------------| 
| **Layout** | Liste / Raster / Karten | 
| **Sichtbarkeit des Abschnitts** | Alle Suchbereiche ein- oder ausblenden | 
| **Abschnittsreihenfolge** | Die Darstellung der Abschnitte neu anordnen | 
| **Rasterspalten** | 2–4 auf dem iPhone, 2–4 auf dem iPad (separat gespeichert) | 

### Sucheintrag (vor iOS 26) 

Öffnen Sie unter iOS 17–25 die Suche über das **Suchfeld** oben in „Durchsuchen“ oder über Spotlight/Siri. Verwenden Sie unter **iOS 26+** die spezielle Registerkarte **Suchen** (Teil 7). 

--- 

## Teil 4 – Detaillesung 

Tippen Sie auf ein beliebiges Ci, um **Work Detail** zu öffnen – das zentrale Leseerlebnis.

### Symbolleiste (oben rechts) 

| Knopf | Aktion | 
|--------|--------| 
| **♥** | Zu Favoriten hinzufügen oder daraus entfernen (beim Markieren wird Ihre Akzentfarbe verwendet) | 
| **Sprecher** | **TTS-Vorlesen** starten; Tippen Sie erneut, um die Wiedergabe anzuhalten/fortzusetzen | 
| **⋯ Mehr** | Öffnet das Aktionsmenü (siehe unten) | 

### Inhaltsabschnitte 

Nicht jedes Werk hat jede Schicht. Abschnitte werden nur angezeigt, wenn Inhalt vorhanden ist: 

| Abschnitt | Abdeckung | Was Sie sehen | 
|---------|----------|--------------| 
| **Originaltext** | Alle 21.592 | Vollständiges CI mit optionalem Pinyin | 
| **Klassische Noten** | Wo verfügbar | Traditionelle wissenschaftliche Anmerkungen | 
| **Einfache Übersetzung** | **11.029 Werke** | Moderne volkssprachliche Wiedergabe | 
| **Moderner Kommentar** | Kuratierte Teilmenge | Wertschätzung und literarischer Kontext | 
| **Cipai-Einführung** | Empfohlene und verlinkte Cipai | Erklärung des Abstimmungsmusters | 
| **Biografie des Autors** | 1.509 Autoren | Dichterbiographie | 
| **Verwandte Werke** | Intelligente Links | Gleicher Autor, gleicher Titel oder gleiches Thema | 

Schalten Sie jeden Abschnitt beim Lesen ein oder aus. **Private Notizen** werden unten angezeigt – Ihre persönlichen Anmerkungen, nur für Sie sichtbar (synchronisiert über iCloud, wenn aktiviert). 

### Mehr Menü (⋯)

| Artikel | Was es tut | 
|------|----------------| 
| **Schriftgröße** | Öffnet das Skalierungsfenster (50 %–300 %, Standardbasis 22 pt) | 
| **Fesselnde Lektüre** | Ablenkungsfreie Vollbildansicht (Teil 5) | 
| **Pinyin** | Werkspezifische Überschreibung der globalen Pinyin-Einstellung | 
| **Vertikales Layout** | Überschreibung der Leserichtung pro Werk | 
| **Volltext kopieren** | Kopiert das gesamte CI in die Zwischenablage | 
| **Text teilen** | Systemfreigabeblatt mit Klartext | 
| **Aktienkarte generieren** | Öffnet den Bildkarten-Editor mit 13 Stilen (Teil 11) | 
| **Private Notiz** | Fügen Sie Ihre persönliche Notiz für dieses Werk hinzu oder bearbeiten Sie sie | 

### Leseoptionen 

- **Pinyin** – globale Standardeinstellung in den Einstellungen; Überschreibung pro Werk im Detail 
- **Vertikales Layout** – klassisches Lesen von oben nach unten; Überschreibung pro Werk 
- **Originaltext zentrieren** – standardmäßig aktiviert; Richtet den Haupttextblock aus 
- **Systemübersetzung** (iOS 17.4+) – Apples Übersetzungsfenster für ausgewählten Text 
- **Abschnitt umschaltbar** – Übersetzung, Notizen, Kommentar, Cipai-Einführung, Autorenbiografie ein-/ausblenden 

### TTS vorlesen 

Tippen Sie auf das **Lautsprechersymbol**, um die Text-zu-Sprache auf dem Gerät zu aktivieren. Verwendet Systemstimmen – kein Netzwerk. Ideal zum Zuhören beim Pendeln oder zum Lernen der Aussprache mit sichtbarem Pinyin.

### Langes Drücken auf Listenzeilen 

Drücken Sie in einer Arbeitsliste **lange** auf eine Zeile, um schnelle Aktionen auszuführen: **Favoriten**, **Vorlesen**, **Teilen** oder **Aus dem Verlauf entfernen** (in Verlaufsansichten). 

### Deep-Link 

Öffnen Sie ein bestimmtes Werk mit der Katalog-ID: `isongci://poem?id=42` 

--- 

## Teil 5 – Immersives Lesen 

Rufen Sie unter Detail **Mehr → Immersive Lektüre** eine übersichtliche Vollbildseite auf, die zum Rezitieren, Präsentieren und gezielten Lernen konzipiert ist. 

### Layout 

- **Vertikal** – klassischer Scroll-Stil von oben nach unten (Standard für immersiv) 
- **Horizontal** – moderner Fluss von links nach rechts 
- Wechseln Sie jederzeit in den immersiven Modus; Die Präferenz kann den globalen Einstellungen folgen 

### Typografie & Atmosphäre 

- **Kalligraphie-inspirierte Schriftart** für den Haupttext – erinnert an die Pinselschrift von Song Ci 
- **Hintergrund aus Xuan-Papier (宣纸)** – warmes, strukturiertes literarisches Gefühl 
- Passt sich an Ihr **Hell/Dunkel/System**-Thema und Ihre **Akzentfarbe** an 

### Steuerelemente 

- Ziehen Sie die Finger zusammen oder verwenden Sie die **Schriftskalierung**-Steuerung (50 %–300 %). 
- Tippen, um Chrome ein-/auszublenden (Symbolleiste, Abschnitt umschaltbar) 
- **TTS** verfügbar, ohne den immersiven Modus zu verlassen 
- Wischen Sie oder verwenden Sie die Pfeile, um im aktuellen Listenkontext zum **vorherigen/nächsten** Werk zu wechseln 

### Am besten für

- iPad-Präsentation oder Schreibtischlektüre 
- Auswendiglernen und Rezitationsübungen 
- Screenshots und Sharecard-Vorbereitung 

--- 

## Teil 6 – Favoriten 

### Darsteller funktionieren 

Tippen Sie auf **♥** auf ein beliebiges Arbeitsdetail oder drücken Sie lange auf eine Listenzeile → **Favorit**. In den bevorzugten Zeilen wird Ihre **Akzentfarbe** für den Stern verwendet. 

### Layouts der Registerkarte „Favoriten“. 

Öffnen Sie die Registerkarte **Favoriten**. Tippen Sie auf **⋯**, um zu wechseln: 

| Layout | Am besten für | 
|--------|----------| 
| **Liste** | Dichtes Scannen mit Titel, Autor, Cipai | 
| **Gitter** | Visuelles Browsen mit anpassbaren Spalten | 
| **Karten** | Große Vorschaukarten mit Auszug | 

### Gruppierung 

Organisieren Sie Ihre Sammlung nach: 

| Gruppieren nach | Verhalten | 
|----------|----------| 
| **Autor** | Cluster arbeitet unter jedem Dichter | 
| **Dynastie** | 五代 / 北宋 / 南宋 Abschnitte | 
| **Cipai** | Gruppiert nach Melodiemuster | 

### Stapelbearbeitung 

Tippen Sie auf der Favoritenseite auf **Bearbeiten**: 

- **Mehrfachauswahl** funktioniert mit Häkchen 
- **Alle auswählen / Alle abwählen** 
- **Batch-Entfernung** aus Favoriten (mit Bestätigung) 

Wischen Sie in einer Zeile nach links, um schnell die Aktion **Entfernen** auszuführen. 

### Lieblings-Ci-Widget 

Das **Lieblings-Ci**-Startbildschirm-Widget rotiert durch Ihre markierten Werke – eine persönliche tägliche Auswahl aus Ihrer eigenen Sammlung. 

### Exportieren

**Einstellungen → Daten → Favoriten exportieren** – Geben Sie Ihre Sammlung als Datei zur Sicherung oder Migration frei. 

--- 

## Teil 7 – Suche 

Öffnen Sie unter iOS die **Handschrift-Lyric-Suche** über das Steuerelement neben der Home-Suche, wenn Sie lieber Zeichen zeichnen als Pinyin eingeben möchten. 

iSongCi bietet **zweistufige Offline-Suche** – zuerst schnelle Metadaten, bei Bedarf ausführlicher Volltext. 

### Stufe 1 – Sofortige Metadatensuche 

Während Sie tippen, gleicht die App sofort die gebündelten Metadaten ab: 

- **Titel** (CI-Namen) 
- **Autorennamen** 
- **Cipai-Namen** 
- **Tags und Kategorien** 

Kein Lade-Spinner – Ergebnisse werden bei jedem Tastendruck angezeigt. 

### Stufe 2 – Lazy-Volltext-Tiefensuche 

Bei Übereinstimmungen auf Zeilenebene innerhalb von CI-Körpern lädt die App bei der ersten Tiefensuche langsam **`fulltext.json`** aus dem Bundle. Nach dem einmaligen Laden läuft die Volltextsuche vollständig auf dem Gerät. 

- Entspricht **jeder Zeile** im 21.592 Werke umfassenden Korpus 
- Beim ersten Start der Tiefensuche etwas langsamer; danach zwischengespeichert 
- **Kein Netzwerk** – Datei wird mit der App geliefert 

### Spezielle Registerkarte „Suche“ (iOS 26+) 

Unter **iOS 26 und höher** verfügt die Suche über eine eigene Registerkarte in der Registerkartenleiste. Verwenden Sie in früheren Versionen das Suchfeld unter **Durchsuchen** oder die Systemintegrationen unten. 

### Spotlight

Die App indexiert bis zu **~1.000 Werke** für die System-Spotsuche. Tippen Sie auf ein Spotlight-Ergebnis, um dieses Werk direkt in iSongCi zu öffnen.

### Siri & Deep Links

- Siri: *„In iSongCi suchen“* (mit Stichwort)
- Deep Link: `isongci://search?q=明月`

### Suchtipps

| Tipp | Warum |
|-----|-----|
| Autor + Stichwort suchen | Engt große Ergebnismengen ein |
| Probieren Sie den Cipai-Namen | Findet alle Werke in einem Melodiemuster |
| Verwenden Sie eine bekannte Zeile | Aktiviert die Volltext-Ebene für Zeilenübereinstimmung |
| In traditionellem Chinesisch suchen | UI wandelt; Korpus stimmt mit vereinfachtem Original überein |

---

## Teil 8 — Themen & Erscheinungsbild

Öffnen Sie **Einstellungen → Erscheinungsbild**.

### Themenmodus

| Modus | Verhalten |
|------|----------|
| **Hell** | Papierheller Lesehintergrund |
| **Dunkel** | Tinten-dunkles Nachtlesen |
| **System** | Folgt dem iOS-/macOS-Erscheinungsbild |

### Akzentfarbe — 15 Voreinstellungen + benutzerdefiniert

Wählen Sie aus **15 Themenvoreinstellungen**, inspiriert von der Ästhetik der Song-Dynastie:

| # | Voreinstellung | Stimmung | 
|---|--------|------| 
| 1 | 水墨 Tinte | Neutrales literarisches Grau | 
| 2 | Beschreibung Rouge | Warmer purpurroter Akzent | 
| 3 | 朱砂 Cinnabar | Klassisches Siegelrot | 
| 4 | 青瓷 Seladon | Kühle grüne Glasur | 
| 5 | 松绿 Kiefer | Tiefes Waldgrün | 
| 6 | 黛蓝 Indigo | Blauschwarz des Gelehrten | 
| 7 | 群青 Azure | Helles Mineralblau | 
| 8 | 青莲 Lotus | Lila-blaue Blüte | 
| 9 | 琥珀 Amber | Goldener warmer Ton | 
| 10 | 赭金 Ocker | Erdiges Goldbraun | 
| 11 | 月白 Mond | Blass silberweiß | 
| 12 | 竹青 Bambus | Frisches Bambusgrün | 
| 13 | 藕荷 Lotuswurzel | Zartes Rosa-Lavendel | 
| 14 | 玄色 Ebenholz | Tiefschwarzer Akzent | 
| 15 | Seide | Gealtertes Manuskript gelb | 

Tippen Sie auf ein beliebiges Farbfeld – ausgewählten Ring + Häkchen. Oder wählen Sie **Benutzerdefiniert**, um eine beliebige Farbe aus der Farbauswahl des Systems auszuwählen. 

Die Akzentfarbe gilt für: Lieblingssterne, Schaltflächen, Hervorhebungen, Share-Card-Akzente und Widget-Tönung (wenn **App-Design folgen** aktiviert ist). 

### Sprache 

**Englisch / 简体中文 / 繁體中文** – Die Benutzeroberfläche wechselt sofort. Der Korpustext wird in vereinfachtem Chinesisch gespeichert; Bei der herkömmlichen Anzeige wird die Konvertierung auf dem Gerät verwendet. 

### iCloud-Synchronisierung 

**Darstellung** (Hell/Dunkel/System), **Akzentvoreinstellung** und **Schriftartskalierung** werden über optionales iCloud KVS synchronisiert. 

--- 

## Teil 9 – Widgets

### Fügen Sie ein Startbildschirm-Widget hinzu 

1. Drücken Sie lange auf den Startbildschirm → **Startbildschirm bearbeiten** → tippen Sie auf ***** 
2. Suchen Sie nach **iSongCi** / **爱宋词** 
3. Wählen Sie einen Widget-Typ und eine Widget-Größe aus → **Widget hinzufügen** 

### Widget-Typen 

| Widget | Größen | Verhalten | 
|--------|-------|----------| 
| **Tägliches Ci** | Klein / Mittel / Groß + Sperrbildschirm | Das heutige deterministische ci; Tippen öffnet Details | 
| **Zufälliges Ci** | Klein / Mittel / Groß + Sperrbildschirm | Serendipity-Pick; wird auf der Timeline aktualisiert | 
| **Lieblings-Ci** | Klein / Mittel | Öffnet Ihre Favoriten | 
| **Strecke** | Klein / Rund (Sperrbildschirm) | Lesestreifenanzahl und Flammensymbol | 

### Sperrbildschirm-Widgets 

Wechseln Sie beim Hinzufügen von Widgets zur Anpassungsseite **Sperrbildschirm** und wählen Sie rechteckiges, rundes oder Inline-Zubehör von iSongCi. 

### Widget-Thema 

**Einstellungen → Widgets → App-Design folgen** – Widgets passen zu Ihrer Hell-/Dunkel-/Akzentauswahl. 

### Kontrollzentrum (iOS 18+) 

Fügen Sie unter iOS 18 und höher Steuerelemente für **Today's Ci**, **Serendipity** und **Suche** über **Einstellungen → Kontrollzentrum** hinzu. 

### Fehlerbehebung bei Widgets

- Öffne die App einmal nach der Installation, damit der tägliche Ci-Cache in die App-Gruppe geschrieben wird
- Wenn der Text nach einer Sprachänderung falsch aussieht, öffne die App kurz — sie aktualisiert automatisch die Widget-Caches
- Das tägliche Ci-Widget wird um Mitternacht lokal aktualisiert
- Das zufällige Ci-Widget aktualisiert seine Timeline periodisch für Abwechslung

### Widget-Anleitung in der App

**Einstellungen → Widgets → Widget-Anleitung** oder `isongci://widget-guide` für Screenshots und Tipps zu einzelnen Widgets.

---

## Teil 10 — Siri, Kurzbefehle & Aktionen auf dem Home-Bildschirm

### Siri-Intents (3)

| Intent | Beispielphrase |
|--------|----------------|
| **Heute Ci** | "Today's ci in iSongCi" |
| **Serendipity** | "Serendipity in iSongCi" |
| **Ci suchen** | "Search in iSongCi" (mit Schlüsselwort) |

Füge diese in der **Kurzbefehle**-App für Automatisierungen hinzu — z. B. `isongci://daily` jeden Morgen öffnen.

### Schnellaktionen auf dem Home-Bildschirm (15 verfügbar, max. 4 aktiviert)

Drücke lange auf das App-Symbol. Anpassen in **Einstellungen → Kurzbefehle → Schnellaktionen auf dem Home-Bildschirm**:

| # | Aktion | Öffnet | 
|---|--------|-------| 
| 1 | Das heutige Ci | `isongci://daily` | 
| 2 | Zufall | `isongci://random` | 
| 3 | Weiterlesen | `isongci://continue-reading` | 
| 4 | Favoriten | `isongci://favorites` | 
| 5 | Suche | `isongci://search` | 
| 6 | Durchsuchen | `isongci://category` | 
| 7 | Startseite | `isongci://home` | 
| 8 | Einstellungen | `isongci://settings` | 
| 9 | Nutzungsleitfaden | `isongci://usage-guide` | 
| 10 | Widget-Anleitung | `isongci://widget-guide` | 
| 11 | Shortcuts-Leitfaden | `isongci://shortcuts-guide` | 
| 12 | Funktionsleitfaden | `isongci://feature-guide` | 
| 13 | Feedback | `isongci://feedback` | 
| 14 | In-App-Rezension | `isongci://in-app-review` | 
| 15 | Home-Verknüpfungen-Einstellungen | `isongci://home-shortcuts` | 

Only **4** appear on the icon menu at once — pick your most-used four.

 ### Deep Links (`isongci://`) 

Vollständige Referenz: [Shortcut-Links](../url-scheme). Gängige URLs: 

| URL | Öffnet | 
|-----|-------| 
| `isongci://poem?id=42` | Ci-Detail nach Katalog-ID | 
| `isongci://author?id=12` | Autorenprofil | 
| `isongci://daily` | Das heutige Ci | 
| `isongci://random` | Zufall | 
| `isongci://continue-reading` | Weiterlesen | 
| `isongci://search?q=明月` | Suchen Sie nach 明月 | 
| `isongci://favorites` | Registerkarte „Favoriten“ | 

Use in Shortcuts, Notes, Safari, or MDM configuration profiles.

 ### Shortcuts-Anleitung in der App

**Einstellungen → Verknüpfungen → Anleitung zu Verknüpfungen** oder `isongci://shortcuts-guide` – Schaltflächen zum Kopieren mit einem Tastendruck für jede URL. 

--- 

## Teil 11 – Share Cards (13 Stile) 

Aus dem Detail **Mehr → Share-Karte generieren**: 

| Stil | Stimmung | 
|-------|------| 
| Klassisch | Sauberes literarisches Layout | 
| Tinte | Brush-and-Wash-Ästhetik | 
| Minimal | Typografie-fokussiert | 
| Vertikal | Klassisch von oben nach unten | 
| Zinnober | Robbenroter Akzent | 
| Dunkel | Nachttintenhintergrund | 
| Seladon | Cooles Keramikgrün | 
| Ocker-Gold | Warmer Goldton | 
| Schneewittchen | Helles Papierweiß | 
| Scrollen | Horizontales Scrollmotiv | 
| Mondweiß | Blasse Mondlichtpalette | 
| Bambusschatten | Grüne Bambusstruktur | 
| Xuan-Papier | Strukturierter Hintergrund | 

### Exportoptionen 

- **Volltext** vs. **Auszug** – für das nächste Mal gespeichert 
- **3-fache Auflösung** PNG – scharf auf Retina-Displays und sozialen Medien 
- **PNG exportieren** – in Fotos speichern oder über eine beliebige App teilen 
- Stilpräferenz automatisch gespeichert 

Erfordert die Berechtigung **Fotobibliothek (Hinzufügen)** nur beim Speichern in Fotos – nur Schreibzugriff, kein Lesezugriff. 

--- 

## Teil 12 – iCloud-Synchronisierung 

Optionale Synchronisierung über **iCloud Key-Value Store** – kein iHTC Studio-Server.

| Synchronisiert | Nicht synchronisiert | 
|--------|------------| 
| Favoriten | Schnellaktionsoptionen auf dem Startbildschirm | 
| Private Notizen | Onboarding-/Welcome-Guide-Flags | 
| Aussehen (hell/dunkel/system) | Widget-Shuffle-Status | 
| Akzentfarbe und Schriftskala | Ci-Text (immer im App-Bundle) | 
| Sichtbarkeit der Registerkarte „Durchsuchen/Favoriten“ | Volltext-Cache durchsuchen | 
| Lesesträhne | Benutzerdefinierter Farbton für die Akzentauswahl (auf neuem Gerät erneut auswählen) | 

Einschalten: **Einstellungen → Daten → iCloud-Synchronisierung**. Erfordert eine iCloud-Anmeldung auf dem Gerät. **Ci-Text wird niemals hochgeladen** – nur Ihre persönlichen Daten und Präferenzen. 

--- 

## Teil 13 – Benachrichtigungen 

### Tägliche Ci-Erinnerung 

Die optionale **lokale Benachrichtigung** erinnert Sie daran, die heutige Ci zu lesen. 

| Einstellung | Standort | 
|---------|----------| 
| Aktivieren/Deaktivieren | **Einstellungen → Benachrichtigungen** | 
| Erinnerungszeit | Wählen Sie Ihre bevorzugte Stunde und Minute | 
| Erlaubnis | iOS fragt bei der ersten Aktivierung – kein Server beteiligt | 

Benachrichtigungen werden **vollständig auf dem Gerät geplant**. Kein Push-Server, kein Tracking-Pixel, keine Remote-Payload. 

### Tipps

- Wenn die Erinnerungen nach einem iOS-Update nicht mehr angezeigt werden, öffnen Sie die App einmal, um einen neuen Termin zu vereinbaren 
- Das Deaktivieren von Benachrichtigungen hat keinen Einfluss auf die Lesestreak-Logik 
- Streak zählt, wenn Sie ein Arbeitsdetail öffnen – die Benachrichtigung ist nur eine optionale Ermutigung 

--- 

## Teil 14 – Einstellungen und Anleitungen 

Öffnen Sie **Einstellungen**. Abschnitte von oben nach unten: 

### Aussehen 

- **Thema** – Hell / Dunkel / System 
- **Akzentfarbe** – 15 Voreinstellungen + benutzerdefiniert (Teil 8) 
- **Sprache** – Englisch / 简体中文 / 繁體中文 

### Lesen 

- **Schieberegler für die Schriftgröße** – kontinuierliche Skalierung von 50 %–300 % (auch im Menü „Mehr“ im Detail) 
- **Vertikale Lesung** – globales Umschalten 
- **Pinyin** – standardmäßig aktiviert 
- **Originaltext zentrieren** – standardmäßig aktiviert 
- **Kalligraphie-Schriftart** – immersive und detaillierte Typografie 

### Daten 

- **Lesesträhne** – Statistiken zur Lesesträhne anzeigen 
- **iCloud Sync** – optional (Teil 12) 
- **Favoriten exportieren** – Sammlung als Datei teilen 

### Tab-Leiste 

- Sichtbarkeit der Registerkarte **Durchsuchen** umschalten (standardmäßig aktiviert) 
- Sichtbarkeit der Registerkarte **Favoriten** umschalten (standardmäßig aktiviert) 

### Widgets 

- **Widget-Anleitung** – Anweisungen pro Widget 
- **App-Thema folgen** umschalten 

### Verknüpfungen 

- **Schnellaktionen auf dem Startbildschirm** – wählen Sie bis zu 4 von 15 aus 
- **Shortcuts Guide** – Deep-Link-Referenz mit Kopierschaltflächen

### Benachrichtigungen 

- **Tägliche Ci-Erinnerung** – Aktivierung, Uhrzeit, Berechtigungsstatus 

### Hilfe 

- **Nutzungsleitfaden** – Replay-Feature-Tour 
- **Feature Guide** – ausführlichere Feature-Karten (`isongci://feature-guide`) 
- **Feedback senden** – öffnet E-Mail (`isongci://feedback`) 

### Über 

- Versionsnummer 
- **Trinkgeldglas** – optionaler In-App-Kauf `com.iHTCboy.iSongCi.6` (abgewickelt durch Apple StoreKit) 
- App Store-Link 
- Willkommens-Onboarding noch einmal abspielen 

--- 

## Teil 15 – Holen Sie sich die App 

| Kanal | Link | 
|---------|------| 
| App Store | [Im App Store herunterladen](https://apps.apple.com/app/id6788433450) | 

### Systemanforderungen 

| Plattform | Minimum | 
|----------|---------| 
| iPhone / iPad | iOS 17.0+ (Registerkarte „Suchen“: iOS 26.0+) | 
| Mac | macOS 13.0+ | 

### Kontakt 

- **E-Mail:** [AppleOSer@gmail.com](mailto:AppleOSer@gmail.com) – wir antworten normalerweise innerhalb von 48 Stunden. 

### Optionales Trinkgeldglas 

Wenn Ihnen iSongCi gefällt, beachten Sie den optionalen Tipp über **Einstellungen → Info**. Produkt-ID: `com.iHTCboy.iSongCi.6`. Die Zahlungsabwicklung erfolgt vollständig über Apple. 

[FAQ](../faq) · [Shortcut-Links](../url-scheme) · [Datenschutzerklärung](../privacy)

</section>
<section lang="fr" markdown="1">

### L'application est-elle entièrement hors ligne ? 

Oui. Toutes les **21 592 œuvres Song Ci** sont regroupées. Après l'installation, l'application n'effectue **aucune requête réseau sortante** : pas de compte, pas de publicité, pas d'analyse. iCloud en option utilise le service Apple uniquement lorsque vous l'activez. 

### En quoi est-ce différent des applications de poésie Tang/poésie générique ? 

iSongCi est **vertical par rapport à Song Ci (宋词)** — et non un catalogue de poésie mixte Tang/Song/Yuan. Il ajoute **1 461 connaissances cipai**, **traduction simple et commentaires modernes**, **lecture verticale immersive** avec pinyin, ci quotidien, cartes de partage, widgets, centre de contrôle, Siri et iCloud en option. 

### Quelle quantité de contenu est incluse ? 

| Article | Comte | 
|------|-------| 
| Travaux Ci (total) | 21 592 | 
| Auteurs | 1 509 | 
| Cipai (modèles de mélodies) | 1 461 | 
| Cipai en vedette avec intro | 60 | 
| Traductions simples | 11 029 | 
| Commentaire moderne | Tous les travaux | 
| Collections | 12 (Haofang 363 · Wanyue 520 · 10 ensembles thématiques) | 
| Dynasties | Cinq Dynasties, Song du Nord, Song du Sud | 

### Que sont la traduction simple, les notes classiques et les commentaires modernes ? 

Trois calques distincts sur la page de détails : basculez chaque section indépendamment :

- **Traduction simple (白话译文)** — rendu chinois moderne du texte intégral (~11 029 œuvres) 
- **Notes classiques (注释)** — annotations savantes traditionnelles lorsqu'elles sont disponibles 
- **Commentaire moderne (白话赏析)** — contexte, résumé et conseils de lecture générés automatiquement pour chaque ouvrage (à titre de référence, pas de citation académique) 

### Toutes les œuvres ont-elles des traductions ? 

Non. **11 029** œuvres incluent une traduction complète et simple ; le reste montre le texte original ainsi que des commentaires modernes. Les notes classiques apparaissent uniquement lorsque les données sources les incluent. L'application est un studio de lecture et de découverte, et non une édition académique complète de chaque ci. 

### Comment fonctionne le Ci d'aujourd'hui ? 

Une pièce est choisie **de manière déterministe parmi le pool présenté** (chefs-d'œuvre de Haofang + Wanyue) en utilisant le **jour calendaire comme graine** — tout le monde voit le **même ci à la même date**. Il se retourne à **minuit local**. Ouvrir depuis **Accueil** ou `isongci://daily`. 

### Qu'est-ce que le sérendipité ? 

**邂逅一词** tire une pièce **aléatoire** de la réserve en vedette – différente à chaque pression. Utilisez **Accueil → Serendipity**, `isongci://random`, le widget **Random Ci** ou Siri. 

### Quelle est la précision du pinyin ?

Le pinyin est **généré automatiquement** par segment. Cela fonctionne bien pour la plupart des lignes mais **peut mal lire les caractères polyphoniques** (多音字). Utilisez-le comme une aide à la lecture, pas comme une autorité de prononciation. 

### Affichage chinois traditionnel ? 

L'interface utilisateur a des chaînes **繁體中文** dédiées. Le texte du corpus est stocké en chinois simplifié et **converti au moment de l'affichage** (table s2t au niveau des caractères) pour le mode traditionnel — vous n'avez pas besoin de deux copies de la base de données. 

### Comment fonctionnent la lecture verticale et le pinyin ? 

Activez globalement dans **Paramètres → Lecture** (disposition verticale, pinyin, police de calligraphie). Dans n'importe quel détail de travail, vous pouvez ouvrir la **Lecture immersive** pour une page verticale (de droite à gauche) ou horizontale en plein écran avec un fond en papier xuan et une mise à l'échelle des polices indépendante. 

### Qu'est-ce que la lecture immersive ? 

**Détail → Plus → Lecture immersive** ouvre une page sans chrome, idéale pour réciter ou présenter sur iPad ou sur grand écran. Basculez vertical/horizontal et calligraphie à l'intérieur du lecteur. 

### Comment modifier la taille de la police ? 

Curseur **Paramètres → Lecture**, ou **Détail → Plus → Taille de police**. Met à l'échelle le corps du texte indépendamment du type dynamique du système ; se synchronise via iCloud si activé. 

### Comment fonctionne la lecture à haute voix (TTS) ?

Appuyez sur l'icône **haut-parleur** dans la barre d'outils de détail. Utilise la synthèse vocale en mandarin sur l'appareil. Pause et reprise avec le même bouton. 

### Comment fonctionnent les favoris, les notes et iCloud ? 

**Favoris** — appuyez sur ♥ sur n'importe quelle œuvre. **Notes privées** — annotations par poème que vous seul pouvez voir (page de détail). **iCloud Sync** en option reflète les favoris, les notes, l'apparence, l'échelle de police, la visibilité des onglets et la séquence de lecture sur tous les appareils. **Le texte Ci n'est jamais téléchargé** : il reste toujours dans l'ensemble d'applications. 

### Quelles sont les règles des séries de lecture ? 

Ouvrez **n'importe quel ci** dans l'application pour compter pour ce jour calendaire. **Jours consécutifs** augmentez votre séquence ; **sautez plus d'un jour** et la séquence se réinitialise à zéro lors de la prochaine ouverture. **Nombre total de lectures** suit les pièces ouvertes à vie. Streak apparaît sur Accueil et sur le widget **Reading Streak**. 

### Quels styles de cartes de partage existent ? 

**13 styles :** Classique, Lavis à l'encre, Sceau de cinabre, Parchemin de soie, Parchemin long, Or ocre, Neige d'hiver, Paysage vert, Feuilles de bambou, Argent au clair de lune, Minimal, Foncé minimal, Script vertical. Choisissez le texte intégral ou un extrait ; inclure éventuellement des commentaires ; exporter PNG à une résolution 3×. 

### Quels widgets sont disponibles ?

| Widget | Objectif | 
|--------|---------| 
| Ci d'aujourd'hui | La pièce phare du jour | 
| Sérendipité | Ci sélectionné au hasard (rafraîchit toutes les heures) | 
| Ci préféré | Dernière œuvre étoilée | 
| Série de lecture | Jours consécutifs + nombre total de lectures | 
| Centre de contrôle | Ouvrez en un seul clic le Ci d'aujourd'hui (iOS 18+) | 

Tailles : Petite/Moyenne/Grande sur l'écran d'accueil ; Écran de verrouillage circulaire, en ligne ou rectangulaire. Prend en charge **StandBy**. La langue du widget suit la **langue de l'application**, et non la langue du système. 

### Le widget affiche un texte erroné ou vide ? 

1. Ouvrez l'application une fois après l'installation 
2. Tirez pour actualiser l'accueil pour réécrire le cache des widgets 
3. Après avoir changé la langue, ouvrez brièvement l'application pour actualiser 
4. **Ci** préféré nécessite au moins une œuvre étoilée 
5. **Reading Streak** nécessite que vous ouvriez d'abord une œuvre dans l'application. 
6. Assurez-vous que les widgets sont autorisés pour iSongCi dans les paramètres système 

### Qu'est-ce que le widget Control Center (iOS 18+) ? 

Ajoutez **Aujourd'hui Ci** depuis **Paramètres → Centre de contrôle** (ou l'éditeur du Centre de contrôle du système). Nécessite **iOS 18.0+**. En appuyant sur, l'application s'ouvre directement sur la pièce d'aujourd'hui. 

### Quels raccourcis Siri existent ? 

Trois intentions d'application sont livrées avec l'application :

| Intention | Exemple de phrase | 
|--------|----------------| 
| Ouvrez le Ci d'aujourd'hui | "Le ci d'aujourd'hui dans iSongCi" | 
| Ci aléatoire | « Sérendipité dans iSongCi » | 
| Rechercher Ci | "Rechercher dans iSongCi" (avec mot-clé) | 

Configurez jusqu'à **4 actions rapides sur l'écran d'accueil** dans Paramètres. Liste complète des liens profonds dans [Liens de raccourci] (../url-scheme). 

### Quelles sont les limitations de Spotlight ? 

Spotlight indexe le **pool en vedette ainsi que vos favoris** — jusqu'à **~1 000** entrées. Les œuvres rares n'apparaîtront pas dans la recherche du système ; utilisez plutôt la **recherche approfondie en texte intégral dans l'application** (charge paresseusement le corpus complet). Appuyez sur un résultat Spotlight pour ouvrir ce ci directement. 

### Puis-je masquer les onglets ? 

Oui. **Paramètres → Barre d'onglets** : basculez entre les onglets **Catégories** et/ou **Favoris**. Les onglets masqués restent accessibles via des actions détaillées, des menus à pression longue, des widgets et des liens `isongci://`. 




|---------|---------------|------------------| 
| Actions rapides sur l'écran d'accueil | ✅ | ❌ | 
| Widgets et centre de contrôle | ✅ (iOS 18+CC) | Widgets principalement sur iPhone/iPad | 
| Retour haptique | ✅ | ❌ | 
| Onglet Recherche dédiée | iOS26+ | Recherche via bouton / feuille | 
| Lecture de base, favoris, iCloud | ✅ | ✅ | 

### L'application est-elle gratuite ? Qu'est-ce que le pot à pourboires ?

**Entièrement gratuit** : les 21 592 œuvres et toutes les fonctionnalités, sans abonnement, ni publicité. Un **pot de conseils facultatif** (`com.iHTCboy.iSongCi.6`) vous permet de prendre en charge le développement via l'achat Apple In-App ; cela ne débloque rien de plus. 

### Configuration système requise 

| Plateforme | Minimum | 
|--------------|---------| 
| iPhone/iPad | iOS 17.0+ | 
| Mac | macOS 13.0+ | 
| Widget du Centre de contrôle | iOS 18.0+ | 
| Panneau de traduction du système | iOS 17.4+ / macOS 14.4+ | 

### Comment puis-je obtenir l'application ? 

[Télécharger sur l'App Store](https://apps.apple.com/app/id6788433450) (ID d'application **6788433450**). 

### Comment contacter l'assistance ? 

[AppleOSer@gmail.com](mailto:AppleOSer@gmail.com) — nous répondons généralement dans les 48 heures. 

--- 

### Comment fonctionne la lecture continue ? 

Activez la **lecture continue** dans Paramètres → Lecture. Une fois le travail terminé TTS, une barre inférieure apparaît ; si vous ne faites rien pendant quelques secondes, l'élément suivant de la file d'attente actuelle (parcourir / playlist / favoris / quotidien) démarre automatiquement. Vous pouvez également choisir des lignes lors de la génération de cartes de partage. 

### Comment fonctionnent les rappels quotidiens ?

Les **notifications locales** facultatives vous rappellent de lire le ci d'aujourd'hui. Appuyez sur la notification pour ouvrir l'œuvre correspondante via un lien profond. La désactivation des notifications n'efface pas votre séquence de lecture. 

## Guide de l'utilisateur complet 

Les sections ci-dessous constituent la présentation complète du produit précédemment sur la page d'assistance. Les éléments de questions-réponses rapides restent ci-dessus (le cas échéant). 

--- 

## Partie 1 — Premier lancement et interface 

### Guide de bienvenue 

Lors du premier lancement, un **guide de bienvenue de plusieurs pages** présente l'application : échelle de la bibliothèque, ci quotidien, lecture immersive, favoris, widgets et confidentialité. Parcourez chaque page, puis appuyez sur **Commencer**. Rejouez à tout moment : **Paramètres → Aide → Guide d'utilisation** ou lien profond `isongci://feature-guide`. 

### Présentation de la barre d'onglets 

| Onglet | Ce qu'il fait | 
|-----|----------------| 
| **Accueil** | Ci d'aujourd'hui, Serendipity, Continuer la lecture, séquence de lecture, avant-premières thématiques | 
| **Parcourir** | Auteurs, cipai, dynasties, genres, collections thématiques, catalogue complet | 
| **Favoris** | Les favoris fonctionnent avec les dispositions et le regroupement de listes/grilles/cartes | 
| **Paramètres** | Apparence, lecture, données, onglets, widgets, raccourcis, aide | 
| **Recherche** | Recherche instantanée de métadonnées + recherche approfondie en texte intégral paresseuse (onglet dédié sur **iOS 26+**) |

> **Conseil :** Masquez l'onglet **Parcourir** ou **Favoris** dans **Paramètres → Barre d'onglets**. Si vous fermez l'onglet sur lequel vous vous trouvez, l'application revient automatiquement à l'accueil. La visibilité des onglets se synchronise via iCloud en option. 

### Plateformes 

| Plateforme | Minimum | 
|--------------|---------| 
| iPhone/iPad | iOS 17.0+ | 
| Mac | macOS 13.0+ | 

L'**onglet Recherche** dédié nécessite **iOS 26+**. Sur les versions iOS antérieures, la recherche est disponible depuis la page Parcourir ou via Spotlight/Siri. 

### Confidentialité lors de l'installation 

- **Pas d'inscription · pas de publicité · pas de SDK d'analyse** 
- Corpus est livré dans l'ensemble d'applications - pas de CDN, pas de télémétrie 
- iCloud en option utilise **votre iCloud privé** uniquement ; le texte ci n'est jamais téléchargé 

--- 

## Partie 2 — Accueil 

L'onglet **Accueil** est votre point d'entrée quotidien : une découverte organisée sans parcourir 21 592 œuvres. 

### Ci d'aujourd'hui (每日一词) 

Un **sélection quotidienne déterministe** — le même ci pour tout le monde à la même date calendaire, choisi dans la bibliothèque complète par un algorithme basé sur la date. Appuyez sur la carte pour ouvrir la page de détails complète. 

- S'actualise automatiquement à **minuit local** 
- Écrit dans le stockage **App Group** au lancement de l'application afin que les widgets **Daily Ci** restent synchronisés 
- Lien profond : `isongci://daily` 
- Siri : *"Le ci d'aujourd'hui dans iSongCi"*

### Sérendipité (邂逅一词) 

Appuyez sur **Serendipity** pour un **ci** sélectionné au hasard : idéal lorsque vous souhaitez une surprise plutôt que le choix fixe du jour. Chaque pression dessine une nouvelle pièce de la bibliothèque hors ligne. 

- Lien profond : `isongci://random` 
- Siri : *"Sérendipité dans iSongCi"* 

### Continuer la lecture 

Si vous avez récemment ouvert une œuvre, **Continuer la lecture** apparaît sur l'accueil avec le titre et l'auteur. Un simple clic reprend là où vous vous étiez arrêté. 

- Lien profond : `isongci://continue-reading` 
- Également disponible en tant qu'action rapide sur l'écran d'accueil 

### Séquence de lecture 

Accueil affiche votre **série de lecture** : les jours consécutifs pendant lesquels vous avez lu au moins un ci, plus un nombre cumulé de lectures. L'ouverture de n'importe quel détail de travail compte pour la séquence d'aujourd'hui. 

- Synchronisé via **iCloud KVS** en option 
- Le widget **Streak** affiche une séquence sur l'écran d'accueil et l'écran de verrouillage 

### Aperçus thématiques 

Faites défiler vers le bas pour accéder aux cartes d'accès rapide : **cipai en vedette**, **collections thématiques**, genres **豪放 / 婉约** et faits saillants de la **dynastie**. Appuyez sur **Afficher tout** pour accéder à Parcourir dans cette section. 

### Actions rapides sur l'écran d'accueil

Appuyez longuement sur l'icône de l'application pour accéder à des raccourcis tels que **Today's Ci**, **Serendipity**, **Continuer la lecture**, **Favoris** et **Recherche**. Personnalisez jusqu'à **4** éléments dans **Paramètres → Raccourcis → Actions rapides de l'écran d'accueil** (15 actions disponibles — voir partie 10). 

--- 

## Partie 3 — Parcourir 

Ouvrez l'onglet **Parcourir**. Plusieurs sections vous permettent d'explorer la bibliothèque sous différents angles : 

### 1. Auteurs (名家) 

**1 509 poètes Song Ci** avec biographies. Appuyez sur un auteur pour son profil et sa liste de travail complète. 

- Changer de disposition via **⋯** : **Liste**, **Grille** ou **Cartes** 
- Nombre de colonnes de la grille (2 à 4) mémorisé séparément sur iPhone et iPad 
- Lien profond : `isongci://author?id=12` 

### 2. Cipai (词牌) 

**1 461 modèles de mélodies cipai** dans l'index complet. **60 cipai en vedette** comprennent des essais d'introduction expliquant la forme, le rythme et l'ambiance représentative : apprenez le modèle, puis parcourez les œuvres écrites sur cet air. 

Exemples : 水调歌头, 念奴娇, 满江红, 蝶恋花, 浣溪沙. 

### 3. Dynasties (朝代) 

Naviguer par période historique : 

| Dynastie | Couverture | 
|---------|----------| 
| **五代** | Première tradition *ci* avant les Song | 
| **北宋** | Maîtres des chants du Nord | 
| **南宋** | Paroliers de chansons du Sud | 

### 4. Genres (流派)

| Genre | Comte | Caractère | 
|-------|-------|---------------| 
| **豪放** | 363 | Ton audacieux, expansif et héroïque | 
| **婉约** | 520 | Ton délicat, lyrique et intime | 

Les œuvres peuvent apparaître dans l'un ou les deux groupes, le cas échéant. 

### 5. Collections thématiques (主题) 

**10 collections thématiques** : amour, séparation, nostalgie, nature, patriotisme, philosophie, festivals et plus encore. Chaque collection regroupe des ci qui partagent un motif. 

### 6. Catalogue complet (全集) 

L'index complet des **21 592 travaux**. À utiliser lorsque vous voulez que tout soit dans une liste déroulante avec des options de tri et de filtrage. 

### Options de mise en page et de section 

Appuyez sur **⋯** sur les pages Parcourir ou Auteur : 

| Options | Ce qu'il fait | 
|--------|----------------| 
| **Mise en page** | Liste / Grille / Cartes | 
| **Visibilité des sections** | Afficher ou masquer n'importe quelle section de navigation | 
| **Ordre des sections** | Réorganiser l'apparence des sections | 
| **Colonnes de la grille** | 2 à 4 sur iPhone, 2 à 4 sur iPad (mémorisés séparément) | 

### Entrée de recherche (avant iOS 26) 

Sur iOS 17-25, ouvrez la recherche à partir du **champ de recherche** en haut de Parcourir ou via Spotlight/Siri. Sur **iOS 26+**, utilisez l'onglet **Recherche** dédié (partie 7). 

--- 

## Partie 4 — Lecture détaillée 

Appuyez sur n'importe quel ci pour ouvrir **Work Detail** — l'expérience de lecture principale.

### Barre d'outils (en haut à droite) 

| Bouton | Actions | 
|--------|--------| 
| **♥** | Ajouter ou supprimer des Favoris (utilise votre couleur d'accent lorsque vous êtes suivi) | 
| **Président** | Démarrez la **lecture TTS à haute voix** ; appuyez à nouveau pour mettre en pause/reprendre | 
| **⋯ Plus** | Ouvre le menu d'action (voir ci-dessous) | 

### Sections de contenu 

Toutes les œuvres n'ont pas toutes les couches. Les sections apparaissent uniquement lorsque le contenu existe : 

| Rubrique | Couverture | Ce que vous voyez | 
|---------|----------|--------------| 
| **Texte original** | Tous les 21 592 | Ci complet avec pinyin en option | 
| **Notes classiques** | Là où disponible | Annotations scientifiques traditionnelles | 
| **Traduction simple** | **11 029 œuvres** | Rendu vernaculaire moderne | 
| **Commentaire moderne** | Sous-ensemble organisé | Appréciation et contexte littéraire | 
| **Introduction à Cipai** | cipai en vedette et lié | Explication du modèle de réglage | 
| **Biographie de l'auteur** | 1 509 auteurs | Biographie du poète | 
| **Œuvres connexes** | Liens intelligents | Même auteur, cipai ou thème | 

Activez ou désactivez chaque section pendant la lecture. **Les notes privées** apparaissent en bas : vos annotations personnelles, visibles uniquement par vous (synchronisées via iCloud lorsqu'elles sont activées). 

### Plus de menu (⋯)

| Article | Ce qu'il fait | 
|------|----------------| 
| **Taille de la police** | Ouvre le panneau de mise à l'échelle (50 % à 300 %, base par défaut 22 pt) | 
| **Lecture immersive** | Affichage plein écran sans distraction (partie 5) | 
| **Pinyin** | Remplacement par travail du paramètre pinyin global | 
| **Disposition verticale** | Remplacement par œuvre du sens de lecture | 
| **Copier le texte intégral** | Copie l'intégralité du ci dans le presse-papiers | 
| **Partager du texte** | Feuille de partage système avec texte brut | 
| **Générer une carte de partage** | Ouvre l'éditeur de cartes image de style 13 (Partie 11) | 
| **Note privée** | Ajoutez ou modifiez votre note personnelle pour ce travail | 

### Options de lecture 

- **Pinyin** — valeur par défaut globale dans Paramètres ; remplacement par travail en détail 
- **Disposition verticale** — lecture classique de haut en bas ; remplacement par travail 
- **Centrer le texte original** — activé par défaut ; aligne le bloc de texte principal 
- **Traduction du système** (iOS 17.4+) – Panneau de traduction d'Apple pour le texte sélectionné 
- **La section bascule** — afficher/masquer la traduction, les notes, le commentaire, l'intro Cipai, la biographie de l'auteur 

### TTS lecture à haute voix 

Appuyez sur l'icône **haut-parleur** pour la synthèse vocale sur l'appareil. Utilise les voix du système – pas de réseau. Idéal pour écouter pendant les déplacements ou étudier la prononciation avec le pinyin visible.

### Appui long sur les lignes de la liste 

Dans n'importe quelle liste de travail, **appuyez longuement** sur une ligne pour effectuer des actions rapides : **Favoris**, **Lire à haute voix**, **Partager** ou **Supprimer de l'historique** (dans les vues de l'historique). 

### Lien profond 

Ouvrir une œuvre spécifique par ID de catalogue : `isongci://poem?id=42` 

--- 

## Partie 5 — Lecture immersive 

Depuis les détails **Plus → Lecture immersive**, accédez à une page plein écran propre conçue pour la récitation, la présentation et l'étude ciblée. 

### Disposition 

- **Vertical** — flux classique de haut en bas de style défilement (par défaut pour immersif) 
- **Horizontal** — flux moderne de gauche à droite 
- Basculez à tout moment en mode immersif ; la préférence peut suivre les paramètres globaux 

### Typographie & ambiance 

- **Police inspirée de la calligraphie** pour le texte principal — évoque Song Ci écrit au pinceau 
- **Fond en papier Xuan (宣纸)** — sensation littéraire chaleureuse et texturée 
- S'adapte à votre thème **clair/sombre/système** et à votre **couleur d'accent** 

### Contrôles 

- Pincez ou utilisez le contrôle **échelle de police** (50 % à 300 %) 
- Appuyez pour afficher/masquer Chrome (barre d'outils, bascule de section) 
- **TTS** disponible sans quitter le mode immersif 
- Faites glisser ou utilisez les flèches pour passer au travail ** précédent / suivant ** dans le contexte de la liste actuelle 

### Idéal pour

- Présentation sur iPad ou lecture de bureau 
- Pratique de la mémorisation et de la récitation 
- Captures d'écran et préparation de la carte de partage 

--- 

## Partie 6 — Favoris 

### Œuvres vedettes 

Appuyez sur **♥** sur n'importe quel détail du travail ou appuyez longuement sur une ligne de la liste → **Favoris**. Les lignes favorites utilisent votre **couleur d'accent** pour l'étoile. 

### Dispositions de l'onglet Favoris 

Ouvrez l'onglet **Favoris**. Appuyez sur **⋯** pour changer : 

| Mise en page | Idéal pour | 
|--------|----------| 
| **Liste** | Numérisation dense avec titre, auteur, cipai | 
| **Grille** | Navigation visuelle avec colonnes réglables | 
| **Cartes** | Grandes cartes d'aperçu avec extrait | 

### Regroupement 

Organisez votre collection par : 

| Regrouper par | Comportement | 
|----------|----------| 
| **Auteur** | Clusters travaille sous chaque poète | 
| **Dynastie** | Sections 五代 / 北宋 / 南宋 | 
| **Cipaï** | Groupes par modèle de mélodie | 

### Modification par lots 

Appuyez sur **Modifier** sur la page Favoris : 

- **La sélection multiple** fonctionne avec des coches 
- **Sélectionner tout / Tout désélectionner** 
- **Suppression par lots** des favoris (avec confirmation) 

Faites glisser votre doigt vers la gauche sur une ligne pour effectuer une action **Supprimer** rapide. 

### Widget Ci préféré 

Le widget d'écran d'accueil **Favorite Ci** fait défiler vos œuvres favorites : une sélection quotidienne personnelle de votre propre collection. 

### Exporter

**Paramètres → Données → Exporter les favoris** — partagez votre collection sous forme de fichier pour la sauvegarde ou la migration. 

--- 

## Partie 7 — Recherche 

Sur iOS, ouvrez la **recherche de paroles d'écriture manuscrite** à partir de la commande située à côté de la recherche Accueil lorsque vous préférez dessiner des caractères plutôt que de taper du pinyin. 

iSongCi propose une **recherche hors ligne à deux niveaux** : des métadonnées rapides d'abord, du texte intégral approfondi si nécessaire. 

### Niveau 1 – Recherche instantanée de métadonnées 

Au fur et à mesure que vous tapez, l'application compare instantanément les métadonnées regroupées : 

- **Titres** (noms ci) 
- **Noms des auteurs** 
- **Noms Cipai** 
- **Balises et catégories** 

Pas de fileur de chargement : les résultats apparaissent à chaque frappe. 

### Niveau 2 – Recherche approfondie en texte intégral paresseuse 

Pour les correspondances au niveau de la ligne dans les corps ci, l'application charge paresseusement **`fulltext.json`** à partir du bundle lors de la première utilisation de recherche approfondie. Après le chargement unique, la recherche en texte intégral s'exécute entièrement sur l'appareil. 

- Correspond à **n'importe quelle ligne** dans le corpus de 21 592 œuvres 
- Légèrement plus lent au premier lancement de la recherche approfondie ; mis en cache par la suite 
- **Zéro réseau** — le fichier est livré avec l'application 

### Onglet Recherche dédiée (iOS 26+) 

Sur **iOS 26 et versions ultérieures**, la recherche dispose de son propre onglet dans la barre d'onglets. Sur les versions antérieures, utilisez le champ de recherche dans **Parcourir** ou les intégrations système ci-dessous. 

### Pleins feux

L'application indexe jusqu'à **~1 000 œuvres** pour la recherche Spotlight du système. Touchez un résultat Spotlight pour ouvrir directement cette œuvre dans iSongCi.

### Siri & liens profonds

- Siri : *"Rechercher dans iSongCi"* (avec mot-clé)
- Lien profond : `isongci://search?q=明月`

### Conseils de recherche

| Astuce | Pourquoi |
|--------|---------|
| Rechercher auteur + mot-clé | Réduit les ensembles de résultats volumineux |
| Essayer le nom de la cipai | Trouve toutes les œuvres dans un même schéma musical |
| Utiliser une phrase célèbre | Déclenche le niveau texte intégral pour correspondance de ligne |
| Rechercher en chinois traditionnel | L'interface convertit ; le corpus correspond à la source simplifiée |

---

## Partie 8 — Thèmes & Apparence

Ouvrez **Réglages → Apparence**.

### Mode thème

| Mode | Comportement |
|------|-------------|
| **Clair** | Fond de lecture lumineux comme du papier |
| **Sombre** | Lecture nocturne sur fond sombre d'encre |
| **Système** | Suit l'apparence iOS / macOS |

### Couleur d'accent — 15 préréglages + personnalisé

Choisissez parmi **15 préréglages de thème** inspirés par l'esthétique de la dynastie Song :

| # | Préréglage | Humeur | 
|---|--------|------| 
| 1 | 水墨 Encre | Gris littéraire neutre | 
| 2 | 胭脂 Rouge | Accent cramoisi chaud | 
| 3 | 朱砂 Cinabre | Sceau classique-rouge | 
| 4 | 青瓷 Céladon | Glaçage vert frais | 
| 5 | Bois Pin | Vert forêt profonde | 
| 6 | Couleur Indigo | Bleu-noir du savant | 
| 7 | 群青 Azur | Bleu minéral brillant | 
| 8 | 青莲 Lotus | Fleur bleu-violet | 
| 9 | 琥珀 Ambre | Ton chaud doré | 
| 10 | 赭金 Ocre | Brun doré terreux | 
| 11 | 月白 Lune | Blanc argenté pâle | 
| 12 | 竹青 Bambou | Vert bambou frais | 
| 13 | 藕荷 Racine de Lotus | Rose tendre-lavande | 
| 14 | Couleur Ébène | Accent noir profond | 
| 15 | 缃色 Soie | Manuscrit vieilli jaune | 

Appuyez sur n'importe quel échantillon – bague sélectionnée + coche. Ou choisissez **Personnalisé** pour choisir n'importe quelle couleur dans le sélecteur de couleurs du système. 

La couleur d'accentuation s'applique aux : étoiles, boutons, surlignages favoris, accents de carte de partage et teinte du widget (lorsque **Suivez le thème de l'application** est activé). 

### Langue 

**Anglais / 简体中文 / 繁體中文** — L'interface utilisateur change instantanément. Le texte du corpus est stocké en chinois simplifié ; L'affichage traditionnel utilise la conversion sur l'appareil. 

### Synchronisation iCloud 

**Apparence** (clair/foncé/système), **préréglage d'accent** et **échelle de police** synchronisés via iCloud KVS en option. 

--- 

## Partie 9 — Widgets

### Ajouter un widget d'écran d'accueil 

1. Appuyez longuement sur l'écran d'accueil → **Modifier l'écran d'accueil** → appuyez sur **+** 
2. Recherchez **iSongCi** / **爱宋词** 
3. Choisissez un type et une taille de widget → **Ajouter un widget** 

### Types de widgets 

| Widget | Tailles | Comportement | 
|--------|-------|--------------| 
| **Ci quotidien** | Petit/Moyen/Grand + Écran de verrouillage | L'IC déterministe d'aujourd'hui ; le robinet ouvre le détail | 
| **Ci aléatoire** | Petit/Moyen/Grand + Écran de verrouillage | Choix de hasard ; actualise la chronologie | 
| **Ci préféré** | Petit/Moyen | Tourne à travers vos favoris | 
| **Série** | Petit / Circulaire (écran de verrouillage) | Nombre de séquences de lecture et icône de flamme | 

### Widgets d'écran de verrouillage 

Lors de l'ajout de widgets, passez à la page de personnalisation **Écran de verrouillage** et choisissez les accessoires iSongCi rectangulaires, circulaires ou en ligne. 

### Thème des widgets 

**Paramètres → Widgets → Suivre le thème de l'application** — les widgets correspondent à votre choix clair/sombre/accent. 

### Centre de contrôle (iOS 18+) 

Ajoutez des contrôles pour **Today's Ci**, **Serendipity** et **Recherche** depuis **Paramètres → Centre de contrôle** sur iOS 18 et versions ultérieures. 

### Widgets de dépannage

- Ouvrir l'application une fois après l'installation afin que le cache ci quotidien soit écrit dans le groupe App
- Si le texte semble incorrect après un changement de langue, ouvrir brièvement l'application — elle rafraîchit automatiquement les caches des widgets
- Mises à jour quotidiennes des widgets Ci à minuit local
- La chronologie aléatoire du widget Ci se rafraîchit périodiquement pour varier

### Guide des widgets dans l'application

**Paramètres → Widgets → Guide des widgets** ou `isongci://widget-guide` pour des captures d'écran et des conseils par widget. 

--- 

## Partie 10 — Siri, raccourcis et actions sur l'écran d'accueil

### Intentions Siri (3)

| Intention | Exemple de phrase |
|--------|----------------|
| **Le Ci d'aujourd'hui** | « Le ci d'aujourd'hui dans iSongCi » |
| **Sérendipité** | « Sérendipité dans iSongCi » |
| **Rechercher Ci** | « Rechercher dans iSongCi » (avec mot-clé) |

Ajoutez-les dans l'application **Raccourcis** pour les automatisations — par exemple, ouvrir `isongci://daily` chaque matin. 

### Actions rapides sur l'écran d'accueil (15 disponibles, maximum 4 activés)

Appuie longuement sur l'icône de l'application. Personnaliser dans **Paramètres → Raccourcis → Actions rapides de l'écran d'accueil** :

| # | Actions | Ouvre | 
|---|--------|-------| 
| 1 | Ci d'aujourd'hui | `isongci://daily` |
| 2 | Sérendipité | `isongci://random` |
| 3 | Continuer la lecture | `isongci://continue-reading` |
| 4 | Favoris | `isongci://favorites` |
| 5 | Rechercher | `isongci://search` |
| 6 | Parcourir | `isongci://category` |
| 7 | Accueil | `isongci://home` |
| 8 | Paramètres | `isongci://settings` |
| 9 | Guide d'utilisation | `isongci://usage-guide` |
| 10 | Guide des widgets | `isongci://widget-guide` |
| 11 | Guide des raccourcis | `isongci://shortcuts-guide` |
| 12 | Guide des fonctionnalités | `isongci://feature-guide` |
| 13 | Commentaires | `isongci://feedback` |
| 14 | Examen dans l'application | `isongci://in-app-review` |
| 15 | Paramètres des raccourcis d'accueil | `isongci://home-shortcuts` |

Seuls **4** apparaissent simultanément dans le menu d'icônes : choisissez les quatre les plus utilisés. 

### Liens profonds (`isongci://`) 

Référence complète : [Liens de raccourci] (../url-scheme). URL courantes : 

| URL | Ouvre | 
|-----|-------| 
| `isongci://poem?id=42` | Détail Ci par numéro de catalogue |
| `isongci://author?id=12` | Profil de l'auteur |
| `isongci://daily` | Ci d'aujourd'hui |
| `isongci://random` | Sérendipité |
| `isongci://continue-reading` | Continuer la lecture |
| `isongci://search?q=明月` | Rechercher 明月 |
| `isongci://favorites` | Onglet Favoris |

À utiliser dans les profils de configuration Raccourcis, Notes, Safari ou MDM. 

### Guide des raccourcis dans l'application

**Paramètres → Raccourcis → Guide des raccourcis** ou `isongci://shortcuts-guide` — boutons de copie en un clic pour chaque URL. 

--- 

## Partie 11 — Partager des cartes (13 styles) 

À partir du détail **Plus → Générer une carte de partage** : 

| Style | Humeur | 
|-------|------| 
| Classique | Mise en page littéraire épurée | 
| Encre | Esthétique du brossage et du lavage | 
| Minime | Axé sur la typographie | 
| verticale | Classique de haut en bas | 
| Cinabre | Accent rouge phoque | 
| Sombre | Fond d'encre de nuit | 
| Céladon | Vert céramique cool | 
| Ocre-or | Ton doré chaud | 
| Blanche-Neige | Papier brillant blanc | 
| Faire défiler | Motif de défilement horizontal | 
| Lune blanche | Palette pâle au clair de lune | 
| Ombre de bambou | Texture de bambou vert | 
| Papier Xuan | Fond texturé 宣纸 | 

### Options d'exportation 

- **Texte intégral** vs **extrait** — mémorisé pour la prochaine fois 
- **Résolution 3×** PNG — net sur les écrans Retina et les réseaux sociaux 
- **Exporter PNG** : enregistrez-le dans Photos ou partagez-le via n'importe quelle application. 
- Préférence de style enregistrée automatiquement 

Nécessite l'autorisation **Bibliothèque de photos (Ajouter)** uniquement lors de l'enregistrement dans Photos : accès en écriture seule, pas d'accès en lecture. 

--- 

## Partie 12 — Synchronisation iCloud 

Synchronisation facultative via **iCloud Key-Value Store** — pas de serveur iHTC Studio.

| Synchronisé | Non synchronisé | 
|--------|------------| 
| Favoris | Choix d'action rapide sur l'écran d'accueil | 
| Notes privées | Drapeaux d'intégration/guide de bienvenue | 
| Apparence (clair/foncé/système) | État de lecture aléatoire des widgets | 
| Couleur d'accentuation et échelle de police | Texte Ci (toujours dans l'ensemble d'applications) | 
| Visibilité de l'onglet Parcourir / Favoris | Rechercher dans le cache texte intégral | 
| Séquence de lecture | Teinte du sélecteur d'accent personnalisé (re-sélectionner sur le nouvel appareil) | 

Activez : **Paramètres → Données → iCloud Sync**. Nécessite une connexion iCloud sur l'appareil. **Le texte Ci n'est jamais téléchargé** — uniquement vos données personnelles et vos préférences. 

--- 

## Partie 13 — Notifications 

### Rappel Ci quotidien 

La **notification locale** facultative vous rappelle de lire le ci d'aujourd'hui. 

| Paramètre | Localisation | 
|---------|----------| 
| Activer/désactiver | **Paramètres → Notifications** | 
| Heure de rappel | Choisissez votre heure et minute préférée | 
| Autorisation | iOS demande lors de la première activation – aucun serveur impliqué | 

Les notifications sont **programmées entièrement sur l'appareil**. Pas de serveur push, pas de pixel de suivi, pas de charge utile distante. 

### Conseils

- Si les rappels s'arrêtent après une mise à jour iOS, ouvrez l'application une fois pour reprogrammer 
- La désactivation des notifications n'affecte pas la logique des séquences de lecture 
- Les séquences comptent lorsque vous ouvrez un détail de travail - la notification est un encouragement facultatif uniquement 

--- 

## Partie 14 — Paramètres et guides 

Ouvrez **Paramètres**. Sections, de haut en bas : 

### Apparence 

- **Thème** — Clair/Obscur/Système 
- **Couleur d'accent** — 15 préréglages + personnalisé (Partie 8) 
- **Langue** — Anglais / 简体中文 / 繁體中文 

### Lecture 

- **Curseur de taille de police** — Échelle continue de 50 % à 300 % (également dans le menu Plus détaillé) 
- **Lecture verticale** — bascule globale 
- **Pinyin** — activé par défaut 
- **Centrer le texte original** — activé par défaut 
- **Police calligraphique** — typographie immersive et détaillée 

### Données 

- **Série de lecture** – afficher les statistiques de la séquence 
- **iCloud Sync** — facultatif (partie 12) 
- **Exporter les favoris** — partager la collection sous forme de fichier 

### Barre d'onglets 

- Activer la visibilité de l'onglet **Parcourir** (activé par défaut) 
- Basculer la visibilité de l'onglet **Favoris** (activé par défaut) 

### Widgets 

- **Guide des widgets** — instructions par widget 
- Basculer **Suivez le thème de l'application** 

### Raccourcis 

- **Actions rapides sur l'écran d'accueil** : choisissez jusqu'à 4 sur 15 
- **Guide des raccourcis** — référence de lien profond avec boutons de copie

###Notifications 

- **Rappel Ci quotidien** — activation, heure, statut d'autorisation 

### Aide 

- **Guide d'utilisation** — visite guidée des fonctionnalités de relecture 
- **Guide des fonctionnalités** – cartes de fonctionnalités plus approfondies (`isongci://feature-guide`) 
- **Envoyer des commentaires** : ouvre l'e-mail (`isongci://feedback`) 

### À propos 

- Numéro de version 
- **Bocal de pourboires** — achat intégré en option `com.iHTCboy.iSongCi.6` (géré par Apple StoreKit) 
- Lien App Store 
- Replay bienvenue à l'intégration 

--- 

## Partie 15 — Obtenez l'application 

| Chaîne | Lien | 
|---------|------| 
| Magasin d'applications | [Télécharger sur l'App Store](https://apps.apple.com/app/id6788433450) | 

### Configuration système requise 

| Plateforme | Minimum | 
|--------------|---------| 
| iPhone/iPad | iOS 17.0+ (onglet Recherche : iOS 26.0+) | 
| Mac | macOS 13.0+ | 

### Contacter 

- **E-mail :** [AppleOSer@gmail.com](mailto:AppleOSer@gmail.com) — nous répondons généralement dans les 48 heures. 

### Pot de pourboire en option 

Si vous appréciez iSongCi, pensez au conseil facultatif via **Paramètres → À propos**. ID du produit : `com.iHTCboy.iSongCi.6`. Le paiement est entièrement traité par Apple. 

[FAQ](../faq) · [Liens de raccourci](../url-scheme) · [Politique de confidentialité](../privacy)

</section>
<section lang="tr" markdown="1">

### Uygulama tamamen çevrimdışı mı? 

Evet. **21.592 Song Ci çalışmasının** tümü paket halindedir. Uygulama yüklendikten sonra **sıfır giden ağ isteği** yapar; hesap yok, reklam yok, analiz yok. İsteğe bağlı iCloud, Apple'ın hizmetini yalnızca siz etkinleştirdiğinizde kullanır. 

### Bunun Tang şiiri / genel şiir uygulamalarından farkı nedir? 

iSongCi **Song Ci'ye (宋词) göre dikeydir** — karışık bir Tang/Song/Yuan şiir kataloğu değildir. **1.461 cipai** bilgisi, **sade çeviri ve modern yorum**, pinyin, günlük ci, paylaşım kartları, widget'lar, Kontrol Merkezi, Siri ve isteğe bağlı iCloud ile **sürükleyici dikey okuma** ekler. 

### Ne kadar içerik dahil ediliyor? 

| Ürün | Sayısı | 
|------|-------| 
| Ci işleri (toplam) | 21.592 | 
| Yazarlar | 1.509 | 
| Cipai (ayar kalıpları) | 1.461 | 
| Girişli öne çıkan cipai | 60 | 
| Düz çeviriler | 11.029 | 
| Modern yorum | Tüm işler | 
| Koleksiyonlar | 12 (Haofang 363 · Wanyue 520 · 10 tema seti) | 
| Hanedanlıklar | Beş Hanedan, Kuzey Şarkısı, Güney Şarkısı | 

### Düz çeviri, klasik notlar ve modern yorum nedir? 

Ayrıntı sayfasında üç ayrı katman; her bölüme bağımsız olarak geçiş yapın:

- **Düz çeviri (白话译文)** — tam metnin modern Çince çevirisi (~11.029 eser) 
- **Klasik notlar (注释)** — mevcut olduğu durumlarda geleneksel bilimsel ek açıklamalar 
- **Modern yorum (白话赏析)** — her çalışma için otomatik olarak oluşturulan arka plan, özet ve okuma ipuçları (akademik alıntı değil, referans amaçlı) 

### Tüm eserlerin çevirileri var mı? 

No. **11.029** eser tam düz tercümeyi içermektedir; geri kalanı orijinal metni ve modern yorumları gösterir. Klasik notlar yalnızca kaynak veriler bunları içerdiğinde görünür. Uygulama bir okuma ve keşif stüdyosudur, her ci'nin tam akademik baskısı değildir. 

### Bugünün Ci'si nasıl çalışıyor? 

**Takvim gününü tohum olarak** kullanarak **belirleyici bir şekilde öne çıkan havuzdan** (Haofang + Wanyue başyapıtları) bir parça seçilir — herkes **aynı tarihte aynı ci'yi görür**. **yerel gece yarısı** devreden çıkar. **Home** veya `isongci://daily` adresinden açın. 

### Serendipity nedir? 

**邂逅一词** öne çıkan havuzdan **rastgele** bir parça çeker - her dokunuşta farklı. **Home → Serendipity**, `isongci://random`, **Random Ci** widget'ını veya Siri'yi kullanın. 

### Pinyin ne kadar doğrudur?

Pinyin, segment başına **otomatik olarak oluşturulur**. Çoğu satırda işe yarar ancak **çok sesli karakterleri yanlış okuyabilir** (多音字). Bunu bir telaffuz otoritesi olarak değil, okumaya yardımcı olarak kullanın. 

### Geleneksel Çin ekranı mı? 

Kullanıcı arayüzünde özel **özellik** dizeleri vardır. Corpus metni basitleştirilmiş Çince olarak saklanır ve Geleneksel mod için **görüntüleme zamanında dönüştürülür** (karakter düzeyinde s2t tablosu) — veritabanının iki kopyasına ihtiyacınız yoktur. 

### Dikey okuma ve pinyin nasıl çalışır? 

**Ayarlar → Okuma** (dikey düzen, pinyin, kaligrafi yazı tipi) bölümünden genel olarak açın. Herhangi bir çalışma detayında, xuan kağıt arka planı ve bağımsız yazı tipi ölçeklendirmesi ile tam ekran dikey (sağdan sola) veya yatay sayfa için **Sürükleyici Okuma**'yı açabilirsiniz. 

### Sürükleyici Okuma Nedir? 

**Ayrıntı → Daha Fazla → Sürükleyici Okuma** krom içermeyen bir sayfa açar; iPad'de veya büyük ekranda kitap okumak veya sunum yapmak için idealdir. Okuyucunun içinde dikey/yatay ve kaligrafi arasında geçiş yapın. 

### Yazı tipi boyutunu nasıl değiştiririm? 

**Ayarlar → Okuma** kaydırma çubuğu veya **Ayrıntı → Diğer → Yazı tipi boyutu**. Gövde metnini sistem Dinamik Türünden bağımsız olarak ölçeklendirir; etkinleştirilirse iCloud aracılığıyla senkronize edilir. 

### Sesli okuma (TTS) nasıl çalışır?

Ayrıntı araç çubuğundaki **hoparlör** simgesine dokunun. Cihazdaki Mandarin konuşma sentezini kullanır. Aynı düğmeyle duraklatın ve devam ettirin. 

### Favoriler, notlar ve iCloud nasıl çalışır? 

**Favoriler** — herhangi bir çalışma üzerinde ♥'ya dokunun. **Özel notlar** — yalnızca sizin görebileceğiniz şiir başına ek açıklamalar (ayrıntı sayfası). İsteğe bağlı **iCloud Sync**, favorileri, notları, görünümü, yazı tipi ölçeğini, sekme görünürlüğünü ve okuma çizgisini cihazlar arasında yansıtır. **Ci metni hiçbir zaman yüklenmez**; her zaman uygulama paketinde kalır. 

### Okuma serisi kuralları nelerdir? 

Söz konusu takvim gününü saymak için uygulamada **herhangi bir ci**'yi açın. **Ardışık günler** serinizi artırır; **bir günden fazla atlarsanız** bir sonraki açılışta seri sıfırlanır. **Toplam okuma sayısı** ömür boyu açılan parçaları izler. Çizgi, Ana Sayfa'da ve **Okuma Çizgisi** widget'ında görünür. 

### Hangi paylaşım kartı stilleri mevcut? 

**13 stil:** Klasik, Mürekkep Yıkama, Zinciber Mühür, İpek Parşömen, Uzun Parşömen, Koyu Sarı Altın, Kış Kar, Yeşil Manzara, Bambu Slipler, Ayışığı Gümüş, Minimal, Koyu Minimal, Dikey Yazı. Tam metni veya alıntıyı seçin; isteğe bağlı olarak yorum ekleyin; PNG'yi 3× çözünürlükte dışa aktarın. 

### Hangi widget'lar mevcut?

| Widget | Amaç | 
|--------|---------| 
| Bugünün Ci | Bugünün öne çıkan parçası | 
| Mutluluk | Rastgele öne çıkan ci (saatte bir yenilenir) | 
| Favori Ci | En son yıldızlı çalışma | 
| Okuma Serisi | Ardışık günler + toplam okuma sayısı | 
| Kontrol Merkezi | Tek dokunuşla Bugünün Ci'sini açın (iOS 18+) | 

Boyutlar: Ana Ekranda Küçük / Orta / Büyük; Kilit Ekranı dairesel, satır içi veya dikdörtgen. **Bekleme**'yi destekler. Widget dili sistem dilini değil **uygulama içi dili** izler. 

### Widget yanlış veya boş metin mi gösteriyor? 

1. Uygulamayı yükledikten sonra bir kez açın 
2. Widget önbelleğini yeniden yazmak için Ana Sayfa'yı yenilemek için çekin 
3. Dili değiştirdikten sonra yenilemek için uygulamayı kısa süre açın 
4. **Favori Ci**'nin en az bir yıldızlı çalışmaya ihtiyacı var 
5. **Reading Streak** önce uygulamanın içinde bir çalışma açmanızı gerektirir 
6. Sistem ayarlarında iSongCi için widget'lara izin verildiğinden emin olun 

### Kontrol Merkezi widget'ı nedir (iOS 18+)? 

**Ayarlar → Kontrol Merkezi**'nden (veya sistem Kontrol Merkezi düzenleyicisinden) **Bugünün Ci**'sini ekleyin. **iOS 18.0+** gerektirir. Dokunduğunuzda uygulama doğrudan bugünün parçasına açılır. 

### Hangi Siri kısayolları mevcut? 

Uygulamayla birlikte üç Uygulama Amacı gelir:

| Niyet | Örnek ifade | 
|----------|----------------| 
| Bugünün Ci'sini Açın | "iSongCi'de bugünün ci'si" | 
| Rastgele Ci | "iSongCi'de Şans" | 
| Ci'de Ara | "iSongCi'de ara" (anahtar kelimeyle) | 

Ayarlar'da en fazla **4 Ana Ekran hızlı eylemini** yapılandırın. [Kısayol Bağlantıları](../url-scheme) içindeki tam derin bağlantı listesi. 

### Spotlight sınırlamaları nelerdir? 

Spotlight, **öne çıkan havuz artı favorilerinizi** — **~1.000** girişe kadar indeksler. Nadir eserler sistem aramasında görünmez; bunun yerine **uygulama içi derin tam metin aramasını** kullanın (tüm derlemeyi tembel olarak yükler). İlgili ci'yi doğrudan açmak için bir Spotlight sonucuna dokunun. 

### Sekmeleri gizleyebilir miyim? 

Evet. **Ayarlar → Sekme Çubuğu** — **Kategoriler** ve/veya **Favoriler** sekmeleri arasında geçiş yapın. Gizli sekmelere ayrıntılı işlemler, uzun basılan menüler, widget'lar ve `isongci://` bağlantıları yoluyla erişilebilir durumda kalır. 




|-----------|---------------|------------------| 
| Ana Ekran hızlı eylemler | ✅ | ❌ | 
| Widget'lar ve Kontrol Merkezi | ✅ (iOS 18+ CC) | Widget'lar öncelikli olarak iPhone/iPad'de | 
| Dokunsal geribildirim | ✅ | ❌ | 
| Özel Arama sekmesi | iOS 26+ | Düğme / sayfa aracılığıyla arama yapın | 
| Temel okuma, favoriler, iCloud | ✅ | ✅ | 

### Uygulama ücretsiz mi? Uç kavanozu nedir?

**Tamamen ücretsiz** — 21.592 eserin tümü ve her özellik, abonelik yok, reklam yok. **İsteğe bağlı bir ipucu kavanozu** (`com.iHTCboy.iSongCi.6`), Apple Uygulama İçi Satın Alma yoluyla geliştirmeyi desteklemenize olanak tanır; ekstra hiçbir şeyin kilidini açmaz. 

### Sistem gereksinimleri 

| Platformu | Asgari | 
|----------|---------| 
| iPhone / iPad | iOS 17.0+ | 
| Mac | macOS 13.0+ | 
| Kontrol Merkezi widget'ı | iOS 18.0+ | 
| Sistem çeviri paneli | iOS 17.4+ / macOS 14.4+ | 

### Uygulamayı nasıl edinebilirim? 

[App Store'dan indirin](https://apps.apple.com/app/id6788433450) (Uygulama Kimliği **6788433450**). 

### Destek ekibiyle nasıl iletişime geçebilirim? 

[AppleOSer@gmail.com](mailto:AppleOSer@gmail.com) — Genellikle 48 saat içinde yanıt veririz. 

--- 

### Sürekli okuma nasıl çalışır? 

Ayarlar → Okuma bölümünde **sürekli okumayı** etkinleştirin. Bir çalışma TTS'yi tamamladıktan sonra bir alt çubuk görünür; Birkaç saniye boyunca hiçbir şey yapmazsanız geçerli sıradaki bir sonraki öğe (gözatma / çalma listesi / favoriler / günlük) otomatik olarak başlar. Ayrıca paylaşım kartları oluştururken satırları da seçebilirsiniz. 

### Günlük hatırlatıcılar nasıl çalışır?

İsteğe bağlı **yerel bildirimler** size bugünün ci'sini okumanızı hatırlatır. Eşleşen çalışmayı derin bağlantı yoluyla açmak için bildirime dokunun. Bildirimleri devre dışı bırakmak okuma serinizi temizlemez. 

## Tam Kullanım Kılavuzu 

Aşağıdaki bölümler, daha önce destek sayfasında yer alan tam ürün açıklamasıdır. Hızlı Soru-Cevap öğeleri (varsa) yukarıda kalır. 

--- 

## Bölüm 1 — İlk Başlatma ve Arayüz 

### Hoş geldiniz kılavuzu 

İlk açılışta, **çok sayfalı bir karşılama kılavuzu** uygulamayı tanıtır: kitaplık ölçeği, günlük ci, sürükleyici okuma, favoriler, widget'lar ve gizlilik. Her sayfayı hızlıca kaydırın ve ardından **Başlayın**'a dokunun. İstediğiniz zaman tekrar oynatın: **Ayarlar → Yardım → Kullanım Kılavuzu** veya derin bağlantı `isongci://feature-guide`. 

### Sekme çubuğuna genel bakış 

| Sekme | Ne işe yarar | 
|-----|----------------| 
| **Ana sayfa** | Bugünün Ci, Serendipity, Okumaya Devam Et, okuma serisi, temalı önizlemeler | 
| **Gözat** | Yazarlar, cipai, hanedanlar, türler, tema koleksiyonları, tam katalog | 
| **Favoriler** | Yıldızlı liste/ızgara/kart düzenleri ve gruplamayla çalışır | 
| **Ayarlar** | Görünüm, okuma, veriler, sekmeler, widget'lar, kısayollar, yardım | 
| **Arama** | Anında meta veri arama + tembel tam metin derin arama (**iOS 26+**'da özel sekme) |

> **İpucu:** **Ayarlar → Sekme Çubuğu**'nda **Gözat** veya **Favoriler** sekmesini gizleyin. Bulunduğunuz sekmeyi kapatırsanız uygulama otomatik olarak Ana Sayfa'ya döner. Sekme görünürlüğü isteğe bağlı iCloud aracılığıyla senkronize edilir. 

### Platformlar 

| Platformu | Asgari | 
|----------|---------| 
| iPhone / iPad | iOS 17.0+ | 
| Mac | macOS 13.0+ | 

Özel **Arama sekmesi** **iOS 26+** gerektirir. Önceki iOS sürümlerinde arama, Gözat sayfasından veya Spotlight / Siri aracılığıyla yapılabilir. 

### Kurulum sırasında gizlilik 

- **Kayıt yok · reklam yok · analiz SDK'sı yok** 
- Corpus uygulama paketinin içinde gönderilir - CDN yok, telemetri yok 
- İsteğe bağlı iCloud yalnızca **özel iCloud'unuzu** kullanır; ci metni hiçbir zaman yüklenmez 

--- 

## Bölüm 2 — Ana Sayfa 

**Ana Sayfa** sekmesi günlük giriş noktanızdır; 21.592 eser arasında arama yapmadan seçilmiş keşifler sunar. 

### Bugünün Ci'si (每日一词) 

**Belirleyici bir günlük seçim** — aynı takvim tarihindeki herkes için aynı ci, tarihe dayalı bir algoritma tarafından tüm kitaplıktan seçilir. Tam ayrıntı sayfasını açmak için karta dokunun. 

- **yerel gece yarısı** otomatik olarak yenilenir 
- Uygulama başlatıldığında **Uygulama Grubu** depolama alanına yazılır, böylece **Daily Ci** widget'leri senkronize kalır 
- Derin bağlantı: `isongci://daily` 
- Siri: *"iSongCi'de bugünün ci'si"*

### Serendipity (邂逅一词) 

**Rastgele seçilmiş bir ci** için **Serendipity**'e dokunun; bugünün sabit seçimi yerine sürpriz yapmak istediğinizde harikadır. Her dokunuş, çevrimdışı kitaplıktan yeni bir parça çeker. 

- Derin bağlantı: `isongci://random` 
- Siri: *"iSongCi'de Şans"* 

### Okumaya Devam Et 

Yakın zamanda bir çalışma açtıysanız Ana Sayfada başlık ve yazarla birlikte **Okumaya Devam Et** görünür. Tek dokunuşla kaldığınız yerden devam edersiniz. 

- Derin bağlantı: `isongci://continue-reading` 
- Ana Ekran hızlı eylemi olarak da mevcuttur 

### Okuma serisi 

Ana Sayfa, **okuma serinizi** gösterir; art arda en az bir ci okuduğunuz günler ve kümülatif okuma sayısı. Herhangi bir çalışma detayının açılması bugünkü galibiyet serisine sayılır. 

- İsteğe bağlı **iCloud KVS** aracılığıyla senkronize edilir 
- **Çizgi** widget'ı Ana Ekranda ve Kilit Ekranında çizgi gösteriyor 

### Temalı önizlemeler 

Hızlı giriş kartları için aşağı kaydırın — **özellikli cipai**, **tema koleksiyonları**, **豪放 / 婉约** türleri ve **hanedan** öne çıkanları. Bu bölümde Gözat'a geçmek için **Tümünü Görüntüle**'ye dokunun. 

### Ana Ekrandaki hızlı işlemler

**Bugünün Ci**, **Serendipity**, **Okumaya Devam Et**, **Favoriler** ve **Ara** gibi kısayollar için uygulama simgesine uzun basın. **Ayarlar → Kısayollar → Ana Ekran Hızlı Eylemleri** bölümünde en fazla **4** öğeyi özelleştirin (15 eylem mevcuttur — bkz. Bölüm 10). 

--- 

## Bölüm 3 — Göz Atın 

**Gözat** sekmesini açın. Birden fazla bölüm, kitaplığı farklı açılardan keşfetmenize olanak tanır: 

### 1. Yazarlar (名家) 

**1.509 Song Ci şairi** biyografileriyle birlikte. Profili ve tam çalışma listesi için bir yazara dokunun. 

- Düzeni **⋯** aracılığıyla değiştirin: **Liste**, **Izgara** veya **Kartlar** 
- Izgara sütun sayısı (2-4) iPhone ve iPad'de ayrı ayrı hatırlanır 
- Derin bağlantı: `isongci://author?id=12` 

### 2. Cipai (词牌) 

**1.461 cipai** tam indeksteki ayar kalıpları. **60 öne çıkan cipai** biçimi, ritmi ve temsili ruh halini açıklayan giriş niteliğindeki makaleleri içerir; kalıbı öğrenin ve ardından o melodiye göre yazılmış eserlere göz atın. 

Örnekler: 水调歌头, 念奴娇, 满江红, 蝶恋花, 浣溪沙. 

### 3. Hanedanlıklar (朝代) 

Tarihsel döneme göre göz atın: 

| Hanedanı | Kapsam | 
|-----------|----------| 
| **İşte ** | Şarkıdan önceki erken *ci* geleneği | 
| **Çizim** | Kuzey Şarkısı ustaları | 
| **Bölüm** | Güney Şarkısı şarkı sözleri | 

### 4. Türler (流派)

| Tür | Sayısı | Karakter | 
|----------|-----------|-----------| 
| **tanıtım** | 363 | Cesur, geniş, kahramanca bir ton | 
| **Çizim** | 520 | Narin, lirik, samimi ton | 

Çalışmalar uygun olduğu durumlarda bir veya her iki grupta yer alabilir. 

### 5. Tema koleksiyonları (主题) 

**10 seçilmiş tema koleksiyonu** — aşk, ayrılık, nostalji, doğa, vatanseverlik, felsefe, festivaller ve daha fazlası. Her koleksiyon bir motifi paylaşan ci gruplarından oluşur. 

### 6. Tam katalog (全集) 

**21.592 iş** endeksinin tamamı. Sıralama ve filtreleme seçenekleriyle her şeyin kaydırılabilir tek bir listede olmasını istediğinizde kullanın. 

### Düzen ve bölüm seçenekleri 

Gözat veya Yazar sayfalarında **⋯** öğesine dokunun: 

| Seçenek | Ne işe yarar | 
|----------|----------------| 
| **Düzen** | Liste / Izgara / Kartlar | 
| **Bölüm görünürlüğü** | Herhangi bir göz atma bölümünü gösterin veya gizleyin | 
| **Bölüm sırası** | Bölümlerin görünme biçimini yeniden düzenleyin | 
| **Izgara sütunları** | iPhone'da 2–4, iPad'de 2–4 (ayrı olarak hatırlanır) | 

### Arama girişi (iOS 26 öncesi) 

iOS 17–25'te, Gözat'ın üst kısmındaki **arama alanından** veya Spotlight / Siri aracılığıyla aramayı açın. **iOS 26+**'da özel **Arama** sekmesini (Bölüm 7) kullanın. 

--- 

## Bölüm 4 — Ayrıntılı Okuma 

Temel okuma deneyimi olan **İş Ayrıntısı**'nı açmak için herhangi bir ci'ye dokunun.

### Araç Çubuğu (sağ üst) 

| Düğme | Eylem | 
|----------|------------| 
| **♥** | Favorilere ekle veya favorilerden kaldır (yıldızla işaretlendiğinde vurgu renginizi kullanır) | 
| **Hoparlör** | **TTS sesli okumayı** başlatın; duraklatmak / devam ettirmek için tekrar dokunun | 
| **⋯ Daha Fazla** | Eylem menüsünü açar (aşağıya bakın) | 

### İçerik bölümleri 

Her işin her katmanı yoktur. Bölümler yalnızca içerik mevcut olduğunda görünür: 

| Bölüm | Kapsam | Ne görüyorsun | 
|-----------|----------|----------------| 
| **Orijinal metin** | 21.592'nin tamamı | İsteğe bağlı pinyin ile tam ci | 
| **Klasik notlar** | Mevcut olduğu yerde | Geleneksel bilimsel açıklamalar | 
| **Düz çeviri** | **11.029 çalışma** | Modern yerel anlatım | 
| **Modern yorum** | Seçilmiş alt küme | Takdir ve edebi bağlam | 
| **Cipai'ye giriş** | Öne çıkan ve bağlantılı cipai | Ayar modeli açıklaması | 
| **Yazar biyografisi** | 1.509 yazar | Şair biyografisi | 
| **İlgili çalışmalar** | Akıllı bağlantılar | Aynı yazar, cipai veya tema | 

Okurken her bölümü açın veya kapatın. **Özel notlar** altta görünür; kişisel notlarınız yalnızca sizin tarafınızdan görülebilir (etkinleştirildiğinde iCloud aracılığıyla senkronize edilir). 

### Diğer menü (⋯)

| Ürün | Ne işe yarar | 
|----------------||-----| 
| **Yazı tipi boyutu** | Ölçeklendirme panelini açar (%50–%300, varsayılan taban 22 punto) | 
| **Sürükleyici okuma** | Tam ekran, dikkat dağıtıcı olmayan görünüm (Bölüm 5) | 
| **Pinyin** | Küresel pinyin ayarının iş başına geçersiz kılınması | 
| **Dikey düzen** | Okuma yönünün iş başına geçersiz kılınması | 
| **Tam metni kopyala** | Ci'nin tamamını panoya kopyalar | 
| **Metni paylaş** | Düz metinli sistem paylaşım sayfası | 
| **Paylaşım kartı oluştur** | 13 tarzı resim kartı düzenleyicisini açar (Bölüm 11) | 
| **Özel not** | Bu çalışma için kişisel notunuzu ekleyin veya düzenleyin | 

### Okuma seçenekleri 

- **Pinyin** — Ayarlar'da genel varsayılan; ayrıntılı olarak iş başına geçersiz kılma 
- **Dikey düzen** — klasik yukarıdan aşağıya okuma; iş başına geçersiz kılma 
- **Orijinal metni ortala** — varsayılan olarak açıktır; ana metin bloğunu hizalar 
- **Sistem çevirisi** (iOS 17.4+) — Seçilen metin için Apple'ın çeviri paneli 
- **Bölüm geçişleri** — Çeviriyi, Notları, Yorumu, Cipai girişini, Yazar biyografisini göster/gizle 

### TTS sesli okuma 

Cihazdaki metinden konuşmaya geçiş için **hoparlör** simgesine dokunun. Sistem seslerini kullanır; ağ yoktur. Pinyin'in görünür olmasıyla işe giderken veya telaffuz çalışırken dinlemek için idealdir.

### Liste satırlarına uzun basın 

Herhangi bir çalışma listesinde, hızlı işlemler için bir satıra **uzun basın**: **Favorilere ekle**, **Yüksek sesle oku**, **Paylaş** veya **Geçmişten kaldır** (geçmiş görünümlerinde). 

### Derin bağlantı 

Belirli bir çalışmayı katalog kimliğine göre açın: `isongci://poem?id=42` 

--- 

## Bölüm 5 — Sürükleyici Okuma 

Ayrıntıdan **Diğer → Sürükleyici Okuma**, okuma, sunum ve odaklanmış çalışma için tasarlanmış temiz, tam ekran bir sayfaya girin. 

### Düzen 

- **Dikey** — klasik kaydırma tarzı yukarıdan aşağıya akış (sürükleyici için varsayılan) 
- **Yatay** — modern soldan sağa akış 
- Sürükleyici modda istediğiniz zaman geçiş yapın; tercih genel Ayarları takip edebilir 

### Tipografi ve atmosfer 

- Ana metin için **Kaligrafiden ilham alan yazı tipi** — fırçayla yazılmış Song Ci'yi çağrıştırıyor 
- **Xuan kağıdı (宣纸) arka planı** — sıcak, dokulu edebi his 
- **açık / koyu / sistem** temanıza ve **vurgu renginize** uyum sağlar 

### Kontroller 

- **Yazı tipi ölçeği** kontrolünü sıkıştırın veya kullanın (%50–%300) 
- Kromu göstermek/gizlemek için dokunun (araç çubuğu, bölüm geçişleri) 
- **TTS** sürükleyici moddan çıkmadan kullanılabilir 
- Geçerli liste bağlamında **önceki / sonraki** çalışmaya gitmek için kaydırın veya okları kullanın 

### Şunun için en iyisi

- iPad sunumu veya masa başında okuma 
- Ezberleme ve okuma uygulaması 
- Ekran görüntüleri ve paylaşım kartı hazırlığı 

--- 

## Bölüm 6 — Favoriler 

### Başrol oyunculuğu çalışmaları 

Herhangi bir iş detayına **♥** dokunun veya bir liste satırına uzun basın → **Favori**. Favorilere eklenen satırlar, yıldız için **vurgu renginizi** kullanır. 

### Favoriler sekmesi düzenleri 

**Favoriler** sekmesini açın. Geçiş yapmak için **⋯**'e dokunun: 

| Düzen | Şunun için en iyisi | 
|----------|----------| 
| **Liste** | Başlık, yazar, cipai ile yoğun tarama | 
| **ızgara** | Ayarlanabilir sütunlarla görsel tarama | 
| **Kartlar** | Alıntı içeren büyük önizleme kartları | 

### Gruplandırma 

Koleksiyonunuzu şu şekilde düzenleyin: 

| Gruplama kriteri | Davranış | 
|----------|----------| 
| **Yazar** | Her şairin altında kümeler çalışır | 
| **Hanedan** | Birleşme / Birleşme / Birleşme bölümleri | 
| **Çipai** | Melodi modeline göre gruplar | 

### Toplu düzenleme 

Favoriler sayfasında **Düzenle**'ye dokunun: 

- **Çoklu seçim** onay işaretleriyle çalışır 
- **Tümünü seç / Tüm seçimleri kaldır** 
- **Favorilerden toplu kaldırma** (onay ile) 

Hızlı bir **Kaldır** işlemi için arka arkaya sola kaydırın. 

### Favori Ci widget'ı 

**Favori Ci** ana ekran widget'ı, kendi koleksiyonunuzdan günlük olarak kişisel olarak seçtiğiniz, yıldızlı çalışmalarınızı dönüşümlü olarak görüntüler. 

### İhracat

**Ayarlar → Veri → Favorileri dışa aktar** — koleksiyonunuzu yedekleme veya taşıma için dosya olarak paylaşın. 

--- 

## Bölüm 7 — Arama 

iOS'ta, pinyin yazmak yerine karakter çizmeyi tercih ettiğinizde Ana Sayfa aramasının yanındaki kontrolden **el yazısı şarkı sözü aramasını** açın. 

iSongCi **iki katmanlı çevrimdışı arama** sunar; önce hızlı meta veriler, gerektiğinde derin tam metin. 

### Tier 1 — Anında meta veri araması 

Siz yazarken uygulama, paketlenmiş meta verilerle anında eşleşir: 

- **Başlıklar** (ci adları) 
- **Yazar adları** 
- **Cipai isimleri** 
- **Etiketler ve kategoriler** 

Yükleme döndürücü yok; sonuçlar her tuş vuruşunda görünür. 

### Tier 2 — Tembel tam metin derin arama 

Ci gövdeleri içindeki satır düzeyindeki eşleşmeler için uygulama, ilk derin arama kullanımında paketten **_`fulltext.json`_** tembel bir şekilde yüklenir. Tek seferlik yüklemeden sonra, tam metin araması tamamen cihaz üzerinde çalışır. 

- 21.592 eserlik derlemedeki **herhangi bir satırla** eşleşir 
- Derin aramanın ilk başlatılmasında biraz daha yavaş; bundan sonra önbelleğe alındı 
- **Sıfır ağ** — dosya uygulamayla birlikte gönderilir 

### Özel Arama sekmesi (iOS 26+) 

**iOS 26 ve sonraki sürümlerde** Arama'nın sekme çubuğunda kendi sekmesi vardır. Önceki sürümlerde, **Gözat** bölümündeki arama alanını veya aşağıdaki sistem entegrasyonlarını kullanın. 

### Gündem

Uygulama, sistem Spotlight araması için **~1.000 eseri** indeksler. Bir Spotlight sonucuna dokunarak o eseri doğrudan iSongCi'de açabilirsiniz.

### Siri ve derin bağlantılar

- Siri: *"iSongCi'de ara"* (anahtar kelime ile)
- Derin bağlantı: `isongci://search?q=明月`

### Arama ipuçları

| İpucu | Neden |
|-------|------|
| Yazar + anahtar kelime ile ara | Büyük sonuç kümelerini daraltır |
| Cipai ismini dene | Bir melodi kalıbındaki tüm eserleri bulur |
| Ünlü bir satırı kullan | Satır eşleşmesi için tam metin katmanını tetikler |
| Geleneksel Çince ile ara | Arayüz dönüştürür; korpus basitleştirilmiş kaynağa uyar |

---

## Bölüm 8 — Temalar ve Görünüm

**Ayarlar → Görünüm**'ü açın.

### Tema modu

| Mod | Davranış |
|-----|----------|
| **Açık** | Kağıt parlaklığında okuma arka planı |
| **Koyu** | Mürekkep koyuluğunda gece okuması |
| **Sistem** | iOS / macOS görünümünü takip eder |

### Vurgu rengi — 15 ön ayar + özel

Song Hanedanlığı estetiğinden ilham alan **15 tema ön ayarından** seçim yapabilirsiniz:

| # | Ön Ayar | Ruh Hali | 
|---|--------|------| 
| 1 | Renk Mürekkep | Nötr edebi gri | 
| 2 | Rouge | Sıcak kızıl vurgu | 
| 3 | Cinnabar | Klasik mühür kırmızısı | 
| 4 | Seladonlar | Soğuk yeşil sır | 
| 5 | Çam Çamı | Derin orman yeşili | 
| 6 | Indigo | Scholar'ın mavi-siyah | 
| 7 | Azure | Parlak mineral mavisi | 
| 8 | Lotus | Mor-mavi çiçeği | 
| 9 | Amber | Altın sıcak tonu | 
| 10 | 赭金 Toprak boyası | Dünyevi altın-kahverengi | 
| 11 | Ay | Soluk gümüş-beyaz | 
| 12 | Bambu | Taze bambu yeşili | 
| 13 | Lotus kökü | Yumuşak pembe-lavanta | 
| 14 | Fotoğraf Ebony | Derin siyah vurgu | 
| 15 | Çin İpek | Eski el yazması sarı | 

Herhangi bir renk örneğine dokunun — seçili halka + onay işareti. Veya sistem renk seçicisinden herhangi bir rengi seçmek için **Özel**'i seçin. 

Vurgu rengi şunlar için geçerlidir: favori yıldızlar, düğmeler, vurgular, paylaşım kartı vurguları ve widget renk tonu (**Uygulama temasını takip et** açık olduğunda). 

### Dil 

**İngilizce / 简体中文 / 繁體中文** — Kullanıcı arayüzü anında değişir. Corpus metni basitleştirilmiş Çince olarak saklanır; Geleneksel ekran, cihaz içi dönüştürmeyi kullanır. 

### iCloud senkronizasyonu 

İsteğe bağlı iCloud KVS aracılığıyla **görünüm** (açık/koyu/sistem), **vurgu ön ayarı** ve **yazı tipi ölçeği** senkronizasyonu. 

--- 

## Bölüm 9 — Widget'lar

### Ana Ekran widget'ı ekleyin 

1. Ana Ekrana uzun basın → **Ana Ekranı Düzenle** → **+** öğesine dokunun 
2. **iSongCi** / **iSongCi**'yi arayın 
3. Bir widget türü ve boyutu seçin → **Widget Ekle** 

### Widget türleri 

| Widget | Boyutlar | Davranış | 
|----------|----------|----------| 
| **Günlük Ci** | Küçük / Orta / Büyük + Kilit Ekranı | Günümüzün deterministik ci'si; musluk detayı açar | 
| **Rastgele Ci** | Küçük / Orta / Büyük + Kilit Ekranı | Serendipity seçimi; zaman çizelgesinde yenilenir | 
| **Favori Ci** | Küçük / Orta | Favorileriniz arasında geçiş yapar | 
| **Çizgi** | Küçük / Dairesel (Kilit Ekranı) | Çizgi sayısı ve alev simgesi okunuyor | 

### Kilit Ekranı widget'ları 

Widget'lar eklerken **Kilit Ekranı** özelleştirme sayfasına geçin ve iSongCi dikdörtgen, dairesel veya satır içi aksesuarları seçin. 

### Widget teması 

**Ayarlar → Widget'lar → Uygulama temasını takip et** — widget'lar açık/koyu/vurgu seçiminize uygundur. 

### Kontrol Merkezi (iOS 18+) 

iOS 18 ve sonraki sürümlerde **Ayarlar → Kontrol Merkezi**'nden **Bugünün Ci**, **Serendipity** ve **Arama** için kontroller ekleyin. 

### Widget'larda sorun giderme

- Uygulamayı kurulumdan sonra bir kez açın, böylece günlük ci önbelleği Uygulama Grubuna yazılır
- Dil değişikliğinden sonra metin yanlış görünüyorsa, uygulamayı kısa süreliğine açın — widget önbellekleri otomatik olarak yenilenir
- Günlük Ci widget'ı yerel gece yarısında güncellenir
- Rastgele Ci widget zaman çizelgesi, çeşitlilik sağlamak için periyodik olarak yenilenir

### Uygulamadaki Widget rehberi

**Ayarlar → Widget'lar → Widget Rehberi** veya `isongci://widget-guide` ile her widget için ekran görüntüleri ve ipuçları.

---

## Bölüm 10 — Siri, Kestirmeler ve Ana Ekran İşlemleri

### Siri niyetleri (3)

| Niyet | Örnek ifade |
|--------|----------------|
| **Bugünün Ci'si** | "Bugünün ci'si iSongCi'de" |
| **Serendipity** | "Serendipity iSongCi'de" |
| **Ci Ara** | "iSongCi'de Ara" (anahtar kelime ile) |

Bunları otomasyonlar için **Kestirmeler** uygulamasına ekleyin — ör. `isongci://daily`'i her sabah açtırmak.

### Ana Ekran hızlı işlemleri (15 mevcut, en fazla 4 etkin)

Uygulama simgesine uzun basın. **Ayarlar → Kestirmeler → Ana Ekran Hızlı İşlemleri** bölümünden özelleştirin:

| # | Eylem | Açılıyor | 
|---|--------|-------| 
| 1 | Bugünün Ci | `isongci://daily` |
| 2 | Mutluluk | `isongci://random` |
| 3 | Okumaya Devam Et | `isongci://continue-reading` |
| 4 | Favoriler | `isongci://favorites` |
| 5 | Ara | `isongci://search` |
| 6 | Gözat | `isongci://category` |
| 7 | Ana Sayfa | `isongci://home` |
| 8 | Ayarlar | `isongci://settings` |
| 9 | Kullanım Kılavuzu | `isongci://usage-guide` |
| 10 | Widget Kılavuzu | `isongci://widget-guide` |
| 11 | Kısayol Kılavuzu | `isongci://shortcuts-guide` |
| 12 | Özellik Kılavuzu | `isongci://feature-guide` |
| 13 | Geribildirim | `isongci://feedback` |
| 14 | Uygulama İçi İnceleme | `isongci://in-app-review` |
| 15 | Ana Sayfa Kısayolları Ayarları | `isongci://home-shortcuts` |

Simge menüsünde aynı anda yalnızca **4** görünüyor; en çok kullandığınız dördünü seçin. 

### Derin bağlantılar (`isongci://`) 

Tam referans: [Kısayol Bağlantıları](../url-scheme). Ortak URL'ler: 

| URL'si | Açılıyor | 
|-----|----------| 
| `isongci://poem?id=42` | Katalog kimliğine göre Ci ayrıntıları |
| `isongci://author?id=12` | Yazar profili |
| `isongci://daily` | Bugünün Ci |
| `isongci://random` | Mutluluk |
| `isongci://continue-reading` | Okumaya Devam Et |
| `isongci://search?q=明月` | 明月'ı arayın |
| `isongci://favorites` | Favoriler sekmesi |

Kısayollar, Notlar, Safari veya MDM yapılandırma profillerinde kullanın. 

### Uygulamadaki kısayol kılavuzu

**Ayarlar → Kısayollar → Kısayol Kılavuzu** veya `isongci://shortcuts-guide` — her URL için tek dokunuşla kopyalama düğmeleri. 

--- 

## Bölüm 11 — Paylaşım Kartları (13 Stil) 

Detaydan **Daha fazla → Paylaşım kartı oluştur**: 

| Stil | Ruh Hali | 
|----------|------| 
| Klasik | Temiz edebi düzen | 
| Mürekkep | Fırçala ve yıka estetiği | 
| Asgari | Tipografi odaklı | 
| Dikey | Klasik yukarıdan aşağıya | 
| Zincifre | Mühür kırmızısı vurgulu | 
| Koyu | Gece mürekkebi arka planı | 
| Seladonlar | Serin seramik yeşili | 
| Koyu sarı altın | Sıcak altın tonu | 
| Kar beyazı | Parlak kağıt beyazı | 
| Kaydır | Yatay kaydırma motifi | 
| Ay beyazı | Soluk mehtaplı palet | 
| Bambu gölgesi | Yeşil bambu doku | 
| Xuan kağıdı | Dokulu arka plan | 

### Dışa aktarma seçenekleri 

- **Tam metin** ve **alıntı** — bir dahaki sefere hatırlanır 
- **3× çözünürlük** PNG — Retina ekranlarda ve sosyal medyada net 
- **PNG'yi dışa aktar** — Fotoğraflar'a kaydedin veya herhangi bir uygulama aracılığıyla paylaşın 
- Stil tercihi otomatik olarak kaydedilir 

Yalnızca Fotoğraflar'a kaydederken **Fotoğraf Kitaplığı (Ekle)** izni gerektirir; salt yazılır, okuma erişimi yoktur. 

--- 

## Bölüm 12 — iCloud Senkronizasyonu 

**iCloud Anahtar-Değer Deposu** aracılığıyla isteğe bağlı senkronizasyon — iHTC Studio sunucusu yok.

| Senkronize | Senkronize edilmedi | 
|----------|----------------| 
| Favoriler | Ana Ekran hızlı eylem seçenekleri | 
| Özel notlar | İlk katılım / karşılama kılavuzu bayrakları | 
| Görünüm (açık/karanlık/sistem) | Widget karıştırma durumu | 
| Vurgu rengi ve yazı tipi ölçeği | Ci metni (her zaman uygulama paketinde) | 
| Gözat / Favoriler sekmesinin görünürlüğü | Tam metin önbelleğinde ara | 
| Okuma serisi | Özel vurgu seçici renk tonu (yeni cihazda yeniden seçin) | 

Şunu açın: **Ayarlar → Veri → iCloud Senkronizasyonu**. Cihazda iCloud ile oturum açmayı gerektirir. **Ci metni hiçbir zaman yüklenmez**; yalnızca kişisel verileriniz ve tercihleriniz. 

--- 

## Bölüm 13 — Bildirimler 

### Günlük Ci hatırlatıcısı 

İsteğe bağlı **yerel bildirim** size bugünün ci'sini okumanızı hatırlatır. 

| Ayar | Konum | 
|-----------|----------| 
| Etkinleştir / devre dışı bırak | **Ayarlar → Bildirimler** | 
| Hatırlatma zamanı | Tercih ettiğiniz saat ve dakikayı seçin | 
| İzin | iOS ilk etkinleştirmede sorar; sunucu dahil değildir | 

Bildirimler **tamamen cihaz üzerinde planlanmıştır**. Push sunucusu yok, izleme pikseli yok, uzak yük yok. 

### İpuçları

- Bir iOS güncellemesinden sonra hatırlatıcılar durursa yeniden planlamak için uygulamayı bir kez açın 
- Bildirimlerin devre dışı bırakılması okuma çizgisi mantığını etkilemez 
- Herhangi bir iş ayrıntısını açtığınızda seri sayılır; bildirim yalnızca isteğe bağlı teşviktir 

--- 

## Bölüm 14 — Ayarlar ve Kılavuzlar 

**Ayarlar**'ı açın. Bölümler, yukarıdan aşağıya: 

### Görünüm 

- **Tema** — Açık / Koyu / Sistem 
- **Vurgu rengi** — 15 ön ayar + özel (Bölüm 8) 
- **Dil** — İngilizce / 简体中文 / 繁體中文 

### Okuma 

- **Yazı tipi boyutu kaydırıcısı** — %50–%300 sürekli ölçek (aynı zamanda ayrıntılı olarak Diğer menüsü) 
- **Dikey okuma** — genel geçiş 
- **Pinyin** — varsayılan olarak açıktır 
- **Orijinal metni ortala** — varsayılan olarak açıktır 
- **Kaligrafi yazı tipi** — sürükleyici ve ayrıntılı tipografi 

### Veri 

- **Okuma serisi** — seri istatistiklerini görüntüleyin 
- **iCloud Sync** — isteğe bağlı (Bölüm 12) 
- **Favorileri dışa aktar** — koleksiyonu dosya olarak paylaşın 

### Sekme Çubuğu 

- **Gözat** sekmesinin görünürlüğünü açın/kapatın (varsayılan olarak açık) 
- **Favoriler** sekmesinin görünürlüğünü açın/kapatın (varsayılan olarak açıktır) 

### Widget'lar 

- **Widget Kılavuzu** — widget başına talimatlar 
- **Uygulama temasını takip et** geçişi 

### Kısayollar 

- **Ana Ekran Hızlı Eylemleri** — 15'ten 4'e kadar seçim yapın 
- **Kısayol Kılavuzu** — kopyalama düğmeleriyle derin bağlantı referansı

### Bildirimler 

- **Günlük Ci hatırlatıcısı** — etkinleştirme, zaman, izin durumu 

### Yardım 

- **Kullanım Kılavuzu** — tekrar oynatma özelliği turu 
- **Özellik Kılavuzu** — daha ayrıntılı özellik kartları (`isongci://feature-guide`) 
- **Geri Bildirim Gönder** — e-postayı açar (`isongci://feedback`) 

### Hakkında 

- Sürüm numarası 
- **İpucu kavanozu** — isteğe bağlı uygulama içi satın alma `com.iHTCboy.iSongCi.6` (Apple StoreKit tarafından yönetilir) 
- App Store bağlantısı 
- Hoş geldiniz ilk katılım işlemini tekrar oynatın 

--- 

## Bölüm 15 — Uygulamayı İndirin 

| Kanal | Bağlantı | 
|-----------|------| 
| Uygulama Mağazası | [App Store'dan İndirin](https://apps.apple.com/app/id6788433450) | 

### Sistem gereksinimleri 

| Platformu | Asgari | 
|----------|---------| 
| iPhone / iPad | iOS 17.0+ (Arama sekmesi: iOS 26.0+) | 
| Mac | macOS 13.0+ | 

### İletişim 

- **E-posta:** [AppleOSer@gmail.com](mailto:AppleOSer@gmail.com) — Genellikle 48 saat içinde yanıt veririz. 

### İsteğe bağlı uç kavanozu 

iSongCi'den hoşlanıyorsanız **Ayarlar → Hakkında** aracılığıyla isteğe bağlı ipucunu değerlendirebilirsiniz. Ürün Kimliği: `com.iHTCboy.iSongCi.6`. Ödeme tamamen Apple tarafından işlenir. 

[SSS](../faq) · [Kısayol Bağlantıları](../url-scheme) · [Gizlilik Politikası](../privacy)

</section>
