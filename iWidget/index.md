---
layout: app
title: iWidget — Support
app_id: iWidget
description: iWidget (爱组件) — widget designer for iPhone, iPad & Mac. 54 preset sets, block editor, lunar calendar, weather, countdowns, wallpaper tint & tap shield. Offline-first, optional iCloud.
---

<section lang="en" markdown="1">

**Tint your wallpaper. Build the widget you actually want.**

**iWidget** (爱组件 / 愛組件) is a **widget design studio** for **iPhone, iPad, and Mac** — not another calendar app. Calendar, weather, countdowns, and device stats are **data blocks** you arrange on a grid: **54 preset sets** (126 size instances), a full **block editor**, **per-slot wallpaper cropping**, optional **transparent** home widgets, and **tap shield** so glances stay on the Home Screen.

Paid download on the App Store. **No feature-unlocking IAP** — optional **Tip Developer** (StoreKit consumable) in Settings → About only.

## Getting Started

1. Complete the **first-run guide**. If **My Widgets** is empty, iWidget seeds **Calendar**, **Weather**, and **Month** presets automatically.
2. Open **Today** for solar & lunar date, holidays, almanac, weather, and countdown previews — tap a card for detail sheets.
3. Browse **Widget Library** — filter by category, search preset or set names, tap a set to preview small / medium / large, then **Add** or **Add & Edit**.
4. Open **My Widgets** — grid by size, light/dark preview, search and sort; tap a card to push into the **editor**.
5. On iPhone/iPad, long-press the Home Screen → **＋** → search **iWidget** → pick size → **Edit Widget** → choose a **saved design** from **My Widgets** (grouped by size).
6. Read **Settings → Help** for full-screen guides: **User guide**, **Add widgets**, **Shortcuts & Siri**, and **Highlights**.

## Today

Your at-a-glance hub — grouped cards with a consistent style:

- **Solar & lunar** — Gregorian line, lunar date, stems-branches, zodiac, work/rest badges.
- **Solar term card** — interval progress, phenology, classical poem; tap through to day detail.
- **Weather** — optional block controlled by **Settings → Weather display**; pull to refresh on Today. Home hourly row scrolls history plus forecast (`homeHourlyScroll`).
- **Upcoming holidays** — horizontal preview (up to 8 deduped events); **See all** opens the full list (~one year). Empty state can jump to festival filters in Settings.
- **Countdowns** — preview up to 5; **All** opens list with manual / date / name sort, drag reorder in edit mode (preference stored in App Group).
- **Almanac (黄历)** — daily auspicious / inauspicious tags, clash, etc.; tap for day detail.
- Tap the date to open the **month grid**, then **day detail** (term poems included).

## Widget Library & My Widgets

| Area | What you get |
|------|----------------|
| **Library** | ~**54 sets**, **126** instances (small / medium / large). One row per set, three columns; dashed placeholder if a size is missing. Featured + category filters; search set or member preset names. |
| **My Widgets** | Saved designs in a grid by size; light/dark thumbnail toggle; search; sort by manual order, name, newest, or oldest. Thumbnails use **rasterized cache** for smooth scrolling. |
| **Actions** | Share board image, rename, duplicate, delete (with confirmation). Stale designs referenced by an old widget show an in-app banner → **Widget guide**. |

## Block Editor

- **Grid** — drag and resize blocks; delete, replace same-size type; **Recent** block kinds remembered.
- **Layouts** — one design can store separate layouts for **4×4**, **8×4**, and **8×8** grids.
- **Appearance** — per-block alignment, text color/size (incl. height ratio), fill role/opacity/corner radius/padding, borders (solid/dash/dot), shadow; **copy appearance** to other sizes/slots; **default appearance to all blocks**.
- **Background** — solid, gradient, or **wallpaper** (global or per-design screenshots); **12 color presets**; optional **Describe colors** (Apple Intelligence on supported devices).
- **Behavior** — per-design week start override; **intercept taps** (widget opens only when you allow); weak-contrast hints with fix menu.
- **Undo** — 30 steps; share rendered board image from the editor.

### Block families (high level)

