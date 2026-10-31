iPhotoは** `iphoto://` **ディープリンクと**アプリのインテント/シリショートカット**をサポートしています。 リンクはアプリ内を移動するだけなので、データをアップロードしません。

## スキーム


```
iphoto://<host>[?query]
```


| Rule | 詳細を見る |
|------|--------|
| Scheme | ライフォト |
| Empty | アプリのデフォルトタブを開きます |
| Unknown hosts | 安全に無視 |

---

## タブとナビゲーション

| URL | 開く画面 |
|-----|-------|
| `iphoto://library` | ライブラリタブ |
| `iphoto://capture` | キャプチャタブ |
| `iphoto://settings` | 設定タブ |
| `iphoto://search` | 検索タブ (iOS 18 +) |
| `iphoto://recent-projects` | 最近の仕事に焦点を当てた図書館 |

---

## ダウンロード

| URL | 開く画面 |
|-----|-------|
| `iphoto://editor?id=<projectID>` | 指定したプロジェクト ID のエディタ |

---

## ガイド&アクション

| URL | 開く画面 |
|-----|-------|
| `iphoto://usage-guide` | 使い方ガイド |
| `iphoto://widget-guide` | ウィジェットガイド |
| `iphoto://shortcuts-guide` | ショートカットガイド |
| `iphoto://feature-guide` | 特徴/転写再生 |
| `iphoto://export-presets` | 輸出関連の設定 |
| `iphoto://feedback` | フィードバックメール |
| `iphoto://in-app-review` | アプリ内レビュー プロンプト |

---

## シリとショートカット

作り付けの意図は下記のものを含んでいます:

- オープンキャプチャ
- オープンライブラリー
- インポート写真
- 設定を開く

Shortcuts アプリで追加するか、ショートカットに示すフレーズを使用して Siri で呼び出す。

## 例


```
iphoto://capture
iphoto://library
iphoto://editor?id=YOUR-PROJECT-ID
iphoto://widget-guide
```


[FAQ](../faq)・[プライバシーポリシー](../privacy)・[iPhotoに戻る](./)


