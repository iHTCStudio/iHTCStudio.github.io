---
layout: doc
title: iConverter — FAQ
app_id: iConverter
doc_title_en: Frequently Asked Questions
doc_title_zh_cn: 常见问题
doc_title_zh_tw: 常見問題
description: Frequently asked questions about iConverter.
---

<section lang="en" markdown="1">

### How do I find a specific tool?

Use the search bar at the top of the tool menu. You can search in English, Simplified Chinese or Traditional Chinese. Results match tool names, subtitles and keywords simultaneously.

### Can I pin tools to the home screen?

Yes. Tap the ⋯ menu button in any tool's toolbar, or go to **Settings → Pinned Tools** to add up to 8 tools to the quick-access row on the home screen.

### How do I add iConverter widgets?

Long-press your Home Screen or Lock Screen to enter edit mode, tap the **＋** button, search for "iConverter," and choose the widget size and tool you want. Interactive widgets (tap to update values directly on the widget) require iOS 17 or later. For a full walkthrough, open **Settings → About → Widget guide**.

### How do widget accent colors work?

**Settings → Widget color style** offers three modes: **Default** (each widget keeps its tool color), **Partial accent** (buttons and numbers follow your accent), and **Full accent** (background included). Changes refresh all widgets immediately.

### Why isn't Web Browser in the Launcher widget?

The **Launcher** widget lists tools with persistent or deep-link state. **Web Browser** is excluded because it has no widget snapshot to restore — open it from the app menu instead.

### Does the in-app language affect widget configuration?

**No.** The language you pick under **Settings → Language** applies to the main app UI only. When iOS shows the widget tool picker (add/edit widget), that system UI follows your **iPhone/iPad system language**, not the in-app override.

### Can I change the app language independently of my iPhone's language?

Yes. Go to **Settings → Language** inside the app. You can choose Simplified Chinese, Traditional Chinese or English regardless of your system language.

### How do I restore the last session when opening a tool?

Go to **Settings → Calculator History → Restore Last Session**. When enabled, opening a supported tool will automatically restore the most recent values from history.

### How do I share a calculation result?

Tap any result value to copy it to the clipboard. A brief toast confirms the copy. You can then paste it anywhere. For QR codes, use **Generate** or **Scan** tabs in the QR Code tool — Share or Save buttons export generated codes; scanning opens `iconverter://` links directly.

### What is the URL Scheme / Deep Link feature?

iConverter supports the `iconverter://` URL scheme, which lets you open any of the 101 tools from Safari, Apple Shortcuts, another app or a scanned QR code. Many tools also accept URL parameters to pre-fill input fields automatically.

See the full [URL Scheme Reference](../url-scheme) for all supported tools and parameters.

### How do I use iConverter with Apple Shortcuts?

1. Open the **Shortcuts** app and create a new shortcut.
2. Add an **Open URLs** action.
3. Enter an `iconverter://` URL, for example: `iconverter://tool/bmi?h=175&w=70`
4. Run the shortcut to open iConverter and pre-fill the BMI tool.

### Can I open iConverter from a QR code?

Yes. The **QR Code** tool can **scan** codes with the camera, or you can generate a QR for any `iconverter://` URL. When scanned with the in-app scanner, iPhone Camera, or another reader, it opens the corresponding tool — optionally with pre-filled values.

### How do I change the accent colour?

Go to **Settings → Accent Colour**. Choose from 12 preset colours or tap the colour wheel icon to pick any custom colour with the system colour picker.

### Can I change the app icon?

Yes. Go to **Settings → App Icon** to switch between the default icon and several alternate designs.

### What are "Home Screen Shortcuts"?

Home Screen Shortcuts let you add up to 4 specific tools as icon-sized shortcuts directly on your iOS Home Screen (using `UIApplicationShortcutItem`). Configure them in **Settings → Home Screen Shortcuts**.

### How does the Calculator History work?

All three calculators (Standard, Scientific, Programmer) share one history log. Each entry shows the expression and result. Tap an entry in the history sheet to restore it. History recording can be toggled in **Settings → Calculator History**. You can delete individual entries by swiping left, or clear all entries at once.

### The web browser tool can't open a URL — what's wrong?

- Make sure the URL starts with `http://` or `https://`. If you type a plain domain, the browser will auto-add `https://`.
- If the URL looks like a search query, the browser will search using your selected search engine.
- `iconverter://` links opened inside the web browser are passed back to the system to handle — they will open the corresponding iConverter tool.