| Family | Examples |
|--------|----------|
| **Gregorian** | Day number styles, date, weekday, work/rest, day note, month grid (subtitle strategy, badges, outer-month days, today highlight), week strip, year progress |
| **Lunar** | Lunar line, stems-branches, next festival/term, holiday countdown, almanac, term poem / interval / phenology, moon phase |
| **Clock** | Digital, analog face |
| **Weather** | Layout tiers, hourly count, detail field toggles, precipitation |
| **Countdown** | Title + days / days only / large number; cycle entries on widget |
| **Device (iOS)** | Battery, storage, Now Playing, Health steps — refreshed in app & background task |
| **Decor** | Text, divider, sticker (SF Symbols), greeting |

Library and in-app previews may use **sample data**; **home-screen widgets use live data only**.

## Home Screen, Lock Screen & Mac

| Surface | Notes |
|---------|--------|
| **Home (S/M/L)** | One **board** per saved design. Widget configuration picks from **My Widgets** by size. Options: appearance, transparent background, tap opens app or stays on widget (`BoardIntent`). |
| **Lock Screen (iOS)** | Circular, rectangular, inline — lunar, next festival, work/rest, countdown, weather, year progress. |
| **Control Center (iOS 18+)** | Today’s lunar snippet; **Refresh widgets** control. |
| **StandBy** | Uses compact standby preset (large type, dark) on small board. |
| **Mac menu bar** | Month calendar; tap a day → deep link to Today / day detail. |

**Transparent widgets** — crop light/dark wallpapers per slot so the board blends with your Home Screen (see in-app **Add widgets** guide).

## Notifications (optional)

Local notifications only — up to **48** scheduled:

- Evening **20:00** — next-day **work/rest** swap, holiday start, festival, solar term (within **21 days**).
- **09:00** on countdown target day.

Toggle categories in **Settings → Notifications**.

## Settings highlights

- **Appearance** — App light/dark/system; **in-app language** (System / 简体 / 繁體 / English); large text; week starts Monday; °C/°F; festival layers; **location or manual city** for weather; wallpaper; Health for steps (iOS).
- **iCloud** — off by default; when on, syncs design JSON and cropped wallpapers via **CloudKit** private database (your Apple ID).
- **Data** — reload widget timelines; clear weather cache.
- **About** — rate, optional tip, feedback email with diagnostics, more apps, licenses.

## Siri, Shortcuts & URLs

- Built-in phrases (examples): *“Today’s lunar in iWidget”*, *“Next festival in iWidget”*.
- Separate **Workday** App Intent — ask whether a **date** is a work or rest day (add in Shortcuts manually).
- Deep links: `iwidget://today`, `iwidget://day?y=&m=&d=`, `iwidget://settings?scroll=festivals` — see [URL Scheme](url-scheme).

## Data & privacy

- Lunar almanac, festivals, and term tables compute **on device** (calendar tables aligned with iHTC Studio’s iCalendar lineage; **UI and widgets are a separate product**).
- Weather via **Apple WeatherKit** when online; cached in App Group.
- **No iHTC Studio account.** Optional iCloud is Apple-hosted. Details: [Privacy Policy](privacy).

## System Requirements

| Platform | Minimum |
|----------|---------|
| iPhone / iPad | iOS 17.0+ |
| Mac | macOS 14.0+ |

## App Store

