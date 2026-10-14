iYijingは** `iyijing://` **ショートカットリンク(URLスキーム)をサポートしています。 コールドスタートとホーム画面のショートカットは、統一されたバッファを介して配信されますので、リンクはオンボーディング後2回開いていません。

## リンク形式


```
iyijing://{host}/{path}?{params}
```


## ヘキサグラムと発見

| URL | 開く画面 |
|-----|-------|
| `iyijing://home` | ホーム |
| `iyijing://daily` | 今日の毎日のヘキサグラム |
| `iyijing://random` | ランダムヘキサグラム |
| `iyijing://hexagram/{id}` | ヘキサグラムの詳細(`グア/{id}`エイリアス) |
| `iyijing://wing/{id}` | テンウィングステキスト(`イジアン/{id}`エイリアス) |
| `iyijing://trigram/{id}` | トライグラム (`bagua/{id}` alias) |
| `iyijing://browse` | ブラウズ |
| `iyijing://favorites` | お気に入り |
| `iyijing://famous` | 名句一覧 |
| `iyijing://search` / `?q=` | 検索 |
| `iyijing://study` | イージング・スタディ |
| `iyijing://hunt` | キーワードハント |
| `iyijing://divination` | 文化キャスティング (`qigua`/`cast`) |
| `iyijing://recite` / `recite/{id}` | 新着情報 |
| `iyijing://collection` | ヘキサグラムリスト (`playlist` alias) |
| `iyijing://last-read` | 最後に読んだ項目 |
| `iyijing://reading-history` | 閲覧履歴 |
| `iyijing://notes` | ノート |
| `iyijing://mastered` | マスタード |
| `iyijing://wrong-book` | 間違った書籍を学ぶ |
| `iyijing://recite-wrong` | 間違った本を認めて下さい |

## 設定とガイド

| URL | 開く画面 |
|-----|-------|
| `iyijing://settings` | 設定 |
| `iyijing://usage-guide` | 使い方ガイド |
| `iyijing://widget-guide` | ウィジェットガイド |
| `iyijing://shortcuts-guide` | ショートカットガイド |
| `iyijing://feature-guide` | オンボーディングの再生 |
| `iyijing://feedback` | フィードバックメール |

## 例


```
iyijing://daily
iyijing://hexagram/1
iyijing://wing/301
iyijing://divination
iyijing://study
iyijing://hunt
iyijing://famous
iyijing://search?q=乾
```


これらをショートカットアプリ、ホーム画面のクイックアクション、ウィジェット、コントロールセンター、またはSafariで使用してください。 アプリ内設定 → ショートカットガイド** も参照してください。


