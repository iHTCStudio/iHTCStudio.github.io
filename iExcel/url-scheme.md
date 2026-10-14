---
layout: doc
title: iExcel — Shortcut Links
app_id: iExcel
doc_title_en: Shortcut Links
doc_title_zh_cn: 快捷链接说明
doc_title_zh_tw: 快捷連結說明
description: iexcel:// shortcut links for iExcel — home, category, item, playground, quiz, search, favorites, and guides.
---

<section lang="en" markdown="1">

iExcel supports **`iexcel://`** shortcut links for Shortcuts, Safari bookmarks, widgets, and automation.

## Link format

```
iexcel://{host}?{params}
```

## Learning

| URL | Opens |
|-----|-------|
| `iexcel://playground` | Formula Playground |
| `iexcel://quiz` | Practice quizzes category |
| `iexcel://item?kind=function&id=SUM` | Function detail (e.g. SUM) |
| `iexcel://item?kind=tip&id={id}` | Tip detail |
| `iexcel://item?kind=lesson&id={id}` | Lesson detail |
| `iexcel://item?kind=quiz&id={id}` | Quiz detail |
| `iexcel://item?kind=shortcut&id={id}` | Shortcut detail |

### Item `kind` values

`function` · `tip` · `lesson` · `quiz` · `shortcut`

Function ids are typically uppercase names (e.g. `SUM`, `VLOOKUP`, `XLOOKUP`).

## Browse & search

| URL | Opens |
|-----|-------|
| `iexcel://home` | Home |
| `iexcel://category?id=popular` | Category by id |
| `iexcel://search` | Search tab |
| `iexcel://search?q=SUM` | Search with query |
| `iexcel://favorites` | Favorites tab |
| `iexcel://settings` | Settings |

### Common category ids

`popular` · `math` · `stat` · `text` · `logical` · `lookup` · `datetime` · `financial` · `info` · `array` · `engineering` · `database` · `tips` · `lessons` · `quizzes` · `shortcuts`

## Guides & actions

| URL | Opens |
|-----|-------|
| `iexcel://feature-guide` | Feature onboarding (replay) |
| `iexcel://widget-guide` | Widget guide |
| `iexcel://shortcuts-guide` | Shortcuts guide |
| `iexcel://usage-guide` | Usage guide |
| `iexcel://feedback` | Feedback email |
| `iexcel://in-app-review` | In-app App Store rating |

## Siri & App Shortcuts

Built-in phrases (English / 简体 / 繁體):

| Action | Example phrases |
|--------|-----------------|
| Open Home | “Open iExcel” / “打开 iExcel” / “開啟 iExcel” |
| Playground | “Open playground in iExcel” / “用 iExcel 打开演练场” |
| Quiz | “Start quiz in iExcel” / “用 iExcel 开始测验” |
| Function | “Open function in iExcel” (then provide the function name) |

`Search Content` is available as an App Intent in the Shortcuts app (not listed as a spoken App Shortcut phrase).

## Home Screen Quick Actions

Long-press the app icon:

| Action | Destination |
|--------|-------------|
| Home | Home tab |
| Playground | Formula Playground |
| Quiz | Quizzes category |
| Search | Search |

</section>
<section lang="zh-CN" markdown="1">

爱表格支持 **`iexcel://`** 快捷链接，可用于快捷指令、Safari 书签、小组件与自动化。

## 链接格式

```
iexcel://{host}?{params}
```

## 学习

| 链接 | 打开 |
|------|------|
| `iexcel://playground` | 公式演练场 |
| `iexcel://quiz` | 练习测验分类 |
| `iexcel://item?kind=function&id=SUM` | 函数详情（如 SUM） |
| `iexcel://item?kind=tip&id={id}` | 技巧详情 |
| `iexcel://item?kind=lesson&id={id}` | 课程详情 |
| `iexcel://item?kind=quiz&id={id}` | 测验详情 |
| `iexcel://item?kind=shortcut&id={id}` | 快捷键详情 |

