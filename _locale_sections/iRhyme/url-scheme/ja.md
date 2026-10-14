iRhymeは** `irhyme://` **ショートカットリンク(URLスキーム)をサポートしています。 コールドスタートとホーム画面のショートカットは、統一されたバッファを介して配信されますので、リンクはオンボーディング後2回開いていません。

## リンク形式


```
irhyme://{host}?{params}
```


## パスポートと著者

| URL | 開く画面 |
|-----|-------|
| `irhyme://passage?id={id}` | 章句の詳細 |
| `irhyme://saying?id={id}` / `irhyme://couplet?id={id}` / `irhyme://poem?id={id}` | 通路と同じ(互換性) |
| `irhyme://passage?id={id}&card=1` | 通路の細部およびカード シート |
| `irhyme://card?id={id}` / `irhyme://share-card?id={id}` | ライムカード |
| `irhyme://author?id={id}` | 作者の詳細 |
| `irhyme://recite` / `irhyme://recite?id={id}` | 誦読フロー |

## ディスカバリー&プラクティス

| URL | 開く画面 |
|-----|-------|
| `irhyme://home` | ホーム |
| `irhyme://daily` | 今日のライム |
| `irhyme://random` | ランダムな章句 |
| `irhyme://favorites` | お気に入り |
| `irhyme://famous` | 名句一覧 |
| `irhyme://search` / `irhyme://search?q={query}` | 検索 |
| `irhyme://study` / `irhyme://study?id={id}` | ライムアカデミー |
| `irhyme://hunt` | ライムハント (`keyword-hunt`/`flyflower`) |
| `irhyme://handwriting` | 手書き検索 (`handwrite`; iOS) |
| `irhyme://mastered` | マスタード (`progress`) |
| `irhyme://categories` / `irhyme://categories?section=` | ブラウズ |
| `irhyme://collection?id=` | コレクション / book (`shenglv` / `liweng` / `qianjia` /`youxue`) |
| `irhyme://corpus` | すべての通路 (`all`) |
| `irhyme://last-read` | 最後に読んだ項目 |
| `irhyme://reading-history` | 閲覧履歴 |
| `irhyme://notes` | ノート |
| `irhyme://pair` | 並列練習 |
| `irhyme://prosody` | プロソディデスク |
| `irhyme://rhyme?id=dong` | 1つの韻のクラス |
| `irhyme://compare?rhyme=dong` | 同じ韻比較 |
| `irhyme://glossary?id=` | 用語集 |

## 設定とガイド

| URL | 開く画面 |
|-----|-------|
| `irhyme://settings` | 設定 |
| `irhyme://usage-guide` | 使い方ガイド |
| `irhyme://widget-guide` | ウィジェットガイド |
| `irhyme://shortcuts-guide` | ショートカットガイド |
| `irhyme://feature-guide` | オンボーディングの再生 |
| `irhyme://feedback` | フィードバックメール |
| `irhyme://in-app-review` | アプリ内／App Store レビュー |

## 例


```
irhyme://daily
irhyme://passage?id=1001
irhyme://pair
irhyme://compare?rhyme=dong
irhyme://collection?id=shenglv
irhyme://study
irhyme://hunt
```


## ノート

- パラメータはIDが数値である場合感度です。
- シリ、ショートカット、ウィジェット、およびコントロールセンターコントロールは、同じディープリンクルートを使用します。
- 最新リストのアプリ内設定 → Help** ガイドを参照してください。


