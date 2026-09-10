---
layout: doc
title: iThousand — Shortcut Links
app_id: iThousand
doc_title_en: Shortcut Links
doc_title_zh_cn: 快捷链接说明
doc_title_zh_tw: 快捷連結說明
description: ithousand:// deep links for iThousand — passage, daily, recite, study, hunt, character cards, collections, themes, settings guides, and more.
---

<section lang="en" markdown="1">

iThousand supports **`ithousand://`** shortcut links (URL scheme). Cold start and Home Screen shortcuts are delivered through a unified buffer so links are not opened twice after onboarding.

## Link format

```
ithousand://{host}?{params}
```

## Passages, authors & characters

| URL | Opens |
|-----|-------|
| `ithousand://passage?id={id}` | Passage detail |
| `ithousand://passage?id={id}&open=study` | Passage → Primer Hall |
| `ithousand://passage?id={id}&open=characters` | Passage → character table |
| `ithousand://passage?id={id}&open=note` | Passage → note |
| `ithousand://author?id={id}` | Author detail |
| `ithousand://recite` / `ithousand://recite?id={id}` | Recite flow |
| `ithousand://characters` | Character library |
| `ithousand://character?char=天` | Focus a character card |
| `ithousand://characters?id={id}` | Character card by ID |
| `ithousand://saved-characters` | Saved Characters |
| `ithousand://saved-famous` | Saved famous lines |

## Discovery

| URL | Opens |
|-----|-------|
| `ithousand://home` | Home |
| `ithousand://daily` | Today’s Daily Line |
| `ithousand://random` | Random passage |
| `ithousand://favorites` | Favorites |
| `ithousand://list?id={uuid}` | A personal list (千单) |
| `ithousand://famous` | Famous lines |
| `ithousand://search` / `ithousand://search?q={query}` | Search |
| `ithousand://study` | Primer Hall |
| `ithousand://hunt` | Hunt (寻字); aliases `keyword-hunt` / `flyflower` |
| `ithousand://mastered` | Mastered |
| `ithousand://categories` / `ithousand://categories?section=` | Browse |
| `ithousand://collection?id=qianziwen` | Primer collection (`name=` also supported) |
| `ithousand://theme?id=dizigui-filial` | Theme |
| `ithousand://last-read` | Last read |
| `ithousand://reading-history` | Reading history |
| `ithousand://notes` | Notes |

## Settings & guides

| URL | Opens |
|-----|-------|
| `ithousand://settings` | Settings |
| `ithousand://privacy` | In-app privacy |
| `ithousand://usage-guide` | Usage guide |
| `ithousand://widget-guide` | Widget guide |
| `ithousand://shortcuts-guide` | Shortcuts guide |
| `ithousand://feature-guide` | Replay onboarding |
| `ithousand://feedback` | Feedback email |
| `ithousand://in-app-review` | In-app / Store review entry |

## Examples

```
ithousand://daily
ithousand://passage?id=1
ithousand://passage?id=1&open=characters
ithousand://character?char=天
ithousand://collection?id=qianziwen
ithousand://study
ithousand://hunt
ithousand://saved-characters
```

Use these in the Shortcuts app, Home Screen quick actions, widgets, or Safari. Prefer stable `id` parameters when available. See also in-app **Settings → Shortcuts Guide**.

</section>

<section lang="zh-CN" markdown="1">

爱千字文支持 **`ithousand://`** 快捷链接（URL Scheme）。冷启动与主屏快捷经统一缓冲投递，避免引导后重复打开。

## 链接格式

```
ithousand://{host}?{params}
```

## 篇目、作者与字卡

| URL | 打开 |
|-----|------|
| `ithousand://passage?id={id}` | 篇目详情 |
| `ithousand://passage?id={id}&open=study` | 篇目 → 蒙学堂 |
| `ithousand://passage?id={id}&open=characters` | 篇目 → 本篇字表 |
| `ithousand://passage?id={id}&open=note` | 篇目 → 笔记 |
| `ithousand://author?id={id}` | 作者详情 |
| `ithousand://recite` / `ithousand://recite?id={id}` | 诵读 |
| `ithousand://characters` | 字库 |
| `ithousand://character?char=天` | 指定字卡 |
| `ithousand://saved-characters` | 生字本 |
| `ithousand://saved-famous` | 已收藏名句 |

## 发现与练习

| URL | 打开 |
|-----|------|
| `ithousand://home` | 首页 |
| `ithousand://daily` | 今日每日一句 |
| `ithousand://random` | 随机篇目 |
| `ithousand://favorites` | 收藏 |
| `ithousand://list?id={uuid}` | 指定千单 |
| `ithousand://famous` | 名句 |
| `ithousand://search` / `ithousand://search?q={关键词}` | 搜索 |
| `ithousand://study` | 蒙学堂 |
| `ithousand://hunt` | 寻字 |
| `ithousand://mastered` | 已掌握 |
| `ithousand://categories` | 分类浏览 |
| `ithousand://collection?id=qianziwen` | 千字文等合集 |
| `ithousand://theme?id=dizigui-filial` | 主题 |
| `ithousand://last-read` | 上次阅读 |
| `ithousand://reading-history` | 阅读历史 |
| `ithousand://notes` | 笔记 |

## 设置与引导

| URL | 打开 |
|-----|------|
| `ithousand://settings` | 设置 |
| `ithousand://privacy` | 应用内隐私政策 |
| `ithousand://usage-guide` | 使用说明 |
| `ithousand://widget-guide` | 小组件指南 |
| `ithousand://shortcuts-guide` | 快捷指南 |
| `ithousand://feature-guide` | 重播欢迎引导 |
| `ithousand://feedback` | 反馈邮件 |
| `ithousand://in-app-review` | 应用内评价入口 |

## 示例

```
ithousand://daily
ithousand://passage?id=1
ithousand://character?char=天
ithousand://study
ithousand://hunt
ithousand://saved-characters
```

可在快捷指令、主屏快捷、小组件或 Safari 中使用。建议优先使用稳定的 `id` 参数。详见应用内 **设置 → 快捷指南**。

</section>

<section lang="zh-TW" markdown="1">

愛千字文支援 **`ithousand://`** 快捷連結（URL Scheme）。冷啟動與主畫面捷徑經統一緩衝投遞，避免引導後重複開啟。

## 連結格式

```
ithousand://{host}?{params}
```

## 篇目、作者與字卡

| URL | 開啟 |
|-----|------|
| `ithousand://passage?id={id}` | 篇目詳情 |
| `ithousand://recite` / `ithousand://recite?id={id}` | 誦讀 |
| `ithousand://characters` | 字庫 |
| `ithousand://character?char=天` | 指定字卡 |
| `ithousand://saved-characters` | 生字本 |

## 發現與練習

| URL | 開啟 |
|-----|------|
| `ithousand://daily` | 今日每日一句 |
| `ithousand://study` | 蒙學堂 |
| `ithousand://hunt` | 尋字 |
| `ithousand://collection?id=qianziwen` | 千字文等合集 |
| `ithousand://theme?id=dizigui-filial` | 主題 |

## 設定與引導

`ithousand://settings` · `ithousand://privacy` · `ithousand://usage-guide` · `ithousand://widget-guide` · `ithousand://shortcuts-guide` · `ithousand://feature-guide` · `ithousand://feedback`

詳見應用內 **設定 → 捷徑指南**。

</section>
