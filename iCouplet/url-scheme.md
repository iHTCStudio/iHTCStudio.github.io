---
layout: doc
title: iCouplet — Shortcut Links
app_id: iCouplet
doc_title_en: Shortcut Links
doc_title_zh_cn: 快捷链接说明
doc_title_zh_tw: 快捷連結說明
description: icouplet:// deep links for iCouplet — couplet, daily, recite, study, famous, settings guides, and more.
---

<section lang="en" markdown="1">

iCouplet supports **`icouplet://`** shortcut links (URL scheme). Cold start and Home Screen shortcuts are delivered through a unified buffer so links are not opened twice after onboarding.

## Link format

```
icouplet://{host}?{params}
```

## Couplets & authors

| URL | Opens |
|-----|-------|
| `icouplet://couplet?id={id}` | Couplet detail |
| `icouplet://poem?id={id}` | Same as couplet (compatibility alias) |
| `icouplet://author?id={id}` | Author (联家) detail |
| `icouplet://recite` | Recite flow (auto-speak when possible) |
| `icouplet://recite?id={id}` | Open couplet and auto-recite |

## Discovery

| URL | Opens |
|-----|-------|
| `icouplet://home` | Home tab |
| `icouplet://daily` | Today’s Daily Couplet |
| `icouplet://random` | Random couplet |
| `icouplet://favorites` | Favorites |
| `icouplet://famous` | Famous lines list |
| `icouplet://search` | Search |
| `icouplet://search?q={query}` | Search with query |
| `icouplet://study` | Study / 对对子 entry |
| `icouplet://categories` | Browse categories |
| `icouplet://categories?section=form` | Form (体裁) section |
| `icouplet://categories?section=theme` | Theme section |
| `icouplet://categories?section=author` | Author section |
| `icouplet://categories?section=famous` | Famous lines section |
| `icouplet://categories?section=corpus` | Collections / corpus |
| `icouplet://last-read` | Last read couplet |
| `icouplet://reading-history` | Reading history |

## Settings & guides

| URL | Opens |
|-----|-------|
| `icouplet://settings` | Settings root |
| `icouplet://usage-guide` | Usage guide |
| `icouplet://widget-guide` | Widget guide |
| `icouplet://shortcuts-guide` | Shortcuts guide |
| `icouplet://feature-guide` | Replay feature onboarding |
| `icouplet://feedback` | Feedback email |
| `icouplet://in-app-review` | In-app / Store review entry |

## Examples

```
icouplet://daily
icouplet://couplet?id=1
icouplet://recite?id=1
icouplet://search?q=春
icouplet://categories?section=famous
icouplet://widget-guide
```

Use these in the Shortcuts app, Home Screen quick actions, widgets, or Safari. See also in-app **Settings → Shortcuts Guide**.

</section>

<section lang="zh-CN" markdown="1">

爱对联支持 **`icouplet://`** 快捷链接。冷启动与主屏快捷经统一缓冲投递，避免引导结束后重复打开。

## 链接格式

```
icouplet://{host}?{params}
```

## 对联与联家

| 链接 | 打开 |
|------|------|
| `icouplet://couplet?id={id}` | 联详情 |
| `icouplet://poem?id={id}` | 同 couplet（兼容别名） |
| `icouplet://author?id={id}` | 联家详情 |
| `icouplet://recite` | 诵联流程（可自动开读） |
| `icouplet://recite?id={id}` | 打开指定联并自动诵联 |

## 发现

| 链接 | 打开 |
|------|------|
| `icouplet://home` | 首页 |
| `icouplet://daily` | 每日一联 |
| `icouplet://random` | 随机一联 |
| `icouplet://favorites` | 收藏 |
| `icouplet://famous` | 名句列表 |
| `icouplet://search` | 搜索 |
| `icouplet://search?q={query}` | 带关键词搜索 |
| `icouplet://study` | 对课 / 对对子入口 |
| `icouplet://categories` | 分类浏览 |
| `icouplet://categories?section=form` | 体裁 |
| `icouplet://categories?section=theme` | 主题 |
| `icouplet://categories?section=author` | 联家 |
| `icouplet://categories?section=famous` | 名句 |
| `icouplet://categories?section=corpus` | 合集 |
| `icouplet://last-read` | 最近阅读 |
| `icouplet://reading-history` | 浏览记录 |

## 设置与教程

| 链接 | 打开 |
|------|------|
| `icouplet://settings` | 设置根页 |
| `icouplet://usage-guide` | 使用说明 |
| `icouplet://widget-guide` | 小组件指南 |
| `icouplet://shortcuts-guide` | 快捷指南 |
| `icouplet://feature-guide` | 重播功能引导 |
| `icouplet://feedback` | 反馈邮件 |
| `icouplet://in-app-review` | 应用内评价入口 |

## 示例

```
icouplet://daily
icouplet://couplet?id=1
icouplet://recite?id=1
icouplet://search?q=春
icouplet://categories?section=famous
icouplet://widget-guide
```

可用于「快捷指令」、主屏长按、小组件或 Safari。详见 App 内 **设置 → 快捷指南**。

</section>

<section lang="zh-TW" markdown="1">

愛對聯支援 **`icouplet://`** 快捷連結。冷啟動與主畫面捷徑經統一緩衝投遞，避免引導結束後重複開啟。

## 連結格式

```
icouplet://{host}?{params}
```

## 對聯與聯家

| 連結 | 開啟 |
|------|------|
| `icouplet://couplet?id={id}` | 聯詳情 |
| `icouplet://poem?id={id}` | 同 couplet（相容別名） |
| `icouplet://author?id={id}` | 聯家詳情 |
| `icouplet://recite` | 誦聯流程（可自動開讀） |
| `icouplet://recite?id={id}` | 開啟指定聯並自動誦聯 |

## 發現

| 連結 | 開啟 |
|------|------|
| `icouplet://home` | 首頁 |
| `icouplet://daily` | 每日一聯 |
| `icouplet://random` | 隨機一聯 |
| `icouplet://favorites` | 收藏 |
| `icouplet://famous` | 名句列表 |
| `icouplet://search` | 搜尋 |
| `icouplet://search?q={query}` | 帶關鍵詞搜尋 |
| `icouplet://study` | 對課 / 對對子入口 |
| `icouplet://categories` | 分類瀏覽 |
| `icouplet://categories?section=form` | 體裁 |
| `icouplet://categories?section=theme` | 主題 |
| `icouplet://categories?section=author` | 聯家 |
| `icouplet://categories?section=famous` | 名句 |
| `icouplet://categories?section=corpus` | 合集 |
| `icouplet://last-read` | 最近閱讀 |
| `icouplet://reading-history` | 瀏覽紀錄 |

## 設定與教學

| 連結 | 開啟 |
|------|------|
| `icouplet://settings` | 設定根頁 |
| `icouplet://usage-guide` | 使用說明 |
| `icouplet://widget-guide` | 小工具指南 |
| `icouplet://shortcuts-guide` | 捷徑指南 |
| `icouplet://feature-guide` | 重播功能引導 |
| `icouplet://feedback` | 回饋郵件 |
| `icouplet://in-app-review` | 應用內評價入口 |

## 範例

```
icouplet://daily
icouplet://couplet?id=1
icouplet://recite?id=1
icouplet://search?q=春
icouplet://categories?section=famous
icouplet://widget-guide
```

可用於「捷徑」、主畫面長按、小工具或 Safari。詳見 App 內 **設定 → 捷徑指南**。

</section>
