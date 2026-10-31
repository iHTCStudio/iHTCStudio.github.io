---
layout: doc
title: iStore — Shortcut Links
app_id: iStore
doc_title_en: Shortcut Links
doc_title_zh_cn: 快捷链接说明
doc_title_zh_tw: 快捷連結說明
description: istore:// shortcut links — switch a region, switch last, open tabs, availability check, guides, and Siri & Shortcuts.
---

<section lang="en" markdown="1">

iStore supports **`istore://`** shortcut links. Use them in **Shortcuts**, Safari bookmarks, or from **widgets**, **Control Center**, **Spotlight**, and the **Share Extension** to **switch a region**, **re-switch your last region**, **open a tab**, or **jump to a guide**.

## Link format

```
istore://{host}?{params}
```

Hosts are **case-insensitive**. Region codes use standard **Alpha-2** values (`us`, `cn`, `jp`, `hk`, `tw`, …).

| What you want | Link |
|---------------|------|
| Switch to a region | `istore://switch?region={code}` |
| Switch to your last region | `istore://switch-last` |
| Open the Store / Favorites / Settings tab | `istore://store` · `istore://favorites` · `istore://settings` |
| Open App Availability | `istore://availability` |

---

## Switch to a region

Requests a switch to the given region (routed through the in-app confirmation, if enabled).

```
istore://switch?region={code}
```

| Parameter | Required | Description |
|-----------|----------|-------------|
| `region` | **Yes** | Region code, e.g. `us`, `cn`, `jp`, `hk`, `tw` |

**Example**

```
istore://switch?region=us
```

Used by: **interactive widgets**, **Spotlight** results, and **Shortcuts / Siri**.

---

## Switch to your last region

```
istore://switch-last
```

Reads your most recent switch target and switches to it again. Powers the **Switch Last** Control Center control (iOS 18+) and the matching Shortcut / Siri action.

---

## Tabs & pages (no query)

| URL | Opens |
|-----|-------|
| `istore://store` | Store tab |
| `istore://favorites` | Favorites tab |
| `istore://settings` | Settings tab |
| `istore://availability` | Settings → App Availability (also used by the Share Extension) |
| `istore://switch-history` | Switch History |
| `istore://quick-regions` | Quick Regions settings |
| `istore://feature-guide` | Feature guide |
| `istore://widget-guide` | Widget guide |
| `istore://shortcuts-guide` | Shortcuts guide |
| `istore://usage-guide` | Usage guide |
| `istore://feedback` | Feedback email |
| `istore://in-app-review` | In-app App Store rating |

---

## Widgets, Control Center & Spotlight

These generate `istore://` links automatically when you tap:

| Source | Tap target | Effect |
|--------|------------|--------|
| **Quick Regions / Recent / Custom widget** | A region tile | `istore://switch?region=…` |
| **Switch Last control** (iOS 18+) | The control | `istore://switch-last` |
| **Spotlight** | A region result | `istore://switch?region=…` |

Interactive switching from widgets and Control Center opens the app to complete the official App Store redirect.

---

## Share Extension

Share any **App Store link** into iStore. The Share Extension checks availability across popular regions, then can open the app via `istore://availability` so you can review the result and switch.

---

## Siri & Shortcuts

Find built-in actions in the **Shortcuts** app or ask **Siri**. Titles and phrases are localized in English / 简体中文 / 繁體中文.

| Action | What you can set | Effect |
|--------|------------------|--------|
| Switch region | Region | Switches to that region |
| Switch last region | — | Switches to your last target |
| Switch favorite region | A favorite | Switches to a favorited region |
| Open store | — | Opens iStore |
| Check availability | App link or ID | Checks where the app is available |

---

## Region codes in links

Deep links and widget-generated URLs always use stable **region codes** (`us`, `cn`, `hk`, `tw`, …) — not localized display names.

**Examples**

```
istore://switch?region=jp
istore://switch?region=hk
```

[Back to overview](..) · [FAQ](../faq) · [Privacy](../privacy)

</section>
<section lang="zh-CN" markdown="1">

爱商店支持 **`istore://`** 快捷链接。可在**快捷指令**、Safari 书签，或从**小组件**、**控制中心**、**Spotlight** 与**分享扩展**中用来**切换地区**、**再次切换上次地区**、**打开某个 Tab** 或**直达指南**。

## 链接格式

```
istore://{host}?{参数}
```

Host **不区分大小写**。地区代码使用标准 **Alpha-2** 值（`us`、`cn`、`jp`、`hk`、`tw` 等）。

| 目的 | 链接 |
|------|------|
| 切换到某地区 | `istore://switch?region={代码}` |
| 切换到上次地区 | `istore://switch-last` |
| 打开 商店 / 收藏 / 设置 Tab | `istore://store` · `istore://favorites` · `istore://settings` |
| 打开上架查询 | `istore://availability` |

---

## 切换到某地区

请求切换到指定地区（若已开启，会经过 App 内确认）。

