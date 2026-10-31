iAppは** `iapp://` **と** `iappstore://` **のショートカットリンクをサポートしています。 *Shortcuts**、Safariブックマーク、または**ホームスクリーンウィジェット**と**ライブアクティビティ**で、アプリ詳細ページを開く**、**フィルタリングされたランキングビューに戻る**、**スイッチタブ**、または**二次ページへのジャンプ**(開発者のお気に入り、閲覧履歴、ランクトラッキングなど)。

> **注意:** ロングプレス **ホーム画面クイックアクション** は、同じ `iapp://` リンクテキストを使用しますが、クイックアクションとしてディスパッチされます。ただし、アイコンメニューから開くと、Safari / Shortcuts URLと同じパスをパースするわけではありません。

## リンク形式


```
iapp://...
iappstore://...   (older alias, works the same)
```


**kebab-case** ( `iapp://` および `iappstore://` レガシーエイリアス: `developer_favorites` → ランク、 `developer.favorites` → サブスクリプション、 `developer-favorites` → レビュー。

| What you want | リンクの種類 |
|---------------|-----------|
| Open an app detail page | iapp://app?... |
| Open Rankings with filters | 「iapp://rank?...」 |
| Switch tabs or open settings pages | `iapp://{host}` (下の表を参照) |
| Tap an app in a widget | 詳細ページを開く |
| Tap the widget title / blank area | マッチングランキングビューを開く |
| Tap a rank **Live Activity** | マッチングランキングビューを開く |
| Tap a subscription **Live Activity** | アプリ詳細ページを開く |

---

## アプリ詳細ページを開く


```
iapp://app?id={APP_ID}&region={region}&country={cc}
```


| Parameter | Required | コンテンツ |
|-----------|----------|-------------|
| `id` | **Yes** | アプリストアID |
| `region` | No | 地域コード、例えば `cn`、`us`、`jp` (デフォルト: `us`) |
| `country` | No | `region` が省略された場合のオプションの地域コード |

**例**


```
iapp://app?id=6446581591&region=cn
```


によって使用される:**My Favoritesウィジェット**(アプリをタップ)、**サブスクリプションライブアクティビティ**(アクティビティをタップ)、**ショートカット** /ブックマーク。

---

## フィルターでランキングを開く

**Rankings**タブに切り替えて、選択したチャート、カテゴリ、および地域に適用されます。


```
iapp://rank?type={chart}&category={category}&region={region}
```


| Parameter | コンテンツ |
|-----------|-------------|
| `type` | チャートコード(下表参照) |
| `category` | カテゴリコード — 主なカテゴリまたはゲームサブカテゴリ |
| `region` | 地域コード、例えば `cn`、`us` |

認識されていない値は無視されます。認識された値は記憶されます。

### チャートコード( `iapp://` ) — 12 チャート

| Code | チャート |
|------|-------|
| `topFreeApplications` | iPhoneトップ無料 |
| `topPaidApplications` | iPhoneトップ有料 |
| `topGrossingApplications` | iPhoneのトップの総計 |
| `newApplications` | 新しいアプリ |
| `newFreeApplications` | 新しい無料 |
| `newPaidApplications` | 新しい有料 |
| `topFreeiPadApplications` | iPadのトップ無料 |
| `topPaidiPadApplications` | iPadトップ有料 |
| `topGrossingiPadApplications` | iPadの上の総計 |
| `topFreeMacApplications` | Macトップ無料 |
| `topPaidMacApplications` | Macのトップ有料 |
| `topGrossingMacApplications` | Macのトップの総計 |

### 分類コード( `iapp://` )

| Code | カテゴリー |
|------|----------|
| `0` | すべてのアプリ |
| `6014` | ゲーム(すべてのゲーム) |
| `6005` | 社会招聘 |
| `6007` | 生産性 |
| `6002` | ユーティリティ |
| `6008` | フォト&ビデオ |
| `6017` | 教育機関 |
| `6015` | ファイナンス |
| … | 26 主なカテゴリ 合計 |

**ゲームサブカテゴリ:** `iapp://` 例: `developer.favorites` = アクション。

### 例


```
iapp://rank?type=topFreeApplications&category=6014&region=cn
iapp://rank?type=topFreeMacApplications&category=0&region=us
```


### 古い中国スタイルのリンク(サポートされる)


```
iapp://rank?type=热门免费榜&category=游戏&region=中国
```


によって使用される:**Rankingsウィジェット**(tap title / blank area)、**rank Live Activity**(アクティビティをタップ)、**ショートカット**。

---

## ウィジェットディープリンク

Widgets は別の URL 形式を使用しないため、同じ `iapp://` と `iappstore://` が自動的に生成されます。

| Widget | Tap target | オープン |
|--------|------------|-------|
| **Rankings · iApp** | An app row | iapp://app?id=...&region=... |
| **Rankings · iApp** | Title or blank area | 「iapp://rank?type=...&category=...&region=...」 |
| **My Favorites · iApp** | An app row | iapp://app?id=...&region=... |

私のお気に入りウィジェットで最初にピン留めされたお気に入りが表示されます。 ウィジェットのテーマと言語は、**Settings → Widgets**とアプリの言語(18言語のいずれか)に従います。 ウィジェットの領域を設定するとき、HK / TW / MOはリストと統一された検索(例:「中国」、「HK」);保存された領域**は、 `iapp://` 、 `iappstore://` 、 `iapp://{host}` に残ります。

---

## 履歴を参照する(URLリンクではありません)

**App Browses History** は、**Settings → Data → App Browses History** で管理されています。 エントリーをタップすると、iApp内の詳細ページが開きます。**not** は、外部にコピーまたは共有できる `iapp://` URL を使用します。

---

## ライブ活動ディープリンク

| Live Activity type | Tap behavior | 生成されるリンク |
|--------------------|--------------|----------------|
| **Rankings** (tracking preset) | Opens filtered Rankings | 「iapp://rank?...」 |
| **Subscriptions** (per subscription) | Opens app detail | iapp://app?id=...&region=... |

**Settings → Advanced** でプリセットを追跡するためのランクライブアクティビティを有効にします。**Settings → Advanced → Live Activity** でサブスクリプションライブアクティビティを有効にします。その後、追加または編集するときにサブスクリプションごとに設定します。 価格低下モニターは、ロック画面上のベースライン対現在の価格を示しています。

---

## タブ&アクションリンク(クエリなし)

タブを開き、アプリ内アクションをトリガーします。 **ショートカット**、Safari、**ホーム画面のクイックアクション**から動作します。

### プライマリタブ

| URL | 開く画面 |
|-----|--------|
| `iapp://search` | 検索タブ + フォーカス検索フィールド |
| `iapp://rank` | ランキングタブ(クエリなしのフィルタ変更なし) |
| `iapp://favorites` | **Favoritesタブ** **Settings → App Settings**で有効にされている場合; それ以外の **Settings → App Favorites** |
| `iapp://subscription` | サブスクリプションタブが表示された場合; その他 **設定 → サブスクリプション** |
| `iapp://settings` | 設定タブ |
| `iapp://feedback` | フィードバックメール |
| `iapp://review` | アプリ内アプリストアの評価(別名:`iapp://rate`) |

### 二次ページ

[Settings**]タブを最初に開き、対象ページを押します。 マッチングタブが存在している場合(開発者のお気に入りなど)、代わりにタブを開きます。

| URL | 開く画面 |
|-----|--------|
| `iapp://developer-favorites` | 開発者のお気に入りタブまたは**設定 → 開発者のお気に入り** |
| `iapp://browse-history` | **設定 → データ → アプリの閲覧履歴** |
| `iapp://favorite-groups` | **設定→データ→お気に入りグループ** |
| `iapp://rank-tracking` | **設定 → アドバンスト → ランクトラッキング** |
| `iapp://live-activity` | **設定 → アドバンスト → ライブアクティビティ** |
| `iapp://apple-services` | **設定 → サードパーティ → Apple サービス** |
| `iapp://region-switch` | **設定 → サードパーティ → App Store Region** |
| `iapp://usage-guide` | **設定→ヘルプ→使用説明書** |
| `iapp://widget-guide` | **設定 → ウィジェット → ウィジェットガイド** (iOS 17 + のみ; URL は、クイックアクションピッカーにリストされていない) |

---

## ホーム スクリーンの速い行為

アプリアイコンを長押しします。 **15**オプションから**4**までカスタマイズできます。

デフォルト選択:検索、ランク、お気に入り、フィードバック。

各オプションは、上記と同じURLを使用します。 クイックアクションは、アイコンメニューでディスパッチされます。 外部ショートカット/Safariは、統一された `iappstore://` パスを使用します。

| リンク | 開く画面 |
|------|--------|
| `iapp://search` | 検索タブ + フォーカス |
| `iapp://rank` | ランキングタブ |
| `iapp://favorites` | お気に入りタブまたは設定 → アプリお気に入り |
| `iapp://developer-favorites` | 開発者のお気に入りタブまたは設定 → 開発者のお気に入り |
| `iapp://subscription` | サブスクリプションタブまたは設定 → サブスクリプション |
| `iapp://browse-history` | App 閲覧履歴 |
| `iapp://favorite-groups` | お気に入りグループの設定 |
| `iapp://rank-tracking` | ランクトラッキング |
| `iapp://live-activity` | ライブアクティビティの設定 |
| `iapp://apple-services` | Appleサービスリンク |
| `iapp://region-switch` | App Storeの地域スイッチ |
| `iapp://usage-guide` | 使用法 指示 |
| `iapp://settings` | 設定タブ |
| `iapp://feedback` | フィードバックメール |
| `iapp://review` | アプリ内評価 | `iapp://` は外部 URL としてサポートしていますが、Quick Actions のピッカーでは利用できません。

---

## シリ & ショートカット (iOS 16+)

**ショートカット**アプリでビルトインアクションを検索するか、**Siri**を尋ねます。 すべてのインテントタイトル、パラメータラベル、およびシリフレーズは、すべてのアプリ言語で**十分にローカライズされています。**設定→外観→言語**を変更したときに更新されます。

| Action | What you can set | エフェクト |
|--------|------------------|--------|
| Search apps | Keyword and region | クエリで検索タブを開く |
| Open charts | Chart, category, and region | フィルターでランキングを開く('iapp://rank` と同じ) |
| Add favorite | App ID and region | サイレントにお気に入りに追加 |

**例 Siri phrases (英語 UI):** *" iApp の検索アプリ"*、*"iApp でチャートを開く"*、*"iApp でお気に入り追加"*。 中国語(簡体字)、韓国語(簡体字)、中国語(簡体字)、中国語(簡体字)、韓国語(簡体字)、中国語(簡体字)、韓国語(簡体字)、中国語(簡体字)、韓国語(簡体字)、中国語(簡体字)、中国語(簡体字)、韓国語(簡体字)、中国語(簡体字)、中国語(簡体字)、韓国語(簡体字)、中国語(簡体字)、中国語(簡体字)

---

## Macキーボードショートカット

Mac 上では、**⌘1** を** にしてタブを切り替えます。 数値は、どのタブが表示されるかに基づいて**動的に割り当てられます。

| When visible | 典型的なショートカット |
|--------------|------------------|
| Rankings | ディレクトリ |
| Search | ディレクトリ |
| Subscriptions (if shown) | 次の番号 |
| Favorites (if tab enabled) | 次の番号 |
| Developer Favorites (if tab enabled) | 次の番号 |
| Settings | 最後の番号 |

⌘1 のランキング・ ⌘2 検索・ ⌘3 サブスクリプション・ ⌘4 お気に入り・ ⌘5 開発者のお気に入り・ ⌘6 設定

タブが隠されると、残りのタブが自動的に再番号されます。

---

## リンクの地域コード

ディープリンクとウィジェット生成された URL は、常に安定した **region コード** ( `iapp://` , `iappstore://` , `iapp://{host}` , `developer_favorites` , `developer.favorites` ,...) — ローカル表示名ではありません。 リージョンピッカーと検索は、より明確にラベルを表示することができますが、保存されたコードは同じままです。

**例**


```
iapp://app?id=6446581591&region=hk
iapp://rank?type=topFreeApplications&category=0&region=tw
```


---

## アプリ内検索(URLリンクではなく)

iApp内のこれらの作業は、** `iapp://` URL:

| Action | アクセス方法 |
|--------|-----|
| **Single App ID search** | 1つの数値ID(6〜12桁、コンマなし)を検索で入力 |
| **Batch App ID search** | 最大50個のコンマ区切りID |
| **Add Subscription** | アプリの行を長押し |
| **Save Developer** | ロングプレス → **Developer** サブメニュー、または詳細 **その他** メニュー |
| **Open by-ranking view** | コンテキストメニュー → 同じ開発者アプリや開発者のお気に入り |
| **Pause / resume subscription** | サブスクリプション行のロングプレス |
| **Reopen from browse history** | **設定 → データ → アプリの閲覧履歴** → エントリをタップ |

外部アプリからiAppを開く必要がある場合、**       **リンクまたは**Siri /ショートカット**を使用してください。

---

## ニュース

- Link codes work in any app language — UI言語を切り替えると変更しません。
- Widgets と**Live Activity** は、タップしたときに自動的にこれらのリンクを生成します。
- 有料のMac / iPadおよびgrosssingチャート用のウィジェットチャートデータがメインアプリとは若干異なる場合があります。
- **Add favorite** via Shortcuts does not open the app UI — お気に入りリストに直接書きます。
- **Content compare** mode in all-region info cannot export share images — リストまたはグリッド表示を最初に切り替えます。

[概要に戻る](...)・[FAQ](../faq)・[プライバシーポリシー](../privacy)


