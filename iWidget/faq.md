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
<section lang="ja" markdown="1">

### iWidget はカレンダーアプリですか？

いいえ。**ウィジェットデザインスタジオ**です。カレンダー、天気、カウントダウンはグリッド上の **ブロック**。**今日** タブはダッシュボード；ホーム画面ウィジェットは **マイウィジェット** の **保存済みデザイン** を使います。

### iCalendar との違いは？

別製品・UI・アイコン・ウィジェットスタイル。iWidget は **ブロックレイアウト**、**壁紙トーン**、**透明スロット**、**タップシールド** が中心。农历表は iCalendar 系譜ですが App Store 上は別アプリです。

### ホーム画面ウィジェットの追加方法は？

1. **マイウィジェット** にデザインを保存（ライブラリまたはエディタから）
2. ホーム画面長押し → **＋** → **iWidget** を検索
3. デザイン族に合う **小/中/大** を選択
4. **ウィジェットを編集** → サイズ別リストからデザインを選択

詳細：**設定 → ヘルプ → ウィジェットを追加**。

### 期待どおりのデザインが表示されない？

- サイズはデザイン族と一致（小ボード → 小ウィジェット）
- 削除後も古い UUID を指す場合 — アプリで **失効デザイン** バナーを確認し、ウィジェット設定で再選択
- **設定 → データ → ウィジェットを更新** でタイムライン再読み込み

### タップシールド（インターセプト）とは？

**インターセプト** オン時、タップしても **アプリを開きません** — 壁紙風ボード向け。エディタ **動作** またはウィジェット設定でオフにすると `iwidget://today` を開けます。

### 透明ウィジェットの使い方？

明暗 **壁紙スクショ** を **スロットごと** に切り抜き、ウィジェット設定で透明背景を有効化。**ウィジェットを追加** ガイド参照。

### オフラインで使えますか？

**农历・黄历・エディタ・描画** はオフライン。**天気** は WeatherKit で更新時にネット必要。**祝日 JSON** は時々オンライン更新。**フォント** は初回選択時にダウンロードの場合あり。

### アカウントは必要？

**不要。** 任意 **iCloud** は Apple CloudKit — iHTC Studio アカウントではありません。

### iCloud は何を同期？

デザイン JSON と切り抜き壁紙（私有 **Designs** ゾーン）。既定オフ。オフ後もローカルは削除するまで残ります。

### 通知の仕組みは？

すべて **ローカル** — 休暇前夜、祝日/节气、カウントダウン朝など、最大 **48** 件。**設定 → 通知** で種類を切替。

### 対応言語は？

**設定 → 外観 → 言語**：システム、简体中文、繁體中文、English。iOS のウィジェット picker は **システム言語** に従います。

### Siri とショートカット？

例：*「iWidget で今日の农历」*、*「iWidget で次の祝日」*。**Workday** Intent は日付指定で Shortcuts に手動追加。URL：[URL Scheme](../url-scheme)。

### 個人データを収集しますか？

いいえ。[プライバシーポリシー](../privacy)：Data Not Collected；WeatherKit/HealthKit/位置情報は有効時のみ。

### 無料ですか？

**有料ダウンロード。** 機能解放 IAP なし — **設定 → について** の任意 **開発者チップ** のみ。

### App Store にありますか？

