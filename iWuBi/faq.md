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

iWuBi supports the `iWuBi://` URL scheme. Paths include `search`, `word`, `quiz`, `favorites`, `wrong`, `levels`, `learn`, and **`typing`**. Use them in Shortcuts, bookmarks, or widgets to jump directly into a feature. See the [URL Scheme Reference](../url-scheme).

### How does the tip jar work?

iWuBi offers optional tips via **StoreKit 2** in Settings. All payment processing is handled entirely by Apple. We do not receive or store any financial information.

### Does iWuBi work on Mac?

Yes. iWuBi is a native macOS app with an inline Lookup search bar, Esc back navigation, a floating in-app browser for tutorial links, system dictionary cards, system share sheet, and full typing practice with Mac keyboard shortcuts.

### Does iWuBi work offline?

Yes. The word library, quizzes, tutorials, typing practice, and pinyin tools work offline. iCloud sync is optional and uses Apple's iCloud Key-Value Storage when enabled.

### Does iWuBi collect any personal data?

No. iWuBi does not collect, store, or transmit personal data. There are no analytics, advertising SDKs, or tracking. See the [Privacy Policy](../privacy).

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

爱五笔支持 `iWuBi://` 深度链接，路径包括 `search`、`word`、`quiz`、`favorites`、`wrong`、`levels`、`learn`、**`typing`**。可在快捷指令、书签或自动化中使用。详见 [URL Scheme 说明](../url-scheme)。

### 打赏功能如何使用？

爱五笔在设置中通过 **StoreKit 2** 提供可选打赏，所有支付由 Apple 处理，我们不接收或存储任何财务信息。

### Mac 版有什么特色？

爱五笔提供原生 macOS 版本：查字独立搜索栏、Esc 回退、浮动内嵌浏览器、系统词典卡片、系统分享面板，以及完整打字练习与 Mac 专属键盘快捷键。

### 爱五笔能离线使用吗？

可以。字库、测验、教程、打字练习与拼音工具均可离线使用。iCloud 同步为可选项，启用后通过 Apple iCloud 键值存储同步。

### 爱五笔会收集个人数据吗？

不会。爱五笔不收集、存储或传输个人数据，没有统计分析、广告 SDK 或追踪。详见 [隐私政策](../privacy)。

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

愛五筆支援 `iWuBi://` 深度連結，路徑包括 `search`、`word`、`quiz`、`favorites`、`wrong`、`levels`、`learn`、**`typing`**。可在捷徑、書籤或自動化中使用。詳見 [URL Scheme 說明](../url-scheme)。

### 打賞功能如何使用？

愛五筆在設定中透過 **StoreKit 2** 提供可選打賞，所有付款由 Apple 處理，我們不接收或儲存任何財務資訊。

### Mac 版有什麼特色？

愛五筆提供原生 macOS 版本：查字獨立搜尋列、Esc 返回、浮動內嵌瀏覽器、系統辭典卡片、系統分享面板，以及完整打字練習與 Mac 專屬鍵盤快速鍵。

### 愛五筆能離線使用嗎？

可以。字庫、測驗、教程、打字練習與拼音工具均可離線使用。iCloud 同步為可選項，啟用後透過 Apple iCloud 鍵值儲存同步。

### 愛五筆會收集個人資料嗎？

不會。愛五筆不收集、儲存或傳送個人資料，沒有統計分析、廣告 SDK 或追蹤。詳見 [隱私政策](../privacy)。

### 仍需協助？

寄信到 [AppleOSer@gmail.com](mailto:AppleOSer@gmail.com)，我們會在 48 小時內回覆。

</section>
<section lang="ja" markdown="1">

### 五筆字型入力とは？

五筆（五笔）は、発音ではなく文字の構造的な部品（字根）で漢字をコード化する、字形ベースの中国語入力方式です。各文字は 1〜4 個のアルファベットキーの並びに対応します。習熟すれば、同音字から選ぶ必要がなく、きわめて高速かつ正確に中国語を入力できます。

### 86 版、98 版、新世紀版の違いは？

86 版（王码五笔86版）は 1986 年に公開された、最も広く使われている標準です。98 版（王码五笔98版）は 1998 年に改訂され、字根配置の更新と一部の文字のコード改善が行われました。新世紀版（新世纪五笔）は最新の改訂版で、字根とコードがさらに最適化されています。iWuBi は 3 つの標準すべてに対応しており、設定で切り替えて、コードを並べて比較できます。

### オンボーディングの流れは？

初回起動時、iWuBi は検索、レベル、タイピング、クイズ、ウィジェットを紹介する **5 画面のオンボーディング**を表示します。いつでもスキップできます。チュートリアルは**学習**タブからいつでも見直せます。

### タイピング練習の仕組みは？

**タイピング**タブを開き、モードを選びます。

- **フルコード** — 各文字の最長の五筆コードを入力します。
- **レベルコード** — 選択したレベル 1〜4 のコードを練習します。
- **ミックス** — まずレベルコードを試し、間違えるとアプリが答えを表示してフルコードに切り替わります。

コンテンツの出典は、貼り付けたテキスト、ランダムな文字（設定可能な**文字数**）、14 本の内蔵文章、生成された単語リスト、お気に入り、間違い帳です。練習中は**ヒント**、**答えを見る**、**スキップ**が使えます。任意の画面字根キーボードがあり、iOS では一時的に非表示にして、システムキーボードまたはハードウェアキーボードを使うこともできます。

**キーボードのヒント：**

- **iOS / iPad：** スペースでヒントを表示、リターンで確定、バックスペースで削除。答えの表示とスキップは画面上のボタンを使います。
- **Mac：** スペースまたは `1` でヒント、`2` で答えを表示、`3` でスキップ、リターンで確定、Backspace / Delete で削除。

フルコードは最大 4 キーで自動送信されます。セッション統計（正答率、連続記録、セッション数）と内蔵文章の進捗は、有効にしている場合 iCloud で同期されます。

### ピンイン検索の仕組みは？

**検索**でアルファベットのみを入力すると、iWuBi は**コード**検索と**ピンイン**検索を切り替えられます（**設定 → アプリ設定 → ピンイン検索**で切り替え）。ピンインモードでは、声調なしのピンインの前方一致で単一の文字を検索します。バックグラウンドのインデックスは初回使用時に作成されます。

### ピンイン変換とは？

**設定 → テキストツール → ピンイン変換**で、中国語のテキストを貼り付けると、複数の出力スタイル（声調付き、声調なし、数字声調、注音符号、2 行、整列グリッドなど）をプレビューできます。現在の標準の五筆コードを重ねて表示することもでき、コピーや長い画像としての共有が可能です。

### デイリークイズの仕組みは？

毎日 8 問のクイズが出題されます。出題形式は 3 種類で、文字が示されて五筆コードを入力する、五筆コードが示されて文字を答える、文字が示されてそれが属する字根キーを答える、です。間違えた回答は自動的に間違い帳に追加され、後で復習できます。ベストスコアと連続日数は記録され、iCloud で同期されます。

### 学習状況の仕組みは？

ライブラリのすべての文字には、未学習、学習中、学習済み、習得済みの 4 つの学習状況のいずれかが設定されます。検索、クイズ、文字の操作を行いながら、手動で状況を上げ下げできます。統計画面では、すべてのレベルと五筆バージョンにわたる進捗の内訳を確認できます。

### iCloud 同期を設定するには？

**設定 → iCloud 同期**に移動して、オン/オフを切り替えます。**新規ユーザーでは iCloud 同期が既定でオンです。** デバイスで iCloud にサインインしていることを確認してください。有効になると、iWuBi はお気に入り、学習状況、間違い帳、クイズのベストスコア、連続記録、**タイピング統計**、**内蔵文章の進捗**をデバイス間で同期します。

タイピング UI の設定（仮想キーボード、文章のピンイン、ミスキーの保持）は、各デバイスにのみ保存されます。

### ウィジェットの追加と使い方は？

