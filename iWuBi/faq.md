---
layout: doc
title: iWuBi — FAQ
app_id: iWuBi
doc_title_en: Frequently Asked Questions
doc_title_zh_cn: 常见问题
doc_title_zh_tw: 常見問題
description: Frequently asked questions about iWuBi.
---

<section lang="en" markdown="1">

### What is Wubi input method?

Wubi (五笔) is a shape-based Chinese input method that encodes characters by their structural components (roots) rather than pronunciation. Each character maps to a sequence of 1–4 letter keys. Once mastered, Wubi allows extremely fast and accurate Chinese typing without needing to select from homophones.

### What is the difference between the 86, 98, and New Century versions?

The 86-version (王码五笔86版) was published in 1986 and is the most widely used standard. The 98-version (王码五笔98版) was revised in 1998 with an updated root layout and improved encoding for some characters. The New Century version (新世纪五笔) is the latest revision with further optimized roots and encoding. iWuBi supports all three standards — you can switch between them in Settings and compare encodings side by side.

### What is the onboarding flow?

On first launch, iWuBi shows a **5-screen onboarding** introducing lookup, levels, typing, quiz, and widgets. You can skip at any time. Revisit tutorials from the **Learn** tab anytime.

### How does Typing Practice work?

Open the **Typing** tab and choose a mode:

- **Full code** — type the longest Wubi code for each character.
- **Level code** — practice codes at levels 1–4 you select.
- **Mixed** — try the level code first; after a mistake, the app reveals and switches to full code.

Content sources include pasted text, random characters (with a configurable **character count**), 14 built-in passages, generated word lists, favorites, and your wrong-book. During practice you can use **Hint**, **Reveal**, and **Skip**. An optional on-screen radical keyboard is available; on iOS you can hide it temporarily and use the system or hardware keyboard instead.

**Keyboard tips:**

- **iOS / iPad:** Space shows a hint; Return confirms; Backspace deletes. Reveal and Skip use on-screen buttons.
- **Mac:** Space or `1` hints; `2` reveals; `3` skips; Return confirms; Backspace / Delete deletes.

Full input auto-submits at up to 4 keys. Session stats (accuracy, streak, sessions) and built-in passage progress sync via iCloud when enabled.

### How does Pinyin Search work?

In **Lookup**, when you type letters only, iWuBi can switch between **code** and **pinyin** search modes (toggle in **Settings → App Settings → Pinyin Search**). Pinyin mode matches single characters by toneless pinyin prefix. A background index is built on first use.

### What is the Pinyin Converter?

Under **Settings → Text Tools → Pinyin Converter**, paste Chinese text and preview multiple output styles (toned, toneless, numeric tone, Bopomofo, two-line, aligned grid, and more). You can optionally overlay Wubi codes for your current standard, then copy or share as a long image.

### How does the Daily Quiz work?

Each day you receive 8 quiz questions drawn from three question types: given a character, type its Wubi code; given a Wubi code, identify the character; and given a character, identify the root key it belongs to. Incorrect answers are automatically added to your Wrong Question Book for later review. Your best score and daily streak are recorded and synced via iCloud.

### How does Learning Status work?

Every character in the library has one of four learning statuses: Not Learned, Learning, Learned, or Mastered. As you look up, quiz, and interact with characters, you can manually promote or demote their status. The Statistics view shows your progress breakdown across all levels and Wubi versions.

### How do I set up iCloud sync?

Go to **Settings → iCloud Sync** and toggle it on or off. **iCloud sync is on by default for new users.** Make sure you are signed in to iCloud on your device. Once active, iWuBi syncs favorites, learning status, wrong question book, best quiz score, streak, **typing statistics**, and **built-in passage progress** across your devices.

Typing UI preferences (virtual keyboard, passage pinyin, wrong-key retention) stay on each device only.

### How do I add and use widgets?

Long-press your Home Screen or Lock Screen, tap **+**, and search for "iWuBi." iWuBi offers **8 widget kinds**: Daily Character (with shuffle button), Level Spotlight, Daily Quiz, **Typing Glance**, Favorites, Wrong Book, Recent, and Learning Progress. Favorites and Wrong Book widgets show a character grid with Wubi codes on small and medium sizes. Widgets also work in StandBy (iOS 17+). Data is shared via an on-device App Group container.

