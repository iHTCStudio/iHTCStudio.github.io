---
layout: doc
title: iWool — FAQ
app_id: iWool
doc_title_en: Frequently Asked Questions
doc_title_zh_cn: 常见问题
doc_title_zh_tw: 常見問題
description: Frequently asked questions about iWool.
---

<section lang="en" markdown="1">

### Does iWool work on iPad?

Yes. iWool is a universal app for **iPhone and iPad** (iOS 15.0+). Layout adapts to iPad screen sizes; widgets and Live Activities follow the same rules as on iPhone.

### Does iWool require an account or internet connection?

No. iWool works entirely offline. All data is stored locally on your device using SQLite. No account, no sign-up and no network connection are required to use any feature (except opening http/https links inside the app).

### Where is my data stored? Is it safe?

All data — activities, reminders, earnings records, recurrence states — is stored in a local SQLite database on your device. Nothing is uploaded to any server. If you uninstall the app, your data will be deleted. Back up regularly using **Settings → Data → Export Full Backup**.

### How do I back up and restore my data?

Go to **Settings → Data → Export Full Backup** to generate a CSV file. Save it to Files, AirDrop it to your Mac or send it by email.

To restore, go to **Settings → Data → Import Backup** and choose your file. You will be asked to choose between:

- **Replace all data** — clears everything and restores from backup. Use this when switching devices or reinstalling.
- **Append only (keep existing)** — inserts backup activities as new records without deleting anything on your device. Use this to merge data from another device.

### How do recurring activities work?

When you set a recurrence rule (daily, weekly, monthly, yearly or a custom interval), iWool stores one master record and virtually expands it into individual occurrences on each day. The list and calendar always show today's occurrence for a recurring series.

To mark a specific day's occurrence as complete, use the long-press menu or the detail page bottom toolbar. That marks only that day; the series continues.

### Why is a reminder not showing up?

iOS limits each app to approximately 64 pending local notifications at a time. iWool prioritises non-recurring activities and schedules up to 120 days of future occurrences for recurring ones, but very large collections of recurring reminders may be trimmed.

Check **Settings → Notifications → Scheduled Local Reminders** to see exactly which reminders are currently registered.

Also verify:

- Notification permission is granted (iOS Settings → iWool → Notifications).
- The activity is not cancelled (cancelled activities have their reminders cleared automatically).
- The reminder time is in the future.

### What is the difference between "estimated earnings" and "recorded earnings"?

- **Estimated earnings** — entered in the activity form. Displayed on the activity card. Does not count in Statistics.
- **Recorded earnings** — entered in the activity detail page via the earnings form. These are the actual amounts counted in all Statistics totals, trend charts and platform rankings.

### How do I record earnings for a specific day of a recurring activity?

Open the activity detail for that day's occurrence (tap the activity in the list or calendar on that day). In the detail page, tap **Record** in the earnings section. The record date will default to that day's occurrence date.

### Can I delete a single earnings entry without affecting the activity?

Yes. Open the activity detail, tap the earnings row you want to edit, and in the edit form scroll to the bottom. Tap **Delete this earnings record** and confirm. Only that one entry is removed; the activity and all other records remain untouched.

### The statistics chart is showing wrong amounts for Japanese Yen (JPY) / Korean Won (KRW).

These currencies have no decimal places by default, which may have caused amounts to appear as whole numbers in older versions. In the current version you can configure the number of decimal places independently:

- Go to **Settings → Appearance & Language → Amount Decimals** to set the number of decimal places for all amount displays (default: 2).
- Go to **Settings → Appearance & Language → Chart Amount Decimals** to set the decimal places for chart bar labels specifically (default: 0).

### How do I use the Dynamic Island / Live Activity feature?

**Event countdown** (iOS 16.1+, supported iPhone): enable in **Settings → Notifications → Live Activity**. Set lead time (1–480 minutes). Activities in the window are picked automatically; long-press on Home or Calendar → **Add to Dynamic Island**.

**Quick Countdown** (iOS 16.2+): a **standalone** island timer **not tied to your activity database**. Open **Settings → Island Reminder**, use a Home Screen Quick Action, or `iwool://island`. Duration **1 second to 8 hours**; optional title, note and accent colour. When it ends, the Live Activity dismisses — nothing is saved unless you create a wool activity separately.

### What is Quick Countdown vs event Live Activity?