Apple ID **6817595772**。地域未公開なら本サポートページをブックマーク；[App Store リンク](https://apps.apple.com/app/id6817595772) は公開後に有効。

### まだ助けが必要ですか？

[AppleOSer@gmail.com](mailto:AppleOSer@gmail.com) — 通常 48 時間以内。

</section>
<section lang="ko" markdown="1">

### iWidget는 달력 앱인가요?

아닙니다. **위젯 디자인 스튜디오**입니다. 달력·날씨·카운트다운은 그리드 **블록**입니다. **오늘** 탭은 대시보드이며, 홈 화면 위젯은 **내 위젯**의 **저장된 디자인**을 사용합니다.

### iCalendar와 차이?

별도 제품·UI·아이콘·위젯 스타일. iWidget은 **블록 배치**, **배경화면 톤**, **투명 슬롯**, **탭 방지**에 중점. 음력 데이터는 iCalendar 계보이나 App Store에서는 별도 앱입니다.

### 홈 화면 위젯 추가?

1. **내 위젯**에 디자인 저장
2. 홈 화면 길게 누르기 → **＋** → **iWidget** 검색
3. **소/중/대** 크기 선택
4. **위젯 편집** → 디자인 선택

**설정 → 도움말 → 위젯 추가** 참고.

### 디자인이 맞지 않을 때?

- 크기와 디자인族 일치
- 삭제 후 UUID 불일치 → **만료된 디자인** 배너 후 재선택
- **설정 → 데이터 → 위젯 새로고침**

### 탭 방지(가로채기)?

켜면 탭해도 **앱이 열리지 않음**. 끄면 `iwidget://today` 가능.

### 투명 위젯?

밝/어두운 **배경화면 캡처**를 **슬롯별** 자르고 투명 배경 활성화.

### 오프라인?

**음력·황历·편집기·렌더링** 오프라인. **날씨**는 WeatherKit 갱신 시 네트워크. **공휴일 JSON**은 가끔 온라인.

### 계정?

**불필요.** 선택 **iCloud**는 CloudKit.

### iCloud 동기화?

디자인 JSON·잘린 배경화면( **Designs** ). 기본 꺼짐.

### 알림?

**로컬**만, 최대 **48**개. **설정 → 알림**.

### 언어?

**설정 → 모양 → 언어**: 시스템, 简体中文, 繁體中文, English.

### Siri·Shortcuts?

*「iWidget 오늘 음력」* 등. **Workday** Intent는 Shortcuts에 수동 추가. [URL Scheme](../url-scheme).

### 개인정보?

아니요. [개인정보 처리방침](../privacy).

### 무료?

**유료 다운로드.** 기능 잠금 IAP 없음.

### App Store?

ID **6817595772**. [App Store](https://apps.apple.com/app/id6817595772).

### 도움?

[AppleOSer@gmail.com](mailto:AppleOSer@gmail.com).

</section>
<section lang="ru" markdown="1">

### iWidget — это календарь?

Нет, это **студия дизайна виджетов**. Календарь, погода и обратный отсчёт — **блоки** на сетке. **Сегодня** — панель; виджеты дома используют **сохранённые макеты** из **Мои виджеты**.

### Отличие от iCalendar?

Отдельный продукт и UI. Акцент: **блоки**, **тон обоев**, **прозрачные слоты**, **защита от нажатий**. Лунные таблицы родственны iCalendar, в App Store — разные приложения.

### Добавить виджет?

Сохранить макет → долгое нажатие → **＋** → **iWidget** → размер → **Изменить виджет**. **Настройки → Справка → Добавление виджетов**.

### Неверный макет?

Размер; **устаревший макет**; **Настройки → Данные → Обновить виджеты**.

### Защита от нажатий?

При **перехвате** приложение **не открывается** — для «обоев». Выключите для `iwidget://today`.

### Прозрачные виджеты?

Скриншоты обоев, обрезка **по слотам**, прозрачный фон.

### Офлайн?

Календарь/альманах/редактор — да; **погода** — WeatherKit онлайн.

### Аккаунт?

**Не нужен.** iCloud опционально.

### iCloud?

JSON макетов и обои (**Designs**).

### Уведомления?

Только **локальные** (до **48**).

### Языки?

**Настройки → Оформление → Язык**.

### Siri?

[URL Scheme](../url-scheme).

### Данные?

Нет — [Конфиденциальность](../privacy).

### Цена?

**Платная загрузка**, без IAP функций.

### App Store?

**6817595772** — [ссылка](https://apps.apple.com/app/id6817595772).

### Помощь?

[AppleOSer@gmail.com](mailto:AppleOSer@gmail.com).

</section>
<section lang="th" markdown="1">

### iWidget เป็นแอปปฏิทินหรือไม่?

ไม่ — เป็น **สตูดิออกแบบวิดเจ็ต** ปฏิทิน สภาพอากาศ และนับถอยหลังคือ **บล็อก** แท็บ **วันนี้** เป็นหน้าสรุป วิดเจ็ตหน้าจอโฮมใช้ **ดีไซน์ที่บันทึก** ใน **วิดเจ็ตของฉัน**

### ต่างจาก iCalendar?

ผลิตภัณฑ์ UI และไอคอนคนละชุด เน้น **เลย์เอาต์บล็อก** **โทนวอลเปเปอร์** **ช่องโปร่งใส** **กันแตะพลาด**

### เพิ่มวิดเจ็ตหน้าจอโฮม?

บันทึกดีไซน์ → กดค้าง → **＋** → **iWidget** → เลือกขนาด → **แก้ไขวิดเจ็ต** — **การตั้งค่า → ความช่วยเหลือ → เพิ่มวิดเจ็ต**

### ดีไซน์ไม่ตรง?

ขนาดต้องตรง **ดีไซน์หมดอายุ** **การตั้งค่า → ข้อมูล → รีเฟรชวิดเจ็ต**

### กันแตะพลาด?

เปิด **ดักแตะ** แล้วแตะ **ไม่เปิดแอป** — ปิดเพื่อ `iwidget://today`

### วิดเจ็ตโปร่งใส?

จับภาพวอลเปเปอร์ ครอบ **ตามช่อง** เปิดพื้นหลังโปร่งใส

### ออฟไลน์?

ปฏิทิน/ฮ่องเต้/ตัวแก้ไขได้ **สภาพอากาศ** ต้องใช้เน็ต

### บัญชี?

**ไม่ต้อง** iCloud ทางเลือก

### iCloud?

JSON ดีไซน์ + วอลเปเปอร์ (**Designs**)

### การแจ้งเตือน?

**เฉพาะในเครื่อง** สูงสุด **48**

### ภาษา?

**การตั้งค่า → รูปลักษณ์ → ภาษา**

### Siri?

[URL Scheme](../url-scheme)

### ข้อมูลส่วนตัว?

ไม่ — [นโยบายความเป็นส่วนตัว](../privacy)

### ราคา?

**ดาวน์โหลดแบบเสียเงิน**

### App Store?

**6817595772** — [ลิงก์](https://apps.apple.com/app/id6817595772)

### ช่วยเหลือ?

[AppleOSer@gmail.com](mailto:AppleOSer@gmail.com)

</section>
<section lang="de" markdown="1">

### Ist iWidget eine Kalender-App?

Nein — ein **Widget-Design-Studio**. Kalender, Wetter und Countdowns sind **Blöcke** auf einem Raster. Der Tab **Heute** ist ein Dashboard; Home-Widgets nutzen **gespeicherte Designs** unter **Meine Widgets**.

### Unterschied zu iCalendar?

Eigenes Produkt, UI, Icons und Stile. Fokus: **Block-Layout**, **Hintergrundtönung**, **transparente Slots**, **Tippschutz**. Lunar-Tabellen teilen Herkunft mit iCalendar, separater App-Store-Eintrag.

### Home-Widget hinzufügen?

1. Design in **Meine Widgets** speichern  
2. Home long press → **＋** → **iWidget**  
3. **S/M/L** passend zur Design-Familie  
4. **Widget bearbeiten** → Design wählen  

**Einstellungen → Hilfe → Widgets hinzufügen**.

### Falsches Design?

Größe muss passen; nach Löschen ggf. **veraltetes Design** — im Editor neu wählen; **Einstellungen → Daten → Widgets aktualisieren**.

### Tippschutz?

Mit **Abfangen** öffnet Tippen **nicht** die App — für Wallpaper-Boards. Aus für `iwidget://today`.

### Transparente Widgets?

Hell/dunkel **Wallpaper-Screenshots**, **pro Slot** zuschneiden, transparent aktivieren.

### Offline?

Kalender/Almanach/Editor offline; **Wetter** braucht Netz (WeatherKit).

### Konto?

**Nein.** Optional **iCloud** via CloudKit.

### iCloud?

Design-JSON + zugeschnittene Wallpapers (**Designs**), standardmäßig aus.

### Benachrichtigungen?

Nur **lokal**, bis **48**. **Einstellungen → Mitteilungen**.

### Sprachen?

**Einstellungen → Erscheinungsbild → Sprache** — System, 简体, 繁体, English.

### Siri & Kurzbefehle?

Siehe [URL Scheme](../url-scheme). **Workday**-Intent manuell in Kurzbefehle.

### Datenerfassung?

Nein — [Datenschutz](../privacy).

### Kosten?

**Kostenpflichtiger Download**, keine Feature-IAP.

### App Store?

ID **6817595772** — [Link](https://apps.apple.com/app/id6817595772).

### Hilfe?

[AppleOSer@gmail.com](mailto:AppleOSer@gmail.com).

</section>
<section lang="fr" markdown="1">

### iWidget est-il une app calendrier ?

Non — un **studio de conception de widgets**. Calendrier, météo et comptes à rebours sont des **blocs**. L’onglet **Aujourd’hui** est un tableau de bord ; les widgets d’accueil utilisent les **designs enregistrés** dans **Mes widgets**.

### Différence avec iCalendar ?

Produit, UI, icônes et styles distincts. Accent : **mise en page**, **teinte du fond**, **emplacements transparents**, **bouclier anti-tap**. Tables lunaires liées à iCalendar, apps séparées sur l’App Store.

### Ajouter un widget d’accueil ?

Enregistrer un design → appui long → **＋** → **iWidget** → taille **S/M/L** → **Modifier le widget** → choisir le design. **Réglages → Aide → Ajouter des widgets**.

### Mauvais design affiché ?

Taille cohérente ; bannière **design obsolète** ; **Réglages → Données → Actualiser les widgets**.

### Bouclier anti-tap ?

Si **intercepter** est actif, le tap **n’ouvre pas** l’app — utile pour fond d’écran. Désactiver pour `iwidget://today`.

### Widgets transparents ?

Captures **clair/sombre**, recadrage **par emplacement**, fond transparent.

### Hors ligne ?

Calendrier/almanach/éditeur oui ; **météo** via WeatherKit en ligne.

### Compte ?

**Non.** iCloud optionnel (CloudKit).

### iCloud ?

JSON de design + fonds recadrés (**Designs**), désactivé par défaut.

### Notifications ?

**Locales** uniquement (max **48**).

### Langues ?

**Réglages → Apparence → Langue** — système, 简体, 繁体, English.

### Siri & Raccourcis ?

[Voir URL Scheme](../url-scheme).

### Données ?

Non — [Confidentialité](../privacy).

### Gratuit ?

**App payante**, pas d’IAP de déblocage.

### App Store ?

ID **6817595772** — [lien](https://apps.apple.com/app/id6817595772).

### Aide ?

[AppleOSer@gmail.com](mailto:AppleOSer@gmail.com).

</section>
<section lang="tr" markdown="1">

### iWidget takvim uygulaması mı?

Hayır — **widget tasarım stüdyosu**. Takvim, hava ve geri sayımlar **bloklardır**. **Bugün** sekmesi özet panelidir; Ana ekran widget'ları **Widget'larım**daki **kayıtlı tasarımları** kullanır.

### iCalendar farkı?

Ayrı ürün ve arayüz. **Blok düzeni**, **duvar kâğıdı tonu**, **şeffaf yuvalar**, **dokunma kalkanı**.

### Ana ekran widget'ı?

Tasarım kaydet → uzun bas → **＋** → **iWidget** → boyut → **Widget'ı Düzenle**. **Ayarlar → Yardım → Widget ekle**.

### Yanlış tasarım?

Boyut eşleşmesi; **eski tasarım** uyarısı; **Ayarlar → Veri → Widget'ları yenile**.

### Dokunma kalkanı?

**Yakala** açıkken uygulama **açılmaz** — `iwidget://today` için kapatın.

### Şeffaf widget?

Açık/koyu **duvar kâğıdı**, **yuva** kırpma, şeffaf arka plan.

### Çevrimdışı?

Takvim/almanak/editör evet; **hava** WeatherKit ile çevrimiçi.

### Hesap?

**Gerekmez.** İsteğe bağlı **iCloud**.

### iCloud?

Tasarım JSON + kırpılmış duvar kâğıtları (**Designs**).

### Bildirimler?

Yalnızca **yerel** (en fazla **48**).

### Diller?

**Ayarlar → Görünüm → Dil**.

### Siri?

[URL Scheme](../url-scheme).

### Veri?

Hayır — [Gizlilik](../privacy).

### Ücret?

**Ücretli indirme**, özellik IAP yok.

### App Store?

**6817595772** — [bağlantı](https://apps.apple.com/app/id6817595772).

### Yardım?

[AppleOSer@gmail.com](mailto:AppleOSer@gmail.com).

</section>