### How do I export a video frame?

1. Open **Video Frame Export** from the Lifestyle category.
2. Tap the video icon to pick a video from Photos.
3. Use the slider and step buttons to navigate to the exact frame.
4. Tap **Save to Photos** or the share icon to export the frame.
5. For batch export, tap ⋯ and choose **Burst Export**.

### Are all tools available offline?

Yes — all 101 tools work fully offline. The only exception is the **Web Browser** tool, which requires an internet connection to load web pages. The Web Browser's own features (bookmarks, history, JS injection, etc.) work locally.

### Does iConverter collect any personal data?

No. See the [Privacy Policy](../privacy) for details.

### Still need help?

Contact us at [AppleOSer@gmail.com](mailto:AppleOSer@gmail.com) and we will get back to you within 48 hours.

</section>
<section lang="zh-CN" markdown="1">

### 如何找到特定工具？

使用工具菜单顶部的搜索栏。可使用英文、简体中文或繁体中文搜索，结果会同时匹配工具名、副标题与关键词。

### 可以把工具置顶到首页吗？

可以。点按任意工具工具栏上的 ⋯ 菜单，或进入 **设置 → 置顶工具** 添加最多 8 个工具到首页快速访问条。

### 如何添加爱计算的小组件？

长按主屏幕或锁屏进入编辑模式，点按 **＋** 按钮，搜索「iConverter」，选择想要的小组件尺寸与工具。交互式小组件（直接在小组件上点按更新数值）需 iOS 17 或更新版本。完整教程见 **设置 → 关于 → 小组件教程**。

### 小组件强调色怎么设置？

**设置 → 小组件颜色风格** 三档：**默认**（各小组件保留工具原色）、**部分跟随**（按钮与数字用强调色）、**全部跟随**（含背景）。修改后立即刷新所有小组件。

### 为什么启动器小组件里没有网页浏览器？

**启动器** 小组件列出可持久化或通过 deep link 恢复的工具。**网页浏览器** 无 widget 快照可恢复，因此不在列表中——请从 App 菜单打开。

### App 内语言会影响小组件配置界面吗？

**不会。** **设置 → 语言** 仅影响 App 内界面。iOS 添加/编辑小组件时的系统选择器跟随 **设备系统语言**，不受 App 内语言覆盖影响。

### 能否独立于 iPhone 系统语言切换应用语言？

可以。在应用内进入 **设置 → 语言**。你可以选择简体中文、繁体中文或英文，与系统语言无关。

### 打开工具时如何恢复上次会话？

进入 **设置 → 计算器历史 → 恢复上次会话**。开启后，打开支持的工具会自动从历史中恢复最近的数值。

### 如何分享计算结果？

点按任意结果值即可复制到剪贴板，简短提示确认复制成功，之后可以粘贴到任意位置。二维码工具含 **生成** 与 **扫描** 标签——生成后可分享/保存；扫描可直接打开 `iconverter://` 链接。

### 什么是 URL Scheme / 深度链接？

爱计算支持 `iconverter://` URL Scheme，可从 Safari、苹果快捷指令、其他应用或扫描二维码打开 101 个工具中的任意一个。许多工具还接受 URL 参数自动预填输入框。

完整支持工具与参数详见 [URL Scheme 说明](../url-scheme)。

### 如何在快捷指令中使用爱计算？

1. 打开 **快捷指令** 应用，创建一个新的快捷指令。
2. 添加 **打开 URL** 动作。
3. 输入 `iconverter://` URL，例如：`iconverter://tool/bmi?h=175&w=70`
4. 运行该快捷指令即可打开爱计算并预填 BMI 工具。

### 可以从二维码打开爱计算吗？

可以。**二维码** 工具支持 **相机扫描**，也可为 `iconverter://` URL 生成二维码。用 App 内扫描、iPhone 相机或其他读码器扫描后会直接打开对应工具——可选预填数值。

### 如何更改主题色？

进入 **设置 → 主题色**。从 12 款预设颜色中选择，或点按颜色轮图标使用系统颜色选择器选择任意自定义颜色。

### 可以更换应用图标吗？

可以。进入 **设置 → 应用图标** 在默认图标与多款备用设计之间切换。

### 什么是「主屏快捷方式」？

主屏快捷方式让你直接在 iOS 主屏添加最多 4 个工具作为图标尺寸的快捷方式（使用 `UIApplicationShortcutItem`）。在 **设置 → 主屏快捷方式** 配置。

