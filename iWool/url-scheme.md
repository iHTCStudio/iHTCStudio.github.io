---
layout: doc
title: iWool — URL Scheme Reference
app_id: iWool
doc_title_en: URL Scheme Reference
doc_title_zh_cn: URL Scheme 深度链接文档
doc_title_zh_tw: URL Scheme 深度連結文件
description: Complete reference of iwool:// deep links — tabs, actions, event detail, widgets and Home Screen Quick Actions.
---

<section lang="en" markdown="1">

iWool supports **`iwool://`** URL scheme deep links — open a tab, start an in-app action, or jump to a specific activity from Safari, Apple Shortcuts, a widget tap, or a Home Screen Quick Action (long-press the app icon).

> **Important:** Deep links only **navigate inside iWool**. They do not create server connections or sync data to the cloud.

## Protocol Specification

```
iwool://<path>[?query]
```

| Rule | Detail |
|------|--------|
| **Scheme** | `iwool` (case-insensitive) |
| **Routing** | First path segment (host or path) selects the destination |
| **Empty URL** | `iwool://` with no path → **Home** |
| **Unknown paths** | **Ignored** (no silent fallback to Home) |
| **Parser** | `IWoolDeepLink.parse(_:)` → `ContentView.applyDeepLink` |

---

## 1. Tab destinations

| URL | Opens | Aliases |
|-----|--------|---------|
| `iwool://home` | **Home** tab | — |
| `iwool://calendar` | **Calendar** tab | `cal` |
| `iwool://stats` | **Statistics** tab | `statistics`, `stat` |
| `iwool://settings` | **Settings** tab | `setting`, `preferences` |

---

## 2. In-app actions

These routes match **Home Screen Quick Actions** and open sheets or sub-pages:

| URL | Opens | Aliases |
|-----|--------|---------|
| `iwool://new` | **Create activity** sheet | `create`, `add`, `new-event`, `newevent` |
| `iwool://island` | **Quick Countdown** (Dynamic Island reminder) sheet | `island-reminder`, `islandreminder`, `countdown`, `quick-countdown`, `quickcountdown` |
| `iwool://reminders` | **Scheduled local reminders** list (Settings) | `scheduled-reminders`, `scheduledreminders`, `scheduled`, `notification-reminders` |
| `iwool://scanner` | **QR / barcode scanner** (Settings → Tools) | `scan`, `qrcode`, `barcode` |
| `iwool://rate` | In-app **App Store rating** prompt | `rating`, `review`, `rate-in-app`, `rateinapp` |
| `iwool://feedback` | **Feedback** email compose | `mail`, `support`, `contact` |

**Nested settings paths** (same actions):

```
iwool://settings/scanner
iwool://settings/reminders
iwool://settings/rate
iwool://settings/feedback
```

---

## 3. Activity detail

Open a single wool activity by database ID.

| Parameter | Required | Description |
|-----------|----------|-------------|
| Path `event/{id}` | One of path / query | Activity ID (positive integer) |
| Query `id={id}` | One of path / query | Same as path form |
| Query `day={seconds}` | No | For **recurring** activities — natural-day start as `timeIntervalSince1970` (midnight of that occurrence day) |

**Open activity 42**

```
iwool://event/42
iwool://event?id=42
```

**Recurring occurrence on a specific day**

```
iwool://event/42?day=189345600
```

When building links for recurring series, iWool can derive `day` from the same logic as the home list (`IWoolDeepLink.occurrenceDayStartForDeepLink`).

---

## 4. Home Screen Quick Actions (iOS)

Long-press the iWool icon → up to **4** actions. Customize in **Settings → Tools → Home Screen Shortcuts** (9 options, drag to reorder, reset to defaults).

| Option | URL |
|--------|-----|
| Home | `iwool://home` |
| Calendar | `iwool://calendar` |
| Statistics | `iwool://stats` |
| Quick Countdown | `iwool://island` |
| New Activity | `iwool://new` |
| Scheduled Reminders | `iwool://reminders` |
| Scanner | `iwool://scanner` |
| Rate App | `iwool://rate` |
| Feedback | `iwool://feedback` |

**Default on first install:** Home · Calendar · Statistics · Quick Countdown.

Quick-action `type` strings use the same `iwool://` paths and route through `ShortcutSceneDelegate` → `ShortcutObserver` on cold start.

---

## 5. Widget deep links

Widget taps use the same `iwool://` URLs:

| Widget | Tap target | URL |
|--------|------------|-----|
| Today Active / Today All / Today Upcoming / All Events | Home | `iwool://home` |
| Stats Overview / Earnings / Top Platforms | Statistics | `iwool://stats` |
| Glance | First event or Home | `iwool://event/{id}` or `iwool://home` |
| Lock Screen accessories | First event or Home | `iwool://event/{id}` or `iwool://home` |
| List row (iOS 17+) | Activity detail | `iwool://event/{id}` |

Quick Countdown Live Activities use in-app UI only — **no separate URL** to start an island countdown from outside the app (use `iwool://island` to open the creation sheet).

---

## Apple Shortcuts examples

**Open Statistics**

```
iwool://stats
```

**Create a new activity**

```
iwool://new
```

**Open Quick Countdown sheet**

```
iwool://island
```

**Open activity after copying ID**

```
iwool://event?id=42
```

---

## Launch behaviour

| Scenario | Flow |
|----------|------|
| **Widget / Shortcuts `onOpenURL`** | `AppRouter` → `applyDeepLink` |
| **Cold start — Quick Action** | `ShortcutSceneDelegate` → `PendingShortcutBuffer` → `ShortcutObserver` |
| **Warm start — Quick Action** | Scene callback → notification → `ShortcutObserver` |
| **Feedback / Rate (cold start)** | Short delay so mail sheet / StoreKit has an active window scene |
| **Invalid event ID** | Link ignored — no alert |

---

## Troubleshooting

| Issue | What to check |
|-------|----------------|
| Link opens app but nothing happens | Path must match a supported route; unknown paths are not redirected to Home |
| `event` link shows wrong occurrence | Add `?day=` for recurring activities |
| Quick Action does nothing on cold launch | Wait ~0.4 s or retry; feedback/rate need UI mount time |
| `iwool://island` does not start countdown automatically | Opens the **creation sheet** — confirm duration and tap Start inside the app |
| Quick Countdown requires iOS 16.2+ | Event Live Activities need iOS 16.1+; standalone island countdown needs 16.2+ |

---

[Back to iWool Support](..) · [FAQ](../faq) · [Privacy Policy](../privacy)

</section>
<section lang="zh-CN" markdown="1">

爱羊毛支持 **`iwool://`** URL Scheme 深度链接——从 Safari、苹果快捷指令、小组件点击或主屏快捷方式（长按图标）打开标签页、应用内操作或指定活动。

> **说明：** 深度链接仅用于**应用内导航**，不会连接服务器或上传数据。

## 协议规范

```
iwool://<path>[?query]
```

| 规则 | 说明 |
|------|------|
| **Scheme** | `iwool`（不区分大小写） |
| **空 URL** | `iwool://` → **首页** |
| **未知路径** | **忽略**（不再静默回首页） |

---

## 1. Tab 入口

| URL | 打开 | 别名 |
|-----|------|------|
| `iwool://home` | **首页** | — |
| `iwool://calendar` | **日历** | `cal` |
| `iwool://stats` | **统计** | `statistics`、`stat` |
| `iwool://settings` | **设置** | `setting`、`preferences` |

---

## 2. 应用内操作

| URL | 打开 | 别名 |
|-----|------|------|
| `iwool://new` | **新建活动** | `create`、`add`、`new-event` |
| `iwool://island` | **灵动岛提醒**（Quick Countdown 创建页） | `countdown`、`quick-countdown` 等 |
| `iwool://reminders` | **已登记本地提醒**列表 | `scheduled-reminders`、`scheduled` |
| `iwool://scanner` | **扫码器** | `scan`、`qrcode`、`barcode` |
| `iwool://rate` | 应用内**评分** | `rating`、`review` |
| `iwool://feedback` | **意见反馈** | `mail`、`support`、`contact` |

