iMenciusは** `imencius://` **ショートカットリンク(URLスキーム)をサポートしています。 コールドスタートとホーム画面のショートカットは、統一されたバッファを介して配信されますので、リンクはオンボーディング後2回開いていません。

## リンク形式


```
imencius://{host}?{params}
```


## パスポートと著者

| URL | 開く画面 |
|-----|-------|
| `imencius://passage?id={id}` | 章句の詳細 |
| `imencius://saying?id={id}` / `imencius://couplet?id={id}` / `imencius://poem?id={id}` | 通路と同じ(互換性) |
| `imencius://passage?id={id}&card=1` | 通路の細部およびカード シート |
| `imencius://card?id={id}` / `imencius://share-card?id={id}` | カード |
| `imencius://author?id={id}` | 作者の詳細 |
| `imencius://recite` / `imencius://recite?id={id}` | 誦読フロー |

## ディスカバリー&プラクティス

| URL | 開く画面 |
|-----|-------|
| `imencius://home` | ホーム |
| `imencius://daily` | 日常の言うこと |
| `imencius://random` | ランダムな章句 |
| `imencius://favorites` | お気に入り |
| `imencius://famous` | 名句一覧 |
| `imencius://search` / `imencius://search?q={query}` | 検索 |
| `imencius://study` / `imencius://study?id={id}` | Qiの学習 |
| `imencius://hunt` | 李ハント (`keyword-hunt`/`flyflower`) |
| `imencius://handwriting` | 手書き検索 (`handwrite`; iOS) |
| `imencius://mastered` | マスタード (`progress`) |
| `imencius://categories` / `imencius://categories?section=` | ブラウズ |
| `imencius://collection?id=` | コレクション/書籍 |
| `imencius://corpus` | すべての通路 (`all`) |
| `imencius://last-read` | 最後に読んだ項目 |
| `imencius://reading-history` | 閲覧履歴 |
| `imencius://notes` | ノート |
| `imencius://fables` / `imencius://allegories` / `imencius://concepts` | 利用できる場合の特別な棚 |

## 設定とガイド

| URL | 開く画面 |
|-----|-------|
| `imencius://settings` | 設定 |
| `imencius://usage-guide` | 使い方ガイド |
| `imencius://widget-guide` | ウィジェットガイド |
| `imencius://shortcuts-guide` | ショートカットガイド |
| `imencius://feature-guide` | オンボーディングの再生 |
| `imencius://feedback` | フィードバックメール |
| `imencius://in-app-review` | アプリ内／App Store レビュー |

## 例


```
imencius://daily
imencius://passage?id=1
imencius://study
imencius://hunt
```



