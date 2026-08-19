---
layout: doc
title: iCangJie — FAQ
app_id: iCangJie
doc_title_en: Frequently Asked Questions
doc_title_zh_cn: 常见问题
doc_title_zh_tw: 常見問題
description: Frequently asked questions about iCangJie.
---

<section lang="en" markdown="1">

### What is Cangjie input method?

Cangjie (倉頡) is a shape-based Chinese input method invented by Chu Bong-Foo. Each character is encoded by its structural components (radicals) mapped to 24 letter keys on a virtual keyboard. Once mastered, Cangjie allows fast and precise Chinese typing without homophone disambiguation.

### What is the difference between Cangjie 3rd Gen and 5th Gen?

The **3rd Gen** (三代倉頡) standard is the classic layout widely used in Hong Kong and Taiwan. The **5th Gen** (五代倉頡) refines some encodings and expands coverage for modern characters. iCangJie bundles both standards — switch the default version in **Settings → App Settings**. On **single-character** word detail pages, a **side-by-side compare card** shows both editions with radical keyboard strips; tap **copy** on any code badge or use the toolbar to copy the character or all codes.

### What does "quick method" (速成) mean?

Quick method uses only the **first and last radical keys** of the full Cangjie code (levels 1–2). iCangJie supports quick-method browsing in **Levels**, quick-code typing practice, and mixed mode (try quick first, fall back to full code after a mistake).

### How does Lookup search work?

Open the **Lookup** tab and type:

- **Cangjie code prefix** — e.g. `ab` matches codes starting with AB.
- **Exact character** — paste or pick a single Han character.
- **Pinyin prefix** — toneless pinyin (toggle in Settings).
- **Jyutping prefix** — Cantonese romanization.

When a mode returns no results, iCangJie suggests switching modes. Four **char-set priorities** (Hong Kong, Taiwan Traditional, Simplified, General) affect ranking.

### How does Typing Practice work?

Open **Typing** and choose a mode:

- **Full code** — type the complete Cangjie code for each character.
- **Quick code** — practice levels 1–2 quick codes only.
- **Mixed** — try quick code first; after a mistake, the app reveals and switches to full code.

Content sources include 16 built-in classical passages (Simplified & Traditional), random word lists, pasted text, favorites, and your wrong-book (auto-resolves the correct Han character). Live **radical key highlights** help you see which keys to press. Wrong-key behaviour can be set to **keep or clear** in Settings.

Session stats (accuracy, streak) and **daily aggregates** (kept ~120 days) sync via iCloud when enabled. Open **Practice Report** from the Typing hub or **Settings → Learning Stats** for 7/30-day trend charts and code-length distribution.

### How does the Daily Quiz work?

Each day you receive a configurable number of questions (**5 / 8 / 10 / 15** by default 8). Tap the **gear icon** on the quiz screen to open **Quiz Settings**:

- **Word source** — full dictionary, favorites, or wrong book
- **Code length** — any or 1–5
- **Question types** — toggle character→code, code→character, and first-key questions

Three types rotate when enabled. Card-style options with instant feedback; end-of-round **wrong review** links to word detail. **Reshuffle** for a fresh set. Wrong records feed the Wrong Book and typing retry.

### What is the Newcomer Path and onboarding?

On first launch, a **5-screen onboarding** introduces lookup, learn/quiz, typing, and widgets (skippable). Re-run it anytime from **Settings → App Settings**. In the **Learn** tab, a **Newcomer Path** card offers one-tap links to try lookup, today's quiz, the first tutorial, and the widget guide (iOS). Dismiss the card with ✕ to hide it permanently.

### How do I back up and restore learning data?

Go to **Settings → Learning Stats → Backup & Restore**. **Export JSON** saves favorites, learning status, wrong book, quiz scores, typing stats, daily typing records, and passage progress to a `.icangjie-backup` file. **Import** lets you **merge** with existing data or **replace** local learning data entirely. Backups stay on your device or cloud storage you choose — iHTC Studio never receives them.

