---
layout: doc
title: iStore — FAQ
app_id: iStore
doc_title_en: Frequently Asked Questions
doc_title_zh_cn: 常见问题
doc_title_zh_tw: 常見問題
description: Frequently asked questions about iStore — App Store region switching, availability checks, favorites, widgets, and iCloud sync.
---

<section lang="en" markdown="1">

### How does region switching work?

iStore opens Apple's **official App Store redirect link** for the region you pick. The App Store then asks you to confirm the change on Apple's own screen. iStore never sees your Apple ID, password, or payment details.

### Do I need to sign in?

No. iStore requires **no account and no login**. You only interact with your existing Apple ID inside Apple's own App Store screen when you confirm a switch.

### Will switching region log me out or lose my apps?

No. Switching your storefront changes which region's App Store you browse and buy from. Your installed apps stay installed. Apple may require your billing region and payment method to match before you can purchase in a new region.

### Is iStore affiliated with Apple?

No. iStore is an independent tool built by iHTC Studio contributors. It is **not affiliated with Apple Inc.** It simply uses Apple's official redirect link to switch regions.

### How many regions are supported?

**175 regions** across 7 continents, each with its flag and a localized name (English / Simplified / Traditional Chinese).

### What is the App Availability check?

Paste an **App Store link or numeric App ID** and iStore checks (via Apple's public iTunes Lookup API) **which regions the app is available in**. Scope the check to **Popular**, **Favorites**, or **All** regions, then switch to any available region with one tap. It works in the app and from the **Share Extension**.

### How do I check availability from another app?

Use the **Share** sheet on any App Store link (Safari, Messages, App Store, etc.) and choose **iStore**. The Share Extension checks popular regions and lets you open the result in the app to switch.

### What is the difference between Favorites and Pinned?

**Favorites** are the regions you star. **Pinned** regions are a subset you want to keep at the very top everywhere (store, favorites, and widgets). Unfavoriting a region also removes it from pinned.

### What's the Map Picker?

A **full-screen map** with a pin for each region. Scope it to Popular, Favorites, or All, then tap a pin to switch. It's a visual way to explore stores by location.

### Which widgets are available?

- **Quick Regions** and **Recent** widgets (Home & Lock Screen)
- A **Custom** widget you configure with your own regions (iOS 17+)
- **Interactive widgets** (iOS 17+) — tap a region tile to switch directly

### What is the Control Center control?

On **iOS 18+**, add the **Switch Last** control to Control Center to re-switch to your most recent target region in one tap.

### Can I switch using Siri or Shortcuts?

Yes. iStore provides Siri & Shortcuts actions to **switch a region**, **switch your last region**, **switch a favorite**, **open the store**, or **check availability**. See [Shortcut Links](../url-scheme).

### Does Spotlight search work?

Yes. All 175 regions are indexed in **Spotlight** — search a region from the Home Screen and tap the result to switch directly in iStore.

### What does iCloud Sync cover?

Optional iCloud sync keeps these in step across your devices: **favorites**, **pinned regions**, **quick regions**, **switch history**, **last switched region**, and appearance / layout / favorites preferences. Data syncs through **your private iCloud** — not iHTC Studio servers. Sync is on by default and can be turned off in Settings.

### Can I turn off the confirmation before switching?

Yes. **Confirm before switch** is on by default to prevent mistaps; you can disable it in Settings.

### What languages does iStore support?

**English, 简体中文, and 繁體中文.** You can also choose how region names are displayed (region name display mode).

### Which devices are supported?

- **iPhone / iPad** — iOS 16.2+ (main app)
- **Configurable / interactive widgets** — iOS 17.0+
- **Control Center control & iPhone Search tab** — iOS 18.0+
- **Shortcuts & Siri** — iOS 16.2+

### Does iStore work offline?

Browsing and switching links work offline, but the **App Availability** check needs a network connection (it queries Apple's public lookup API). Your favorites, pinned regions, and history are saved on your device.

### How do I get iStore?

### How do I get iStore?

Download from the [App Store](https://apps.apple.com/app/id6786123132).

### Still need help?

Contact [AppleOSer@gmail.com](mailto:AppleOSer@gmail.com). We typically respond within 48 hours.

</section>
<section lang="zh-CN" markdown="1">

### 地区切换是怎么实现的？

爱商店会打开你所选地区的 **App Store 官方跳转链接**，随后由 App Store 在 Apple 自己的界面上请你确认更改。爱商店不会看到你的 Apple ID、密码或支付信息。

### 需要登录吗？

不需要。爱商店**无需账号、无需登录**。只有在你确认切换时，才会在 Apple 自己的 App Store 界面上与你现有的 Apple ID 交互。

### 切换地区会退出登录或丢失已装 App 吗？

不会。切换商店地区只改变你浏览与购买所用的地区 App Store，已安装的 App 仍然保留。Apple 可能要求你的账单地区与支付方式匹配后，才能在新地区购买。

### 爱商店与 Apple 有关联吗？

没有。爱商店是 iHTC Studio 贡献者开发的独立工具，**与 Apple Inc. 无关联**，仅使用 Apple 官方跳转链接进行地区切换。

### 支持多少个地区？

**175 个地区**，横跨 7 大洲，每个地区含旗帜与本地化名称（英文 / 简体 / 繁体）。

### 上架查询是什么？

粘贴 **App Store 链接或数字 App ID**，爱商店通过 Apple 公开的 iTunes Lookup API 查询该 **App 在哪些地区上架**。查询范围可选**常用**、**收藏**或**全部**地区，然后可一键切换到任意可用地区。App 内与**分享扩展**均可使用。

### 如何从其他 App 查询上架？

在任意 App Store 链接上使用**分享**面板（Safari、信息、App Store 等），选择 **iStore**。分享扩展会查询常用地区，并可在 App 内打开结果进行切换。

### 收藏与置顶有什么区别？

**收藏**是你加星标的地区；**置顶**是收藏中你希望始终排在最前（商店、收藏与小组件中）的子集。取消收藏某地区时也会从置顶中移除。

### 地图选区是什么？

一张**全屏地图**，每个地区带有定位标记。范围可选常用、收藏或全部，点按标记即可切换——用地理方式直观探索各地商店。

### 有哪些小组件？

- **常用地区**与**最近**小组件（主屏与锁屏）
- 可自定义地区的**自定义**小组件（iOS 17+）
- **交互式小组件**（iOS 17+）——点按地区磁贴直接切换

### 控制中心控件是什么？

在 **iOS 18+** 上，可将**切换上次**控件添加到控制中心，一键再次切换到最近的目标地区。

### 能用 Siri 或快捷指令切换吗？

可以。爱商店提供 Siri 与快捷指令操作：**切换地区**、**切换上次**、**切换收藏**、**打开商店**或**查询上架**。详见 [快捷链接说明](../url-scheme)。

### 支持 Spotlight 搜索吗？

支持。全部 175 个地区都会被索引到 **Spotlight**——在主屏搜索地区并点按结果，即可在爱商店中直接切换。

### iCloud 同步包含什么？

可选 iCloud 同步会在各设备间同步：**收藏**、**置顶地区**、**常用地区**、**切换历史**、**上次切换地区**以及外观 / 布局 / 收藏偏好。数据通过**你的私有 iCloud** 同步，不经过 iHTC Studio 服务器。默认开启，可在设置中关闭。

### 可以关闭切换前的确认吗？

可以。**切换前确认**默认开启以防误触，你可以在设置中关闭。

### 爱商店支持哪些语言？

**English、简体中文、繁體中文。** 你还可以选择地区名的显示方式（地区名显示模式）。

### 支持哪些设备？

- **iPhone / iPad** — iOS 16.2+（主应用）
- **可配置 / 交互式小组件** — iOS 17.0+
- **控制中心控件与 iPhone 搜索 Tab** — iOS 18.0+
- **快捷指令与 Siri** — iOS 16.2+

### 爱商店能离线使用吗？

浏览与切换链接可离线使用，但**上架查询**需要联网（调用 Apple 公开的查询 API）。你的收藏、置顶地区与历史保存在本机。

### 如何获取爱商店？

在 [App Store](https://apps.apple.com/app/id6786123132) 下载。

### 仍有问题？

联系 [AppleOSer@gmail.com](mailto:AppleOSer@gmail.com)，我们通常在 48 小时内回复。

</section>
<section lang="zh-TW" markdown="1">

### 地區切換是怎麼實現的？

愛商店會開啟你所選地區的 **App Store 官方跳轉連結**，隨後由 App Store 在 Apple 自己的介面上請你確認更改。愛商店不會看到你的 Apple ID、密碼或付款資訊。

### 需要登入嗎？

不需要。愛商店**無需帳號、無需登入**。只有在你確認切換時，才會在 Apple 自己的 App Store 介面上與你現有的 Apple ID 互動。

### 切換地區會登出或遺失已裝 App 嗎？

不會。切換商店地區只改變你瀏覽與購買所用的地區 App Store，已安裝的 App 仍然保留。Apple 可能要求你的帳單地區與付款方式相符後，才能在新地區購買。

### 愛商店與 Apple 有關聯嗎？

沒有。愛商店是 iHTC Studio 貢獻者開發的獨立工具，**與 Apple Inc. 無關聯**，僅使用 Apple 官方跳轉連結進行地區切換。

### 支援多少個地區？

**175 個地區**，橫跨 7 大洲，每個地區含旗幟與本地化名稱（英文 / 簡體 / 繁體）。

### 上架查詢是什麼？

貼上 **App Store 連結或數字 App ID**，愛商店透過 Apple 公開的 iTunes Lookup API 查詢該 **App 在哪些地區上架**。查詢範圍可選**常用**、**收藏**或**全部**地區，然後可一鍵切換到任意可用地區。App 內與**分享延伸功能**均可使用。

### 如何從其他 App 查詢上架？

在任意 App Store 連結上使用**分享**面板（Safari、訊息、App Store 等），選擇 **iStore**。分享延伸功能會查詢常用地區，並可在 App 內開啟結果進行切換。

### 收藏與置頂有什麼區別？

**收藏**是你加星號的地區；**置頂**是收藏中你希望始終排在最前（商店、收藏與小工具中）的子集。取消收藏某地區時也會從置頂中移除。

### 地圖選區是什麼？

一張**全螢幕地圖**，每個地區帶有定位標記。範圍可選常用、收藏或全部，點按標記即可切換——用地理方式直觀探索各地商店。

### 有哪些小工具？

- **常用地區**與**最近**小工具（主畫面與鎖定畫面）
- 可自訂地區的**自訂**小工具（iOS 17+）
- **互動式小工具**（iOS 17+）——點按地區磁貼直接切換

### 控制中心控制項是什麼？

在 **iOS 18+** 上，可將**切換上次**控制項加入控制中心，一鍵再次切換到最近的目標地區。

### 能用 Siri 或捷徑切換嗎？

可以。愛商店提供 Siri 與捷徑操作：**切換地區**、**切換上次**、**切換收藏**、**開啟商店**或**查詢上架**。詳見 [快捷連結說明](../url-scheme)。

### 支援 Spotlight 搜尋嗎？

支援。全部 175 個地區都會被索引到 **Spotlight**——在主畫面搜尋地區並點按結果，即可在愛商店中直接切換。

### iCloud 同步包含什麼？

可選 iCloud 同步會在各裝置間同步：**收藏**、**置頂地區**、**常用地區**、**切換歷史**、**上次切換地區**以及外觀 / 版面 / 收藏偏好。資料透過**你的私有 iCloud** 同步，不經過 iHTC Studio 伺服器。預設開啟，可在設定中關閉。

### 可以關閉切換前的確認嗎？

可以。**切換前確認**預設開啟以防誤觸，你可以在設定中關閉。

### 愛商店支援哪些語言？

**English、简体中文、繁體中文。** 你還可以選擇地區名的顯示方式（地區名顯示模式）。

### 支援哪些裝置？

- **iPhone / iPad** — iOS 16.2+（主應用）
- **可配置 / 互動式小工具** — iOS 17.0+
- **控制中心控制項與 iPhone 搜尋 Tab** — iOS 18.0+
- **捷徑與 Siri** — iOS 16.2+

### 愛商店能離線使用嗎？

瀏覽與切換連結可離線使用，但**上架查詢**需要連網（呼叫 Apple 公開的查詢 API）。你的收藏、置頂地區與歷史保存在本機。

### 如何取得愛商店？

在 [App Store](https://apps.apple.com/app/id6786123132) 下載。

### 仍有問題？

聯絡 [AppleOSer@gmail.com](mailto:AppleOSer@gmail.com)，我們通常在 48 小時內回覆。

</section>
<section lang="ja" markdown="1">

### 地域の切り替えはどのように機能しますか？

iStore は、選んだ地域に対応する Apple の**公式 App Store リダイレクトリンク**を開きます。その後、App Store が Apple 自身の画面で変更の確認を求めます。iStore がお客様の Apple ID、パスワード、お支払い情報を見ることはありません。

### サインインは必要ですか？

いいえ。iStore は**アカウントもログインも不要**です。切り替えを確認するときに、Apple 自身の App Store 画面の中で、既存の Apple ID を使うだけです。

### 地域を切り替えるとログアウトされたり、アプリが消えたりしますか？

いいえ。ストアフロントを切り替えると、閲覧・購入する App Store の地域が変わります。インストール済みのアプリはそのまま残ります。新しい地域で購入するには、Apple の仕様により、請求先の地域と支払い方法が一致している必要がある場合があります。

### iStore は Apple と提携していますか？

いいえ。iStore は iHTC Studio のメンバーが開発した独立したツールで、**Apple Inc. とは提携していません。** 地域の切り替えに、Apple の公式リダイレクトリンクを使っているだけです。

### 対応している地域はいくつですか？

7 つの大陸にわたる **175 の地域**に対応し、それぞれに国旗とローカライズされた名称（English / 簡体字 / 繁体字）があります。

### アプリの提供状況の確認とは何ですか？

**App Store のリンクまたは数字のアプリ ID** を貼り付けると、iStore が（Apple の公開 iTunes Lookup API を使って）**そのアプリが提供されている地域**を調べます。確認の対象を**人気**、**お気に入り**、**すべて**の地域から選び、提供中の地域へワンタップで切り替えられます。アプリ内でも、**共有機能拡張**からでも使えます。

### 他のアプリから提供状況を確認するには？

App Store のリンク（Safari、メッセージ、App Store など）の**共有**シートで **iStore** を選びます。共有機能拡張が人気の地域を調べ、結果をアプリで開いて切り替えられます。

### お気に入りとピン留めの違いは何ですか？

**お気に入り**は、スターを付けた地域です。**ピン留め**は、すべての場所（ストア、お気に入り、ウィジェット）で常に最上部に置きたい、お気に入りの一部の地域です。お気に入りを解除すると、ピン留めからも外れます。

### 地図ピッカーとは何ですか？

各地域にピンが立つ**フルスクリーンの地図**です。対象を人気、お気に入り、すべてから選び、ピンをタップして切り替えます。場所からストアを探せる、視覚的な方法です。

### どんなウィジェットがありますか？

- **クイック地域**と**最近**のウィジェット（ホーム画面・ロック画面）
- ご自身の地域を設定できる**カスタム**ウィジェット（iOS 17 以降）
- **インタラクティブウィジェット**（iOS 17 以降）— 地域のタイルをタップして直接切り替え

### コントロールセンター用のコントロールとは何ですか？

**iOS 18 以降**では、コントロールセンターに**前回の地域に切り替え**コントロールを追加すると、直近の切り替え先の地域にワンタップで切り替え直せます。

### Siri やショートカットで切り替えられますか？

はい。iStore は、**地域の切り替え**、**前回の地域への切り替え**、**お気に入りへの切り替え**、**ストアを開く**、**提供状況の確認**を行う Siri・ショートカットのアクションを提供します。[ショートカットリンク](../url-scheme)をご覧ください。

### Spotlight 検索は使えますか？

はい。175 のすべての地域が **Spotlight** にインデックス化されています。ホーム画面から地域を検索し、結果をタップすると iStore で直接切り替えられます。

### iCloud 同期の対象は何ですか？

任意の iCloud 同期は、次の項目を端末間で揃えます：**お気に入り**、**ピン留めした地域**、**クイック地域**、**切り替え履歴**、**最後に切り替えた地域**、外観 / レイアウト / お気に入りの設定。データは iHTC Studio のサーバーではなく、**お客様のプライベートな iCloud** を通じて同期されます。同期は初期設定でオンで、設定からオフにできます。

### 切り替え前の確認をオフにできますか？

はい。誤タップを防ぐため、**切り替え前に確認**は初期設定でオンになっています。設定でオフにできます。

### iStore は何語に対応していますか？

**English、简体中文、繁體中文**に対応しています。地域名の表示方法（地域名の表示モード）も選べます。

### 対応デバイスは何ですか？

- **iPhone / iPad** — iOS 16.2 以降（メインアプリ）
- **設定可能 / インタラクティブなウィジェット** — iOS 17.0 以降
- **コントロールセンター用コントロールと iPhone の検索タブ** — iOS 18.0 以降
- **ショートカットと Siri** — iOS 16.2 以降

### iStore はオフラインで使えますか？

閲覧と切り替えリンクはオフラインでも動作しますが、**アプリの提供状況**の確認にはネットワーク接続が必要です（Apple の公開 Lookup API に問い合わせます）。お気に入り、ピン留めした地域、履歴は端末内に保存されます。

### iStore はどこで入手できますか？

[App Store](https://apps.apple.com/app/id6786123132) からダウンロードしてください。

### まだお困りですか？

[AppleOSer@gmail.com](mailto:AppleOSer@gmail.com) までご連絡ください。通常 48 時間以内に返信します。

</section>
<section lang="ko" markdown="1">

### 지역 전환은 어떻게 작동하나요?

iStore는 선택한 지역에 대한 Apple의 **공식 App Store 리디렉션 링크**를 엽니다. 그러면 App Store가 Apple의 자체 화면에서 변경 확인을 요청합니다. iStore는 Apple ID, 비밀번호, 결제 정보를 볼 수 없습니다.

### 로그인해야 하나요?

아니요. iStore는 **계정도 로그인도 필요 없습니다.** 전환을 확인할 때 Apple의 자체 App Store 화면 안에서 기존 Apple ID를 사용할 뿐입니다.

### 지역을 전환하면 로그아웃되거나 앱이 사라지나요?

아니요. 스토어프론트를 전환하면 탐색하고 구매하는 App Store의 지역이 바뀔 뿐입니다. 설치된 앱은 그대로 유지됩니다. 새 지역에서 구매하려면 Apple 정책에 따라 결제 지역과 결제 수단이 일치해야 할 수 있습니다.

### iStore는 Apple과 제휴 관계인가요?

아니요. iStore는 iHTC Studio 구성원이 만든 독립적인 도구로, **Apple Inc.와 제휴 관계가 아닙니다.** 지역을 전환하기 위해 Apple의 공식 리디렉션 링크를 사용할 뿐입니다.

### 몇 개 지역을 지원하나요?

7개 대륙에 걸친 **175개 지역**을 지원하며, 각 지역에는 국기와 현지화된 이름(English / 간체 / 번체)이 있습니다.

### 앱 제공 여부 확인이란 무엇인가요?

**App Store 링크 또는 숫자 앱 ID**를 붙여넣으면 iStore가 (Apple의 공개 iTunes Lookup API를 통해) **그 앱이 어느 지역에서 제공되는지** 확인합니다. 확인 범위를 **인기**, **즐겨찾기**, **전체** 지역으로 정하고, 제공되는 지역으로 한 번 탭해 전환할 수 있습니다. 앱 안에서도, **공유 확장**에서도 작동합니다.

### 다른 앱에서 제공 여부를 확인하려면 어떻게 하나요?

App Store 링크(Safari, 메시지, App Store 등)의 **공유** 시트에서 **iStore**를 선택하세요. 공유 확장이 인기 지역을 확인해 주고, 결과를 앱에서 열어 전환할 수 있습니다.

### 즐겨찾기와 고정의 차이는 무엇인가요?

**즐겨찾기**는 별표를 표시한 지역입니다. **고정**은 모든 곳(스토어, 즐겨찾기, 위젯)에서 항상 맨 위에 두고 싶은, 즐겨찾기의 일부 지역입니다. 지역의 즐겨찾기를 해제하면 고정에서도 제거됩니다.

### 지도 선택기란 무엇인가요?

각 지역에 핀이 표시되는 **전체 화면 지도**입니다. 범위를 인기, 즐겨찾기, 전체로 정한 뒤 핀을 탭해 전환하세요. 위치로 스토어를 둘러보는 시각적인 방법입니다.

### 어떤 위젯이 있나요?

- **빠른 지역**과 **최근** 위젯(홈 및 잠금 화면)
- 원하는 지역으로 설정할 수 있는 **사용자 지정** 위젯(iOS 17 이상)
- **인터랙티브 위젯**(iOS 17 이상) — 지역 타일을 탭해 바로 전환

### 제어 센터 컨트롤이란 무엇인가요?

**iOS 18 이상**에서는 제어 센터에 **마지막 지역으로 전환** 컨트롤을 추가하면 가장 최근 대상 지역으로 한 번에 다시 전환할 수 있습니다.

### Siri나 단축어로 전환할 수 있나요?

네. iStore는 **지역 전환**, **마지막 지역으로 전환**, **즐겨찾기 지역으로 전환**, **스토어 열기**, **제공 여부 확인**을 위한 Siri 및 단축어 동작을 제공합니다. [바로가기 링크](../url-scheme)를 참고하세요.

### Spotlight 검색이 작동하나요?

네. 175개 지역이 모두 **Spotlight**에 색인되어 있습니다. 홈 화면에서 지역을 검색하고 결과를 탭하면 iStore에서 바로 전환할 수 있습니다.

### iCloud 동기화는 무엇을 포함하나요?

선택적 iCloud 동기화는 다음 항목을 기기 간에 맞춰 줍니다: **즐겨찾기**, **고정한 지역**, **빠른 지역**, **전환 기록**, **마지막으로 전환한 지역**, 화면 / 레이아웃 / 즐겨찾기 설정. 데이터는 iHTC Studio 서버가 아니라 **개인 iCloud**를 통해 동기화됩니다. 동기화는 기본값이 켜짐이며 설정에서 끌 수 있습니다.

### 전환 전 확인을 끌 수 있나요?

네. 잘못 누르는 것을 막기 위해 **전환 전 확인**은 기본값이 켜짐이며, 설정에서 끌 수 있습니다.

### iStore는 어떤 언어를 지원하나요?

**English, 简体中文, 繁體中文**을 지원합니다. 지역 이름을 표시하는 방식(지역 이름 표시 방식)도 선택할 수 있습니다.

### 어떤 기기를 지원하나요?

- **iPhone / iPad** — iOS 16.2 이상(메인 앱)
- **구성 가능 / 인터랙티브 위젯** — iOS 17.0 이상
- **제어 센터 컨트롤 및 iPhone 검색 탭** — iOS 18.0 이상
- **단축어 및 Siri** — iOS 16.2 이상

### iStore는 오프라인에서도 작동하나요?

탐색과 전환 링크는 오프라인에서도 작동하지만, **앱 제공 여부** 확인에는 네트워크 연결이 필요합니다(Apple의 공개 Lookup API를 조회합니다). 즐겨찾기, 고정한 지역, 기록은 기기에 저장됩니다.

### iStore는 어디서 받을 수 있나요?

[App Store](https://apps.apple.com/app/id6786123132)에서 다운로드하세요.

### 더 도움이 필요하신가요?

[AppleOSer@gmail.com](mailto:AppleOSer@gmail.com)으로 문의해 주세요. 보통 48시간 이내에 답변드립니다.

</section>
<section lang="ru" markdown="1">

### Как работает смена региона?

iStore открывает **официальную ссылку-перенаправление App Store** от Apple для выбранного вами региона. Затем App Store просит вас подтвердить изменение на собственном экране Apple. iStore никогда не видит ваш Apple ID, пароль или платёжные данные.

### Нужно ли входить в аккаунт?

Нет. iStore **не требует ни учётной записи, ни входа**. Вы взаимодействуете со своим существующим Apple ID только внутри собственного экрана App Store от Apple, когда подтверждаете переключение.

### Приведёт ли смена региона к выходу из аккаунта или потере приложений?

Нет. Смена региона магазина меняет только то, в каком региональном App Store вы просматриваете и покупаете. Установленные приложения остаются на месте. Apple может требовать, чтобы ваш платёжный регион и способ оплаты совпадали, прежде чем вы сможете покупать в новом регионе.

### Связано ли iStore с Apple?

Нет. iStore — независимый инструмент, созданный участниками iHTC Studio. Он **не связан с Apple Inc.** Для смены региона он просто использует официальную ссылку-перенаправление Apple.

### Сколько регионов поддерживается?

**175 регионов** на 7 континентах, у каждого — флаг и локализованное название (английский / упрощённый / традиционный китайский).

### Что такое проверка доступности приложения?

Вставьте **ссылку на App Store или числовой ID приложения**, и iStore проверит (через публичный API iTunes Lookup от Apple), **в каких регионах приложение доступно**. Ограничьте проверку регионами **«Популярные»**, **«Избранное»** или **«Все»**, затем одним нажатием переключитесь на любой доступный регион. Работает в приложении и из **расширения «Поделиться»**.

### Как проверить доступность из другого приложения?

Используйте меню **«Поделиться»** для любой ссылки на App Store (Safari, «Сообщения», App Store и т. д.) и выберите **iStore**. Расширение «Поделиться» проверит популярные регионы и позволит открыть результат в приложении для переключения.

### В чём разница между «Избранным» и «Закреплёнными»?

**Избранное** — регионы, которые вы отметили звёздочкой. **Закреплённые** — подмножество, которое вы хотите всегда держать в самом верху везде (в магазине, избранном и виджетах). Если убрать регион из избранного, он также перестаёт быть закреплённым.

### Что такое «Выбор на карте»?

**Полноэкранная карта** с отметкой для каждого региона. Ограничьте её регионами «Популярные», «Избранное» или «Все», затем нажмите на отметку, чтобы переключиться. Это наглядный способ изучать магазины по расположению.

### Какие виджеты доступны?

- Виджеты **«Быстрые регионы»** и **«Недавние»** (экран «Домой» и экран блокировки)
- **Настраиваемый** виджет, для которого вы выбираете собственные регионы (iOS 17+)
- **Интерактивные виджеты** (iOS 17+) — нажмите на плитку региона, чтобы переключиться сразу

### Что за элемент Пункта управления?

В **iOS 18+** добавьте в Пункт управления элемент **«Вернуть последний»**, чтобы одним нажатием снова переключиться на последний выбранный регион.

### Можно ли переключаться через Siri или «Быстрые команды»?

Да. iStore предоставляет действия для Siri и «Быстрых команд»: **сменить регион**, **вернуть последний регион**, **переключиться на регион из избранного**, **открыть магазин** и **проверить доступность**. См. [Ссылки быстрых команд](../url-scheme).

### Работает ли поиск Spotlight?

Да. Все 175 регионов проиндексированы в **Spotlight** — найдите регион на экране «Домой» и нажмите на результат, чтобы переключиться прямо в iStore.

### Что охватывает синхронизация через iCloud?

Необязательная синхронизация iCloud поддерживает одинаковыми на ваших устройствах: **избранное**, **закреплённые регионы**, **быстрые регионы**, **историю переключений**, **последний выбранный регион** и настройки оформления / раскладки / избранного. Данные синхронизируются через **ваш личный iCloud**, а не через серверы iHTC Studio. По умолчанию синхронизация включена; её можно отключить в настройках.

### Можно ли отключить подтверждение перед переключением?

Да. **Подтверждение перед переключением** включено по умолчанию, чтобы избежать случайных нажатий; его можно отключить в настройках.

### Какие языки поддерживает iStore?

**English, 简体中文 и 繁體中文.** Вы также можете выбрать, как отображаются названия регионов (режим отображения названий регионов).

### Какие устройства поддерживаются?

- **iPhone / iPad** — iOS 16.2+ (основное приложение)
- **Настраиваемые / интерактивные виджеты** — iOS 17.0+
- **Элемент Пункта управления и вкладка поиска на iPhone** — iOS 18.0+
- **«Быстрые команды» и Siri** — iOS 16.2+

### Работает ли iStore офлайн?

Просмотр и ссылки для переключения работают офлайн, но для проверки **доступности приложения** нужно подключение к сети (запрашивается публичный API Lookup от Apple). Ваше избранное, закреплённые регионы и история сохраняются на устройстве.

### Где скачать iStore?

Загрузите из [App Store](https://apps.apple.com/app/id6786123132).

### Нужна дополнительная помощь?

Напишите на [AppleOSer@gmail.com](mailto:AppleOSer@gmail.com). Обычно мы отвечаем в течение 48 часов.

</section>
<section lang="th" markdown="1">

### การสลับภูมิภาคทำงานอย่างไร

iStore จะเปิด **ลิงก์เปลี่ยนเส้นทาง App Store อย่างเป็นทางการ** ของ Apple สำหรับภูมิภาคที่คุณเลือก จากนั้น App Store จะให้คุณยืนยันการเปลี่ยนแปลงบนหน้าจอของ Apple เอง iStore ไม่เคยเห็น Apple ID รหัสผ่าน หรือรายละเอียดการชำระเงินของคุณ

### ต้องลงชื่อเข้าใช้ไหม

ไม่ต้อง iStore **ไม่ต้องมีบัญชีและไม่ต้องเข้าสู่ระบบ** คุณใช้ Apple ID ที่มีอยู่เฉพาะภายในหน้าจอ App Store ของ Apple เองเมื่อยืนยันการสลับ

### การสลับภูมิภาคจะทำให้ออกจากระบบหรือแอปหายไปไหม

ไม่ การสลับร้านค้าเพียงเปลี่ยนว่าคุณเรียกดูและซื้อจาก App Store ของภูมิภาคใด แอปที่ติดตั้งแล้วจะยังอยู่ Apple อาจกำหนดให้ภูมิภาคการเรียกเก็บเงินและวิธีชำระเงินของคุณต้องตรงกันก่อนจึงจะซื้อในภูมิภาคใหม่ได้

### iStore เกี่ยวข้องกับ Apple หรือไม่

ไม่ iStore เป็นเครื่องมืออิสระที่สร้างโดยผู้ร่วมงานของ iHTC Studio และ **ไม่มีความเกี่ยวข้องกับ Apple Inc.** แอปเพียงใช้ลิงก์เปลี่ยนเส้นทางอย่างเป็นทางการของ Apple เพื่อสลับภูมิภาค

### รองรับกี่ภูมิภาค

**175 ภูมิภาค** ใน 7 ทวีป แต่ละภูมิภาคมีธงและชื่อที่แปลเป็นภาษาท้องถิ่น (อังกฤษ / จีนตัวย่อ / จีนตัวเต็ม)

### การตรวจสอบความพร้อมให้บริการของแอปคืออะไร

วาง **ลิงก์ App Store หรือ App ID ที่เป็นตัวเลข** แล้ว iStore จะตรวจสอบ (ผ่าน iTunes Lookup API สาธารณะของ Apple) ว่า **แอปมีให้บริการในภูมิภาคใดบ้าง** กำหนดขอบเขตการตรวจสอบเป็นภูมิภาค **ยอดนิยม** **รายการโปรด** หรือ **ทั้งหมด** แล้วสลับไปยังภูมิภาคที่มีให้บริการได้ด้วยการแตะครั้งเดียว ใช้งานได้ทั้งในแอปและจาก **ส่วนขยายการแชร์ (Share Extension)**

### ตรวจสอบความพร้อมให้บริการจากแอปอื่นได้อย่างไร

ใช้ชีต **แชร์** บนลิงก์ App Store ใดก็ได้ (Safari, ข้อความ, App Store ฯลฯ) แล้วเลือก **iStore** ส่วนขยายการแชร์จะตรวจสอบภูมิภาคยอดนิยมและให้คุณเปิดผลลัพธ์ในแอปเพื่อสลับได้

### รายการโปรดกับภูมิภาคที่ปักหมุดต่างกันอย่างไร

**รายการโปรด** คือภูมิภาคที่คุณติดดาว ส่วน **ภูมิภาคที่ปักหมุด** เป็นส่วนย่อยที่คุณต้องการให้อยู่บนสุดเสมอในทุกที่ (ร้านค้า รายการโปรด และวิดเจ็ต) การเลิกเป็นรายการโปรดของภูมิภาคหนึ่งจะนำออกจากการปักหมุดด้วย

### ตัวเลือกบนแผนที่คืออะไร

**แผนที่เต็มหน้าจอ** ที่มีหมุดสำหรับแต่ละภูมิภาค กำหนดขอบเขตเป็นยอดนิยม รายการโปรด หรือทั้งหมด แล้วแตะหมุดเพื่อสลับ เป็นวิธีสำรวจร้านค้าตามตำแหน่งที่ตั้งแบบเห็นภาพ

### มีวิดเจ็ตอะไรบ้าง

- วิดเจ็ต **ภูมิภาคด่วน** และ **ล่าสุด** (หน้าจอหลักและหน้าจอล็อก)
- วิดเจ็ต **กำหนดเอง** ที่คุณตั้งค่าด้วยภูมิภาคของคุณเอง (iOS 17+)
- **วิดเจ็ตแบบโต้ตอบ** (iOS 17+) — แตะไทล์ภูมิภาคเพื่อสลับโดยตรง

### ตัวควบคุมใน Control Center คืออะไร

บน **iOS 18+** เพิ่มตัวควบคุม **สลับกลับภูมิภาคล่าสุด** ใน Control Center เพื่อสลับกลับไปยังภูมิภาคปลายทางล่าสุดได้ด้วยการแตะครั้งเดียว

### สลับด้วย Siri หรือคำสั่งลัดได้ไหม

ได้ iStore มีการทำงานสำหรับ Siri และคำสั่งลัดเพื่อ **สลับภูมิภาค** **สลับกลับภูมิภาคล่าสุด** **สลับไปยังภูมิภาคที่เป็นรายการโปรด** **เปิดร้านค้า** หรือ **ตรวจสอบความพร้อมให้บริการ** ดู [ลิงก์ทางลัด](../url-scheme)

### การค้นหาด้วย Spotlight ใช้ได้ไหม

ได้ ทั้ง 175 ภูมิภาคถูกจัดทำดัชนีใน **Spotlight** — ค้นหาภูมิภาคจากหน้าจอหลักแล้วแตะผลลัพธ์เพื่อสลับใน iStore ได้โดยตรง

### การซิงค์ iCloud ครอบคลุมอะไรบ้าง

การซิงค์ iCloud แบบเลือกใช้ช่วยให้สิ่งเหล่านี้ตรงกันในทุกอุปกรณ์ของคุณ: **รายการโปรด** **ภูมิภาคที่ปักหมุด** **ภูมิภาคด่วน** **ประวัติการสลับ** **ภูมิภาคที่สลับล่าสุด** และการตั้งค่ารูปลักษณ์ / เค้าโครง / รายการโปรด ข้อมูลจะซิงค์ผ่าน **iCloud ส่วนตัวของคุณ** ไม่ใช่เซิร์ฟเวอร์ของ iHTC Studio การซิงค์เปิดไว้เป็นค่าเริ่มต้นและปิดได้ในการตั้งค่า

### ปิดการยืนยันก่อนสลับได้ไหม

ได้ **ยืนยันก่อนสลับ** เปิดไว้เป็นค่าเริ่มต้นเพื่อป้องกันการแตะผิด คุณปิดได้ในการตั้งค่า

### iStore รองรับภาษาอะไรบ้าง

**English, 简体中文 และ 繁體中文** คุณยังเลือกวิธีแสดงชื่อภูมิภาคได้ด้วย (โหมดการแสดงชื่อภูมิภาค)

### รองรับอุปกรณ์อะไรบ้าง

- **iPhone / iPad** — iOS 16.2+ (แอปหลัก)
- **วิดเจ็ตที่ตั้งค่าได้ / โต้ตอบได้** — iOS 17.0+
- **ตัวควบคุม Control Center และแท็บค้นหาบน iPhone** — iOS 18.0+
- **คำสั่งลัดและ Siri** — iOS 16.2+

### iStore ใช้งานแบบออฟไลน์ได้ไหม

การเรียกดูและลิงก์สลับทำงานแบบออฟไลน์ได้ แต่การตรวจสอบ **ความพร้อมให้บริการของแอป** ต้องใช้การเชื่อมต่อเครือข่าย (เป็นการเรียก Lookup API สาธารณะของ Apple) รายการโปรด ภูมิภาคที่ปักหมุด และประวัติของคุณบันทึกไว้บนอุปกรณ์

### ดาวน์โหลด iStore ได้อย่างไร

ดาวน์โหลดจาก [App Store](https://apps.apple.com/app/id6786123132)

### ยังต้องการความช่วยเหลือไหม

ติดต่อ [AppleOSer@gmail.com](mailto:AppleOSer@gmail.com) โดยปกติเราจะตอบกลับภายใน 48 ชั่วโมง

</section>
<section lang="de" markdown="1">

### Wie funktioniert das Wechseln der Region?

iStore öffnet Apples **offiziellen App-Store-Weiterleitungslink** für die von Ihnen gewählte Region. Der App Store bittet Sie dann auf Apples eigenem Bildschirm, die Änderung zu bestätigen. iStore sieht niemals Ihre Apple-ID, Ihr Passwort oder Ihre Zahlungsdaten.

### Muss ich mich anmelden?

Nein. iStore erfordert **kein Konto und keine Anmeldung**. Sie interagieren mit Ihrer vorhandenen Apple-ID nur auf Apples eigenem App-Store-Bildschirm, wenn Sie einen Wechsel bestätigen.

### Werde ich beim Wechseln der Region abgemeldet oder verliere meine Apps?

Nein. Das Wechseln der Storefront ändert nur, aus welchem regionalen App Store Sie stöbern und kaufen. Ihre installierten Apps bleiben installiert. Apple kann verlangen, dass Ihre Rechnungsregion und Zahlungsmethode übereinstimmen, bevor Sie in einer neuen Region kaufen können.

### Ist iStore mit Apple verbunden?

Nein. iStore ist ein unabhängiges Werkzeug von Mitwirkenden bei iHTC Studio. Es steht **in keiner Verbindung zu Apple Inc.** und nutzt lediglich Apples offiziellen Weiterleitungslink zum Wechseln der Region.

### Wie viele Regionen werden unterstützt?

**175 Regionen** auf 7 Kontinenten, jeweils mit Flagge und lokalisiertem Namen (Englisch / vereinfachtes / traditionelles Chinesisch).

### Was ist die Verfügbarkeitsprüfung?

Fügen Sie einen **App-Store-Link oder eine numerische App-ID** ein, und iStore prüft (über Apples öffentliche iTunes-Lookup-API), **in welchen Regionen die App verfügbar ist**. Beschränken Sie die Prüfung auf **Beliebte**, **Favoriten** oder **alle** Regionen und wechseln Sie dann mit einem Tipp in eine verfügbare Region. Das funktioniert in der App und über die **Share-Extension**.

### Wie prüfe ich die Verfügbarkeit aus einer anderen App?

Nutzen Sie das **Teilen**-Menü bei einem beliebigen App-Store-Link (Safari, Nachrichten, App Store usw.) und wählen Sie **iStore**. Die Share-Extension prüft beliebte Regionen und lässt Sie das Ergebnis in der App öffnen, um zu wechseln.

### Was ist der Unterschied zwischen Favoriten und Angeheftet?

**Favoriten** sind die Regionen, die Sie mit einem Stern markieren. **Angeheftete** Regionen sind eine Teilmenge, die überall ganz oben bleiben soll (Store, Favoriten und Widgets). Wenn Sie eine Region aus den Favoriten entfernen, wird sie auch nicht mehr angeheftet.

### Was ist die Kartenauswahl?

Eine **Vollbildkarte** mit einer Markierung für jede Region. Beschränken Sie sie auf Beliebte, Favoriten oder alle und tippen Sie dann auf eine Markierung, um zu wechseln. So erkunden Sie Stores anschaulich nach Standort.

### Welche Widgets gibt es?

- Widgets **Schnellregionen** und **Zuletzt** (Home- und Sperrbildschirm)
- Ein **eigenes** Widget, das Sie mit Ihren Regionen konfigurieren (iOS 17+)
- **Interaktive Widgets** (iOS 17+) — auf eine Regionskachel tippen, um direkt zu wechseln

### Was ist das Steuerelement im Kontrollzentrum?

Ab **iOS 18** können Sie das Steuerelement **Zuletzt wechseln** zum Kontrollzentrum hinzufügen, um mit einem Tipp erneut in Ihre zuletzt gewählte Region zu wechseln.

### Kann ich mit Siri oder Kurzbefehlen wechseln?

Ja. iStore bietet Siri- und Kurzbefehle-Aktionen, um **eine Region zu wechseln**, **zur letzten Region zu wechseln**, **zu einer Favoritenregion zu wechseln**, **den Store zu öffnen** oder **die Verfügbarkeit zu prüfen**. Siehe [Kurzbefehl-Links](../url-scheme).

### Funktioniert die Spotlight-Suche?

Ja. Alle 175 Regionen sind in **Spotlight** indiziert — suchen Sie vom Home-Bildschirm aus nach einer Region und tippen Sie auf das Ergebnis, um direkt in iStore zu wechseln.

### Was umfasst die iCloud-Synchronisierung?

Die optionale iCloud-Synchronisierung hält Folgendes auf Ihren Geräten abgeglichen: **Favoriten**, **angeheftete Regionen**, **Schnellregionen**, **Wechselverlauf**, **zuletzt gewechselte Region** sowie Einstellungen zu Darstellung / Layout / Favoriten. Die Daten werden über **Ihr privates iCloud** synchronisiert — nicht über Server von iHTC Studio. Die Synchronisierung ist standardmäßig an und lässt sich in den Einstellungen ausschalten.

### Kann ich die Bestätigung vor dem Wechsel ausschalten?

Ja. **Vor dem Wechsel bestätigen** ist standardmäßig an, um Fehltipps zu vermeiden; Sie können es in den Einstellungen deaktivieren.

### Welche Sprachen unterstützt iStore?

**English, 简体中文 und 繁體中文.** Außerdem können Sie wählen, wie Regionsnamen angezeigt werden (Anzeigemodus der Regionsnamen).

### Welche Geräte werden unterstützt?

- **iPhone / iPad** — iOS 16.2+ (Haupt-App)
- **Konfigurierbare / interaktive Widgets** — iOS 17.0+
- **Steuerelement im Kontrollzentrum und Suchtab auf dem iPhone** — iOS 18.0+
- **Kurzbefehle und Siri** — iOS 16.2+

### Funktioniert iStore offline?

Stöbern und Wechsel-Links funktionieren offline, aber die **Verfügbarkeitsprüfung** benötigt eine Netzwerkverbindung (sie fragt Apples öffentliche Lookup-API ab). Ihre Favoriten, angehefteten Regionen und Ihr Verlauf werden auf Ihrem Gerät gespeichert.

### Wie bekomme ich iStore?

Laden Sie die App im [App Store](https://apps.apple.com/app/id6786123132) herunter.

### Brauchen Sie noch Hilfe?

Kontaktieren Sie [AppleOSer@gmail.com](mailto:AppleOSer@gmail.com). Wir antworten in der Regel innerhalb von 48 Stunden.

</section>
<section lang="fr" markdown="1">

### Comment fonctionne le changement de région ?

iStore ouvre le **lien de redirection officiel de l'App Store** d'Apple pour la région que vous choisissez. L'App Store vous demande ensuite de confirmer le changement sur l'écran d'Apple. iStore ne voit jamais votre identifiant Apple, votre mot de passe ni vos informations de paiement.

### Dois-je me connecter ?

Non. iStore ne nécessite **ni compte ni connexion**. Vous n'interagissez avec votre identifiant Apple existant que dans l'écran de l'App Store d'Apple lorsque vous confirmez un changement.

### Changer de région me déconnectera-t-il ou me fera-t-il perdre mes apps ?

Non. Changer de boutique modifie seulement l'App Store régional dans lequel vous naviguez et achetez. Vos apps installées restent installées. Apple peut exiger que votre région de facturation et votre moyen de paiement correspondent avant de pouvoir acheter dans une nouvelle région.

### iStore est-il affilié à Apple ?

Non. iStore est un outil indépendant créé par des contributeurs d'iHTC Studio. Il **n'est pas affilié à Apple Inc.** Il utilise simplement le lien de redirection officiel d'Apple pour changer de région.

### Combien de régions sont prises en charge ?

**175 régions** sur 7 continents, chacune avec son drapeau et un nom localisé (anglais / chinois simplifié / chinois traditionnel).

### Qu'est-ce que la vérification de disponibilité des apps ?

Collez un **lien App Store ou un identifiant d'app numérique** et iStore vérifie (via l'API publique iTunes Lookup d'Apple) **dans quelles régions l'app est disponible**. Limitez la vérification aux régions **Populaires**, **Favoris** ou **Toutes**, puis passez à n'importe quelle région disponible d'un seul geste. Cela fonctionne dans l'app et depuis l'**extension de partage**.

### Comment vérifier la disponibilité depuis une autre app ?

Utilisez la feuille **Partager** sur n'importe quel lien App Store (Safari, Messages, App Store, etc.) et choisissez **iStore**. L'extension de partage vérifie les régions populaires et vous permet d'ouvrir le résultat dans l'app pour changer de région.

### Quelle est la différence entre Favoris et Épinglées ?

Les **Favoris** sont les régions que vous marquez d'une étoile. Les régions **épinglées** sont un sous-ensemble que vous voulez garder tout en haut partout (Store, favoris et widgets). Retirer une région des favoris la retire aussi des épinglées.

### Qu'est-ce que le sélecteur de carte ?

Une **carte plein écran** avec une épingle pour chaque région. Limitez-la aux régions Populaires, Favoris ou Toutes, puis touchez une épingle pour changer de région. C'est une façon visuelle d'explorer les boutiques par localisation.

### Quels widgets sont disponibles ?

- Widgets **Régions rapides** et **Récentes** (écran d'accueil et écran verrouillé)
- Un widget **Personnalisé** que vous configurez avec vos propres régions (iOS 17+)
- **Widgets interactifs** (iOS 17+) — touchez une vignette de région pour changer directement

### Qu'est-ce que le contrôle du Centre de contrôle ?

Sous **iOS 18+**, ajoutez le contrôle **Revenir à la dernière** au Centre de contrôle pour basculer de nouveau vers votre dernière région cible d'un seul geste.

### Puis-je changer de région avec Siri ou Raccourcis ?

Oui. iStore propose des actions Siri et Raccourcis pour **changer de région**, **revenir à la dernière région**, **passer à une région favorite**, **ouvrir le Store** ou **vérifier la disponibilité**. Voir [Liens de raccourcis](../url-scheme).

### La recherche Spotlight fonctionne-t-elle ?

Oui. Les 175 régions sont indexées dans **Spotlight** — cherchez une région depuis l'écran d'accueil et touchez le résultat pour changer directement dans iStore.

### Que couvre la synchronisation iCloud ?

La synchronisation iCloud facultative garde ces éléments à jour sur vos appareils : **favoris**, **régions épinglées**, **régions rapides**, **historique de changements**, **dernière région utilisée**, ainsi que les préférences d'apparence / de disposition / de favoris. Les données sont synchronisées via **votre iCloud privé** — et non via les serveurs d'iHTC Studio. La synchronisation est activée par défaut et peut être désactivée dans les Réglages.

### Puis-je désactiver la confirmation avant de changer ?

Oui. **Confirmer avant de changer** est activé par défaut pour éviter les faux appuis ; vous pouvez le désactiver dans les Réglages.

### Quelles langues iStore prend-il en charge ?

**English, 简体中文 et 繁體中文.** Vous pouvez aussi choisir la façon dont les noms de régions sont affichés (mode d'affichage des noms de régions).

### Quels appareils sont pris en charge ?

- **iPhone / iPad** — iOS 16.2+ (app principale)
- **Widgets configurables / interactifs** — iOS 17.0+
- **Contrôle du Centre de contrôle et onglet Recherche sur iPhone** — iOS 18.0+
- **Raccourcis et Siri** — iOS 16.2+

### iStore fonctionne-t-il hors ligne ?

La navigation et les liens de changement fonctionnent hors ligne, mais la **vérification de disponibilité des apps** nécessite une connexion réseau (elle interroge l'API publique Lookup d'Apple). Vos favoris, régions épinglées et historique sont enregistrés sur votre appareil.

### Comment obtenir iStore ?

Téléchargez-le depuis l'[App Store](https://apps.apple.com/app/id6786123132).

### Besoin d'aide supplémentaire ?

Contactez [AppleOSer@gmail.com](mailto:AppleOSer@gmail.com). Nous répondons généralement sous 48 heures.

</section>
<section lang="tr" markdown="1">

### Bölge değiştirme nasıl çalışır?

iStore, seçtiğiniz bölge için Apple'ın **resmi App Store yönlendirme bağlantısını** açar. Ardından App Store, değişikliği Apple'ın kendi ekranında onaylamanızı ister. iStore Apple Kimliğinizi, parolanızı veya ödeme ayrıntılarınızı asla görmez.

### Oturum açmam gerekiyor mu?

Hayır. iStore **hesap ve giriş gerektirmez**. Mevcut Apple Kimliğinizle yalnızca bir değiştirmeyi onayladığınızda Apple'ın kendi App Store ekranında etkileşime girersiniz.

### Bölge değiştirmek oturumumu kapatır veya uygulamalarımı kaybettirir mi?

Hayır. Mağaza bölgesini değiştirmek yalnızca hangi bölgenin App Store'unda gezindiğinizi ve alışveriş yaptığınızı değiştirir. Yüklü uygulamalarınız yüklü kalır. Apple, yeni bir bölgede satın alma yapabilmeniz için fatura bölgenizin ve ödeme yönteminizin eşleşmesini isteyebilir.

### iStore, Apple ile bağlantılı mı?

Hayır. iStore, iHTC Studio katkıda bulunanları tarafından geliştirilmiş bağımsız bir araçtır ve **Apple Inc. ile bağlantılı değildir.** Bölge değiştirmek için yalnızca Apple'ın resmi yönlendirme bağlantısını kullanır.

### Kaç bölge destekleniyor?

7 kıtada **175 bölge**; her birinin bayrağı ve yerelleştirilmiş adı (İngilizce / Basitleştirilmiş / Geleneksel Çince) vardır.

### Uygulama Kullanılabilirliği kontrolü nedir?

Bir **App Store bağlantısı veya sayısal Uygulama Kimliği** yapıştırın; iStore (Apple'ın herkese açık iTunes Lookup API'si aracılığıyla) **uygulamanın hangi bölgelerde bulunduğunu** kontrol eder. Kontrolü **Popüler**, **Favoriler** veya **Tüm** bölgelerle sınırlayın, ardından tek dokunuşla kullanılabilir herhangi bir bölgeye geçin. Hem uygulamada hem de **Paylaşım Uzantısı**'ndan çalışır.

### Başka bir uygulamadan kullanılabilirliği nasıl kontrol ederim?

Herhangi bir App Store bağlantısında (Safari, Mesajlar, App Store vb.) **Paylaş** sayfasını kullanın ve **iStore**'u seçin. Paylaşım Uzantısı popüler bölgeleri kontrol eder ve sonucu geçiş yapmak için uygulamada açmanızı sağlar.

### Favoriler ile Sabitlenenler arasındaki fark nedir?

**Favoriler**, yıldızladığınız bölgelerdir. **Sabitlenmiş** bölgeler ise her yerde (mağaza, favoriler ve widget'lar) en üstte tutmak istediğiniz bir alt kümedir. Bir bölgeyi favorilerden çıkarmak, onu sabitlenenlerden de kaldırır.

### Harita Seçici nedir?

Her bölge için bir iğne bulunan **tam ekran harita**. Popüler, Favoriler veya Tümü ile sınırlayın, ardından geçiş yapmak için bir iğneye dokunun. Mağazaları konuma göre görsel olarak keşfetmenin bir yoludur.

### Hangi widget'lar var?

- **Hızlı Bölgeler** ve **Son Kullanılanlar** widget'ları (Ana ve Kilit Ekranı)
- Kendi bölgelerinizle yapılandırdığınız **Özel** widget (iOS 17+)
- **Etkileşimli widget'lar** (iOS 17+) — doğrudan geçiş yapmak için bir bölge kutucuğuna dokunun

### Denetim Merkezi kontrolü nedir?

**iOS 18+** sürümünde, en son hedef bölgenize tek dokunuşla yeniden geçmek için Denetim Merkezi'ne **Sonuncuya Geç** kontrolünü ekleyin.

### Siri veya Kısayollar ile geçiş yapabilir miyim?

Evet. iStore, **bir bölgeye geçmek**, **son bölgeye geçmek**, **bir favoriye geçmek**, **mağazayı açmak** veya **kullanılabilirliği kontrol etmek** için Siri ve Kısayollar eylemleri sunar. Bkz. [Kısayol Bağlantıları](../url-scheme).

### Spotlight araması çalışıyor mu?

Evet. 175 bölgenin tamamı **Spotlight**'ta dizinlenmiştir — Ana Ekran'dan bir bölge arayın ve sonuca dokunarak doğrudan iStore'da geçiş yapın.

### iCloud Senkronizasyonu neleri kapsar?

İsteğe bağlı iCloud senkronizasyonu şunları cihazlarınız arasında eşit tutar: **favoriler**, **sabitlenmiş bölgeler**, **hızlı bölgeler**, **değiştirme geçmişi**, **son değiştirilen bölge** ve görünüm / düzen / favoriler tercihleri. Veriler iHTC Studio sunucuları üzerinden değil, **özel iCloud'unuz** üzerinden senkronize edilir. Senkronizasyon varsayılan olarak açıktır ve Ayarlar'dan kapatılabilir.

### Değiştirmeden önceki onayı kapatabilir miyim?

Evet. Yanlış dokunuşları önlemek için **Değiştirmeden önce onayla** varsayılan olarak açıktır; Ayarlar'dan devre dışı bırakabilirsiniz.

### iStore hangi dilleri destekler?

**English, 简体中文 ve 繁體中文.** Bölge adlarının nasıl görüntüleneceğini de seçebilirsiniz (bölge adı görüntüleme modu).

### Hangi cihazlar desteklenir?

- **iPhone / iPad** — iOS 16.2+ (ana uygulama)
- **Yapılandırılabilir / etkileşimli widget'lar** — iOS 17.0+
- **Denetim Merkezi kontrolü ve iPhone Arama sekmesi** — iOS 18.0+
- **Kısayollar ve Siri** — iOS 16.2+

### iStore çevrimdışı çalışır mı?

Göz atma ve geçiş bağlantıları çevrimdışı çalışır, ancak **Uygulama Kullanılabilirliği** kontrolü ağ bağlantısı gerektirir (Apple'ın herkese açık Lookup API'sini sorgular). Favorileriniz, sabitlenmiş bölgeleriniz ve geçmişiniz cihazınıza kaydedilir.

### iStore'u nasıl edinirim?

[App Store](https://apps.apple.com/app/id6786123132)'dan indirin.

### Hâlâ yardıma mı ihtiyacınız var?

[AppleOSer@gmail.com](mailto:AppleOSer@gmail.com) ile iletişime geçin. Genellikle 48 saat içinde yanıt veririz.

</section>
