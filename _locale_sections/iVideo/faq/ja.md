### iVideo はどの動画形式に対応していますか？

iOS/macOS がネイティブにデコードできる形式（MP4、MOV、M4V など）すべてに対応。エクスポートは MP4 または MOV、選択した画質プリセット。

### 動画はどこに保存されますか？

すべて端末ローカル：

- **録画** — App Group 共有コンテナ
- **インポート** — `Documents/ImportedVideos`
- **エクスポート** — `Documents/Exports`

クラウドへのアップロードはありません。

### 4K 編集は可能？

はい。4K の取り込み・編集・エクスポートに対応。Ultra HD (4K) プリセットほか Original、2K、1080p、720p、540p。

### 可変速度は？

**0.05×〜8×**。8 つのプリセット、カスタムスライダー、直近 2 つのカスタム速度、JKL ショートカット、iPhone ではピンチ調整。設定はセッション間で保持し iCloud 同期可。

### JKL ショートカットは？

- **L** — 順再生、連打で 2×→4×→8×
- **J** — 逆再生
- **K** — 一時停止・速度リセット
- **K+J/L** — 0.5× スロー
- **Space** — 再生/一時停止
- **← →** — 1 フレーム、**Shift+← →** 10 秒

JKL HUD と任意の Live Activity（iOS 16.1+）。

### 画面録画は？

- **iOS** — Record タブ → システム **Broadcast Picker** → **iVideo** → **Start Broadcast**。設定で自動スナップショット間隔。
- **macOS** — **ScreenCaptureKit**。初回は **システム設定 → プライバシーとセキュリティ → 画面収録**。

iOS 録画は **実機** が必要（Simulator 不可）。

### Live Activity とは？

JKL 使用時、現在の速度段階をロック画面/Dynamic Island に表示（iOS 16.1+、**設定 → 外観 → Live Activity**、外付けキーボード推奨）。

### 端末間同期は？

iCloud KVS で軽量設定のみ（テーマ、言語、速度、ミュート、カスタム速度履歴、お気に入りツールバー）。**動画ファイル自体は同期しません。**

### Metadata Strip とは？

EXIF、GPS、デバイス情報等の埋め込みメタデータを除去 — 公開共有時のプライバシー向上。

### コラージュの使い方？

ライブラリで 2〜4 本を複数選択 → Collage → レイアウト選択 → 1920×1080 単一動画。長さは最短クリップに合わせ aspect-fill。

### Live Photo / GIF 変換？

Live Photo Studio で双方向変換、バッチ対応。

### 端末内字幕は？

Apple Speech、`requiresOnDeviceRecognition` — 音声アップロードなし。Speech / Sound Events / 複合モード、60+ 言語、SRT/ASS または焼き付け、Apple Translation で二言語行も可。

### 顔ぼかしは？

Vision で全フレーム自動検出、Gaussian/Mosaic、手動矩形でナンバー板等も。すべて端末内。

### バッチ処理は？

複数選択 → Batch Process → レシピ（rotate→speed→mute→watermark→metadata strip→compress 等）を順次実行。

### Edit Projects とは？

**Edit Projects** タブのマルチトラック NLE — クリップ、オーバーレイ、PiP、BGM+ナレーション、Stabilize/Smart Reframe/Slow-Mo/Multicam、Publish Wizard。

### エクスポートキューは？

バックグラウンド直列処理、pending/running/completed/failed、iOS バックグラウンド継続、完了通知（**設定 → Export**）。

### エクスポートプリセットは？

組み込み 4 + カスタム（画質+コンテナ MP4/MOV）。

### カラーグレーディングは？

7 パラメータ、内蔵 LUT 6 種、11 フィルター、`.cube` インポート。

### スピードランプ / ビート同期 / SNS フォーマット？

Speed Ramp、Beat Sync（4 種トランジション）、Social Format（9:16 等）— 各ツールはワークスペースから。

### フィードバックは？

**設定 → About → Feedback** または [AppleOSer@gmail.com](mailto:AppleOSer@gmail.com)。

### iVideo は無料？

無料ダウンロード。任意の Tip Jar あり。
