---
layout: doc
title: iConnect — URL Scheme Reference
app_id: iConnect
doc_title_en: URL Scheme Reference
doc_title_zh_cn: URL Scheme 深度链接文档
doc_title_zh_tw: URL Scheme 深度連結文件
description: Complete reference of iconnect:// deep links — open tabs, settings pages, share, feedback, and review from Safari, Shortcuts, or other apps.
---

<section lang="en" markdown="1">

iConnect supports **`iconnect://`** URL scheme deep links — open a tab, a Settings page, or an in-app sheet from Safari, another app, a bookmark, or Apple Shortcuts. These URLs mirror the destinations available as **Home Screen Quick Actions** on iPhone and iPad (long-press the app icon).

> **Note:** URL links only **navigate inside iConnect**. They do not connect to a peer, start a transfer, or open a specific chat thread.

## Protocol Specification

```
iconnect://<host>
iconnect://<host>?refresh=1
```

| Rule | Detail |
|------|--------|
| **Scheme** | `iconnect` |
| **Host / path** | Single segment, **case-insensitive** — resolved from the URL **host** or first **path** segment |
| **Aliases** | Several hosts accept synonyms (see table below) |
| **Query** | Only `refresh=1` / `refresh=true` on **Devices** triggers a discovery refresh |

Examples of equivalent forms:

```
iconnect://devices
iconnect://open/devices
```

---

## Tab destinations

| URL | Opens | Aliases |
|-----|--------|---------|
| `iconnect://devices` | **Devices** tab (radar / discovery) | `device` |
| `iconnect://devices?refresh=1` | **Devices** tab and **refreshes** nearby discovery | — |
| `iconnect://chat` | **Chats** tab | `messages` |
| `iconnect://transfers` | **Transfers** tab | `transfer` |
| `iconnect://history` | **History** tab (transfer log) | — |
| `iconnect://settings` | **Settings** tab | `setting` |

**Refresh discovery**

```
iconnect://devices?refresh=1
iconnect://devices/refresh
```

---

## Settings sub-pages

These links switch to **Settings**, then open the matching page:

| URL | Opens | Aliases |
|-----|--------|---------|
| `iconnect://about` | About | — |
| `iconnect://usage` | Usage Guide | `guide`, `help`, `usageguide` |
| `iconnect://shortcuts` | Home Screen shortcuts picker (iOS) | `homeshortcuts` |
| `iconnect://debug` | Debug / diagnostics info | `debuginfo` |

---

## In-app actions

| URL | Opens |
|-----|--------|
| `iconnect://share` | Share iConnect sheet (App Store link + recommendation text) |
| `iconnect://feedback` | Feedback email compose (falls back to `mailto:` if Mail is unavailable) |
| `iconnect://review` | In-app App Store rating prompt |

**Review aliases:** `iconnect://rate`, `iconnect://rating`

---

## Examples

**Open Chats tab**

```
iconnect://chat
```

**Open Transfers tab**

```
iconnect://transfers
```

**Refresh device discovery**

```
iconnect://devices?refresh=1
```

**Open Usage Guide**

```
iconnect://usage
```

**Share the app**

```
iconnect://share
```

---

## Home Screen Quick Actions (iOS)

Long-press the iConnect icon. Customize up to **4** shortcuts in **Settings → Home Screen shortcuts** (drag to reorder).

| Quick Action | URL |
|--------------|-----|
| Devices | `iconnect://devices` |
| Chats | `iconnect://chat` |
| Transfers | `iconnect://transfers` |
| History | `iconnect://history` |
| Share | `iconnect://share` |
| Feedback | `iconnect://feedback` |
| Rate | `iconnect://review` |
| About | `iconnect://about` |

Default enabled: **Devices**, **Chats**, **Share**, **Feedback**.

Quick-action types use the same `iconnect://` strings and are routed through the same parser as external URLs.

---

## Apple Shortcuts

**Open Transfers tab**

1. Add action **Open URL**
2. URL: `iconnect://transfers`

**Refresh nearby devices after joining Wi‑Fi**

```
iconnect://devices?refresh=1
```

Use **Open URL** in a Personal Automation (e.g. when Wi‑Fi connects) to jump to discovery and rescan.

---

## Launch behavior

When iConnect receives a URL (cold start or while running):

1. The link is parsed by `IConnectDeepLink`.
2. Tab switches animate immediately; **share**, **feedback**, and **review** open after a short delay (~0.4 s on iOS) so the UI can finish mounting.
3. **Feedback** uses in-app Mail when available; otherwise opens the default mail client via `mailto:`.
4. **Share** on Mac uses the system share picker; on iOS it presents a share sheet.

---

## Troubleshooting

| Issue | What to check |
|-------|----------------|
| Link does nothing | Ensure iConnect is installed; host must match a supported name above |
| `feedback` opens Mail only | No Mail account configured on the device — expected fallback |
| `shortcuts` has no effect on Mac | Home Screen shortcut customization is **iOS-only** |
| URL does not connect to a device | Deep links only navigate — use the Devices tab to discover peers manually |

---

[Back to iConnect Support](..) · [FAQ](../faq) · [Privacy Policy](../privacy)

</section>
<section lang="zh-CN" markdown="1">

爱联（iConnect）支持 **`iconnect://`** URL Scheme 深度链接——可从 Safari、其他 App、书签或苹果快捷指令打开指定 Tab、设置页或应用内操作。这些 URL 与 iPhone / iPad 上 **主屏 Quick Actions**（长按图标）指向相同目的地。

> **说明：** URL 仅用于 **应用内导航**，不会自动连接设备、发起传输或打开某个聊天会话。

## 协议规范

```
iconnect://<host>
iconnect://<host>?refresh=1
```

| 规则 | 说明 |
|------|------|
| **Scheme** | `iconnect` |
| **Host / 路径** | 单段名称，**不区分大小写** — 从 URL **host** 或第一段 **path** 解析 |
| **别名** | 部分 host 支持同义词（见下表） |
| **Query** | 仅 **设备** 页支持 `refresh=1` / `refresh=true` 触发重新扫描 |

---

## Tab 入口

| URL | 打开 | 别名 |
|-----|------|------|
| `iconnect://devices` | **设备** Tab（雷达 / 发现） | `device` |
| `iconnect://devices?refresh=1` | **设备** Tab 并**刷新**附近设备 | — |
| `iconnect://chat` | **聊天** Tab | `messages` |
| `iconnect://transfers` | **传输** Tab | `transfer` |
| `iconnect://history` | **历史** Tab（传输记录） | — |
| `iconnect://settings` | **设置** Tab | `setting` |

**刷新发现**

```
iconnect://devices?refresh=1
iconnect://devices/refresh
```

---

## 设置子页面

以下链接会先进入 **设置**，再打开对应页面：

