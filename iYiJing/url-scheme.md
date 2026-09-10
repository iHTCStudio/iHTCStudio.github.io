---
layout: doc
title: iYijing — Shortcut Links
app_id: iYiJing
doc_title_en: Shortcut Links
doc_title_zh_cn: 快捷链接说明
doc_title_zh_tw: 快捷連結說明
description: iyijing:// deep links for iYijing — hexagram, daily, cast, study, hunt, Ten Wings, settings guides, and more.
---

<section lang="en" markdown="1">

iYijing supports **`iyijing://`** shortcut links (URL scheme). Cold start and Home Screen shortcuts are delivered through a unified buffer so links are not opened twice after onboarding.

## Link format

```
iyijing://{host}/{path}?{params}
```

## Hexagrams & discovery

| URL | Opens |
|-----|-------|
| `iyijing://home` | Home |
| `iyijing://daily` | Today’s Daily Hexagram |
| `iyijing://random` | Random hexagram |
| `iyijing://hexagram/{id}` | Hexagram detail (`gua/{id}` alias) |
| `iyijing://wing/{id}` | Ten Wings text (`yizhuan/{id}` alias) |
| `iyijing://trigram/{id}` | Trigram (`bagua/{id}` alias) |
| `iyijing://browse` | Browse |
| `iyijing://favorites` | Favorites |
| `iyijing://famous` | Famous lines |
| `iyijing://search` / `?q=` | Search |
| `iyijing://study` | Yijing Study |
| `iyijing://hunt` | Keyword hunt |
| `iyijing://divination` | Cultural casting (`qigua` / `cast`) |
| `iyijing://recite` / `recite/{id}` | Recitation |
| `iyijing://collection` | Hexagram list (`playlist` alias) |
| `iyijing://last-read` | Last read |
| `iyijing://reading-history` | Reading history |
| `iyijing://notes` | Notes |
| `iyijing://mastered` | Mastered |
| `iyijing://wrong-book` | Study wrong-book |
| `iyijing://recite-wrong` | Recite wrong-book |

## Settings & guides

| URL | Opens |
|-----|-------|
| `iyijing://settings` | Settings |
| `iyijing://usage-guide` | Usage guide |
| `iyijing://widget-guide` | Widget guide |
| `iyijing://shortcuts-guide` | Shortcuts guide |
| `iyijing://feature-guide` | Replay onboarding |
| `iyijing://feedback` | Feedback email |

## Examples

```
iyijing://daily
iyijing://hexagram/1
iyijing://wing/301
iyijing://divination
iyijing://study
iyijing://hunt
iyijing://famous
iyijing://search?q=乾
```

Use these in the Shortcuts app, Home Screen quick actions, widgets, Control Center, or Safari. See also in-app **Settings → Shortcuts Guide**.

</section>

<section lang="zh-CN" markdown="1">

爱周易支持 **`iyijing://`** 快捷链接（URL Scheme）。冷启动与主屏快捷经统一缓冲投递，避免引导后重复打开。

## 链接格式

```
iyijing://{host}/{path}?{params}
```

## 卦象与发现

| URL | 打开 |
|-----|------|
| `iyijing://home` | 首页 |
| `iyijing://daily` | 每日一卦 |
| `iyijing://random` | 随机 |
| `iyijing://hexagram/{id}` | 卦象详情（别名 `gua/{id}`） |
| `iyijing://wing/{id}` | 十翼（别名 `yizhuan/{id}`） |
| `iyijing://trigram/{id}` | 八卦（别名 `bagua/{id}`） |
| `iyijing://browse` | 分类 |
| `iyijing://favorites` | 收藏 |
| `iyijing://famous` | 名句 |
| `iyijing://search` / `?q=` | 搜索 |
| `iyijing://study` | 易学学堂 |
| `iyijing://hunt` | 识辞 |
| `iyijing://divination` | 文化起卦（`qigua` / `cast`） |
| `iyijing://recite` / `recite/{id}` | 诵读 |
| `iyijing://collection` | 卦单（别名 `playlist`） |
| `iyijing://last-read` | 上次阅读 |
| `iyijing://reading-history` | 浏览记录 |
| `iyijing://notes` | 笔记 |
| `iyijing://mastered` | 已精通 |
| `iyijing://wrong-book` | 错题本 |
| `iyijing://recite-wrong` | 诵读错题本 |

## 设置与教程

| URL | 打开 |
|-----|------|
| `iyijing://settings` | 设置 |
| `iyijing://usage-guide` | 使用说明 |
| `iyijing://widget-guide` | 小组件指南 |
| `iyijing://shortcuts-guide` | 快捷指南 |
| `iyijing://feature-guide` | 重播引导 |
| `iyijing://feedback` | 反馈邮件 |

## 示例

```
iyijing://daily
iyijing://hexagram/1
iyijing://wing/301
iyijing://divination
iyijing://study
iyijing://hunt
iyijing://famous
iyijing://search?q=乾
```

可在「快捷指令」、主屏快捷、小组件、控制中心或 Safari 中使用。也可查看应用内 **设置 → 快捷指南**。

</section>

<section lang="zh-TW" markdown="1">

愛周易支援 **`iyijing://`** 快捷連結（URL Scheme）。冷啟動與主畫面捷徑經統一緩衝投遞，避免引導後重複開啟。

## 連結格式

```
iyijing://{host}/{path}?{params}
```

## 卦象與發現

| URL | 開啟 |
|-----|------|
| `iyijing://home` | 首頁 |
| `iyijing://daily` | 每日一卦 |
| `iyijing://random` | 隨機 |
| `iyijing://hexagram/{id}` | 卦象詳情（別名 `gua/{id}`） |
| `iyijing://wing/{id}` | 十翼（別名 `yizhuan/{id}`） |
| `iyijing://trigram/{id}` | 八卦（別名 `bagua/{id}`） |
| `iyijing://browse` | 分類 |
| `iyijing://favorites` | 收藏 |
| `iyijing://famous` | 名句 |
| `iyijing://search` / `?q=` | 搜尋 |
| `iyijing://study` | 易學學堂 |
| `iyijing://hunt` | 識辭 |
| `iyijing://divination` | 文化起卦（`qigua` / `cast`） |
| `iyijing://recite` / `recite/{id}` | 誦讀 |
| `iyijing://collection` | 卦單（別名 `playlist`） |
| `iyijing://last-read` | 上次閱讀 |
| `iyijing://reading-history` | 瀏覽記錄 |
| `iyijing://notes` | 筆記 |
| `iyijing://mastered` | 已精通 |
| `iyijing://wrong-book` | 錯題本 |
| `iyijing://recite-wrong` | 誦讀錯題本 |

## 設定與教學

| URL | 開啟 |
|-----|------|
| `iyijing://settings` | 設定 |
| `iyijing://usage-guide` | 使用說明 |
| `iyijing://widget-guide` | 小工具指南 |
| `iyijing://shortcuts-guide` | 捷徑指南 |
| `iyijing://feature-guide` | 重播引導 |
| `iyijing://feedback` | 回饋郵件 |

## 範例

```
iyijing://daily
iyijing://hexagram/1
iyijing://wing/301
iyijing://divination
iyijing://study
iyijing://hunt
iyijing://famous
iyijing://search?q=乾
```

可在「捷徑」、主畫面捷徑、小工具、控制中心或 Safari 中使用。也可查看應用內 **設定 → 捷徑指南**。

</section>