### 计算器历史如何工作？

三个计算器（标准、科学、程序员）共享一份历史记录。每条记录显示表达式与结果。在历史面板中点按任意条目可恢复。可在 **设置 → 计算器历史** 切换是否记录。可左滑删除单条记录，或一次清空全部。

### 网页浏览器工具无法打开 URL 怎么办？

- 确认 URL 以 `http://` 或 `https://` 开头。如果输入的是纯域名，浏览器会自动加上 `https://`。
- 如果输入像搜索词，浏览器会用你选择的搜索引擎进行搜索。
- 在网页浏览器内打开的 `iconverter://` 链接会被交回系统处理——会打开对应的爱计算工具。

### 如何导出视频帧？

1. 从「生活」分类打开 **视频关键帧**。
2. 点按视频图标从相册选取视频。
3. 使用滑块和步进按钮导航到目标帧。
4. 点按 **保存到相册** 或分享图标导出帧。
5. 批量导出请点 ⋯ 选择 **连拍导出**。

### 所有工具都能离线使用吗？

是的——101 个工具全部完全离线运行。唯一例外是 **网页浏览器** 工具，加载网页需要联网。网页浏览器自身的功能（书签、历史、JS 注入等）都在本地。

### 爱计算会收集个人数据吗？

不会。详情请见 [隐私政策](../privacy)。

### 仍需帮助？

发邮件到 [AppleOSer@gmail.com](mailto:AppleOSer@gmail.com)，我们会在 48 小时内回复。

</section>
<section lang="zh-TW" markdown="1">

### 如何找到特定工具？

使用工具選單頂部的搜尋列。可使用英文、簡體中文或繁體中文搜尋，結果會同時比對工具名、副標題與關鍵字。

### 可以把工具置頂到首頁嗎？

可以。點按任意工具工具列上的 ⋯ 選單，或進入 **設定 → 置頂工具** 新增最多 8 個工具到首頁快速存取條。

### 如何新增愛計算的小工具？

長按主畫面或鎖定畫面進入編輯模式，點按 **＋** 按鈕，搜尋「iConverter」，選擇想要的小工具尺寸與工具。互動式小工具（直接在小工具上點按更新數值）需 iOS 17 或更新版本。完整教學見 **設定 → 關於 → 小工具教學**。

### 小工具強調色怎麼設定？

**設定 → 小工具顏色風格** 三檔：**預設**（各小工具保留工具原色）、**部分跟隨**（按鈕與數字用強調色）、**全部跟隨**（含背景）。修改後立即重新整理所有小工具。

### 為什麼啟動器小工具裡沒有網頁瀏覽器？

**啟動器** 小工具列出可持久化或透過 deep link 還原的工具。**網頁瀏覽器** 無 widget 快照可還原，因此不在列表中——請從 App 選單開啟。

### App 內語言會影響小工具設定介面嗎？

**不會。** **設定 → 語言** 僅影響 App 內介面。iOS 新增/編輯小工具時的系統選擇器跟隨 **裝置系統語言**，不受 App 內語言覆寫影響。

### 能否獨立於 iPhone 系統語言切換應用語言？

可以。在應用內進入 **設定 → 語言**。你可以選擇簡體中文、繁體中文或英文，與系統語言無關。

### 開啟工具時如何還原上次工作階段？

進入 **設定 → 計算器歷史 → 還原上次工作階段**。開啟後，開啟支援的工具會自動從歷史中還原最近的數值。

### 如何分享計算結果？

點按任意結果值即可複製到剪貼簿，簡短提示確認複製成功，之後可以貼上到任意位置。QR Code 工具含 **產生** 與 **掃描** 標籤——產生後可分享/儲存；掃描可直接開啟 `iconverter://` 連結。

### 什麼是 URL Scheme / 深度連結？

愛計算支援 `iconverter://` URL Scheme，可從 Safari、Apple 捷徑、其他應用或掃描 QR Code 開啟 101 個工具中的任意一個。許多工具還接受 URL 參數自動預填輸入框。

完整支援工具與參數詳見 [URL Scheme 說明](../url-scheme)。

### 如何在捷徑中使用愛計算？

1. 開啟 **捷徑** 應用，建立一個新的捷徑。
2. 新增 **開啟 URL** 動作。
3. 輸入 `iconverter://` URL，例如：`iconverter://tool/bmi?h=175&w=70`
4. 執行該捷徑即可開啟愛計算並預填 BMI 工具。