嵌套路径示例：`iwool://settings/scanner`

---

## 3. 活动详情

| 参数 | 说明 |
|------|------|
| `iwool://event/{id}` 或 `?id=` | 活动 ID |
| `?day={秒}` | 重复活动指定自然日 0 点的 `timeIntervalSince1970` |

```
iwool://event/42
iwool://event/42?day=189345600
```

---

## 4. 主屏快捷方式（iOS）

长按图标 → 最多 **4** 项。在 **设置 → 工具 → 主屏快捷方式** 配置（9 项可选）。

默认：**首页 · 日历 · 统计 · 灵动岛提醒**。

| 选项 | URL |
|------|-----|
| 首页 | `iwool://home` |
| 日历 | `iwool://calendar` |
| 统计 | `iwool://stats` |
| 灵动岛提醒 | `iwool://island` |
| 新建活动 | `iwool://new` |
| 已登记提醒 | `iwool://reminders` |
| 扫码 | `iwool://scanner` |
| 评分 | `iwool://rate` |
| 反馈 | `iwool://feedback` |

---

## 5. 小组件深度链接

| 小组件 | URL |
|--------|-----|
| 今日系列 / 全部活动 | `iwool://home` |
| 统计 / 收益 / 平台排行 | `iwool://stats` |
| 列表单行（iOS 17+） | `iwool://event/{id}` |

`iwool://island` 打开创建页，不会从外部直接启动倒计时——需在应用内确认时长。

---

## 示例

```
iwool://stats
iwool://new
iwool://island
iwool://event?id=42
```

---

## 常见问题

| 现象 | 处理 |
|------|------|
| 链接无反应 | 路径须为支持名称；无效路径不会回首页 |
| 重复活动场次不对 | 加 `?day=` 参数 |
| 灵动岛提醒需 iOS 16.2+ | 活动 Live Activity 为 16.1+ |

---

[返回爱羊毛支持](..) · [常见问题](../faq) · [隐私政策](../privacy)

</section>
<section lang="zh-TW" markdown="1">

愛羊毛支援 **`iwool://`** URL Scheme 深度連結——從 Safari、Apple 捷徑、小工具點擊或主畫面捷徑（長按圖示）開啟標籤頁、應用內操作或指定活動。

> **說明：** 深度連結僅用於**應用內導覽**，不會連接伺服器或上傳資料。

## 協定規範

| 規則 | 說明 |
|------|------|
| **Scheme** | `iwool` |
| **空 URL** | `iwool://` → **首頁** |
| **未知路徑** | **忽略** |

---

## 1. Tab 入口

| URL | 開啟 | 別名 |
|-----|------|------|
| `iwool://home` | **首頁** | — |
| `iwool://calendar` | **日曆** | `cal` |
| `iwool://stats` | **統計** | `statistics`、`stat` |
| `iwool://settings` | **設定** | `setting`、`preferences` |

---

## 2. 應用內操作

| URL | 開啟 | 別名 |
|-----|------|------|
| `iwool://new` | **新建活動** | `create`、`add` |
| `iwool://island` | **靈動島提醒**（Quick Countdown） | `countdown`、`quick-countdown` |
| `iwool://reminders` | **已登記本地提醒** | `scheduled-reminders` |
| `iwool://scanner` | **掃碼器** | `scan`、`qrcode` |
| `iwool://rate` | 應用內**評分** | `rating`、`review` |
| `iwool://feedback` | **意見回饋** | `mail`、`support` |

---

## 3. 活動詳情

```
iwool://event/42
iwool://event/42?day=189345600
```

`?day=` 為重複活動指定自然日場次。

---

## 4. 主畫面捷徑（iOS）

最多 **4** 項；**設定 → 工具 → 主畫面捷徑**（9 項可選）。預設：首頁 · 日曆 · 統計 · 靈動島提醒。

---

## 5. 小工具連結

今日系列 → `iwool://home`；統計系列 → `iwool://stats`；列表列 → `iwool://event/{id}`。

---

[返回愛羊毛支援](..) · [常見問題](../faq) · [隱私政策](../privacy)

</section>
<section lang="ja" markdown="1">

iWool サポート ** `iwool://` ** URLスキームのディープリンク — タブを開き、アプリ内アクションを開始したり、Safari、Apple Shortcuts、ウィジェットタップ、またはホーム画面クイックアクションから特定のアクティビティにジャンプしたりできます。

> **重要:** ディープリンクのみ**iWool内でナビゲート**。 サーバ接続やデータをクラウドに同期させません。

## プロトコル仕様


```
iwool://<path>[?query]
```


| Rule | 詳細を見る |
|------|--------|
| **Scheme** | `iwool` (ケースインセンティブ) |
| **Routing** | 最初のパスセグメント(ホストまたはパス)は、目的地を選択 |
| **Empty URL** | `iwool://` パスなし → **ホーム** |
| **Unknown paths** | **無視**(ホームへのサイレントフォールバックなし) |
| **Parser** | 「IWoolDeepLink.parse( :)」→「ContentView.applyDeepLink」 |

---

## 1. タブの宛先

| URL | 開く画面 |
|-----|--------|---------|
| `iwool://home` | **Home** tab | — |
| `iwool://calendar` | **Calendar** tab | ログイン |
| `iwool://stats` | **Statistics** tab | `statistics`、`stat` |
| `iwool://settings` | **Settings** tab | `setting`, `preferences` |

---

## 2. アプリ内アクション

これらのルートは、**ホーム画面クイックアクション**とシートまたはサブページを一致します。

| URL | 開く画面 |
|-----|--------|---------|
| `iwool://new` | **Create activity** sheet | `create`、`add`、`new-event`、`newevent` |
| `iwool://island` | **Quick Countdown** (Dynamic Island reminder) sheet | `island-reminder`、`islandreminder`、`countdown`、`quick-countdown`、`quickcountdown` |
| `iwool://reminders` | **Scheduled local reminders** list (Settings) | `scheduled-reminders`、`scheduledreminders`、`scheduled`、`notification-reminders` |
| `iwool://scanner` | **QR / barcode scanner** (Settings → Tools) | `scan`、`qrcode`、`barcode` |
| `iwool://rate` | In-app **App Store rating** prompt | `rating`、`review`、`rate-in-app`、`rateinapp` |
| `iwool://feedback` | **Feedback** email compose | `mail`, `support`, `contact` |

**Nested settings paths** (same action) は、


```
iwool://settings/scanner
iwool://settings/reminders
iwool://settings/rate
iwool://settings/feedback
```


---

## 3. 活動の細部

データベースIDで単一のウールアクティビティを開きます。

| Parameter | Required | コンテンツ |
|-----------|----------|-------------|
| Path `event/{id}` | One of path / query | アクティビティID(陽性整数) |
| Query `id={id}` | One of path / query | パスフォームと同じ |
| Query `day={seconds}` | No | **注意** 活動 — 自然一日の始まりは `timeIntervalSince1970` (その日の深夜) |

**アクティビティを開く 42**


```
iwool://event/42
iwool://event?id=42
```


**特定の日に発生する再発**


```
iwool://event/42?day=189345600
```


再帰シリーズのリンクを作成する場合、iWool は、ホームリスト ( `iwool` ) と同じロジックから ```````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````

---

## 4. ホーム画面クイックアクション(iOS)

iWoolアイコンを長押しする → 4** アクションまで。 カスタマイズします。**設定 → ツール → ホーム画面ショートカット** (9オプション, 再注文するドラッグ, デフォルトにリセット).

| Option | 忍耐 を 生み出 し なさ い . |
|--------|-----|
| Home | シェアハウス |
| Calendar | 「iwool://calendar」 |
| Statistics | `iwool://stats` |
| Quick Countdown | 「iwool://island」は、 |
| New Activity | "iwool" は、 |
| Scheduled Reminders | "iwool://reminders" は、 |
| Scanner | 「iwool://scanner」をダウンロード |
| Rate App | 「iwool://rate」 |
| Feedback | "iwool://feedback" は、 |