| URL | 打开 | 别名 |
|-----|------|------|
| `iconnect://about` | 关于 | — |
| `iconnect://usage` | 使用说明 | `guide`、`help`、`usageguide` |
| `iconnect://shortcuts` | 主屏快捷指令配置（iOS） | `homeshortcuts` |
| `iconnect://debug` | 调试 / 诊断信息 | `debuginfo` |

---

## 应用内操作

| URL | 打开 |
|-----|------|
| `iconnect://share` | 分享爱联（App Store 链接 + 推荐文案） |
| `iconnect://feedback` | 意见反馈邮件（无邮件账户时回退 `mailto:`） |
| `iconnect://review` | 应用内 App Store 评分 |

**评分别名：** `iconnect://rate`、`iconnect://rating`

---

## 示例

```
iconnect://chat
iconnect://transfers
iconnect://devices?refresh=1
iconnect://usage
iconnect://share
```

---

## 主屏 Quick Actions（iOS）

长按爱联图标。在 **设置 → 主屏快捷指令** 中最多选 **4** 项并排顺序。

| 快捷指令 | URL |
|----------|-----|
| 设备 | `iconnect://devices` |
| 聊天 | `iconnect://chat` |
| 传输 | `iconnect://transfers` |
| 历史 | `iconnect://history` |
| 分享 | `iconnect://share` |
| 反馈 | `iconnect://feedback` |
| 评分 | `iconnect://review` |
| 关于 | `iconnect://about` |

默认启用：**设备**、**聊天**、**分享**、**反馈**。

---

## 苹果快捷指令

**打开传输 Tab**

1. 添加 **打开 URL**
2. URL：`iconnect://transfers`

**连上 Wi‑Fi 后刷新附近设备**

```
iconnect://devices?refresh=1
```

可在个人自动化（例如「Wi‑Fi 连接时」）中使用 **打开 URL**。

---

## 启动行为

- Tab 切换立即执行；**分享**、**反馈**、**评分** 在 iOS 上约延迟 0.4 秒后弹出，以便界面完成加载。
- **反馈** 优先使用应用内邮件；否则打开系统邮件客户端。
- Mac 上 **分享** 使用系统分享面板。

---

## 常见问题

| 现象 | 处理 |
|------|------|
| 链接无反应 | 确认已安装爱联；host 须为上表支持名称 |
| `feedback` 只打开邮件 App | 设备未配置邮件账户 — 属正常回退 |
| Mac 上 `shortcuts` 无效 | 主屏快捷指令配置**仅 iOS** |
| URL 无法连接设备 | 深度链接仅导航 — 请在设备 Tab 手动发现 |

---

[返回爱联支持](..) · [常见问题](../faq) · [隐私政策](../privacy)

</section>
<section lang="zh-TW" markdown="1">

愛聯（iConnect）支援 **`iconnect://`** URL Scheme 深度連結——可從 Safari、其他 App、書籤或 Apple 捷徑開啟指定 Tab、設定頁或應用內操作。這些 URL 與 iPhone / iPad 上 **主畫面 Quick Actions**（長按圖示）指向相同目的地。

> **說明：** URL 僅用於 **應用內導覽**，不會自動連線裝置、發起傳輸或開啟某個聊天對話。

## 協定規範

```
iconnect://<host>
iconnect://<host>?refresh=1
```

| 規則 | 說明 |
|------|------|
| **Scheme** | `iconnect` |
| **Host / 路徑** | 單段名稱，**不區分大小寫** — 從 URL **host** 或第一段 **path** 解析 |
| **別名** | 部分 host 支援同義詞（見下表） |
| **Query** | 僅 **裝置** 頁支援 `refresh=1` / `refresh=true` 觸發重新掃描 |

---

## Tab 入口

| URL | 開啟 | 別名 |
|-----|------|------|
| `iconnect://devices` | **裝置** Tab（雷達 / 探索） | `device` |
| `iconnect://devices?refresh=1` | **裝置** Tab 並**刷新**附近裝置 | — |
| `iconnect://chat` | **聊天** Tab | `messages` |
| `iconnect://transfers` | **傳輸** Tab | `transfer` |
| `iconnect://history` | **歷史** Tab（傳輸紀錄） | — |
| `iconnect://settings` | **設定** Tab | `setting` |

**刷新探索**

```
iconnect://devices?refresh=1
iconnect://devices/refresh
```

---

## 設定子頁面

以下連結會先進入 **設定**，再開啟對應頁面：

| URL | 開啟 | 別名 |
|-----|------|------|
| `iconnect://about` | 關於 | — |
| `iconnect://usage` | 使用說明 | `guide`、`help`、`usageguide` |
| `iconnect://shortcuts` | 主畫面捷徑設定（iOS） | `homeshortcuts` |
| `iconnect://debug` | 偵錯 / 診斷資訊 | `debuginfo` |

---

## 應用內操作

| URL | 開啟 |
|-----|------|
| `iconnect://share` | 分享愛聯（App Store 連結 + 推薦文案） |
| `iconnect://feedback` | 意見回饋郵件（無郵件帳戶時回退 `mailto:`） |
| `iconnect://review` | 應用內 App Store 評分 |

**評分別名：** `iconnect://rate`、`iconnect://rating`

---

## 範例

```
iconnect://chat
iconnect://transfers
iconnect://devices?refresh=1
iconnect://usage
iconnect://share
```

---

## 主畫面 Quick Actions（iOS）

長按愛聯圖示。在 **設定 → 主畫面捷徑** 中最多選 **4** 項並排序。

| 捷徑 | URL |
|------|-----|
| 裝置 | `iconnect://devices` |
| 聊天 | `iconnect://chat` |
| 傳輸 | `iconnect://transfers` |
| 歷史 | `iconnect://history` |
| 分享 | `iconnect://share` |
| 回饋 | `iconnect://feedback` |
| 評分 | `iconnect://review` |
| 關於 | `iconnect://about` |

預設啟用：**裝置**、**聊天**、**分享**、**回饋**。

---

## Apple 捷徑

**開啟傳輸 Tab**

1. 新增 **打開 URL**
2. URL：`iconnect://transfers`

**連上 Wi‑Fi 後刷新附近裝置**

```
iconnect://devices?refresh=1
```

---

## 啟動行為

- Tab 切換立即執行；**分享**、**回饋**、**評分** 在 iOS 上約延遲 0.4 秒後彈出。
- **回饋** 優先使用應用內郵件；否則開啟系統郵件用戶端。
- Mac 上 **分享** 使用系統分享面板。

---

## 常見問題

| 現象 | 處理 |
|------|------|
| 連結無反應 | 確認已安裝愛聯；host 須為上表支援名稱 |
| `feedback` 只開啟郵件 App | 裝置未設定郵件帳戶 — 屬正常回退 |
| Mac 上 `shortcuts` 無效 | 主畫面捷徑設定**僅 iOS** |
| URL 無法連線裝置 | 深度連結僅導覽 — 請在裝置 Tab 手動探索 |

---

