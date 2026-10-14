iSutraは** `isutra://` **ショートカットリンク(URLスキーム)をサポートしています。 コールドスタートとホーム画面のショートカットは、統一されたバッファを介して配信されますので、リンクはオンボーディング後2回開いていません。

## リンク形式


```
isutra://{host}?{params}
```


## Sutrasと著者

| URL | 開く画面 |
|-----|-------|
| `isutra://passage?id={id}` | ストラディテール |
| `isutra://couplet?id={id}` / `isutra://poem?id={id}` | 通路と同じ(互換性) |
| `isutra://author?id={id}` | トランスレーター/作者詳細 |
| `isutra://recite` / `isutra://recite?id={id}` | 誦読フロー |
| `isutra://large?id=diamond` / `isutra://large?id=dizang` | 大型書籍ボリュームカタログ |

## ディスカバリー&プラクティス

| URL | 開く画面 |
|-----|-------|
| `isutra://home` | ホーム |
| `isutra://daily` | 本日の日替わりスートラ |
| `isutra://random` | ランダムな章句 |
| `isutra://favorites` | お気に入り |
| `isutra://famous` | 名句一覧 |
| `isutra://search` / `isutra://search?q={query}` | 検索 |
| `isutra://study` | スタディホール |
| `isutra://hunt` | ハント (寻经); エイリアス `keyword-hunt`/`flyflower` |
| `isutra://count` | 木魚ちゃん (`chant`/`muyu`/`counter`) |
| `isutra://copy` / `isutra://copy?id={id}` | コピーストラ(iOS) |
| `isutra://practice` | 朝/夕方の練習 |
| `isutra://mastered` | マスタード |
| `isutra://categories` / `isutra://categories?section=` | ブラウズ |
| `isutra://collection?id=` | コレクション(例えば、`prajna`、`forty-two`;`name=`) |
| `isutra://theme?id=` | テーマ(例:`xingyuan`、`yaoshi`、`platform`) |
| `isutra://last-read` | 最後に読んだ項目 |
| `isutra://reading-history` | 閲覧履歴 |
| `isutra://notes` | ノート |

## 設定とガイド

| URL | 開く画面 |
|-----|-------|
| `isutra://settings` | 設定 |
| `isutra://usage-guide` | 使い方ガイド |
| `isutra://widget-guide` | ウィジェットガイド |
| `isutra://shortcuts-guide` | ショートカットガイド |
| `isutra://feature-guide` | オンボーディングの再生 |
| `isutra://privacy` | アプリ内プライバシー |
| `isutra://feedback` | フィードバックメール |
| `isutra://in-app-review` | アプリ内／App Store レビュー |

## 例


```
isutra://daily
isutra://passage?id=1
isutra://large?id=diamond
isutra://count
isutra://copy?id=1
isutra://practice
isutra://collection?id=prajna
isutra://theme?id=xingyuan
isutra://study
isutra://hunt
```


これらをショートカットアプリ、ホーム画面のクイックアクション、ウィジェット、またはSafariで使用してください。 アプリ内設定 → ショートカットガイド** も参照してください。


