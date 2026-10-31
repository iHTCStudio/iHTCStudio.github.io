iStore は、** `istore://` ** ショートカットリンクをサポートしています。 **ショートカット**、Safariブックマーク、または**ウィジェット**、**コントロールセンター**、**Spotlight**、**共有エクステンション**で領域**を切り替える**、**最後の領域を再スイッチ**、**タブを開く**、または**ガイドへの**ジャンプ**。

## リンク形式


```
istore://{host}?{params}
```


ホストは**case-inpathy**です。 地域コードは標準 **Alpha-2** 値 ( `istore://` 、 `us` 、 `cn` 、 `jp` 、 `hk` 、...) を使用します。

| What you want | サイトマップ |
|---------------|------|
| Switch to a region | 「istore://switch?region={code}`」の |
| Switch to your last region | 「istore://switch-last」の一覧 |
| Open the Store / Favorites / Settings tab | 「istore://store」・「istore://favorites」・「istore://settings」 |
| Open App Availability | 「istore/アベイラビリティ」 |

---

## 地域への切り替え

指定した地域への切り替えをリクエスト(有効化した場合、アプリ内確認を通過)。


```
istore://switch?region={code}
```


| Parameter | Required | コンテンツ |
|-----------|----------|-------------|
| `region` | **Yes** | 地域コード、例えば `us`、`cn`、`jp`、`hk`、`tw` |

**例**


```
istore://switch?region=us
```


によって使用される:**インタラクティブウィジェット**、**Spotlight**結果、**ショートカット/Siri**。

---

## 最後の地域への切り替え


```
istore://switch-last
```


最近のスイッチターゲットを読んで、スイッチをもう一度読みます。 **スイッチLast**コントロールセンターコントロール(iOS 18 +)とマッチングショートカット/シリアクション。

---

## タブとページ(クエリなし)

| URL | 開く画面 |
|-----|-------|
| `istore://store` | ストアタブ |
| `istore://favorites` | お気に入りタブ |
| `istore://settings` | 設定タブ |
| `istore://availability` | 設定→アプリの可用性(また、共有延長によって使用される) |
| `istore://switch-history` | スイッチ履歴 |
| `istore://quick-regions` | クイックエリアの設定 |
| `istore://feature-guide` | 機能ガイド |
| `istore://widget-guide` | ウィジェットガイド |
| `istore://shortcuts-guide` | ショートカットガイド |
| `istore://usage-guide` | 使い方ガイド |
| `istore://feedback` | フィードバックメール |
| `istore://in-app-review` | アプリ内 App Store 評価 |

---

## ウィジェット、コントロールセンター、スポットライト

をタップすると、自動的に `istore://` が生成されます。

| Source | Tap target | エフェクト |
|--------|------------|--------|
| **Quick Regions / Recent / Custom widget** | A region tile | 「istore://switch?region=...」 |
| **Switch Last control** (iOS 18+) | The control | 「istore://switch-last」の一覧 |
| **Spotlight** | A region result | 「istore://switch?region=...」 |

ウィジェットとコントロールセンターからのインタラクティブな切り替えは、公式のApp Storeリダイレクトを完了するためにアプリを開きます。

---

## シェアエクステンション

任意の**App Storeリンク**をiStoreに共有します。 共有エクステンションは、一般的な領域で空室状況をチェックし、 `istore://` でアプリを開くことができますので、結果を確認し、切り替えることができます。

---

## シリとショートカット

**ショートカット**アプリでビルトインアクションを検索するか、**Siri**を尋ねます。 タイトルとフレーズは、英語 / 日本語 / 繁體中文

| Action | What you can set | エフェクト |
|--------|------------------|--------|
| Switch region | Region | その地域への切り替え |
| Switch last region | — | 最後のターゲットに切り替える |
| Switch favorite region | A favorite | お気に入りの地域への切り替え |
| Open store | — | iStoreを開く |
| Check availability | App link or ID | アプリが利用可能なチェック |

---

## リンクの地域コード

ディープリンクとウィジェット生成された URL は、常に安定した **region コード** ( `istore://` , `us` , `cn` , `jp` , ...) — ローカル表示名ではありません。

**例**


```
istore://switch?region=jp
istore://switch?region=hk
```


[概要に戻る](...)・[FAQ](../faq)・[プライバシーポリシー](../privacy)


