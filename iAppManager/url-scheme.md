---
layout: doc
title: iAppManager — Shortcut Links
app_id: iAppManager
doc_title_en: Shortcut Links
doc_title_zh_cn: 快捷链接说明
doc_title_zh_tw: 快捷連結說明
description: iappmanager:// shortcut links for iAppManager — apps, modules, guides, certificates, reports, settings.
---

<section lang="en" markdown="1">

iAppManager supports **`iappmanager://`** links for Shortcuts, widgets, App Intents, and Home Screen actions.

## Link format

```
iappmanager://{host}[/…]
```

## Apps & modules

| URL | Opens |
|-----|-------|
| `iappmanager://apps` | My Apps |
| `iappmanager://apps/{appleId}` | Specific app (Overview) |
| `iappmanager://apps/{appleId}/{tab}` | App detail module |

`{appleId}` is the numeric App Store Connect / App Store app id. `{tab}` examples:

| Tab | Module |
|-----|--------|
| `overview` | Overview |
| `versions` | Versions |
| `builds` | Builds |
| `backgroundAssets` | Background Assets |
| `encryption` | Encryption |
| `submissions` | Review Submissions |
| `reviewDetail` | Review Detail |
| `metadata` | Metadata |
| `media` | Screenshots & Previews |
| `productPages` | Custom Product Pages |
| `appEvents` | In-App Events |
| `appClips` | App Clips |
| `experiments` | Store Experiments |
| `nominations` | Featuring Nominations |
| `availability` | Availability |
| `pricing` | Pricing |
| `ageRating` | Age Rating |
| `accessibility` | Accessibility |
| `appTags` | App Tags |
| `iap` | In-App Purchases |
| `gameCenter` | Game Center |
| `testflight` | TestFlight |
| `reviews` | Customer Reviews |
| `privacy` | Privacy (nutrition note) |
| `promoCodes` | Promo Codes |
| `webhooks` | Webhooks |

Example: `iappmanager://apps/1234567890/versions`

## Sidebar & tools

| URL | Opens |
|-----|-------|
| `iappmanager://certificates` | Certificates & Identifiers |
| `iappmanager://users` | Users & Access |
| `iappmanager://reports` | Reports |
| `iappmanager://settings` | Settings |
| `iappmanager://add-account` | Add API Key account |
| `iappmanager://about` | About |
| `iappmanager://feedback` | Feedback email |
| `iappmanager://in-app-review` | Rate prompt |

## In-app guides

| URL | Guide |
|-----|-------|
| `iappmanager://feature-guide` | Feature tour |
| `iappmanager://usage-guide` | Usage guide |
| `iappmanager://widget-guide` | Widget guide |
| `iappmanager://shortcuts-guide` | Shortcuts guide |
| `iappmanager://release-guide` | Release readiness |
| `iappmanager://iap-guide` | IAP & subscriptions |
| `iappmanager://testflight-guide` | TestFlight |
| `iappmanager://reports-guide` | Reports |

Cold and warm launches buffer deep links briefly so onboarding can finish first. App Intents can also open a managed app with an optional module.

</section>

<section lang="zh-CN" markdown="1">

爱应用者支持 **`iappmanager://`** 链接，可用于快捷指令、小组件、App Intents 与主屏操作。

## 链接格式

```
iappmanager://{host}[/…]
```

## App 与模块

| 链接 | 打开 |
|------|------|
| `iappmanager://apps` | 我的 App |
| `iappmanager://apps/{appleId}` | 指定 App（Overview） |
| `iappmanager://apps/{appleId}/{tab}` | App 详情模块 |

`{appleId}` 为数字 App ID。`{tab}` 示例：

| Tab | 模块 |
|-----|------|
| `overview` | Overview |
| `versions` | 版本 |
| `builds` | 构建 |
| `backgroundAssets` | 后台资源 |
| `encryption` | 加密声明 |
| `submissions` | 审核提交 |
| `reviewDetail` | 审核备注 |
| `metadata` | 元数据 |
| `media` | 截图与预览 |
| `productPages` | 自定义产品页 |
| `appEvents` | App 内活动 |
| `appClips` | App Clips |
| `experiments` | 商店实验 |
| `nominations` | 推荐提名 |
| `availability` | 上架地区 |
| `pricing` | 定价 |
| `ageRating` | 年龄分级 |
| `accessibility` | 辅助功能 |
| `appTags` | App Tags |
| `iap` | 内购 / 订阅 |
| `gameCenter` | Game Center |
| `testflight` | TestFlight |
| `reviews` | 顾客评价 |
| `privacy` | 隐私说明 |
| `promoCodes` | 推广码 |
| `webhooks` | Webhooks |