| | Event countdown | Quick Countdown |
|---|-----------------|-----------------|
| Linked to activity | Yes | No |
| Persisted in app | Yes | No |
| Min iOS | 16.1 | 16.2 |
| How to start | Auto or long-press activity | Settings / shortcut / `iwool://island` |

### How do Home Screen Quick Actions work?

Long-press the iWool icon (iOS). Choose up to **4** from **9** presets in **Settings → Tools → Home Screen Shortcuts**: Home, Calendar, Statistics, Quick Countdown, New Activity, Scheduled Reminders, Scanner, Rate, Feedback. Default: Home, Calendar, Statistics, Quick Countdown. Each uses an `iwool://` URL.

### How do `iwool://` deep links work?

iWool supports **`iwool://`** for tabs, actions and event detail — used by widgets, Shortcuts and Quick Actions. Examples:

- `iwool://home`, `iwool://calendar`, `iwool://stats`, `iwool://settings`
- `iwool://new`, `iwool://island`, `iwool://scanner`, `iwool://reminders`
- `iwool://event/42`, `iwool://event/42?day=189345600` (recurring occurrence)

Unknown paths are ignored (no silent redirect to Home). See the full [**URL Scheme reference**](url-scheme).

### How do I share an activity or stats as an image?

From an activity detail page or the **Statistics** tab toolbar, use **Share** to render a branded **PNG image card** (gradient, QR code, optional earnings if enabled in Settings). The image is generated on-device; saving to Photos may request photo library access.

### How many widgets does iWool include?

**12 widget families** — eight Home Screen widgets (Today Active, Today All, Today Upcoming, All Events, Stats Overview, Earnings, Glance, Top Platforms) plus four Lock Screen accessory styles (iOS 16+).

### How do I add widgets to my Home Screen or Lock Screen?

Detailed step-by-step instructions are available in **Settings → Widgets → Widget Guide** inside the app. In short:

1. Long-press an empty area of your Home Screen and tap the **+** button.
2. Search for **iWool** in the widget gallery.
3. Choose a widget style and size, then tap **Add Widget**.

For Lock Screen widgets (iOS 16+): long-press your Lock Screen and tap **Customise**, then add iWool widgets to the Lock Screen widget row.

### Why does the widget show outdated data?

Widgets refresh when you open the app or when data changes. iOS also refreshes widget timelines periodically in the background (about every 15 minutes at best). If the widget is stale, open iWool once to force a refresh.

### How do I change the display language?

Go to **Settings → Appearance & Language → Display Language**. You can choose from 13 languages independently of your device's system language:

English, Simplified Chinese, Traditional Chinese, Japanese, Korean, Thai, Hindi, Spanish, French, German, Brazilian Portuguese, Russian, Arabic.

The change takes effect immediately throughout the app.

### Can I share an activity without sharing my earnings amounts?

Yes. By default, copying or sharing an activity does not include your earnings records. If you want to include them, go to **Settings → Appearance & Language** and enable **Include earnings when sharing**.

### How do I scan a QR code or barcode?

Go to **Settings → Tools → QR / Barcode Scanner**. Point your camera at a code or tap the album icon to pick an image. Results appear in a list you can copy or open in Safari.

You can also scan directly from the activity form: when filling in the Activity URL field, tap the scan icon next to it to scan a code and fill the URL automatically.

### What does "archive" mean? Is it the same as delete?

No. Archiving hides an activity from the main list without deleting it. Archived activities can be viewed, restored or deleted from **Settings → Activity Management → Archived Activities**.

Long-press a completed, expired or cancelled activity to see the Archive option. To archive all completed, expired and cancelled non-recurring activities at once, use **Settings → Activity Management → Archive All Completed**.

### Still need help?

Contact us at [AppleOSer@gmail.com](mailto:AppleOSer@gmail.com) or use the in-app **Settings → Send Feedback** option. We typically respond within 48 hours.

</section>

<section lang="zh-CN" markdown="1">

### 爱羊毛支持 iPad 吗？

支持。爱羊毛是 **iPhone 与 iPad** 通用应用（iOS 15.0+）。界面会适配 iPad 屏幕；小组件与实时活动规则与 iPhone 相同。

### 爱羊毛需要账号或联网吗？

不需要。爱羊毛完全离线工作。所有数据使用 SQLite 存储在设备本地。除了在应用内打开 http/https 链接以外，所有功能都无需账号、无需注册、无需联网。

### 数据存在哪里？是否安全？

