iMoZiは** `imozi://` **ショートカットリンク(URLスキーム)をサポートしています。 コールドスタートとホーム画面のショートカットは、統一されたバッファを介して配信されますので、リンクはオンボーディング後2回開いていません。

## リンク形式


```
imozi://{host}?{params}
```


## パスポートと著者

| URL | 開く画面 |
|-----|-------|
| `imozi://passage?id={id}` | 章句の詳細 |
| `imozi://saying?id={id}` / `imozi://couplet?id={id}` / `imozi://poem?id={id}` | 通路と同じ(互換性) |
| `imozi://passage?id={id}&card=1` | 通路の細部およびカード シート |
| `imozi://card?id={id}` / `imozi://share-card?id={id}` | 墨カード |
| `imozi://author?id={id}` | 作者の詳細 |
| `imozi://recite` / `imozi://recite?id={id}` | 誦読フロー |

## ディスカバリー&プラクティス

| URL | 開く画面 |
|-----|-------|
| `imozi://home` | ホーム |
| `imozi://daily` | 今日のMo |
| `imozi://random` | ランダムな章句 |
| `imozi://favorites` | お気に入り |
| `imozi://famous` | 名句一覧 |
| `imozi://search` / `imozi://search?q={query}` | 検索 |
| `imozi://study` / `imozi://study?id={id}` | モヒズム研究 |
| `imozi://hunt` | センテンスハント (`keyword-hunt`/`flyflower`) |
| `imozi://handwriting` | 手書き検索 (`handwrite`; iOS) |
| `imozi://mastered` | マスタード (`progress`) |
| `imozi://categories` / `imozi://categories?section=` | ブラウズ |
| `imozi://collection?id=` | コレクション/書籍 |
| `imozi://corpus` | すべての通路 (`all`) |
| `imozi://last-read` | 最後に読んだ項目 |
| `imozi://reading-history` | 閲覧履歴 |
| `imozi://notes` | ノート |
| `imozi://ask` | Moziを依頼する |
| `imozi://fables` / `imozi://allegories` / `imozi://concepts` | 利用できる場合の特別な棚 |

## 設定とガイド

| URL | 開く画面 |
|-----|-------|
| `imozi://settings` | 設定 |
| `imozi://usage-guide` | 使い方ガイド |
| `imozi://widget-guide` | ウィジェットガイド |
| `imozi://shortcuts-guide` | ショートカットガイド |
| `imozi://feature-guide` | オンボーディングの再生 |
| `imozi://feedback` | フィードバックメール |
| `imozi://in-app-review` | アプリ内／App Store レビュー |

## 例


```
imozi://daily
imozi://passage?id=1
imozi://ask
imozi://study
imozi://hunt
```



