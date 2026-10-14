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