### 条目 `kind` 取值

`function` · `tip` · `lesson` · `quiz` · `shortcut`

函数 id 一般为大写名称（如 `SUM`、`VLOOKUP`、`XLOOKUP`）。

## 浏览与搜索

| 链接 | 打开 |
|------|------|
| `iexcel://home` | 首页 |
| `iexcel://category?id=popular` | 按 id 打开分类 |
| `iexcel://search` | 搜索 |
| `iexcel://search?q=SUM` | 带关键词搜索 |
| `iexcel://favorites` | 收藏 Tab |
| `iexcel://settings` | 设置 |

### 常用分类 id

`popular` · `math` · `stat` · `text` · `logical` · `lookup` · `datetime` · `financial` · `info` · `array` · `engineering` · `database` · `tips` · `lessons` · `quizzes` · `shortcuts`

## 指南与操作

| 链接 | 打开 |
|------|------|
| `iexcel://feature-guide` | 功能引导（重播） |
| `iexcel://widget-guide` | 小组件指南 |
| `iexcel://shortcuts-guide` | 快捷指令指南 |
| `iexcel://usage-guide` | 使用说明 |
| `iexcel://feedback` | 反馈邮件 |
| `iexcel://in-app-review` | 应用内评分 |

## Siri 与快捷指令

内置短语（英文 / 简体 / 繁体）：

| 操作 | 示例说法 |
|------|----------|
| 打开首页 | “Open iExcel” / “打开 iExcel” / “開啟 iExcel” |
| 演练场 | “Open playground in iExcel” / “用 iExcel 打开演练场” |
| 测验 | “Start quiz in iExcel” / “用 iExcel 开始测验” |
| 函数 | “Open function in iExcel”（再提供函数名） |

`Search Content` 可作为 App Intent 在快捷指令 App 中调用（未注册为口语 App Shortcut 短语）。

## 主屏快捷操作

长按应用图标：

| 操作 | 目标 |
|------|------|
| Home | 首页 |
| Playground | 公式演练场 |
| Quiz | 测验分类 |
| Search | 搜索 |

</section>
<section lang="zh-TW" markdown="1">

愛表格支援 **`iexcel://`** 快捷連結，可用於捷徑、Safari 書籤、小工具與自動化。

## 連結格式

```
iexcel://{host}?{params}
```

## 學習

| 連結 | 開啟 |
|------|------|
| `iexcel://playground` | 公式演練場 |
| `iexcel://quiz` | 練習測驗分類 |
| `iexcel://item?kind=function&id=SUM` | 函數詳情（如 SUM） |
| `iexcel://item?kind=tip&id={id}` | 技巧詳情 |
| `iexcel://item?kind=lesson&id={id}` | 課程詳情 |
| `iexcel://item?kind=quiz&id={id}` | 測驗詳情 |
| `iexcel://item?kind=shortcut&id={id}` | 快捷鍵詳情 |

### 條目 `kind` 取值

`function` · `tip` · `lesson` · `quiz` · `shortcut`

函數 id 一般為大寫名稱（如 `SUM`、`VLOOKUP`、`XLOOKUP`）。

## 瀏覽與搜尋

| 連結 | 開啟 |
|------|------|
| `iexcel://home` | 首頁 |
| `iexcel://category?id=popular` | 依 id 開啟分類 |
| `iexcel://search` | 搜尋 |
| `iexcel://search?q=SUM` | 帶關鍵詞搜尋 |
| `iexcel://favorites` | 收藏 Tab |
| `iexcel://settings` | 設定 |

### 常用分類 id

`popular` · `math` · `stat` · `text` · `logical` · `lookup` · `datetime` · `financial` · `info` · `array` · `engineering` · `database` · `tips` · `lessons` · `quizzes` · `shortcuts`

## 指南與操作

| 連結 | 開啟 |
|------|------|
| `iexcel://feature-guide` | 功能引導（重播） |
| `iexcel://widget-guide` | 小工具指南 |
| `iexcel://shortcuts-guide` | 捷徑指南 |
| `iexcel://usage-guide` | 使用說明 |
| `iexcel://feedback` | 回饋郵件 |
| `iexcel://in-app-review` | 應用內評分 |

