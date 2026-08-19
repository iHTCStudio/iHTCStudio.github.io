---
layout: doc
title: iSutra — Shortcut Links
app_id: iSutra
doc_title_en: Shortcut Links
doc_title_zh_cn: 快捷链接说明
doc_title_zh_tw: 快捷連結說明
description: isutra:// deep links for iSutra — passage, daily, recite, study, hunt, chant, copy, practice, collections, themes, settings guides, and more.
---

<section lang="en" markdown="1">

iSutra supports **`isutra://`** shortcut links (URL scheme). Cold start and Home Screen shortcuts are delivered through a unified buffer so links are not opened twice after onboarding.

## Link format

```
isutra://{host}?{params}
```

## Sutras & authors

| URL | Opens |
|-----|-------|
| `isutra://passage?id={id}` | Sutra detail |
| `isutra://couplet?id={id}` / `isutra://poem?id={id}` | Same as passage (compatibility) |
| `isutra://author?id={id}` | Translator / author detail |
| `isutra://recite` / `isutra://recite?id={id}` | Recite flow |
| `isutra://large?id=diamond` / `isutra://large?id=dizang` | Large-book volume catalog |

## Discovery & practice

| URL | Opens |
|-----|-------|
| `isutra://home` | Home |
| `isutra://daily` | Today’s Daily Sutra |
| `isutra://random` | Random passage |
| `isutra://favorites` | Favorites |
| `isutra://famous` | Famous lines |
| `isutra://search` / `isutra://search?q={query}` | Search |
| `isutra://study` | Study Hall |
| `isutra://hunt` | Hunt (寻经); aliases `keyword-hunt` / `flyflower` |
| `isutra://count` | Wooden-fish chant (`chant` / `muyu` / `counter`) |
| `isutra://copy` / `isutra://copy?id={id}` | Copy-sutra (iOS) |
| `isutra://practice` | Morning / evening practice |
| `isutra://mastered` | Mastered |
| `isutra://categories` / `isutra://categories?section=` | Browse |
| `isutra://collection?id=` | Collection (e.g. `prajna`, `forty-two`; also `name=`) |
| `isutra://theme?id=` | Theme (e.g. `xingyuan`, `yaoshi`, `platform`) |
| `isutra://last-read` | Last read |
| `isutra://reading-history` | Reading history |
| `isutra://notes` | Notes |

## Settings & guides

| URL | Opens |
|-----|-------|
| `isutra://settings` | Settings |
| `isutra://usage-guide` | Usage guide |
| `isutra://widget-guide` | Widget guide |
| `isutra://shortcuts-guide` | Shortcuts guide |
| `isutra://feature-guide` | Replay onboarding |
| `isutra://privacy` | In-app privacy |
| `isutra://feedback` | Feedback email |
| `isutra://in-app-review` | In-app / Store review entry |

## Examples

```
isutra://daily
isutra://passage?id=1
isutra://large?id=diamond
isutra://count
isutra://copy?id=1
isutra://practice
isutra://collection?id=prajna
isutra://theme?id=xingyuan
isutra://study
isutra://hunt
```

Use these in the Shortcuts app, Home Screen quick actions, widgets, or Safari. See also in-app **Settings → Shortcuts Guide**.

</section>

<section lang="zh-CN" markdown="1">

爱佛经支持 **`isutra://`** 快捷链接（URL Scheme）。冷启动与主屏快捷经统一缓冲投递，避免引导后重复打开。

## 链接格式

```
isutra://{host}?{params}
```

## 经目与译者

| URL | 打开 |
|-----|------|
| `isutra://passage?id={id}` | 经文详情 |
| `isutra://couplet?id={id}` / `isutra://poem?id={id}` | 同上（兼容别名） |
| `isutra://author?id={id}` | 译者详情 |
| `isutra://recite` / `isutra://recite?id={id}` | 诵经 |
| `isutra://large?id=diamond` / `isutra://large?id=dizang` | 大部头分卷目录 |

## 发现与修习

