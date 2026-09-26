---
layout: doc
title: iPrimer — Shortcut Links
app_id: iPrimer
doc_title_en: Shortcut Links
doc_title_zh_cn: 快捷链接说明
doc_title_zh_tw: 快捷連結說明
description: iprimer:// deep links for iPrimer — chapter, daily, recite, study, meditation, guidance, hunt, collections, themes, settings guides, and more.
---

<section lang="en" markdown="1">

iPrimer supports **`iprimer://`** shortcut links (URL scheme). Cold start and Home Screen shortcuts are delivered through a unified buffer so links are not opened twice after onboarding.

## Link format

```
iprimer://{host}?{params}
```

## Chapters & authors

| URL | Opens |
|-----|-------|
| `iprimer://chapter?id={id}` | Chapter detail |
| `iprimer://passage?id={id}` / `iprimer://poem?id={id}` | Same as chapter (compatibility) |
| `iprimer://author?id={id}` | Author detail |
| `iprimer://recite` / `iprimer://recite?id={id}` | Recite flow |

## Discovery

| URL | Opens |
|-----|-------|
| `iprimer://home` | Home |
| `iprimer://daily` | Today’s Daily Study |
| `iprimer://random` | Random chapter |
| `iprimer://favorites` | Favorites |
| `iprimer://famous` | Famous lines |
| `iprimer://search` / `iprimer://search?q={query}` | Search |
| `iprimer://study` | Character Study |
| `iprimer://meditation` | Meditation course list |
| `iprimer://meditation?slug={slug}&autostart=1` | Open session and auto-start (foreground) |
| `iprimer://guidance` | Life Guidance (journal & habits) |
| `iprimer://hunt` | Hunt (寻句); aliases `keyword-hunt` / `flyflower` |
| `iprimer://mastered` | Mastered chapters |
| `iprimer://categories` / `iprimer://categories?section=` | Browse |
| `iprimer://collection?id=xiaoxue` | Xiaoxue collection (`name=` also supported) |
| `iprimer://theme?id=lijiao` | Volume / theme (`name=立教` or `Relationships` also supported) |
| `iprimer://last-read` | Last read |
| `iprimer://reading-history` | Reading history |
| `iprimer://notes` | Notes |

## Settings & guides

| URL | Opens |
|-----|-------|
| `iprimer://settings` | Settings |
| `iprimer://usage-guide` | Usage guide |
| `iprimer://widget-guide` | Widget guide |
| `iprimer://shortcuts-guide` | Shortcuts guide |
| `iprimer://feature-guide` | Replay onboarding |
| `iprimer://feedback` | Feedback email |
| `iprimer://in-app-review` | In-app / Store review entry |

## Examples

```
iprimer://daily
iprimer://chapter?id=3
iprimer://collection?id=xiaoxue
iprimer://theme?id=lijiao
iprimer://study
iprimer://meditation?slug=emotion_calm&autostart=1
iprimer://guidance
iprimer://hunt
```

Use these in the Shortcuts app, Home Screen quick actions, widgets, or Safari. Prefer stable `id` parameters when available. See also in-app **Settings → Shortcuts Guide**.

</section>

<section lang="zh-CN" markdown="1">

爱小学支持 **`iprimer://`** 快捷链接（URL Scheme）。冷启动与主屏快捷经统一缓冲投递，避免引导后重复打开。

## 链接格式

```
iprimer://{host}?{params}
```

## 篇章与作者

| URL | 打开 |
|-----|------|
| `iprimer://chapter?id={id}` | 篇章详情 |
| `iprimer://passage?id={id}` / `iprimer://poem?id={id}` | 同篇章（兼容） |
| `iprimer://author?id={id}` | 作者详情 |
| `iprimer://recite` / `iprimer://recite?id={id}` | 诵读 |

## 发现与练习

| URL | 打开 |
|-----|------|
| `iprimer://home` | 首页 |
| `iprimer://daily` | 今日每日一学 |
| `iprimer://random` | 随机篇章 |
| `iprimer://favorites` | 收藏 |
| `iprimer://famous` | 名句 |
| `iprimer://search` / `iprimer://search?q={关键词}` | 搜索 |
| `iprimer://study` | 品格学堂 |
| `iprimer://meditation` | 静心冥想课表 |
| `iprimer://meditation?slug={slug}&autostart=1` | 直达课程并自动开始（需前景） |
| `iprimer://guidance` | 人生指导（反思日记与洒扫打卡） |
| `iprimer://hunt` | 寻句 |
| `iprimer://mastered` | 已掌握 |
| `iprimer://categories` | 分类浏览 |
| `iprimer://collection?id=xiaoxue` | 《小学》合集 |
| `iprimer://theme?id=lijiao` | 六卷 / 主题（`name=立教` 等仍兼容） |
| `iprimer://last-read` | 上次阅读 |
| `iprimer://reading-history` | 阅读历史 |
| `iprimer://notes` | 笔记 |

## 设置与引导

| URL | 打开 |
|-----|------|
| `iprimer://settings` | 设置 |
| `iprimer://usage-guide` | 使用说明 |
| `iprimer://widget-guide` | 小组件指南 |
| `iprimer://shortcuts-guide` | 快捷指南 |
| `iprimer://feature-guide` | 重播欢迎引导 |
| `iprimer://feedback` | 反馈邮件 |
| `iprimer://in-app-review` | 应用内评价入口 |

## 示例

```
iprimer://daily
iprimer://chapter?id=3
iprimer://theme?id=lijiao
iprimer://study
iprimer://meditation?slug=emotion_calm&autostart=1
iprimer://guidance
```

可在快捷指令、主屏快捷、小组件或 Safari 中使用。建议优先使用稳定的 `id` 参数。详见应用内 **设置 → 快捷指南**。

</section>

<section lang="zh-TW" markdown="1">

愛小學支援 **`iprimer://`** 快捷連結（URL Scheme）。冷啟動與主畫面捷徑經統一緩衝投遞，避免引導後重複開啟。

## 連結格式

```
iprimer://{host}?{params}
```

## 篇章與作者

| URL | 開啟 |
|-----|------|
| `iprimer://chapter?id={id}` | 篇章詳情 |
| `iprimer://author?id={id}` | 作者詳情 |
| `iprimer://recite` / `iprimer://recite?id={id}` | 誦讀 |

## 發現與練習

| URL | 開啟 |
|-----|------|
| `iprimer://daily` | 今日每日一學 |
| `iprimer://study` | 品格學堂 |
| `iprimer://meditation` | 靜心冥想 |
| `iprimer://guidance` | 人生指導 |
| `iprimer://hunt` | 尋句 |
| `iprimer://collection?id=xiaoxue` | 《小學》合集 |
| `iprimer://theme?id=lijiao` | 六卷 / 主題 |

## 設定與引導

`iprimer://settings` · `iprimer://usage-guide` · `iprimer://widget-guide` · `iprimer://shortcuts-guide` · `iprimer://feature-guide` · `iprimer://feedback`

詳見應用內 **設定 → 捷徑指南**。

</section>
