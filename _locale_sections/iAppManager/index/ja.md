**出荷を速く。ブラウザの迷路から抜け出す。**

iAppManager（爱应用者）は、iPhone、iPad、Mac 向けの **ネイティブ App Store Connect ワークステーション**です。**API Key** でサインインし、資格情報は **Keychain** に保存。Apple と **直接**通信 — バージョン、スクリーンショット、IAP、TestFlight、証明書、売上レポート、カスタマーレビューを一括管理。**iHTC Studio アカウント不要。広告なし。分析 SDK なし。ASC データ用の第三者 backend なし。**

**一覧：** マルチアカウント API Key ログイン · プラットフォーム／パイプライン filter のアプリ一覧 · Overview 準備チェックリスト · バージョンとレビュー提出 · Build Upload REST（IPA/PKG）· クロスロケールコピー付きメタデータ／メディア · Custom Product Pages · In-App Events · App Clips · ストア実験 · フィーチャー提名 · 提供状況と価格 · 年齢制限 · アクセシビリティ · App Tags · IAP／サブスクリプション · Game Center · TestFlight · カスタマーレビュー · 証明書とデバイス · ユーザーとロール · 売上／財務／Analytics レポート · Webhooks · ウィジェットと `iappmanager://` ディープリンク · English／简体／繁體

> 毎週 App Store Connect に住むインディー開発者と小規模チーム向け — タブだらけの Web ではなく、Mac アプリのようなデスク。

## はじめに

1. **App Store Connect API Key** を作成（Admin または App Manager 推奨）：App Store Connect → **Users and Access** → **Integrations** → **App Store Connect API** → キー作成、**`.p8` を一度だけ** ダウンロード、**Issuer ID** + **Key ID** を控える。
2. iAppManager を開く → Issuer ID／Key ID／PEM を貼付（または `.p8` を選択）→ 検証（`GET /v1/apps`）。キーは **このデバイスの Keychain** に保存。
3. 短い **オンボーディング**（証明書 · レポート · ウィジェット · プライバシー）。**設定 → ヘルプ** でいつでも再生。
4. **My Apps** で **リスト／グリッド／カード**、お気に入りピン、**プラットフォーム**（iOS／macOS／tvOS／visionOS）または **ステータス**（販売中 · 非販売 · 待機 · 審査中 · 却下 · 開発者リリース待ち）でフィルタ。
5. アプリを開く → **Overview** から（最新バージョン／ビルド、ショートカット、ソフト準備チェックリスト、最近の提出）。
6. リリース経路：**Versions** → **Build** 添付 → **Metadata／Media** → **Review Detail** → **Review Submissions** で提出（または「今すぐ送信」）。
7. **ホーム画面ウィジェット**（Account Hub、Apps Pulse、Review Desk、Quick Actions）と Shortcuts から `iappmanager://` を試す。

> アプリ内 **Release／IAP／TestFlight／Reports** ガイドはワンタップ（下記ディープリンクも可）。

## ダウンロードする理由

- **出荷全体を一つのネイティブデスク** — バージョン、素材、IAP、TestFlight、証明書、レポートの ASC Web タブ往復をやめる。
- **API Key — 別のパスワード踊りではない** — Issuer ID + Key ID + `.p8` を Keychain；マルチアカウント；アカウント削除でローカルキー削除。
- **Transporter なしでビルドアップロード** — WWDC25 **Build Upload REST**（IPA/PKG）；iOS も同じ API（大容量は **Mac** 推奨）。
- **アプリ内の手厚いガイド** — リリース準備、IAP、TestFlight、レポートで hard／soft チェックを説明。
- **ロック画面でパイプライン** — ウィジェットが My Apps と同じ区分で on-sale／waiting／in-review／rejected／pending-release を表示。
- **アーキテクチャによるプライバシー** — ASC 通信は `api.appstoreconnect.apple.com`；iHTC Studio はアプリ・キー・レポートをホストしない。

## 機能

### サインインとアカウント

- **API Key のみ**（Issuer ID／Key ID／`.p8`）— アプリ内 Apple ID OAuth なし
- Keychain；**マルチアカウント**；サインアウト／削除でローカル秘密鍵削除
- アプリ内 **「API Key の取得方法」** 図解ガイド

### My Apps

- **リスト／グリッド／カード**（既定リスト）と列コントロール
- アカウントごと **ピン**；**プラットフォーム**・**ステータス** filt（約 10 分キャッシュ、強制更新で再スキャン）
- **On sale = 少なくとも 1 地域で提供**；パイプライン区分は storefront とは独立
- コンテキストメニュー：ピン、モジュールへ、名前／Bundle ID／Apple ID／SKU／ストア · ASC · ディープリンク／概要のコピー；App Store または ASC を開く
- アイコン：ASC ビルド artwork → iTunes Lookup → モノグラム、ディスクキャッシュ

### Overview とリリース準備

