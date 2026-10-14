iCangJieは** `iCangJie://` **をサポートしています URLスキームの深いリンク — 参照検索、単語詳細、毎日のクイズ、タイピング、お気に入り、間違ったブック、レベル、またはSafari、別のアプリ、QRコード、ウィジェットタップ、またはAppleショートカットから学びます。

**ホーム画面クイックアクション**(アプリのアイコンを長押し)の並列セットは、検索、フィードバック、およびレートなどの追加の目的地をカバーしています。 *Settings → App Settings → Home Screen Shortcuts**で最大4つのショートカットを設定します。

## プロトコル仕様


```
iCangJie://<host>[?query]
```


| Rule | 詳細を見る |
|------|--------|
| **Scheme** | `icangjie`/`iCangJie` — ケースを無感覚に比較 |
| **Host routing** | プライマリルータはURL **ホスト**です。 |
| **Query aliases** | `q`, `word`, `name` は、検索/単語のホストに交換可能 |
| **Parser** | `ICangJieDeepLink.parse( :)` — を `onOpenURL` → `AppRouter.pendingDeepLink` 経由で消費 |

**3つの配達チャネル**

| Channel | Handled by | 例 |
|---------|------------|----------|
| **Universal deep link** (`onOpenURL`) | `ICangJieDeepLink.parse` → `RootTabView` | `search`、`word`、`quiz`、`typing`、`favorites`、`wrong`、`levels`、`learn` |
| **Home Screen Quick Action** | `ShortcutObserver.dispatch` | `search`、`quiz`、`favorites`、`wrong`、`levels`、`feedback`、`review` |
| **App Intents / Siri / Widget pending URL** | Writes `AppGroup.pendingDeepLinkURL` → `RootTabView.consumePendingDeepLinkFromAppGroup()` | ルックアップコード、クイズ、オープン検索を開始 |

クイックアクションタイプは、タイプ文字列にマッチする** `iCangJie://` **を使うので、 `icangjie` とレガシーのバリアントも正しくルーティングします。

---

## 1. 探査検索

**Lookup**タブを開きます。 オプションで、検索フィールドを事前に入力します。

| Parameter | Required | コンテンツ |
|-----------|----------|-------------|
| `q` | No | 検索クエリ(コードプレフィックス、文字、ピンイン、またはJyutping) |
| `word` | No | `q` の同義語 |
| `name` | No | `q` の同義語 |

**Lookup(空検索)を開く**


```
iCangJie://search
```


**コード接頭辞の検索 `iCangJie://` **


```
iCangJie://search?q=ab
```


**キャラクター検索**


```
iCangJie://search?q=颉
```


---

## 2. 単語の細部

1つの文字の詳細はページを開きます。 非空のクエリが必要です。

| Parameter | Required | コンテンツ |
|-----------|----------|-------------|
| `q` | One of `q` / `word` / `name` | ターゲットハンキャラ |
| `word` | One of `q` / `word` / `name` | `q` の同義語 |
| `name` | One of `q` / `word` / `name` | `q` の同義語 |

**主催:** `iCangJie://` , `icangjie` , `iCangJie` ** KURA のオープンディテール**


```
iCangJie://word?q=倉
```


代替ホスト:


```
iCangJie://character?word=颉
```


クエリが **empty または文字が辞書にない場合**、リンクは無視されます**。

---

## 3. 毎日のクイズ

**デイリークイズ**に直接ジャンプします。 質問を自動起動またはスキップしません。


```
iCangJie://quiz
```


別名で: `iCangJie://` ---

## 4. タイピング練習

**Typing**タブハブを開きます。


```
iCangJie://typing
```


別名で: `iCangJie://` 、 `icangjie` ---

## 5.お気に入り

**お気に入り**リストを開きます。


```
iCangJie://favorites
```


別名で: `iCangJie://` ---

## 6. 間違った答えの本

### 6.1 リスト

**間違った回答ブック**リストを開きます。


```
iCangJie://wrong
```