### How does Learning Status work?

Every character has one of four statuses: Not Learned, Learning, Learned, or Mastered. Promote or demote manually on the word detail page. The Statistics card in Settings shows your breakdown. Widget **Learning Progress** mirrors these counts.

### How do I read tutorials?

Go to **Learn** for 11 HTML lessons and grouped radical chart images. Adjust **reading size** (85%–160%) in the tutorial toolbar. HTML adapts to light/dark; Traditional script when app language is zh-Hant. Pinch-zoom charts; swipe between images at 1× zoom; save to Photos or share (iOS).

### What is the Pinyin & Cangjie Converter?

Under **Settings → Text Tools → Pinyin & Cangjie Converter**, paste Chinese text and preview multiple output styles (toned, plain, numbered, annotated, aligned grid, and more). Optionally overlay Cangjie codes for your current standard, then copy or share as a preview image.

### How do I set up iCloud sync?

Go to **Settings → iCloud Sync** and toggle it on. Ensure you are signed in to iCloud. Once active, iCangJie syncs favorites, learning status, wrong question book, quiz scores & streak, typing statistics, and built-in passage progress across your devices. You can turn it off at any time.

Typing UI preferences (wrong-key retention, passage pinyin) stay on each device only.

### How do I add and use widgets?

Long-press your Home Screen or Lock Screen, tap **+**, and search for "iCangJie." iCangJie offers **8 widget kinds**: Daily Character (shuffle on small & medium), Code Length (pick 1–5 when adding; **shuffle button** on small & medium to refresh the trio), Daily Quiz, Typing Glance, Favorites, Wrong Book, Recent, and Learning Progress. Favorites / Wrong / Recent show rice-grid previews with codes. Widgets also work in StandBy (iOS 17+). See the in-app **Widget Guide** for step-by-step setup.

### How do I customize themes and language?

Go to **Settings → Theme** for **15 preset gradient themes** or a custom accent color. Character **tile grids follow your theme** accent in list and grid views. Set appearance to system / light / dark. Under **App Settings**, pick **in-app language** (English, Simplified Chinese, Traditional Chinese, or follow system) — the UI refreshes instantly. Widgets mirror language and accent via App Group.

Configure up to **4 Home Screen Quick Actions** under **Settings → App Settings → Home Screen shortcuts**. On iOS, toggle **Spotlight Search** in the same card to index favorites and recent characters in system Spotlight (up to 80 entries, 30-day expiry).

### What are Siri and Shortcuts App Intents?

On iOS 16+, iCangJie registers built-in **App Intents**: look up the Cangjie code for a character, start the daily quiz, and open lookup search. Find them in the **Shortcuts** app or say phrases like *"Look up Cangjie code for 颉 in iCangJie"*. Intents write a pending deep link consumed when the app opens. See the [URL Scheme Reference](url-scheme).

### What are Deep Links and how do I use them?

iCangJie supports the `iCangJie://` URL scheme. Paths include `search`, `word`, `quiz`, `typing`, `favorites`, `wrong`, `levels`, `learn`, `feedback`, and `review`. Use them in Shortcuts, bookmarks, or automations. See the [URL Scheme Reference](url-scheme).

### Does iCangJie work on Mac?

Yes. iCangJie is a native macOS app with transparent navigation chrome, Esc back navigation, system share sheet, and full typing practice. Lookup integrates with the system search bar; tutorial external links open in Safari.

### Does iCangJie work offline?

Yes. The dictionary, quizzes, tutorials, typing practice, and converter tools work offline. Optional iCloud sync uses Apple's iCloud Key-Value Storage. Online lookup (Youdao) and external tutorial links require network.

### Why does iCangJie ask for Photo Library access?