### How do I customize themes and app icons?

Go to **Settings → Theme** for 16 built-in themes or a custom accent color. On **iOS**, go to **Settings → App Settings → App Icon** for 8 alternate icons. Language, default Wubi version, pinyin display, and pinyin search are also under **App Settings**.

### What are Deep Links and how do I use them?

iWuBi supports the `iWuBi://` URL scheme. Paths include `search`, `word`, `quiz`, `favorites`, `wrong`, `levels`, `learn`, and **`typing`**. Use them in Shortcuts, bookmarks, or widgets to jump directly into a feature. See the [URL Scheme Reference](url-scheme).

### How does the tip jar work?

iWuBi offers optional tips via **StoreKit 2** in Settings. All payment processing is handled entirely by Apple. We do not receive or store any financial information.

### Does iWuBi work on Mac?

Yes. iWuBi is a native macOS app with an inline Lookup search bar, Esc back navigation, a floating in-app browser for tutorial links, system dictionary cards, system share sheet, and full typing practice with Mac keyboard shortcuts.

### Does iWuBi work offline?

Yes. The word library, quizzes, tutorials, typing practice, and pinyin tools work offline. iCloud sync is optional and uses Apple's iCloud Key-Value Storage when enabled.

### Does iWuBi collect any personal data?

No. iWuBi does not collect, store, or transmit personal data. There are no analytics, advertising SDKs, or tracking. See the [Privacy Policy](privacy).

### Still need help?

Contact us at [AppleOSer@gmail.com](mailto:AppleOSer@gmail.com) and we will get back to you within 48 hours.

</section>

<section lang="zh-CN" markdown="1">

### 什么是五笔输入法？

五笔是一种形码输入法，按字形结构（字根）编码，而不是按发音。每个汉字对应 1–4 个字母键。熟练掌握后，五笔可以实现极快且准确的中文打字，无需在同音字中反复选择。

### 86 版、98 版和新世纪版五笔有什么区别？

86 版（王码五笔86版）发布于 1986 年，是目前使用最广泛的标准。98 版（王码五笔98版）于 1998 年修订，更新了字根布局并改进了部分字的编码。新世纪版（新世纪五笔）是最新修订版，进一步优化了字根和编码。爱五笔同时支持三种标准——可在设置中切换，并对比编码。

### 首次引导是什么？

首次启动会显示 **五屏引导**，介绍查字、简码、打字、测验与小组件，可随时跳过。教程仍可在 **学习** Tab 中访问。

### 打字练习怎么用？

打开 **打字** Tab，选择练习模式：

- **看字打全码** — 输入每个字的最长五笔编码。
- **简码专练** — 按所选 1–4 级简码长度练习。
- **简码优先** — 先打简码，错误后揭示并改用全码。

内容来源包括粘贴文本、随机抽字（可设置 **抽字数量**）、14 篇内置文章、按级别生成字表、收藏与错题本。练习中可使用 **提示**、**看答案**、**跳过**；可选字根虚拟键盘。iOS 上可临时隐藏字根键盘，改用系统键盘或外接键盘。

**键盘技巧：**

- **iOS / iPad：** 按 **空格** 显示提示；回车确认；退格删除。看答案与跳过请点屏幕按钮。
- **Mac：** 空格或数字 **1** 提示；**2** 看答案；**3** 跳过；回车确认；退格或 Delete 删除。

满四码自动提交。准确率、连胜、场次与内置文章进度在开启 iCloud 时可跨设备同步。

### 查字拼音搜索怎么用？

在 **查字** 中纯字母输入时，可在 **编码 / 拼音** 两种模式间切换（**设置 → 应用设置 → 查字拼音搜索**）。拼音模式按无声调拼音前缀匹配单字，首次使用会在后台建立索引。

### 拼音转换器是什么？

在 **设置 → 文本转换工具 → 文字转拼音、五笔编码** 中粘贴中文，可预览多种拼音格式（带调、无声调、数字调、注音、双行、对齐网格等），并可同时显示当前五笔版本的编码，支持复制或长图分享。

### 每日测验怎么玩？