**最初のインストール時にデフォルト:** ホーム·カレンダー·統計·クイックカウントダウン。

クイックアクション `iwool://` 文字列は、同じ `iwool` パスと、寒さのスタートで `iwool://` を経由してルートを使用します。

---

## 5. ウィジェットの深いリンク

Widget は同じ `iwool://` URL を使用します。

| Widget | Tap target | 忍耐 を 生み出 し なさ い . |
|--------|------------|-----|
| Today Active / Today All / Today Upcoming / All Events | Home | シェアハウス |
| Stats Overview / Earnings / Top Platforms | Statistics | `iwool://stats` |
| Glance | First event or Home | `iwool://event/{id}` または `iwool://home` |
| Lock Screen accessories | First event or Home | `iwool://event/{id}` または `iwool://home` |
| List row (iOS 17+) | Activity detail | 「iwool://event/{id}`」 |

クイックカウントダウンライブアクティビティは、アプリ内UIのみを使用しています。**別々のURL**は、アプリ外から島のカウントダウンを開始する(作成シートを開くために `iwool://` を使用して)。

---

## Appleのショートカットの例

**オープン統計**


```
iwool://stats
```


**新しいアクティビティを作成する**


```
iwool://new
```


**クイックカウントダウンシートを開く**


```
iwool://island
```


**IDをコピーした後の活動を開く**


```
iwool://event?id=42
```


---

## 起動動作

| Scenario | フローリング |
|----------|------|
| **Widget / Shortcuts `onOpenURL`** | 「AppRouter」 → 「applyDeep」 リンク |
| **Cold start — Quick Action** | 「ショートカットキー」→「PendingShortcutBuffer」→「ショートカットObserver」 |
| **Warm start — Quick Action** | シーンコールバック → 通知 → ショートカットObserver` |
| **Feedback / Rate (cold start)** | ショートディレイなので、メールシート/ストアキットはアクティブウィンドウシーン |
| **Invalid event ID** | 無視されるリンク — アラートなし |

---

## トラブルシューティング

| Issue | 確認する |
|-------|----------------|
| Link opens app but nothing happens | パスはサポートされたルートと一致しなければなりません。未知のパスはホームにリダイレクトされません。 |
| `event` link shows wrong occurrence | 再発活動のために `?day=` を追加 |
| Quick Action does nothing on cold launch | 待ち時間 ~0.4 s または再試行; フィードバック/レートの必要性 UI の台紙の時間 |
| `iwool://island` does not start countdown automatically | *creation シートを開く** — 期間を確認し、アプリ内で [スタート] をタップします。 |
| Quick Countdown requires iOS 16.2+ | イベントのライブ活動はiOS 16.1 +を必要としています。スタンドアローン島カウントダウンは16.2 +を必要とします |

---

[iWoolサポートに戻る](..)・ [FAQ](../faq)・ [プライバシーポリシー](./privacy)

</section>
<section lang="ko" markdown="1">

iWool 지원 ** `iwool://` ** URL 계획 딥 링크 — 탭을 열고, 앱 액션을 시작하거나, Safari, Apple Shortcuts, 위젯 탭 또는 홈 화면 빠른 행동 (앱 아이콘을 길게 누릅니다)에서 특정 활동으로 이동합니다.

> ** 중요 : ** 딥 링크 만 ** iWool 내부 나비 게이트 **. 서버 연결 또는 동기화 데이터를 클라우드로 만들지 않습니다.

## 프로토콜


```
iwool://<path>[?query]
```


| Rule | 제품 정보 |
|------|--------|
| **Scheme** | `iwool` (케이스 민감성) |
| **Routing** | 첫 번째 경로 세그먼트 (호스트 또는 경로) 목적지 선택 |
| **Empty URL** | `iwool://` 경로 없음 → **홈** |
| **Unknown paths** | ** 임신 ** (집에 침묵 낙하 없음) |
| **Parser** | `IWoolDeepLink.parse( :)`→ `ContentView.applyDeepLink`````````````` |

---

## 1. 탭 대상

| URL | 열리는 화면 |
|-----|--------|---------|
| `iwool://home` | **Home** tab | — |
| `iwool://calendar` | **Calendar** tab | '칼' |
| `iwool://stats` | **Statistics** tab | `statistics`, `stat` |
| `iwool://settings` | **Settings** tab | `설정`, `preferences` |

---

## 2. 앱 작업

이 경로 일치 **홈 화면 빠른 행동** 및 열린 시트 또는 하위 페이지:

| URL | 열리는 화면 |
|-----|--------|---------|
| `iwool://new` | **Create activity** sheet | `create`, `add`, `new-event`, `newevent` |
| `iwool://island` | **Quick Countdown** (Dynamic Island reminder) sheet | `island-reminder`, `islandreminder`, `countdown`, `quick-countdown`, `quickcountdown` |
| `iwool://reminders` | **Scheduled local reminders** list (Settings) | `scheduled-reminders`, `scheduledreminders`, `scheduled`, `notification-reminders` |
| `iwool://scanner` | **QR / barcode scanner** (Settings → Tools) | `scan`, `qrcode`, `barcode` |
| `iwool://rate` | In-app **App Store rating** prompt | `rating`, `review`, `rate-in-app`, `rateinapp` |
| `iwool://feedback` | **Feedback** email compose | `mail`, `support`, `contact` |

**제한 설정 경로**(same action):


```
iwool://settings/scanner
iwool://settings/reminders
iwool://settings/rate
iwool://settings/feedback
```


---

## 3. 활동 세부사항

데이터베이스 ID로 단일 울 활동을 엽니 다.

| Parameter | Required | 이름 * |
|-----------|----------|-------------|
| Path `event/{id}` | One of path / query | 활동 ID (긍정 정수) |
| Query `id={id}` | One of path / query | 경로 형태와 동일 |
| Query `day={seconds}` | No | ** 등록 ** 활동 - 자연 일 시작으로 `timeIntervalSince1970` (그런 결과의 밤) |

**영업 42**


```
iwool://event/42
iwool://event?id=42
```


**특정 당일에 발생한 발생 **


```
iwool://event/42?day=189345600
```


recurring 시리즈를 위한 건물 연결 때, iWool는 가정 명부 ( `iwool` )와 동일한 논리에서 derive `iwool://` 할 수 있습니다.

---

## 4. 홈 화면 빠른 행동 (iOS)

iWool 아이콘 → 최대 **4** 작업. 에서 사용자 지정 ** 설정 → 도구 → 홈 화면 단축키 ** (9 옵션, 명령으로 드래그, 기본값으로 재설정).

| Option | 사이트 맵 |
|--------|-----|
| Home | `iwool=홈` |
| Calendar | `iwool://calendar``````` |
| Statistics | `iwool://stats`````` |
| Quick Countdown | `iwool://island````````` |
| New Activity | `iwool://new````````` |
| Scheduled Reminders | `iwool://reminders`````` |
| Scanner | `iwool://scanner```````` |
| Rate App | `iwool://rate```````` |
| Feedback | `iwool://feedback`````` |

**기본 설치:** 집 · 달력 · 통계 · 빠른 카운트 다운.

Quick-action `iwool://` 문자열은 같은 사용 `iwool` 경로와 경로를 통해 `iwool://` → `IWoolDeepLink.parse(_:)` 감기 시작.

---

## 5. 위젯 딥 링크

위젯 탭은 같은 사용 `iwool://` URL:

| Widget | Tap target | 사이트 맵 |
|--------|------------|-----|
| Today Active / Today All / Today Upcoming / All Events | Home | `iwool=홈` |
| Stats Overview / Earnings / Top Platforms | Statistics | `iwool://stats`````` |
| Glance | First event or Home | `iwool://event/{id}` 또는 `iwool://home` |
| Lock Screen accessories | First event or Home | `iwool://event/{id}` 또는 `iwool://home` |
| List row (iOS 17+) | Activity detail | `iwool://event/{id}````` |

Quick Countdown Live Activities use in-app UI only — ** 별도의 URL** 앱 외부에서 섬 카운트 다운을 시작합니다 (use `iwool://` 생성 시트를 열려면).

---

## Apple Shortcuts 예제

** 통계 숨기기 **


```
iwool://stats
```


**새로운 활동을 등록 **


```
iwool://new
```


** Quick Countdown 시트 열기 **


```
iwool://island
```


** ID 복사 후 활동 열기 **


```
iwool://event?id=42
```


---

## 시작 동작

| Scenario | 제품정보 |
|----------|------|
| **Widget / Shortcuts `onOpenURL`** | `AppRouter` → `applyDeep 링크` |
| **Cold start — Quick Action** | `ShortcutSceneDelegate` → `PendingShortcutBuffer` → `ShortcutObserver` |
| **Warm start — Quick Action** | 장면 콜백 → 알림 → `ShortcutObserver` |
| **Feedback / Rate (cold start)** | 짧은 지연 그래서 메일 시트 / StoreKit는 활성 창 장면 |
| **Invalid event ID** | 링크 무시 — 알림 없음 |

---

## 문제 해결

| Issue | 자주 묻는 질문 |
|-------|----------------|
| Link opens app but nothing happens | 경로는 지원된 경로에 일치해야합니다; 알 수없는 경로는 홈으로 리디렉션되지 않습니다 |
| `event` link shows wrong occurrence | recurring 활동을 위한 `?day=` 추가 |
| Quick Action does nothing on cold launch | ~0.4 s 또는 retry를 대기하십시오; 의견/rate 필요 UI 산 시간 |
| `iwool://island` does not start countdown automatically | **creation sheet**를 엽니다. - 앱 내에서 지속적이고 탭 시작을 확인합니다. |
| Quick Countdown requires iOS 16.2+ | 이벤트 라이브 활동 필요 iOS 16.1+; 독립 섬 카운트 다운 필요 16.2+ |

---

[Back to iWool Support](..) · [FAQ](../faq) · [개인정보 보호정책](../privacy)

</section>
<section lang="ru" markdown="1">

iWool поддерживает ** `iwool://` ** Схема URL глубоких ссылок - откройте вкладку, начните действие в приложении или перейдите к определенной деятельности из Safari, ярлыков Apple, нажатия виджета или быстрого действия на домашнем экране (нажмите значок приложения).

> ** Важно:** Глубокие ссылки ** перемещаются внутри iWool**. Они не создают подключения к серверу и не синхронизируют данные с облаком.

## Спецификация протокола


```
iwool://<path>[?query]
```


| Rule | Подробнее |
|------|--------|
| **Scheme** | "iwool" (случайно нечувствительный) |
| **Routing** | Первый сегмент пути (хозяин или путь) выбирает пункт назначения. |
| **Empty URL** | «Iwool://» (без дорожки) |
| **Unknown paths** | **Игнорированный** (без молчаливого возвращения домой) |
| **Parser** | «IWoolDeepLink.parse( :)» → «ContentView.applyDeepLink» |

---

## 1. Пункты назначения вкладок

| URL | Открывает |
|-----|--------|---------|
| `iwool://home` | **Home** tab | — |
| `iwool://calendar` | **Calendar** tab | "каль" |
| `iwool://stats` | **Statistics** tab | "статистика", "статистика" |
| `iwool://settings` | **Settings** tab | "установка", "предпочтения" |

---

## 2. Действия в приложении

Эти маршруты соответствуют **Home Screen Quick Actions** и открытым листам или подстраницам:

| URL | Открывает |
|-----|--------|---------|
| `iwool://new` | **Create activity** sheet | «создать», «добавить», «новое событие», «новое событие» |
| `iwool://island` | **Quick Countdown** (Dynamic Island reminder) sheet | "остров-напоминание", "остров-напоминание", "отсчет", "быстрый отсчет", "быстрый отсчет" |
| `iwool://reminders` | **Scheduled local reminders** list (Settings) | "плановые напоминания", "плановые напоминания", "плановые напоминания" |
| `iwool://scanner` | **QR / barcode scanner** (Settings → Tools) | «scan», «qrcode», «barcode» |
| `iwool://rate` | In-app **App Store rating** prompt | «рейтинг», «обзор», «rate-in-app», «rateinapp» |
| `iwool://feedback` | **Feedback** email compose | "почта", "поддержка", "контакт" |

** Настроенные пути настроек** (те же действия):


```
iwool://settings/scanner
iwool://settings/reminders
iwool://settings/rate
iwool://settings/feedback
```


---

## 3. Детали деятельности

Откройте одну шерстяную активность по идентификатору базы данных.

| Parameter | Required | Описание |
|-----------|----------|-------------|
| Path `event/{id}` | One of path / query | Идентификатор активности (положительное целое число) |
| Query `id={id}` | One of path / query | Как и форма пути |
| Query `day={seconds}` | No | Для ** повторяющихся** действий — естественный день начинается как «timeIntervalSince1970» |

** Открытая деятельность 42**


```
iwool://event/42
iwool://event?id=42
```


** Повторяющиеся события в определенный день**


```
iwool://event/42?day=189345600
```


При создании ссылок для повторяющихся серий iWool может вывести `iwool://` из той же логики, что и домашний список ( `iwool` ).

---

## 4. Быстрые действия (iOS)

Длительное нажатие иконки iWool → до **4** действий. Настройка в **Настройки → Инструменты → Ярлыки домашнего экрана** (9 опций, перетащите на переупорядочение, сбросьте на по умолчанию).

| Option | URL |
|--------|-----|
| Home | "iwool://home" |
| Calendar | "iwool://calendar" |
| Statistics | "iwool://stats" |
| Quick Countdown | "iwool://island" |
| New Activity | "iwool://new" |
| Scheduled Reminders | "iwool://reminders" |
| Scanner | "iwool://scanner" |
| Rate App | "iwool://rate" |
| Feedback | "iwool://feedback" |

** Дефолт при первой установке: ** Домой · Календарь · Статистика · Быстрый обратный отсчет.

Струны быстрого действия `iwool://` используют те же пути `iwool` и маршрут через `iwool://` → `IWoolDeepLink.parse(_:)` на холодном старте.

---

## 5. Виджеты глубоких связей

Виджеты используют те же `iwool://` URL:

| Widget | Tap target | URL |
|--------|------------|-----|
| Today Active / Today All / Today Upcoming / All Events | Home | "iwool://home" |
| Stats Overview / Earnings / Top Platforms | Statistics | "iwool://stats" |
| Glance | First event or Home | "iwool://event/{id}" или "iwool://home" |
| Lock Screen accessories | First event or Home | "iwool://event/{id}" или "iwool://home" |
| List row (iOS 17+) | Activity detail | "iwool://event/{id}" |

Quick Countdown Live Activities использует только пользовательский интерфейс в приложении — ** нет отдельного URL**, чтобы начать обратный отсчет острова из-за пределов приложения (используйте `iwool://` , чтобы открыть лист создания).

---

## Примеры Apple Shortcuts

** Открытая статистика**


```
iwool://stats
```


**Создать новый проект**


```
iwool://new
```


** Быстрый обратный отсчет **


```
iwool://island
```


** Открытая деятельность после копирования ID**


```
iwool://event?id=42
```


---

## Запускное поведение