ホーム画面またはロック画面を長押しし、**+** をタップして「iWuBi」を検索します。iWuBi は **8 種類のウィジェット**を提供しています。Daily Character（シャッフルボタン付き）、Level Spotlight、Daily Quiz、**Typing Glance**、Favorites、Wrong Book、Recent、Learning Progress です。Favorites と Wrong Book のウィジェットは、スモールとミディアムのサイズで五筆コード付きの文字グリッドを表示します。ウィジェットは StandBy（iOS 17 以降）でも動作します。データは端末内の App Group コンテナで共有されます。

### テーマとアプリアイコンをカスタマイズするには？

**設定 → テーマ**で、16 種類の内蔵テーマまたはカスタムのアクセントカラーを選べます。**iOS** では、**設定 → アプリ設定 → アプリアイコン**で 8 種類の代替アイコンを選べます。言語、既定の五筆バージョン、ピンイン表示、ピンイン検索も**アプリ設定**にあります。

### ディープリンクとは何で、どう使いますか？

iWuBi は `iWuBi://` URL スキームに対応しています。パスは `search`、`word`、`quiz`、`favorites`、`wrong`、`levels`、`learn`、**`typing`** です。ショートカット、ブックマーク、ウィジェットで利用すると、機能に直接ジャンプできます。[URL スキームリファレンス](../url-scheme)をご覧ください。

### 投げ銭の仕組みは？

iWuBi は、設定から **StoreKit 2** による任意の投げ銭を用意しています。決済処理はすべて Apple が行います。当社は金融情報を受け取ったり保存したりすることはありません。

### iWuBi は Mac で動作しますか？

はい。iWuBi はネイティブの macOS アプリで、インライン検索バー、Esc で戻る操作、チュートリアルリンク用のフローティング内蔵ブラウザ、システム辞書カード、システムの共有シート、Mac のキーボードショートカットに対応した本格的なタイピング練習を備えています。

### iWuBi はオフラインで動作しますか？

はい。単語ライブラリ、クイズ、チュートリアル、タイピング練習、ピンインツールはオフラインで動作します。iCloud 同期は任意で、有効にすると Apple の iCloud キーバリューストレージを使用します。

### iWuBi は個人データを収集しますか？

いいえ。iWuBi は個人データを収集、保存、送信しません。分析、広告 SDK、トラッキングはありません。[プライバシーポリシー](../privacy)をご覧ください。

### まだ解決しませんか？

[AppleOSer@gmail.com](mailto:AppleOSer@gmail.com) までご連絡ください。48 時間以内にご返信します。

</section>
<section lang="ko" markdown="1">

### 오필(五笔) 입력법이란 무엇인가요?

오필(五笔)은 발음이 아니라 글자의 구조적 구성 요소(자근)로 한자를 코딩하는 자형 기반 중국어 입력 방식입니다. 각 글자는 1~4개의 알파벳 키 시퀀스에 대응합니다. 익히고 나면 동음자 중에서 고를 필요 없이 매우 빠르고 정확하게 중국어를 입력할 수 있습니다.

### 86 버전, 98 버전, 새 세기 버전의 차이는 무엇인가요?

86 버전(王码五笔86版)은 1986년에 공개된 가장 널리 쓰이는 표준입니다. 98 버전(王码五笔98版)은 1998년에 자근 배치를 갱신하고 일부 글자의 코드를 개선해 개정되었습니다. 새 세기 버전(新世纪五笔)은 자근과 코드를 더욱 최적화한 최신 개정판입니다. iWuBi는 세 가지 표준을 모두 지원하며, 설정에서 전환해 코드를 나란히 비교할 수 있습니다.

### 온보딩은 어떻게 진행되나요?

처음 실행하면 iWuBi가 조회, 레벨, 타이핑, 퀴즈, 위젯을 소개하는 **5화면 온보딩**을 보여 줍니다. 언제든 건너뛸 수 있으며, **학습** 탭에서 튜토리얼을 언제든 다시 볼 수 있습니다.

### 타이핑 연습은 어떻게 작동하나요?

**타이핑** 탭을 열고 모드를 선택하세요.

- **전체 코드** — 각 글자의 가장 긴 오필 코드를 입력합니다.
- **레벨 코드** — 선택한 1~4레벨의 코드를 연습합니다.
- **혼합** — 먼저 레벨 코드를 시도하고, 틀리면 앱이 정답을 보여 주고 전체 코드로 전환합니다.

콘텐츠 출처는 붙여넣은 텍스트, 무작위 글자(설정 가능한 **글자 수**), 14개의 내장 글, 생성된 단어 목록, 즐겨찾기, 오답 노트입니다. 연습 중에는 **힌트**, **정답 보기**, **건너뛰기**를 사용할 수 있습니다. 선택형 화면 자근 키보드가 있으며, iOS에서는 일시적으로 숨기고 시스템 또는 하드웨어 키보드를 사용할 수 있습니다.

**키보드 팁:**

- **iOS / iPad:** 스페이스는 힌트 표시, 리턴은 확인, 백스페이스는 삭제. 정답 보기와 건너뛰기는 화면 버튼을 사용합니다.
- **Mac:** 스페이스 또는 `1`은 힌트, `2`는 정답 보기, `3`은 건너뛰기, 리턴은 확인, Backspace / Delete는 삭제.

전체 입력은 최대 4키에서 자동 제출됩니다. 세션 통계(정확도, 연속 기록, 세션 수)와 내장 글 진행 상황은 켜져 있으면 iCloud로 동기화됩니다.

### 병음 검색은 어떻게 작동하나요?

**조회**에서 알파벳만 입력하면 iWuBi가 **코드** 검색과 **병음** 검색 모드를 전환할 수 있습니다(**설정 → 앱 설정 → 병음 검색**에서 전환). 병음 모드는 성조 없는 병음 접두사로 단일 글자를 찾습니다. 백그라운드 색인은 처음 사용할 때 만들어집니다.

### 병음 변환기란 무엇인가요?

**설정 → 텍스트 도구 → 병음 변환기**에서 중국어 텍스트를 붙여넣으면 여러 출력 스타일(성조 포함, 성조 없음, 숫자 성조, 주음부호, 두 줄, 정렬 그리드 등)을 미리 볼 수 있습니다. 현재 표준의 오필 코드를 겹쳐 표시할 수도 있고, 복사하거나 긴 이미지로 공유할 수 있습니다.

### 일일 퀴즈는 어떻게 진행되나요?

매일 8개의 퀴즈 문제가 출제됩니다. 문제 유형은 세 가지로, 글자가 주어지면 오필 코드를 입력하기, 오필 코드가 주어지면 글자 고르기, 글자가 주어지면 그 글자가 속한 자근 키 고르기입니다. 틀린 답은 나중에 복습할 수 있도록 자동으로 오답 노트에 추가됩니다. 최고 점수와 연속 일수는 기록되어 iCloud로 동기화됩니다.

### 학습 상태는 어떻게 작동하나요?

라이브러리의 모든 글자에는 미학습, 학습 중, 학습함, 마스터함의 네 가지 학습 상태 중 하나가 있습니다. 조회, 퀴즈, 글자 상호작용을 하면서 상태를 수동으로 올리거나 내릴 수 있습니다. 통계 화면에서는 모든 레벨과 오필 버전에 걸친 진행 상황 내역을 볼 수 있습니다.

### iCloud 동기화는 어떻게 설정하나요?

**설정 → iCloud 동기화**로 이동해 켜거나 끄세요. **신규 사용자는 iCloud 동기화가 기본으로 켜져 있습니다.** 기기에서 iCloud에 로그인되어 있는지 확인하세요. 활성화되면 iWuBi는 즐겨찾기, 학습 상태, 오답 노트, 퀴즈 최고 점수, 연속 기록, **타이핑 통계**, **내장 글 진행 상황**을 기기 간에 동기화합니다.

타이핑 UI 환경설정(가상 키보드, 글 병음, 오타 키 유지)은 각 기기에만 저장됩니다.

