iHTC Studio (「私たち」、「私たち」、または「私たちの」) は、iPhoto (「愛修图」 / 「愛修圖」としても知られています) を構築しました。このページでは、アプリ使用時のデータに関するポリシーについて説明します。

## 概要

**iPhoto にはアカウントは必要なく、写真を iHTC Studio サーバーにアップロードすることもありません。** キャプチャ、美容、フィルター、エクスポートはデバイス上で実行されます。オプションの **iCloud 同期** は設定のみを対象とし、写真ファイルは対象としません。

## データ収集

当社は、お客様の個人情報を収集するバックエンドを運営しません。

- **アカウントなし** — 登録、電子メール、電話番号は必要ありません。
- **分析や広告なし** — サードパーティの分析、広告、または追跡 SDK はありません。
- **分析用の写真のアップロードはありません** — 顔のランドマークとレンダリングはデバイス上に残ります。

## アプリの仕組み

- **ストレージ** — プロジェクト (オリジナル/サムネイル/編集状態) はアプリのサンドボックス内に存在します。ウィジェットのサムネイルは、アプリ グループ コンテナを使用します。
- **顔の美しさ** — 以下の **顔データとデバイス上の美しさの処理**を参照してください。
- **フォト ライブラリ** — アクセスは、選択したインポートと、開始したオプションのエクスポート保存に制限されます。
- **メタデータ ストリップ** — 必要に応じて、作成したエクスポートから EXIF / GPS / デバイス フィールドを削除します。

## 顔データとデバイス上の美容処理

When you use beauty features (Capture live preview, shutter bake, or the editor Beauty tool), iPhoto analyzes faces **only on your device** using Apple’s Vision framework (`VNDetectFaceLandmarksRequest`). This is **not** face recognition, identity matching, biometrics enrollment, or authentication.

### どのような顔データが処理されるか

- **一時的なランドマーク (メモリのみ):** 顔の境界ボックス、顔の輪郭、目、眉毛、外側/内側の唇、瞳孔、およびオプションの化粧編集 (滑らか、美白、スリム、目、歯、頬紅、口紅) 用のマスクを構築するために使用される関連ジオメトリ。
- **プロジェクトとともに保存 (オプション):** **正規化された顔の境界四角形**と選択した**美しさの強さ/色のパラメータ** (`FaceBeautyEdit`)。これにより、プロジェクトを再度開いたときに顔ごとの設定を復元できます。 **完全なランドマーク座標はディスクに書き込まれません。**

### 使用する

Face geometry is used solely to apply the beauty adjustments **you** enable during capture preview, photo capture, editor preview, thumbnail refresh, and export/share. It is not used for advertising, profiling, or identification.

### 共有

**顔データは第三者と共有されることはありません。** iHTC Studio サーバーやクラウド分析 API にアップロードされることはありません。オプションの iCloud Key-Value 同期では、**環境設定のみ** (言語、テーマ、キャプチャービューティレシピの切り替えなど) が対象となり、**写真や顔のランドマークは同期されません**。

### 保管場所

- 写真とプロジェクト編集ファイル: **デバイス上のアプリ サンドボックス**
- 一時的なランドマーク: **RAM のみ** (エディターを終了するとクリア / 分析キャッシュをクリア)
- ウィジェットのサムネイル: デバイス上のアプリ グループ (ランドマーク データセットではなく、レンダリングされたイメージ)

### 保存と削除

- 一時的なランドマークは処理中にのみ存在し、その後は破棄されます。
- Persisted face boxes and beauty parameters remain **only while you keep the related photo project**.
- プロジェクトを**削除**するか、編集を**リセット**するか、アプリを**アンインストール**して関連する顔のメタデータとローカル写真を削除します。

### 第三者

なし。すべての顔の分析とレンダリングには、デバイス上の Apple Vision と Core Image が使用されます。

## デバイスに保存されているデータ

| データ | どこで | 目的 |
|------|-------|---------|
| 写真プロジェクト | アプリのドキュメント | オリジナル、サム、編集状態 |
| 顔の美しさの編集メタデータ | プロジェクト編集状態（サンドボックス） | 正規化されたフェイスボックス + 美容パラメータのみ |
| 設定 | アプリグループのUserDefaults | 言語、テーマ、キャプチャ/エクスポートのオプション |
| ウィジェットのスナップショット | アプリグループ | 最近のプロジェクト/ウィジェットの統計 |
| 美容レシピをキャプチャー | アプリグループ (オプションで記憶) | 強さと美しさのパラメータ |
| iCloudの設定 | あなたのプライベート iCloud KVS | オプションの設定同期 |

## iCloud同期

Optional sync uses Apple's `NSUbiquitousKeyValueStore` for lightweight preferences (appearance, language, export defaults, capture beauty settings, and similar). **Photo files and face landmarks are not synced.** Sync can be turned off in Settings.

## 権限

| 許可 | 目的 |
|------------|---------|
| カメラ | 「キャプチャ」タブ |
| フォトライブラリー（閲覧） | インポート |
| フォトライブラリ（追加のみ） | オプションで写真にエクスポート |
| マイク | 音声付きビデオを録画する場合のオプションの音声。写真のキャプチャには必要ありません |

## アプリ内購入

オプションの **Tip Developer** は消耗品の StoreKit の購入です。機能のロックが解除されることはなく、別のアプリ アカウントは必要ありません。

## 子供のプライバシー

iPhoto は、故意に子供から個人データを収集しません。コア処理はデバイス上に留まり、iHTC Studio データ収集バックエンドはありません。

## 免責事項

iPhoto は **Apple Inc. とは提携していません**

## 変更点

このページでこのポリシーを更新する場合があります。定期的に見直してください。

## お問い合わせ

- **電子メール:** [AppleOSer@gmail.com](mailto:AppleOSer@gmail.com)
