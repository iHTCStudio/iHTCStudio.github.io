iPreceptsは** `iprecepts://` **ショートカットリンク(URLスキーム)をサポートしています。 コールドスタートとホーム画面のショートカットは、統一されたバッファを介して配信されますので、リンクはオンボーディング後2回開いていません。

## リンク形式


```
iprecepts://{host}?{params}
```


## パスポートと著者

| URL | 開く画面 |
|-----|-------|
| `iprecepts://passage?id={id}` | 章句の詳細 |
| `iprecepts://saying?id={id}` / `iprecepts://couplet?id={id}` / `iprecepts://poem?id={id}` | 通路と同じ(互換性) |
| `iprecepts://passage?id={id}&card=1` | 通路の細部およびカード シート |
| `iprecepts://card?id={id}` / `iprecepts://share-card?id={id}` | クレジットカード |
| `iprecepts://author?id={id}` | 作者の詳細 |
| `iprecepts://recite` / `iprecepts://recite?id={id}` | 誦読フロー |

## ディスカバリー&プラクティス

| URL | 開く画面 |
|-----|-------|
| `iprecepts://home` | ホーム |
| `iprecepts://daily` | 毎日の受け入れ |
| `iprecepts://random` | ランダムな章句 |
| `iprecepts://favorites` | お気に入り |
| `iprecepts://famous` | 名句一覧 |
| `iprecepts://search` / `iprecepts://search?q={query}` | 検索 |
| `iprecepts://study` / `iprecepts://study?id={id}` | ファミリースタディ |
| `iprecepts://hunt` | チャント (`keyword-hunt`/`flyflower`) |
| `iprecepts://handwriting` | 手書き検索 (`handwrite`; iOS) |
| `iprecepts://mastered` | マスタード (`progress`) |
| `iprecepts://categories` / `iprecepts://categories?section=` | ブラウズ |
| `iprecepts://collection?id=` | コレクション / book(zhuxi / zhubailu / yanshi / zhuge / zeng / yuanshi / qian / tingxun / ショートワークス) |
| `iprecepts://corpus` | すべての通路 (`all`) |
| `iprecepts://last-read` | 最後に読んだ項目 |
| `iprecepts://reading-history` | 閲覧履歴 |
| `iprecepts://notes` | ノート |
| `iprecepts://compare` | 並列比較 |
| `iprecepts://theme?id=` | テーマ: |
| `iprecepts://authors` | プロフィール |

## 設定とガイド

| URL | 開く画面 |
|-----|-------|
| `iprecepts://settings` | 設定 |
| `iprecepts://usage-guide` | 使い方ガイド |
| `iprecepts://widget-guide` | ウィジェットガイド |
| `iprecepts://shortcuts-guide` | ショートカットガイド |
| `iprecepts://feature-guide` | オンボーディングの再生 |
| `iprecepts://feedback` | フィードバックメール |
| `iprecepts://in-app-review` | アプリ内／App Store レビュー |

## 例


```
iprecepts://daily
iprecepts://passage?id=1
iprecepts://passage?id=1&card=1
iprecepts://compare
iprecepts://collection?id=yanshi
iprecepts://study
iprecepts://hunt
```


## ノート

- パラメータはIDが数値である場合感度です。
- シリ、ショートカット、ウィジェット、およびコントロールセンターコントロールは、同じディープリンクルートを使用します。
- 最新リストのアプリ内設定 → Help** ガイドを参照してください。