所有数据——活动、提醒、收益记录、重复状态——都存放在设备本地的 SQLite 数据库中。不会上传到任何服务器。如果卸载应用，数据将被删除。请使用 **设置 → 数据 → 导出完整备份** 定期备份。

### 如何备份与恢复数据？

进入 **设置 → 数据 → 导出完整备份** 生成 CSV 文件。可保存到「文件」、AirDrop 到 Mac 或邮件发送。

恢复时，进入 **设置 → 数据 → 导入备份** 选择文件。你将被询问：

- **替换全部数据** — 清空所有数据后从备份恢复。换设备或重新安装时使用。
- **仅追加（保留现有）** — 把备份中的活动作为新记录追加，不删除任何已有数据。用于合并来自另一台设备的数据。

### 重复活动如何工作？

设置重复规则（每日、每周、每月、每年或自定义间隔）后，爱羊毛会保存一条主记录，并虚拟展开为每一天的实例。列表与日历总是显示重复系列在今日的实例。

要把某一天的实例标为完成，使用长按菜单或详情页底部工具栏。这只会标记那一天；系列继续。

### 为什么提醒没有出现？

iOS 限制每个应用同时挂起约 64 条本地通知。爱羊毛优先安排非重复活动，重复活动会安排未来 120 天的实例，但极大量的重复提醒可能会被裁剪。

可在 **设置 → 通知 → 已计划的本地提醒** 查看当前已注册的提醒。

也请确认：

- 已授予通知权限（iOS 设置 → iWool → 通知）。
- 活动未被取消（取消的活动会自动清除提醒）。
- 提醒时间在未来。

### 「预估收益」与「记录收益」的区别？

- **预估收益** — 在活动表单中填写。在活动卡片上显示。不计入统计。
- **记录收益** — 在活动详情页通过收益表单填写。这是计入所有统计总计、趋势图和平台排名的实际金额。

### 如何为重复活动的特定一天记录收益？

打开那一天对应的活动实例（在那一天的列表或日历中点按活动）。在详情页的收益区域点 **记录**。记录日期默认为那一天的实例日期。

### 可以删除单条收益记录而不影响活动吗？

可以。打开活动详情，点按你想编辑的收益行，编辑表单滚到底部，点 **删除此条收益记录** 并确认。只删除那一条；活动与其他记录保持不变。

### 日元（JPY）/ 韩元（KRW）的统计图表金额显示有问题。

这些货币默认无小数位，旧版可能导致金额显示为整数。在当前版本中可独立配置小数位：

- 进入 **设置 → 外观与语言 → 金额小数位** 设置所有金额显示的小数位（默认 2）。
- 进入 **设置 → 外观与语言 → 图表金额小数位** 单独设置图表柱形标签的小数位（默认 0）。

### 如何使用灵动岛 / 实时活动？

**活动倒计时**（iOS 16.1+）：**设置 → 通知 → 实时活动**，提前 1–480 分钟；长按活动 → **加入灵动岛**。

**灵动岛提醒 Quick Countdown**（iOS 16.2+）：独立倒计时，不写入活动库。**设置 → 灵动岛提醒**、主屏快捷方式或 `iwool://island`，时长 1 秒–8 小时。

### 主屏快捷方式怎么用？

长按图标，**设置 → 工具 → 主屏快捷方式** 从 9 项选 4 项。默认：首页、日历、统计、灵动岛提醒。

### `iwool://` 深度链接怎么用？

- Tab：`home`、`calendar`、`stats`、`settings`
- 操作：`new`、`island`、`scanner`、`reminders`、`rate`、`feedback`
- 活动：`event/42`、`event/42?day=…`

无效路径不会回首页。详见 [**URL Scheme 文档**](url-scheme)。

### 如何把活动或统计分享成图片？

在活动详情页或统计页工具栏使用 **分享**，生成 **PNG 分享图**（渐变、二维码；设置中可选含收益）。保存到相册可能请求权限。

### 爱羊毛有多少款小组件？

共 **12 款小组件**——8 款主屏（今日进行中、今日全部、今日待开始、全部事件、统计概览、收益、一览、平台 Top）+ 4 款锁屏附件样式（iOS 16+）。

### 如何添加主屏幕或锁屏小组件？

应用内 **设置 → 小组件 → 小组件指南** 提供详细分步说明。简要：

1. 长按主屏空白区域点 **+** 按钮。
2. 在小组件库中搜索 **iWool**。
3. 选择小组件样式与尺寸后点 **添加小组件**。