| URL | 打开 |
|-----|------|
| `isutra://home` | 首页 |
| `isutra://daily` | 今日一经 |
| `isutra://random` | 随机经文 |
| `isutra://favorites` | 收藏 |
| `isutra://famous` | 法语 |
| `isutra://search` / `isutra://search?q={query}` | 搜索 |
| `isutra://study` | 持诵学堂 |
| `isutra://hunt` | 寻经（别名 `keyword-hunt` / `flyflower`） |
| `isutra://count` | 木鱼念诵（`chant` / `muyu` / `counter`） |
| `isutra://copy` / `isutra://copy?id={id}` | 抄经（iOS） |
| `isutra://practice` | 早晚功课 |
| `isutra://mastered` | 已掌握 |
| `isutra://categories` / `isutra://categories?section=` | 分类浏览 |
| `isutra://collection?id=` | 合集（如 `prajna`、`forty-two`；亦支持 `name=`） |
| `isutra://theme?id=` | 主题（如 `xingyuan`、`yaoshi`、`platform`） |
| `isutra://last-read` | 最近阅读 |
| `isutra://reading-history` | 浏览记录 |
| `isutra://notes` | 笔记 |

## 设置与指南

| URL | 打开 |
|-----|------|
| `isutra://settings` | 设置 |
| `isutra://usage-guide` | 使用说明 |
| `isutra://widget-guide` | 小组件指南 |
| `isutra://shortcuts-guide` | 快捷指南 |
| `isutra://feature-guide` | 重播功能引导 |
| `isutra://privacy` | 应用内隐私 |
| `isutra://feedback` | 反馈邮件 |
| `isutra://in-app-review` | 应用内 / 商店评价入口 |

## 示例

```
isutra://daily
isutra://passage?id=1
isutra://large?id=diamond
isutra://count
isutra://copy?id=1
isutra://practice
isutra://collection?id=prajna
isutra://theme?id=xingyuan
isutra://study
isutra://hunt
```

可在「快捷指令」、主屏快捷、小组件或 Safari 中使用。亦可参考应用内 **设置 → 快捷指南**。

</section>

<section lang="zh-TW" markdown="1">

愛佛經支援 **`isutra://`** 快捷連結（URL Scheme）。冷啟動與主畫面捷徑經統一緩衝投遞，避免引導後重複開啟。

## 連結格式

```
isutra://{host}?{params}
```

## 經目與譯者

| URL | 開啟 |
|-----|------|
| `isutra://passage?id={id}` | 經文詳情 |
| `isutra://couplet?id={id}` / `isutra://poem?id={id}` | 同上（相容別名） |
| `isutra://author?id={id}` | 譯者詳情 |
| `isutra://recite` / `isutra://recite?id={id}` | 誦經 |
| `isutra://large?id=diamond` / `isutra://large?id=dizang` | 大部頭分卷目錄 |

## 發現與修習

| URL | 開啟 |
|-----|------|
| `isutra://home` | 首頁 |
| `isutra://daily` | 今日一經 |
| `isutra://random` | 隨機經文 |
| `isutra://favorites` | 收藏 |
| `isutra://famous` | 法語 |
| `isutra://search` / `isutra://search?q={query}` | 搜尋 |
| `isutra://study` | 持誦學堂 |
| `isutra://hunt` | 尋經（別名 `keyword-hunt` / `flyflower`） |
| `isutra://count` | 木魚念誦（`chant` / `muyu` / `counter`） |
| `isutra://copy` / `isutra://copy?id={id}` | 抄經（iOS） |
| `isutra://practice` | 早晚功課 |
| `isutra://mastered` | 已掌握 |
| `isutra://categories` / `isutra://categories?section=` | 分類瀏覽 |
| `isutra://collection?id=` | 合集（如 `prajna`、`forty-two`；亦支援 `name=`） |
| `isutra://theme?id=` | 主題（如 `xingyuan`、`yaoshi`、`platform`） |
| `isutra://last-read` | 最近閱讀 |
| `isutra://reading-history` | 瀏覽記錄 |
| `isutra://notes` | 筆記 |

## 設定與指南

| URL | 開啟 |
|-----|------|
| `isutra://settings` | 設定 |
| `isutra://usage-guide` | 使用說明 |
| `isutra://widget-guide` | 小工具指南 |
| `isutra://shortcuts-guide` | 捷徑指南 |
| `isutra://feature-guide` | 重播功能引導 |
| `isutra://privacy` | 應用內隱私 |
| `isutra://feedback` | 回饋郵件 |
| `isutra://in-app-review` | 應用內 / 商店評價入口 |

## 範例

```
isutra://daily
isutra://passage?id=1
isutra://large?id=diamond
isutra://count
isutra://copy?id=1
isutra://practice
isutra://collection?id=prajna
isutra://theme?id=xingyuan
isutra://study
isutra://hunt
```

可在「捷徑」、主畫面捷徑、小工具或 Safari 中使用。亦可參考應用內 **設定 → 捷徑指南**。

</section>
