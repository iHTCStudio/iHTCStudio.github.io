iEnglishは** `ienglish://` **をサポート URLスキームの深いリンク - 単語、毎日のクイズ、お気に入り、間違ったブック、プレイリスト、またはSafari、ショートカット、ウィジェット、または別のアプリからカテゴリを開きます。

**ホーム画面のクイックアクション**(アプリのアイコンを長押し)検索、フィードバック、およびレートを追加 — これらのタイプは、 `ienglish://` によってパースされていないが、まだショートカットのオブザーバーを介してアプリを開きます。

> **注意:** リンクはアプリ内の**navigate**のみです。 発音や遠隔で学習設定を変更しない。

## プロトコル


```
ienglish://<host>[?query]
```


| Rule | 詳細を見る |
|------|--------|
| **Scheme** | `ienglish` (ケースインセンティブ) |
| **Word detail** | ホスト `word` — クエリ **id=<wordID>`** (必須、非空) |
| **Quiz** | ホスト `quiz` |
| **Favourites** | ホスト `お気に入り` |
| **Wrong book** | ホスト `wrong` または `mistakes` — オプション `record=<UID>` は 1 つの間違いを開きます |
| **Playlist** | ホスト `playlist` |
| **Categories** | ホスト `categories` |

## 例


```
ienglish://word?id=apple
ienglish://quiz
ienglish://favorites
ienglish://wrong
ienglish://wrong?record=550E8400-E29B-41D4-A716-446655440000
ienglish://playlist
ienglish://categories
```


## ホーム スクリーンの速い行為

**設定 → ホーム画面ショートカット**で**4**まで設定します。 種類には、 `ienglish://` 、 `IEnglishDeepLink` 、 `ienglish` 、 `word` 、 `id=<wordID>` 、 `quiz` 、 `favorites` - 検索/フィードバック/レビューは、クイックアクションとしてのみ配信されます。

## ウィジェットディープリンク

Widget は `ienglish://` と同じホストを使用します (例: デイリー・クイズ → `IEnglishDeepLink` , お気に入り・グレンス → `ienglish` )。

[概要に戻る](...)・[FAQ](../faq)・[プライバシーポリシー](../privacy)