锁屏小组件（iOS 16+）：长按锁屏点 **自定义**，把 iWool 小组件添加到锁屏小组件行。

### 为什么小组件显示过时数据？

小组件在你打开应用或数据变化时刷新。iOS 也会在后台周期性刷新小组件时间线（最快约每 15 分钟一次）。如果小组件过时，打开一次爱羊毛即可强制刷新。

### 如何更改显示语言？

进入 **设置 → 外观与语言 → 显示语言**。可独立于设备系统语言从 13 种语言中选择：

英文、简体中文、繁体中文、日文、韩文、泰文、印地文、西班牙文、法文、德文、巴西葡萄牙文、俄文、阿拉伯文。

切换在整个应用中立即生效。

### 可以分享活动而不分享收益金额吗？

可以。默认情况下，复制或分享活动不会包含收益记录。如需包含，进入 **设置 → 外观与语言** 开启 **分享时包含收益**。

### 如何扫描二维码或条码？

进入 **设置 → 工具 → 二维码 / 条码扫描**。把相机对准条码或点按相册图标选择图片。结果以列表形式呈现，可复制或在 Safari 中打开。

也可在活动表单中直接扫描：填写活动 URL 时点按旁边的扫描图标，扫码后自动填入 URL。

### 「归档」是什么意思？跟删除一样吗？

不一样。归档将活动从主列表中隐藏，但不删除。可在 **设置 → 活动管理 → 已归档活动** 查看、恢复或删除。

长按已完成、已过期或已取消的活动可看到「归档」选项。一次归档所有已完成、已过期、已取消的非重复活动，请使用 **设置 → 活动管理 → 归档全部已完成**。

### 仍需帮助？

发邮件到 [AppleOSer@gmail.com](mailto:AppleOSer@gmail.com)，或使用应用内 **设置 → 发送反馈**。我们通常在 48 小时内回复。

</section>

<section lang="zh-TW" markdown="1">

### 愛羊毛支援 iPad 嗎？

支援。愛羊毛是 **iPhone 與 iPad** 通用應用（iOS 15.0+）。介面會適配 iPad 螢幕；小工具與即時活動規則與 iPhone 相同。

### 愛羊毛需要帳號或連網嗎？

不需要。愛羊毛完全離線工作。所有資料使用 SQLite 儲存在裝置本地。除了在應用內開啟 http/https 連結以外，所有功能都無需帳號、無需註冊、無需連網。

### 資料存在哪裡？是否安全？

所有資料——活動、提醒、收益紀錄、重複狀態——都存放在裝置本地的 SQLite 資料庫中。不會上傳到任何伺服器。如果解除安裝應用，資料將被刪除。請使用 **設定 → 資料 → 匯出完整備份** 定期備份。

### 如何備份與還原資料？

進入 **設定 → 資料 → 匯出完整備份** 產生 CSV 檔案。可儲存到「檔案」、AirDrop 到 Mac 或郵件傳送。

還原時，進入 **設定 → 資料 → 匯入備份** 選擇檔案。你將被詢問：

- **取代全部資料** — 清空所有資料後從備份還原。換裝置或重新安裝時使用。
- **僅附加（保留現有）** — 把備份中的活動作為新紀錄附加，不刪除任何已有資料。用於合併來自另一台裝置的資料。

### 重複活動如何運作？

設定重複規則（每日、每週、每月、每年或自訂間隔）後，愛羊毛會儲存一條主紀錄，並虛擬展開為每一天的實例。列表與日曆總是顯示重複系列在今日的實例。

要把某一天的實例標為完成，使用長按選單或詳情頁底部工具列。這只會標記那一天；系列繼續。

### 為什麼提醒沒有出現？

iOS 限制每個應用同時掛起約 64 條本地通知。愛羊毛優先安排非重複活動，重複活動會安排未來 120 天的實例，但極大量的重複提醒可能會被裁剪。

可在 **設定 → 通知 → 已排定的本地提醒** 查看目前已註冊的提醒。

也請確認：

- 已授予通知權限（iOS 設定 → iWool → 通知）。
- 活動未被取消（取消的活動會自動清除提醒）。
- 提醒時間在未來。

### 「預估收益」與「記錄收益」的區別？

- **預估收益** — 在活動表單中填寫。在活動卡片上顯示。不計入統計。
- **記錄收益** — 在活動詳情頁透過收益表單填寫。這是計入所有統計總計、趨勢圖和平台排名的實際金額。