Only when you tap **Save to Photos** on a radical chart image in a tutorial. iCangJie requests **add-only** photo library permission — it never reads your existing photos.

### Does iCangJie collect any personal data?

No. iCangJie does not collect, store, or transmit personal data. There are no analytics, advertising SDKs, or tracking. See the [Privacy Policy](privacy).

### Still need help?

Contact us at [AppleOSer@gmail.com](mailto:AppleOSer@gmail.com) and we will get back to you within 48 hours.

</section>

<section lang="zh-CN" markdown="1">

### 什么是仓颉输入法？

仓颉是由朱邦复先生发明的形码输入法。每个汉字按其字形结构（字根）映射到 24 个字母键上。熟练掌握后，可实现快速、准确的中文打字，无需在同音字中反复选择。

### 仓颉三代和五代有什么区别？

**三代仓颉**是港台广泛使用的经典标准。**五代仓颉**优化了部分编码并扩展了现代用字覆盖。爱仓颉同时内置两套码表——可在 **设置 → 应用设置** 切换默认版本。单字详情页有 **三代/五代并排对照卡**（含字根条）；码卡片与工具栏支持 **一键复制** 汉字或编码。

### 「速成法」是什么？

速成法只取完整仓颉码的 **首码与尾码**（1–2 码）。爱仓颉在 **码长** 支持速成法分桶浏览，打字练习支持速成专练与混合模式（先速成，错误后揭示全码）。

### 查字搜索怎么用？

在 **查字** Tab 输入：

- **仓颉码前缀** — 如 `ab` 匹配以 AB 开头的编码。
- **汉字** — 粘贴或选择单个汉字。
- **拼音前缀** — 无声调拼音（可在设置中开关）。
- **粤拼前缀** — 粤语罗马字。

无结果时会智能提示切换模式。四套 **字集优先级**（香港 / 台湾 / 简体 / 综合）影响排序。

### 打字练习怎么用？

打开 **打字**，选择模式：

- **完整码** — 输入每个字的完整仓颉编码。
- **速成** — 仅练习 1–2 码速成。
- **混合** — 先打速成，错误后揭示并改用全码。

内容来源包括 16 篇简繁内置名篇、随机字表、粘贴文本、收藏与错题本（自动解析单字）。实时 **字根键位高亮** 辅助记忆。错键可设为 **保留或清空**（设置 → 打字练习）。

准确率、连胜与 **按日打字记录**（约 120 天）在开启 iCloud 时可跨设备同步。在打字 Hub 或 **设置 → 学习统计 → 练习报告** 查看 7/30 天曲线与码长分布。

### 每日测验怎么玩？

默认每天 **8 题**，可在测验页点 **齿轮** 打开 **测验设置**：题量 5/8/10/15、字词来源（字典/收藏/错题本）、码长 1–5、题型开关。题型：字→码、码→字、字→首键。完成页 **错题回顾**；**重新出题** 换一批。错题供打字重练。

### 新手引导和新手路径是什么？

首次启动有 **五屏引导**（可跳过，亦可在 **设置 → 应用设置** 重新观看）。**学习** Tab 顶部 **新手路径** 卡片可一键试查字、做测验、读首篇教程、看 Widget 教程（iOS）。点 ✕ 可永久关闭。

### 如何备份和恢复学习数据？

**设置 → 学习统计 → 备份与恢复**。导出 JSON（`.icangjie-backup`）含收藏、学习状态、错题、测验成绩、打字统计与按日记录、篇章进度。导入可选 **合并** 或 **覆盖**。备份文件由你自行保管，我们不会接收。

### 学习状态如何运作？

每个字有四种状态：未学、学习中、已学、已掌握。可在字词详情页手动升降。设置页统计卡片展示进度；**学习进度** 小组件同步显示。

### 教程怎么读？

进入 **学习** 阅读 11 篇 HTML 教程与分组字根图。工具栏可调 **阅读字号**（85%–160%）。HTML 深浅自适应；繁体语言下简转繁。字根图支持捏合缩放、1× 时画廊左右滑、保存相册/分享（iOS）。