| Scenario | Поток |
|----------|------|
| **Widget / Shortcuts `onOpenURL`** | «AppRouter» — «applyDeep» Ссылка |
| **Cold start — Quick Action** | «ShortcutSceneDelegate» → «PendingShortcutBuffer» → «ShortcutObserver» |
| **Warm start — Quick Action** | Обратный вызов сцены → уведомление → «ShortcutObserver» |
| **Feedback / Rate (cold start)** | Короткая задержка, поэтому почтовый лист / StoreKit имеет активную сцену окна |
| **Invalid event ID** | Ссылка проигнорирована — нет предупреждения |

---

## устранение неполадок

| Issue | Что проверить |
|-------|----------------|
| Link opens app but nothing happens | Путь должен соответствовать поддерживаемому маршруту; неизвестные пути не перенаправлены на Домой |
| `event` link shows wrong occurrence | Добавить «?day=» для повторяющихся действий |
| Quick Action does nothing on cold launch | Подождите ~0,4 с или повторите; обратная связь / скорость требует времени установки пользовательского интерфейса |
| `iwool://island` does not start countdown automatically | Открывает **креационный лист ** — подтверждает продолжительность и нажимает Старт внутри приложения |
| Quick Countdown requires iOS 16.2+ | Event Live Activities требуется iOS 16.1+; автономный отсчет времени на острове требует 16.2+ |

---

[Назад в поддержку iWool] (..) · [FAQ] (../faq) · [Политика конфиденциальности] (../privacy)

</section>
<section lang="th" markdown="1">

ivol รองรับ~ `iwool://` BAR ~ ที่อยู่ URL กําหนดที่อยู่เชื่อมโยงแบบลึก — เปิดแท็บ, เริ่มการเรียกใช้งานโปรแกรมในการใช้งาน, หรือกระโดดไปยังกิจกรรมเฉพาะจากซาฟารี, ปุ่มพิมพ์ลัดของแอปเปิล, แท็บวิดเจ็ต, หรือการกระทําด่วนของหน้าจอส่วนตัว (ยาว- กดไอคอนโปรแกรม)

> ~! ~ เชื่อมโยงลึกเท่านั้น... .... พวกเขาไม่ได้สร้างการเชื่อมต่อของแม่ข่ายหรือปรับเทียบข้อมูลกับข้อมูลบนก้อนเมฆ

## การกําหนดโพรโทคอล


```
iwool://<path>[?query]
```


| Rule | รายละเอียด |
|------|--------|
| **Scheme** | 'Oiวูล' (ตัวอ่อน) |
| **Routing** | พาธในช่วงแรก (เครื่องหรือพาธ) เลือกปลายทาง |
| **Empty URL** | ~ไม่มีเส้นทาง~ |
| **Unknown paths** | ~ถูกเปิดโปง~ |
| **Parser** | 'I Woodl Deeplink.parse(:):'''OfftitleView. apply Deeplink' |

---

## 1. ปลายทางแท็บ

| URL | เปิด |
|-----|--------|---------|
| `iwool://home` | **Home** tab | — |
| `iwool://calendar` | **Calendar** tab | 'Cal' |
| `iwool://stats` | **Statistics** tab | อัลกอริอะฮ์ |
| `iwool://settings` | **Settings** tab | (จะมีคําบัญชาแก่มะลาอิกะฮฺว่า) จงนําเขาไป |

---

## 2. การกระทําในการเรียกใช้

เส้นทางเหล่านี้ตรงกัน ~Home screen securication ~ และเปิดแผ่นหรือหน้าย่อย:

| URL | เปิด |
|-----|--------|---------|
| `iwool://new` | **Create activity** sheet | จงสร้าง, จง, จง, จง, จง, จง... |
| `iwool://island` | **Quick Countdown** (Dynamic Island reminder) sheet | ISland-reminder', islandreminder', searchdown', queck-countdown ', queckclown' |
| `iwool://reminders` | **Scheduled local reminders** list (Settings) | 'reculted-reminders', "'recreduledminds',"','ประกาศประกาศ' |
| `iwool://scanner` | **QR / barcode scanner** (Settings → Tools) | 'Scan', 'Crcode', 'บาร์โค้ด' |
| `iwool://rate` | In-app **App Store rating** prompt | จงประกาศอย่างเปิดเผย |
| `iwool://feedback` | **Feedback** email compose | 'อีเมล' "ช่วยเหลือ' |

** พาธการตั้งค่าที่ฝังอยู่ **


```
iwool://settings/scanner
iwool://settings/reminders
iwool://settings/rate
iwool://settings/feedback
```


---

## 3. รายละเอียดกิจกรรม

เปิดกิจกรรมขนสัตว์เพียงตัวเดียวโดยใช้หมายเลขฐานข้อมูล

| Parameter | Required | คําอธิบาย |
|-----------|----------|-------------|
| Path `event/{id}` | One of path / query | หมายเลขประจํากิจกรรม (จํานวนเต็มบวก) |
| Query `id={id}` | One of path / query | เหมือนกับรูปแบบพาธ |
| Query `day={seconds}` | No | 2551 สําหรับกิจกรรมที่ตามมานี้ -- การเริ่มต้นของวันตามธรรมชาติคือ 'Timetervalue ตั้งแต่ปี ค.ศ. |

** เปิดกิจกรรม 42*


```
iwool://event/42
iwool://event?id=42
```


~ เกิดขึ้นอีกในวันพิเศษ~


```
iwool://event/42?day=189345600
```


เมื่อสร้างลิงก์สําหรับอนุกรมซ้ํา, ivol สามารถหา `iwool://` จากตรรกะเดียวกับรายการที่บ้าน ( `iwool` )

---

## 4. การกระทําด่วนของหน้าจอส่วนตัว (ไอOS)

กดยาวไอคอน ivill ถึง 4 การกระทํา ปรับค่าเองใน ~ ตั้งค่าเครื่องมือ ○ จอภาพส่วนตัว ~ (9 ตัวเลือก, ลากเพื่อทําการเรียงใหม่, ตั้งใหม่เป็นค่าปริยาย)

| Option | ที่อยู่ URL |
|--------|-----|
| Home | บ้าน |
| Calendar | ~โอ้~ |
| Statistics | ~โอ้วววว~ |
| Quick Countdown | ~~~~~~~ ~โอ~ |
| New Activity | ~โอ้~ |
| Scheduled Reminders | 'Oivolreminders' |
| Scanner | ~ฮู้วววว~ |
| Rate App | ~โอ้~ |
| Feedback | 'เอาอาหารกลับมา' |

~Deflobal on the first ติดตั้ง: ~ปฏิทิน Home althythys atsized ethody lognown.

ทําเร็ว `iwool://` สตริง ใช้  c1 th thath thath ath ath ath พาธและเส้นทางผ่าน  c2  p       /C3   th on cold start.

---

## 5. วิดเจ็ตลิงก์ลึก

เสียงเคาะของวิดเจ็ตใช้ที่อยู่ URL แบบเดียวกัน `iwool://` BAR :

| Widget | Tap target | ที่อยู่ URL |
|--------|------------|-----|
| Today Active / Today All / Today Upcoming / All Events | Home | บ้าน |
| Stats Overview / Earnings / Top Platforms | Statistics | ~โอ้วววว~ |
| Glance | First event or Home | 'Offict=////////////////////////////////////ค่ะ |
| Lock Screen accessories | First event or Home | 'Offict=////////////////////////////////////ค่ะ |
| List row (iOS 17+) | Activity detail | ~ |

Office Tountown Life ใช้เฉพาะที่อยู่ URL แบบย่อเท่านั้น -- ~ ไม่แยกที่อยู่ URL * เพื่อเริ่มการนับถอยหลังของเกาะจากด้านนอกโปรแกรม (ใช้  c0     เพื่อเปิดแผ่นการสร้าง)

---

## ตัวอย่างปุ่มพิมพ์ลัดของแอปเปิล

