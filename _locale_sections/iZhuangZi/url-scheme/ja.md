iZhuangZiは** `izhuangzi://` **ショートカットリンク(URLスキーム)をサポートしています。 コールドスタートとホーム画面のショートカットは、統一されたバッファを介して配信されますので、リンクはオンボーディング後2回開いていません。

## リンク形式


```
izhuangzi://{host}?{params}
```


## パスポートと著者

| URL | 開く画面 |
|-----|-------|
| `izhuangzi://passage?id={id}` | 章句の詳細 |
| `izhuangzi://saying?id={id}` / `izhuangzi://couplet?id={id}` / `izhuangzi://poem?id={id}` | 通路と同じ(互換性) |
| `izhuangzi://passage?id={id}&card=1` | 通路の細部およびカード シート |
| `izhuangzi://card?id={id}` / `izhuangzi://share-card?id={id}` | クレジットカード |
| `izhuangzi://author?id={id}` | 作者の詳細 |
| `izhuangzi://recite` / `izhuangzi://recite?id={id}` | 誦読フロー |

## ディスカバリー&プラクティス

| URL | 開く画面 |
|-----|-------|
| `izhuangzi://home` | ホーム |
| `izhuangzi://daily` | 毎日のZhuangzi |
| `izhuangzi://random` | ランダムな章句 |
| `izhuangzi://favorites` | お気に入り |
| `izhuangzi://famous` | 名句一覧 |
| `izhuangzi://search` / `izhuangzi://search?q={query}` | 検索 |
| `izhuangzi://study` / `izhuangzi://study?id={id}` | 大夫研究 |
| `izhuangzi://hunt` | チュアン・ハント (`keyword-hunt`/`flyflower`) |
| `izhuangzi://handwriting` | 手書き検索 (`handwrite`; iOS) |
| `izhuangzi://mastered` | マスタード (`progress`) |
| `izhuangzi://categories` / `izhuangzi://categories?section=` | ブラウズ |
| `izhuangzi://collection?id=` | コレクション / ブック (`neipian`/`waipian`/`zapian`) |
| `izhuangzi://corpus` | すべての通路 (`all`) |
| `izhuangzi://last-read` | 最後に読んだ項目 |
| `izhuangzi://reading-history` | 閲覧履歴 |
| `izhuangzi://notes` | ノート |
| `izhuangzi://ask` | お問い合わせ |
| `izhuangzi://allegories` | パナブル |
| `izhuangzi://concepts` | コンセプト |
| `izhuangzi://theme?id=neipian` | インナー・アウター・その他 |

## 設定とガイド

| URL | 開く画面 |
|-----|-------|
| `izhuangzi://settings` | 設定 |
| `izhuangzi://usage-guide` | 使い方ガイド |
| `izhuangzi://widget-guide` | ウィジェットガイド |
| `izhuangzi://shortcuts-guide` | ショートカットガイド |
| `izhuangzi://feature-guide` | オンボーディングの再生 |
| `izhuangzi://feedback` | フィードバックメール |
| `izhuangzi://in-app-review` | アプリ内／App Store レビュー |

## 例


```
izhuangzi://daily
izhuangzi://passage?id=1
izhuangzi://ask
izhuangzi://allegories
izhuangzi://collection?id=neipian
izhuangzi://study
izhuangzi://hunt
```


## ノート

- パラメータはIDが数値である場合感度です。
- シリ、ショートカット、ウィジェット、およびコントロールセンターコントロールは、同じディープリンクルートを使用します。
- 最新リストのアプリ内設定 → Help** ガイドを参照してください。