別名で: `iCangJie://` 、 `icangjie` ### 6.2 シングルレコード `iCangJie://` が保存された不備なエントリの有効な UUID である場合、このアプリはレコードの単語の詳細(レコードがまだ存在する場合)を開きます。

| Parameter | Required | フォーマット |
|-----------|----------|--------|
| `record` | Yes | UUID 文字列 |
| `id` | Yes | `record` の同義語 |


```
iCangJie://wrong?record=550e8400-e29b-41d4-a716-446655440000
```


---

## 7. レベル(コードの長さ)

**Levels**タブを開きます。


```
iCangJie://levels
```


別名で: `iCangJie://` 、 `icangjie` ---

## 8. 学習(チュートリアル)

**Learn** ハブを開きます。


```
iCangJie://learn
```


別名で: `iCangJie://` ---

## 9. フィードバック(クイックアクションのみ)

プレフィルドフィードバックメールコンポーザー(または `iCangJie://` フォールバック)を開きます。


```
iCangJie://feedback
```


**ホーム画面クイックアクション** / `iCangJie://` , `icangjie` ではなく、処理

---

## 10. アプリストアレビュー(クイックアクションのみ)

アプリ内 App Store レビュー プロンプトをリクエストします。


```
iCangJie://review
```


Alias マッチングは、クイックアクション型の文字列で `iCangJie://` も受け付けます。

---

## 11. アプリの意図とシリ (iOS 16 +)

内蔵**Appショートカット**はショートカットアプリとシリに表示されます。 各インテントは、App Group で `iCangJie://` をセットします。アプリは起動時に消費します。

| Intent | Action | 送信URL |
|--------|--------|-------------|
| **Look up Cangjie code** | Opens word detail for the given character | iCangJie://word?q=<char>` |
| **Start daily quiz** | Opens Daily Quiz | 「iCangJie://quiz」 |
| **Open lookup search** | Opens Lookup tab | 「iCangJie://search」 |

**シリフレーズ例(英語)**

- *「Cangjieコードを調べる」*
- *「iCangJieで日々のクイズを始める」*
- *「iCangJieでカンジエを検索」*

**ショートカット**で、iCangJieアプリセクションからアクションを追加します。 **Look up** は、** 中国語文字** パラメータ ( `iCangJie://` ) が必要です。

> App Intents は、**iOS のみです。 macOS は `iCangJie://` の URL とメニューのナビゲーションに依存しています。

---

## ウィジェットディープリンク

ウィジェットは同じ `iCangJie://` の URL をタップします。 例:

| Widget | 典型的な URL |
|--------|-------------|
| Daily Character | iCangJie://word?q=<char>` |
| Code Length | 「iCangJie://levels」 |
| Daily Quiz | 「iCangJie://quiz」 |
| Typing Glance | iCangJie://タイピング |
| Favorites | 「iCangJie」 http://favorites」 |
| Wrong Book | 「iCangJie://wrong」 |
| Recent | 「iCangJie://search」 |
| Learning Progress | 「iCangJie」 http://learn` |

---

## ショートカット例

**今日のクイズを開く**


```
iCangJie://quiz
```


**クリップボードからキャラクターを見る**

Shortcuts **Get Clipboard** アクションを使用して、** URL** を以下で開きます。


```
iCangJie://word?q=[Clipboard]
```


**タイピング練習を開始**


```
iCangJie://typing
```


---

## ホーム スクリーンの速い行為

iCangJieアプリアイコンを長押しします。 デフォルトオプション(設定で最大4つを選択):

| Action | サイトマップ |
|--------|-----|
| Search | 「iCangJie://search」 |
| Daily Quiz | 「iCangJie://quiz」 |
| Favorites | 「iCangJie」 http://favorites」 |
| Wrong Book | 「iCangJie://wrong」 |
| Code Length | 「iCangJie://levels」 |
| Feedback | 「iCangJie://feedback」 |
| Rate App | 「iCangJie://review」 |