每天 8 道题，题型共三种：给汉字写编码、给编码选汉字、给汉字选字根所在键。答错的题目会自动加入错题本。最佳成绩和连续天数会记录并通过 iCloud 同步。

### 学习状态如何运作？

字词库中的每个汉字都有四种学习状态：未学、学习中、已学、已掌握。你可以在查阅、测验和互动过程中手动升降状态。统计视图按级别和五笔版本展示进度。

### 如何设置 iCloud 同步？

进入 **设置 → iCloud 同步** 开关即可。**新用户默认开启。** 确保设备已登录 iCloud。开启后会同步收藏、学习状态、错题本、测验最佳分、连胜、**打字统计**与**内置文章进度**。

打字界面偏好（字根键盘、篇章拼音、输错保留策略）仅保存在本机。

### 如何添加和使用小组件？

长按主屏幕或锁屏，点 **+**，搜索「iWuBi」。爱五笔提供 **8 款小组件**：每日一字（支持换字按钮）、简码精选、每日测验、**打字一览**、收藏、错题本、最近浏览、学习进度。收藏与错题在中尺寸与小尺寸以网格显示字词与编码。待机模式（iOS 17+）同样可用。数据通过本机 App Group 共享。

### 如何自定义主题和应用图标？

**设置 → 主题** 选择 16 款内置主题或自定义主色。**iOS** 在 **设置 → 应用设置 → 应用图标** 更换 8 款备用图标。语言、默认五笔、显示拼音、查字拼音搜索等也在应用设置中。

### 什么是 Deep Link，如何使用？

爱五笔支持 `iWuBi://` 深度链接，路径包括 `search`、`word`、`quiz`、`favorites`、`wrong`、`levels`、`learn`、**`typing`**。可在快捷指令、书签或自动化中使用。详见 [URL Scheme 说明](url-scheme)。

### 打赏功能如何使用？

爱五笔在设置中通过 **StoreKit 2** 提供可选打赏，所有支付由 Apple 处理，我们不接收或存储任何财务信息。

### Mac 版有什么特色？

爱五笔提供原生 macOS 版本：查字独立搜索栏、Esc 回退、浮动内嵌浏览器、系统词典卡片、系统分享面板，以及完整打字练习与 Mac 专属键盘快捷键。

### 爱五笔能离线使用吗？

可以。字库、测验、教程、打字练习与拼音工具均可离线使用。iCloud 同步为可选项，启用后通过 Apple iCloud 键值存储同步。

### 爱五笔会收集个人数据吗？

不会。爱五笔不收集、存储或传输个人数据，没有统计分析、广告 SDK 或追踪。详见 [隐私政策](privacy)。

### 仍需帮助？

发邮件到 [AppleOSer@gmail.com](mailto:AppleOSer@gmail.com)，我们会在 48 小时内回复。

</section>

<section lang="zh-TW" markdown="1">

### 什麼是五筆輸入法？

五筆是一種形碼輸入法，按字形結構（字根）編碼，而不是按發音。每個漢字對應 1–4 個字母鍵。熟練掌握後，五筆可以實現極快且準確的中文打字，無需在同音字中反覆選擇。

### 86 版、98 版和新世紀版五筆有什麼區別？

86 版（王碼五筆86版）發佈於 1986 年，是目前使用最廣泛的標準。98 版（王碼五筆98版）於 1998 年修訂，更新了字根佈局並改進了部分字的編碼。新世紀版（新世紀五筆）是最新修訂版，進一步優化了字根和編碼。愛五筆同時支援三種標準——可在設定中切換，並對比編碼。

### 首次引導是什麼？

首次啟動會顯示 **五屏引導**，介紹查字、簡碼、打字、測驗與小工具，可隨時跳過。教程仍可在 **學習** 分頁中存取。

### 打字練習怎麼用？

開啟 **打字** 分頁，選擇練習模式：

- **看字打全碼** — 輸入每個字的最長五筆編碼。
- **簡碼專練** — 依所選 1–4 級簡碼長度練習。
- **簡碼優先** — 先打簡碼，錯誤後揭示並改用全碼。

內容來源包括貼上文字、隨機抽字（可設定 **抽字數量**）、14 篇內建文章、依級別產生字表、收藏與錯題本。練習中可使用 **提示**、**看答案**、**跳過**；可選字根虛擬鍵盤。iOS 上可暫時隱藏字根鍵盤，改用系統鍵盤或外接鍵盤。