### 위젯은 어떻게 추가하고 사용하나요?

홈 화면이나 잠금 화면을 길게 누르고 **+**를 눌러 "iWuBi"를 검색하세요. iWuBi는 **8종류의 위젯**을 제공합니다. Daily Character(셔플 버튼 포함), Level Spotlight, Daily Quiz, **Typing Glance**, Favorites, Wrong Book, Recent, Learning Progress입니다. Favorites와 Wrong Book 위젯은 소형과 중형 크기에서 오필 코드가 있는 글자 그리드를 보여 줍니다. 위젯은 StandBy(iOS 17 이상)에서도 작동합니다. 데이터는 기기 내 App Group 컨테이너로 공유됩니다.

### 테마와 앱 아이콘은 어떻게 꾸미나요?

**설정 → 테마**에서 16가지 내장 테마나 사용자 지정 강조 색상을 고를 수 있습니다. **iOS**에서는 **설정 → 앱 설정 → 앱 아이콘**에서 8가지 대체 아이콘을 쓸 수 있습니다. 언어, 기본 오필 버전, 병음 표시, 병음 검색도 **앱 설정**에 있습니다.

### 딥링크란 무엇이며 어떻게 사용하나요?

iWuBi는 `iWuBi://` URL 스킴을 지원합니다. 경로는 `search`, `word`, `quiz`, `favorites`, `wrong`, `levels`, `learn`, **`typing`**입니다. 단축어, 북마크, 위젯에서 사용하면 기능으로 바로 이동할 수 있습니다. [URL 스킴 참조](../url-scheme)를 확인하세요.

### 후원 기능은 어떻게 작동하나요?

iWuBi는 설정에서 **StoreKit 2**를 통한 선택적 후원을 제공합니다. 모든 결제 처리는 전적으로 Apple이 담당합니다. 당사는 어떤 금융 정보도 받거나 저장하지 않습니다.

### iWuBi는 Mac에서 작동하나요?

네. iWuBi는 인라인 조회 검색창, Esc로 뒤로 가기, 튜토리얼 링크용 플로팅 앱 내 브라우저, 시스템 사전 카드, 시스템 공유 시트, Mac 키보드 단축키를 지원하는 완전한 타이핑 연습을 갖춘 네이티브 macOS 앱입니다.

### iWuBi는 오프라인에서 작동하나요?

네. 단어 라이브러리, 퀴즈, 튜토리얼, 타이핑 연습, 병음 도구는 오프라인으로 작동합니다. iCloud 동기화는 선택 사항이며, 켜면 Apple의 iCloud 키-값 저장소를 사용합니다.

### iWuBi는 개인 데이터를 수집하나요?

아니요. iWuBi는 개인 데이터를 수집, 저장, 전송하지 않습니다. 분석, 광고 SDK, 추적이 없습니다. [개인정보 처리방침](../privacy)을 확인하세요.

### 아직 도움이 필요하신가요?

[AppleOSer@gmail.com](mailto:AppleOSer@gmail.com)으로 연락해 주시면 48시간 이내에 답변드리겠습니다.

</section>
<section lang="ru" markdown="1">

### Что такое метод ввода «Утби» (Wubi)?

Утби (五笔) — это графический метод ввода китайского текста, который кодирует иероглифы по их структурным компонентам (корням), а не по произношению. Каждому иероглифу соответствует последовательность из 1–4 клавиш с буквами. После освоения Утби позволяет печатать по-китайски очень быстро и точно, без выбора среди омофонов.

### В чём разница между версиями 86, 98 и «Новый век»?

Версия 86 (王码五笔86版) была опубликована в 1986 году и остаётся самым распространённым стандартом. Версия 98 (王码五笔98版) была пересмотрена в 1998 году: обновлена раскладка корней и улучшено кодирование некоторых иероглифов. Версия «Новый век» (新世纪五笔) — самая новая редакция с дополнительно оптимизированными корнями и кодированием. iWuBi поддерживает все три стандарта — переключайтесь между ними в настройках и сравнивайте коды бок о бок.

### Как проходит знакомство с приложением?

При первом запуске iWuBi показывает **онбординг из 5 экранов**, знакомящий с поиском, уровнями, набором, викториной и виджетами. Его можно пропустить в любой момент. Обучающие материалы всегда доступны на вкладке **Обучение**.

### Как работает тренировка набора?

Откройте вкладку **Набор** и выберите режим:

- **Полный код** — вводите самый длинный код Утби для каждого иероглифа.
- **Код уровня** — тренируйте коды выбранных уровней 1–4.
- **Смешанный** — сначала пробуйте код уровня; после ошибки приложение показывает ответ и переключается на полный код.

Источники материала: вставленный текст, случайные иероглифы (с настраиваемым **количеством иероглифов**), 14 встроенных текстов, сгенерированные списки слов, избранное и журнал ошибок. Во время тренировки доступны **Подсказка**, **Показать** и **Пропустить**. Есть необязательная экранная клавиатура корней; на iOS её можно временно скрыть и использовать системную или внешнюю клавиатуру.

**Советы по клавиатуре:**

- **iOS / iPad:** пробел показывает подсказку; Return подтверждает; Backspace удаляет. «Показать» и «Пропустить» — экранные кнопки.
- **Mac:** пробел или `1` — подсказка; `2` — показать ответ; `3` — пропустить; Return подтверждает; Backspace / Delete удаляет.

Полный ввод автоматически отправляется при вводе до 4 клавиш. Статистика сессий (точность, серия, сессии) и прогресс по встроенным текстам синхронизируются через iCloud, если она включена.

### Как работает поиск по пиньиню?

В **Поиске**, когда вы вводите только буквы, iWuBi может переключаться между режимами поиска по **коду** и по **пиньиню** (переключатель в **Настройки → Настройки приложения → Поиск по пиньиню**). Режим пиньиня находит отдельные иероглифы по префиксу пиньиня без тонов. Фоновый индекс создаётся при первом использовании.

### Что такое конвертер пиньиня?

В **Настройки → Текстовые инструменты → Конвертер пиньиня** вставьте китайский текст и просмотрите несколько стилей вывода (с тонами, без тонов, с цифрами тонов, чжуинь, в две строки, выровненная сетка и другие). Можно дополнительно наложить коды Утби для текущего стандарта, затем скопировать результат или поделиться им длинным изображением.

### Как работает ежедневная викторина?

Каждый день вы получаете 8 вопросов трёх типов: по иероглифу ввести его код Утби; по коду Утби определить иероглиф; по иероглифу определить корневую клавишу, к которой он относится. Неверные ответы автоматически добавляются в Журнал ошибок для последующего повторения. Ваш лучший результат и ежедневная серия записываются и синхронизируются через iCloud.

### Как работает статус изучения?

У каждого иероглифа в библиотеке один из четырёх статусов изучения: Не изучен, Изучается, Выучен или Освоен. Пока вы ищете иероглифы, проходите викторины и взаимодействуете с ними, статус можно вручную повышать или понижать. В статистике показана разбивка прогресса по всем уровням и версиям Утби.

### Как настроить синхронизацию iCloud?

Перейдите в **Настройки → Синхронизация iCloud** и включите или выключите её. **Для новых пользователей синхронизация iCloud включена по умолчанию.** Убедитесь, что на устройстве выполнен вход в iCloud. После включения iWuBi синхронизирует между вашими устройствами избранное, статус изучения, журнал ошибок, лучший результат викторины, серию, **статистику набора** и **прогресс по встроенным текстам**.

Настройки интерфейса набора (виртуальная клавиатура, пиньинь текста, сохранение неверных клавиш) остаются только на каждом устройстве.

### Как добавить и использовать виджеты?