- 最新バージョン／ビルド、モジュールショートカット、最近のレビュー提出
- **ソフトチェックリスト**（主スクリーンショットサイズ、著作権、年齢制限など）
- Versions／Submissions の **hard blocker**（ビルド状態、必要時デモ資格情報）
- ガイド：`iappmanager://release-guide`

### バージョン、ビルド、提出

- バージョン作成、ビルド添付、提出／キャンセル、リリースモード（手動／自動／スケジュール）、段階的リリース、**Release Now**（開発者リリース待ち時）
- **Build Upload REST**（IPA/PKG）；サイズ；診断；Beta App Clip；輸出コンプライアンス
- **Background Assets**（`.aar`）作成／チャンクアップロード／External Beta と App Store 審査経路
- **暗号化申告**とドキュメントアップロード；Overview からソフトチェック
- **Review Submissions** 下書き／項目追加／提出；「今すぐ」または下書きへ
- **Review Detail** — 連絡先、デモアカウント、メモ、添付、Routing App Coverage

### ストア掲載と成長

- **Metadata** — App Info と Version Listing；カテゴリ、著作権、EULA、プライマリロケール；Android マッピング；★ プライマリのマルチロケール；**クロスロケールコピー**
- **スクリーンショットとプレビュー** — バージョン／ロケール／デバイスサイズ；予約アップロード；クロスロケール；ポスターフレームタイムコード；実アセットによるカバレッジ
- **バッチアセットワークステーション** — ロケール×サイズ一括アップロード
- **ダウンロードサイズワークベンチ** — ソフト上限ヒント付きサイズ確認
- My Apps の **SKU 検索**；狭い画面の適応型アクションバー
- **Custom Product Pages** — 可視性、ディープリンク、プロモ、Search Keywords、メディア、提出
- **In-App Events**、**App Clips**、**ストア実験**（トラフィックは審査と分離）、**フィーチャー提名**
- **Availability**、**pricing**（価格ポイント選択と適用、均等化プレビュー含む）、**年齢制限**、**アクセシビリティ**、**App Tags**
- Mac では **⌘S** 保存

### 収益化と Game Center

- IAP／サブスクリプショングループ、ローカライズ、レビュー用スクショ／メモ、地域提供、価格ポイント
- 紹介／プロモ／ウィンバック；**Offer Codes**；プロモ画像；猶予期間；サーバー通知 URL；CSV 入出力；提出（サブスクリプショングループ含む）
- ガイド：`iappmanager://iap-guide`
- **Game Center** — 実績、リーダーボード／セット、チャレンジ／アクティビティ、マルチプレイ、マッチメイキング

### TestFlight

- グループ、公開リンク、募集条件、メトリクス、招待、個人テスター、ビルド、What to Test、ベータライセンス／レビュー
- フィードバック受信箱と CSV + **フルサイズスクショ／クラッシュログ一括エクスポート**（Mac フォルダ／iOS zip + manifest）
- ガイド：`iappmanager://testflight-guide`

### 証明書、ユーザー、レポート、レビュー

- 証明書（アプリ内 CSR／インポート）· プロファイル · Bundle ID と Capabilities · Merchant／Pass Type · デバイス（**macOS** で Keychain インストール）
- ユーザー招待、ロール、アプリ可視性、プロビジョニング；Sandbox テスター
- **Reports** — 売上／財務／Analytics、シナリオ、カスタムプリセット、**ワイド TSV プレビュー**（列切替、検索、全画面横向き）と**軽量サマリーチャート**；`iappmanager://reports-guide`
- カスタマーレビュー — filt、検索、返信／削除、**返信テンプレート**（アカウント最大 20）
- **Webhooks** — 作成／編集／ping／配信（公開コールバックはホストしない）

### ウィジェット、ショートカット、仕上げ

- ウィジェット：**Account Hub**、**Apps Pulse**（S/M/L）、**Review Desk**、**Quick Actions**
- `iappmanager://` + App Intents — [Shortcut Links](url-scheme)
- 外観、アクセント、EN／简／繁（ナビを失わずホットスワップ）
- iOS **代替アイコン**（IconStyle1–7）；StoreKit チップ；フィードバックメール

### プライバシー

- API 秘密鍵は **デバイス Keychain**；業務 API は **Apple** のみ
- iTunes Lookup による任意アイコン；Settings でサムネキャッシュ削除
- App Group は **ローカル** ウィジェットスナップショットのみ — iHTC Studio にアップロードしない
- 詳細：[Privacy Policy](privacy)

## アプリを入手

| チャンネル | リンク |
|---------|------|
| App Store | [Download on the App Store](https://apps.apple.com/app/id6794497110) |

## システム要件

| コンポーネント | 最小 |
|-----------|---------|
| iPhone / iPad | iOS 17.0+ |
| Mac | macOS 14.0+ |
| ウィジェット | iOS 17.0+ |
| 大容量 IPA | **Mac** 推奨 |

## お問い合わせ

- **Email:** [AppleOSer@gmail.com](mailto:AppleOSer@gmail.com)

通常 48 時間以内に返信します。

[FAQ](faq) · [Shortcut Links](url-scheme) · [Privacy Policy](privacy)