## Siri 與捷徑

內建短語（英文 / 簡體 / 繁體）：

| 操作 | 範例說法 |
|------|----------|
| 開啟首頁 | “Open iExcel” / “打开 iExcel” / “開啟 iExcel” |
| 演練場 | “Open playground in iExcel” / “用 iExcel 打开演练场” |
| 測驗 | “Start quiz in iExcel” / “用 iExcel 开始测验” |
| 函數 | “Open function in iExcel”（再提供函數名） |

`Search Content` 可作為 App Intent 在捷徑 App 中呼叫（未註冊為口語 App Shortcut 短語）。

## 主畫面快捷操作

長按應用圖示：

| 操作 | 目標 |
|------|------|
| Home | 首頁 |
| Playground | 公式演練場 |
| Quiz | 測驗分類 |
| Search | 搜尋 |

</section>
<section lang="ja" markdown="1">

iExcelは、ショートカット、Safariブックマーク、ウィジェット、および自動化のための**      **ショートカットリンクをサポートしています。

## リンク形式


```
iexcel://{host}?{params}
```


## 学習

| URL | 開く画面 |
|-----|-------|
| `iexcel://playground` | フォーミュラプレイグラウンド |
| `iexcel://quiz` | 練習クイズカテゴリ |
| `iexcel://item?kind=function&id=SUM` | 機能詳細(例:SUM) |
| `iexcel://item?kind=tip&id={id}` | ヒント詳細 |
| `iexcel://item?kind=lesson&id={id}` | レッスン詳細 |
| `iexcel://item?kind=quiz&id={id}` | クイズ詳細 |
| `iexcel://item?kind=shortcut&id={id}` | ショートカット詳細 |

### 項目 `iexcel://` 値



関数 ID は、通常、大文字 (例: `iexcel://` , `iexcel://playground` , `iexcel://quiz` ) です。

## 閲覧と検索

| URL | 開く画面 |
|-----|-------|
| `iexcel://home` | ホーム |
| `iexcel://category?id=popular` | idによるカテゴリ |
| `iexcel://search` | タブ検索 |
| `iexcel://search?q=SUM` | キーワード付き検索 |
| `iexcel://favorites` | お気に入りタブ |
| `iexcel://settings` | 設定 |

### 一般的なカテゴリ ids



## ガイド&アクション

| URL | 開く画面 |
|-----|-------|
| `iexcel://feature-guide` | 特徴 オンボーディング(再生) |
| `iexcel://widget-guide` | ウィジェットガイド |
| `iexcel://shortcuts-guide` | ショートカットガイド |
| `iexcel://usage-guide` | 使い方ガイド |
| `iexcel://feedback` | フィードバックメール |
| `iexcel://in-app-review` | アプリ内 App Store 評価 |

## Siri & App ショートカット

作り付けのフレーズ(英語/简体/繁體)

| Action | サンプルフレーズ |
|--------|-----------------|
| Open Home | 「iExcelを開く」/「iExcelを開く」/「iExcelを開く」 |
| Playground | 「iExcelで遊び場を開く」/「iExcelを使う」 |
| Quiz | 「iExcelでquizを起動する」/「iExcelで起動する」 |
| Function | “iExcelで機能を開く”(関数名を提供) | `iexcel://` は、ショートカットアプリでApp Intentとして利用できます(音声アプリのショートカットフレーズとしてリストされていない)。

## ホーム スクリーンの速い行為

アプリアイコンを長押し:

| Action | 目的地 |
|--------|-------------|
| Home | ホームタブ |
| Playground | フォーミュラプレイグラウンド |
| Quiz | クイズカテゴリ |
| Search | 検索 |

</section>
<section lang="ko" markdown="1">

iExcel은 ** `iexcel://` ** Shortcuts, Safari bookmarks, 위젯 및 자동화에 대한 단축 링크.

