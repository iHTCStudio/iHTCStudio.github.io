### iAppManager とは？

iPhone、iPad、Mac 向けの **ネイティブ App Store Connect ワークステーション**です。**API Key** でサインインし、バージョン、スクリーンショット、IAP、TestFlight、証明書、レポート、レビューを管理します。通信は **Apple に直接**。iHTC Studio アカウントは不要です。

### API Key の取得方法は？

1. [App Store Connect](https://appstoreconnect.apple.com) を開く → **Users and Access** → **Integrations** → **App Store Connect API**
2. キーを作成（Admin または App Manager を推奨）
3. `.p8` を **一度だけ** ダウンロードし、**Issuer ID** と **Key ID** を控える
4. iAppManager に貼り付ける（またはファイルを選択）。アプリ内ガイドがスクリーンショット付きで案内します。

### `.p8` は iHTC Studio にアップロードされますか？

**いいえ。** 秘密鍵は **デバイスの Keychain** にのみ保存されます。リクエストはローカルで署名され、`api.appstoreconnect.apple.com` に送信されます。アカウントを削除するとローカルキーも削除されます。

### アプリ内で Apple ID のパスワードは必要ですか？

**不要です。** 認証は **API Key のみ**（Issuer ID + Key ID + `.p8`）です。公開 API がない機能（プライバシー栄養表示ラベル、無料 App プロモコードなど）は Safari/ASC で Apple ID を使います——アプリは Apple のサイトを開きます。

### Transporter なしで IPA / PKG をアップロードできますか？

**はい。** iAppManager は Apple の **Build Upload REST**（WWDC25）を使用します。大容量ファイルは **Mac** を推奨。iOS も同じ API ですが、大きなアップロードは向きません。

### フィルター / ウィジェットの「on sale」とは？

**少なくとも 1 つの App Store 地域で配信可能**という意味です。パイプライン（waiting / in review / rejected / pending developer release）は別途追跡します。ウィジェット **Needs attention** = waiting + in review + rejected + pending release（ローカル合計、ASC フィールドではありません）。

### 提出前の hard / soft チェックとは？

**Hard blockers** は提出を止めます（例：ビルド未準備、デモアカウント必須だが未入力）。**Soft checks** は警告（主スクリーンショットサイズ、著作権、年齢制限など）で、確認後に続行できます。Overview / Versions / Submissions の `?` または `iappmanager://release-guide` を参照。

### 対応言語は？

**English · 简体中文 · 繁體中文**。システムに従うか、設定で固定。言語のホットスワップはルートを **再マウントせず**（ナビゲーションと下書きを保持）。

### ウィジェットが ASC のライブ数値を表示しないのはなぜ？

ウィジェットは **ASC を呼び出しません**。メインアプリがスキャンしスナップショットを書き込みます（約 10 分 TTL、My Apps と同じ区分）。アプリを開きリストを更新（またはステータスを強制更新）してください。

### macOS と iOS の違いは？

両方ともストア、マネタイズ、TestFlight、Game Center、ユーザー、レポート、レビュー、Webhooks をカバー。**大容量 IPA** と証明書のシステム Keychain へのインストールは **Mac** を推奨。代替アプリアイコンは **iOS のみ**。

### App Store Connect 用のプライバシーポリシー URL は？

本サイトの [Privacy Policy](../privacy) を開き、ブラウザのアドレスバーから URL をコピーしてください。

### システム要件は？

iPhone / iPad **iOS 17.0+**、Mac **macOS 14.0+**。

### サポートへの連絡方法は？

[AppleOSer@gmail.com](mailto:AppleOSer@gmail.com) — 通常 48 時間以内に返信します。