### 可以從 QR Code 開啟愛計算嗎？

可以。**QR Code** 工具支援 **相機掃描**，亦可為 `iconverter://` URL 產生 QR Code。用 App 內掃描、iPhone 相機或其他讀碼器掃描後會直接開啟對應工具——可選預填數值。

### 如何更改主題色？

進入 **設定 → 主題色**。從 12 款預設顏色中選擇，或點按顏色輪圖示使用系統顏色選擇器選擇任意自訂顏色。

### 可以更換應用圖示嗎？

可以。進入 **設定 → 應用圖示** 在預設圖示與多款備用設計之間切換。

### 什麼是「主畫面捷徑」？

主畫面捷徑讓你直接在 iOS 主畫面新增最多 4 個工具作為圖示大小的捷徑（使用 `UIApplicationShortcutItem`）。在 **設定 → 主畫面捷徑** 設定。

### 計算器歷史如何運作？

三個計算器（標準、科學、程式設計師）共用一份歷史紀錄。每條紀錄顯示表達式與結果。在歷史面板中點按任意條目可還原。可在 **設定 → 計算器歷史** 切換是否記錄。可左滑刪除單條紀錄，或一次清空全部。

### 網頁瀏覽器工具無法開啟 URL 怎麼辦？

- 確認 URL 以 `http://` 或 `https://` 開頭。如果輸入的是純網域，瀏覽器會自動加上 `https://`。
- 如果輸入像搜尋詞，瀏覽器會用你選擇的搜尋引擎進行搜尋。
- 在網頁瀏覽器內開啟的 `iconverter://` 連結會被交回系統處理——會開啟對應的愛計算工具。

### 如何匯出影片幀？

1. 從「生活」分類開啟 **影片關鍵幀**。
2. 點按影片圖示從相簿選取影片。
3. 使用滑桿和步進按鈕導航到目標幀。
4. 點按 **儲存到相簿** 或分享圖示匯出幀。
5. 批次匯出請點 ⋯ 選擇 **連拍匯出**。

### 所有工具都能離線使用嗎？

是的——101 個工具全部完全離線運行。唯一例外是 **網頁瀏覽器** 工具，載入網頁需要連網。網頁瀏覽器自身的功能（書籤、歷史、JS 注入等）都在本地。

### 愛計算會收集個人資料嗎？

不會。詳情請見 [隱私政策](../privacy)。

### 仍需協助？

寄信到 [AppleOSer@gmail.com](mailto:AppleOSer@gmail.com)，我們會在 48 小時內回覆。

</section>
<section lang="ja" markdown="1">

### 特定のツールを見つけるには？

ツールメニュー上部の検索バーを使います。English、简体中文、繁體中文で検索でき、名前・サブタイトル・キーワードに同時マッチします。

### ホーム画面にツールをピン留めできますか？

はい。各ツールのツールバー **⋯** メニュー、または **設定 → ピン留めツール** から最大 8 個をホームのクイック行に追加できます。

### iConverter ウィジェットの追加方法は？

ホーム画面またはロック画面を長押し → **＋** → 「iConverter」を検索 → サイズとツールを選択。インタラクティブウィジェット（タップで値更新）は iOS 17 以降。**設定 → について → ウィジェットガイド** に詳しい手順があります。

### ウィジェットのアクセント色は？

**設定 → ウィジェットの色スタイル**：**デフォルト**（各ウィジェットのツール色）、**部分アクセント**（ボタンと数字）、**フルアクセント**（背景含む）。変更は全ウィジェットに即反映されます。

### Launcher ウィジェットに Web ブラウザがないのはなぜ？

**Launcher** は永続状態またはディープリンク状態を持つツールを一覧します。**Web ブラウザ** は復元するウィジェットスナップショットがないため除外 — アプリメニューから開いてください。

### アプリ内言語はウィジェット設定に影響しますか？

**いいえ。** **設定 → 言語** はメイン UI のみ。iOS のウィジェット追加/編集ピッカーは **端末のシステム言語** に従います。

### システム言語と独立してアプリ言語を変えられますか？

はい。**設定 → 言語** で简体・繁体・English を選べます（システムと無関係）。

### ツールを開いたとき前回セッションを復元するには？

**設定 → 電卓履歴 → 前回セッションを復元** をオンに。対応ツールで直近の値が自動復元されます。

