---
layout: doc
title: iXin — Shortcut Links
app_id: iXin
doc_title_en: Shortcut Links
doc_title_zh_cn: 快捷链接说明
doc_title_zh_tw: 快捷連結說明
description: ixin:// deep links for iXin — passage, daily, recite, study, hunt, collections, settings guides, and more.
---

<section lang="en" markdown="1">

iXin supports **`ixin://`** shortcut links (URL scheme). Cold start and Home Screen shortcuts are delivered through a unified buffer so links are not opened twice after onboarding.

## Link format

```
ixin://{host}?{params}
```

## Passages & authors

| URL | Opens |
|-----|-------|
| `ixin://passage?id={id}` | Passage detail |
| `ixin://saying?id={id}` / `ixin://couplet?id={id}` / `ixin://poem?id={id}` | Same as passage (compatibility) |
| `ixin://passage?id={id}&card=1` | Passage detail and card sheet |
| `ixin://card?id={id}` / `ixin://share-card?id={id}` | Insight cards |
| `ixin://author?id={id}` | Author detail |
| `ixin://recite` / `ixin://recite?id={id}` | Recite flow |

## Discovery & practice

| URL | Opens |
|-----|-------|
| `ixin://home` | Home |
| `ixin://daily` | Daily Insight |
| `ixin://random` | Random passage |
| `ixin://favorites` | Favorites |
| `ixin://famous` | Famous lines |
| `ixin://search` / `ixin://search?q={query}` | Search |
| `ixin://study` / `ixin://study?id={id}` | Heart School |
| `ixin://hunt` | Heart Hunt (`keyword-hunt` / `flyflower`) |
| `ixin://handwriting` | Handwriting search (`handwrite`; iOS) |
| `ixin://mastered` | Mastered (`progress`) |
| `ixin://categories` / `ixin://categories?section=` | Browse |
| `ixin://collection?id=` | Collection / book (`chuanxilu` / `daxuewen` / `jiaotiao` / `yilvwen` / poems) |
| `ixin://corpus` | All passages (`all`) |
| `ixin://last-read` | Last read |
| `ixin://reading-history` | Reading history |
| `ixin://notes` | Notes |
| `ixin://journal` | Knowing-Acting journal |
| `ixin://liangzhi` | Three Questions of Liangzhi |
| `ixin://graph` | Concept graph |
| `ixin://timeline` | Annals / timeline |
| `ixin://map` | Map |
| `ixin://people` | People |
| `ixin://achievements` | Achievements |
| `ixin://theme?id=` | Theme |

## Settings & guides

| URL | Opens |
|-----|-------|
| `ixin://settings` | Settings |
| `ixin://usage-guide` | Usage guide |
| `ixin://widget-guide` | Widget guide |
| `ixin://shortcuts-guide` | Shortcuts guide |
| `ixin://feature-guide` | Replay onboarding |
| `ixin://feedback` | Feedback email |
| `ixin://in-app-review` | In-app / Store review entry |

## Examples

```
ixin://daily
ixin://passage?id=1
ixin://journal
ixin://liangzhi
ixin://collection?id=chuanxilu
ixin://study
ixin://hunt
```

## Notes

- Parameters are case-sensitive where IDs are numeric.
- Siri, Shortcuts, widgets, and Control Center controls use the same deep-link routes.
- See the in-app **Settings → Help** guides for the latest list.

</section>

<section lang="zh-CN" markdown="1">

爱王阳明支持 **`ixin://`** 快捷链接（URL Scheme）。冷启动与主屏快捷经统一缓冲投递，避免引导页结束后重复打开。

## 链接格式

```
ixin://{host}?{params}
```

## 篇目与作者

| URL | 打开 |
|-----|------|
| `ixin://passage?id={id}` | 篇目详情 |
| `ixin://saying?id={id}` / `ixin://couplet?id={id}` / `ixin://poem?id={id}` | 同详情（兼容别名） |
| `ixin://passage?id={id}&card=1` | 详情并弹出心卡 |
| `ixin://card?id={id}` / `ixin://share-card?id={id}` | 心卡 |
| `ixin://author?id={id}` | 作者详情 |
| `ixin://recite` / `ixin://recite?id={id}` | 诵读 |

## 发现与学堂

