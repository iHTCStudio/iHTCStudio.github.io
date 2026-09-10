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