[返回愛聯支援](..) · [常見問題](../faq) · [隱私政策](../privacy)

</section>
<section lang="ja" markdown="1">

iConnectは** `iconnect://` **をサポート URLスキームの深いリンク — タブ、設定ページ、またはSafari、別のアプリ、ブックマーク、またはAppleショートカットからアプリ内シートを開きます。 これらのURLは、iPhoneとiPadで**ホーム画面クイックアクション**として利用可能な目的地をミラーリングします(アプリアイコンを長押し)。

> **注記:** URL は iConnect** 内の **navigate** のみリンクします。 相手に接続したり、転送を開始したり、特定のチャットスレッドを開くことはありません。

## プロトコル仕様


```
iconnect://<host>
iconnect://<host>?refresh=1
```


| Rule | 詳細を見る |
|------|--------|
| **Scheme** | ツイート |
| **Host / path** | 単一のセグメント、**case-inpathy** — URL**host**またはfirst **path**セグメントから解決 |
| **Aliases** | 複数のホストは同義語を受け入れます(下の表を参照して下さい) |
| **Query** | "refresh=1`/`refresh=true` のみ**Devices** はディスカバリーリフレッシュをトリガーします |

同等形態の例:


```
iconnect://devices
iconnect://open/devices
```


---

## タブの宛先

| URL | 開く画面 |
|-----|--------|---------|
| `iconnect://devices` | **Devices** tab (radar / discovery) | デバイス |
| `iconnect://devices?refresh=1` | **Devices** tab and **refreshes** nearby discovery | — |
| `iconnect://chat` | **Chats** tab | 「メッセージ」 |
| `iconnect://transfers` | **Transfers** tab | トランスファー |
| `iconnect://history` | **History** tab (transfer log) | — |
| `iconnect://settings` | **Settings** tab | ログイン |

**参考文献**


```
iconnect://devices?refresh=1
iconnect://devices/refresh
```


---

## 設定サブページ

これらのリンクは、**Settings**に切り替え、一致するページを開きます。

| URL | 開く画面 |
|-----|--------|---------|
| `iconnect://about` | About | — |
| `iconnect://usage` | Usage Guide | `guide`、`help`、`usageguide` |
| `iconnect://shortcuts` | Home Screen shortcuts picker (iOS) | 「ホームショートカット」 |
| `iconnect://debug` | Debug / diagnostics info | `debuginfo` |

---

## アプリ内アクション

| URL | 開く画面 |
|-----|--------|
| `iconnect://share` | iConnectシート共有(App Storeリンク+推奨テキスト) |
| `iconnect://feedback` | フィードバックメールコンポーズ(メールが利用できなくなった場合は、`mailto:` に戻ってフォール) |
| `iconnect://review` | アプリ内アプリ 店の評価のプロンプト |

**レビューエイリアス:** `iconnect://` 、 `iconnect` ---

## 例

**チャットタブを開く**


```
iconnect://chat
```


**転送タブを開く**


```
iconnect://transfers
```


**リフレッシュ装置発見**


```
iconnect://devices?refresh=1
```


**オープン利用ガイド**


```
iconnect://usage
```


**アプリを共有する**


```
iconnect://share
```


---

## ホーム スクリーンクイックアクション (iOS)

iConnectアイコンを長押しします。 **設定 → ホーム画面のショートカット** (再注文するドラッグ)で最大** 4**ショートカットをカスタマイズします。