| URL | 打开 |
|-----|------|
| `ixin://home` | 首页 |
| `ixin://daily` | 每日一心 |
| `ixin://random` | 随机篇目 |
| `ixin://favorites` | 收藏 |
| `ixin://famous` | 金句 |
| `ixin://search` / `ixin://search?q={query}` | 搜索 |
| `ixin://study` / `ixin://study?id={id}` | 心学堂 |
| `ixin://hunt` | 寻心（`keyword-hunt` / `flyflower`） |
| `ixin://handwriting` | 手写搜索（`handwrite`；iOS） |
| `ixin://mastered` | 已掌握（`progress`） |
| `ixin://categories` / `ixin://categories?section=` | 分类浏览 |
| `ixin://collection?id=` | 合集 / 典籍（`chuanxilu` / `daxuewen` / `jiaotiao` / `yilvwen` 等） |
| `ixin://corpus` | 全部篇目（`all`） |
| `ixin://last-read` | 最近阅读 |
| `ixin://reading-history` | 阅读历史 |
| `ixin://notes` | 笔记 |
| `ixin://journal` | 知行日记 |
| `ixin://liangzhi` | 良知三问 |
| `ixin://graph` | 概念图谱 |
| `ixin://timeline` | 年谱 |
| `ixin://map` | 地图 |
| `ixin://people` | 人物 |
| `ixin://achievements` | 成就 |
| `ixin://theme?id=` | 主题 |

## 设置与指南

| URL | 打开 |
|-----|------|
| `ixin://settings` | 设置 |
| `ixin://usage-guide` | 使用说明 |
| `ixin://widget-guide` | 小组件指南 |
| `ixin://shortcuts-guide` | 快捷指南 |
| `ixin://feature-guide` | 重播功能引导 |
| `ixin://feedback` | 反馈邮件 |
| `ixin://in-app-review` | 应用内评价入口 |

## 示例

```
ixin://daily
ixin://passage?id=1
ixin://journal
ixin://liangzhi
ixin://collection?id=chuanxilu
ixin://study
ixin://hunt
```

## 说明

- 数字 ID 参数区分大小写。
- Siri、快捷指令、小组件与控制中心使用同一套深链。
- 最新列表见应用内 **设置 → 帮助**。

</section>

<section lang="zh-TW" markdown="1">

愛王陽明支援 **`ixin://`** 快捷連結（URL Scheme）。冷啟動與主畫面捷徑經統一緩衝投遞，避免引導頁結束後重複打開。

## 連結格式

```
ixin://{host}?{params}
```

## 篇目與作者

| URL | 打開 |
|-----|------|
| `ixin://passage?id={id}` | 篇目詳情 |
| `ixin://saying?id={id}` / `ixin://couplet?id={id}` / `ixin://poem?id={id}` | 同詳情（相容別名） |
| `ixin://passage?id={id}&card=1` | 詳情並彈出心卡 |
| `ixin://card?id={id}` / `ixin://share-card?id={id}` | 心卡 |
| `ixin://author?id={id}` | 作者詳情 |
| `ixin://recite` / `ixin://recite?id={id}` | 誦讀 |

## 發現與學堂

| URL | 打開 |
|-----|------|
| `ixin://home` | 首頁 |
| `ixin://daily` | 每日一心 |
| `ixin://random` | 隨機篇目 |
| `ixin://favorites` | 收藏 |
| `ixin://famous` | 金句 |
| `ixin://search` / `ixin://search?q={query}` | 搜尋 |
| `ixin://study` / `ixin://study?id={id}` | 心學堂 |
| `ixin://hunt` | 尋心（`keyword-hunt` / `flyflower`） |
| `ixin://handwriting` | 手寫搜尋（`handwrite`；iOS） |
| `ixin://mastered` | 已掌握（`progress`） |
| `ixin://categories` / `ixin://categories?section=` | 分類瀏覽 |
| `ixin://collection?id=` | 合集 / 典籍（`chuanxilu` / `daxuewen` / `jiaotiao` / `yilvwen` 等） |
| `ixin://corpus` | 全部篇目（`all`） |
| `ixin://last-read` | 最近閱讀 |
| `ixin://reading-history` | 閱讀歷史 |
| `ixin://notes` | 筆記 |
| `ixin://journal` | 知行日記 |
| `ixin://liangzhi` | 良知三問 |
| `ixin://graph` | 概念圖譜 |
| `ixin://timeline` | 年譜 |
| `ixin://map` | 地圖 |
| `ixin://people` | 人物 |
| `ixin://achievements` | 成就 |
| `ixin://theme?id=` | 主題 |

## 設定與指南

| URL | 打開 |
|-----|------|
| `ixin://settings` | 設定 |
| `ixin://usage-guide` | 使用說明 |
| `ixin://widget-guide` | 小工具指南 |
| `ixin://shortcuts-guide` | 捷徑指南 |
| `ixin://feature-guide` | 重播功能引導 |
| `ixin://feedback` | 回饋郵件 |
| `ixin://in-app-review` | 應用內評價入口 |

## 範例

```
ixin://daily
ixin://passage?id=1
ixin://journal
ixin://liangzhi
ixin://collection?id=chuanxilu
ixin://study
ixin://hunt
```

## 說明

- 數字 ID 參數區分大小寫。
- Siri、捷徑、小工具與控制中心使用同一套深鏈。
- 最新列表見應用內 **設定 → 說明**。

</section>