~สถิติเปิด! ~


```
iwool://stats
```


~ จงสร้างกิจกรรมใหม่~


```
iwool://new
```


~ เปิดแผ่นงานด่วน~


```
iwool://island
```


** เปิดกิจกรรม หลังจากคัดลอกหมายเลข **


```
iwool://event?id=42
```


---

## เรียกใช้พฤติกรรม

| Scenario | ลื่นไถล |
|----------|------|
| **Widget / Shortcuts `onOpenURL`** | 'AppRouter' →'Apply Deep เชื่อมโยง |
| **Cold start — Quick Action** | 'SepteneDeledge' ''''''''hending Proughs Broffer' ~'helpter' |
| **Warm start — Quick Action** | ฉากเรียกกลับ → สืบค้นเมื่อ 'OHE' |
| **Feedback / Rate (cold start)** | หน่วงเวลาสั้นดังนั้นตารางจดหมาย / ร้านค้า kit มีหน้าต่างที่ทํางานอยู่ |
| **Invalid event ID** | ลิ้งค์ ถูก ละเลย — ไม่ มี การ ตื่น ตัว |

---

## การยิงปัญหา

| Issue | จะตรวจอะไร |
|-------|----------------|
| Link opens app but nothing happens | พาธต้องตรงกับเส้นทางที่รองรับ; พาธที่ไม่รู้จักไม่ได้หันไปบ้าน |
| `event` link shows wrong occurrence | เพิ่ม '%? วัน=' สําหรับกิจกรรมที่เกิดขึ้นซ้ํา |
| Quick Action does nothing on cold launch | รอ ~0. 4 s หรือลองใหม่; การแจ้งข้อมูล/ peri ต้องการเวลาแบบ UI |
| `iwool://island` does not start countdown automatically | เปิดแผ่นอาหาร -- ยืนยันระยะเวลาและการเคาะเริ่มต้นภายในแอพ |
| Quick Countdown requires iOS 16.2+ | Event Life Office ต้องการ OS 16.1+; การนับถอยหลังของเกาะเดี่ยวต้องการ 16.2+ |

---

[การรองรับ iWoll] [. ] [FAQ] (./faq) สืบค้นเมื่อ 27 พฤษภาคม พ.ศ.

</section>
<section lang="de" markdown="1">

iWool unterstützt ** `iwool://` ** URL-Schema Deep Links - Öffnen Sie einen Tab, starten Sie eine In-App-Aktion oder springen Sie zu einer bestimmten Aktivität von Safari, Apple Shortcuts, einem Widget-Tipp oder einer Home Screen Quick Action (langes Drücken des App-Symbols).

> **Wichtig:** Nur tiefe Links **navigieren innerhalb von iWool**. Sie erstellen keine Serververbindungen oder synchronisieren Daten mit der Cloud.

## Protokollspezifikation


```
iwool://<path>[?query]
```


| Rule | Einzelheiten |
|------|--------|
| **Scheme** | "iwool" (fallunempfindlich) |
| **Routing** | Erstes Pfadsegment (Host oder Pfad) wählt das Ziel aus |
| **Empty URL** | "iwool://" ohne Pfad → **Home |
| **Unknown paths** | **Ignoriert** (kein stiller Fallback nach Hause) |
| **Parser** | `IWoolDeepLink.parse( :)` → `ContentView.applyDeepLink` |

---

## 1. Tab Destinationen

| URL | Öffnet |
|-----|--------|---------|
| `iwool://home` | **Home** tab | — |
| `iwool://calendar` | **Calendar** tab | „cal |
| `iwool://stats` | **Statistics** tab | "Statistik", "Statistik" |
| `iwool://settings` | **Settings** tab | "Setting", "Präferenzen" |

---

## 2. In-App-Maßnahmen

Diese Routen passen zu **Home Screen Quick Actions ** und öffnen Blätter oder Unterseiten:

| URL | Öffnet |
|-----|--------|---------|
| `iwool://new` | **Create activity** sheet | `create`, `add`, `new-event`, `newevent` |
| `iwool://island` | **Quick Countdown** (Dynamic Island reminder) sheet | "Island-Reminder", "Islandreminder", "Countdown", "Quick-Countdown", "QuickCountdown" |
| `iwool://reminders` | **Scheduled local reminders** list (Settings) | "Scheduled-Reminders", "Scheduled-Reminders", "Notification-Reminders" |
| `iwool://scanner` | **QR / barcode scanner** (Settings → Tools) | `scan`, `qrcode`, `barcode` |
| `iwool://rate` | In-app **App Store rating** prompt | `rating`, `review`, `rate-in-app`, `rateinapp` |
| `iwool://feedback` | **Feedback** email compose | `mail`, `support`, `contact` |

**Nested settings paths** (gleiche Aktionen):


```
iwool://settings/scanner
iwool://settings/reminders
iwool://settings/rate
iwool://settings/feedback
```


---

## 3. Angaben Tätigkeit

Öffnen Sie eine einzelne Wollaktivität nach Datenbank-ID.

| Parameter | Required | Beschreibung |
|-----------|----------|-------------|
| Path `event/{id}` | One of path / query | Aktivitätskennung (positive ganze Zahl) |
| Query `id={id}` | One of path / query | Gleiches wie Pfadform |
| Query `day={seconds}` | No | Für **wiederkehrende ** Aktivitäten - natürlicher Tagesbeginn als "timeIntervalSince1970" (Mitternacht dieses Ereignisses) |

**Offene Aktivität 42**


```
iwool://event/42
iwool://event?id=42
```


**Wiederholtes Ereignis an einem bestimmten Tag**


```
iwool://event/42?day=189345600
```


Beim Erstellen von Links für wiederkehrende Serien kann iWool `iwool://` aus derselben Logik wie die Heimatliste ( `iwool` ) ableiten.

---

## 4. Home Screen Quick Actions (iOS)

Langes Drücken des iWool-Symbols → bis zu **4** Aktionen. Anpassen in **Einstellungen → Tools → Home Screen Shortcuts** (9 Optionen, Drag to Reorder, Zurücksetzen auf Standard).

| Option | URL |
|--------|-----|
| Home | „iwool://home |
| Calendar | „iwool://calendar |
| Statistics | „iwool://stats |
| Quick Countdown | „iwool://island |
| New Activity | „iwool://new |
| Scheduled Reminders | „iwool://reminders |
| Scanner | „iwool://scanner |
| Rate App | „iwool://rate |
| Feedback | „iwool://feedback |

**Standard bei der ersten Installation:** Home · Kalender · Statistiken · Quick Countdown.

Quick-action `iwool://` Strings verwenden die gleichen `iwool` Pfade und Route durch `iwool://` → `IWoolDeepLink.parse(_:)` beim Kaltstart.

---

## 5. Widget Deep Links

Widget Taps verwenden die gleichen `iwool://` URLs:

| Widget | Tap target | URL |
|--------|------------|-----|
| Today Active / Today All / Today Upcoming / All Events | Home | „iwool://home |
| Stats Overview / Earnings / Top Platforms | Statistics | „iwool://stats |
| Glance | First event or Home | `iwool://event/{id}` oder `iwool://home` |
| Lock Screen accessories | First event or Home | `iwool://event/{id}` oder `iwool://home` |
| List row (iOS 17+) | Activity detail | „iwool://event/{id} |

Quick Countdown Live-Aktivitäten verwenden nur die In-App-Benutzeroberfläche - **keine separate URL **, um einen Insel-Countdown von außerhalb der App zu starten (verwenden Sie `iwool://` , um das Erstellungsblatt zu öffnen).

---

## Apple Shortcuts Beispiele

**Offene Statistiken**


```
iwool://stats
```


**Erstelle eine neue Aktivität**


```
iwool://new
```


** Schnelles Countdownblatt öffnen**


```
iwool://island
```


**Offene Aktivität nach Kopieren der ID**