## 링크 형식


```
iexcel://{host}?{params}
```


## 학습

| URL | 열리는 화면 |
|-----|-------|
| `iexcel://playground` | 공식 놀이터 |
| `iexcel://quiz` | 연습 퀴즈 범주 |
| `iexcel://item?kind=function&id=SUM` | 기능 디테일(e.g. SUM) |
| `iexcel://item?kind=tip&id={id}` | 팁 세부 사항 |
| `iexcel://item?kind=lesson&id={id}` | 수업 세부 사항 |
| `iexcel://item?kind=quiz&id={id}` | Quiz 세부사항 |
| `iexcel://item?kind=shortcut&id={id}` | 바로가기 |

### Item `iexcel://` 값 `iexcel://` · `iexcel://playground` · `iexcel://quiz` · `iexcel://item?kind=function&id=SUM` · `iexcel://item?kind=tip&id={id}` 함수 에이즈는 일반적으로 상부 이름 (e.g. `iexcel://` , `iexcel://playground` , `iexcel://quiz` )입니다.

## 탐색 및 검색

| URL | 열리는 화면 |
|-----|-------|
| `iexcel://home` | 홈 |
| `iexcel://category?id=popular` | 카테고리 id |
| `iexcel://search` | 검색 탭 |
| `iexcel://search?q=SUM` | 검색어와 함께 검색 |
| `iexcel://favorites` | 즐겨찾기 탭 |
| `iexcel://settings` | 설정 |

### 일반 카테고리 ids `iexcel://` · `iexcel://playground` · `iexcel://quiz` · `iexcel://item?kind=function&id=SUM` · `iexcel://item?kind=tip&id={id}` · `iexcel://item?kind=lesson&id={id}` · `iexcel://item?kind=quiz&id={id}` · `iexcel://item?kind=shortcut&id={id}` · `kind` · `function` · `tip` · `lesson` · `quiz` · `shortcut` · `SUM` ## 가이드 & 행동

| URL | 열리는 화면 |
|-----|-------|
| `iexcel://feature-guide` | 기능 내장 (replay) |
| `iexcel://widget-guide` | 위젯 가이드 |
| `iexcel://shortcuts-guide` | 단축어 가이드 |
| `iexcel://usage-guide` | 사용 가이드 |
| `iexcel://feedback` | 피드백 이메일 |
| `iexcel://in-app-review` | 앱 내 App Store 평가 |

## Siri & 앱 바로가기

내장 구문 (English / 简体 / 繁體) :

| Action | 예제 구문 |
|--------|-----------------|
| Open Home | “iExcel” / “ i iExcel” / “ i iExcel” |
| Playground | “iExcel에서 열린 놀이터” / “iExcel Ex” |
| Quiz | “iExcel에서 퀴즈 시작” / “iExcel 开始测验” |
| Function | “iExcel에서 기능을 엽니다” (그 후에 기능 이름을 제공합니다) | `iexcel://` 는 Shortcuts 앱에서 App Intent로 사용할 수 있습니다. (말한 App Shortcut 구문으로 나열되지 않음).

## 홈 화면 빠른 행동

앱 아이콘을 길게 누릅니다:

| Action | 여행 정보 |
|--------|-------------|
| Home | 홈 탭 |
| Playground | 공식 놀이터 |
| Quiz | Quizzes 범주 |
| Search | 검색 |

</section>
<section lang="ru" markdown="1">

iExcel поддерживает ярлыки ** `iexcel://` ** для ярлыков, закладок Safari, виджетов и автоматизации.

## Формат ссылки


```
iexcel://{host}?{params}
```


## Обучение

| URL | Открывает |
|-----|-------|
| `iexcel://playground` | Игровая площадка Formula |
| `iexcel://quiz` | Категория практических викторин |
| `iexcel://item?kind=function&id=SUM` | Детали функции (например, SUM) |
| `iexcel://item?kind=tip&id={id}` | Подробнее |
| `iexcel://item?kind=lesson&id={id}` | Подробный урок |
| `iexcel://item?kind=quiz&id={id}` | Подробнее |
| `iexcel://item?kind=shortcut&id={id}` | Короткая деталь |