| | |
|---|---|
| **App** | iWidget |
| **Bundle ID** | `com.iHTCboy.iWidget` |
| **Download** | [App Store](https://apps.apple.com/app/id6817595772) |

## Contact

- **Email:** [AppleOSer@gmail.com](mailto:AppleOSer@gmail.com) — we usually reply within 48 hours.

[FAQ](faq) · [URL Scheme](url-scheme) · [Privacy Policy](privacy)

</section>

<section lang="zh-CN" markdown="1">

**为壁纸调色，拼出真正想要的小组件。**

**爱组件**（iWidget / 愛組件）是面向 **iPhone、iPad 与 Mac** 的 **小组件设计器**——不是换皮日历。公历农历、天气、倒数、设备信息都是可拖拽的 **积木**；**54 套模板**（126 个尺寸实例）、完整 **编辑器**、**按槽位裁壁纸**、可选 **透明底**，以及 **误触拦截**，让 glance 留在主屏。

App Store **付费下载**。**不解锁功能**的内购；仅在 **设置 → 关于** 提供可选 **开发者赞赏**（StoreKit 消耗型）。

## 快速上手

1. 完成 **首次引导**。若 **我的组件** 为空，会自动添加日历、天气、月历三个默认预设副本。
2. 打开 **今日** — 公历农历、节气、节日、黄历、天气与倒数预览；点卡片进详情 Sheet。
3. 浏览 **组件库** — 分类/精选筛选、搜索套名或成员 preset；详情页并排预览小/中/大三尺寸，**添加** 或 **添加并编辑**。
4. 进入 **我的组件** — 按尺寸网格、深浅预览、搜索排序；点卡片 **推入编辑器**。
5. iPhone/iPad：长按主屏 → **＋** → 搜索「爱组件」→ 选尺寸 → **编辑小组件** → 在 **我的组件**（按尺寸分组）中选 **已保存设计**。
6. **设置 → 帮助** 有四本全屏教程：使用说明、添加小组件、快捷指令与 Siri、功能亮点。

## 今日

统一卡片风格的概览页：

- **公历与农历** — 日期行、农历、干支生肖、休班角标。
- **节气卡片** — 区间进度、物候、诗词；可进日详情。
- **天气** — 由 **设置 → 天气展示** 控制是否显示；支持下拉刷新；首页逐时可横向滚动（含当前整点前历史条）。
- **即将到来** — 横向最多 8 条；**查看全部** 约一年内列表；空状态可去设置筛节日。
- **倒数日** — 最多预览 5 条；**全部** 打开列表，支持手动/日期/名称排序与拖拽（偏好存 App Group）。
- **黄历** — 宜忌、冲煞等；点进当日详情。
- 点日期进 **月历**，再进 **日详情**（含节气诗）。

## 组件库与我的组件

| 区域 | 说明 |
|------|------|
| **组件库** | 约 **54 套**、**126** 实例；一套一行三列，缺尺寸显示虚线占位；精选+分类；可搜索。 |
| **我的组件** | 按小/中/大分组；深浅预览；搜索与排序；缩略图 **栅格化缓存** 保证列表流畅。 |
| **操作** | 分享看板图、重命名、复制、删除；桌面仍引用已删设计时会提示并链到 **小组件教程**。 |

## 编辑器

- **网格** — 拖动缩放；删除/替换同尺寸类型；**最近使用** 积木类别。
- **布局** — 同一设计可分别保存 **4×4 / 8×4 / 8×8** 排法。
- **外观** — 对齐、字色字号、底框/边框/阴影；**复制外观**、**默认外观应用到全部**；弱对比橙色虚线与修复菜单。
- **背景** — 纯色/渐变/壁纸；12 套配色预设；支持设备 **按描述配色**（Apple Intelligence）。
- **行为** — 可覆盖 App 周起始；**拦截跳转**（轻触不进 App）。
- **撤销** 30 步；可分享看板截图。

### 积木族（概览）

公历（日号、月历格、周条、年进度等）、农历（农历行、下一节日/节气、黄历、节气诗/物候、月相）、时钟、天气、倒数、设备（电池/存储/音乐/步数，iOS）、装饰（文字/分割线/贴纸/问候）。

库内预览可用 **示例数据**；**桌面小组件仅显示真实数据**。

## 主屏、锁屏与 Mac

| 场景 | 说明 |
|------|------|
| **主屏小/中/大** | 每个已保存设计一块看板；配置 Intent 只从 **我的组件** 按尺寸选设计；可选外观、透明底、点击行为。 |
| **锁屏（iOS）** | 圆形/矩形/单行 — 农历、节日、休班、倒数、天气、年进度等。 |
| **控制中心（iOS 18+）** | 今日农历；**刷新小组件**。 |
| **StandBy** | 小号待机预设（大字深色）。 |
| **Mac 菜单栏** | 月历；点某天用深链打开今日/日详情。 |

**透明小组件** — 按槽位裁切深浅壁纸，与主屏融为一体（见应用内 **添加小组件** 教程）。

## 通知（可选）

仅 **本地通知**，最多 **48** 条：前晚 **20:00** 提醒调休/假期/节日/节气（21 天内）；倒数日当天 **09:00**。可在 **设置 → 通知** 按类型开关。

## 设置要点

- **外观** — App 深浅色；**应用内语言**（跟随系统/简体/繁体/English）；大字；周一起算；温标；节日分层；**定位或手动城市**；壁纸；Health 步数（iOS）。
- **iCloud** — 默认关闭；开启后通过 **CloudKit** 私有库同步设计 JSON 与裁切壁纸。
- **数据** — 刷新小组件时间线；清除天气缓存。
- **关于** — 评分、赞赏、带诊断信息的反馈邮件、更多 App、许可说明。

## Siri、快捷指令与链接

- 系统建议短语示例：「爱组件 今天农历」「爱组件 下一个节日」。
- 独立 **是否上班** App Intent — 在快捷指令里选日期查询（不挂在建议短语上）。
- 深链：`iwidget://today`、`iwidget://day?y=&m=&d=`、`iwidget://settings?scroll=festivals` — 见 [URL Scheme 说明](url-scheme)。

## 数据与隐私

- 农历、节气、节日、黄历 **本机离线计算**（历法数据与 iCalendar 同源，**产品与界面独立**）。
- 天气走 **Apple WeatherKit**，缓存于 App Group。
- **无爱火腿肠账号**；可选 iCloud 由 Apple 托管。详见 [隐私政策](privacy)。

## 系统要求

| 平台 | 最低版本 |
|------|----------|
| iPhone / iPad | iOS 17.0+ |
| Mac | macOS 14.0+ |

## App Store

| | |
|---|---|
| **应用** | 爱组件（iWidget） |
| **Bundle ID** | `com.iHTCboy.iWidget` |
| **下载** | [App Store](https://apps.apple.com/app/id6817595772) |

## 联系

- **邮箱：** [AppleOSer@gmail.com](mailto:AppleOSer@gmail.com) — 通常 48 小时内回复。

[常见问题](faq) · [URL Scheme](url-scheme) · [隐私政策](privacy)

</section>

<section lang="zh-TW" markdown="1">

**為桌布調色，拼出真正想要的小工具。**

**愛組件**（iWidget / 爱组件）是面向 **iPhone、iPad 與 Mac** 的 **小工具設計器**——不是換皮日曆。公農曆、天氣、倒數、裝置資訊都是可拖曳的 **積木**；**54 套模板**（126 個尺寸實例）、完整 **編輯器**、**依槽位裁桌布**、可選 **透明底**，以及 **誤觸攔截**，讓 glance 留在主畫面。

App Store **付費下載**。**不解鎖功能**的內購；僅在 **設定 → 關於** 提供可選 **開發者打賞**（StoreKit 消耗型）。

## 快速上手

1. 完成 **首次引導**。若 **我的組件** 為空，會自動添加日曆、天氣、月曆三個預設副本。
2. 打開 **今日** — 公農曆、節氣、節日、黃曆、天氣與倒數預覽；點卡片進詳情 Sheet。
3. 瀏覽 **組件庫** — 分類/精選篩選、搜尋套名或成員 preset；詳情頁並排預覽小/中/大三尺寸，**添加** 或 **添加並編輯**。
4. 進入 **我的組件** — 依尺寸網格、深淺預覽、搜尋排序；點卡片 **推入編輯器**。
5. iPhone/iPad：長按主畫面 → **＋** → 搜尋「愛組件」→ 選尺寸 → **編輯小工具** → 在 **我的組件**（依尺寸分組）中選 **已儲存設計**。
6. **設定 → 幫助** 有四本全螢幕教學：使用說明、添加小工具、捷徑與 Siri、功能亮點。

## 今日

統一卡片風格的概覽頁：

- **公曆與農曆** — 日期行、農曆、干支生肖、休班角標。
- **節氣卡片** — 區間進度、物候、詩詞；可進日詳情。
- **天氣** — 由 **設定 → 天氣展示** 控制是否顯示；支援下拉重新整理；首頁逐時可橫向捲動（含目前整點前歷史條）。
- **即將到來** — 橫向最多 8 條；**查看全部** 約一年內列表；空狀態可去設定篩節日。
- **倒數日** — 最多預覽 5 條；**全部** 打開列表，支援手動/日期/名稱排序與拖曳（偏好存 App Group）。
- **黃曆** — 宜忌、沖煞等；點進當日詳情。
- 點日期進 **月曆**，再進 **日詳情**（含節氣詩）。

## 組件庫與我的組件

| 區域 | 說明 |
|------|------|
| **組件庫** | 約 **54 套**、**126** 實例；一套一行三列，缺尺寸顯示虛線占位；精選+分類；可搜尋。 |
| **我的組件** | 依小/中/大分組；深淺預覽；搜尋與排序；縮圖 **柵格化快取** 保證列表流暢。 |
| **操作** | 分享看板圖、重新命名、複製、刪除；桌面仍引用已刪設計時會提示並鏈到 **小工具教學**。 |

## 編輯器

- **網格** — 拖動縮放；刪除/替換同尺寸類型；**最近使用** 積木類別。
- **版面** — 同一設計可分別儲存 **4×4 / 8×4 / 8×8** 排法。
- **外觀** — 對齊、字色字級、底框/邊框/陰影；**複製外觀**、**預設外觀套用到全部**；弱對比橘色虛線與修復選單。
- **背景** — 純色/漸層/桌布；12 套配色預設；支援裝置 **依描述配色**（Apple Intelligence）。
- **行為** — 可覆寫 App 週起始；**攔截跳轉**（輕觸不進 App）。
- **復原** 30 步；可分享看板截圖。

### 積木族（概覽）

公曆（日號、月曆格、週條、年進度等）、農曆（農曆行、下一節日/節氣、黃曆、節氣詩/物候、月相）、時鐘、天氣、倒數、裝置（電池/儲存/音樂/步數，iOS）、裝飾（文字/分割線/貼紙/問候）。

庫內預覽可用 **範例資料**；**桌面小工具僅顯示真實資料**。

## 主畫面、鎖定與 Mac

| 場景 | 說明 |
|------|------|
| **主畫面小/中/大** | 每個已儲存設計一塊看板；設定 Intent 只從 **我的組件** 依尺寸選設計；可選外觀、透明底、點按行為。 |
| **鎖定畫面（iOS）** | 圓形/矩形/單行 — 農曆、節日、休班、倒數、天氣、年進度等。 |
| **控制中心（iOS 18+）** | 今日農曆；**重新整理小工具**。 |
| **StandBy** | 小號待機預設（大字深色）。 |
| **Mac 選單列** | 月曆；點某天用深鏈打開今日/日詳情。 |

**透明小工具** — 依槽位裁切深淺桌布，與主畫面融為一體（見 App 內 **添加小工具** 教學）。

## 通知（可選）

僅 **本地通知**，最多 **48** 條：前一晚 **20:00** 提醒調休/假期/節日/節氣（21 天內）；倒數當天 **09:00**。可在 **設定 → 通知** 依類型開關。

## 設定要點

- **外觀** — App 深淺色；**應用內語言**（跟隨系統/簡體/繁體/English）；大字；週一起算；溫標；節日分層；**定位或手動城市**；桌布；Health 步數（iOS）。
- **iCloud** — 預設關閉；開啟後透過 **CloudKit** 私有庫同步設計 JSON 與裁切桌布。
- **資料** — 重新整理小工具時間軸；清除天氣快取。
- **關於** — 評分、赞赏、附診斷資訊的反馈郵件、更多 App、許可說明。

## Siri、捷徑與連結

- 系統建議片語示例：「愛組件 今天農曆」「愛組件 下一個節日」。
- 獨立 **是否上班** App Intent — 在捷徑裡選日期查詢（不掛在建議片語上）。
- 深鏈：`iwidget://today`、`iwidget://day?y=&m=&d=`、`iwidget://settings?scroll=festivals` — 見 [URL Scheme 說明](url-scheme)。

## 資料與隱私

- 農曆、節氣、節日、黃曆 **本機離線計算**（曆法資料與 iCalendar 同源，**產品與介面獨立**）。
- 天氣走 **Apple WeatherKit**，快取於 App Group。
- **無爱火腿肠帳號**；可選 iCloud 由 Apple 代管。詳見 [隱私政策](privacy)。

## 系統要求

| 平台 | 最低版本 |
|------|----------|
| iPhone / iPad | iOS 17.0+ |
| Mac | macOS 14.0+ |

## App Store

| | |
|---|---|
| **應用** | 愛組件（iWidget） |
| **Bundle ID** | `com.iHTCboy.iWidget` |
| **下載** | [App Store](https://apps.apple.com/app/id6817595772) |

## 聯絡

- **信箱：** [AppleOSer@gmail.com](mailto:AppleOSer@gmail.com) — 通常 48 小時內回覆。

[常見問題](faq) · [URL Scheme](url-scheme) · [隱私政策](privacy)

</section>