```
iwool://event?id=42
```


---

## Startverhalten

| Scenario | Durchfluss |
|----------|------|
| **Widget / Shortcuts `onOpenURL`** | AppRouter → ApplyDeep Link |
| **Cold start — Quick Action** | ‘ShortcutSceneDelegate’ → ‘PendingShortcutBuffer’ → ‘ShortcutObserver’ |
| **Warm start — Quick Action** | Scene Callback → Benachrichtigung → `ShortcutObserver` |
| **Feedback / Rate (cold start)** | Kurze Verzögerung so Mailsheet / StoreKit hat eine aktive Fensterszene |
| **Invalid event ID** | Link ignoriert – keine Warnung |

---

## Fehlerbehebung

| Issue | Was zu überprüfen ist |
|-------|----------------|
| Link opens app but nothing happens | Pfad muss mit einer unterstützten Route übereinstimmen; unbekannte Pfade werden nicht nach Hause umgeleitet |
| `event` link shows wrong occurrence | Hinzufügen von `?day=` für wiederkehrende Aktivitäten |
| Quick Action does nothing on cold launch | Warten Sie ~ 0,4 s oder wiederholen Sie; Feedback / Rate benötigen UI-Montagezeit |
| `iwool://island` does not start countdown automatically | Öffnet das **Erstellungsblatt** – Dauer bestätigen und auf Start innerhalb der App tippen |
| Quick Countdown requires iOS 16.2+ | Event Live-Aktivitäten benötigen iOS 16.1+; Standalone-Insel-Countdown benötigt 16.2+ |

---

[Zurück zu iWool Support](..) · [FAQ](../faq) · [Privacy Policy](../privacy]

</section>
<section lang="fr" markdown="1">

iWool prend en charge ** `iwool://` ** Des liens profonds du schéma d'URL – ouvrez un onglet, lancez une action dans l'application, ou sautez à une activité spécifique de Safari, de raccourcis Apple, d'un widget ou d'une action rapide d'écran d'accueil (cliquez sur l'icône de l'application).

> **Important:** Liens profonds seulement **naviggate à l'intérieur iWool**. Ils ne créent pas de connexions de serveur ni ne synchronisent les données vers le cloud.

## Spécification du protocole


```
iwool://<path>[?query]
```


| Rule | Détail |
|------|--------|
| **Scheme** | "iwool" (insensible au cas par cas) |
| **Routing** | Le premier segment de chemin (hôte ou chemin) sélectionne la destination |
| **Empty URL** | `iwool://` sans chemin → **Accueil** |
| **Unknown paths** | **Ignoré** (pas de retour silencieux à la maison) |
| **Parser** | `IWoolDeepLink.parse( :)` → `ContentView.applyDeepLink` |

---

## 1. Destinations des onglets

| URL | Ouvre |
|-----|--------|---------|
| `iwool://home` | **Home** tab | — |
| `iwool://calendar` | **Calendar** tab | «cal» |
| `iwool://stats` | **Statistics** tab | «statistique», «stat» |
| `iwool://settings` | **Settings** tab | `réglage`, `préférences` |

---

## 2. Actions en cours

Ces itinéraires correspondent à **Actions rapides de l'écran d'accueil** et feuilles ou sous-pages ouvertes:

| URL | Ouvre |
|-----|--------|---------|
| `iwool://new` | **Create activity** sheet | `create`, `add`, `new-event`, `new-event` |
| `iwool://island` | **Quick Countdown** (Dynamic Island reminder) sheet | < < Island-Reminer > > , < < Island-Reminer > > , < < Compte à rebours > > , < < Compte à rebours > > , < < Compte à rebours > > |
| `iwool://reminders` | **Scheduled local reminders** list (Settings) | `reminders programmés`, `reminders programmés`, `reminders programmés`, `reminders de notification` |
| `iwool://scanner` | **QR / barcode scanner** (Settings → Tools) | `scan`, `qrcode`, `barcode` |
| `iwool://rate` | In-app **App Store rating** prompt | « rating », « review », «rate-in-app », «rateinapp » |
| `iwool://feedback` | **Feedback** email compose | `mail`, `support`, `contact` |

**Les chemins de paramètres nestés** (même actions):


```
iwool://settings/scanner
iwool://settings/reminders
iwool://settings/rate
iwool://settings/feedback
```


---

## 3. Détail des activités

Ouvrez une seule activité de laine par ID de base de données.

| Parameter | Required | Désignation des marchandises |
|-----------|----------|-------------|
| Path `event/{id}` | One of path / query | Identification de l'activité (entier positif) |
| Query `id={id}` | One of path / query | Comme le chemin |
| Query `day={seconds}` | No | Pour **activités récurrentes** - début de la journée naturelle comme «tempsIntervalDepuis1970» (la nuit du même jour) |

**Ouverture de l'activité 42**


```
iwool://event/42
iwool://event?id=42
```


**Événement récurrent à un jour donné**


```
iwool://event/42?day=189345600
```


Lors de la construction de liens pour les séries récurrentes, iWool peut dériver `iwool://` de la même logique que la liste d'origine ( `iwool` ).

---

## 4. Actions rapides de l'écran d'accueil (iOS)

Appuyez longuement sur l'icône iWool → jusqu'à **4** actions. Personnaliser dans **Paramètres → Outils → Raccourcis d'écran d'accueil** (9 options, glisser pour réorganiser, réinitialiser aux valeurs par défaut).

| Option | URL |
|--------|-----|
| Home | "iwool://home" |
| Calendar | "iwool://calendar" |
| Statistics | 'iwool://stats' |
| Quick Countdown | 'iwool://island' |
| New Activity | "iwool://new" |
| Scheduled Reminders | 'iwool://reminders' |
| Scanner | 'iwool://scanner' |
| Rate App | "iwool://rate" |
| Feedback | "iwool://feedback" |

**Défaut lors de la première installation :** Accueil · Calendrier · Statistiques · Compte à rebours rapide.

Action rapide `iwool://` ---

## 5. Widget liens profonds

Les touches Widget utilisent les mêmes URLs :

| Widget | Tap target | URL |
|--------|------------|-----|
| Today Active / Today All / Today Upcoming / All Events | Home | "iwool://home" |
| Stats Overview / Earnings / Top Platforms | Statistics | 'iwool://stats' |
| Glance | First event or Home | "iwool://event/{id}" ou "iwool://home" |
| Lock Screen accessories | First event or Home | "iwool://event/{id}" ou "iwool://home" |
| List row (iOS 17+) | Activity detail | `iwool://event/{id}` |

Quick Countdown Live Activities utilise l'interface utilisateur dans l'application uniquement — **pas d'URL séparée** pour lancer un compte à rebours à partir de l'extérieur de l'application (utilisez `iwool://` pour ouvrir la feuille de création).

---

## Exemples de raccourcis pour Apple

** Statistiques ouvertes**


```
iwool://stats
```


**Créer une nouvelle activité**


```
iwool://new
```


**Ouvrir la feuille de compte à rebours**


```
iwool://island
```


**Ouvrir l'activité après avoir copié l'ID**


```
iwool://event?id=42
```


---

## Comportement de lancement

| Scenario | Débit |
|----------|------|
| **Widget / Shortcuts `onOpenURL`** | `AppRouter` → `applyDeep Lien |
| **Cold start — Quick Action** | `SceneSceneDelegate` → `PendingShortcutBuffer` → `ScetcutObserver` |
| **Warm start — Quick Action** | Callback de scène → notification → `ShortcutObserver` |
| **Feedback / Rate (cold start)** | Court délai donc la feuille mail / StoreKit a une scène de fenêtre active |
| **Invalid event ID** | Lien ignoré — pas d'alerte |

---

## Dépannage

| Issue | Quoi vérifier |
|-------|----------------|
| Link opens app but nothing happens | Path doit correspondre à une route supportée; les chemins inconnus ne sont pas redirigés vers Home |
| `event` link shows wrong occurrence | Ajouter `?day=` pour les activités récurrentes |
| Quick Action does nothing on cold launch | Attendez ~0.4 s ou réessayez; Feedback/taux besoin temps de montage de l'interface utilisateur |
| `iwool://island` does not start countdown automatically | Ouvre la feuille de création **** — confirmer la durée et appuyez sur Démarrer dans l'application |
| Quick Countdown requires iOS 16.2+ | Les activités de l'événement en direct ont besoin d'iOS 16.1+; compte à rebours île autonome a besoin de 16.2+ |