### Пункт `iexcel://` Функциональные идентификаторы, как правило, являются верхними именами (например, `iexcel://` , `iexcel://playground` , `iexcel://quiz` ).

## Обзор и поиск

| URL | Открывает |
|-----|-------|
| `iexcel://home` | Главная |
| `iexcel://category?id=popular` | Категория:ID |
| `iexcel://search` | Поисковая вкладка |
| `iexcel://search?q=SUM` | Поиск с запросом |
| `iexcel://favorites` | Любимая вкладка |
| `iexcel://settings` | Настройки |

### ids общей категории



## Руководство и действия

| URL | Открывает |
|-----|-------|
| `iexcel://feature-guide` | Особенности игры Onboarding (Replay) |
| `iexcel://widget-guide` | Руководство по виджетам |
| `iexcel://shortcuts-guide` | Руководство по «Командам» |
| `iexcel://usage-guide` | Руководство по использованию |
| `iexcel://feedback` | Письмо с отзывом |
| `iexcel://in-app-review` | Оценка в App Store из приложения |

## Обсуждение Siri & App Shortcuts

Встроенные фразы (английский / - / -):

| Action | Примерные фразы |
|--------|-----------------|
| Open Home | «Открытый iExcel» / «” iExcel» / «” iExcel» |
| Playground | «Открытая игровая площадка в iExcel» / «” iExcel ”» |
| Quiz | «Начать викторину в iExcel» / «” iExcel ” |
| Function | «Открытая функция в iExcel» (название функции) | `iexcel://` доступна в приложении «Намерение приложения» (не указана как произнесенная фраза «Ярлык приложения»).

## Домой Экран Быстрые действия

Дальше нажмите значок приложения:

| Action | Направление |
|--------|-------------|
| Home | Вкладка «Главная» |
| Playground | Игровая площадка Formula |
| Quiz | Категория Quizzs |
| Search | Поиск |

</section>
<section lang="th" markdown="1">

i Excel รองรับ} `iexcel://` BAR -~ ลิงก์ลัดสําหรับปุ่มพิมพ์ลัด, คั่นหน้า Safari, วิดเจ็ต และอัตโนมัติ

## รูปแบบลิงก์


```
iexcel://{host}?{params}
```


## การเรียนรู้

| URL | เปิด |
|-----|-------|
| `iexcel://playground` | พื้นเล่นสูตร |
| `iexcel://quiz` | ข้อสอบประเภท |
| `iexcel://item?kind=function&id=SUM` | รายละเอียดการทํางาน (เช่น Sum) |
| `iexcel://item?kind=tip&id={id}` | รายละเอียด |
| `iexcel://item?kind=lesson&id={id}` | รายละเอียดบทเรียน |
| `iexcel://item?kind=quiz&id={id}` | รายละเอียด Quiz |
| `iexcel://item?kind=shortcut&id={id}` | รายละเอียดปุ่มพิมพ์ลัด |

### เ พิ่มค่าของรายการ `iexcel://` BAR `iexcel://playground` C2                                                                  .

IDs มักเป็นชื่อตัวใหญ่ (เช่น `iexcel://` , `iexcel://playground` )

## เรียกดูและค้นหา

| URL | เปิด |
|-----|-------|
| `iexcel://home` | หน้าแรก |
| `iexcel://category?id=popular` | หมวดหมู่โดยหมายเลข |
| `iexcel://search` | ค้นหาในแท็บ |
| `iexcel://search?q=SUM` | ค้นหาพร้อมคำค้น |
| `iexcel://favorites` | แท็บโปรด |
| `iexcel://settings` | การตั้งค่า |

### หมายเลขหมวดหมู่ทั่วไป `iexcel://item?kind=function&id=SUM` ## ทิศทางการทํางาน