```
istore://switch?region={代码}
```

| 参数 | 必填 | 说明 |
|------|------|------|
| `region` | **是** | 地区代码，如 `us`、`cn`、`jp`、`hk`、`tw` |

**示例**

```
istore://switch?region=us
```

用于：**交互式小组件**、**Spotlight** 结果、**快捷指令 / Siri**。

---

## 切换到上次地区

```
istore://switch-last
```

读取你最近的切换目标并再次切换。驱动**切换上次**控制中心控件（iOS 18+）与对应的快捷指令 / Siri 操作。

---

## Tab 与页面（无 query）

| 链接 | 打开 |
|------|------|
| `istore://store` | 商店 Tab |
| `istore://favorites` | 收藏 Tab |
| `istore://settings` | 设置 Tab |
| `istore://availability` | 设置 → 上架查询（分享扩展也会用到） |
| `istore://switch-history` | 切换历史 |
| `istore://quick-regions` | 常用地区设置 |
| `istore://feature-guide` | 功能引导 |
| `istore://widget-guide` | 小组件指南 |
| `istore://shortcuts-guide` | 快捷指令指南 |
| `istore://usage-guide` | 使用说明 |
| `istore://feedback` | 意见反馈 |
| `istore://in-app-review` | 应用内评分 |

---

## 小组件、控制中心与 Spotlight

点击时自动生成 `istore://` 链接：

| 来源 | 点击目标 | 效果 |
|------|----------|------|
| **常用 / 最近 / 自定义小组件** | 地区磁贴 | `istore://switch?region=…` |
| **切换上次控件**（iOS 18+） | 控件本身 | `istore://switch-last` |
| **Spotlight** | 地区结果 | `istore://switch?region=…` |

从小组件与控制中心进行的交互式切换会打开 App，以完成 App Store 官方跳转。

---

## 分享扩展

把任意 **App Store 链接**分享到爱商店。分享扩展会查询常用地区的上架情况，随后可通过 `istore://availability` 打开 App，让你查看结果并切换。

---

## Siri 与快捷指令

在**快捷指令** App 中添加内置操作，或对 **Siri** 说出指令。标题与短语已本地化为 英文 / 简体中文 / 繁體中文。

| 操作 | 可设置内容 | 效果 |
|------|------------|------|
| 切换地区 | 地区 | 切换到该地区 |
| 切换上次地区 | — | 切换到上次目标 |
| 切换收藏地区 | 某收藏 | 切换到已收藏地区 |
| 打开商店 | — | 打开爱商店 |
| 查询上架 | App 链接或 ID | 查询该 App 的上架地区 |

---

## 链接中的地区代码

快捷链接与小组件生成的 URL 始终使用稳定的**地区代码**（`us`、`cn`、`hk`、`tw` 等），而非本地化显示名称。

**示例**

```
istore://switch?region=jp
istore://switch?region=hk
```

[返回概览](..) · [常见问题](../faq) · [隐私政策](../privacy)

</section>
<section lang="zh-TW" markdown="1">

愛商店支援 **`istore://`** 快捷連結。可在**捷徑**、Safari 書籤，或從**小工具**、**控制中心**、**Spotlight** 與**分享延伸功能**中用來**切換地區**、**再次切換上次地區**、**開啟某個 Tab** 或**直達指南**。

## 連結格式

```
istore://{host}?{參數}
```

Host **不區分大小寫**。地區代碼使用標準 **Alpha-2** 值（`us`、`cn`、`jp`、`hk`、`tw` 等）。

| 目的 | 連結 |
|------|------|
| 切換到某地區 | `istore://switch?region={代碼}` |
| 切換到上次地區 | `istore://switch-last` |
| 開啟 商店 / 收藏 / 設定 Tab | `istore://store` · `istore://favorites` · `istore://settings` |
| 開啟上架查詢 | `istore://availability` |

---

## 切換到某地區

請求切換到指定地區（若已開啟，會經過 App 內確認）。

```
istore://switch?region={代碼}
```

| 參數 | 必填 | 說明 |
|------|------|------|
| `region` | **是** | 地區代碼，如 `us`、`cn`、`jp`、`hk`、`tw` |

**範例**

```
istore://switch?region=us
```

用於：**互動式小工具**、**Spotlight** 結果、**捷徑 / Siri**。

---

## 切換到上次地區

```
istore://switch-last
```

讀取你最近的切換目標並再次切換。驅動**切換上次**控制中心控制項（iOS 18+）與對應的捷徑 / Siri 操作。

---

## Tab 與頁面（無 query）

| 連結 | 開啟 |
|------|------|
| `istore://store` | 商店 Tab |
| `istore://favorites` | 收藏 Tab |
| `istore://settings` | 設定 Tab |
| `istore://availability` | 設定 → 上架查詢（分享延伸功能也會用到） |
| `istore://switch-history` | 切換歷史 |
| `istore://quick-regions` | 常用地區設定 |
| `istore://feature-guide` | 功能引導 |
| `istore://widget-guide` | 小工具指南 |
| `istore://shortcuts-guide` | 捷徑指南 |
| `istore://usage-guide` | 使用說明 |
| `istore://feedback` | 意見回饋 |
| `istore://in-app-review` | 應用內評分 |