---

[Retour à iWool Support](..) · [FAQ](../faq) · [Politique de confidentialité](../privacy)

</section>
<section lang="tr" markdown="1">

iWool, ** `iwool://` ** URL planı derin bağlantıları - bir sekme açın, bir in-app eylemine başlayın veya Safari'den belirli bir aktiviteye atlamak, Apple Shortcuts, bir widget dokunuşu veya bir Ev Ekran Hızlı Eylem (Uygulama ikonunu baskılayın).

> **İmportant:** Derin bağlantılar sadece ** içinde iWool**. Buluta sunucu bağlantıları veya senkronize verileri yaratmazlar.

## Protokol Doğrulaması


```
iwool://<path>[?query]
```


| Rule | Detaylı Bilgi |
|------|--------|
| **Scheme** | "iwool" (case-in sensitive) |
| **Routing** | İlk yol segmenti (hayal veya yol) varış noktasını seçer |
| **Empty URL** | “iwool https://’ with no road → **Home** |
| **Unknown paths** | **Ignored** (Evde sessiz bir düşüş yok) |
| **Parser** | "IWool DeepLink.parse( :)" → "ContentView.apply DeepLink" |

---

## 1. Tab destinasyonları

| URL | Açar |
|-----|--------|---------|
| `iwool://home` | **Home** tab | — |
| `iwool://calendar` | **Calendar** tab | "cal" |
| `iwool://stats` | **Statistics** tab | "statistikler", "stat" |
| `iwool://settings` | **Settings** tab | "Hayır", "preferences" |

---

## 2.In-app actions

Bu rotalar maç **Home Quick Actions ** ve açık çarşaflar veya alt sayfalar:

| URL | Açar |
|-----|--------|---------|
| `iwool://new` | **Create activity** sheet | "create", "add", "newevent", "newevent" |
| `iwool://island` | **Quick Countdown** (Dynamic Island reminder) sheet | “Köpücü”, “Kırdar”, “saygınlık”, “hakkınlık”, “hakkın” |
| `iwool://reminders` | **Scheduled local reminders** list (Settings) | “Kömürgeciler”, “sömürgeciler”, “dövülsüzler”, “göçücüler” |
| `iwool://scanner` | **QR / barcode scanner** (Settings → Tools) | "Scan", "qrcode", "barcode" |
| `iwool://rate` | In-app **App Store rating** prompt | "Şeytan", "düşün", " |
| `iwool://feedback` | **Feedback** email compose | "mail", "support", "Contact" |

**Nested ayarları yolları** (same eylemleri):


```
iwool://settings/scanner
iwool://settings/reminders
iwool://settings/rate
iwool://settings/feedback
```


---

## 3. Aktivite detayı

Veritabanı ID tarafından tek bir yün aktivite açın.

| Parameter | Required | Açıklama |
|-----------|----------|-------------|
| Path `event/{id}` | One of path / query | Faaliyet ID (pozitif tamsayı) |
| Query `id={id}` | One of path / query | Aynı şekilde yol formu |
| Query `day={seconds}` | No | **recurring ** aktiviteler – doğal gün 1970'ten beri “timeInterval” olarak başlıyor (bu olayın gecesi). |

**Açık aktivite 42**


```
iwool://event/42
iwool://event?id=42
```


** Belirli bir günde meydana gelen olaylar**


```
iwool://event/42?day=189345600
```


Tekrarlanan seriler için bina bağlantıları inşa ederken, iWool, ev listesi ( `iwool` ) ile aynı mantıktan `iwool://` elde edebilir.

---

## 4. Ev Ekran Hızlı Eylemler (iOS)

IWool i →'a kadar, **4** eylemleri. **Aptallar → Tools → Ev Ekran Kısakesler** (9 seçenek, yeniden sipariş etmeye sürüklenmek, varsayılanlere sıfırlamak).

| Option | URL URL URL URL |
|--------|-----|
| Home | "iwool httphome" |
| Calendar | "iwool httpcalendar" |
| Statistics | "iwool httpstats" |
| Quick Countdown | "iwool httpisland" |
| New Activity | "iwool httpnew" |
| Scheduled Reminders | "iwool httpreminders" |
| Scanner | "iwool httpscanner" |
| Rate App | "iwool httprate" |
| Feedback | "iwool httpfeedback" |

**İlk yüklemedeDefault:** Home · Takvim · İstatistikler · Hızlı Kontdown.

Quick-action `iwool://` stringler aynı `iwool` yolları ve rota aracılığıyla `iwool://` → `IWoolDeepLink.parse(_:)` soğuk başlangıç.

---

## 5. Widget derin bağlantılar

Widget musluklar aynı `iwool://` URL'leri kullanır:

| Widget | Tap target | URL URL URL URL |
|--------|------------|-----|
| Today Active / Today All / Today Upcoming / All Events | Home | "iwool httphome" |
| Stats Overview / Earnings / Top Platforms | Statistics | "iwool httpstats" |
| Glance | First event or Home | "iwool httpevent/{id}" veya "iwool: |
| Lock Screen accessories | First event or Home | "iwool httpevent/{id}" veya "iwool: |
| List row (iOS 17+) | Activity detail | “iwool https://event/{id} |

Hızlı Kontdown Canlı Etkinlikler sadece uygulama arayüzünde kullanılır - ** farklı URL ** uygulamanın dışında bir ada sayımı başlatmak için (foto `iwool://` 'i oluşturma sayfası açmak için).

---

## Apple Shortcuts örnekler

**Açık İstatistikler**


```
iwool://stats
```


**Yeni bir aktivite oluşturun**


```
iwool://new
```


**Open Quick Countdown sayfası**


```
iwool://island
```


** ID'yi kopyalamaktan sonra açık aktivite**


```
iwool://event?id=42
```


---

## Başlangıç davranışı

| Scenario | Akış Akış |
|----------|------|
| **Widget / Shortcuts `onOpenURL`** | "AppRouter" → "Uygulamalı Link' |
| **Cold start — Quick Action** | "ShortcutSceneDelegate" → "PendingShortcutBuffer" → "ShortcutObserver" |
| **Warm start — Quick Action** | Sahne geri dönüş → “ShortcutObserver’ |
| **Feedback / Rate (cold start)** | Kısa gecikme o posta sayfası / MağazaKit aktif bir pencere sahnesine sahiptir |
| **Invalid event ID** | Link görmezden gelin - hiçbir uyarı |

---

## Sorun Giderme

| Issue | Ne kontrol edecek |
|-------|----------------|
| Link opens app but nothing happens | Yol desteklenen bir rotayla eşleşmeli; bilinmeyen yollar Home'a yönlendirilmiyor |
| `event` link shows wrong occurrence | Tekrarlanan aktiviteler için "?day=" ekleyin |
| Quick Action does nothing on cold launch | Bekle ~0.4 s veya yeniden deneme; geri bildirim / ihtiyaç UI Dağı zamanı |
| `iwool://island` does not start countdown automatically | **kreasyon sayfası** - onay süresi ve uygulama içine başlayın |
| Quick Countdown requires iOS 16.2+ | Event Live Activities iOS 16.1+'ya ihtiyaç duyar; standalone ada sayısı 16.2+ |

---

[Privacy Policy](./privacy)

</section>
