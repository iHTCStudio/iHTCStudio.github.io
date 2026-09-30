---
layout: doc
title: iWidget — FAQ
app_id: iWidget
doc_title_en: Frequently Asked Questions
doc_title_zh_cn: 常见问题
doc_title_zh_tw: 常見問題
description: FAQ for iWidget — widget designer, presets, editor, transparent widgets, tap shield, iCloud, weather, notifications, and Siri.
---

<section lang="en" markdown="1">

### Is iWidget a calendar app?

No. iWidget is a **widget design studio**. Calendar, weather, and countdowns are **blocks** you place on a grid. The **Today** tab is a convenient dashboard; home-screen widgets use **saved designs** from **My Widgets**.

### How is iWidget different from iCalendar?

Different product, UI, icons, and widget styles. iWidget focuses on **block layout**, **wallpaper tinting**, **transparent slots**, and **tap shield**. Calendar tables share lineage for lunar accuracy, but the apps are separate on the App Store.

### How do I add a home-screen widget?

1. Save a design in **My Widgets** (from the library or editor).
2. Long-press the Home Screen → **＋** → search **iWidget**.
3. Pick **small / medium / large** to match your design’s family.
4. Tap **Edit Widget** → choose the design (listed by size).

Full steps: **Settings → Help → Add widgets**.

### Why doesn’t my widget show the design I expect?

- Widget size must match the design family (small board → small widget).
- After deleting a design, an old widget may point to a missing UUID — open the app for a **stale design** banner and re-pick in the widget editor.
- Reload timelines: **Settings → Data → Refresh widgets**.

### What is tap shield (intercept taps)?

When **intercept** is on for a design, tapping the widget **does not** open the app — useful for wallpaper-style boards. Turn it off in the editor **Behavior** page or widget configuration if you want `iwidget://today` on tap.

### How do transparent widgets work?

Capture light/dark **wallpaper screenshots**, crop **per slot**, and enable transparent background in widget settings. See **Add widgets** guide for slot alignment tips.

### Does iWidget work offline?

**Yes** for calendar, almanac, editor, and rendering. **Weather** needs network via WeatherKit when refreshing. **Holiday JSON** may update occasionally when online. **Fonts** download on demand when selected.

### Do I need an account?

**No.** Optional **iCloud** uses your Apple ID through Apple’s CloudKit — not an iHTC Studio account.

### What does iCloud sync?

Design JSON and cropped wallpaper assets in the private **Designs** zone. Off by default. Turning it off stops sync; local files remain until deleted.

### How do notifications work?

All **local** — work/rest eve reminders, festivals, solar terms (21-day window), countdown morning alerts. Up to **48** pending. Toggle types in **Settings → Notifications**.

### Which languages are supported?

**Settings → Appearance → Language:** System, 简体中文, 繁體中文, English. Widget configuration UI follows **system language** when iOS shows the picker.

### How do Siri and Shortcuts work?

Suggested phrases include *“Today’s lunar in iWidget”* and *“Next festival in iWidget”*. Add **Workday** intent manually for a specific date. URL examples: [URL Scheme](../url-scheme).

### Does iWidget collect personal data?

No. See the [Privacy Policy](../privacy): Data Not Collected by iHTC Studio; WeatherKit/HealthKit/location only when you enable those features.

### Is the app free?

iWidget is a **paid download**. There is **no** IAP that unlocks features — only optional **Tip Developer** in About.

### Is iWidget on the App Store?