### 計算結果を共有するには？

結果値をタップでクリップボードにコピー（トースト表示）。QR ツールの **生成** / **スキャン** タブでは共有・保存が可能。スキャンで `iconverter://` を直接開けます。

### URL Scheme / ディープリンクとは？

`iconverter://` で 101 ツールを Safari、ショートカット、他アプリ、QR から開けます。多くのツールは URL パラメータで入力を事前入力できます。詳細は [URL Scheme](../url-scheme)。

### Apple ショートカットでの使い方は？

1. **ショートカット** で新規作成
2. **URL を開く** を追加
3. 例：`iconverter://tool/bmi?h=175&w=70`
4. 実行で iConverter が開き BMI が事前入力されます

### QR コードから iConverter を開けますか？

はい。**QR コード** ツールでカメラスキャンまたは `iconverter://` の QR 生成。アプリ内スキャナ、iPhone カメラ、他リーダーで対応ツールが開きます（値の事前入力可）。

### アクセント色の変更は？

**設定 → アクセントカラー** — 12 プリセットまたはカラーホイール。

### アプリアイコンの変更は？

**設定 → アプリアイコン** でデフォルトと代替デザインを切り替え。

### 「ホーム画面ショートカット」とは？

最大 4 ツールを iOS ホーム画面にアイコンサイズで追加（`UIApplicationShortcutItem`）。**設定 → ホーム画面ショートカット** で構成。

### 電卓履歴の仕組みは？

標準・関数・プログラマ電卓で履歴共有。式と結果を表示。履歴シートでタップ復元。**設定 → 電卓履歴** で記録のオン/オフ、左スワイプ削除、一括消去。

### Web ブラウザが URL を開けない場合は？

- `http://` または `https://` で始める（ドメインのみなら `https://` を自動付与）
- 検索クエリ風なら選択エンジンで検索
- ブラウザ内の `iconverter://` はシステムに渡され対応ツールが開きます

### 動画フレームの書き出しは？

1. ライフスタイルカテゴリの **動画フレーム書き出し** を開く
2. 写真から動画を選択
3. スライダーとステップでフレーム移動
4. **写真に保存** または共有
5. **バースト書き出し** は ⋯ メニュー

### すべてオフラインで使えますか？

**101 ツールすべてオフライン**（**Web ブラウザ** のページ読み込みのみ要ネット）。ブックマーク、履歴、JS 注入などブラウザ機能自体はローカル。

### 個人データを収集しますか？

いいえ。詳細は [プライバシーポリシー](../privacy)。

### まだ助けが必要ですか？

[AppleOSer@gmail.com](mailto:AppleOSer@gmail.com) — 通常 48 時間以内に返信します。

</section>
<section lang="ko" markdown="1">

### 특정 도구를 찾으려면?

도구 메뉴 상단 검색창을 사용하세요. English, 简体中文, 繁體中文로 검색할 수 있으며 이름·부제·키워드에 동시에 매칭됩니다.

### 홈 화면에 도구를 고정할 수 있나요?

네. 도구 툴바 **⋯** 메뉴 또는 **설정 → 고정된 도구**에서 최대 8개를 홈 빠른 실행 줄에 추가할 수 있습니다.

### iConverter 위젯 추가 방법?

홈/잠금 화면 길게 누르기 → **＋** → "iConverter" 검색 → 크기와 도구 선택. 인터랙티브 위젯(iOS 17+)은 위젯에서 값을 직접 갱신합니다. **설정 → 정보 → 위젯 가이드** 참고.

### 위젯 강조 색상은?

**설정 → 위젯 색상 스타일**: **기본**, **부분 강조**, **전체 강조**. 변경 시 모든 위젯이 즉시 새로고침됩니다.

### Launcher 위젯에 웹 브라우저가 없는 이유?

**Launcher**는 상태를 저장하거나 딥 링크하는 도구만 나열합니다. **웹 브라우저**는 복원할 스냅샷이 없어 제외 — 앱 메뉴에서 여세요.

### 앱 언어가 위젯 구성에 영향을 주나요?

**아니요.** **설정 → 언어**는 앱 UI만. iOS 위젯 선택 UI는 **시스템 언어**를 따릅니다.

### 시스템과 별도로 앱 언어를 바꿀 수 있나요?

네. **설정 → 언어**에서 简体·繁体·English 선택.

### 마지막 세션 복원?

