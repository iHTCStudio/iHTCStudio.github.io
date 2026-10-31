---
layout: doc
title: iCangJie — Privacy Policy
app_id: iCangJie
doc_title_en: Privacy Policy
doc_title_zh_cn: 隐私政策
doc_title_zh_tw: 隱私政策
description: Privacy policy for iCangJie.
---

<section lang="en" markdown="1">

iHTC Studio ("we", "us" or "our") built iCangJie (also known as "爱仓颉" / "愛倉頡"). This page describes our policies regarding data collection, use and disclosure when you use our app.

## Summary

**iCangJie does not collect, store or transmit any personal data.** All character lookups, quizzes, typing practice and learning progress are processed entirely on your device. No account is required, and no internet connection is needed for any core feature.

## Data Collection

We do not collect any data. Specifically:

- **No personal information** is collected (no name, email, phone number or account).
- **No usage data** or analytics are collected.
- **No third-party SDKs** for advertising, analytics or crash reporting are integrated.
- **No cookies or tracking** technologies are used.

## iCloud Sync

iCangJie offers an optional iCloud sync feature (toggleable in Settings). When enabled, the following data is synced via **iCloud Key-Value Storage (iCloud KVS)**, a service provided and managed entirely by Apple:

| Synced Data | Purpose |
|-------------|---------|
| Favorites | Your bookmarked characters |
| Learning status | Progress level for each character |
| Wrong question book | Incorrectly answered quiz questions |
| Quiz scores & streak | Your daily quiz performance |
| Typing statistics | Accuracy, streak, and session counts from typing practice |
| Daily typing records | Per-day character counts and code-length histograms (~120 days) |
| Built-in passage progress | Resume position in built-in typing passages |