The public listing uses Apple ID **6817595772**. If the store page is not visible in your region yet, bookmark this support page; the [App Store link](https://apps.apple.com/app/id6817595772) will work once Apple publishes the app.

### Still need help?

[AppleOSer@gmail.com](mailto:AppleOSer@gmail.com) — typically within 48 hours.

</section>

<section lang="zh-CN" markdown="1">

### 爱组件是日历 App 吗？

不是。爱组件是 **小组件设计器**。日历、天气、倒数是网格上的 **积木**。**今日** 页是便捷总览；主屏小组件使用 **我的组件** 里 **已保存的设计**。

### 和爱日历有什么区别？

不同产品、界面、图标与组件样式。爱组件侧重 **积木排版**、**壁纸取色**、**透明槽位** 与 **误触拦截**。农历数据与 iCalendar 同源算法，但 App Store 上是独立应用。

### 如何添加主屏小组件？

1. 在 **我的组件** 保存设计（来自组件库或编辑器）。
2. 长按主屏 → **＋** → 搜索「爱组件」。
3. 选择与小/中/大设计匹配的 **尺寸**。
4. **编辑小组件** → 选择对应设计。

完整步骤：**设置 → 帮助 → 添加小组件**。

### 小组件显示不对怎么办？

- 尺寸须与设计族一致（小号看板 → 小号组件）。
- 删除设计后，旧组件可能仍指向无效 UUID — 打开 App 看 **失效设计** 横幅，并在组件配置里重选。
- **设置 → 数据 → 刷新小组件** 重载时间线。

### 什么是误触拦截？

设计开启 **拦截跳转** 时，点按小组件 **不会** 打开 App，适合纯壁纸看板。可在编辑器 **行为** 页或小组件配置里关闭，以允许打开 `iwidget://today`。

### 透明小组件怎么用？

截取深浅色 **壁纸截图**，**按槽位裁切**，并在小组件设置里启用透明底。对齐技巧见 **添加小组件** 教程。

### 能否离线使用？

**农历、黄历、编辑器与渲染** 可离线。**天气** 刷新需 WeatherKit 联网。**调休 JSON** 可能偶尔在线更新。**字体** 首次选用时可能下载。

### 需要账号吗？

**不需要。** 可选 **iCloud** 走 Apple CloudKit，不是爱火腿肠工作室账号。

### iCloud 同步什么？

设计 JSON 与裁切壁纸（私有 **Designs** 区域）。默认关闭；关闭后停止同步，本机文件仍保留直至删除。

### 通知如何工作？

全部为 **本地通知** — 调休前晚、节日/节气、倒数日上午等，最多 **48** 条。在 **设置 → 通知** 按类型开关。

### 支持哪些语言？

**设置 → 外观 → 语言**：跟随系统、简体中文、繁体中文、English。系统添加/编辑小组件时的选择器跟随 **设备系统语言**。

### Siri 与快捷指令？

建议短语如「爱组件 今天农历」「爱组件 下一个节日」。**是否上班** 需在快捷指令里单独添加 Intent 并选日期。URL 见 [URL Scheme 说明](../url-scheme)。

### 会收集个人数据吗？

不会。见 [隐私政策](../privacy)：爱火腿肠工作室不收集数据；天气/健康/定位仅在您启用相关功能时使用。

### 应用免费吗？

爱组件为 **付费下载**。**没有** 解锁功能的内购；**设置 → 关于** 仅有可选 **开发者赞赏**。

### 是否已上架 App Store？

商店 ID 为 **6817595772**。若你所在地区尚未看到页面，可先收藏本支持页；Apple 发布后 [App Store 链接](https://apps.apple.com/app/id6817595772) 即可打开。

### 仍需帮助？

[AppleOSer@gmail.com](mailto:AppleOSer@gmail.com) — 通常 48 小时内回复。

</section>

<section lang="zh-TW" markdown="1">

### 愛組件是日曆 App 嗎？

不是。愛組件是 **小工具設計器**。日曆、天氣、倒數是網格上的 **積木**。**今日** 頁是便捷總覽；主畫面小工具使用 **我的組件** 裡 **已儲存的設計**。

### 和愛日曆有什麼區別？

不同產品、介面、圖示與組件樣式。愛組件側重 **積木排版**、**桌布取色**、**透明槽位** 與 **誤觸攔截**。農曆資料與 iCalendar 同源演算法，但 App Store 上是獨立 App。

### 如何新增主畫面小工具？

1. 在 **我的組件** 儲存設計。
2. 長按主畫面 → **＋** → 搜尋「愛組件」。
3. 選擇與小/中/大設計匹配的 **尺寸**。
4. **編輯小工具** → 選擇對應設計。

完整步驟：**設定 → 幫助 → 添加小工具**。

### 小工具顯示不對怎麼辦？

- 尺寸須與設計族一致。
- 刪除設計後，舊組件可能仍指向無效 UUID — 開啟 App 看 **失效設計** 橫幅並重新選擇。
- **設定 → 資料 → 重新整理小工具**。

### 什麼是誤觸攔截？

設計開啟 **攔截跳轉** 時，點按小工具 **不會** 開啟 App。可在編輯器 **行為** 頁或組件設定中關閉。

### 透明小工具怎麼用？

截取深淺色 **桌布截圖**，**依槽位裁切**，並啟用透明底。見 **添加小工具** 教學。

### 能否離線使用？

**農曆、黃曆、編輯器與渲染** 可離線。**天氣** 刷新需 WeatherKit 連網。**調休 JSON** 可能偶爾線上更新。

### 需要帳號嗎？

**不需要。** 可選 **iCloud** 走 Apple CloudKit。

### iCloud 同步什麼？

設計 JSON 與裁切桌布。預設關閉。

### 通知如何運作？

全部為 **本地通知**，最多 **48** 條；在 **設定 → 通知** 管理。

### 支援哪些語言？

**設定 → 外觀 → 語言**：跟隨系統、簡體中文、繁體中文、English。系統組件選擇器跟隨 **裝置系統語言**。

### Siri 與捷徑？

建議片語如「愛組件 今天農曆」。**是否上班** 需單獨添加 Intent。URL 見 [URL Scheme 說明](../url-scheme)。

### 會收集個人資料嗎？

不會。見 [隱私政策](../privacy)。

### 應用免費嗎？

**付費下載**；無解鎖功能內購；可選 **開發者打賞**。

### 是否已上架 App Store？

商店 ID **6817595772**。若尚未看到頁面，可先收藏本支援頁；[App Store 連結](https://apps.apple.com/app/id6817595772) 在 Apple 發佈後可用。

### 仍需協助？

[AppleOSer@gmail.com](mailto:AppleOSer@gmail.com) — 通常 48 小時內回覆。

</section>
