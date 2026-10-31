iLvShiは、** `ilvshi://` **ショートカットリンク(URLスキーム)をサポートしています。 コールドスタートとホーム画面のショートカットは、統一されたバッファを介して配信されますので、リンクはオンボーディング後2回開いていません。

## リンク形式


```
ilvshi://{host}?{params}
```


## パスポートと著者

| URL | 開く画面 |
|-----|-------|
| `ilvshi://passage?id={id}` | 章句の詳細 |
| `ilvshi://saying?id={id}` / `ilvshi://couplet?id={id}` / `ilvshi://poem?id={id}` | 通路と同じ(互換性) |
| `ilvshi://passage?id={id}&card=1` | 通路の細部およびカード シート |
| `ilvshi://card?id={id}` / `ilvshi://share-card?id={id}` | 秋のカード |
| `ilvshi://author?id={id}` | 作者の詳細 |
| `ilvshi://recite` / `ilvshi://recite?id={id}` | 誦読フロー |

## ディスカバリー&プラクティス

| URL | 開く画面 |
|-----|-------|
| `ilvshi://home` | ホーム |
| `ilvshi://daily` | 毎日のパッセージ |
| `ilvshi://random` | ランダムな章句 |
| `ilvshi://favorites` | お気に入り |
| `ilvshi://famous` | 名句一覧 |
| `ilvshi://search` / `ilvshi://search?q={query}` | 検索 |
| `ilvshi://study` / `ilvshi://study?id={id}` | 春-秋学研究 |
| `ilvshi://hunt` | 秋のハント (`keyword-hunt`/`flyflower`) |
| `ilvshi://handwriting` | 手書き検索 (`handwrite`; iOS) |
| `ilvshi://mastered` | マスタード (`progress`) |
| `ilvshi://categories` / `ilvshi://categories?section=` | ブラウズ |
| `ilvshi://collection?id=` | コレクション/書籍 |
| `ilvshi://corpus` | すべての通路 (`all`) |
| `ilvshi://last-read` | 最後に読んだ項目 |
| `ilvshi://reading-history` | 閲覧履歴 |
| `ilvshi://notes` | ノート |
| `ilvshi://fables` / `ilvshi://allegories` / `ilvshi://concepts` | 利用できる場合の特別な棚 |

## 設定とガイド

| URL | 開く画面 |
|-----|-------|
| `ilvshi://settings` | 設定 |
| `ilvshi://usage-guide` | 使い方ガイド |
| `ilvshi://widget-guide` | ウィジェットガイド |
| `ilvshi://shortcuts-guide` | ショートカットガイド |
| `ilvshi://feature-guide` | オンボーディングの再生 |
| `ilvshi://feedback` | フィードバックメール |
| `ilvshi://in-app-review` | アプリ内／App Store レビュー |

## 例


```
ilvshi://daily
ilvshi://passage?id=1
ilvshi://study
ilvshi://hunt
```