This data is transmitted directly between your devices through Apple's iCloud infrastructure. iHTC Studio does not operate any server and has no access to your iCloud data. Apple's handling of iCloud data is governed by [Apple's Privacy Policy](https://www.apple.com/privacy/).

You can disable iCloud sync at any time in Settings. When disabled, all data stays local to each device.

Typing UI preferences (wrong-key retention, passage pinyin) are stored locally on each device and are **not** synced via iCloud.

## Data Stored Locally on Your Device

All data created by iCangJie stays on your device:

| Data | Storage | User Control |
|------|---------|--------------|
| Favorites | Local (UserDefaults / App Group) | Remove individual items or clear all in app |
| Learning status | Local (UserDefaults) | Reset in app settings |
| Wrong question book | Local (UserDefaults) | Clear in app |
| Quiz scores & streak | Local (UserDefaults) | Reset in app settings |
| Typing statistics & daily records | Local (UserDefaults / App Group); optional iCloud KVS | Cleared when learning data is reset |
| Passage progress | Local (UserDefaults / App Group); optional iCloud KVS | Cleared when learning data is reset |
| Typing UI preferences | Local (UserDefaults) | Change in Settings → Typing |
| Onboarding & newcomer path flags | Local (UserDefaults) | Shown again only if you reset app data |
| Quiz preferences | Local (UserDefaults) | Change in quiz settings |
| Spotlight indexing preference | Local (UserDefaults) | Toggle in Settings → Home shortcuts |
| App preferences & theme | Local (UserDefaults) | Reset by deleting the app |

Widgets use an **App Group** container to share data between the main app and widget extensions. This container stays on your device and is not accessible to any third party.

### JSON Backup (user-initiated)

You may **export** a JSON backup file (`.icangjie-backup`) containing learning data. The file is written to a location **you choose** (Files, AirDrop, etc.). **Import** reads a file you select. iHTC Studio does not upload, host, or access backup files.

### Spotlight Indexing (iOS, optional)

When enabled, iCangJie indexes up to **80** favorite and recent characters into the **on-device** iOS Spotlight index (domain `com.iHTCboy.iCangJie.words`). Entries expire after 30 days. This data never leaves your device except through Apple's Spotlight system on your iPhone/iPad. Disable anytime in Settings.

## Permissions

iCangJie requests **only one optional permission**:

| Permission | When requested | Purpose |
|------------|----------------|---------|
| **Photo Library (Add Only)** | When you tap **Save to Photos** on a radical chart image in a tutorial | Save the image to your photo library |

iCangJie does **not** read your existing photos. There is no access to your camera, microphone, contacts, location, or local network for core features.

Optional features that open external websites (Youdao online lookup, tutorial links) use the system browser and do not grant iCangJie access to your browsing history.

## Children's Privacy

iCangJie does not knowingly collect any personal data from anyone, including children under 13. Since no data is collected at all, no special provisions are required.

## Changes to This Policy

We may update this Privacy Policy from time to time. Any changes will be posted on this page with an updated date. We encourage you to review this page periodically.

## Contact Us

If you have any questions about this Privacy Policy, please contact us:

- **Email:** [AppleOSer@gmail.com](mailto:AppleOSer@gmail.com)

</section>
<section lang="zh-CN" markdown="1">

爱火腿肠工作室（iHTC Studio）（「我们」）为爱仓颉（iCangJie，亦称「愛倉頡」）这款应用开发并维护本页面，以告知你在使用应用过程中，我们关于数据收集、使用与披露的政策。

## 概要

**爱仓颉不收集、存储或传输任何个人数据。** 所有查字、测验、打字练习与学习进度完全在你的设备上处理。无需账号，所有核心功能也无需联网。

## 数据收集

我们不收集任何数据。具体而言：

- **不收集任何个人信息**（无姓名、邮箱、电话或账号）。
- **不收集使用数据**或统计分析。
- **不集成任何第三方 SDK**用于广告、统计或崩溃上报。
- **不使用 Cookie 或追踪**技术。

## iCloud 同步

爱仓颉提供可选的 iCloud 同步功能（可在设置中开关）。启用后，以下数据通过 **iCloud 键值存储（iCloud KVS）** 同步，该服务完全由 Apple 提供和管理：

| 同步数据 | 用途 |
|-------------|---------|
| 收藏夹 | 你收藏的汉字 |
| 学习状态 | 每个汉字的学习进度等级 |
| 错题本 | 测验中答错的题目 |
| 测验成绩与连胜 | 每日测验表现 |
| 打字统计 | 打字练习的准确率、连胜与场次 |
| 按日打字记录 | 每日字数与码长直方图（约 120 天） |
| 内置文章进度 | 内置打字文章的续练位置 |

这些数据通过 Apple 的 iCloud 基础架构在你的设备之间直接传输。iHTC Studio 不运营任何服务器，也无法访问你的 iCloud 数据。Apple 对 iCloud 数据的处理受 [Apple 隐私政策](https://www.apple.com/privacy/) 约束。

你可以随时在设置中关闭 iCloud 同步。关闭后，所有数据仅保留在各设备本地。

打字界面偏好（错键保留、篇章拼音）仅保存在各设备本地，**不会**通过 iCloud 同步。

## 设备本地存储的数据

爱仓颉创建的所有数据都留在你的设备上：

| 数据 | 存储位置 | 用户控制 |
|------|---------|--------------|
| 收藏夹 | 本地（UserDefaults / App Group）| 在应用中移除单个项目或清空全部 |
| 学习状态 | 本地（UserDefaults）| 在应用设置中重置 |
| 错题本 | 本地（UserDefaults）| 在应用中清除 |
| 测验成绩与连胜 | 本地（UserDefaults）| 在应用设置中重置 |
| 打字统计与按日记录 | 本地（UserDefaults / App Group）；可选 iCloud KVS | 重置学习数据时清除 |
| 篇章进度 | 本地；可选 iCloud KVS | 重置学习数据时清除 |
| 打字界面偏好 | 本地（UserDefaults）| 在设置 → 打字练习中修改 |
| 引导与测验偏好 | 本地（UserDefaults）| 删除应用重置 |
| Spotlight 开关 | 本地（UserDefaults）| 设置 → 主屏快捷操作 |
| 应用偏好与主题 | 本地（UserDefaults）| 删除应用即可重置 |

小组件使用 **App Group** 容器在主应用与小组件扩展之间共享数据。该容器留在你的设备上，第三方无法访问。

### JSON 备份（用户主动操作）

你可 **导出** `.icangjie-backup` JSON 文件到自选位置（文件、隔空投送等），也可 **导入** 自选文件。我们不会上传或访问备份内容。

### Spotlight 索引（iOS，可选）

开启后，最多 **80** 个收藏与最近浏览汉字写入本机 Spotlight 索引，30 天过期。仅在本机 Spotlight 使用，可随时在设置中关闭。

## 权限

爱仓颉**仅请求一项可选权限**：

| 权限 | 何时请求 | 用途 |
|------|----------|------|
| **相册（仅添加）** | 在教程字根图点击 **保存到相册** 时 | 将图片保存到你的相册 |

爱仓颉**不会**读取你已有的照片。不访问相机、麦克风、通讯录、位置或本地网络（核心功能）。

可选的在线查词（有道）与教程外链通过系统浏览器打开，爱仓颉无法访问你的浏览记录。

## 儿童隐私

爱仓颉不会有意收集任何人（包括 13 岁以下儿童）的个人数据。因为我们完全不收集数据，所以无需特别条款。

## 政策变更

我们可能不时更新本隐私政策。任何变更都会更新本页并标注日期。建议你定期回访。

## 联系我们

如果你对本隐私政策有任何疑问，请联系：

- **邮箱：** [AppleOSer@gmail.com](mailto:AppleOSer@gmail.com)

</section>
<section lang="zh-TW" markdown="1">

愛火腿腸工作室（iHTC Studio）（「我們」）為愛倉頡（iCangJie）這款應用開發並維護本頁面，以告知你在使用應用過程中，我們關於資料收集、使用與揭露的政策。

## 概要

**愛倉頡不收集、儲存或傳送任何個人資料。** 所有查字、測驗、打字練習與學習進度完全在你的裝置上處理。無需帳號，所有核心功能也無需連網。

## 資料收集

我們不收集任何資料。具體而言：

- **不收集任何個人資訊**（無姓名、電子郵件、電話或帳號）。
- **不收集使用資料**或統計分析。
- **不整合任何第三方 SDK**用於廣告、統計或當機回報。
- **不使用 Cookie 或追蹤**技術。

## iCloud 同步

愛倉頡提供可選的 iCloud 同步功能（可在設定中開關）。啟用後，以下資料透過 **iCloud 鍵值儲存（iCloud KVS）** 同步：

| 同步資料 | 用途 |
|-------------|---------|
| 收藏夾 | 你收藏的漢字 |
| 學習狀態 | 每個漢字的學習進度等級 |
| 錯題本 | 測驗中答錯的題目 |
| 測驗成績與連勝 | 每日測驗表現 |
| 打字統計 | 打字練習的準確率、連勝與場次 |
| 按日打字記錄 | 每日字數與碼長直方圖（約 120 天） |
| 內建文章進度 | 內建打字文章的續練位置 |

這些資料透過 Apple 的 iCloud 基礎架構在你的裝置之間直接傳輸。iHTC Studio 不營運任何伺服器，也無法存取你的 iCloud 資料。

## 裝置本地儲存的資料

愛倉頡建立的所有資料都留在你的裝置上，可透過應用內設定清除或重置。

### JSON 備份

由你主動匯出/匯入 `.icangjie-backup` 檔案；我們不會上傳或存取。

### Spotlight 索引（iOS）

可選；最多 80 字寫入本機 Spotlight，可隨時關閉。

## 權限

愛倉頡**僅請求一項可選權限**：

| 權限 | 何時請求 | 用途 |
|------|----------|------|
| **相簿（僅新增）** | 在教程字根圖點擊 **儲存到相簿** 時 | 將圖片儲存到你的相簿 |

愛倉頡**不會**讀取你已有的照片。不存取相機、麥克風、通訊錄、位置或區域網路（核心功能）。

## 兒童隱私

愛倉頡不會有意收集任何人（包括 13 歲以下兒童）的個人資料。

## 政策變更

我們可能不時更新本隱私政策。任何變更都會更新本頁並標註日期。

## 聯絡我們

如果你對本隱私政策有任何疑問，請聯絡：

- **電子郵件：** [AppleOSer@gmail.com](mailto:AppleOSer@gmail.com)

</section>
<section lang="ja" markdown="1">

iHTC Studio（以下「当社」）は、iCangJie（「爱仓颉」/「愛倉頡」とも呼ばれます）を開発しました。このページでは、本アプリのご利用時におけるデータの収集、利用、開示に関する方針を説明します。

## 概要

**iCangJie は、個人データを収集、保存、送信することは一切ありません。** 文字の検索、クイズ、タイピング練習、学習の進捗はすべて端末上だけで処理されます。アカウントは不要で、主要機能にインターネット接続は必要ありません。

## データ収集について

当社はデータを一切収集しません。具体的には次のとおりです。

- **個人情報は収集されません**（氏名、メールアドレス、電話番号、アカウントなし）。
- **利用データや分析データは収集されません。**
- 広告、分析、クラッシュレポート向けの**サードパーティ SDK は組み込まれていません。**
- **Cookie やトラッキング技術は使用しません。**

## iCloud 同期

iCangJie には、任意の iCloud 同期機能があります（設定で切り替え可能）。有効にすると、次のデータが、Apple が提供・管理するサービスである **iCloud キーバリューストレージ（iCloud KVS）** を通じて同期されます。

| 同期されるデータ | 目的 |
|-------------|---------|
| お気に入り | ブックマークした文字 |
| 学習状況 | 各文字の進捗レベル |
| 間違い帳 | クイズで間違えた問題 |
| クイズのスコアと連続記録 | デイリークイズの成績 |
| タイピング統計 | タイピング練習の正答率、連続記録、セッション数 |
| 日別タイピング記録 | 1 日ごとの文字数とコード長のヒストグラム（約 120 日分） |
| 内蔵文章の進捗 | 内蔵タイピング文章の再開位置 |

このデータは、Apple の iCloud インフラを通じて、お客様のデバイス間で直接送信されます。iHTC Studio はサーバーを運用しておらず、お客様の iCloud データにアクセスすることはできません。iCloud データの取り扱いには [Apple のプライバシーポリシー](https://www.apple.com/privacy/)が適用されます。

iCloud 同期は、設定でいつでも無効にできます。無効にすると、すべてのデータは各デバイスのローカルにとどまります。

タイピング UI の設定（ミスキーの保持、文章のピンイン）は各デバイスにローカルで保存され、iCloud では同期されません。

## 端末内に保存されるデータ

iCangJie が作成するデータはすべて端末内にとどまります。

| データ | 保存場所 | ユーザーによる管理 |
|------|---------|--------------|
| お気に入り | ローカル（UserDefaults / App Group） | アプリ内で個別に削除、またはすべて消去 |
| 学習状況 | ローカル（UserDefaults） | アプリの設定でリセット |
| 間違い帳 | ローカル（UserDefaults） | アプリ内で消去 |
| クイズのスコアと連続記録 | ローカル（UserDefaults） | アプリの設定でリセット |
| タイピング統計と日別記録 | ローカル（UserDefaults / App Group）、任意で iCloud KVS | 学習データのリセット時に消去 |
| 文章の進捗 | ローカル（UserDefaults / App Group）、任意で iCloud KVS | 学習データのリセット時に消去 |
| タイピング UI の設定 | ローカル（UserDefaults） | 設定 → タイピングで変更 |
| オンボーディングと初心者向けパスのフラグ | ローカル（UserDefaults） | アプリのデータをリセットした場合のみ再表示 |
| クイズの設定 | ローカル（UserDefaults） | クイズ設定で変更 |
| Spotlight インデックスの設定 | ローカル（UserDefaults） | 設定 → ホーム画面ショートカットで切り替え |
| アプリの設定とテーマ | ローカル（UserDefaults） | アプリを削除してリセット |

ウィジェットは、メインアプリとウィジェット機能拡張の間でデータを共有するために **App Group** コンテナを使用します。このコンテナは端末内にとどまり、第三者がアクセスすることはできません。

### JSON バックアップ（ユーザー操作による）

学習データを含む JSON バックアップファイル（`.icangjie-backup`）を**書き出す**ことができます。ファイルは**お客様が選んだ場所**（ファイル、AirDrop など）に書き込まれます。**読み込み**では、お客様が選択したファイルを読み取ります。iHTC Studio がバックアップファイルをアップロード、ホスト、またはアクセスすることはありません。

### Spotlight インデックス（iOS、任意）

有効にすると、iCangJie はお気に入りと最近の文字を最大 **80** 件、**端末内**の iOS Spotlight インデックス（ドメイン `com.iHTCboy.iCangJie.words`）に登録します。エントリーは 30 日後に失効します。このデータは、iPhone / iPad 上の Apple の Spotlight システムを除き、端末の外に出ることはありません。設定でいつでも無効にできます。

## 権限

iCangJie が要求する権限は**任意の 1 つだけ**です。

| 権限 | 要求されるタイミング | 目的 |
|------------|----------------|---------|
| **写真ライブラリ（追加のみ）** | チュートリアル内の字根図の画像で**写真に保存**をタップしたとき | 画像を写真ライブラリに保存するため |

iCangJie は、既存の写真を読み取ることは**ありません**。主要機能では、カメラ、マイク、連絡先、位置情報、ローカルネットワークにはアクセスしません。

外部ウェブサイトを開く任意の機能（有道のオンライン検索、チュートリアルのリンク）はシステムのブラウザを使用し、iCangJie に閲覧履歴へのアクセス権を与えることはありません。

## お子様のプライバシー

iCangJie は、13 歳未満のお子様を含め、誰からも個人データを意図的に収集することはありません。データをまったく収集しないため、特別な措置は必要ありません。

## 本ポリシーの変更

当社は、本プライバシーポリシーを随時更新することがあります。変更は更新日とともにこのページに掲載します。定期的にこのページをご確認いただくことをお勧めします。

## お問い合わせ

本プライバシーポリシーについてご質問がある場合は、次の連絡先までご連絡ください。

- **メール：** [AppleOSer@gmail.com](mailto:AppleOSer@gmail.com)

</section>
<section lang="ko" markdown="1">

iHTC Studio("당사")는 iCangJie("爱仓颉" / "愛倉頡"로도 알려져 있음)를 만들었습니다. 이 페이지는 앱 사용 시 데이터 수집, 이용 및 공개에 관한 당사의 방침을 설명합니다.

## 요약

**iCangJie는 어떤 개인 데이터도 수집, 저장 또는 전송하지 않습니다.** 모든 글자 조회, 퀴즈, 타이핑 연습, 학습 진행 상황은 전적으로 기기에서 처리됩니다. 계정이 필요 없으며, 핵심 기능에는 인터넷 연결이 필요하지 않습니다.

## 데이터 수집

당사는 어떤 데이터도 수집하지 않습니다. 구체적으로 다음과 같습니다.

- **개인정보를 수집하지 않습니다**(이름, 이메일, 전화번호, 계정 없음).
- **사용 데이터나 분석 데이터를 수집하지 않습니다.**
- 광고, 분석, 충돌 보고용 **서드파티 SDK가 통합되어 있지 않습니다.**
- **쿠키나 추적 기술을 사용하지 않습니다.**

## iCloud 동기화

iCangJie는 선택적 iCloud 동기화 기능을 제공합니다(설정에서 전환 가능). 켜면 다음 데이터가 Apple이 전적으로 제공하고 관리하는 서비스인 **iCloud 키-값 저장소(iCloud KVS)**를 통해 동기화됩니다.

| 동기화되는 데이터 | 목적 |
|-------------|---------|
| 즐겨찾기 | 북마크한 글자 |
| 학습 상태 | 각 글자의 진행 단계 |
| 오답 노트 | 퀴즈에서 틀린 문제 |
| 퀴즈 점수 및 연속 기록 | 일일 퀴즈 성적 |
| 타이핑 통계 | 타이핑 연습의 정확도, 연속 기록, 세션 수 |
| 일별 타이핑 기록 | 하루별 글자 수와 코드 길이 히스토그램(약 120일) |
| 내장 글 진행 상황 | 내장 타이핑 글의 이어하기 위치 |

이 데이터는 Apple의 iCloud 인프라를 통해 기기 간에 직접 전송됩니다. iHTC Studio는 서버를 운영하지 않으며 사용자의 iCloud 데이터에 접근할 수 없습니다. iCloud 데이터의 처리에는 [Apple 개인정보 보호 정책](https://www.apple.com/privacy/)이 적용됩니다.

설정에서 언제든 iCloud 동기화를 끌 수 있습니다. 끄면 모든 데이터는 각 기기에 로컬로 남습니다.

타이핑 UI 환경설정(오타 키 유지, 글 병음)은 각 기기에 로컬로 저장되며 iCloud로 동기화되지 **않습니다**.

## 기기에 로컬로 저장되는 데이터

iCangJie가 만드는 모든 데이터는 기기에 남습니다.

| 데이터 | 저장 위치 | 사용자 제어 |
|------|---------|--------------|
| 즐겨찾기 | 로컬(UserDefaults / App Group) | 앱에서 개별 삭제 또는 전체 지우기 |
| 학습 상태 | 로컬(UserDefaults) | 앱 설정에서 초기화 |
| 오답 노트 | 로컬(UserDefaults) | 앱에서 지우기 |
| 퀴즈 점수 및 연속 기록 | 로컬(UserDefaults) | 앱 설정에서 초기화 |
| 타이핑 통계 및 일별 기록 | 로컬(UserDefaults / App Group), 선택적으로 iCloud KVS | 학습 데이터 초기화 시 삭제 |
| 글 진행 상황 | 로컬(UserDefaults / App Group), 선택적으로 iCloud KVS | 학습 데이터 초기화 시 삭제 |
| 타이핑 UI 환경설정 | 로컬(UserDefaults) | 설정 → 타이핑에서 변경 |
| 온보딩 및 초보자 경로 플래그 | 로컬(UserDefaults) | 앱 데이터를 초기화한 경우에만 다시 표시 |
| 퀴즈 환경설정 | 로컬(UserDefaults) | 퀴즈 설정에서 변경 |
| Spotlight 색인 환경설정 | 로컬(UserDefaults) | 설정 → 홈 화면 단축 항목에서 전환 |
| 앱 환경설정 및 테마 | 로컬(UserDefaults) | 앱을 삭제해 초기화 |

위젯은 메인 앱과 위젯 확장 간에 데이터를 공유하기 위해 **App Group** 컨테이너를 사용합니다. 이 컨테이너는 기기에 남으며 어떤 제3자도 접근할 수 없습니다.

### JSON 백업(사용자가 직접 실행)

학습 데이터가 담긴 JSON 백업 파일(`.icangjie-backup`)을 **내보낼** 수 있습니다. 파일은 **사용자가 선택한 위치**(파일, AirDrop 등)에 저장됩니다. **가져오기**는 사용자가 선택한 파일을 읽습니다. iHTC Studio는 백업 파일을 업로드, 호스팅하거나 접근하지 않습니다.

### Spotlight 색인(iOS, 선택 사항)

켜면 iCangJie는 즐겨찾기와 최근 글자를 최대 **80**개까지 **기기 내** iOS Spotlight 색인(도메인 `com.iHTCboy.iCangJie.words`)에 등록합니다. 항목은 30일 후 만료됩니다. 이 데이터는 iPhone/iPad의 Apple Spotlight 시스템을 제외하고는 기기를 벗어나지 않습니다. 설정에서 언제든 끌 수 있습니다.

## 권한

iCangJie가 요청하는 권한은 **선택적 한 가지뿐**입니다.

| 권한 | 요청 시점 | 목적 |
|------------|----------------|---------|
| **사진 보관함(추가 전용)** | 튜토리얼의 자근 도표 이미지에서 **사진에 저장**을 눌렀을 때 | 이미지를 사진 보관함에 저장 |

iCangJie는 기존 사진을 읽지 **않습니다**. 핵심 기능에서는 카메라, 마이크, 연락처, 위치, 로컬 네트워크에 접근하지 않습니다.

외부 웹사이트를 여는 선택 기능(Youdao 온라인 조회, 튜토리얼 링크)은 시스템 브라우저를 사용하며 iCangJie에 탐색 기록에 대한 접근 권한을 부여하지 않습니다.

## 아동 개인정보 보호

iCangJie는 13세 미만 아동을 포함해 누구에게서도 개인 데이터를 의도적으로 수집하지 않습니다. 데이터를 전혀 수집하지 않으므로 별도의 조치는 필요하지 않습니다.

## 본 방침의 변경

당사는 본 개인정보 처리방침을 수시로 업데이트할 수 있습니다. 변경 사항은 갱신된 날짜와 함께 이 페이지에 게시됩니다. 이 페이지를 주기적으로 확인하시기 바랍니다.

## 문의

본 개인정보 처리방침에 대해 궁금한 점이 있으시면 연락해 주세요.

- **이메일:** [AppleOSer@gmail.com](mailto:AppleOSer@gmail.com)

</section>
<section lang="ru" markdown="1">

iHTC Studio («мы», «нас» или «наш») создала iCangJie (также известное как «爱仓颉» / «愛倉頡»). На этой странице описана наша политика в отношении сбора, использования и раскрытия данных при использовании приложения.

## Кратко

**iCangJie не собирает, не хранит и не передаёт никаких персональных данных.** Весь поиск иероглифов, викторины, тренировка набора и прогресс обучения обрабатываются исключительно на вашем устройстве. Учётная запись не нужна, а ни для одной основной функции не требуется подключение к интернету.

## Сбор данных

Мы не собираем никаких данных. В частности:

- **Персональная информация не собирается** (ни имени, ни электронной почты, ни номера телефона, ни учётной записи).
- **Данные об использовании и аналитика не собираются.**
- **Сторонние SDK** для рекламы, аналитики или отчётов о сбоях **не встроены**.
- **Файлы cookie и технологии отслеживания не используются.**

## Синхронизация через iCloud

iCangJie предлагает необязательную синхронизацию через iCloud (переключается в настройках). Когда она включена, следующие данные синхронизируются через **хранилище «ключ — значение» iCloud (iCloud KVS)** — сервис, который полностью предоставляется и управляется Apple:

| Синхронизируемые данные | Назначение |
|-------------|---------|
| Избранное | Иероглифы, добавленные в закладки |
| Статус изучения | Уровень прогресса по каждому иероглифу |
| Журнал ошибок | Вопросы викторин, на которые вы ответили неверно |
| Результаты викторин и серия | Ваши ежедневные результаты в викторинах |
| Статистика набора | Точность, серия и число сессий в тренировке набора |
| Ежедневные записи набора | Число иероглифов за день и гистограммы длины кода (~120 дней) |
| Прогресс по встроенным текстам | Позиция возобновления во встроенных текстах для набора |

Эти данные передаются напрямую между вашими устройствами через инфраструктуру Apple iCloud. iHTC Studio не использует никаких серверов и не имеет доступа к вашим данным iCloud. Обработка данных iCloud регулируется [Политикой конфиденциальности Apple](https://www.apple.com/privacy/).

Синхронизацию iCloud можно отключить в любой момент в настройках. После отключения все данные остаются локально на каждом устройстве.

Настройки интерфейса набора (сохранение неверных клавиш, пиньинь текста) хранятся локально на каждом устройстве и **не** синхронизируются через iCloud.

## Данные, хранящиеся локально на вашем устройстве

Все данные, созданные iCangJie, остаются на вашем устройстве:

| Данные | Хранение | Управление пользователем |
|------|---------|--------------|
| Избранное | Локально (UserDefaults / App Group) | Удаление отдельных элементов или полная очистка в приложении |
| Статус изучения | Локально (UserDefaults) | Сброс в настройках приложения |
| Журнал ошибок | Локально (UserDefaults) | Очистка в приложении |
| Результаты викторин и серия | Локально (UserDefaults) | Сброс в настройках приложения |
| Статистика набора и ежедневные записи | Локально (UserDefaults / App Group); по желанию iCloud KVS | Очищается при сбросе данных обучения |
| Прогресс по текстам | Локально (UserDefaults / App Group); по желанию iCloud KVS | Очищается при сбросе данных обучения |
| Настройки интерфейса набора | Локально (UserDefaults) | Изменение в Настройки → Набор |
| Флаги онбординга и «пути новичка» | Локально (UserDefaults) | Показываются снова только после сброса данных приложения |
| Настройки викторины | Локально (UserDefaults) | Изменение в настройках викторины |
| Настройка индексирования Spotlight | Локально (UserDefaults) | Переключатель в Настройки → Ярлыки экрана «Домой» |
| Настройки приложения и тема | Локально (UserDefaults) | Сброс удалением приложения |

Виджеты используют контейнер **App Group** для обмена данными между основным приложением и расширениями виджетов. Этот контейнер остаётся на вашем устройстве и недоступен третьим лицам.

### Резервная копия JSON (по инициативе пользователя)

Вы можете **экспортировать** файл резервной копии JSON (`.icangjie-backup`) с данными обучения. Файл записывается в место, которое **выбираете вы** (Файлы, AirDrop и т. д.). **Импорт** читает выбранный вами файл. iHTC Studio не загружает, не размещает и не имеет доступа к файлам резервных копий.

### Индексирование Spotlight (iOS, необязательно)

Если функция включена, iCangJie добавляет до **80** избранных и недавних иероглифов в индекс Spotlight iOS **на устройстве** (домен `com.iHTCboy.iCangJie.words`). Записи истекают через 30 дней. Эти данные не покидают ваше устройство, за исключением системы Spotlight от Apple на вашем iPhone/iPad. Отключить можно в любой момент в настройках.

## Разрешения

iCangJie запрашивает **только одно необязательное разрешение**:

| Разрешение | Когда запрашивается | Назначение |
|------------|----------------|---------|
| **Фототека (только добавление)** | Когда вы нажимаете **Сохранить в «Фото»** на изображении таблицы корней в обучающем материале | Сохранить изображение в вашу фототеку |

iCangJie **не** читает ваши существующие фотографии. Для основных функций нет доступа к камере, микрофону, контактам, геопозиции или локальной сети.

Необязательные функции, открывающие внешние сайты (онлайн-поиск Youdao, ссылки из обучения), используют системный браузер и не дают iCangJie доступа к вашей истории просмотров.

## Конфиденциальность детей

iCangJie сознательно не собирает персональные данные ни у кого, включая детей младше 13 лет. Поскольку данные не собираются вовсе, никаких особых мер не требуется.

## Изменения в политике

Мы можем время от времени обновлять настоящую Политику конфиденциальности. Любые изменения будут опубликованы на этой странице с обновлённой датой. Рекомендуем периодически перечитывать её.

## Связаться с нами

Если у вас есть вопросы о настоящей Политике конфиденциальности, свяжитесь с нами:

- **Эл. почта:** [AppleOSer@gmail.com](mailto:AppleOSer@gmail.com)

</section>
<section lang="th" markdown="1">

iHTC Studio ("เรา") เป็นผู้พัฒนา iCangJie (หรือที่รู้จักในชื่อ "爱仓颉" / "愛倉頡") หน้านี้อธิบายนโยบายของเราเกี่ยวกับการเก็บรวบรวม การใช้ และการเปิดเผยข้อมูลเมื่อคุณใช้แอปของเรา

## สรุป

**iCangJie ไม่เก็บรวบรวม จัดเก็บ หรือส่งข้อมูลส่วนบุคคลใด ๆ** การค้นหาตัวอักษร แบบทดสอบ การฝึกพิมพ์ และความคืบหน้าการเรียนรู้ทั้งหมดประมวลผลบนอุปกรณ์ของคุณเท่านั้น ไม่ต้องมีบัญชี และฟีเจอร์หลักทั้งหมดไม่ต้องเชื่อมต่ออินเทอร์เน็ต

## การเก็บรวบรวมข้อมูล

เราไม่เก็บรวบรวมข้อมูลใด ๆ โดยเฉพาะอย่างยิ่ง:

- **ไม่เก็บข้อมูลส่วนบุคคล** (ไม่มีชื่อ อีเมล หมายเลขโทรศัพท์ หรือบัญชี)
- **ไม่เก็บข้อมูลการใช้งาน** หรือการวิเคราะห์
- **ไม่มี SDK ของบุคคลที่สาม** สำหรับโฆษณา การวิเคราะห์ หรือรายงานข้อขัดข้อง
- **ไม่ใช้คุกกี้หรือเทคโนโลยีติดตาม**

## การซิงค์ iCloud

iCangJie มีฟีเจอร์ซิงค์ iCloud แบบเลือกใช้ (เปิด/ปิดได้ในการตั้งค่า) เมื่อเปิดใช้ ข้อมูลต่อไปนี้จะซิงค์ผ่าน **ที่เก็บข้อมูลคีย์-ค่าของ iCloud (iCloud KVS)** ซึ่งเป็นบริการที่ Apple จัดหาและดูแลทั้งหมด:

| ข้อมูลที่ซิงค์ | วัตถุประสงค์ |
|-------------|---------|
| รายการโปรด | ตัวอักษรที่คุณบุ๊กมาร์กไว้ |
| สถานะการเรียนรู้ | ระดับความคืบหน้าของแต่ละตัวอักษร |
| สมุดบันทึกข้อที่ตอบผิด | คำถามแบบทดสอบที่ตอบผิด |
| คะแนนแบบทดสอบและสถิติต่อเนื่อง | ผลงานแบบทดสอบประจำวันของคุณ |
| สถิติการพิมพ์ | ความแม่นยำ สถิติต่อเนื่อง และจำนวนรอบจากการฝึกพิมพ์ |
| บันทึกการพิมพ์รายวัน | จำนวนตัวอักษรต่อวันและฮิสโตแกรมความยาวรหัส (ประมาณ 120 วัน) |
| ความคืบหน้าบทความในตัว | ตำแหน่งที่ทำต่อในบทความฝึกพิมพ์ในตัว |

ข้อมูลนี้ส่งตรงระหว่างอุปกรณ์ของคุณผ่านโครงสร้างพื้นฐาน iCloud ของ Apple iHTC Studio ไม่ได้ดำเนินการเซิร์ฟเวอร์ใด ๆ และไม่สามารถเข้าถึงข้อมูล iCloud ของคุณ การจัดการข้อมูล iCloud อยู่ภายใต้ [นโยบายความเป็นส่วนตัวของ Apple](https://www.apple.com/privacy/)

คุณปิดการซิงค์ iCloud ได้ทุกเมื่อในการตั้งค่า เมื่อปิด ข้อมูลทั้งหมดจะอยู่ในเครื่องของแต่ละอุปกรณ์

ค่ากำหนด UI การพิมพ์ (การคงปุ่มที่กดผิด พินอินของบทความ) จะจัดเก็บในเครื่องของแต่ละอุปกรณ์และ **ไม่** ซิงค์ผ่าน iCloud

## ข้อมูลที่จัดเก็บในเครื่องบนอุปกรณ์ของคุณ

ข้อมูลทั้งหมดที่ iCangJie สร้างขึ้นจะอยู่บนอุปกรณ์ของคุณ:

| ข้อมูล | ที่เก็บ | การควบคุมโดยผู้ใช้ |
|------|---------|--------------|
| รายการโปรด | ในเครื่อง (UserDefaults / App Group) | ลบทีละรายการหรือล้างทั้งหมดในแอป |
| สถานะการเรียนรู้ | ในเครื่อง (UserDefaults) | รีเซ็ตในการตั้งค่าแอป |
| สมุดบันทึกข้อที่ตอบผิด | ในเครื่อง (UserDefaults) | ล้างในแอป |
| คะแนนแบบทดสอบและสถิติต่อเนื่อง | ในเครื่อง (UserDefaults) | รีเซ็ตในการตั้งค่าแอป |
| สถิติการพิมพ์และบันทึกรายวัน | ในเครื่อง (UserDefaults / App Group); iCloud KVS แบบเลือกได้ | ล้างเมื่อรีเซ็ตข้อมูลการเรียนรู้ |
| ความคืบหน้าบทความ | ในเครื่อง (UserDefaults / App Group); iCloud KVS แบบเลือกได้ | ล้างเมื่อรีเซ็ตข้อมูลการเรียนรู้ |
| ค่ากำหนด UI การพิมพ์ | ในเครื่อง (UserDefaults) | เปลี่ยนใน การตั้งค่า → การพิมพ์ |
| แฟล็กการแนะนำการใช้งานและเส้นทางผู้เริ่มต้น | ในเครื่อง (UserDefaults) | แสดงอีกครั้งเฉพาะเมื่อคุณรีเซ็ตข้อมูลแอป |
| ค่ากำหนดแบบทดสอบ | ในเครื่อง (UserDefaults) | เปลี่ยนในการตั้งค่าแบบทดสอบ |
| ค่ากำหนดการจัดทำดัชนี Spotlight | ในเครื่อง (UserDefaults) | เปิด/ปิดใน การตั้งค่า → ทางลัดหน้าจอโฮม |
| การตั้งค่าแอปและธีม | ในเครื่อง (UserDefaults) | รีเซ็ตโดยลบแอป |

วิดเจ็ตใช้คอนเทนเนอร์ **App Group** เพื่อแบ่งปันข้อมูลระหว่างแอปหลักและส่วนขยายวิดเจ็ต คอนเทนเนอร์นี้อยู่บนอุปกรณ์ของคุณและบุคคลที่สามเข้าถึงไม่ได้

### การสำรองข้อมูล JSON (ผู้ใช้เป็นผู้เริ่ม)

คุณ **ส่งออก** ไฟล์สำรองข้อมูล JSON (`.icangjie-backup`) ที่มีข้อมูลการเรียนรู้ได้ ไฟล์จะถูกเขียนไปยังตำแหน่งที่ **คุณเลือก** (ไฟล์ AirDrop ฯลฯ) การ **นำเข้า** จะอ่านไฟล์ที่คุณเลือก iHTC Studio ไม่อัปโหลด โฮสต์ หรือเข้าถึงไฟล์สำรองข้อมูล

### การจัดทำดัชนี Spotlight (iOS แบบเลือกได้)

เมื่อเปิดใช้ iCangJie จะจัดทำดัชนีรายการโปรดและตัวอักษรล่าสุดสูงสุด **80** ตัวลงในดัชนี Spotlight ของ iOS **บนอุปกรณ์** (โดเมน `com.iHTCboy.iCangJie.words`) รายการจะหมดอายุหลัง 30 วัน ข้อมูลนี้ไม่ออกจากอุปกรณ์ของคุณ ยกเว้นผ่านระบบ Spotlight ของ Apple บน iPhone/iPad ของคุณ ปิดได้ทุกเมื่อในการตั้งค่า

## สิทธิ์การเข้าถึง

iCangJie ขอ **สิทธิ์แบบเลือกได้เพียงอย่างเดียว**:

| สิทธิ์ | ขอเมื่อใด | วัตถุประสงค์ |
|------------|----------------|---------|
| **คลังรูปภาพ (เพิ่มอย่างเดียว)** | เมื่อคุณแตะ **บันทึกลงในรูปภาพ** บนภาพแผนภูมิรากในบทเรียน | บันทึกภาพลงในคลังรูปภาพของคุณ |

iCangJie **ไม่** อ่านรูปภาพที่มีอยู่ของคุณ ไม่มีการเข้าถึงกล้อง ไมโครโฟน รายชื่อติดต่อ ตำแหน่งที่ตั้ง หรือเครือข่ายภายในเครื่องสำหรับฟีเจอร์หลัก

ฟีเจอร์เสริมที่เปิดเว็บไซต์ภายนอก (การค้นหา Youdao ออนไลน์ ลิงก์บทเรียน) ใช้เบราว์เซอร์ของระบบ และไม่ให้ iCangJie เข้าถึงประวัติการเรียกดูของคุณ

## ความเป็นส่วนตัวของเด็ก

iCangJie ไม่ได้ตั้งใจเก็บข้อมูลส่วนบุคคลจากใครก็ตาม รวมถึงเด็กอายุต่ำกว่า 13 ปี เนื่องจากไม่มีการเก็บข้อมูลเลย จึงไม่จำเป็นต้องมีข้อกำหนดพิเศษ

## การเปลี่ยนแปลงนโยบายนี้

เราอาจปรับปรุงนโยบายความเป็นส่วนตัวนี้เป็นครั้งคราว การเปลี่ยนแปลงใด ๆ จะเผยแพร่บนหน้านี้พร้อมวันที่ที่อัปเดต เราขอแนะนำให้คุณตรวจดูหน้านี้เป็นระยะ

## ติดต่อเรา

หากคุณมีคำถามเกี่ยวกับนโยบายความเป็นส่วนตัวนี้ โปรดติดต่อเรา:

- **อีเมล:** [AppleOSer@gmail.com](mailto:AppleOSer@gmail.com)

</section>
<section lang="de" markdown="1">

iHTC Studio („wir“, „uns“ oder „unser“) hat iCangJie (auch bekannt als „爱仓颉“ / „愛倉頡“) entwickelt. Diese Seite beschreibt unsere Richtlinien zur Erhebung, Nutzung und Offenlegung von Daten bei der Nutzung unserer App.

## Zusammenfassung

**iCangJie erhebt, speichert oder überträgt keinerlei personenbezogene Daten.** Alle Zeichensuchen, Quizze, das Tippen-Training und der Lernfortschritt werden ausschließlich auf Ihrem Gerät verarbeitet. Es ist kein Konto erforderlich, und für keine Kernfunktion wird eine Internetverbindung benötigt.

## Datenerhebung

Wir erheben keinerlei Daten. Im Einzelnen:

- Es werden **keine personenbezogenen Informationen** erhoben (kein Name, keine E-Mail-Adresse, keine Telefonnummer, kein Konto).
- Es werden **keine Nutzungsdaten** und keine Analysen erhoben.
- Es sind **keine SDKs von Drittanbietern** für Werbung, Analyse oder Absturzberichte eingebunden.
- Es werden **keine Cookies oder Tracking-Technologien** verwendet.

## iCloud-Synchronisierung

iCangJie bietet eine optionale iCloud-Synchronisierung (in den Einstellungen umschaltbar). Wenn sie aktiviert ist, werden die folgenden Daten über den **iCloud-Schlüssel-Wert-Speicher (iCloud KVS)** synchronisiert, einen vollständig von Apple bereitgestellten und verwalteten Dienst:

| Synchronisierte Daten | Zweck |
|-------------|---------|
| Favoriten | Ihre mit Lesezeichen versehenen Zeichen |
| Lernstatus | Fortschrittsstufe für jedes Zeichen |
| Fehlerheft | Falsch beantwortete Quizfragen |
| Quizergebnisse und Serie | Ihre täglichen Quizleistungen |
| Tippstatistik | Genauigkeit, Serie und Sitzungsanzahl aus dem Tippen-Training |
| Tägliche Tippaufzeichnungen | Zeichenanzahl pro Tag und Histogramme der Codelängen (ca. 120 Tage) |
| Fortschritt in integrierten Texten | Fortsetzungsposition in den integrierten Tipptexten |

Diese Daten werden direkt zwischen Ihren Geräten über Apples iCloud-Infrastruktur übertragen. iHTC Studio betreibt keinen Server und hat keinen Zugriff auf Ihre iCloud-Daten. Für den Umgang von Apple mit iCloud-Daten gilt [Apples Datenschutzrichtlinie](https://www.apple.com/privacy/).

Sie können die iCloud-Synchronisierung jederzeit in den Einstellungen deaktivieren. Wenn sie deaktiviert ist, bleiben alle Daten lokal auf dem jeweiligen Gerät.

Einstellungen der Tipp-Oberfläche (Beibehaltung falscher Tasten, Text-Pinyin) werden lokal auf jedem Gerät gespeichert und **nicht** über iCloud synchronisiert.

## Lokal auf Ihrem Gerät gespeicherte Daten

Alle von iCangJie erzeugten Daten bleiben auf Ihrem Gerät:

| Daten | Speicherung | Kontrolle durch den Nutzer |
|------|---------|--------------|
| Favoriten | Lokal (UserDefaults / App Group) | Einzelne Einträge in der App entfernen oder alle löschen |
| Lernstatus | Lokal (UserDefaults) | In den App-Einstellungen zurücksetzen |
| Fehlerheft | Lokal (UserDefaults) | In der App löschen |
| Quizergebnisse und Serie | Lokal (UserDefaults) | In den App-Einstellungen zurücksetzen |
| Tippstatistik und tägliche Aufzeichnungen | Lokal (UserDefaults / App Group); optional iCloud KVS | Wird beim Zurücksetzen der Lerndaten gelöscht |
| Textfortschritt | Lokal (UserDefaults / App Group); optional iCloud KVS | Wird beim Zurücksetzen der Lerndaten gelöscht |
| Einstellungen der Tipp-Oberfläche | Lokal (UserDefaults) | Unter Einstellungen → Tippen ändern |
| Onboarding- und Einsteigerpfad-Markierungen | Lokal (UserDefaults) | Wird nur erneut angezeigt, wenn Sie die App-Daten zurücksetzen |
| Quiz-Einstellungen | Lokal (UserDefaults) | In den Quiz-Einstellungen ändern |
| Einstellung zur Spotlight-Indizierung | Lokal (UserDefaults) | Unter Einstellungen → Home-Bildschirm-Kurzbefehle umschalten |
| App-Einstellungen und Design | Lokal (UserDefaults) | Durch Löschen der App zurücksetzen |

Widgets nutzen einen **App-Group**-Container, um Daten zwischen der Haupt-App und den Widget-Erweiterungen auszutauschen. Dieser Container bleibt auf Ihrem Gerät und ist für Dritte nicht zugänglich.

### JSON-Sicherung (vom Nutzer ausgelöst)

Sie können eine JSON-Sicherungsdatei (`.icangjie-backup`) mit Lerndaten **exportieren**. Die Datei wird an einem Ort geschrieben, den **Sie wählen** (Dateien, AirDrop usw.). Beim **Import** wird eine von Ihnen ausgewählte Datei gelesen. iHTC Studio lädt Sicherungsdateien weder hoch noch hostet oder öffnet es sie.

### Spotlight-Indizierung (iOS, optional)

Wenn aktiviert, indiziert iCangJie bis zu **80** Favoriten und zuletzt angesehene Zeichen im iOS-Spotlight-Index **auf dem Gerät** (Domain `com.iHTCboy.iCangJie.words`). Einträge laufen nach 30 Tagen ab. Diese Daten verlassen Ihr Gerät nicht, außer über Apples Spotlight-System auf Ihrem iPhone/iPad. Sie können sie jederzeit in den Einstellungen deaktivieren.

## Berechtigungen

iCangJie fordert **nur eine optionale Berechtigung** an:

| Berechtigung | Wann angefordert | Zweck |
|------------|----------------|---------|
| **Fotomediathek (nur Hinzufügen)** | Wenn Sie in einem Tutorial bei einem Wurzeldiagramm-Bild auf **In Fotos sichern** tippen | Das Bild in Ihrer Fotomediathek speichern |

iCangJie liest Ihre vorhandenen Fotos **nicht**. Für die Kernfunktionen gibt es keinen Zugriff auf Kamera, Mikrofon, Kontakte, Standort oder das lokale Netzwerk.

Optionale Funktionen, die externe Websites öffnen (Youdao-Online-Suche, Tutorial-Links), nutzen den System-Browser und gewähren iCangJie keinen Zugriff auf Ihren Browserverlauf.

## Datenschutz für Kinder

iCangJie erhebt wissentlich von niemandem personenbezogene Daten, auch nicht von Kindern unter 13 Jahren. Da überhaupt keine Daten erhoben werden, sind keine besonderen Vorkehrungen erforderlich.

## Änderungen dieser Richtlinie

Wir können diese Datenschutzerklärung von Zeit zu Zeit aktualisieren. Änderungen werden mit aktualisiertem Datum auf dieser Seite veröffentlicht. Wir empfehlen, diese Seite regelmäßig zu prüfen.

## Kontakt

Wenn Sie Fragen zu dieser Datenschutzerklärung haben, kontaktieren Sie uns bitte:

- **E-Mail:** [AppleOSer@gmail.com](mailto:AppleOSer@gmail.com)

</section>
<section lang="fr" markdown="1">

iHTC Studio (« nous », « notre » ou « nos ») a développé iCangJie (également connu sous le nom « 爱仓颉 » / « 愛倉頡 »). Cette page décrit nos politiques en matière de collecte, d'utilisation et de divulgation des données lorsque vous utilisez notre app.

## Résumé

**iCangJie ne collecte, ne stocke ni ne transmet aucune donnée personnelle.** Toutes les recherches de caractères, les quiz, l'entraînement à la saisie et la progression d'apprentissage sont traités entièrement sur votre appareil. Aucun compte n'est requis et aucune connexion Internet n'est nécessaire pour les fonctionnalités principales.

## Collecte de données

Nous ne collectons aucune donnée. Plus précisément :

- **Aucune information personnelle** n'est collectée (ni nom, ni e-mail, ni numéro de téléphone, ni compte).
- **Aucune donnée d'utilisation** ni analyse n'est collectée.
- **Aucun SDK tiers** de publicité, d'analyse ou de rapport de plantage n'est intégré.
- **Aucun cookie ni technologie de suivi** n'est utilisé.

## Synchronisation iCloud

iCangJie propose une synchronisation iCloud facultative (activable dans les Réglages). Lorsqu'elle est activée, les données suivantes sont synchronisées via le **stockage clé-valeur iCloud (iCloud KVS)**, un service entièrement fourni et géré par Apple :

| Données synchronisées | Finalité |
|-------------|---------|
| Favoris | Vos caractères mis en signet |
| Statut d'apprentissage | Niveau de progression pour chaque caractère |
| Carnet d'erreurs | Questions de quiz auxquelles vous avez mal répondu |
| Scores de quiz et série | Vos performances au quiz quotidien |
| Statistiques de saisie | Précision, série et nombre de sessions de l'entraînement à la saisie |
| Enregistrements quotidiens de saisie | Nombre de caractères par jour et histogrammes de longueur de code (~120 jours) |
| Progression des textes intégrés | Position de reprise dans les textes de saisie intégrés |

Ces données sont transmises directement entre vos appareils via l'infrastructure iCloud d'Apple. iHTC Studio n'exploite aucun serveur et n'a pas accès à vos données iCloud. Le traitement des données iCloud par Apple est régi par la [politique de confidentialité d'Apple](https://www.apple.com/privacy/).

Vous pouvez désactiver la synchronisation iCloud à tout moment dans les Réglages. Lorsqu'elle est désactivée, toutes les données restent locales sur chaque appareil.

Les préférences de l'interface de saisie (conservation des touches erronées, pinyin du texte) sont stockées localement sur chaque appareil et **ne** sont **pas** synchronisées via iCloud.

## Données stockées localement sur votre appareil

Toutes les données créées par iCangJie restent sur votre appareil :

| Données | Stockage | Contrôle de l'utilisateur |
|------|---------|--------------|
| Favoris | Local (UserDefaults / App Group) | Supprimer des éléments individuels ou tout effacer dans l'app |
| Statut d'apprentissage | Local (UserDefaults) | Réinitialisation dans les réglages de l'app |
| Carnet d'erreurs | Local (UserDefaults) | Effacement dans l'app |
| Scores de quiz et série | Local (UserDefaults) | Réinitialisation dans les réglages de l'app |
| Statistiques de saisie et enregistrements quotidiens | Local (UserDefaults / App Group) ; iCloud KVS facultatif | Effacés lors de la réinitialisation des données d'apprentissage |
| Progression des textes | Local (UserDefaults / App Group) ; iCloud KVS facultatif | Effacée lors de la réinitialisation des données d'apprentissage |
| Préférences de l'interface de saisie | Local (UserDefaults) | Modification dans Réglages → Saisie |
| Indicateurs de prise en main et de parcours débutant | Local (UserDefaults) | Réaffichés uniquement si vous réinitialisez les données de l'app |
| Préférences du quiz | Local (UserDefaults) | Modification dans les réglages du quiz |
| Préférence d'indexation Spotlight | Local (UserDefaults) | Commutateur dans Réglages → Raccourcis de l'écran d'accueil |
| Préférences de l'app et thème | Local (UserDefaults) | Réinitialisation en supprimant l'app |

Les widgets utilisent un conteneur **App Group** pour partager des données entre l'app principale et les extensions de widgets. Ce conteneur reste sur votre appareil et n'est accessible à aucun tiers.

### Sauvegarde JSON (à l'initiative de l'utilisateur)

Vous pouvez **exporter** un fichier de sauvegarde JSON (`.icangjie-backup`) contenant les données d'apprentissage. Le fichier est écrit à un emplacement **de votre choix** (Fichiers, AirDrop, etc.). **L'importation** lit un fichier que vous sélectionnez. iHTC Studio ne téléverse, n'héberge ni n'accède aux fichiers de sauvegarde.

### Indexation Spotlight (iOS, facultative)

Lorsqu'elle est activée, iCangJie indexe jusqu'à **80** favoris et caractères récents dans l'index Spotlight d'iOS **sur l'appareil** (domaine `com.iHTCboy.iCangJie.words`). Les entrées expirent après 30 jours. Ces données ne quittent jamais votre appareil, sauf via le système Spotlight d'Apple sur votre iPhone/iPad. Vous pouvez la désactiver à tout moment dans les Réglages.

## Autorisations

iCangJie ne demande **qu'une seule autorisation facultative** :

| Autorisation | Quand elle est demandée | Finalité |
|------------|----------------|---------|
| **Photothèque (ajout uniquement)** | Lorsque vous touchez **Enregistrer dans Photos** sur une image de tableau de racines dans un tutoriel | Enregistrer l'image dans votre photothèque |

iCangJie **ne** lit **pas** vos photos existantes. Il n'y a aucun accès à votre appareil photo, au microphone, aux contacts, à la localisation ni au réseau local pour les fonctionnalités principales.

Les fonctionnalités facultatives qui ouvrent des sites web externes (recherche en ligne Youdao, liens de tutoriel) utilisent le navigateur du système et n'accordent pas à iCangJie l'accès à votre historique de navigation.

## Confidentialité des enfants

iCangJie ne collecte sciemment de données personnelles auprès de personne, y compris des enfants de moins de 13 ans. Comme aucune donnée n'est collectée, aucune disposition particulière n'est nécessaire.

## Modifications de cette politique

Nous pouvons mettre à jour cette politique de confidentialité de temps à autre. Toute modification sera publiée sur cette page avec une date mise à jour. Nous vous encourageons à consulter régulièrement cette page.

## Nous contacter

Si vous avez des questions sur cette politique de confidentialité, veuillez nous contacter :

- **E-mail :** [AppleOSer@gmail.com](mailto:AppleOSer@gmail.com)

</section>
<section lang="tr" markdown="1">

iHTC Studio ("biz" veya "bizim"), iCangJie'yi (aynı zamanda "爱仓颉" / "愛倉頡" olarak bilinir) geliştirmiştir. Bu sayfa, uygulamamızı kullandığınızda veri toplama, kullanma ve ifşa etme ile ilgili politikalarımızı açıklar.

## Özet

**iCangJie herhangi bir kişisel veri toplamaz, saklamaz veya iletmez.** Tüm karakter aramaları, testler, yazma alıştırması ve öğrenme ilerlemesi tamamen cihazınızda işlenir. Hesap gerekmez ve hiçbir temel özellik için internet bağlantısına ihtiyaç yoktur.

## Veri Toplama

Hiçbir veri toplamıyoruz. Özellikle:

- **Kişisel bilgi toplanmaz** (ad, e-posta, telefon numarası veya hesap yoktur).
- **Kullanım verisi** veya analiz toplanmaz.
- Reklam, analiz veya çökme raporlama için **üçüncü taraf SDK'sı entegre edilmemiştir**.
- **Çerez veya izleme teknolojileri kullanılmaz.**

## iCloud Senkronizasyonu

iCangJie, isteğe bağlı bir iCloud senkronizasyon özelliği sunar (Ayarlar'da açılıp kapatılabilir). Etkinleştirildiğinde, aşağıdaki veriler tamamen Apple tarafından sağlanan ve yönetilen bir hizmet olan **iCloud Anahtar-Değer Depolaması (iCloud KVS)** üzerinden senkronize edilir:

| Senkronize Edilen Veri | Amaç |
|-------------|---------|
| Favoriler | Yer imi eklediğiniz karakterler |
| Öğrenme durumu | Her karakter için ilerleme seviyesi |
| Yanlış soru defteri | Testte yanlış cevaplanan sorular |
| Test puanları ve seri | Günlük test performansınız |
| Yazma istatistikleri | Yazma alıştırmasından doğruluk, seri ve oturum sayıları |
| Günlük yazma kayıtları | Güne göre karakter sayıları ve kod uzunluğu histogramları (~120 gün) |
| Yerleşik metin ilerlemesi | Yerleşik yazma metinlerinde devam konumu |

Bu veriler, Apple'ın iCloud altyapısı üzerinden doğrudan cihazlarınız arasında iletilir. iHTC Studio herhangi bir sunucu işletmez ve iCloud verilerinize erişimi yoktur. Apple'ın iCloud verilerini ele alışı [Apple'ın Gizlilik Politikası](https://www.apple.com/privacy/) kapsamındadır.

iCloud senkronizasyonunu Ayarlar'dan istediğiniz zaman devre dışı bırakabilirsiniz. Devre dışı bırakıldığında tüm veriler her cihazda yerel olarak kalır.

Yazma arayüzü tercihleri (yanlış tuşları koruma, metin pinyin'i) her cihazda yerel olarak saklanır ve iCloud ile senkronize **edilmez**.

## Cihazınızda Yerel Olarak Saklanan Veriler

iCangJie'nin oluşturduğu tüm veriler cihazınızda kalır:

| Veri | Depolama | Kullanıcı Kontrolü |
|------|---------|--------------|
| Favoriler | Yerel (UserDefaults / App Group) | Uygulamada tek tek öğeleri kaldırın veya hepsini temizleyin |
| Öğrenme durumu | Yerel (UserDefaults) | Uygulama ayarlarından sıfırlayın |
| Yanlış soru defteri | Yerel (UserDefaults) | Uygulamada temizleyin |
| Test puanları ve seri | Yerel (UserDefaults) | Uygulama ayarlarından sıfırlayın |
| Yazma istatistikleri ve günlük kayıtlar | Yerel (UserDefaults / App Group); isteğe bağlı iCloud KVS | Öğrenme verileri sıfırlandığında temizlenir |
| Metin ilerlemesi | Yerel (UserDefaults / App Group); isteğe bağlı iCloud KVS | Öğrenme verileri sıfırlandığında temizlenir |
| Yazma arayüzü tercihleri | Yerel (UserDefaults) | Ayarlar → Yazma bölümünden değiştirin |
| Tanıtım ve yeni başlayan yolu işaretleri | Yerel (UserDefaults) | Yalnızca uygulama verilerini sıfırlarsanız yeniden gösterilir |
| Test tercihleri | Yerel (UserDefaults) | Test ayarlarından değiştirin |
| Spotlight dizinleme tercihi | Yerel (UserDefaults) | Ayarlar → Ana Ekran kısayolları bölümünden açıp kapatın |
| Uygulama tercihleri ve tema | Yerel (UserDefaults) | Uygulamayı silerek sıfırlayın |

Widget'lar, ana uygulama ile widget uzantıları arasında veri paylaşmak için bir **App Group** kapsayıcısı kullanır. Bu kapsayıcı cihazınızda kalır ve hiçbir üçüncü tarafça erişilemez.

### JSON Yedekleme (kullanıcı tarafından başlatılır)

Öğrenme verilerini içeren bir JSON yedek dosyasını (`.icangjie-backup`) **dışa aktarabilirsiniz**. Dosya, **sizin seçtiğiniz** bir konuma (Dosyalar, AirDrop vb.) yazılır. **İçe aktarma**, sizin seçtiğiniz bir dosyayı okur. iHTC Studio yedek dosyalarını yüklemez, barındırmaz veya bunlara erişmez.

### Spotlight Dizinleme (iOS, isteğe bağlı)

Etkinleştirildiğinde iCangJie, **cihaz üzerindeki** iOS Spotlight dizinine (alan adı `com.iHTCboy.iCangJie.words`) en fazla **80** favori ve son karakteri dizinler. Girdiler 30 gün sonra sona erer. Bu veriler, iPhone/iPad'inizdeki Apple'ın Spotlight sistemi dışında cihazınızdan asla çıkmaz. Ayarlar'dan istediğiniz zaman devre dışı bırakabilirsiniz.

## İzinler

iCangJie **yalnızca bir isteğe bağlı izin** ister:

| İzin | Ne zaman istenir | Amaç |
|------------|----------------|---------|
| **Fotoğraf Kitaplığı (Yalnızca Ekleme)** | Bir eğitimdeki kök tablosu görselinde **Fotoğraflar'a Kaydet**'e dokunduğunuzda | Görseli fotoğraf kitaplığınıza kaydetmek |

iCangJie mevcut fotoğraflarınızı **okumaz**. Temel özellikler için kameranıza, mikrofonunuza, kişilerinize, konumunuza veya yerel ağınıza erişim yoktur.

Harici web sitelerini açan isteğe bağlı özellikler (Youdao çevrimiçi arama, eğitim bağlantıları) sistem tarayıcısını kullanır ve iCangJie'ye gezinti geçmişinize erişim vermez.

## Çocukların Gizliliği

iCangJie, 13 yaşın altındaki çocuklar dahil hiç kimseden bilerek kişisel veri toplamaz. Hiç veri toplanmadığı için özel bir düzenleme gerekmez.

## Bu Politikadaki Değişiklikler

Bu Gizlilik Politikası'nı zaman zaman güncelleyebiliriz. Değişiklikler, güncellenmiş bir tarihle bu sayfada yayımlanacaktır. Bu sayfayı düzenli olarak gözden geçirmenizi öneririz.

## Bize Ulaşın

Bu Gizlilik Politikası hakkında sorularınız varsa lütfen bizimle iletişime geçin:

- **E-posta:** [AppleOSer@gmail.com](mailto:AppleOSer@gmail.com)

</section>