---

## 小工具、控制中心與 Spotlight

點擊時自動產生 `istore://` 連結：

| 來源 | 點擊目標 | 效果 |
|------|----------|------|
| **常用 / 最近 / 自訂小工具** | 地區磁貼 | `istore://switch?region=…` |
| **切換上次控制項**（iOS 18+） | 控制項本身 | `istore://switch-last` |
| **Spotlight** | 地區結果 | `istore://switch?region=…` |

從小工具與控制中心進行的互動式切換會開啟 App，以完成 App Store 官方跳轉。

---

## 分享延伸功能

把任意 **App Store 連結**分享到愛商店。分享延伸功能會查詢常用地區的上架情況，隨後可透過 `istore://availability` 開啟 App，讓你查看結果並切換。

---

## Siri 與捷徑

在**捷徑** App 中新增內建操作，或對 **Siri** 說出指令。標題與短語已本地化為 英文 / 简体中文 / 繁體中文。

| 操作 | 可設定內容 | 效果 |
|------|------------|------|
| 切換地區 | 地區 | 切換到該地區 |
| 切換上次地區 | — | 切換到上次目標 |
| 切換收藏地區 | 某收藏 | 切換到已收藏地區 |
| 開啟商店 | — | 開啟愛商店 |
| 查詢上架 | App 連結或 ID | 查詢該 App 的上架地區 |

---

## 連結中的地區代碼

快捷連結與小工具產生的 URL 始終使用穩定的**地區代碼**（`us`、`cn`、`hk`、`tw` 等），而非本地化顯示名稱。

**範例**

```
istore://switch?region=jp
istore://switch?region=hk
```

[返回概覽](..) · [常見問題](../faq) · [隱私政策](../privacy)

</section>
<section lang="ja" markdown="1">

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

</section>
<section lang="ko" markdown="1">

iStore 지원 ** `istore://` ** 단축 링크. **Shortcuts**, Safari bookmarks, 또는 **widgets**, **Control Center**, **Spotlight** 및 **Share Extension** to ** 지역을 전환 **, **re-switch your last area**, ** 탭 열기 **, 또는 **jump to guide**.

## 링크 형식


```
istore://{host}?{params}
```


호스트는 **case-insensitive**입니다. 지역 코드 사용 표준 **Alpha-2** 값 ( `istore://` , `us` , `cn` , `jp` , `hk` , ...).

| What you want | 링크 메뉴 |
|---------------|------|
| Switch to a region | `istore://switch?region={code}`를 호출합니다. |
| Switch to your last region | `istore://switch-last````````` |
| Open the Store / Favorites / Settings tab | `istore://store` · `istore://favorites` · `istore://settings` |
| Open App Availability | `istore://availability```````` |

---

## 지역 전환

지정된 지역에 스위치를 요청합니다 (인앱 확인을 통해 루트).


```
istore://switch?region={code}
```


| Parameter | Required | 이름 * |
|-----------|----------|-------------|
| `region` | **Yes** | 지역 코드, 예를 들어 `us`, `cn`, `jp`, `hk`, `tw` |

**예금 **


```
istore://switch?region=us
```


에 의해 사용하는: **interactive 위젯**, **Spotlight** 결과, **Shortcuts / Siri**.

---

## 당신의 마지막 지역에 스위치


```
istore://switch-last
```


가장 최근의 스위치 대상을 읽고 다시 전환합니다. ** Switch Last** 제어 센터 제어(iOS 18+) 및 일치 단축키 / Siri 동작.

---

## 탭 & 페이지 (질문 없음)

| URL | 열리는 화면 |
|-----|-------|
| `istore://store` | 상점 탭 |
| `istore://favorites` | 즐겨찾기 탭 |
| `istore://settings` | 설정 탭 |
| `istore://availability` | 설정 → App Availability (또한 공유 확장에 의해 사용) |
| `istore://switch-history` | 스위치 History |
| `istore://quick-regions` | 빠른 지역 설정 |
| `istore://feature-guide` | 기능 가이드 |
| `istore://widget-guide` | 위젯 가이드 |
| `istore://shortcuts-guide` | 단축어 가이드 |
| `istore://usage-guide` | 사용 가이드 |
| `istore://feedback` | 피드백 이메일 |
| `istore://in-app-review` | 앱 내 App Store 평가 |

---

## Widgets, 제어 센터 및 스포트라이트

이 생성 `istore://` 링크는 자동으로 입력할 때:

| Source | Tap target | 제품 정보 |
|--------|------------|--------|
| **Quick Regions / Recent / Custom widget** | A region tile | `istore://switch?region=...` |
| **Switch Last control** (iOS 18+) | The control | `istore://switch-last````````` |
| **Spotlight** | A region result | `istore://switch?region=...` |

위젯과 컨트롤 센터의 대화식 전환은 앱을 열고 공식 앱 스토어 리디렉션을 완료합니다.

---

## 공유 확장

** 앱 스토어 링크 ** iStore로 공유하십시오. 대중적인 지역에 걸쳐 공유 확장 체크 가용성, 다음을 통해 앱을 열 수 있습니다 `istore://` 그래서 당신은 결과와 스위치를 검토할 수 있습니다.

---

## Siri 및 단축키

**Shortcuts** 앱 또는 요청 **Siri**에서 내장 작업을 찾습니다. 제목과 문구는 영어로 현지화 / 한국어 / 繁體中文.

| Action | What you can set | 제품 정보 |
|--------|------------------|--------|
| Switch region | Region | 해당 지역으로 전환 |
| Switch last region | — | 당신의 마지막 목표에 전환 |
| Switch favorite region | A favorite | 가장 좋아하는 지역으로 전환 |
| Open store | — | iStore 오픈 |
| Check availability | App link or ID | 앱을 사용할 수 있는 체크 |

---

## 링크에서 지역 코드

딥 링크 및 위젯 생성 된 URL은 항상 안정 ** 등록 코드 ** ( `istore://` , `us` , `cn` , `jp` , ...) - 현지화 된 디스플레이 이름.

**예시**


```
istore://switch?region=jp
istore://switch?region=hk
```


[경찰](..) · [FAQ](../faq) · [Privacy](../privacy)

</section>
<section lang="ru" markdown="1">

iStore поддерживает ярлыки ** `istore://` **. Используйте их в **Shortcuts**, закладках Safari или от **widgets**, **Control Center**, **Spotlight** и **Share Extension** до **switch a region**, **re-switch your last region**, **open a tab**, или **jump to a guide**.

## Формат ссылки


```
istore://{host}?{params}
```


Хозяева нечувствительны к делу. Коды регионов используют стандартные значения **Alpha-2** ( `istore://` , `us` , `cn` , `jp` , `hk` , ...).

| What you want | Ссылка |
|---------------|------|
| Switch to a region | 'istore://switch?region={code} |
| Switch to your last region | "istore://switch-last" |
| Open the Store / Favorites / Settings tab | "istore://store" · "istore://favorites" · "istore://settings" |
| Open App Availability | "история://доступность" |

---

## Переключитесь на регион

Запрашивает переключение на данный регион (направляется через подтверждение в приложении, если включено).


```
istore://switch?region={code}
```


| Parameter | Required | Описание |
|-----------|----------|-------------|
| `region` | **Yes** | Код региона, например "us", "cn", "jp", "hk", "tw" |

**Пример **


```
istore://switch?region=us
```


Используются: **интерактивные виджеты**, **Spotlight** и **Shortcuts/Siri**.

---

## Переключитесь на последний регион


```
istore://switch-last
```


Прочтите свою последнюю цель переключения и переключитесь на нее снова. Управляет **Switch Last** Control Center control (iOS 18+) и соответствующим действием Shortcut/Siri.

---

## Вкладки и страницы (без запроса)

| URL | Открывает |
|-----|-------|
| `istore://store` | Закладка магазина |
| `istore://favorites` | Любимая вкладка |
| `istore://settings` | Настройка вкладки |
| `istore://availability` | Настройки → Доступность приложений (также используется расширением акций) |
| `istore://switch-history` | Переключение истории |
| `istore://quick-regions` | Быстрые настройки регионов |
| `istore://feature-guide` | Обзор функций |
| `istore://widget-guide` | Руководство по виджетам |
| `istore://shortcuts-guide` | Руководство по «Командам» |
| `istore://usage-guide` | Руководство по использованию |
| `istore://feedback` | Письмо с отзывом |
| `istore://in-app-review` | Оценка в App Store из приложения |

---

## Виджеты, Центр управления и Spotlight

Они генерируют ссылки `istore://` автоматически при нажатии:

| Source | Tap target | Эффект |
|--------|------------|--------|
| **Quick Regions / Recent / Custom widget** | A region tile | "istore://switch?region=..." |
| **Switch Last control** (iOS 18+) | The control | "istore://switch-last" |
| **Spotlight** | A region result | "istore://switch?region=..." |

Интерактивное переключение с виджетов и Центра управления открывает приложение для завершения официального перенаправления App Store.

---

## Расширение доли

Поделитесь любой ссылкой ** App Store** в iStore. Share Extension проверяет доступность в популярных регионах, а затем может открыть приложение через `istore://` , чтобы вы могли просмотреть результат и переключиться.

---

## Siri и Shortcuts

Найдите встроенные действия в приложении **Shortcuts** или спросите **Siri**. Названия и фразы локализованы на английском языке / .中. / .中..