**설정 → 계산기 기록 → 마지막 세션 복원** 활성화.

### 결과 공유?

결과 값 탭 → 클립보드. QR 도구에서 생성/스캔, `iconverter://` 직접 열기.

### URL Scheme?

`iconverter://`로 101개 도구를 Safari·Shortcuts·QR에서 열 수 있습니다. [URL Scheme](../url-scheme) 참고.

### Shortcuts?

**URL 열기**에 `iconverter://tool/bmi?h=175&w=70` 등 입력.

### QR로 열기?

**QR 코드** 도구로 스캔/생성.

### 강조 색?

**설정 → 강조 색**.

### 앱 아이콘?

**설정 → 앱 아이콘**.

### 홈 화면 바로가기?

**설정 → 홈 화면 바로가기** (최대 4개).

### 계산기 기록?

세 계산기 공유 기록. **설정 → 계산기 기록**에서 관리.

### 웹 브라우저 URL 문제?

`http(s)://` 확인. `iconverter://`는 시스템이 처리.

### 동영상 프레임 내보내기?

**동영상 프레임 내보내기** → 동영상 선택 → 프레임 이동 → 저장/공유.

### 오프라인?

101개 도구 모두 오프라인(**웹 브라우저** 페이지 로드만 네트워크 필요).

### 개인정보 수집?

아니요. [개인정보 처리방침](../privacy).

### 도움이 더 필요하면?

[AppleOSer@gmail.com](mailto:AppleOSer@gmail.com) — 보통 48시간 이내.

</section>
<section lang="ru" markdown="1">

### Как найти инструмент?

Строка поиска в меню (English, 简体中文, 繁體中文).

### Закрепить на главном экране?

**⋯** или **Настройки → Закреплённые инструменты** (до 8).

### Виджеты?

Долгое нажатие → **＋** → « iConverter ». **Настройки → О приложении → Руководство по виджетам**.

### Цвета виджетов?

**Настройки → Стиль цвета виджета**.

### Почему нет браузера в Launcher?

Нет снимка состояния — открывайте из меню.

### Язык приложения и виджет?

In-app язык не меняет системный picker виджета.

### Язык независимо от системы?

**Настройки → Язык**.

### Восстановление сессии?

**Настройки → История калькулятора → Восстановить последнюю сессию**.

### URL Scheme?

`iconverter://` — [URL Scheme](../url-scheme).

### Офлайн?

101 инструмент офлайн; браузеру нужна сеть для страниц.

### Данные?

Нет — [Конфиденциальность](../privacy).

### Помощь?

[AppleOSer@gmail.com](mailto:AppleOSer@gmail.com).

</section>
<section lang="th" markdown="1">

### หาเครื่องมือเฉพาะอย่างไร?

ใช้แถบค้นหา (English, 简体中文, 繁體中文)

### ปักหมุดเครื่องมือ?

**⋯** หรือ **การตั้งค่า → เครื่องมือที่ปักหมุด** (สูงสุด 8)

### วิดเจ็ต?

กดค้าง → **＋** → "iConverter" — **การตั้งค่า → เกี่ยวกับ → คู่มือวิดเจ็ต**

### สี accent วิดเจ็ต?

**การตั้งค่า → สไตล์สีวิดเจ็ต**

### ทำไมไม่มีเบราว์เซอร์ใน Launcher?

ไม่มี snapshot — เปิดจากเมนูแอป

### ภาษาในแอป vs วิดเจ็ต?

ภาษาในแอปไม่เปลี่ยน picker ของระบบ

### ออฟไลน์?

เครื่องมือ 101 รายการออฟไลน์ (เบราว์เซอร์โหลดหน้าเว็บต้องใช้เน็ต)

### ข้อมูลส่วนตัว?

ไม่ — [นโยบายความเป็นส่วนตัว](../privacy)

### ช่วยเหลือ?

[AppleOSer@gmail.com](mailto:AppleOSer@gmail.com)

</section>
<section lang="de" markdown="1">

### Wie finde ich ein bestimmtes Tool?

Nutzen Sie die Suche oben im Tool-Menü (English, 简体中文, 繁體中文). Treffer in Namen, Untertiteln und Stichwörtern gleichzeitig.

### Tools anheften?

Ja — **⋯** in der Toolbar oder **Einstellungen → Angeheftete Tools** (bis zu 8 auf dem Startbildschirm).

### Widgets hinzufügen?

