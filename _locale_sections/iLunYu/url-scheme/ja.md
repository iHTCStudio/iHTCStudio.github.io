iLunYuは** `ilunyu://` **ショートカットリンク(URLスキーム)をサポートしています。 コールドスタートとホーム画面のショートカットは、統一されたバッファを介して配信されますので、リンクはオンボーディング後2回開いていません。

## リンク形式


```
ilunyu://{host}?{params}
```


## 章と著者

| URL | 開く画面 |
|-----|-------|
| `ilunyu://passage?id={id}` | 章の詳細 |
| `ilunyu://couplet?id={id}` / `ilunyu://poem?id={id}` | 通路と同じ(互換性) |
| `ilunyu://author?id={id}` | 作者の詳細 |
| `ilunyu://recite` | 誦読フロー |
| `ilunyu://recite?id={id}` | 章を開き、自動recite |

## 発見

| URL | 開く画面 |
|-----|-------|
| `ilunyu://home` | ホームタブ |
| `ilunyu://daily` | 本日のデイリーVerse |
| `ilunyu://random` | ランダムチャプター |
| `ilunyu://favorites` | お気に入り |
| `ilunyu://famous` | 名句一覧 |
| `ilunyu://search` / `ilunyu://search?q={query}` | 検索 |
| `ilunyu://study` | 学習教室 |
| `ilunyu://hunt` | Hunt(寻)。aliases`keyword-hunt`/`flyflower` |
| `ilunyu://mastered` / `ilunyu://progress` | マスタード/進行 |
| `ilunyu://categories` / `ilunyu://categories?section=` | ブラウズ |
| `ilunyu://collection?id=lunyu` | ブックコレクション(別名 `book`/`form`;`name=`) |
| `ilunyu://theme?id=` | テーマまたはボリューム(例えば `junzi`、`xue-er`; aliases`suite`/`volume`) |
| `ilunyu://last-read` | 最後に読んだ項目 |
| `ilunyu://reading-history` | 閲覧履歴 |
| `ilunyu://notes` | ノート |

## 設定とガイド

| URL | 開く画面 |
|-----|-------|
| `ilunyu://settings` | 設定 |
| `ilunyu://usage-guide` | 使い方ガイド |
| `ilunyu://widget-guide` | ウィジェットガイド |
| `ilunyu://shortcuts-guide` | ショートカットガイド |
| `ilunyu://feature-guide` | オンボーディングの再生 |
| `ilunyu://feedback` | フィードバックメール |
| `ilunyu://in-app-review` | アプリ内／App Store レビュー |

## 例


```
ilunyu://daily
ilunyu://passage?id=1
ilunyu://recite?id=20
ilunyu://theme?id=junzi
ilunyu://study
ilunyu://hunt
```


これらをショートカットアプリ、ホーム画面のクイックアクション、ウィジェット、またはSafariで使用してください。 アプリ内設定 → ショートカットガイド** も参照してください。