| Quick Action | サイトマップ |
|--------------|-----|
| Devices | `iconnect://devices` |
| Chats | チャット |
| Transfers | `iconnect://transfer` |
| History | 「iconnect://history」とは |
| Share | 「iconnect://share」 |
| Feedback | `iconnect://feedback` |
| Rate | 「iconnect://review」の |
| About | [iconnect://about`] |

デフォルトで有効:**Devices**、**Chats**、**Share**、**Feedback**。

クイックアクション型は、同じ `iconnect://` 文字列を使用し、外部 URL と同じパーサでルーティングされます。

---

## Appleのショートカット

**転送タブを開く**

1. アクションを追加**URLを開く**
2. URL: `iconnect://` **Wi-Fiに加入した後、近くのデバイスをリフレッシュ**


```
iconnect://devices?refresh=1
```


パーソナルオートメーション(Wi-Fi接続時など)で[URL**を開く]を使用して、発見と再スキャンにジャンプします。

---

## 起動動作

iConnect が URL を受信したときに (cold start または while run)

1. リンクは `iconnect://` で区切られます。
2. タブはすぐにアニメーションを切り替えます。**share**、**feedback**、および**review**は短い遅延(iOSの~0.4 s)後に開くので、UIは取り付けを完了することができます。
3。**Feedback**は、利用可能なときにアプリ内メールを使用します。 それ以外の場合は、 `iconnect://` でデフォルトのメールクライアントを開きます。
4。 Mac上で**共有**は、システム共有ピッカーを使用しています。 iOSでは共有シートが表示されます。

---

## トラブルシューティング

| Issue | 確認する |
|-------|----------------|
| Link does nothing | iConnectがインストールされていることを確認してください。ホストは上記のサポート名に一致しなければなりません |
| `feedback` opens Mail only | デバイスで設定されたメールアカウントがない — 期待されるフォールバック |
| `shortcuts` has no effect on Mac | ホーム スクリーンのショートカットのカスタマイズは**iOS専用** |
| URL does not connect to a device | ディープリンクのみのナビゲーション — デバイスタブを使用して、手動でピアを発見 |

---

[iConnectサポートに戻る](..)・ [FAQ](../faq)・ [プライバシーポリシー](../privacy)

</section>
<section lang="ko" markdown="1">

iConnect 지원 ** `iconnect://` ** URL 계획 딥 링크 — 탭을 열고, 설정 페이지, 또는 사파리에서 인앱 시트, 다른 응용 프로그램, 북마크, 또는 애플 단축키. 이 URL은 iPhone 및 iPad에서 **홈 화면 빠른 동작 **로 사용할 수있는 목적지를 미러합니다 (앱 아이콘을 길게 누릅니다).

> **참고: ** URL 링크만 ** iConnect 내부의 navigate **. 그들은 동료에 연결하지 않고 전송을 시작하거나 특정 채팅 스레드를 엽니 다.

## 프로토콜


```
iconnect://<host>
iconnect://<host>?refresh=1
```


| Rule | 제품 정보 |
|------|--------|
| **Scheme** | `iconnect``를 |
| **Host / path** | 단일 세그먼트,**case-insensitive** — URL**host** 또는 첫번째 **path** 세그먼트에서 해결 |
| **Aliases** | 몇몇 주인은 동의를 받아들입니다 (아래 표 참조) |
| **Query** | 단지 `refresh=1`/`refresh=true` 에 **Devices** 트리거 발견 새로 고침 |

동등한 형태의 예:


```
iconnect://devices
iconnect://open/devices
```


---

## 탭 대상

| URL | 열리는 화면 |
|-----|--------|---------|
| `iconnect://devices` | **Devices** tab (radar / discovery) | `장치` |
| `iconnect://devices?refresh=1` | **Devices** tab and **refreshes** nearby discovery | — |
| `iconnect://chat` | **Chats** tab | `메시지` |
| `iconnect://transfers` | **Transfers** tab | `전송` |
| `iconnect://history` | **History** tab (transfer log) | — |
| `iconnect://settings` | **Settings** tab | `설정` |

**추천**


```
iconnect://devices?refresh=1
iconnect://devices/refresh
```


---

## 설정 하위 페이지

이 링크 스위치 ** 설정**, 다음 일치하는 페이지를 엽니다:

| URL | 열리는 화면 |
|-----|--------|---------|
| `iconnect://about` | About | — |
| `iconnect://usage` | Usage Guide | `guide`, `help`, `usageguide` |
| `iconnect://shortcuts` | Home Screen shortcuts picker (iOS) | `homeshortcuts``에 대하여 |
| `iconnect://debug` | Debug / diagnostics info | `debuginfo````를 호출합니다. |

---

## In-app 작업

| URL | 열리는 화면 |
|-----|--------|
| `iconnect://share` | iConnect 시트 (App Store 링크 + 권장 텍스트) |
| `iconnect://feedback` | 피드백 이메일 compose (우편이 사용 불가) |
| `iconnect://review` | 앱 앱 상점 평가 신속한 |

**리뷰 별명:** `iconnect://` , `iconnect` ---

## 예시

** 채팅 탭 열기 **


```
iconnect://chat
```


**환불 탭 열기 **


```
iconnect://transfers
```


** Refresh 장치 발견 **


```
iconnect://devices?refresh=1
```


**사용 가이드**


```
iconnect://usage
```


** 앱 공유 **


```
iconnect://share
```


---

## 홈 화면 빠른 행동 (iOS)

iConnect 아이콘을 오래 누르십시오. **4** shortcuts in **Settings → Home Screen Shortcuts** (주문에 드래그).

| Quick Action | 사이트 맵 |
|--------------|-----|
| Devices | `iconnect://장치` |
| Chats | `iconnect://chat`````````` |
| Transfers | `iconnect://transfers```를 입력합니다. |
| History | `iconnect://history````````` |
| Share | `iconnect://share`````````` |
| Feedback | `iconnect://feedback```````` |
| Rate | [공식 홈페이지] |
| About | `iconnect://about`에 관하여 |

기본 활성화: **Devices**, **Chats**, **Share**, **Feedback**.

Quick-action 유형은 동일한 `iconnect://` 문자열을 사용하며 외부 URL과 동일한 파서를 통해 경로화됩니다.

---

## Apple 바로가기

**환불 탭 열기 **

1. 행동 추가 ** URL 열기 **
2. URL: `iconnect://` ** Wi-Fi 가입 후 주변 장치 검색 **


```
iconnect://devices?refresh=1
```


use **Open URL** 개인 자동화에서 (예: Wi-Fi가 연결될 때) 검색 및 재스캔으로 이동합니다.

---

## 시작 동작

iConnect가 URL (cold 시작 또는 실행 중)을받을 때 :

1. 링크는 `iconnect://` 에 의해 파싱됩니다.
2. 탭은 즉시 animate를 전환합니다; **share**, **feedback**, **review**는 짧은 지연 후에 열립니다 (~0.4 iOS에서 s) 그래서 UI는 설치를 완료할 수 있습니다.
3.**Feedback**는 in-app Mail을 사용할 때 사용합니다. 그렇지 않으면 `iconnect://` 를 통해 기본 메일 클라이언트를 엽니다.
4. ** 공유 ** Mac에서는 시스템 공유 피커를 사용합니다. iOS에서는 공유 시트를 제공합니다.

---

## 문제 해결

| Issue | 자주 묻는 질문 |
|-------|----------------|
| Link does nothing | iConnect가 설치됩니다. 호스트는 위의 지원 이름을 일치해야합니다. |
| `feedback` opens Mail only | 장치에서 구성된 메일 계정 없음 — 예상되는 fallback |
| `shortcuts` has no effect on Mac | 홈 화면 바로 가기 사용자 정의 **iOS 전용 ** |
| URL does not connect to a device | 딥 링크만 탐색 — 장치 탭을 사용하여 찾기를 수동으로 |

---

[iConnect Support](..) · [FAQ](../faq) · [Privacy Policy](../privacy)

</section>
<section lang="ru" markdown="1">

iConnect поддерживает ** `iconnect://` ** Схема URL глубоких ссылок — откройте вкладку, страницу настроек или лист в приложении от Safari, другое приложение, закладку или ярлыки Apple. Эти URL-адреса отражают пункты назначения, доступные как * * Home Screen Quick Actions * * на iPhone и iPad (нажмите значок приложения).

> ** Примечание: ** URL-ссылки только ** перемещаются внутри iConnect**. Они не подключаются к одноранговому устройству, не запускают передачу или не открывают определенную нить чата.

## Спецификация протокола


```
iconnect://<host>
iconnect://<host>?refresh=1
```


| Rule | Подробнее |
|------|--------|
| **Scheme** | "подключение" |
| **Host / path** | Единый сегмент, **case-insensitive** — решен из URL **host** или первого **path** сегмента |
| **Aliases** | Несколько хостов принимают синонимы (см. таблицу ниже) |
| **Query** | Только «refresh=1» / «refresh=true» на **Устройствах** запускает обновление обнаружения |

Примеры эквивалентных форм:


```
iconnect://devices
iconnect://open/devices
```


---

## Пункты назначения Tab

| URL | Открывает |
|-----|--------|---------|
| `iconnect://devices` | **Devices** tab (radar / discovery) | "устройство" |
| `iconnect://devices?refresh=1` | **Devices** tab and **refreshes** nearby discovery | — |
| `iconnect://chat` | **Chats** tab | "Послания" |
| `iconnect://transfers` | **Transfers** tab | "передача" |
| `iconnect://history` | **History** tab (transfer log) | — |
| `iconnect://settings` | **Settings** tab | "установка" |

**Обновить открытие**


```
iconnect://devices?refresh=1
iconnect://devices/refresh
```


---

## Настройки подстраниц

Эти ссылки переключаются на ** Настройки **, затем откройте соответствующую страницу:

| URL | Открывает |
|-----|--------|---------|
| `iconnect://about` | About | — |
| `iconnect://usage` | Usage Guide | "руководство", "помощь", "руководство по эксплуатации" |
| `iconnect://shortcuts` | Home Screen shortcuts picker (iOS) | "домашние сокращения" |
| `iconnect://debug` | Debug / diagnostics info | "дебугинфо" |

---

## Действия в приложении

| URL | Открывает |
|-----|--------|
| `iconnect://share` | Share iConnect sheet (ссылка на App Store + текст рекомендации) |
| `iconnect://feedback` | Композиция электронной почты обратной связи (возвращается к «mailto»: если почта недоступна) |
| `iconnect://review` | In-app приложение Рейтинг магазина быстро |

**Обзор псевдонимов: ** `iconnect://` , `iconnect` ---

## Примеры

** Открытая вкладка чатов**


```
iconnect://chat
```


** Открытая вкладка **


```
iconnect://transfers
```


** Открытие нового устройства**


```
iconnect://devices?refresh=1
```


** Руководство по открытому использованию**


```
iconnect://usage
```


**Поделиться приложением**


```
iconnect://share
```


---

## Быстрые действия (iOS)

Нажмите на иконку iConnect. Настройка до **4** ярлыков в ** Настройки → Ярлыки домашнего экрана ** (перезагрузка для переупорядочения).

| Quick Action | URL |
|--------------|-----|
| Devices | "подключение://устройства" |
| Chats | "iconnect://chat" |
| Transfers | "iconnect://transfers" |
| History | "iconnect://История" |
| Share | "iconnect://share" |
| Feedback | "iconnect://feedback" |
| Rate | "iconnect://review" |
| About | "iconnect://about" |

По умолчанию включено: **Устройства**, **Шаты**, **Поделиться**, **Обратная связь**.

Типы быстрого действия используют те же строки `iconnect://` и маршрутизируются через тот же парсер, что и внешние URL.

---

## Apple Shortcuts

** Открытая вкладка **

1 Добавить действие ** Открытый URL**
2. URL: `iconnect://` ** Обновите близлежащие устройства после подключения к Wi-Fi**


```
iconnect://devices?refresh=1
```


Используйте **Открытый URL** в Личной Автоматизации (например, при подключении Wi-Fi), чтобы перейти к обнаружению и сканированию.

---

## Запуск поведения

Когда iConnect получает URL (холодный запуск или во время работы):

1.Ссылка разбирается по `iconnect://` .
2. Переключатели вкладок анимируются немедленно; **share**, **feedback** и **review** открываются после короткой задержки (~0,4 с на iOS), поэтому пользовательский интерфейс может завершить установку.
3. ** Обратная связь** использует встроенную Почту, когда она доступна; в противном случае открывает почтовый клиент по умолчанию через `iconnect://` .
4. **Share** на Mac использует системный сборщик акций; на iOS он представляет лист акций.

---

## устранение неполадок

| Issue | Что проверить |
|-------|----------------|
| Link does nothing | Убедитесь, что iConnect установлен; хост должен соответствовать поддерживаемому имени выше |
| `feedback` opens Mail only | Нет учетной записи Mail, настроенной на устройстве — ожидаемый откат |
| `shortcuts` has no effect on Mac | Настройка ярлыка домашнего экрана - **только для iOS** |
| URL does not connect to a device | Глубокие ссылки только перемещаются — используйте вкладку «Устройства», чтобы вручную обнаруживать сверстников |

---

[Back to iConnect Support] (..) · [FAQ] (../faq) · [Политика конфиденциальности] (../privacy)

</section>
<section lang="th" markdown="1">

iNect รองรับ~ `iconnect://` BAR ~ ที่อยู่ URL วางรูปแบบลิงก์ลึก ๆ — เปิดแท็บ, หน้าการตั้งค่า, หรือแผ่นในเว็บจากซาฟารี, แอพพลิเคชันอื่น, ปุ่มพิมพ์ลัดของที่คั่นหน้า หรือแอปเปิล ที่อยู่ URL เหล่านี้จะสะท้อนไปยังปลายทางที่มีให้ใช้เป็น ~Home หน้าจอด่วน ~ บนไอโฟนและไอแพด (กดที่ไอคอนโปรแกรม)

> ** ข้อสังเกต: ** เชื่อมโยงที่อยู่ URL เท่านั้น ** พวก เขา ไม่ ได้ ติด ต่อ กับ คน รุ่น เดียว กัน, เริ่ม การ ย้าย ถิ่น, หรือ เปิด เส้น ทาง สนทนา โดย เฉพาะ.

## การกําหนดโพรโทคอล


```
iconnect://<host>
iconnect://<host>?refresh=1
```


| Rule | รายละเอียด |
|------|--------|
| **Scheme** | 'การเชื่อมต่อ' |
| **Host / path** | สัดส่วนเดียว... . ความไวแสง |
| **Aliases** | เจ้า ภาพ หลาย คน ยอม รับ คํา อธิบาย (ดู ตาราง ข้าง ล่าง) |
| **Query** | เพียง แต่ 'Refresh=1' / 'Refresh=true' บน ~devices ~ จุดชนวนการค้นพบรีเฟรช |

ตัวอย่างของรูปแบบที่เหมือนกัน:


```
iconnect://devices
iconnect://open/devices
```


---

## ปลายทางของแท็บ

| URL | เปิด |
|-----|--------|---------|
| `iconnect://devices` | **Devices** tab (radar / discovery) | 'ประกาศ' |
| `iconnect://devices?refresh=1` | **Devices** tab and **refreshes** nearby discovery | — |
| `iconnect://chat` | **Chats** tab | 'ข้อความ' |
| `iconnect://transfers` | **Transfers** tab | (เพลง) |
| `iconnect://history` | **History** tab (transfer log) | — |
| `iconnect://settings` | **Settings** tab | 'ตั้งค่า' |

~การค้นพบอีกครั้ง~


```
iconnect://devices?refresh=1
iconnect://devices/refresh
```


---

## ตั้งค่าหน้าย่อย

ลิงก์เหล่านี้สลับไปยัง ~ตั้งค่า~ แล้วเปิดหน้าที่เข้าคู่กัน:

| URL | เปิด |
|-----|--------|---------|
| `iconnect://about` | About | — |
| `iconnect://usage` | Usage Guide | (จะมีคําบัญชาแก่มะลาอิกะฮฺว่า) จงนําเขาไป |
| `iconnect://shortcuts` | Home Screen shortcuts picker (iOS) | 'กลับบ้าน' |
| `iconnect://debug` | Debug / diagnostics info | 'ลบข้อมูล' |

---

## การกระทํากับโปรแกรม

| URL | เปิด |
|-----|--------|
| `iconnect://share` | แผ่นข้อมูลร่วม (ข้อความแนะนําของ App Sport & application) |
| `iconnect://feedback` | เขียนจดหมายที่ส่งแล้ว |
| `iconnect://review` | แอปแบบรวม จัดเก็บการแจ้งเตือนการจัดอันดับ |

** ดูรายละเอียด: ~ BAR `iconnect://` BAR `iconnect` BAR

---

## ตัวอย่าง

~ เปิดแท็บ~


```
iconnect://chat
```


** เปิดทําการถ่ายโอนแท็บ **


```
iconnect://transfers
```


** ค้นพบอุปกรณ์ใหม่ **


```
iconnect://devices?refresh=1
```


~คู่มือใช้ใช้งาน~


```
iconnect://usage
```


~เก็บแอพไว้~


```
iconnect://share
```


---

## การกระทําด่วนของหน้าจอส่วนตัว (OS)

กดยาวไอคอนไอคอนเน็ค ปรับค่าเทียบกับ < 4 ** ทางลัดใน **

| Quick Action | ที่อยู่ URL |
|--------------|-----|
| Devices | การเชื่อมต่อ |
| Chats | 'การเชื่อมต่อ' |
| Transfers | การเชื่อมต่อผู้ติดตาม |
| History | สืบค้นประวัติ |
| Share | 'การแบ่งปัน' |
| Feedback | 'TIFTIATIA' |
| Rate | 'การเชื่อมต่อ' |
| About | (กระซิบ) |

เปิดใช้งานปริยายได้: ~devicess ~ ~~~~~~~~~, ~หลัง ~

ประเภทการกระทําเร็ว ใช้  c0   สตริง และเส้นทางไปยังที่อยู่ URL ภายนอกแบบเดียวกัน

---

## ปุ่มพิมพ์ลัดของแอปเปิล

** เปิดทําการถ่ายโอนแท็บ **

1. เพิ่มการกระทํา... เปิดที่อยู่ URL ~
2. ที่อยู่ URL:   ค.ศ.

** ปรับปรุงอุปกรณ์ที่อยู่ใกล้เคียงอีกครั้ง หลังจากเข้าร่วมโครงการวิซไฟ~


```
iconnect://devices?refresh=1
```


ใช้ที่อยู่ URL แบบเปิด * ในระบบอัตโนมัติส่วนตัว (เช่น เมื่อ WwwiFi Connection) เพื่อกระโดดไปยังการค้นพบและแก้ไขใหม่

---

## พฤติกรรมการเรียกทํางาน

เมื่อเครื่องปลายทางได้รับที่อยู่ URL (เริ่มโปรแกรมหรือทํางาน):

1. ลิงก์ถูกวิเคราะห์โดย `iconnect://` .
2. สลับที่แท็บทันที; ** ใช้งานร่วมกัน **
3. ** คืนค่า ~ ใช้จดหมายเวียนเมื่อมีการใช้งานอยู่ ไม่เช่นนั้นจะเปิดไคลเอนต์จดหมายโดยปริยายผ่านทาง `iconnect://` BAR
4. ~Share ~ บนแมคใช้เครื่องเลือกหุ้นในระบบ; บน OS มันนําเสนอแผ่นหุ้น.

---

## การยิงปัญหา

| Issue | จะตรวจอะไร |
|-------|----------------|
| Link does nothing | แน่ใจว่า iconnect ได้ถูกติดตั้งแล้ว; โฮสต์ต้องตรงกับชื่อที่รองรับด้านบน |
| `feedback` opens Mail only | ไม่ มี การ กําหนด บัญชี อีเมล บน อุปกรณ์ — คาด ว่า จะ มี การ ถอย หลัง |
| `shortcuts` has no effect on Mac | การกําหนดปุ่มพิมพ์ลัดส่วนตัวของจอภาพมี <iOSเท่านั้น* |
| URL does not connect to a device | การ เชื่อม โยง ที่ ลึก เข้า ไป |

---

[การรองรับ iConnect] [. ] [FAQ] [./faq] สืบค้นเมื่อ 20 พฤษภาคม พ.ศ.

</section>
<section lang="de" markdown="1">

iConnect unterstützt ** `iconnect://` ** URL-Schema Deep Links - Öffnen Sie einen Tab, eine Einstellungsseite oder ein In-App-Blatt von Safari, einer anderen App, einem Lesezeichen oder Apple Shortcuts. Diese URLs spiegeln die verfügbaren Ziele als **Home Screen Quick Actions** auf iPhone und iPad wider (langes Drücken des App-Symbols).

> **Hinweis:** URL-Links nur **navigieren innerhalb von iConnect**. Sie verbinden sich nicht mit einem peer, starten eine Übertragung oder öffnen einen bestimmten chat-thread.

## Protokollspezifikation


```
iconnect://<host>
iconnect://<host>?refresh=1
```


| Rule | Einzelheiten |
|------|--------|
| **Scheme** | „iconnect |
| **Host / path** | Ein einzelnes Segment, **case-unsensitive ** - aufgelöst von URL **host ** oder erstem **path ** Segment |
| **Aliases** | Mehrere Hosts akzeptieren Synonyme (siehe Tabelle unten) |
| **Query** | Nur `refresh=1` / `refresh=true` auf **Devices** löst eine Discovery-Aktualisierung aus |

Beispiele für gleichwertige Formulare:


```
iconnect://devices
iconnect://open/devices
```


---

## Tab Destinationen

| URL | Öffnet |
|-----|--------|---------|
| `iconnect://devices` | **Devices** tab (radar / discovery) | "Gerät" |
| `iconnect://devices?refresh=1` | **Devices** tab and **refreshes** nearby discovery | — |
| `iconnect://chat` | **Chats** tab | "Botschaften" |
| `iconnect://transfers` | **Transfers** tab | „Übertragung |
| `iconnect://history` | **History** tab (transfer log) | — |
| `iconnect://settings` | **Settings** tab | "Setzen" |

**Refresh Discovery**


```
iconnect://devices?refresh=1
iconnect://devices/refresh
```


---

## Einstellungen Unterseiten

Diese Links wechseln zu **Settings** und öffnen dann die passende Seite:

| URL | Öffnet |
|-----|--------|---------|
| `iconnect://about` | About | — |
| `iconnect://usage` | Usage Guide | `guide`, `help`, `usageguide` |
| `iconnect://shortcuts` | Home Screen shortcuts picker (iOS) | „Homeshortcuts |
| `iconnect://debug` | Debug / diagnostics info | „Debuginfo |

---

## In-App-Aktionen

| URL | Öffnet |
|-----|--------|
| `iconnect://share` | Teilen Sie iConnect Blatt (App Store Link + Empfehlungstext) |
| `iconnect://feedback` | Feedback E-Mail compose (fällt zurück zu `mailto:`, wenn Mail nicht verfügbar ist) |
| `iconnect://review` | In-App App Aufforderung zur Abgabe von Speicherbewertungen |

**Review Aliase:** `iconnect://` , `iconnect` ---

## Beispiele

** Chats öffnen Tab**


```
iconnect://chat
```


**Offener Transfer-Tab**


```
iconnect://transfers
```


**Refresh Device Discovery**


```
iconnect://devices?refresh=1
```


**Open Usage Guide**


```
iconnect://usage
```


** Teilen Sie die App**


```
iconnect://share
```


---

## Startseite Bildschirm Quick Actions (iOS)

Langes Drücken des iConnect-Icons. Passen Sie bis zu **4** Shortcuts in **Settings → Home Screen Shortcuts ** an (drag to reorder).

| Quick Action | URL |
|--------------|-----|
| Devices | „iconnect://devices |
| Chats | „iconnect://chat |
| Transfers | „iconnect://transfers |
| History | „iconnect://history |
| Share | „iconnect://share |
| Feedback | „iconnect://feedback |
| Rate | „iconnect://review |
| About | „iconnect://about |

Standardmäßig aktiviert: **Geräte**, **Chats**, **Share**, **Feedback**.

Quick-Action-Typen verwenden die gleichen `iconnect://` -Strings und werden durch denselben Parser wie externe URLs geleitet.

---

## Apple Shortcuts

**Offener Transfer-Tab**

1. Aktion hinzufügen **Offene URL**
2. URL: `iconnect://` **Refresh in der Nähe Geräte nach dem Beitritt Wi‐Fi**


```
iconnect://devices?refresh=1
```


Verwenden Sie **Offene URL** in einer persönlichen Automatisierung (z. B. wenn Wi-Fi verbunden ist), um zum Suchen und Scannen zu springen.

---

## Startverhalten

Wenn iConnect eine URL erhält (Kaltstart oder während des Laufens):

1. Der Link wird durch `iconnect://` analysiert.
2. Tab-Schalter animieren sofort; **share**, **feedback** und **review** öffnen sich nach kurzer Verzögerung (~0,4 s auf iOS), damit die Benutzeroberfläche das Montieren beenden kann.
3. **Feedback** verwendet, wenn verfügbar, In-App-Mail; ansonsten wird der Standard-Mail-Client über `iconnect://` geöffnet.
**Share** auf dem Mac verwendet den System-Share-Picker; auf iOS präsentiert er ein Sharesheet.

---

## Fehlerbehebung

| Issue | Was zu überprüfen ist |
|-------|----------------|
| Link does nothing | Stellen Sie sicher, dass iConnect installiert ist; Host muss mit einem unterstützten Namen übereinstimmen |
| `feedback` opens Mail only | Kein auf dem Gerät konfiguriertes Mail-Konto — erwarteter Fallback |
| `shortcuts` has no effect on Mac | Home Screen Shortcut Anpassung ist ** iOS nur ** |
| URL does not connect to a device | Deep Links navigieren nur - Verwenden Sie die Registerkarte Geräte, um Peers manuell zu entdecken |

---

[Zurück zum iConnect Support](..) · [FAQ](../faq) · [Privacy Policy](../Privacy)

</section>
<section lang="fr" markdown="1">

iConnect prend en charge ** `iconnect://` ** Les liens profonds du schéma URL — ouvrez un onglet, une page Paramètres, ou une feuille d'application de Safari, une autre application, un signet ou des raccourcis Apple. Ces URL reflètent les destinations disponibles sous la forme de **Home Screen Quick Actions** sur iPhone et iPad (long-press l'icône de l'application).

> **Note:** Liens URL uniquement **navigate inside iConnect**. Ils ne se connectent pas à un pair, démarrent un transfert ou ouvrent un fil de discussion spécifique.

## Spécification du protocole


```
iconnect://<host>
iconnect://<host>?refresh=1
```


| Rule | Détail |
|------|--------|
| **Scheme** | `connecter` |
| **Host / path** | Un seul segment, **insensible aux cas** — résolu à partir de l'URL **host** ou du premier segment **path** |
| **Aliases** | Plusieurs hôtes acceptent les synonymes (voir tableau ci-dessous) |
| **Query** | Seulement `refresh=1` / `refresh=true` sur **Dispositifs** déclenche un rafraîchissement découverte |

Exemples de formulaires équivalents:


```
iconnect://devices
iconnect://open/devices
```


---

## Destinations des onglets

| URL | Ouvre |
|-----|--------|---------|
| `iconnect://devices` | **Devices** tab (radar / discovery) | "dispositif" |
| `iconnect://devices?refresh=1` | **Devices** tab and **refreshes** nearby discovery | — |
| `iconnect://chat` | **Chats** tab | "messages" |
| `iconnect://transfers` | **Transfers** tab | "transfert" |
| `iconnect://history` | **History** tab (transfer log) | — |
| `iconnect://settings` | **Settings** tab | «réglage» |

**Découverte nouvelle**


```
iconnect://devices?refresh=1
iconnect://devices/refresh
```


---

## Paramètres des sous-pages

Ces liens passent à **Paramètres**, puis ouvrez la page correspondante:

| URL | Ouvre |
|-----|--------|---------|
| `iconnect://about` | About | — |
| `iconnect://usage` | Usage Guide | «guide», «aide», «guide d'usage» |
| `iconnect://shortcuts` | Home Screen shortcuts picker (iOS) | "shortcuts à domicile" |
| `iconnect://debug` | Debug / diagnostics info | `debuginfo` |

---

## Actions en cours

| URL | Ouvre |
|-----|--------|
| `iconnect://share` | Partager la feuille iConnect (Lien de l'App Store + texte de recommandation) |
| `iconnect://feedback` | E-mail de rétroaction composer (reste à `mailto:` si le courrier n'est pas disponible) |
| `iconnect://review` | App dans l'application Note de magasin rapide |

**Alias de l'examen :** `iconnect://` , `iconnect` ---

## Exemples

**Ouvrir l'onglet Chats**


```
iconnect://chat
```


**Ouvrir l'onglet Transferts**


```
iconnect://transfers
```


**Découverte de l'appareil neuf**


```
iconnect://devices?refresh=1
```


**Guide d'utilisation ouvert**


```
iconnect://usage
```


**Partagez l'application**


```
iconnect://share
```


---

## Actions rapides d'écran d'accueil (iOS)

Appuyez sur l'icône iConnect. Personnalisez jusqu'à **4** raccourcis dans **Paramètres → raccourcis d'écran d'accueil** (gouttez pour réorganiser).

| Quick Action | URL |
|--------------|-----|
| Devices | `iconnect://devices` |
| Chats | "iconnect://chat" |
| Transfers | "iconnect://transferts" |
| History | "iconnect://histoire" |
| Share | `iconnect://share` |
| Feedback | `iconnect://feedback` |
| Rate | `iconnect://review` |
| About | `iconnect://about` |

Par défaut activé : **Dispositifs**, **Chats**, **Share**, **Feedback**.

Les types d'action rapide utilisent les mêmes chaînes `iconnect://` et sont acheminés par le même analyseur que les URL externes.

---

## Raccourcis des pommes

**Ouvrir l'onglet Transferts**

1. Ajouter une action **Ouvrir l'URL**
2. URL : `iconnect://` **Rénover les appareils à proximité après avoir joint le Wi-Fi**


```
iconnect://devices?refresh=1
```


Utilisez **Ouvrir l'URL** dans une automatisation personnelle (p. ex. quand Wi‐Fi se connecte) pour sauter à la découverte et à la recherche.

---

## Comportement de lancement

Lorsque iConnect reçoit une URL (démarrage froid ou en cours d'exécution):

1. Le lien est analysé par `iconnect://` .
2. L'onglet s'allume immédiatement; **share**, **feedback** et **review** s'ouvre après un court délai (~0,4 s sur iOS) pour que l'interface utilisateur puisse terminer le montage.
3. **Feedback** utilise le courrier dans l'application lorsque disponible; sinon ouvre le client de messagerie par défaut via `iconnect://` .
4. **Share** sur Mac utilise le sélecteur de partage système; sur iOS il présente une feuille de partage.

---

## Dépannage

| Issue | Quoi vérifier |
|-------|----------------|
| Link does nothing | Assurez-vous que iConnect est installé; l'hôte doit correspondre à un nom supporté ci-dessus |
| `feedback` opens Mail only | Aucun compte Mail configuré sur l'appareil — retour prévu |
| `shortcuts` has no effect on Mac | Home Screen raccourci personnalisation est **iOS-seulement** |
| URL does not connect to a device | Les liens profonds ne naviguent que — utilisez l'onglet Appareils pour découvrir les pairs manuellement |

---

[Retour à iConnect Support](..) · [FAQ](../faq) · [Politique de confidentialité](../privacy)

</section>
<section lang="tr" markdown="1">

iConnect ** `iconnect://` ** URL programı derin bağlantıları - bir sekme açın, bir Ayarlar sayfası veya Safari'den bir in-app sayfası, başka bir uygulama, bir kitap işareti veya Apple Shortcuts. Bu URL'ler **Home Ekran Hızlı Eylemler ** iPhone ve iPad'de ( Uygulama ikonunu uzun baskı) mevcut destinasyonları yansıtıyor.

> **Not: ** URL bağlantıları sadece ** iConnect** içinde kısaltılır. Bir eşe bağlanmazlar, bir transfere başlayın veya belirli bir sohbet ipine açın.

## Protokol Doğrulaması


```
iconnect://<host>
iconnect://<host>?refresh=1
```


| Rule | Detaylı Bilgi |
|------|--------|
| **Scheme** | " |
| **Host / path** | Single segment, **case-in sensitive** - URL **host** veya ilk **path** segmenti |
| **Aliases** | Birkaç ev eş anlamlı kabul eder (aşağıdaki tabloya bakın) |
| **Query** | Sadece "refresh=1" / "refresh=gerçek", **Devices** bir keşif yeniledi |

eşdeğer formların örnekleri:


```
iconnect://devices
iconnect://open/devices
```


---

## Tab destinasyonları

| URL | Açar |
|-----|--------|---------|
| `iconnect://devices` | **Devices** tab (radar / discovery) | " |
| `iconnect://devices?refresh=1` | **Devices** tab and **refreshes** nearby discovery | — |
| `iconnect://chat` | **Chats** tab | “Yeminler” |
| `iconnect://transfers` | **Transfers** tab | "Transfer" |
| `iconnect://history` | **History** tab (transfer log) | — |
| `iconnect://settings` | **Settings** tab | " |

**Refresh keşif**


```
iconnect://devices?refresh=1
iconnect://devices/refresh
```


---

## Ayarlar alt sayfalar

Bu bağlantılar **Settings **, sonra eşleşen sayfasını açın:

| URL | Açar |
|-----|--------|---------|
| `iconnect://about` | About | — |
| `iconnect://usage` | Usage Guide | “ Rehberlik”, “yardım”, “öğrenme” |
| `iconnect://shortcuts` | Home Screen shortcuts picker (iOS) | "Ev 6:cuts" |
| `iconnect://debug` | Debug / diagnostics info | "debuginfo" |

---

## In-app actions

| URL | Açar |
|-----|--------|
| `iconnect://share` | Share iConnect page (App Store link + öneri metni) |
| `iconnect://feedback` | Geri bildirim e-postası (postaya geri dönüyorsa) |
| `iconnect://review` | In-app App Mağaza derecelendirmesi |

**Review alias:** `iconnect://` , `iconnect` ---

## Örnekler

**Açık Sohbetler sekmesi **


```
iconnect://chat
```


**Açık Transferler sekmesi **


```
iconnect://transfers
```


**Refresh cihazı keşfi**


```
iconnect://devices?refresh=1
```


**Açık Kullanım Kılavuzu**


```
iconnect://usage
```


** Uygulamayı paylaşın **


```
iconnect://share
```


---

## Home Screen Quick Actions (iOS)

Long-press the iConnect icon. **4 ** kısayollarına kadar özelleştirin ** Ev Ekran kısayolları** (drag yeniden sipariş vermek için).

| Quick Action | URL URL URL URL |
|--------------|-----|
| Devices | "Ininvices" |
| Chats | "Saç" |
| Transfers | "Aptallar" |
| History | "Aptal" |
| Share | "Seks" |
| Feedback | "Arapback" |
| Rate | "In" (İngilizce). |
| About | "Saç" |

Varsayılan olarak etkinleştirin: **Devices**, **Chats**, **Share**, **Feedback**.

Hızlı aksiyon türleri aynı `iconnect://` dizeleri kullanır ve dış URL'ler olarak aynı . aracılığıyla yönlendirilir.

---

## Apple Shortcuts

**Açık Transferler sekmesi **

1. Hareket ekleyin **Open URL**
2. URL: `iconnect://` **Refresh, Wi-Fi'ye katıldıktan sonra yakın cihazlara üye oldu**


```
iconnect://devices?refresh=1
```


Use **Open URL ** in a Personal Automation (e.g. when Wi-Fi connect) to navigation and rescan.

---

## başlangıç davranışı

IConnect bir URL aldığında (cold start or while running):

1. bağlantı, `iconnect://` tarafından parsedilir.
2. Tab hemen animate kilitler; **share**, **feedback**, ve ** hakem ** kısa bir gecikmeden sonra açılır (~0.4 s iOS'ta) böylece UI monte edilebilir.
3. **Feedback** mevcut olduğunda Mail'de kullanılır; aksi takdirde varsayılan posta istemcisini `iconnect://` ile açın.
4. **Share** on Mac sistem pay seçiciini kullanır; iOS'ta bir pay sayfası sunar.

---

## Sorun Giderme

| Issue | Ne kontrol edecek |
|-------|----------------|
| Link does nothing | Emin iConnect kurulur; host yukarıda desteklenen bir isim eşleştirmeli |
| `feedback` opens Mail only | Cihazda yapılandırılan Mail hesabı yok - beklenen geri çekilme |
| `shortcuts` has no effect on Mac | Home Ekran kısayol özelleştirmesi **iOS-only** |
| URL does not connect to a device | Derin bağlantılar sadece gezinmek - akranları manuel olarak keşfetmek için cihazlar sekmesi kullanın |

---

[Back to iConnect Support](.)

</section>
