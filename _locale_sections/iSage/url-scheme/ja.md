iSageは** `isage://` **ショートカットリンク(URLスキーム)をサポートしています。 コールドスタートとホーム画面のショートカットは、統一されたバッファを介して配信されますので、リンクはオンボーディング後2回開いていません。

## リンク形式


```
isage://{host}?{params}
```


## 言葉と著者

| URL | 開く画面 |
|-----|-------|
| `isage://passage?id={id}` | 詳しく見る |
| `isage://saying?id={id}` / `isage://couplet?id={id}` / `isage://poem?id={id}` | 通路と同じ(互換性) |
| `isage://passage?id={id}&card=1` | 細部およびsageカード シートを言うこと |
| `isage://card?id={id}` / `isage://share-card?id={id}` | セージカード |
| `isage://author?id={id}` | 作者の詳細 |
| `isage://recite` / `isage://recite?id={id}` | 誦読フロー |

## ディスカバリー&プラクティス

| URL | 開く画面 |
|-----|-------|
| `isage://home` | ホーム |
| `isage://daily` | 今日の知恵 |
| `isage://random` | ランダム 言う |
| `isage://favorites` | お気に入り |
| `isage://famous` | 名句一覧 |
| `isage://search` / `isage://search?q={query}` | 検索 |
| `isage://study` / `isage://study?id={id}` | セージアカデミー |
| `isage://hunt` | セージハント (`keyword-hunt`/`flyflower`) |
| `isage://handwriting` | 手書き検索 (`handwrite`; iOS) |
| `isage://mastered` | マスタード (`progress`) |
| `isage://categories` / `isage://categories?section=` | ブラウズ |
| `isage://collection?id=guxun` | クラシック・リセンション (`ZH-Shang`/`ZH-Xia`; また`book`/`form`) |
| `isage://corpus` | すべての言葉 (`all`) |
| `isage://theme?id=conduct` | テーマ(例:`cultivation`、`learning`、`friendship`、`household`、`wealth`、`virtue`、`fortune`、`speech`、`loyalty`、`diligence`、`world`) |
| `isage://last-read` | 最後に読んだ項目 |
| `isage://reading-history` | 閲覧履歴 |
| `isage://notes` | ノート |

## 設定とガイド

| URL | 開く画面 |
|-----|-------|
| `isage://settings` | 設定 |
| `isage://usage-guide` | 使い方ガイド |
| `isage://widget-guide` | ウィジェットガイド |
| `isage://shortcuts-guide` | ショートカットガイド |
| `isage://feature-guide` | オンボーディングの再生 |
| `isage://feedback` | フィードバックメール |
| `isage://in-app-review` | アプリ内／App Store レビュー |

## 例


```
isage://daily
isage://passage?id=1
isage://passage?id=1&card=1
isage://collection?id=guxun
isage://theme?id=conduct
isage://study
isage://hunt
isage://handwriting
```


## ノート

- パラメータはIDが数値である場合感度です。
- シリ、ショートカット、ウィジェット、およびコントロールセンターコントロールは、同じディープリンクルートを使用します。
- 最新リストのアプリ内設定 → Help** ガイドを参照してください。