| Action | What you can set | Эффект |
|--------|------------------|--------|
| Switch region | Region | Переключается на этот регион |
| Switch last region | — | Переключайтесь на последнюю цель |
| Switch favorite region | A favorite | Переход в любимый регион |
| Open store | — | Открытие iStore |
| Check availability | App link or ID | Проверьте, где приложение доступно |

---

## Коды регионов в ссылках

Глубокие ссылки и URL-адреса, генерируемые виджетами, всегда используют стабильные коды **региона ** ( `istore://` , `us` , `cn` , `jp` , ...) — не локализованные имена дисплеев.

**Примеры**


```
istore://switch?region=jp
istore://switch?region=hk
```


[Назад к обзору] (..) · [FAQ] (../faq) · [Privacy] (../privacy)

</section>
<section lang="th" markdown="1">

ispore รองรับ} `istore://` BAR ลิงก์ลัด ใช้มันใน~~, ที่คั่นหน้าซาฟารี, หรือจาก~ Vidgets~, ~Control Center~, ~ไฟ~, ~และช่องสยาม~ เพื่อทําลายภูมิภาค~

## รูปแบบลิงก์


```
istore://{host}?{params}
```


โฮสต์มันไวต่อความรู้สึก รหัสในภูมิภาคใช้มาตรฐาน # Alfa-2* ค่า ( c0       BAR    /                                     BAR    BAR       BAR            ...

| What you want | เชื่อมโยง |
|---------------|------|
| Switch to a region | พ่อมด? Region = {code}' |
| Switch to your last region | ISTorre Awards Witchal' |
| Open the Store / Favorites / Settings tab | ISTorre Ustore' sustore effectite'Histore settings' |
| Open App Availability | 'ความจุ' |

---

## สลับไปยังขอบเขต

ต้องการเปลี่ยนไปยังพื้นที่ที่กําหนด (ส่งผ่านการยืนยันการเปิดใช้ หากเปิดใช้งาน)


```
istore://switch?region={code}
```


| Parameter | Required | คําอธิบาย |
|-----------|----------|-------------|
| `region` | **Yes** | รหัสเขต, e.g. 'us', 'cn', ojp', ohk', othw' |

~Example~


```
istore://switch?region=us
```


ถูกใช้โดย: ~วิดเจ็ตที่ตอบสนอง~ ~ผลการปล่อยไฟ~ และ~/เซอร์อิ~

---

## สลับไปยังพื้นที่ล่าสุดของคุณ


```
istore://switch-last
```


อ่านจุดเปลี่ยนล่าสุดของคุณ และเปลี่ยนไปอีกครั้ง พลังอํานาจของ "Switch  Last control" (ไอโอเอส 18+) และ ปุ่มพิมพ์ลัดที่เข้าคู่กัน / เซอรี แอ็คชั่น

---

## แท็บและหน้า (ไม่ต้องถาม)

| URL | เปิด |
|-----|-------|
| `istore://store` | เก็บแท็บ |
| `istore://favorites` | แท็บโปรด |
| `istore://settings` | แท็บการตั้งค่า |
| `istore://availability` | ตั้งค่าต่าง ๆ app AppAvilable (ยังถูกใช้โดยส่วนขยายใช้งานร่วมกัน) |
| `istore://switch-history` | เปลี่ยนประวัติการใช้ |
| `istore://quick-regions` | ตั้งค่าขอบเขตที่รวดเร็ว |
| `istore://feature-guide` | คู่มือฟีเจอร์ |
| `istore://widget-guide` | คู่มือวิดเจ็ต |
| `istore://shortcuts-guide` | คู่มือทางลัด |
| `istore://usage-guide` | คู่มือการใช้งาน |
| `istore://feedback` | อีเมลข้อเสนอแนะ |
| `istore://in-app-review` | ให้คะแนน App Store ในแอป |

---

## วิดเจ็ต, ศูนย์ควบคุม & จุดแสง

สิ่งเหล่านี้สร้าง `istore://` ลิงก์อัตโนมัติเมื่อคุณเคาะ:

| Source | Tap target | ลูกเล่น |
|--------|------------|--------|
| **Quick Regions / Recent / Custom widget** | A region tile | พ่อมด? |
| **Switch Last control** (iOS 18+) | The control | ISTorre Awards Witchal' |
| **Spotlight** | A region result | พ่อมด? |

การสลับการทํางานจากคอนโทรลและศูนย์ควบคุม เปิดโปรแกรมเพื่อทําเส้นทางไปยัง App อย่างเป็นทางการเสร็จสมบูรณ์

---

## ส่วนขยายการใช้ร่วมกัน

แบ่งส่วนเชื่อมโยงของ APP ให้อยู่ใน iStore Check ส่วนขยายการแบ่งปันสามารถผ่านภูมิภาคที่นิยม จากนั้นสามารถเปิดโปรแกรมผ่าน  c0     r. เพื่อคุณสามารถทบทวนผลลัพธ์และสลับได้