| URL | เปิด |
|-----|-------|
| `iexcel://feature-guide` | คุณสมบัติบน (เล่น) |
| `iexcel://widget-guide` | คู่มือวิดเจ็ต |
| `iexcel://shortcuts-guide` | คู่มือทางลัด |
| `iexcel://usage-guide` | คู่มือการใช้งาน |
| `iexcel://feedback` | อีเมลข้อเสนอแนะ |
| `iexcel://in-app-review` | ให้คะแนน App Store ในแอป |

## ปุ่มพิมพ์ลัดของ Siri & App

วลีที่ประกอบขึ้นเอง (อังกฤษ / 简体 / 繁體) พ.ศ.

| Action | วลีตัวอย่าง |
|--------|-----------------|
| Open Home | "เปิด IExchel" / "IExchel" / "IExchel" |
| Playground | “ เปิดสนามเด็กเล่นในไอเอ็กซ์เซล" / "IExchel 打开演练场" |
| Quiz | "เริ่มทดสอบใน iExchel" / "用 IExchel 开始测验" |
| Function | “ เปิดการทํางานใน iExchel" (จากนั้นให้ชื่อฟังก์ชัน) | `iexcel://` BAR มีการใช้งานเป็น App Infinting ในโปรแกรมปุ่มพิมพ์ลัด (ไม่มีรายการเป็นวลีปุ่มพิมพ์ลัดที่ใช้พูด)

## การกระทําด่วนของจอส่วนตัว

กดเมาส์แบบยาว:

| Action | ปลายทาง |
|--------|-------------|
| Home | แท็บหน้าแรก |
| Playground | พื้นเล่นสูตร |
| Quiz | ประเภท Quizes |
| Search | ค้นหา |

</section>
<section lang="de" markdown="1">

iExcel unterstützt ** `iexcel://` ** Shortcut-Links für Shortcuts, Safari-Lesezeichen, Widgets und Automatisierung.

## Linkformat


```
iexcel://{host}?{params}
```


## Lernen

| URL | Öffnet |
|-----|-------|
| `iexcel://playground` | Formelspielplatz |
| `iexcel://quiz` | Kategorie Praxis Quiz |
| `iexcel://item?kind=function&id=SUM` | Funktionsdetail (z. B. SUMME) |
| `iexcel://item?kind=tip&id={id}` | Angaben zur Spitze |
| `iexcel://item?kind=lesson&id={id}` | Einzelheiten der Lektion |
| `iexcel://item?kind=quiz&id={id}` | Quizdetail |
| `iexcel://item?kind=shortcut&id={id}` | Abkürzung |

### Element `iexcel://` -Werte `iexcel://` · `iexcel://playground` · `iexcel://quiz` · `iexcel://item?kind=function&id=SUM` · `iexcel://item?kind=tip&id={id}` Funktions-IDs sind typischerweise Großbuchstabennamen (z. B. `iexcel://` , `iexcel://playground` , `iexcel://quiz` ).

## Durchsuchen & Suche

| URL | Öffnet |
|-----|-------|
| `iexcel://home` | Startseite |
| `iexcel://category?id=popular` | Kategorie nach ID |
| `iexcel://search` | Suchtipp |
| `iexcel://search?q=SUM` | Suche mit Suchbegriff |
| `iexcel://favorites` | Favoriten-Tab |
| `iexcel://settings` | Einstellungen |

### Gemeinsame Kategorie-IDs `iexcel://` · `iexcel://playground` · `iexcel://quiz` · `iexcel://item?kind=function&id=SUM` · `iexcel://item?kind=tip&id={id}` · `iexcel://item?kind=lesson&id={id}` · `iexcel://item?kind=quiz&id={id}` · `iexcel://item?kind=shortcut&id={id}` · `kind` · `function` · `tip` · `lesson` · `quiz` · `shortcut` · `SUM` ## Leitfäden und Maßnahmen