Нажмите и удерживайте экран «Домой» или экран блокировки, нажмите **+** и найдите «iWuBi». iWuBi предлагает **8 видов виджетов**: Daily Character (с кнопкой перемешивания), Level Spotlight, Daily Quiz, **Typing Glance**, Favorites, Wrong Book, Recent и Learning Progress. Виджеты Favorites и Wrong Book показывают сетку иероглифов с кодами Утби в малом и среднем размерах. Виджеты также работают в режиме «Ожидание» (iOS 17+). Данные передаются через контейнер App Group на устройстве.

### Как настроить темы и значки приложения?

В **Настройки → Тема** доступны 16 встроенных тем или собственный акцентный цвет. На **iOS** в **Настройки → Настройки приложения → Значок приложения** есть 8 альтернативных значков. Язык, версия Утби по умолчанию, отображение пиньиня и поиск по пиньиню также находятся в **Настройках приложения**.

### Что такое глубокие ссылки и как ими пользоваться?

iWuBi поддерживает схему URL `iWuBi://`. Доступные пути: `search`, `word`, `quiz`, `favorites`, `wrong`, `levels`, `learn` и **`typing`**. Используйте их в «Быстрых командах», закладках или виджетах, чтобы сразу переходить к нужной функции. См. [справочник по схеме URL](../url-scheme).

### Как работают пожертвования?

iWuBi предлагает необязательные пожертвования через **StoreKit 2** в настройках. Всю обработку платежей полностью выполняет Apple. Мы не получаем и не храним никакой финансовой информации.

### Работает ли iWuBi на Mac?

Да. iWuBi — нативное приложение для macOS со встроенной строкой поиска, возвратом по Esc, плавающим браузером для ссылок из обучения, карточками системного словаря, системным меню «Поделиться» и полноценной тренировкой набора с сочетаниями клавиш Mac.

### Работает ли iWuBi офлайн?

Да. Библиотека слов, викторины, обучающие материалы, тренировка набора и инструменты пиньиня работают офлайн. Синхронизация iCloud необязательна и при включении использует хранилище «ключ — значение» Apple iCloud.

### Собирает ли iWuBi персональные данные?

Нет. iWuBi не собирает, не хранит и не передаёт персональные данные. Аналитики, рекламных SDK и отслеживания нет. См. [Политику конфиденциальности](../privacy).

### Всё ещё нужна помощь?

Напишите нам на [AppleOSer@gmail.com](mailto:AppleOSer@gmail.com), и мы ответим в течение 48 часов.

</section>
<section lang="th" markdown="1">

### วิธีป้อนอู่ปี่ (Wubi) คืออะไร?

อู่ปี่ (五笔) เป็นวิธีป้อนภาษาจีนแบบอิงรูปอักษร ซึ่งเข้ารหัสตัวอักษรด้วยส่วนประกอบเชิงโครงสร้าง (ราก) แทนการออกเสียง แต่ละตัวอักษรจะแมปกับลำดับปุ่มตัวอักษร 1–4 ตัว เมื่อชำนาญแล้ว อู่ปี่ช่วยให้พิมพ์ภาษาจีนได้เร็วและแม่นยำมาก โดยไม่ต้องเลือกจากคำพ้องเสียง

### ความแตกต่างระหว่างรุ่น 86, 98 และศตวรรษใหม่คืออะไร?

รุ่น 86 (王码五笔86版) เผยแพร่ในปี 1986 และเป็นมาตรฐานที่ใช้กันแพร่หลายที่สุด รุ่น 98 (王码五笔98版) ปรับปรุงในปี 1998 พร้อมผังรากที่อัปเดตและการเข้ารหัสที่ดีขึ้นสำหรับบางตัวอักษร รุ่นศตวรรษใหม่ (新世纪五笔) เป็นฉบับปรับปรุงล่าสุดที่ปรับรากและการเข้ารหัสให้เหมาะสมยิ่งขึ้น iWuBi รองรับทั้งสามมาตรฐาน — สลับได้ในการตั้งค่าและเปรียบเทียบรหัสเคียงข้างกัน

### ขั้นตอนแนะนำการใช้งานเป็นอย่างไร?

เมื่อเปิดครั้งแรก iWuBi จะแสดง **การแนะนำการใช้งาน 5 หน้าจอ** แนะนำการค้นหา ระดับ การพิมพ์ แบบทดสอบ และวิดเจ็ต คุณข้ามได้ทุกเมื่อ และกลับมาดูบทเรียนได้จากแท็บ **เรียนรู้** ตลอดเวลา

### การฝึกพิมพ์ทำงานอย่างไร?

เปิดแท็บ **การพิมพ์** แล้วเลือกโหมด:

- **รหัสเต็ม** — พิมพ์รหัสอู่ปี่ที่ยาวที่สุดของแต่ละตัวอักษร
- **รหัสตามระดับ** — ฝึกรหัสระดับ 1–4 ที่คุณเลือก
- **ผสม** — ลองรหัสตามระดับก่อน หลังจากพิมพ์ผิด แอปจะเฉลยและเปลี่ยนเป็นรหัสเต็ม

แหล่งเนื้อหาได้แก่ ข้อความที่วาง ตัวอักษรสุ่ม (กำหนด **จำนวนตัวอักษร** ได้) บทความในตัว 14 บท รายการคำที่สร้างขึ้น รายการโปรด และสมุดบันทึกข้อที่ตอบผิด ระหว่างฝึกคุณใช้ **คำใบ้** **เฉลย** และ **ข้าม** ได้ มีคีย์บอร์ดรากบนหน้าจอแบบเลือกได้ บน iOS คุณซ่อนชั่วคราวและใช้คีย์บอร์ดของระบบหรือคีย์บอร์ดฮาร์ดแวร์แทนได้

**เคล็ดลับแป้นพิมพ์:**

- **iOS / iPad:** Space แสดงคำใบ้ Return ยืนยัน Backspace ลบ ส่วนเฉลยและข้ามใช้ปุ่มบนหน้าจอ
- **Mac:** Space หรือ `1` คำใบ้ `2` เฉลย `3` ข้าม Return ยืนยัน Backspace / Delete ลบ

เมื่อป้อนครบสูงสุด 4 ปุ่มจะส่งอัตโนมัติ สถิติรอบ (ความแม่นยำ สถิติต่อเนื่อง จำนวนรอบ) และความคืบหน้าบทความในตัวจะซิงค์ผ่าน iCloud เมื่อเปิดใช้

### การค้นหาด้วยพินอินทำงานอย่างไร?

ใน **ค้นหา** เมื่อคุณพิมพ์เฉพาะตัวอักษร iWuBi สลับระหว่างโหมดค้นหาด้วย **รหัส** และ **พินอิน** ได้ (สลับใน **การตั้งค่า → การตั้งค่าแอป → ค้นหาด้วยพินอิน**) โหมดพินอินจับคู่ตัวอักษรเดี่ยวด้วยคำนำหน้าพินอินแบบไม่มีวรรณยุกต์ ดัชนีเบื้องหลังจะถูกสร้างเมื่อใช้งานครั้งแรก

### ตัวแปลงพินอินคืออะไร?

ใน **การตั้งค่า → เครื่องมือข้อความ → ตัวแปลงพินอิน** วางข้อความภาษาจีนแล้วดูตัวอย่างรูปแบบผลลัพธ์หลายแบบ (มีวรรณยุกต์ ไม่มีวรรณยุกต์ วรรณยุกต์ตัวเลข จู้อินฝูเฮ่า สองบรรทัด ตารางจัดแนว และอื่น ๆ) คุณสามารถซ้อนรหัสอู่ปี่ตามมาตรฐานปัจจุบันได้ แล้วคัดลอกหรือแชร์เป็นภาพยาว

### แบบทดสอบประจำวันทำงานอย่างไร?

ทุกวันคุณจะได้แบบทดสอบ 8 ข้อจากคำถามสามประเภท: เมื่อให้ตัวอักษร ให้พิมพ์รหัสอู่ปี่ของมัน เมื่อให้รหัสอู่ปี่ ให้ระบุตัวอักษร และเมื่อให้ตัวอักษร ให้ระบุปุ่มรากที่ตัวอักษรนั้นอยู่ คำตอบที่ผิดจะถูกเพิ่มลงในสมุดบันทึกข้อที่ตอบผิดโดยอัตโนมัติเพื่อทบทวนภายหลัง คะแนนสูงสุดและสถิติต่อเนื่องรายวันของคุณจะถูกบันทึกและซิงค์ผ่าน iCloud