---

## ปุ่มพิมพ์ลัดแบบ Siri

ค้นหาการกระทําที่สร้างขึ้นในโปรแกรมนี้ หัว เรื่อง และ วลี ต่าง ๆ ถูก นํา มา ใช้ ใน ภาษา อังกฤษ / 简体中文 / 繁體中文.

| Action | What you can set | ลูกเล่น |
|--------|------------------|--------|
| Switch region | Region | สลับไปยังพื้นที่ดังกล่าว |
| Switch last region | — | สลับไปยังเป้าหมายสุดท้าย |
| Switch favorite region | A favorite | สลับไปยังพื้นที่ที่ต้องการ |
| Open store | — | เปิดระบบ iStore |
| Check availability | App link or ID | ตรวจสอบว่าโปรแกรมมีตําแหน่งใด |

---

## รหัสเขตอยู่ในลิงก์

ลิงก์ลึกและที่อยู่ URL ที่สร้างจากวิดเจ็ต จะใช้รหัสที่เสถียรเสมอ ** ( `istore://` BAR   BAR `us` BAR    BAR   BAR    BAR    BAR    BAR    BAR         BAR    BAR                  BAR      BAR     BAR    BAR      BAR      BAR

**ตัวอย่าง**


```
istore://switch?region=jp
istore://switch?region=hk
```


[Tack to Broups](. ) สืบค้นเมื่อ 22 พฤษภาคม พ.ศ.

</section>
<section lang="de" markdown="1">

iStore unterstützt ** `istore://` ** Shortcut Links. Verwenden Sie sie in **Shortcuts **, Safari-Lesezeichen oder von **Widgets **, **Control Center **, **Spotlight ** und der **Share Extension **, um ** eine Region zu wechseln **, ** Ihre letzte Region zu wechseln **, ** einen Tab zu öffnen ** oder ** zu einem Guide zu springen **.

## Linkformat


```
istore://{host}?{params}
```


Hosts sind **case-insensitive **. Regionscodes verwenden Standardwerte **Alpha-2** ( `istore://` , `us` , `cn` , `jp` , `hk` , ...).

| What you want | Link |
|---------------|------|
| Switch to a region | „istore://switch?region={code} |
| Switch to your last region | „istore://switch-last |
| Open the Store / Favorites / Settings tab | `istore://store` · `istore://favorites` · `istore://settings` |
| Open App Availability | „istore://availability |

---

## Wechsel zu einer Region

Fordert einen Wechsel in die angegebene Region an (durch die In-App-Bestätigung geleitet, falls aktiviert).


```
istore://switch?region={code}
```


| Parameter | Required | Beschreibung |
|-----------|----------|-------------|
| `region` | **Yes** | Regionscode, z.B. `us`, `cn`, `jp`, `hk`, `tw` |

**Beispiel**


```
istore://switch?region=us
```


Verwendet von: **interaktive Widgets**, **Spotlight** Ergebnisse und **Shortcuts / Siri**.

---

## Wechseln Sie zu Ihrer letzten Region


```
istore://switch-last
```


Lies dein letztes Switch-Ziel und wechsele erneut zu ihm. Betreibt die **Switch Last** Control Center-Steuerung (iOS 18+) und die passende Shortcut / Siri-Aktion.

---

## Tabs & Seiten (keine Abfrage)

| URL | Öffnet |
|-----|-------|
| `istore://store` | Speichertipp |
| `istore://favorites` | Favoriten-Tab |
| `istore://settings` | Tab Einstellungen |
| `istore://availability` | Einstellungen → App-Verfügbarkeit (auch von der Share Extension verwendet) |
| `istore://switch-history` | Switch History |
| `istore://quick-regions` | Quick Regions Einstellungen |
| `istore://feature-guide` | Funktionsübersicht |
| `istore://widget-guide` | Widget-Anleitung |
| `istore://shortcuts-guide` | Kurzbefehle-Anleitung |
| `istore://usage-guide` | Nutzungsanleitung |
| `istore://feedback` | Feedback-E-Mail |
| `istore://in-app-review` | App-Store-Bewertung in der App |

---

## Widgets, Kontrollzentrum & Spotlight

Diese erzeugen automatisch `istore://` -Links, wenn Sie tippen:

| Source | Tap target | Wirkung |
|--------|------------|--------|
| **Quick Regions / Recent / Custom widget** | A region tile | „istore://switch?region=... |
| **Switch Last control** (iOS 18+) | The control | „istore://switch-last |
| **Spotlight** | A region result | „istore://switch?region=... |

Interaktiver Wechsel von Widgets und Control Center öffnet die App, um die offizielle Umleitung des App Store abzuschließen.

---

## Aktienverlängerung

Teilen Sie einen beliebigen **App Store Link** in iStore. Die Share Extension prüft die Verfügbarkeit in beliebten Regionen und kann dann die App über `istore://` öffnen, damit Sie das Ergebnis überprüfen und wechseln können.

---

## Siri & Shortcuts

Finden Sie integrierte Aktionen in der **Shortcuts** App oder fragen Sie **Siri**. Titel und Phrasen sind auf Englisch lokalisiert / 简体中� / 繁體中�.

| Action | What you can set | Wirkung |
|--------|------------------|--------|
| Switch region | Region | Wechsel in diese Region |
| Switch last region | — | Wechsel zu Ihrem letzten Ziel |
| Switch favorite region | A favorite | Wechsel zu einer bevorzugten Region |
| Open store | — | Öffnet iStore |
| Check availability | App link or ID | Prüft, wo die App verfügbar ist |

---

## Regionscodes in Links

Deep Links und widgetgenerierte URLs verwenden immer stabile **Regionalcodes** ( `istore://` , `us` , `cn` , `jp` , ...) — keine lokalisierten Anzeigenamen.

**Beispiele**


```
istore://switch?region=jp
istore://switch?region=hk
```


[Zurück zur Übersicht](..) · [FAQ](../faq) · [Privacy](../privacy]

</section>
<section lang="fr" markdown="1">

iStore supporte les liens de raccourci ** `istore://` **. Utilisez-les dans **Shortcuts**, signets Safari, ou à partir de **widgets**, **Control Center**, **Spotlight** et l'extension **Share** vers **switch une région**, **switchez votre dernière région**, **ouvrez un onglet** ou **jump vers un guide**.

## Format de lien


```
istore://{host}?{params}
```


Les hôtes sont **insensibles aux cas**. Les codes régionaux utilisent la norme **Valeurs alpha-2** ( `istore://` , `us` , `cn` , `jp` , `hk` , ...).

| What you want | Lien |
|---------------|------|
| Switch to a region | `istore://switch?region={code}` |
| Switch to your last region | `istore://switch-last' |
| Open the Store / Favorites / Settings tab | "IStore://store" · "IStore://favorites" · "IStore://settings" |
| Open App Availability | 'estore://disponibilité' |

---

## Passer à une région

Demande un changement vers la région donnée (racheminée par la confirmation de l'application, si activé).


```
istore://switch?region={code}
```


| Parameter | Required | Désignation des marchandises |
|-----------|----------|-------------|
| `region` | **Yes** | Code régional, par exemple `us`, `cn`, `jp`, `hk`, `tw` |

**Exemple**


```
istore://switch?region=us
```


Utilisé par : ** widgets interactifs**, **Spotlight** et **Shortcuts / Siri**.

---

## Passez à votre dernière région


```
istore://switch-last
```


Lis ta cible de commutation la plus récente et change à nouveau. Fonctionne sur la commande **Switch Last** Control Center (iOS 18+) et l'action Shortcut / Siri correspondante.

---

## Tabs & pages (aucune requête)

| URL | Ouvre |
|-----|-------|
| `istore://store` | Onglet Enregistrer |
| `istore://favorites` | Onglet Favoris |
| `istore://settings` | Onglet Paramètres |
| `istore://availability` | Paramètres → Disponibilité de l'application (également utilisée par l'extension de partage) |
| `istore://switch-history` | Historique du commutateur |
| `istore://quick-regions` | Paramètres des régions rapides |
| `istore://feature-guide` | Guide des fonctionnalités |
| `istore://widget-guide` | Guide des widgets |
| `istore://shortcuts-guide` | Guide Raccourcis |
| `istore://usage-guide` | Guide d'utilisation |
| `istore://feedback` | E-mail de commentaires |
| `istore://in-app-review` | Note App Store in-app |

