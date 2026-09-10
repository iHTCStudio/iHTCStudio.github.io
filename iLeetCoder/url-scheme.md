---
layout: doc
title: iCoder — URL Scheme Reference
app_id: iLeetCoder
doc_title_en: URL Scheme Reference
doc_title_zh_cn: URL Scheme 深度链接文档
doc_title_zh_tw: URL Scheme 深度連結文件
description: Complete reference of iLeetCoder:// deep links, widget links and Home Screen Quick Actions supported by iCoder.
---

<section lang="en" markdown="1">

iCoder supports **`iLeetCoder://`** (case-insensitive) deep links — open a problem, daily quiz, favourites, wrong book, or filter by tag / company from Safari, Shortcuts, widgets, or another app.

## Protocol

| Host | Opens | Query |
|------|-------|-------|
| `problem` | Problem detail | `leetId=` or `id=` (e.g. `1`, `206`) |
| `quiz` | Daily Quiz tab | — |
| `favorites` | Favourites list | — |
| `wrong`, `mistakes`, `wrongquestions` | Wrong book | `record=<UUID>` → linked problem |
| `tag` | Problems filtered by tag | `name=` |
| `company` | Problems filtered by company | `name=` |

## Examples

```
iLeetCoder://problem?leetId=1
iLeetCoder://problem?id=206
iLeetCoder://quiz
iLeetCoder://tag?name=Array
iLeetCoder://company?name=Google
iLeetCoder://wrong?record=550E8400-E29B-41D4-A716-446655440000
```

## Home Screen Quick Actions

Up to **4** in **Settings → Home Screen shortcuts**: `search`, `quiz`, `favorites`, `wrong`, `categories`, `feedback`, `review`. Search / categories / feedback / review are Quick Action channels.

[Back to overview](..) · [FAQ](faq) · [Privacy](privacy)

</section>

<section lang="zh-CN" markdown="1">

爱算法支持 **`iLeetCoder://`** 深度链接——打开题目详情、每日测验、收藏、错题本，或按标签 / 公司筛选。

| Host | 打开 | 参数 |
|------|------|------|
| `problem` | 题目详情 | `leetId=` 或 `id=` |
| `quiz` | 每日测验 | — |
| `favorites` | 收藏列表 | — |
| `wrong` / `mistakes` | 错题本 | `record=<UUID>` |
| `tag` | 按标签筛选 | `name=` |
| `company` | 按公司筛选 | `name=` |

```
iLeetCoder://problem?leetId=1
iLeetCoder://tag?name=Array
iLeetCoder://company?name=Google
```

[返回概览](..) · [常见问题](faq) · [隐私政策](privacy)

</section>

<section lang="zh-TW" markdown="1">

愛算法支援 **`iLeetCoder://`** 深度連結——開啟題目詳情、每日測驗、收藏、錯題本，或依標籤 / 公司篩選。

| Host | 開啟 | 參數 |
|------|------|------|
| `problem` | 題目詳情 | `leetId=` 或 `id=` |
| `quiz` | 每日測驗 | — |
| `favorites` | 收藏列表 | — |
| `wrong` / `mistakes` | 錯題本 | `record=<UUID>` |
| `tag` | 依標籤篩選 | `name=` |
| `company` | 依公司篩選 | `name=` |

[返回概覽](..) · [常見問題](faq) · [隱私政策](privacy)

</section>