### สถานะการเรียนรู้ทำงานอย่างไร?

ทุกตัวอักษรในคลังมีหนึ่งในสี่สถานะการเรียนรู้: ยังไม่เรียน กำลังเรียน เรียนแล้ว หรือเชี่ยวชาญ เมื่อคุณค้นหา ทำแบบทดสอบ และโต้ตอบกับตัวอักษร คุณปรับสถานะขึ้นหรือลงด้วยตนเองได้ มุมมองสถิติแสดงรายละเอียดความคืบหน้าของคุณในทุกระดับและทุกรุ่นอู่ปี่

### ตั้งค่าการซิงค์ iCloud อย่างไร?

ไปที่ **การตั้งค่า → การซิงค์ iCloud** แล้วเปิดหรือปิด **สำหรับผู้ใช้ใหม่ การซิงค์ iCloud เปิดไว้เป็นค่าเริ่มต้น** ตรวจสอบว่าคุณลงชื่อเข้าใช้ iCloud บนอุปกรณ์แล้ว เมื่อทำงาน iWuBi จะซิงค์รายการโปรด สถานะการเรียนรู้ สมุดบันทึกข้อที่ตอบผิด คะแนนแบบทดสอบสูงสุด สถิติต่อเนื่อง **สถิติการพิมพ์** และ **ความคืบหน้าบทความในตัว** ข้ามอุปกรณ์ของคุณ

ค่ากำหนด UI การพิมพ์ (คีย์บอร์ดเสมือน พินอินของบทความ การคงปุ่มที่กดผิด) จะอยู่ในแต่ละอุปกรณ์เท่านั้น

### เพิ่มและใช้วิดเจ็ตอย่างไร?

กดค้างที่หน้าจอโฮมหรือหน้าจอล็อก แตะ **+** แล้วค้นหา "iWuBi" iWuBi มี **วิดเจ็ต 8 แบบ**: Daily Character (มีปุ่มสลับ), Level Spotlight, Daily Quiz, **Typing Glance**, Favorites, Wrong Book, Recent และ Learning Progress วิดเจ็ต Favorites และ Wrong Book แสดงตารางตัวอักษรพร้อมรหัสอู่ปี่ในขนาดเล็กและกลาง วิดเจ็ตใช้งานใน StandBy ได้ด้วย (iOS 17+) ข้อมูลแบ่งปันผ่านคอนเทนเนอร์ App Group บนอุปกรณ์

### ปรับแต่งธีมและไอคอนแอปอย่างไร?

ไปที่ **การตั้งค่า → ธีม** เพื่อเลือกธีมในตัว 16 แบบ หรือสีเน้นแบบกำหนดเอง บน **iOS** ไปที่ **การตั้งค่า → การตั้งค่าแอป → ไอคอนแอป** เพื่อเลือกไอคอนทางเลือก 8 แบบ ภาษา รุ่นอู่ปี่เริ่มต้น การแสดงพินอิน และการค้นหาด้วยพินอินก็อยู่ใน **การตั้งค่าแอป** เช่นกัน

### Deep Link คืออะไรและใช้อย่างไร?

iWuBi รองรับ URL scheme `iWuBi://` พาธที่ใช้ได้ ได้แก่ `search`, `word`, `quiz`, `favorites`, `wrong`, `levels`, `learn` และ **`typing`** ใช้ใน คำสั่งลัด บุ๊กมาร์ก หรือวิดเจ็ต เพื่อกระโดดไปยังฟีเจอร์โดยตรง ดู [เอกสารอ้างอิง URL Scheme](../url-scheme)

### ทิปทำงานอย่างไร?

iWuBi มีการให้ทิปแบบเลือกได้ผ่าน **StoreKit 2** ในการตั้งค่า การประมวลผลการชำระเงินทั้งหมดดำเนินการโดย Apple เราไม่ได้รับหรือจัดเก็บข้อมูลทางการเงินใด ๆ

### iWuBi ใช้งานบน Mac ได้ไหม?

ได้ iWuBi เป็นแอป macOS แบบเนทีฟ มีแถบค้นหาแบบอินไลน์ การย้อนกลับด้วย Esc เบราว์เซอร์ลอยในแอปสำหรับลิงก์บทเรียน การ์ดพจนานุกรมของระบบ ชีตแชร์ของระบบ และการฝึกพิมพ์เต็มรูปแบบพร้อมแป้นพิมพ์ลัดของ Mac

### iWuBi ใช้งานออฟไลน์ได้ไหม?

ได้ คลังคำศัพท์ แบบทดสอบ บทเรียน การฝึกพิมพ์ และเครื่องมือพินอินทำงานแบบออฟไลน์ การซิงค์ iCloud เป็นแบบเลือกได้ และเมื่อเปิดใช้จะใช้ที่เก็บข้อมูลคีย์-ค่าของ iCloud ของ Apple

### iWuBi เก็บข้อมูลส่วนบุคคลหรือไม่?

ไม่ iWuBi ไม่เก็บรวบรวม จัดเก็บ หรือส่งข้อมูลส่วนบุคคล ไม่มีการวิเคราะห์ SDK โฆษณา หรือการติดตาม ดู [นโยบายความเป็นส่วนตัว](../privacy)

### ยังต้องการความช่วยเหลืออยู่ไหม?

ติดต่อเราที่ [AppleOSer@gmail.com](mailto:AppleOSer@gmail.com) แล้วเราจะตอบกลับภายใน 48 ชั่วโมง

</section>
<section lang="de" markdown="1">

### Was ist die Wubi-Eingabemethode?

Wubi (五笔) ist eine formbasierte chinesische Eingabemethode, die Zeichen anhand ihrer Strukturkomponenten (Wurzeln) statt anhand der Aussprache kodiert. Jedes Zeichen entspricht einer Folge von 1–4 Buchstabentasten. Wer Wubi beherrscht, kann Chinesisch extrem schnell und genau tippen, ohne aus Homophonen auswählen zu müssen.

### Was ist der Unterschied zwischen der 86er-, der 98er- und der New-Century-Version?

Die 86er-Version (王码五笔86版) wurde 1986 veröffentlicht und ist der am weitesten verbreitete Standard. Die 98er-Version (王码五笔98版) wurde 1998 mit aktualisierter Wurzelanordnung und verbesserter Kodierung einiger Zeichen überarbeitet. Die New-Century-Version (新世纪五笔) ist die neueste Überarbeitung mit weiter optimierten Wurzeln und Kodierung. iWuBi unterstützt alle drei Standards — Sie können in den Einstellungen zwischen ihnen wechseln und die Kodierungen nebeneinander vergleichen.

### Wie läuft das Onboarding ab?

Beim ersten Start zeigt iWuBi ein **Onboarding mit 5 Bildschirmen**, das Suche, Stufen, Tippen, Quiz und Widgets vorstellt. Sie können es jederzeit überspringen. Die Tutorials erreichen Sie jederzeit über den Tab **Lernen**.

### Wie funktioniert das Tippen-Training?

Öffnen Sie den Tab **Tippen** und wählen Sie einen Modus:

- **Vollständiger Code** — Geben Sie für jedes Zeichen den längsten Wubi-Code ein.
- **Stufencode** — Üben Sie Codes der von Ihnen gewählten Stufen 1–4.
- **Gemischt** — Versuchen Sie zuerst den Stufencode; nach einem Fehler zeigt die App die Lösung und wechselt zum vollständigen Code.