---

## Widgets, Control Center & Spotlight

Ces liens génèrent automatiquement `istore://` lorsque vous appuyez sur :

| Source | Tap target | Effet |
|--------|------------|--------|
| **Quick Regions / Recent / Custom widget** | A region tile | `estore://switch?region=...` |
| **Switch Last control** (iOS 18+) | The control | `istore://switch-last' |
| **Spotlight** | A region result | `estore://switch?region=...` |

La commutation interactive depuis les widgets et Control Center ouvre l'application pour compléter la redirection officielle de l'App Store.

---

## Extension du partage

Partager un lien **App Store** dans iStore. L'extension de partage vérifie la disponibilité dans les régions populaires, puis peut ouvrir l'application via `istore://` afin que vous puissiez examiner le résultat et changer.

---

## Siri & raccourcis

Trouvez des actions intégrées dans l'application **Shortcuts** ou demandez **Siri**. Les titres et les phrases sont localisés en anglais / 简体中文 / 简ш中文.

| Action | What you can set | Effet |
|--------|------------------|--------|
| Switch region | Region | Passons à cette région |
| Switch last region | — | Commutation vers votre dernière cible |
| Switch favorite region | A favorite | Passage à une région préférée |
| Open store | — | Ouvre iStore |
| Check availability | App link or ID | Vérifier où l'application est disponible |

