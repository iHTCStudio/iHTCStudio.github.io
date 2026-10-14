# iHTC Studio — iHTCTeam.github.io

Marketing & support site for **iHTC Studio** (爱火腿肠工作室) — built with **Jekyll**, with a fully custom Apple-inspired theme.

> 🌐 **Live:** <https://ihtcteam.github.io>

## Features

- ✨ **Apple-style design system** — minimalist, frosted-glass surfaces, gradient accents, fluid type scale.
- 🌗 **Dark / Light / Auto theme** with `prefers-color-scheme` and a manual toggle.
- 🌐 **Three-language UI** (English · 简体中文 · 繁體中文) — auto-detected from the browser, manually switchable, persisted to `localStorage`.
- 🧭 **Smart navigation** — root site shows all apps; each app sub-page shows only its own sections, plus a floating right-rail to switch to other apps.
- 📱 **Fully responsive**, mobile-first, with a glass mobile drawer.
- ⚡ **Fast** — system fonts, inline critical theme/lang script (no FOUC), zero runtime JS dependencies, ~5 KB compressed JS.
- ♿ **Accessible** — semantic HTML, ARIA, focus rings, skip-link, `prefers-reduced-motion` support.
- 🔍 **SEO-ready** — `jekyll-seo-tag` + `jekyll-sitemap`, semantic OG/Twitter meta, canonical URLs.

## Apps

| Directory | Display Name | Pages |
|-----------|-------------|-------|
| iConnect/ | iConnect | index, faq, privacy, url-scheme |
| iConverter/ | iConverter | index, faq, privacy, url-scheme |
| iLinux/ | iLinux | index, faq, privacy, url-scheme |
| iWool/ | iWool | index, faq, privacy |
| iPomodoros/ | iPomodoro | index, faq, privacy, url-scheme |
| iCalendar/ | iCalendar | index, faq, privacy |
| iEnglish/ | iEnglish | index, faq, privacy |
| iLeetCoder/ | iCoder | index, faq, privacy |
| iTer/ | iTer | index, faq, privacy |
| iWuBi/ | iWuBi | index, faq, privacy |
| iCangJie/ | iCangJie | index, faq, privacy, url-scheme |
| TwinPolarCam/ | TwinPolarCam | index, faq, privacy |
| iPhoto/ | iPhoto / 爱修图 | index, faq, privacy, url-scheme |
| Weber/ | Weber | index, faq, privacy |
| iVideo/ | iVideo | index, faq, privacy |
| iApp/ | iApp | index, faq, privacy, url-scheme |
| iDictionary/ | iDictionary | index, faq, privacy, url-scheme |
| iNutrition/ | iNutrition | index, faq, privacy, url-scheme |
| iTangPoems/ | iTangPoems | index, faq, privacy, url-scheme |
| iStore/ | iStore | index, faq, privacy, url-scheme |
| iWord/ | iWord | index, faq, privacy, url-scheme |
| iRootWord/ | iRootWord | index, faq, privacy, url-scheme |
| GLUT/ | GLUT Campus / 桂林理工大学校园通 | index, faq, privacy |
| iCouplet/ | iCouplet / 爱对联 | index, faq, privacy, url-scheme |

## Project Structure

```
.
├── _config.yml              Jekyll site config (no minima theme)
├── _data/
│   ├── i18n.yml             UI strings in en / zh-CN / zh-TW
│   └── apps.yml             App metadata (name, accent, icon, display_name, blurbs…)
├── _layouts/
│   ├── default.html         Base layout (head, header, footer, app-switcher)
│   ├── home.html            Hero homepage
│   ├── app.html             App landing pages (per app)
│   └── doc.html             FAQ / Privacy / URL Scheme docs
├── _includes/
│   ├── head.html            Meta + favicon + critical script
│   ├── header.html          Top nav (smart per current section)
│   ├── footer.html
│   ├── language-switcher.html
│   ├── theme-switcher.html
│   ├── app-switcher.html    Floating right-rail
│   ├── app-icon.html        App Store icon + SVG fallback
│   ├── app-icon-svg.html    SVG fallback shapes
│   └── icons.html           Generic UI SVG icons
├── _sass/                   Modular SCSS partials (variables, typography…)
├── assets/
│   ├── css/main.scss        SCSS entry (compiled by Jekyll)
│   └── js/main.js           Theme + lang + reveal + drawer
├── index.html               Hero homepage
├── 404.html
├── robots.txt
└── <AppId>/                 Per-app support pages
    ├── index.md             Overview (uses `app` layout)
    ├── faq.md               FAQ (uses `doc` layout)
    ├── privacy.md           Privacy policy
    └── url-scheme.md        URL Scheme reference (optional)
```

## Multi-language Authoring

Content blocks are wrapped in `<section lang="…" markdown="1">` tags. The CSS in `_sass/_i18n.scss` shows only the section that matches `<html lang="…">`, which is set client-side by `assets/js/main.js`.

```html
<section lang="en" markdown="1">
# Hello world
</section>
<section lang="zh-CN" markdown="1">
# 你好，世界
</section>
<section lang="zh-TW" markdown="1">
# 你好，世界
</section>
```

For inline content (e.g. inside an `<a>` or `<span>`), use the `inline` class:

```html
<span lang="en" class="inline">Settings</span>
<span lang="zh-CN" class="inline">设置</span>
<span lang="zh-TW" class="inline">設定</span>
```

UI strings (header, footer, hero, etc.) live in `_data/i18n.yml`. App metadata (icons, accent colors, blurbs) lives in `_data/apps.yml`.

## Adding a new app

1. Add a new entry to `_data/apps.yml` (set `id`, `slug`, `accent`, `icon`, `apple_id`, multi-lang `names`, `taglines`, `blurbs`, `highlights`; optionally set `display_name` if the display name differs from `id`).
2. Run `python3 scripts/sync_app_icons.py` to pull the App Store artwork URL into `_data/app_icons.yml`.
3. Optionally add a custom SVG fallback shape in `_includes/app-icon-svg.html` (used only when artwork fails to load).
4. Create a new directory `<AppId>/` with `index.md`, `faq.md`, `privacy.md`. Set `app_id: <AppId>` in front-matter.
5. The header nav, footer, app cards, and floating switcher all auto-update.

## Local Development

```bash
bundle install
bundle exec jekyll serve --livereload
# open http://localhost:4000
```

## License

Content © iHTC Studio. All rights reserved.