Inhaltsquellen sind eingefügter Text, zufällige Zeichen (mit einstellbarer **Zeichenanzahl**), 14 integrierte Texte, erzeugte Wortlisten, Favoriten und Ihr Fehlerheft. Beim Üben stehen **Hinweis**, **Auflösen** und **Überspringen** zur Verfügung. Eine optionale Bildschirmtastatur mit Wurzeln ist verfügbar; unter iOS können Sie sie vorübergehend ausblenden und stattdessen die System- oder Hardware-Tastatur verwenden.

**Tastaturtipps:**

- **iOS / iPad:** Leertaste zeigt einen Hinweis; Return bestätigt; Rückschritt löscht. Auflösen und Überspringen nutzen Schaltflächen auf dem Bildschirm.
- **Mac:** Leertaste oder `1` Hinweis; `2` Auflösen; `3` Überspringen; Return bestätigt; Rückschritt / Entf löscht.

Eine vollständige Eingabe wird bei bis zu 4 Tasten automatisch abgeschickt. Sitzungsstatistiken (Genauigkeit, Serie, Sitzungen) und der Fortschritt in integrierten Texten werden bei aktivierter iCloud-Synchronisierung synchronisiert.

### Wie funktioniert die Pinyin-Suche?

Wenn Sie in **Suche** nur Buchstaben eingeben, kann iWuBi zwischen den Suchmodi **Code** und **Pinyin** wechseln (Umschalter unter **Einstellungen → App-Einstellungen → Pinyin-Suche**). Der Pinyin-Modus findet einzelne Zeichen anhand des Pinyin-Präfixes ohne Töne. Beim ersten Gebrauch wird im Hintergrund ein Index erstellt.

### Was ist der Pinyin-Konverter?

Unter **Einstellungen → Text-Werkzeuge → Pinyin-Konverter** fügen Sie chinesischen Text ein und sehen eine Vorschau mehrerer Ausgabestile (mit Tönen, ohne Töne, Ziffern-Töne, Bopomofo, zweizeilig, ausgerichtetes Raster und mehr). Optional blenden Sie die Wubi-Codes Ihres aktuellen Standards ein und kopieren oder teilen das Ergebnis als langes Bild.

### Wie funktioniert das tägliche Quiz?

Jeden Tag erhalten Sie 8 Quizfragen aus drei Fragetypen: Zu einem Zeichen den Wubi-Code eingeben; zu einem Wubi-Code das Zeichen bestimmen; und zu einem Zeichen die Wurzeltaste bestimmen, zu der es gehört. Falsche Antworten werden automatisch zu Ihrem Fehlerheft hinzugefügt, damit Sie sie später wiederholen können. Ihr Bestwert und Ihre tägliche Serie werden aufgezeichnet und über iCloud synchronisiert.

### Wie funktioniert der Lernstatus?

Jedes Zeichen in der Bibliothek hat einen von vier Lernstatus: Nicht gelernt, Lernend, Gelernt oder Gemeistert. Beim Nachschlagen, Quizzen und Arbeiten mit Zeichen können Sie den Status manuell hoch- oder herunterstufen. Die Statistikansicht zeigt Ihre Fortschrittsaufteilung über alle Stufen und Wubi-Versionen.

### Wie richte ich die iCloud-Synchronisierung ein?

Gehen Sie zu **Einstellungen → iCloud-Synchronisierung** und schalten Sie sie ein oder aus. **Für neue Nutzer ist die iCloud-Synchronisierung standardmäßig aktiviert.** Stellen Sie sicher, dass Sie auf Ihrem Gerät bei iCloud angemeldet sind. Sobald sie aktiv ist, synchronisiert iWuBi Favoriten, Lernstatus, Fehlerheft, Quiz-Bestwert, Serie, **Tippstatistik** und **Fortschritt in integrierten Texten** über Ihre Geräte hinweg.

Einstellungen der Tipp-Oberfläche (virtuelle Tastatur, Text-Pinyin, Beibehaltung falscher Tasten) bleiben nur auf dem jeweiligen Gerät.

### Wie füge ich Widgets hinzu und nutze sie?

Halten Sie den Home-Bildschirm oder den Sperrbildschirm gedrückt, tippen Sie auf **+** und suchen Sie nach „iWuBi“. iWuBi bietet **8 Widget-Arten**: Daily Character (mit Mischen-Taste), Level Spotlight, Daily Quiz, **Typing Glance**, Favorites, Wrong Book, Recent und Learning Progress. Die Widgets Favorites und Wrong Book zeigen in kleiner und mittlerer Größe ein Zeichenraster mit Wubi-Codes. Widgets funktionieren auch im StandBy-Modus (iOS 17+). Die Daten werden über einen App-Group-Container auf dem Gerät geteilt.

### Wie passe ich Designs und App-Symbole an?

Unter **Einstellungen → Design** finden Sie 16 integrierte Designs oder eine eigene Akzentfarbe. Unter **iOS** gibt es unter **Einstellungen → App-Einstellungen → App-Symbol** 8 alternative Symbole. Sprache, Standard-Wubi-Version, Pinyin-Anzeige und Pinyin-Suche finden Sie ebenfalls unter **App-Einstellungen**.

### Was sind Deep Links und wie verwende ich sie?

iWuBi unterstützt das URL-Schema `iWuBi://`. Pfade sind `search`, `word`, `quiz`, `favorites`, `wrong`, `levels`, `learn` und **`typing`**. Verwenden Sie sie in Kurzbefehlen, Lesezeichen oder Widgets, um direkt in eine Funktion zu springen. Siehe die [URL-Schema-Referenz](../url-scheme).

### Wie funktioniert das Trinkgeld?

iWuBi bietet in den Einstellungen optionale Trinkgelder über **StoreKit 2**. Die gesamte Zahlungsabwicklung übernimmt Apple. Wir erhalten oder speichern keine Finanzinformationen.

### Funktioniert iWuBi auf dem Mac?

Ja. iWuBi ist eine native macOS-App mit Inline-Suchleiste, Zurücknavigation per Esc, schwebendem In-App-Browser für Tutorial-Links, System-Wörterbuchkarten, System-Teilen-Blatt und vollständigem Tippen-Training mit Mac-Tastaturkurzbefehlen.

### Funktioniert iWuBi offline?

Ja. Wortbibliothek, Quizze, Tutorials, Tippen-Training und Pinyin-Werkzeuge funktionieren offline. Die iCloud-Synchronisierung ist optional und nutzt bei Aktivierung Apples iCloud-Schlüssel-Wert-Speicher.

### Erhebt iWuBi personenbezogene Daten?

Nein. iWuBi erhebt, speichert oder überträgt keine personenbezogenen Daten. Es gibt keine Analysen, Werbe-SDKs oder Tracking. Siehe die [Datenschutzerklärung](../privacy).

### Brauchen Sie noch Hilfe?

Schreiben Sie uns an [AppleOSer@gmail.com](mailto:AppleOSer@gmail.com), und wir antworten innerhalb von 48 Stunden.

</section>
<section lang="fr" markdown="1">

### Qu'est-ce que la méthode de saisie Wubi ?

Wubi (五笔) est une méthode de saisie chinoise basée sur la forme, qui encode les caractères par leurs composants structurels (racines) plutôt que par leur prononciation. Chaque caractère correspond à une séquence de 1 à 4 touches de lettres. Une fois maîtrisé, Wubi permet de taper le chinois de façon extrêmement rapide et précise, sans avoir à choisir parmi des homophones.

### Quelle est la différence entre les versions 86, 98 et New Century ?

La version 86 (王码五笔86版) a été publiée en 1986 et reste le standard le plus répandu. La version 98 (王码五笔98版) a été révisée en 1998 avec une disposition des racines mise à jour et un encodage amélioré pour certains caractères. La version New Century (新世纪五笔) est la dernière révision, avec des racines et un encodage encore optimisés. iWuBi prend en charge les trois standards — vous pouvez passer de l'un à l'autre dans les Réglages et comparer les encodages côte à côte.

### Comment se déroule la prise en main ?