示例：`iappmanager://apps/1234567890/versions`

## 侧边栏与工具

| 链接 | 打开 |
|------|------|
| `iappmanager://certificates` | 证书与 Identifiers |
| `iappmanager://users` | 用户与访问 |
| `iappmanager://reports` | 报表 |
| `iappmanager://settings` | 设置 |
| `iappmanager://add-account` | 添加 API Key 账号 |
| `iappmanager://about` | 关于 |
| `iappmanager://feedback` | 反馈邮件 |
| `iappmanager://in-app-review` | 评分引导 |

## 应用内指南

| 链接 | 指南 |
|------|------|
| `iappmanager://feature-guide` | 功能导览 |
| `iappmanager://usage-guide` | 使用指南 |
| `iappmanager://widget-guide` | 小组件指南 |
| `iappmanager://shortcuts-guide` | 快捷指南 |
| `iappmanager://release-guide` | 提审就绪 |
| `iappmanager://iap-guide` | 内购与订阅 |
| `iappmanager://testflight-guide` | TestFlight |
| `iappmanager://reports-guide` | 报表 |

冷热启动会短暂缓冲深链，以便首启引导先完成。App Intents 也可打开指定 App 与可选模块。

</section>

<section lang="zh-TW" markdown="1">

愛應用者支援 **`iappmanager://`** 連結，可用於捷徑、小工具、App Intents 與主畫面操作。

## 連結格式

```
iappmanager://{host}[/…]
```

## App 與模組

| 連結 | 打開 |
|------|------|
| `iappmanager://apps` | 我的 App |
| `iappmanager://apps/{appleId}` | 指定 App（Overview） |
| `iappmanager://apps/{appleId}/{tab}` | App 詳情模組 |

`{appleId}` 為數字 App ID。`{tab}` 範例：

| Tab | 模組 |
|-----|------|
| `overview` | Overview |
| `versions` | 版本 |
| `builds` | 建置 |
| `backgroundAssets` | 背景資源 |
| `encryption` | 加密聲明 |
| `submissions` | 審核提交 |
| `reviewDetail` | 審核備註 |
| `metadata` | 中繼資料 |
| `media` | 截圖與預覽 |
| `productPages` | 自訂產品頁 |
| `appEvents` | App 內活動 |
| `appClips` | App Clips |
| `experiments` | 商店實驗 |
| `nominations` | 推薦提名 |
| `availability` | 上架地區 |
| `pricing` | 定價 |
| `ageRating` | 年齡分級 |
| `accessibility` | 輔助功能 |
| `appTags` | App Tags |
| `iap` | 內購 / 訂閱 |
| `gameCenter` | Game Center |
| `testflight` | TestFlight |
| `reviews` | 顧客評價 |
| `privacy` | 隱私說明 |
| `promoCodes` | 推廣碼 |
| `webhooks` | Webhooks |

範例：`iappmanager://apps/1234567890/versions`

## 側邊欄與工具

| 連結 | 打開 |
|------|------|
| `iappmanager://certificates` | 憑證與 Identifiers |
| `iappmanager://users` | 使用者與存取 |
| `iappmanager://reports` | 報表 |
| `iappmanager://settings` | 設定 |
| `iappmanager://add-account` | 新增 API Key 帳號 |
| `iappmanager://about` | 關於 |
| `iappmanager://feedback` | 回饋郵件 |
| `iappmanager://in-app-review` | 評分引導 |

## 應用內指南

| 連結 | 指南 |
|------|------|
| `iappmanager://feature-guide` | 功能導覽 |
| `iappmanager://usage-guide` | 使用指南 |
| `iappmanager://widget-guide` | 小工具指南 |
| `iappmanager://shortcuts-guide` | 快捷指南 |
| `iappmanager://release-guide` | 送審就緒 |
| `iappmanager://iap-guide` | 內購與訂閱 |
| `iappmanager://testflight-guide` | TestFlight |
| `iappmanager://reports-guide` | 報表 |

冷熱啟動會短暫緩衝深鏈，以便首啟引導先完成。App Intents 也可打開指定 App 與可選模組。

</section>