### 拼音/仓颉转换器是什么？

在 **设置 → 文本转换工具 → 拼音/仓颉转换器** 粘贴中文，可预览多种拼音格式，并可同时显示当前仓颉版本的编码，支持复制或预览长图分享。

### 如何设置 iCloud 同步？

进入 **设置 → iCloud 同步** 并开启，确保设备已登录 iCloud。开启后会同步收藏、学习状态、错题本、测验成绩与连胜、打字统计、内置文章进度。可随时关闭。

打字界面偏好（错键保留、篇章拼音）仅保存在本机。

### 如何添加和使用小组件？

长按主屏幕或锁屏，点 **+**，搜索「爱仓颉」或「iCangJie」。提供 **8 款小组件**：今日一字（小/中尺寸可换字）、码长精选（添加时选 1–5 码，**小/中尺寸换一组**）、每日测验、打字一览、收藏、错题、最近浏览、学习进度。收藏/错题/最近以米字格网格预览。待机模式（iOS 17+）同样可用。详见应用内 **Widget 教程**。

### 如何自定义主题和语言？

**设置 → 主题** 选择 **15 套主题预设** 或自定义主色；列表/网格中的 **米字格跟随主题色**。设置浅色/深色/跟随系统。在 **应用设置** 选择 **应用内语言**（英文 / 简体 / 繁体 / 跟随系统），界面即时刷新。小组件经 App Group 同步语言与主题色。

在 **应用设置 → 主屏快捷操作** 中自选最多 4 项。同卡片可开关 **Spotlight 搜索**，将收藏与最近浏览写入系统 Spotlight（最多 80 条）。

### Siri 和快捷指令 App Intents 是什么？

iOS 16+ 内置 **App Intents**：查某字仓颉码、开始今日测验、打开查字。在快捷指令 App 中添加，或对 Siri 说「在爱仓颉查 颉 的仓颉码」等。详见 [URL Scheme 文档](url-scheme)。

### 什么是 Deep Link，如何使用？

爱仓颉支持 `iCangJie://` 深度链接，路径包括 `search`、`word`、`quiz`、`typing`、`favorites`、`wrong`、`levels`、`learn`、`feedback`、`review`。可在快捷指令、书签或自动化中使用。详见 [URL Scheme 文档](url-scheme)。

### Mac 版有什么特色？

爱仓颉提供原生 macOS 版本：透明导航栏、Esc 返回、系统分享、完整打字练习；教程外链系统浏览器打开。

### 爱仓颉能离线使用吗？

可以。字典、测验、教程、打字与转换工具均可离线。可选 iCloud 通过 Apple 键值存储同步。有道在线查词与教程外链需联网。

### 为什么需要相册权限？

仅在教程字根图点击 **保存到相册** 时请求，且为 **仅添加** 权限——不会读取你已有的照片。

### 爱仓颉会收集个人数据吗？

不会。无统计、广告 SDK 或追踪。详见 [隐私政策](privacy)。

### 仍需帮助？

发邮件到 [AppleOSer@gmail.com](mailto:AppleOSer@gmail.com)，我们会在 48 小时内回复。

</section>

<section lang="zh-TW" markdown="1">

### 什麼是倉頡輸入法？

倉頡是由朱邦復先生發明的形碼輸入法。每個漢字依字形結構（字根）映射到 24 個字母鍵上。熟練掌握後，可實現快速、準確的中文打字，無需在同音字中反覆選擇。

### 倉頡三代和五代有什麼區別？

**三代倉頡**是港台廣泛使用的經典標準。**五代倉頡**優化了部分編碼並擴展了現代用字覆蓋。單字詳情有 **三代/五代並排對照**；支援 **一鍵複製** 漢字或編碼。

### 「速成法」是什麼？