Au premier lancement, iWuBi affiche une **prise en main en 5 écrans** présentant la recherche, les niveaux, la saisie, le quiz et les widgets. Vous pouvez l'ignorer à tout moment. Retrouvez les tutoriels à tout moment dans l'onglet **Apprendre**.

### Comment fonctionne l'entraînement à la saisie ?

Ouvrez l'onglet **Saisie** et choisissez un mode :

- **Code complet** — saisissez le code Wubi le plus long de chaque caractère.
- **Code par niveau** — entraînez-vous sur les codes des niveaux 1 à 4 que vous sélectionnez.
- **Mixte** — essayez d'abord le code par niveau ; après une erreur, l'app révèle la réponse et passe au code complet.

Les sources de contenu comprennent le texte collé, des caractères aléatoires (avec un **nombre de caractères** réglable), 14 textes intégrés, des listes de mots générées, les favoris et votre carnet d'erreurs. Pendant l'entraînement, vous pouvez utiliser **Indice**, **Révéler** et **Passer**. Un clavier de racines à l'écran facultatif est disponible ; sur iOS, vous pouvez le masquer temporairement et utiliser à la place le clavier système ou matériel.

**Astuces clavier :**

- **iOS / iPad :** Espace affiche un indice ; Retour valide ; Suppr. arrière efface. Révéler et Passer utilisent les boutons à l'écran.
- **Mac :** Espace ou `1` pour l'indice ; `2` pour révéler ; `3` pour passer ; Retour valide ; Suppr. arrière / Supprimer efface.

La saisie complète est envoyée automatiquement à 4 touches maximum. Les statistiques de session (précision, série, sessions) et la progression des textes intégrés se synchronisent via iCloud lorsqu'elle est activée.

### Comment fonctionne la recherche par pinyin ?

Dans **Recherche**, lorsque vous saisissez uniquement des lettres, iWuBi peut basculer entre les modes de recherche par **code** et par **pinyin** (commutateur dans **Réglages → Réglages de l'app → Recherche par pinyin**). Le mode pinyin trouve les caractères isolés par préfixe de pinyin sans tons. Un index en arrière-plan est créé à la première utilisation.

### Qu'est-ce que le convertisseur de pinyin ?

Dans **Réglages → Outils de texte → Convertisseur de pinyin**, collez du texte chinois et prévisualisez plusieurs styles de sortie (avec tons, sans tons, tons numériques, bopomofo, sur deux lignes, grille alignée, et plus). Vous pouvez éventuellement superposer les codes Wubi de votre standard actuel, puis copier ou partager le résultat sous forme d'image longue.

### Comment fonctionne le quiz quotidien ?

Chaque jour, vous recevez 8 questions de quiz tirées de trois types : à partir d'un caractère, saisir son code Wubi ; à partir d'un code Wubi, identifier le caractère ; à partir d'un caractère, identifier la touche de racine à laquelle il appartient. Les mauvaises réponses sont automatiquement ajoutées à votre carnet d'erreurs pour une révision ultérieure. Votre meilleur score et votre série quotidienne sont enregistrés et synchronisés via iCloud.

### Comment fonctionne le statut d'apprentissage ?

Chaque caractère de la bibliothèque a l'un des quatre statuts d'apprentissage : Non appris, En cours, Appris ou Maîtrisé. Au fil de vos recherches, quiz et interactions avec les caractères, vous pouvez promouvoir ou rétrograder manuellement leur statut. La vue Statistiques montre la répartition de votre progression sur tous les niveaux et toutes les versions de Wubi.

### Comment configurer la synchronisation iCloud ?

Allez dans **Réglages → Synchronisation iCloud** et activez-la ou désactivez-la. **La synchronisation iCloud est activée par défaut pour les nouveaux utilisateurs.** Assurez-vous d'être connecté à iCloud sur votre appareil. Une fois active, iWuBi synchronise les favoris, le statut d'apprentissage, le carnet d'erreurs, le meilleur score de quiz, la série, les **statistiques de saisie** et la **progression des textes intégrés** sur vos appareils.

Les préférences de l'interface de saisie (clavier virtuel, pinyin du texte, conservation des touches erronées) restent uniquement sur chaque appareil.

### Comment ajouter et utiliser les widgets ?

Appuyez longuement sur l'écran d'accueil ou l'écran verrouillé, touchez **+** et recherchez « iWuBi ». iWuBi propose **8 types de widgets** : Daily Character (avec bouton de mélange), Level Spotlight, Daily Quiz, **Typing Glance**, Favorites, Wrong Book, Recent et Learning Progress. Les widgets Favorites et Wrong Book affichent une grille de caractères avec leurs codes Wubi en petite et moyenne tailles. Les widgets fonctionnent aussi en mode Veille (iOS 17+). Les données sont partagées via un conteneur App Group sur l'appareil.

### Comment personnaliser les thèmes et les icônes de l'app ?

Allez dans **Réglages → Thème** pour choisir parmi 16 thèmes intégrés ou une couleur d'accent personnalisée. Sur **iOS**, allez dans **Réglages → Réglages de l'app → Icône de l'app** pour 8 icônes alternatives. La langue, la version Wubi par défaut, l'affichage du pinyin et la recherche par pinyin se trouvent aussi dans **Réglages de l'app**.

### Que sont les liens profonds et comment les utiliser ?

iWuBi prend en charge le schéma d'URL `iWuBi://`. Les chemins sont `search`, `word`, `quiz`, `favorites`, `wrong`, `levels`, `learn` et **`typing`**. Utilisez-les dans Raccourcis, les signets ou les widgets pour accéder directement à une fonctionnalité. Consultez la [référence du schéma d'URL](../url-scheme).

### Comment fonctionnent les pourboires ?

iWuBi propose des pourboires facultatifs via **StoreKit 2** dans les Réglages. Tout le traitement des paiements est entièrement géré par Apple. Nous ne recevons ni ne stockons aucune information financière.

### iWuBi fonctionne-t-il sur Mac ?

Oui. iWuBi est une app macOS native avec une barre de recherche intégrée, un retour par Échap, un navigateur flottant dans l'app pour les liens de tutoriel, des cartes du dictionnaire système, la feuille de partage système et un entraînement complet à la saisie avec les raccourcis clavier du Mac.

### iWuBi fonctionne-t-il hors ligne ?

Oui. La bibliothèque de mots, les quiz, les tutoriels, l'entraînement à la saisie et les outils de pinyin fonctionnent hors ligne. La synchronisation iCloud est facultative et, lorsqu'elle est activée, utilise le stockage clé-valeur iCloud d'Apple.

### iWuBi collecte-t-il des données personnelles ?

Non. iWuBi ne collecte, ne stocke ni ne transmet de données personnelles. Il n'y a ni analyse, ni SDK publicitaire, ni suivi. Consultez la [politique de confidentialité](../privacy).

### Besoin d'aide supplémentaire ?

Écrivez-nous à [AppleOSer@gmail.com](mailto:AppleOSer@gmail.com) et nous vous répondrons sous 48 heures.

</section>
<section lang="tr" markdown="1">

### Wubi giriş yöntemi nedir?

Wubi (五笔), karakterleri telaffuza göre değil, yapısal bileşenlerine (köklerine) göre kodlayan, şekil tabanlı bir Çince giriş yöntemidir. Her karakter 1–4 harf tuşundan oluşan bir diziyle eşleşir. Ustalaşıldığında Wubi, eşsesli kelimeler arasından seçim yapmaya gerek kalmadan son derece hızlı ve doğru Çince yazmanızı sağlar.

### 86, 98 ve Yeni Yüzyıl sürümleri arasındaki fark nedir?

86 sürümü (王码五笔86版) 1986'da yayımlandı ve en yaygın kullanılan standarttır. 98 sürümü (王码五笔98版) 1998'de güncellenmiş kök düzeni ve bazı karakterler için iyileştirilmiş kodlamayla revize edildi. Yeni Yüzyıl sürümü (新世纪五笔) ise kökleri ve kodlamayı daha da optimize eden en son revizyondur. iWuBi üç standardı da destekler — Ayarlar'dan aralarında geçiş yapabilir ve kodlamaları yan yana karşılaştırabilirsiniz.