| URL | Öffnet |
|-----|-------|
| `iexcel://feature-guide` | Feature Onboarding (Wiederholung) |
| `iexcel://widget-guide` | Widget-Anleitung |
| `iexcel://shortcuts-guide` | Kurzbefehle-Anleitung |
| `iexcel://usage-guide` | Nutzungsanleitung |
| `iexcel://feedback` | Feedback-E-Mail |
| `iexcel://in-app-review` | App-Store-Bewertung in der App |

## Siri & App Shortcuts

Eingebaute Sätze (englisch / 简体 / 繁體):

| Action | Beispielsätze |
|--------|-----------------|
| Open Home | “Open iExcel” / “打开 iExcel” / “開啟 iExcel” |
| Playground | „Offener Spielplatz in iExcel“ / „用 iExcel 打开演练场“ |
| Quiz | „Start quiz in iExcel“ / „用 iExcel 开始测验“ |
| Function | „Funktion in iExcel öffnen (dann den Funktionsnamen angeben) | `iexcel://` ist als App Intent in der Shortcuts App verfügbar (nicht als gesprochene App Shortcut Phrase aufgeführt).

## Home Bildschirm Schnelle Aktionen

Langes Drücken des App-Icons:

| Action | Bestimmungsort |
|--------|-------------|
| Home | Register „Start“ |
| Playground | Formelspielplatz |
| Quiz | Quizkategorie |
| Search | Suche |

</section>
<section lang="fr" markdown="1">

iExcel prend en charge ** `iexcel://` ** liens raccourcis pour raccourcis, signets Safari, widgets et l'automatisation.

## Format de lien


```
iexcel://{host}?{params}
```


## Apprentissage

| URL | Ouvre |
|-----|-------|
| `iexcel://playground` | Terrain de jeu Formule |
| `iexcel://quiz` | Catégorie de quiz pratique |
| `iexcel://item?kind=function&id=SUM` | Détails de la fonction (par exemple SUM) |
| `iexcel://item?kind=tip&id={id}` | Détails du tuyau |
| `iexcel://item?kind=lesson&id={id}` | Détails de la leçon |
| `iexcel://item?kind=quiz&id={id}` | Détails du quiz |
| `iexcel://item?kind=shortcut&id={id}` | Raccourci |

### Valeurs de l'élément `iexcel://` C0    · `iexcel://playground` · `iexcel://quiz` · `iexcel://item?kind=function&id=SUM` · `iexcel://item?kind=tip&id={id}` Les id de fonction sont généralement des noms majuscules (p. ex. `iexcel://` , `iexcel://playground` , `iexcel://quiz` ).

## Parcourir et rechercher

| URL | Ouvre |
|-----|-------|
| `iexcel://home` | Accueil |
| `iexcel://category?id=popular` | Catégorie par id |
| `iexcel://search` | Onglet Recherche |
| `iexcel://search?q=SUM` | Recherche avec requête |
| `iexcel://favorites` | Onglet Favoris |
| `iexcel://settings` | Réglages |

### Identificateurs de catégorie communs `iexcel://` · `iexcel://playground` · `iexcel://quiz` · `iexcel://item?kind=function&id=SUM` · `iexcel://item?kind=tip&id={id}` · `iexcel://item?kind=lesson&id={id}` · `iexcel://item?kind=quiz&id={id}` · `iexcel://item?kind=shortcut&id={id}` · `kind` · `function` · `tip` · `lesson` · `quiz` · `shortcut` · `SUM` · `VLOOKUP` ## Guides et actions

| URL | Ouvre |
|-----|-------|
| `iexcel://feature-guide` | Fonctionnalité à bord (rejouer) |
| `iexcel://widget-guide` | Guide des widgets |
| `iexcel://shortcuts-guide` | Guide Raccourcis |
| `iexcel://usage-guide` | Guide d'utilisation |
| `iexcel://feedback` | E-mail de commentaires |
| `iexcel://in-app-review` | Note App Store in-app |

## Raccourcis Siri & App

Expressions intégrées (anglais / 简体 / 简ш):