**鍵盤技巧：**

- **iOS / iPad：** 按 **空白鍵** 顯示提示；Return 確認；Backspace 刪除。看答案與跳過請點螢幕按鈕。
- **Mac：** 空白鍵或數字 **1** 提示；**2** 看答案；**3** 跳過；Return 確認；Backspace 或 Delete 刪除。

滿四碼自動提交。準確率、連勝、場次與內建文章進度在開啟 iCloud 時可跨裝置同步。

### 查字拼音搜尋怎麼用？

在 **查字** 中純字母輸入時，可在 **編碼 / 拼音** 兩種模式間切換（**設定 → 應用設定 → 查字拼音搜尋**）。拼音模式依無聲調拼音前綴比對單字，首次使用會在背景建立索引。

### 拼音轉換器是什麼？

在 **設定 → 文字轉換工具 → 文字轉拼音、五筆編碼** 中貼上中文，可預覽多種拼音格式（帶調、無聲調、數字調、注音、雙行、對齊網格等），並可同時顯示目前五筆版本的編碼，支援複製或長圖分享。

### 每日測驗怎麼玩？

每天 8 道題，題型共三種：給漢字寫編碼、給編碼選漢字、給漢字選字根所在鍵。答錯的題目會自動加入錯題本。最佳成績和連續天數會記錄並透過 iCloud 同步。

### 學習狀態如何運作？

字詞庫中的每個漢字都有四種學習狀態：未學、學習中、已學、已掌握。你可以在查閱、測驗和互動過程中手動升降狀態。統計檢視依級別和五筆版本展示進度。

### 如何設定 iCloud 同步？

進入 **設定 → iCloud 同步** 開關即可。**新使用者預設開啟。** 確保裝置已登入 iCloud。開啟後會同步收藏、學習狀態、錯題本、測驗最佳分、連勝、**打字統計**與**內建文章進度**。

打字介面偏好（字根鍵盤、篇章拼音、輸錯保留策略）僅保存在本機。

### 如何新增和使用小工具？

長按主畫面或鎖定畫面，點 **+**，搜尋「iWuBi」。愛五筆提供 **8 款小工具**：每日一字（支援換字按鈕）、簡碼精選、每日測驗、**打字一覽**、收藏、錯題本、最近瀏覽、學習進度。收藏與錯題在中尺寸與小尺寸以網格顯示字詞與編碼。待機模式（iOS 17+）同樣可用。資料透過本機 App Group 共享。

### 如何自訂主題和應用圖示？

**設定 → 主題** 選擇 16 套內建主題或自訂主色。**iOS** 在 **設定 → 應用設定 → 應用圖示** 更換 8 款備用圖示。語言、預設五筆、顯示拼音、查字拼音搜尋等也在應用設定中。

### 什麼是 Deep Link，如何使用？

愛五筆支援 `iWuBi://` 深度連結，路徑包括 `search`、`word`、`quiz`、`favorites`、`wrong`、`levels`、`learn`、**`typing`**。可在捷徑、書籤或自動化中使用。詳見 [URL Scheme 說明](url-scheme)。

### 打賞功能如何使用？

愛五筆在設定中透過 **StoreKit 2** 提供可選打賞，所有付款由 Apple 處理，我們不接收或儲存任何財務資訊。

### Mac 版有什麼特色？

愛五筆提供原生 macOS 版本：查字獨立搜尋列、Esc 返回、浮動內嵌瀏覽器、系統辭典卡片、系統分享面板，以及完整打字練習與 Mac 專屬鍵盤快速鍵。

### 愛五筆能離線使用嗎？

可以。字庫、測驗、教程、打字練習與拼音工具均可離線使用。iCloud 同步為可選項，啟用後透過 Apple iCloud 鍵值儲存同步。

### 愛五筆會收集個人資料嗎？

不會。愛五筆不收集、儲存或傳送個人資料，沒有統計分析、廣告 SDK 或追蹤。詳見 [隱私政策](privacy)。

### 仍需協助？

寄信到 [AppleOSer@gmail.com](mailto:AppleOSer@gmail.com)，我們會在 48 小時內回覆。

</section>