### Tanıtım akışı nedir?

İlk açılışta iWuBi; arama, seviyeler, yazma, test ve widget'ları tanıtan **5 ekranlık bir tanıtım** gösterir. İstediğiniz zaman atlayabilirsiniz. Eğitimlere **Öğren** sekmesinden istediğiniz zaman tekrar göz atabilirsiniz.

### Yazma Alıştırması nasıl çalışır?

**Yazma** sekmesini açın ve bir mod seçin:

- **Tam kod** — her karakter için en uzun Wubi kodunu yazın.
- **Seviye kodu** — seçtiğiniz 1–4 seviyelerindeki kodlarla alıştırma yapın.
- **Karışık** — önce seviye kodunu deneyin; bir hatadan sonra uygulama cevabı gösterir ve tam koda geçer.

İçerik kaynakları arasında yapıştırılan metin, rastgele karakterler (ayarlanabilir **karakter sayısıyla**), 14 yerleşik metin, oluşturulan kelime listeleri, favoriler ve yanlış defteriniz bulunur. Alıştırma sırasında **İpucu**, **Göster** ve **Atla** seçeneklerini kullanabilirsiniz. İsteğe bağlı bir ekran kök klavyesi mevcuttur; iOS'ta bunu geçici olarak gizleyip bunun yerine sistem veya donanım klavyesini kullanabilirsiniz.

**Klavye ipuçları:**

- **iOS / iPad:** Boşluk ipucu gösterir; Return onaylar; Geri Sil siler. Göster ve Atla ekrandaki düğmeleri kullanır.
- **Mac:** Boşluk veya `1` ipucu; `2` cevabı gösterir; `3` atlar; Return onaylar; Backspace / Delete siler.

Tam giriş en fazla 4 tuşta otomatik olarak gönderilir. Oturum istatistikleri (doğruluk, seri, oturumlar) ve yerleşik metin ilerlemesi, etkinleştirildiğinde iCloud ile senkronize edilir.

### Pinyin Araması nasıl çalışır?

**Arama**'da yalnızca harf yazdığınızda iWuBi, **kod** ve **pinyin** arama modları arasında geçiş yapabilir (**Ayarlar → Uygulama Ayarları → Pinyin Araması** altından açılıp kapatılır). Pinyin modu, tek karakterleri tonsuz pinyin önekiyle eşleştirir. Arka plan dizini ilk kullanımda oluşturulur.

### Pinyin Dönüştürücü nedir?

**Ayarlar → Metin Araçları → Pinyin Dönüştürücü** altında Çince metni yapıştırın ve birden fazla çıktı stilini (tonlu, tonsuz, sayısal ton, Bopomofo, iki satırlı, hizalı ızgara ve daha fazlası) önizleyin. İsteğe bağlı olarak mevcut standardınızın Wubi kodlarını üst üste bindirebilir, ardından kopyalayabilir veya uzun görsel olarak paylaşabilirsiniz.

### Günlük Test nasıl çalışır?

Her gün üç soru türünden seçilen 8 test sorusu alırsınız: bir karakter verildiğinde Wubi kodunu yazmak; bir Wubi kodu verildiğinde karakteri belirlemek; ve bir karakter verildiğinde ait olduğu kök tuşunu belirlemek. Yanlış cevaplar, daha sonra gözden geçirmeniz için otomatik olarak Yanlış Soru Defteri'nize eklenir. En iyi puanınız ve günlük seriniz kaydedilir ve iCloud ile senkronize edilir.

### Öğrenme Durumu nasıl çalışır?

Kütüphanedeki her karakterin dört öğrenme durumundan biri vardır: Öğrenilmedi, Öğreniliyor, Öğrenildi veya Ustalaşıldı. Karakterleri ararken, test çözerken ve onlarla etkileşim kurarken durumlarını elle yükseltebilir veya düşürebilirsiniz. İstatistikler görünümü, tüm seviyeler ve Wubi sürümleri genelindeki ilerleme dökümünüzü gösterir.

### iCloud senkronizasyonunu nasıl ayarlarım?

**Ayarlar → iCloud Senkronizasyonu**'na gidin ve açın veya kapatın. **Yeni kullanıcılar için iCloud senkronizasyonu varsayılan olarak açıktır.** Cihazınızda iCloud'a giriş yaptığınızdan emin olun. Etkinleştiğinde iWuBi; favorileri, öğrenme durumunu, yanlış soru defterini, en iyi test puanını, seriyi, **yazma istatistiklerini** ve **yerleşik metin ilerlemesini** cihazlarınız arasında senkronize eder.

Yazma arayüzü tercihleri (sanal klavye, metin pinyin'i, yanlış tuşları koruma) yalnızca her cihazda kalır.

### Widget'ları nasıl eklerim ve kullanırım?

Ana Ekran'a veya Kilit Ekranı'na uzun basın, **+** simgesine dokunun ve "iWuBi" araması yapın. iWuBi **8 widget türü** sunar: Daily Character (karıştırma düğmeli), Level Spotlight, Daily Quiz, **Typing Glance**, Favorites, Wrong Book, Recent ve Learning Progress. Favorites ve Wrong Book widget'ları, küçük ve orta boyutlarda Wubi kodlu bir karakter ızgarası gösterir. Widget'lar StandBy'da da çalışır (iOS 17+). Veriler, cihaz üzerindeki bir App Group kapsayıcısı aracılığıyla paylaşılır.

### Temaları ve uygulama simgelerini nasıl özelleştiririm?

16 yerleşik tema veya özel bir vurgu rengi için **Ayarlar → Tema**'ya gidin. **iOS**'ta 8 alternatif simge için **Ayarlar → Uygulama Ayarları → Uygulama Simgesi**'ne gidin. Dil, varsayılan Wubi sürümü, pinyin gösterimi ve pinyin araması da **Uygulama Ayarları** altındadır.

### Derin Bağlantılar nedir ve nasıl kullanılır?

iWuBi, `iWuBi://` URL şemasını destekler. Yollar: `search`, `word`, `quiz`, `favorites`, `wrong`, `levels`, `learn` ve **`typing`**. Bir özelliğe doğrudan atlamak için bunları Kısayollar'da, yer imlerinde veya widget'larda kullanın. [URL Şeması Başvurusu](../url-scheme)'na bakın.

### Bahşiş kutusu nasıl çalışır?

iWuBi, Ayarlar'da **StoreKit 2** aracılığıyla isteğe bağlı bahşiş sunar. Tüm ödeme işlemleri tamamen Apple tarafından yürütülür. Finansal bilgi almayız veya saklamayız.

### iWuBi Mac'te çalışır mı?

Evet. iWuBi; satır içi Arama çubuğu, Esc ile geri gitme, eğitim bağlantıları için yüzen uygulama içi tarayıcı, sistem sözlük kartları, sistem paylaşım sayfası ve Mac klavye kısayollarıyla tam yazma alıştırması içeren yerel bir macOS uygulamasıdır.

### iWuBi çevrimdışı çalışır mı?

Evet. Kelime kütüphanesi, testler, eğitimler, yazma alıştırması ve pinyin araçları çevrimdışı çalışır. iCloud senkronizasyonu isteğe bağlıdır ve etkinleştirildiğinde Apple'ın iCloud Anahtar-Değer Depolaması'nı kullanır.

### iWuBi herhangi bir kişisel veri toplar mı?

Hayır. iWuBi kişisel veri toplamaz, saklamaz veya iletmez. Analiz, reklam SDK'sı veya izleme yoktur. [Gizlilik Politikası](../privacy)'na bakın.

### Hâlâ yardıma mı ihtiyacınız var?

Bize [AppleOSer@gmail.com](mailto:AppleOSer@gmail.com) adresinden ulaşın, 48 saat içinde size dönüş yapacağız.

</section>