| Action | Exemple de phrases |
|--------|-----------------|
| Open Home | Ouvrir iExcel |
| Playground | Ouvrir le terrain de jeux dans iExcel |
| Quiz | Démarrer le quiz dans iExcel |
| Function | Fonction ouverte dans iExcel (fournissez alors le nom de la fonction) | `iexcel://` ## Actions rapides de l'écran d'accueil

Appuyez longuement sur l'icône de l'application :

| Action | Destination |
|--------|-------------|
| Home | Onglet Accueil |
| Playground | Terrain de jeu Formule |
| Quiz | Catégorie de quiz |
| Search | Recherche |

</section>
<section lang="tr" markdown="1">

iExcel, ** `iexcel://` ** Kısa kesimler için kısa bağlantılar, Safari kitap işaretleri, widgets ve otomasyon.

## Bağlantı biçimi


```
iexcel://{host}?{params}
```


## Öğrenme

| URL | Açar |
|-----|-------|
| `iexcel://playground` | Formula Playground |
| `iexcel://quiz` | Uygulama testleri |
| `iexcel://item?kind=function&id=SUM` | Fonksiyonlar detay (e.g. SUM) |
| `iexcel://item?kind=tip&id={id}` | İpucu detayı |
| `iexcel://item?kind=lesson&id={id}` | Lesson detay |
| `iexcel://item?kind=quiz&id={id}` | Quiz detayı |
| `iexcel://item?kind=shortcut&id={id}` | Kısa detay |

### Item `iexcel://` values `iexcel://` · `iexcel://playground` · `iexcel://quiz` · `iexcel://item?kind=function&id=SUM` Fonksiyonlar genellikle üst harf isimleridir (örneğin, `iexcel://` , `iexcel://playground` , `iexcel://quiz` ).

## Gözat ve ara

| URL | Açar |
|-----|-------|
| `iexcel://home` | Ana sayfa |
| `iexcel://category?id=popular` | Kategori: |
| `iexcel://search` | Arama sekmesi |
| `iexcel://search?q=SUM` | Sorgu ile arama |
| `iexcel://favorites` | Favoriler sekmesi |
| `iexcel://settings` | Ayarlar |

### Ortak kategori ids `iexcel://` · `iexcel://playground` · `iexcel://quiz` · `iexcel://item?kind=tip&id={id}` · `iexcel://item?kind=lesson&id={id}` · `iexcel://item?kind=quiz&id={id}` · `iexcel://item?kind=shortcut&id={id}` · `iexcel://item?kind=shortcut&id={id}` · `function` · `tip` · `lesson` · `quiz` ·  C  C   9

## Rehberler ve eylemler

| URL | Açar |
|-----|-------|
| `iexcel://feature-guide` | boarding (replay) |
| `iexcel://widget-guide` | Widget kılavuzu |
| `iexcel://shortcuts-guide` | Kısayol kılavuzu |
| `iexcel://usage-guide` | Kullanım kılavuzu |
| `iexcel://feedback` | Geri bildirim e-postası |
| `iexcel://in-app-review` | Uygulama içi App Store puanı |

## Siri & App Kısakes

Yerleşik cümleler (İngilizce / 简体 / 繁體):

| Action | Örnek cümleleri |
|--------|-----------------|
| Open Home | "Açık iExcel" / " i iExcel" / " i iExcel" |
| Playground | "Açıkçası" / "Ex iExcel 打开演练场" |
| Quiz | "IExcel" / "Ex iExcel 开始测验" |
| Function | "Open function in iExcel" (sonunda işlev adı sağlar) | `iexcel://` , Shortcuts uygulamasında bir App niyet olarak kullanılabilir (Konuşmalı App Kısakes cümlesi olarak listelenme).

## Home Screen Quick Actions

Uygulama ikonunu uzun baskı:

| Action | Hedef |
|--------|-------------|
| Home | Ana sayfa sekmesi |
| Playground | Formula Playground |
| Quiz | Quizzes kategorisi |
| Search | Ara |

</section>