速成法只取完整倉頡碼的 **首碼與尾碼**（1–2 碼）。愛倉頡在 **碼長** 支援速成法分桶瀏覽，打字練習支援速成專練與混合模式。

### 查字搜尋怎麼用？

在 **查字** 分頁輸入倉颉碼前綴、漢字、拼音前綴或粵拼前綴。無結果時會智能提示切換模式。四套字集優先順序影響排序。

### 打字練習怎麼用？

三種模式：完整碼、速成、混合。內容來源包括 16 篇簡繁名篇、隨機字表、貼上文字、收藏與錯題本。即時字根高亮；錯鍵可保留或清空。

### 每日測驗怎麼玩？

題量 5–15、來源、碼長、題型可於 **測驗設定** 調整；齒輪圖示開啟設定。可重新出題。

### 新手引導與新手路徑？

首次 **五屏引導**（可於 **設定 → 應用設定** 重新觀看）；學習 Tab **新手路徑** 一鍵入門；可關閉。

### 如何備份與恢復？

**設定 → 學習統計 → 備份與恢復**；JSON 匯出/匯入，合併或覆蓋。

### 練習報告在哪裡？

打字 Hub 或 **設定 → 學習統計 → 練習報告**；7/30 天曲線與碼長分佈。

### 學習狀態如何運作？

未學 / 學習中 / 已學 / 已掌握；字詞詳情手動升降。

### 教程怎麼讀？

11 篇 HTML + 字根圖；可調字號；簡轉繁；畫廊；儲存/分享。

### 如何設定 iCloud 同步？

進入 **設定 → iCloud 同步** 並開啟，確保裝置已登入 iCloud。開啟後會同步收藏、學習狀態、錯題本、測驗成績與連勝、打字統計、內建文章進度與按日打字記錄。可隨時關閉。

打字介面偏好（錯鍵保留、篇章拼音）僅保存在本機。

### 如何新增小工具？

長按主畫面或鎖定畫面，點 **+**，搜尋「愛倉頡」或「iCangJie」。提供 **8 款小工具**：每日一字（小/中尺寸可換字）、碼長精選（新增時選 1–5 碼，**小/中尺寸換一組**）、每日測驗、打字一覽、收藏、錯題、最近瀏覽、學習進度。收藏/錯題/最近以米字格網格預覽。待機模式（iOS 17+）同樣可用。詳見應用內 **小工具教學**。

### 如何自訂主題與語言？

**設定 → 主題** 選擇 **15 套主題預設** 或自訂主色；列表/網格中的 **米字格跟隨主題色**。在 **應用設定** 選擇應用內語言，介面即時刷新。小工具經 App Group 同步語言與主題色。

### Siri 與捷徑？

內建 App Intents：查倉頡碼、開始測驗、開啟查字。詳見 [URL Scheme 文件](url-scheme)。

### Spotlight 索引？

**設定 → 主屏快捷操作** 卡片內開關；索引收藏與最近瀏覽。

### 什麼是 Deep Link？

支援 `iCangJie://` 深度連結。詳見 [URL Scheme 文件](url-scheme)。

### Mac 版有什麼特色？

愛倉頡提供原生 macOS 版本：透明導覽列、Esc 返回、系統分享、完整打字練習；教程外鏈系統瀏覽器開啟。

### 愛倉頡能離線使用嗎？

可以。字典、測驗、教程、打字與轉換工具均可離線。可選 iCloud 透過 Apple 鍵值儲存同步。有道線上查詞與教程外鏈需連網。

### 為什麼需要相簿權限？

僅在儲存字根圖時請求 **僅新增** 權限。

### 愛倉頡會收集個人資料嗎？

不會。詳見 [隱私政策](privacy)。

### 仍需協助？

寄信到 [AppleOSer@gmail.com](mailto:AppleOSer@gmail.com)，我們會在 48 小時內回覆。

</section>