### 如何為重複活動的特定一天記錄收益？

開啟那一天對應的活動實例（在那一天的列表或日曆中點按活動）。在詳情頁的收益區域點 **記錄**。紀錄日期預設為那一天的實例日期。

### 可以刪除單條收益紀錄而不影響活動嗎？

可以。開啟活動詳情，點按你想編輯的收益行，編輯表單捲到底部，點 **刪除此條收益紀錄** 並確認。只刪除那一條；活動與其他紀錄保持不變。

### 日圓（JPY）/ 韓圜（KRW）的統計圖表金額顯示有問題。

這些貨幣預設無小數位，舊版可能導致金額顯示為整數。在目前版本中可獨立設定小數位：

- 進入 **設定 → 外觀與語言 → 金額小數位** 設定所有金額顯示的小數位（預設 2）。
- 進入 **設定 → 外觀與語言 → 圖表金額小數位** 單獨設定圖表柱形標籤的小數位（預設 0）。

### 如何使用靈動島 / 即時活動？

**活動倒數**（iOS 16.1+）：**設定 → 通知 → 即時活動**。**Quick Countdown**（iOS 16.2+）：獨立倒數、不寫入資料庫，經 **設定 → 靈動島提醒** 或 `iwool://island`。

### 主畫面捷徑？

**設定 → 工具 → 主畫面捷徑**，9 選 4。預設：首頁、日曆、統計、靈動島提醒。

### `iwool://` 深度連結怎麼用？

Tab、操作（`new`/`island`/`scanner` 等）與 `event/{id}?day=…`。詳見 [**URL Scheme 文件**](url-scheme)。

### 如何把活動或統計分享成圖片？

在活動詳情頁或統計頁工具列使用 **分享**，生成 **PNG 分享圖**。保存到相簿可能請求權限。

### 愛羊毛有多少款小工具？

共 **12 款小工具**——8 款主畫面（今日進行中、今日全部、今日待開始、全部事件、統計概覽、收益、一覽、平台 Top）+ 4 款鎖定畫面附件樣式（iOS 16+）。

### 如何新增主畫面或鎖定畫面小工具？

應用內 **設定 → 小工具 → 小工具指南** 提供詳細分步說明。簡要：

1. 長按主畫面空白區域點 **+** 按鈕。
2. 在小工具庫中搜尋 **iWool**。
3. 選擇小工具樣式與尺寸後點 **新增小工具**。

鎖定畫面小工具（iOS 16+）：長按鎖定畫面點 **自訂**，把 iWool 小工具新增到鎖定畫面小工具行。

### 為什麼小工具顯示過時資料？

小工具在你開啟應用或資料變化時重新整理。iOS 也會在背景週期性重新整理小工具時間軸（最快約每 15 分鐘一次）。如果小工具過時，開啟一次愛羊毛即可強制重新整理。

### 如何更改顯示語言？

進入 **設定 → 外觀與語言 → 顯示語言**。可獨立於裝置系統語言從 13 種語言中選擇：

英文、簡體中文、繁體中文、日文、韓文、泰文、印地文、西班牙文、法文、德文、巴西葡萄牙文、俄文、阿拉伯文。

切換在整個應用中立即生效。

### 可以分享活動而不分享收益金額嗎？

可以。預設情況下，複製或分享活動不會包含收益紀錄。如需包含，進入 **設定 → 外觀與語言** 開啟 **分享時包含收益**。

### 如何掃描 QR Code 或條碼？

進入 **設定 → 工具 → QR Code / 條碼掃描**。把相機對準條碼或點按相簿圖示選擇圖片。結果以列表形式呈現，可複製或在 Safari 中開啟。

也可在活動表單中直接掃描：填寫活動 URL 時點按旁邊的掃描圖示，掃碼後自動填入 URL。

### 「封存」是什麼意思？跟刪除一樣嗎？

不一樣。封存將活動從主列表中隱藏，但不刪除。可在 **設定 → 活動管理 → 已封存活動** 查看、還原或刪除。

長按已完成、已過期或已取消的活動可看到「封存」選項。一次封存所有已完成、已過期、已取消的非重複活動，請使用 **設定 → 活動管理 → 封存全部已完成**。

### 仍需協助？

寄信到 [AppleOSer@gmail.com](mailto:AppleOSer@gmail.com)，或使用應用內 **設定 → 傳送回饋**。我們通常在 48 小時內回覆。

</section>
