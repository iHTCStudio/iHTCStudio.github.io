iDaoは** `idao://` **ショートカットリンク(URLスキーム)をサポートしています。 コールドスタートとホーム画面のショートカットは、統一されたバッファを介して配信されますので、リンクはオンボーディング後2回開いていません。

## リンク形式


```
idao://{host}?{params}
```


## 章と発見

| URL | 開く画面 |
|-----|-------|
| `idao://home` | ホーム |
| `idao://daily` | 今日の毎日の章 |
| `idao://random` | ランダムチャプター |
| `idao://chapter?id={id}` | 章の詳細 |
| `idao://recite` / `idao://recite?id={id}` | 誦読フロー |
| `idao://favorites` | お気に入り |
| `idao://famous` | 名句一覧 |
| `idao://search` / `idao://search?q={query}` | 検索 |
| `idao://study` | スタディホール |
| `idao://hunt` | Tao (タオ) |
| `idao://mastered` | マスタード |
| `idao://categories` / `?section=` | ブラウズ(オプションセクション) |
| `idao://book?id=` | ブックコレクション(dd`j`/`qingjing`/`yinfu`) |
| `idao://author` | Laoziイントロ |
| `idao://last-read` | 最後に読んだ項目 |
| `idao://reading-history` | 閲覧履歴 |
| `idao://notes` | ノート |

> 互換性エイリアス: `idao://` ## 設定とガイド

| URL | 開く画面 |
|-----|-------|
| `idao://settings` | 設定 |
| `idao://usage-guide` | 使い方ガイド |
| `idao://widget-guide` | ウィジェットガイド |
| `idao://shortcuts-guide` | ショートカットガイド |
| `idao://feature-guide` | オンボーディングの再生 |
| `idao://feedback` | フィードバックメール |
| `idao://in-app-review` | アプリ内／App Store レビュー |

## 例


```
idao://daily
idao://chapter?id=1
idao://recite?id=1
idao://study
idao://hunt
idao://famous
idao://book?id=ddj
idao://author
idao://search?q=上善若水
```


これらをショートカットアプリ、ホーム画面のクイックアクション、ウィジェット、コントロールセンター、またはSafariで使用してください。 アプリ内設定 → ショートカットガイド** も参照してください。