Home/Lock Screen lang drücken → **＋** → „iConverter“ → Größe & Tool. Interaktive Widgets ab iOS 17. Anleitung: **Einstellungen → Info → Widget-Anleitung**.

### Widget-Akzentfarben?

**Einstellungen → Widget-Farbstil**: Standard, Teil-Akzent, Voll-Akzent — sofort für alle Widgets.

### Warum kein Web-Browser im Launcher-Widget?

Launcher listet Tools mit persistentem/deep-link-Zustand. Der Browser hat keinen Widget-Snapshot — im App-Menü öffnen.

### Beeinflusst die App-Sprache die Widget-Konfiguration?

**Nein.** In-App-Sprache nur für die App; der iOS-Widget-Picker folgt der **Systemsprache**.

### App-Sprache unabhängig vom System?

Ja — **Einstellungen → Sprache** (简体 / 繁体 / English).

### Letzte Sitzung wiederherstellen?

**Einstellungen → Rechner-Verlauf → Letzte Sitzung wiederherstellen**.

### Ergebnis teilen?

Ergebnis antippen → Zwischenablage. QR-Tool: Teilen/Speichern; `iconverter://` beim Scannen.

### URL Scheme?

`iconverter://` öffnet alle 101 Tools — siehe [URL Scheme](../url-scheme).

### Shortcuts / QR / Akzent / Icon / Home-Shortcuts / Verlauf / Browser / Video-Frame?

Wie in der englischen FAQ: Shortcuts mit **URL öffnen**, QR-Tool, **Einstellungen** für Akzent, Icon, Home-Shortcuts, Rechner-Verlauf; Browser braucht `http(s)://`; **Video-Frame-Export** unter Lifestyle.

### Offline?

Alle 101 Tools offline; nur **Web-Browser**-Seiten laden brauchen Netz.

### Datenerfassung?

Nein — [Datenschutz](../privacy).

### Hilfe?

[AppleOSer@gmail.com](mailto:AppleOSer@gmail.com) — meist innerhalb von 48 h.

</section>
<section lang="fr" markdown="1">

### Comment trouver un outil ?

Barre de recherche du menu (English, 简体中文, 繁體中文) — noms, sous-titres et mots-clés.

### Épingler des outils ?

**⋯** ou **Réglages → Outils épinglés** (jusqu’à 8).

### Widgets ?

Appui long → **＋** → « iConverter » → taille et outil. iOS 17+ pour l’interactivité. **Réglages → À propos → Guide widgets**.

### Couleurs d’accent des widgets ?

**Réglages → Style de couleur** : Défaut, Accent partiel, Accent complet.

### Pas de navigateur dans Launcher ?

Pas d’instantané widget — ouvrez-le depuis le menu.

### Langue in-app vs widget ?

L’in-app (**Réglages → Langue**) n’affecte pas le picker système du widget.

### Langue indépendante du système ?

Oui — 简体 / 繁体 / English.

### Restaurer la dernière session ?

**Réglages → Historique calculatrice → Restaurer la dernière session**.

### Partager un résultat ?

Appuyer sur une valeur → presse-papiers. QR : `iconverter://`.

### URL Scheme ?

Voir [URL Scheme](../url-scheme) — 101 outils via `iconverter://`.

### Raccourcis, QR, accent, icône, raccourcis écran d’accueil, historique, navigateur, export de frame ?

Comme dans la FAQ anglaise ; navigateur : URLs `http(s)://` ; export frame dans Lifestyle.

### Hors ligne ?

101 outils hors ligne ; pages web du navigateur seulement en ligne.

### Données personnelles ?

Non — [Politique de confidentialité](../privacy).

### Aide ?

[AppleOSer@gmail.com](mailto:AppleOSer@gmail.com) — en général sous 48 h.

</section>
<section lang="tr" markdown="1">

### Belirli bir aracı nasıl bulurum?

Arama çubuğu (English, 简体中文, 繁體中文).

### Sabitleme?

**⋯** veya **Ayarlar → Sabitlenen araçlar** (en fazla 8).

### Widget?

Uzun bas → **＋** → "iConverter" — **Ayarlar → Hakkında → Widget kılavuzu**.

### Çevrimdışı?

101 araç çevrimdışı; tarayıcı sayfaları için ağ gerekir.

### Veri?

Hayır — [Gizlilik](../privacy).

### Yardım?

[AppleOSer@gmail.com](mailto:AppleOSer@gmail.com)

</section>