---

## Codes régionaux en liens

Les liens profonds et les URL générées par widget utilisent toujours des codes stables **region** ( `istore://` , `us` , `cn` , `jp` , ...) — les noms d'affichage non localisés.

**Exemples**


```
istore://switch?region=jp
istore://switch?region=hk
```


[Retour à l'aperçu](..) · [FAQ](../faq) · [Confidentialité](../privacité)

</section>
<section lang="tr" markdown="1">

i store, ** `istore://` ** kısayollarını destekliyor. Onları **Shortcuts**, Safari kitap işaretlerini veya **widgets**, **Control Center**, **Spotlight** ve **Share Extension a region**, **re-switch your last region**, **

## Bağlantı biçimi


```
istore://{host}?{params}
```


Hosts **case-in sensitive**. Bölge kodları standart **Alpha-2** değerleri ( `istore://` , `us` , `cn` , `jp` , `hk` | What you want | Link Link Link Link |
|---------------|------|
| Switch to a region | "Etmen: http://switch?region={code} |
| Switch to your last region | "istore httpswitch-last" |
| Open the Store / Favorites / Settings tab | "istore httpstore" · "istore https://favorites' · "istore https" |
| Open App Availability | "istore httpavailability" |

---

## Bir bölgeye geçiş

Verilen bölgeye bir geçiş talep eder (eğer etkinleştirirse)


```
istore://switch?region={code}
```


| Parameter | Required | Açıklama |
|-----------|----------|-------------|
| `region` | **Yes** | Bölge kodu, e.g. "us', "cn", "jp', "hk", "tw" |

**Example**


```
istore://switch?region=us
```


Tarafından kullanılır: **interaktif widgets**, **Spotlight** sonuçları ve **Shortcuts / Siri**.

---

## Son bölgenize geçiş


```
istore://switch-last
```


En son geçiş hedefinizi ve anahtarlarınızı tekrar okuyun. Güçler ** Son** Kontrol Merkezi kontrolü (iOS 18+) ve eşleşen Kısa kesim / Siri eylemi.

---

## Tabs & sayfalar (no query)

| URL | Açar |
|-----|-------|
| `istore://store` | Mağaza sekmesi |
| `istore://favorites` | Favoriler sekmesi |
| `istore://settings` | Ayarlar sekmesi |
| `istore://availability` | Ayarlar → App Availability (ayrıca Share Extension tarafından da kullanılır) |
| `istore://switch-history` | Tarih |
| `istore://quick-regions` | Hızlı Bölgeler |
| `istore://feature-guide` | Özellik kılavuzu |
| `istore://widget-guide` | Widget kılavuzu |
| `istore://shortcuts-guide` | Kısayol kılavuzu |
| `istore://usage-guide` | Kullanım kılavuzu |
| `istore://feedback` | Geri bildirim e-postası |
| `istore://in-app-review` | Uygulama içi App Store puanı |

---

## Widgets, Control Center & Spotlight

Bunlar, dokunduğunuzda `istore://` bağlantıları otomatik olarak üretir:

| Source | Tap target | Etkisi Etkisi Etkisi |
|--------|------------|--------|
| **Quick Regions / Recent / Custom widget** | A region tile | "Oturan: " |
| **Switch Last control** (iOS 18+) | The control | "istore httpswitch-last" |
| **Spotlight** | A region result | "Oturan: " |

Widgets ve Control Center'dan interaktif geçiş, resmi App Store yönlendirmesini tamamlamak için uygulamayı açar.

---

## Paylaş

Herhangi bir **App Store linkini paylaşın - i Shop. Share Extension, popüler bölgelerde kullanılabilirliği kontrol eder, sonra uygulama `istore://` aracılığıyla açabilirsiniz, böylece sonucu gözden geçirebilirsiniz ve değiştirebilirsiniz.

---

## Siri & Shortcuts

**Shortcuts ** uygulamasında yerleşik eylemleri bulun veya **Siri**’ye sorun. Başlıklar ve kelimeler İngilizce / . / .'de lokalize edilir.

| Action | What you can set | Etkisi Etkisi Etkisi |
|--------|------------------|--------|
| Switch region | Region | Bu bölgeye Anahtarlar |
| Switch last region | — | Son hedefinize Anahtarlar |
| Switch favorite region | A favorite | Favori bir bölgeye Anahtarlar |
| Open store | — | Opens i store |
| Check availability | App link or ID | Uygulamanın mevcut olduğu kontroller |

---

## Bölge kodları bağlantıları

Derin bağlantılar ve widget tarafından üretilen URL'ler her zaman istikrarlı kullanır **region kodları** ( `istore://` , `us` , `cn` , `jp` , ...) - yerelleştirilmiş ekran isimleri değil.

**Örnekler**


```
istore://switch?region=jp
istore://switch?region=hk
```


[Genellikle] (.) · [FAQ](./faq) · [Privacy] (./privacy)

</section>
