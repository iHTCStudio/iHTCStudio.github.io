---
layout: doc
title: iAppManager — Shortcut Links
app_id: iAppManager
doc_title_en: Shortcut Links
doc_title_zh_cn: 快捷链接说明
doc_title_zh_tw: 快捷連結說明
description: iappmanager:// shortcut links for iAppManager — apps, modules, guides, certificates, reports, settings.
---

<section lang="en" markdown="1">

iAppManager supports **`iappmanager://`** links for Shortcuts, widgets, App Intents, and Home Screen actions.

## Link format

```
iappmanager://{host}[/…]
```

## Apps & modules

| URL | Opens |
|-----|-------|
| `iappmanager://apps` | My Apps |
| `iappmanager://apps/{appleId}` | Specific app (Overview) |
| `iappmanager://apps/{appleId}/{tab}` | App detail module |

`{appleId}` is the numeric App Store Connect / App Store app id. `{tab}` examples:

| Tab | Module |
|-----|--------|
| `overview` | Overview |
| `versions` | Versions |
| `builds` | Builds |
| `backgroundAssets` | Background Assets |
| `encryption` | Encryption |
| `submissions` | Review Submissions |
| `reviewDetail` | Review Detail |
| `metadata` | Metadata |
| `media` | Screenshots & Previews |
| `productPages` | Custom Product Pages |
| `appEvents` | In-App Events |
| `appClips` | App Clips |
| `experiments` | Store Experiments |
| `nominations` | Featuring Nominations |
| `availability` | Availability |
| `pricing` | Pricing |
| `ageRating` | Age Rating |
| `accessibility` | Accessibility |
| `appTags` | App Tags |
| `iap` | In-App Purchases |
| `gameCenter` | Game Center |
| `testflight` | TestFlight |
| `reviews` | Customer Reviews |
| `privacy` | Privacy (nutrition note) |
| `promoCodes` | Promo Codes |
| `webhooks` | Webhooks |

Example: `iappmanager://apps/1234567890/versions`

## Sidebar & tools

| URL | Opens |
|-----|-------|
| `iappmanager://certificates` | Certificates & Identifiers |
| `iappmanager://users` | Users & Access |
| `iappmanager://reports` | Reports |
| `iappmanager://settings` | Settings |
| `iappmanager://add-account` | Add API Key account |
| `iappmanager://about` | About |
| `iappmanager://feedback` | Feedback email |
| `iappmanager://in-app-review` | Rate prompt |

## In-app guides

| URL | Guide |
|-----|-------|
| `iappmanager://feature-guide` | Feature tour |
| `iappmanager://usage-guide` | Usage guide |
| `iappmanager://widget-guide` | Widget guide |
| `iappmanager://shortcuts-guide` | Shortcuts guide |
| `iappmanager://release-guide` | Release readiness |
| `iappmanager://iap-guide` | IAP & subscriptions |
| `iappmanager://testflight-guide` | TestFlight |
| `iappmanager://reports-guide` | Reports |

Cold and warm launches buffer deep links briefly so onboarding can finish first. App Intents can also open a managed app with an optional module.

</section>
<section lang="zh-CN" markdown="1">

爱应用者支持 **`iappmanager://`** 链接，可用于快捷指令、小组件、App Intents 与主屏操作。

## 链接格式

```
iappmanager://{host}[/…]
```

## App 与模块

| 链接 | 打开 |
|------|------|
| `iappmanager://apps` | 我的 App |
| `iappmanager://apps/{appleId}` | 指定 App（Overview） |
| `iappmanager://apps/{appleId}/{tab}` | App 详情模块 |

`{appleId}` 为数字 App ID。`{tab}` 示例：

| Tab | 模块 |
|-----|------|
| `overview` | Overview |
| `versions` | 版本 |
| `builds` | 构建 |
| `backgroundAssets` | 后台资源 |
| `encryption` | 加密声明 |
| `submissions` | 审核提交 |
| `reviewDetail` | 审核备注 |
| `metadata` | 元数据 |
| `media` | 截图与预览 |
| `productPages` | 自定义产品页 |
| `appEvents` | App 内活动 |
| `appClips` | App Clips |
| `experiments` | 商店实验 |
| `nominations` | 推荐提名 |
| `availability` | 上架地区 |
| `pricing` | 定价 |
| `ageRating` | 年龄分级 |
| `accessibility` | 辅助功能 |
| `appTags` | App Tags |
| `iap` | 内购 / 订阅 |
| `gameCenter` | Game Center |
| `testflight` | TestFlight |
| `reviews` | 顾客评价 |
| `privacy` | 隐私说明 |
| `promoCodes` | 推广码 |
| `webhooks` | Webhooks |

示例：`iappmanager://apps/1234567890/versions`

## 侧边栏与工具

| 链接 | 打开 |
|------|------|
| `iappmanager://certificates` | 证书与 Identifiers |
| `iappmanager://users` | 用户与访问 |
| `iappmanager://reports` | 报表 |
| `iappmanager://settings` | 设置 |
| `iappmanager://add-account` | 添加 API Key 账号 |
| `iappmanager://about` | 关于 |
| `iappmanager://feedback` | 反馈邮件 |
| `iappmanager://in-app-review` | 评分引导 |

## 应用内指南

| 链接 | 指南 |
|------|------|
| `iappmanager://feature-guide` | 功能导览 |
| `iappmanager://usage-guide` | 使用指南 |
| `iappmanager://widget-guide` | 小组件指南 |
| `iappmanager://shortcuts-guide` | 快捷指南 |
| `iappmanager://release-guide` | 提审就绪 |
| `iappmanager://iap-guide` | 内购与订阅 |
| `iappmanager://testflight-guide` | TestFlight |
| `iappmanager://reports-guide` | 报表 |

冷热启动会短暂缓冲深链，以便首启引导先完成。App Intents 也可打开指定 App 与可选模块。

</section>
<section lang="zh-TW" markdown="1">

愛應用者支援 **`iappmanager://`** 連結，可用於捷徑、小工具、App Intents 與主畫面操作。

## 連結格式

```
iappmanager://{host}[/…]
```

## App 與模組

| 連結 | 打開 |
|------|------|
| `iappmanager://apps` | 我的 App |
| `iappmanager://apps/{appleId}` | 指定 App（Overview） |
| `iappmanager://apps/{appleId}/{tab}` | App 詳情模組 |

`{appleId}` 為數字 App ID。`{tab}` 範例：

| Tab | 模組 |
|-----|------|
| `overview` | Overview |
| `versions` | 版本 |
| `builds` | 建置 |
| `backgroundAssets` | 背景資源 |
| `encryption` | 加密聲明 |
| `submissions` | 審核提交 |
| `reviewDetail` | 審核備註 |
| `metadata` | 中繼資料 |
| `media` | 截圖與預覽 |
| `productPages` | 自訂產品頁 |
| `appEvents` | App 內活動 |
| `appClips` | App Clips |
| `experiments` | 商店實驗 |
| `nominations` | 推薦提名 |
| `availability` | 上架地區 |
| `pricing` | 定價 |
| `ageRating` | 年齡分級 |
| `accessibility` | 輔助功能 |
| `appTags` | App Tags |
| `iap` | 內購 / 訂閱 |
| `gameCenter` | Game Center |
| `testflight` | TestFlight |
| `reviews` | 顧客評價 |
| `privacy` | 隱私說明 |
| `promoCodes` | 推廣碼 |
| `webhooks` | Webhooks |

範例：`iappmanager://apps/1234567890/versions`

## 側邊欄與工具

| 連結 | 打開 |
|------|------|
| `iappmanager://certificates` | 憑證與 Identifiers |
| `iappmanager://users` | 使用者與存取 |
| `iappmanager://reports` | 報表 |
| `iappmanager://settings` | 設定 |
| `iappmanager://add-account` | 新增 API Key 帳號 |
| `iappmanager://about` | 關於 |
| `iappmanager://feedback` | 回饋郵件 |
| `iappmanager://in-app-review` | 評分引導 |

## 應用內指南

| 連結 | 指南 |
|------|------|
| `iappmanager://feature-guide` | 功能導覽 |
| `iappmanager://usage-guide` | 使用指南 |
| `iappmanager://widget-guide` | 小工具指南 |
| `iappmanager://shortcuts-guide` | 快捷指南 |
| `iappmanager://release-guide` | 送審就緒 |
| `iappmanager://iap-guide` | 內購與訂閱 |
| `iappmanager://testflight-guide` | TestFlight |
| `iappmanager://reports-guide` | 報表 |

冷熱啟動會短暫緩衝深鏈，以便首啟引導先完成。App Intents 也可打開指定 App 與可選模組。

</section>
<section lang="ja" markdown="1">

iAppManager は、ショートカット、ウィジェット、アプリのインテント、ホーム画面のアクションのリンクとして、**         ** をサポートしています。

## リンク形式


```
iappmanager://{host}[/…]
```


## アプリとモジュール

| URL | 開く画面 |
|-----|-------|
| `iappmanager://apps` | 私のアプリ |
| `iappmanager://apps/{appleId}` | 特定のアプリ(概要) |
| `iappmanager://apps/{appleId}/{tab}` | アプリ詳細モジュール | `iappmanager://` は数値アプリストアコネクト/App StoreアプリIDです。 `iappmanager://apps` | Tab | モジュール |
|-----|--------|
| `overview` | プロフィール |
| `versions` | バージョン |
| `builds` | ビルド |
| `backgroundAssets` | 背景資産 |
| `encryption` | 暗号化 |
| `submissions` | レビュー投稿者 |
| `reviewDetail` | レビュー詳細 |
| `metadata` | メタデータ |
| `media` | スクリーンショットとプレビュー |
| `productPages` | カスタム製品ページ |
| `appEvents` | アプリ内イベント |
| `appClips` | アプリクリップ |
| `experiments` | ストア実験 |
| `nominations` | ノミネーションを特徴とする |
| `availability` | 交通アクセス |
| `pricing` | 料金について |
| `ageRating` | 年齢評価 |
| `accessibility` | アクセス |
| `appTags` | アプリタグ |
| `iap` | アプリ内購入 |
| `gameCenter` | ゲームセンター |
| `testflight` | テストフライト |
| `reviews` | 顧客レビュー |
| `privacy` | プライバシー(栄養メモ) |
| `promoCodes` | プロモーションコード |
| `webhooks` | ウェブホック |

例: `iappmanager://` ## サイドバー&ツール

| URL | 開く画面 |
|-----|-------|
| `iappmanager://certificates` | 証明書と識別子 |
| `iappmanager://users` | ユーザーとアクセス |
| `iappmanager://reports` | レポート |
| `iappmanager://settings` | 設定 |
| `iappmanager://add-account` | APIキーアカウントの追加 |
| `iappmanager://about` | お問い合わせ |
| `iappmanager://feedback` | フィードバックメール |
| `iappmanager://in-app-review` | 率のプロンプト |

## アプリ内ガイド

| URL | Guide |
|-----|-------|
| `iappmanager://feature-guide` | 特徴ツアー |
| `iappmanager://usage-guide` | 使い方ガイド |
| `iappmanager://widget-guide` | ウィジェットガイド |
| `iappmanager://shortcuts-guide` | ショートカットガイド |
| `iappmanager://release-guide` | リリース準備 |
| `iappmanager://iap-guide` | IAPとサブスクリプション |
| `iappmanager://testflight-guide` | テストフライト |
| `iappmanager://reports-guide` | レポート |

風邪および暖かい進水は緩衝深いリンクを容易に従ってオンボーディング最初に終えることができます開けます。 App Intentsは、管理されたアプリをオプションのモジュールで開くこともできます。

</section>
<section lang="ko" markdown="1">

iAppManager 지원 ** `iappmanager://` ** 단축키에 대한 링크, 위젯, 앱 Intents 및 홈 화면 작업.

## 링크 형식


```
iappmanager://{host}[/…]
```


## 앱 및 모듈

| URL | 열리는 화면 |
|-----|-------|
| `iappmanager://apps` | 내 앱 |
| `iappmanager://apps/{appleId}` | 특정 앱 (Overview) |
| `iappmanager://apps/{appleId}/{tab}` | App 세부사항 단위 | `iappmanager://` 는 숫자 App Store Connect / App Store 앱 ID입니다. `iappmanager://apps` 예제:

| Tab | 모듈 |
|-----|--------|
| `overview` | 제품정보 |
| `versions` | 이름 * |
| `builds` | 회사연혁 |
| `backgroundAssets` | 배경 자산 |
| `encryption` | 암호화 |
| `submissions` | 제출 제출 |
| `reviewDetail` | 회사연혁 |
| `metadata` | 메타데이터 |
| `media` | 스크린 샷 & 미리보기 |
| `productPages` | 주문 제품 페이지 |
| `appEvents` | In-App 이벤트 |
| `appClips` | 앱 클립 |
| `experiments` | 매장 Experiments |
| `nominations` | Nomination의 특징 |
| `availability` | 적용분야 |
| `pricing` | 가격 책정 |
| `ageRating` | 나이 등급 |
| `accessibility` | 오시는 길 |
| `appTags` | 앱 태그 |
| `iap` | In-App 구매 |
| `gameCenter` | 게임센터 |
| `testflight` | 시험Flight |
| `reviews` | 고객 리뷰 |
| `privacy` | 개인정보처리방침 |
| `promoCodes` | 프로모션 코드 |
| `webhooks` | 웹훅 |

예제: `iappmanager://` ## Sidebar 및 도구

| URL | 열리는 화면 |
|-----|-------|
| `iappmanager://certificates` | 인증 및 인증 |
| `iappmanager://users` | 사용자 및 액세스 |
| `iappmanager://reports` | 제품정보 |
| `iappmanager://settings` | 설정 |
| `iappmanager://add-account` | API 키 계정 추가 |
| `iappmanager://about` | 제품정보 |
| `iappmanager://feedback` | 피드백 이메일 |
| `iappmanager://in-app-review` | 빠른 속도 |

## 앱 가이드

| URL | Guide |
|-----|-------|
| `iappmanager://feature-guide` | 관광 명소 |
| `iappmanager://usage-guide` | 사용 가이드 |
| `iappmanager://widget-guide` | 위젯 가이드 |
| `iappmanager://shortcuts-guide` | 단축어 가이드 |
| `iappmanager://release-guide` | 공지사항 |
| `iappmanager://iap-guide` | IAP 및 구독 |
| `iappmanager://testflight-guide` | 시험Flight |
| `iappmanager://reports-guide` | 제품정보 |

감기와 온난한 발사 완충기 깊은 연결은 간략하게 이렇게 onboarding 첫번째를 완료할 수 있습니다. App Intents는 또한 선택적인 단위로 관리한 앱을 열 수 있습니다.

</section>
<section lang="ru" markdown="1">

iAppManager поддерживает ссылки ** `iappmanager://` ** для ярлыков, виджетов, намерений приложений и действий на домашнем экране.

## Формат ссылки


```
iappmanager://{host}[/…]
```


## Приложения и модули

| URL | Открывает |
|-----|-------|
| `iappmanager://apps` | Мои приложения |
| `iappmanager://apps/{appleId}` | Специальное приложение (Overview) |
| `iappmanager://apps/{appleId}/{tab}` | Модуль детализации | `iappmanager://` - это идентификатор приложения App Store Connect / App Store. `iappmanager://apps` Примеры:

| Tab | модуль |
|-----|--------|
| `overview` | Обзор |
| `versions` | Версии |
| `builds` | строить |
| `backgroundAssets` | Справочная информация об активах |
| `encryption` | шифрование |
| `submissions` | Обзор представлений |
| `reviewDetail` | Подробная информация |
| `metadata` | Метаданные |
| `media` | Скриншоты и предварительные просмотры |
| `productPages` | Пользовательские страницы продукта |
| `appEvents` | События In-App |
| `appClips` | App Clips |
| `experiments` | Хранить эксперименты |
| `nominations` | Показаны номинанты |
| `availability` | наличие |
| `pricing` | цены |
| `ageRating` | Возрастной рейтинг |
| `accessibility` | Доступность |
| `appTags` | App Tags |
| `iap` | Покупки в приложении |
| `gameCenter` | Игровой центр |
| `testflight` | испытательный полет |
| `reviews` | Отзывы клиентов |
| `privacy` | Конфиденциальность (пищевая записка) |
| `promoCodes` | Промо-коды |
| `webhooks` | Вебхуки |

Пример: `iappmanager://` ## Sidebar и инструменты

| URL | Открывает |
|-----|-------|
| `iappmanager://certificates` | Сертификаты и идентификаторы |
| `iappmanager://users` | Пользователи и доступ |
| `iappmanager://reports` | Доклады |
| `iappmanager://settings` | Настройки |
| `iappmanager://add-account` | Добавить API Key Account |
| `iappmanager://about` | О нас |
| `iappmanager://feedback` | Письмо с отзывом |
| `iappmanager://in-app-review` | Быстрая ставка |

## Руководство для приложений

| URL | Guide |
|-----|-------|
| `iappmanager://feature-guide` | Особенности тура |
| `iappmanager://usage-guide` | Руководство по использованию |
| `iappmanager://widget-guide` | Руководство по виджетам |
| `iappmanager://shortcuts-guide` | Руководство по «Командам» |
| `iappmanager://release-guide` | Готовность к освобождению |
| `iappmanager://iap-guide` | IAP и подписки |
| `iappmanager://testflight-guide` | испытательный полет |
| `iappmanager://reports-guide` | Доклады |

Холодные и теплые запуски ненадолго буферизируют глубокие связи, поэтому посадка на борт может закончиться первой. App Intents также может открыть управляемое приложение с дополнительным модулем.

</section>
<section lang="th" markdown="1">

IAppmanger รองรับ~ `iappmanager://` BAR * ลิงก์สําหรับปุ่มพิมพ์ลัด, วิดเจ็ต, App Infints และการกระทําหน้าจอบ้าน

## รูปแบบลิงก์


```
iappmanager://{host}[/…]
```


## & มอดูลต่าง ๆ

| URL | เปิด |
|-----|-------|
| `iappmanager://apps` | แอปของฉัน |
| `iappmanager://apps/{appleId}` | แอพพลิเคชันที่ระบุ (Overview) |
| `iappmanager://apps/{appleId}/{tab}` | มอดูลรายละเอียดของโปรแกรม | `iappmanager://` BAR  คือ ID ของร้านซีดีแอป `iappmanager://apps` ตัวอย่าง:

| Tab | มอดูล |
|-----|--------|
| `overview` | ภาพรวม |
| `versions` | รุ่น |
| `builds` | สร้าง |
| `backgroundAssets` | ชุดสําเร็จ: |
| `encryption` | การเข้ารหัส |
| `submissions` | การ ทบทวน |
| `reviewDetail` | รายละเอียดการทบทวน |
| `metadata` | ข้อมูลกํากับภาพ |
| `media` | จับภาพหน้าจอและแสดงตัวอย่าง |
| `productPages` | แบบอักษรกําหนดเอง |
| `appEvents` | เหตุการณ์ใน App |
| `appClips` | แถบชุดลวดลายStencils |
| `experiments` | จัดเก็บตัวประมวลผล |
| `nominations` | การ หา กิน |
| `availability` | ความสามารถ |
| `pricing` | ความละเอียด |
| `ageRating` | ระดับความชื่นชอบในวัย |
| `accessibility` | การช่วยใช้งาน |
| `appTags` | ป้ายกํากับ App |
| `iap` | เว็บของ App |
| `gameCenter` | ศูนย์ควบคุมเกม |
| `testflight` | & ขาว |
| `reviews` | การทบทวนของลูกค้า |
| `privacy` | เบ็ดเตล็ด (บันทึกการใช้แท่ง) |
| `promoCodes` | รหัสโปรโม |
| `webhooks` | เว็บฮุก |

ตัวอย่าง: `iappmanager://` BAR

## เครื่องมือแถบด้านข้าง

| URL | เปิด |
|-----|-------|
| `iappmanager://certificates` | ใบรับรองและตัวระบุ |
| `iappmanager://users` | ผู้ใช้และเข้าถึง |
| `iappmanager://reports` | รายงาน |
| `iappmanager://settings` | การตั้งค่า |
| `iappmanager://add-account` | เพิ่มบัญชีผู้ใช้คีย์ API |
| `iappmanager://about` | เกี่ยวกับ |
| `iappmanager://feedback` | อีเมลข้อเสนอแนะ |
| `iappmanager://in-app-review` | อัตโนมัติ |

## คู่มือการเรียกดู

| URL | Guide |
|-----|-------|
| `iappmanager://feature-guide` | การเดินทัวร์แบบธรรมชาติ |
| `iappmanager://usage-guide` | คู่มือการใช้งาน |
| `iappmanager://widget-guide` | คู่มือวิดเจ็ต |
| `iappmanager://shortcuts-guide` | คู่มือทางลัด |
| `iappmanager://release-guide` | พร้อมปล่อย |
| `iappmanager://iap-guide` | การบอกรับข้อมูล AP |
| `iappmanager://testflight-guide` | & ขาว |
| `iappmanager://reports-guide` | รายงาน |

ส่วน เชื่อม ที่ ลึก ของ ฟองน้ํา ที่ เย็น และ อบอุ่น ซึ่ง เย็น จัด เพื่อ ให้ การ เดิน ทาง เสร็จ ก่อน. ส่วนติดต่อของ App สามารถเปิดโปรแกรมที่จัดการได้โดยมีโมดูลเลือก

</section>
<section lang="de" markdown="1">

iAppManager unterstützt ** `iappmanager://` ** Links für Shortcuts, Widgets, App Intents und Home Screen Aktionen.

## Linkformat


```
iappmanager://{host}[/…]
```


## Apps & Module

| URL | Öffnet |
|-----|-------|
| `iappmanager://apps` | Meine Apps |
| `iappmanager://apps/{appleId}` | Spezifische App (Übersicht) |
| `iappmanager://apps/{appleId}/{tab}` | App-Detailmodul | `iappmanager://` ist die numerische App Store Connect / App Store App ID. `iappmanager://apps` Beispiele:

| Tab | Modul |
|-----|--------|
| `overview` | Übersicht |
| `versions` | Fassungen |
| `builds` | Bauten |
| `backgroundAssets` | Hintergrund-Assets |
| `encryption` | Verschlüsselung |
| `submissions` | Überprüfungsvorschläge |
| `reviewDetail` | Details zur Überprüfung |
| `metadata` | Metadaten |
| `media` | Screenshots & Previews |
| `productPages` | Kundenspezifische Produktseiten |
| `appEvents` | In-App-Events |
| `appClips` | App Clips |
| `experiments` | Lagerversuche |
| `nominations` | Mit Nominierungen |
| `availability` | Verfügbarkeit |
| `pricing` | Preisgestaltung |
| `ageRating` | Altersbewertung |
| `accessibility` | Zugänglichkeit |
| `appTags` | App Tags |
| `iap` | In-App Käufe |
| `gameCenter` | Game Center |
| `testflight` | Prüfflug |
| `reviews` | Kundenbewertungen |
| `privacy` | Privatsphäre (Ernährungshinweis) |
| `promoCodes` | Promo-Codes |
| `webhooks` | Webhooks |

Beispiel: `iappmanager://` ## Sidebar & Tools

| URL | Öffnet |
|-----|-------|
| `iappmanager://certificates` | Zertifikate und Kennungen |
| `iappmanager://users` | Nutzer & Access |
| `iappmanager://reports` | Berichte |
| `iappmanager://settings` | Einstellungen |
| `iappmanager://add-account` | API Key Account hinzufügen |
| `iappmanager://about` | Über |
| `iappmanager://feedback` | Feedback-E-Mail |
| `iappmanager://in-app-review` | Rate prompt |

## In-App Guides

| URL | Guide |
|-----|-------|
| `iappmanager://feature-guide` | Feature Tour |
| `iappmanager://usage-guide` | Nutzungsanleitung |
| `iappmanager://widget-guide` | Widget-Anleitung |
| `iappmanager://shortcuts-guide` | Kurzbefehle-Anleitung |
| `iappmanager://release-guide` | Freigabebereitschaft |
| `iappmanager://iap-guide` | IAP & Abonnements |
| `iappmanager://testflight-guide` | Prüfflug |
| `iappmanager://reports-guide` | Berichte |

Kalte und warme Starts puffern kurze tiefe Links, damit das Onboarding zuerst beendet werden kann. App Intents kann auch eine verwaltete App mit einem optionalen Modul öffnen.

</section>
<section lang="fr" markdown="1">

iAppManager prend en charge ** `iappmanager://` ** liens pour raccourcis, widgets, App Intents et Home Screen actions.

## Format de lien


```
iappmanager://{host}[/…]
```


## Applications & modules

| URL | Ouvre |
|-----|-------|
| `iappmanager://apps` | Mes applications |
| `iappmanager://apps/{appleId}` | App spécifique (Aperçu) |
| `iappmanager://apps/{appleId}/{tab}` | Module de détail de l'application | `iappmanager://` C1    exemples :

| Tab | Module |
|-----|--------|
| `overview` | Aperçu général |
| `versions` | Versions |
| `builds` | Constructions |
| `backgroundAssets` | Actifs de base |
| `encryption` | Chiffrement |
| `submissions` | Demandes de réexamen |
| `reviewDetail` | Détail du réexamen |
| `metadata` | Métadonnées |
| `media` | Captures d'écran et aperçus |
| `productPages` | Pages de produits personnalisées |
| `appEvents` | Événements dans l'application |
| `appClips` | Clips d'application |
| `experiments` | Expériences de stockage |
| `nominations` | Présentation de candidatures |
| `availability` | Disponibilité |
| `pricing` | Prix |
| `ageRating` | Taux d'âge |
| `accessibility` | Accessibilité |
| `appTags` | Étiquettes de l'application |
| `iap` | Achats dans l'application |
| `gameCenter` | Centre de jeu |
| `testflight` | Essai |
| `reviews` | Avis clients |
| `privacy` | Vie privée (note de nutrition) |
| `promoCodes` | Codes promotionnels |
| `webhooks` | Boucliers Web |

Exemple : `iappmanager://` ## Barre latérale & outils

| URL | Ouvre |
|-----|-------|
| `iappmanager://certificates` | Certificats et identifiants |
| `iappmanager://users` | Utilisateurs & Accès |
| `iappmanager://reports` | Rapports |
| `iappmanager://settings` | Réglages |
| `iappmanager://add-account` | Ajouter un compte API Key |
| `iappmanager://about` | À propos |
| `iappmanager://feedback` | E-mail de commentaires |
| `iappmanager://in-app-review` | Taux |

## Guides d'application

| URL | Guide |
|-----|-------|
| `iappmanager://feature-guide` | Visite principale |
| `iappmanager://usage-guide` | Guide d'utilisation |
| `iappmanager://widget-guide` | Guide des widgets |
| `iappmanager://shortcuts-guide` | Guide Raccourcis |
| `iappmanager://release-guide` | Préparation à la libération |
| `iappmanager://iap-guide` | IAP & abonnements |
| `iappmanager://testflight-guide` | Essai |
| `iappmanager://reports-guide` | Rapports |

Les lancements froids et chauds tampons liens profonds brièvement afin que l'embarquement peut terminer en premier. App Intents peut également ouvrir une application gérée avec un module optionnel.

</section>
<section lang="tr" markdown="1">

iAppManager ** `iappmanager://` ** Kısa kesimler, widgets, App niyetleri ve Home Ekran eylemleri için bağlantılar.

## Bağlantı biçimi


```
iappmanager://{host}[/…]
```


## Uygulamalar ve modüller

| URL | Açar |
|-----|-------|
| `iappmanager://apps` | Uygulamalarım |
| `iappmanager://apps/{appleId}` | Özel uygulama (Overview) |
| `iappmanager://apps/{appleId}/{tab}` | App detay modülü | `iappmanager://` is the numeric App Store Connect / App Store app id. `iappmanager://apps` örnekler:

| Tab | Modül Modül |
|-----|--------|
| `overview` | Genel Bakış |
| `versions` | Versions |
| `builds` | Yapılar |
| `backgroundAssets` | Arka plan Varlıkları |
| `encryption` | Şifreleme |
| `submissions` | Submissions |
| `reviewDetail` | İnceleme Detaylı Bilgi |
| `metadata` | Metadata |
| `media` | Ekranlar ve Previews |
| `productPages` | Özel Ürün Sayfaları |
| `appEvents` | In-App Events |
| `appClips` | App Clips |
| `experiments` | Mağaza Deneyleri |
| `nominations` | Nominations |
| `availability` | Erişilebilirlik |
| `pricing` | Fiyatlandırma |
| `ageRating` | Age Rating |
| `accessibility` | Erişilebilirlik |
| `appTags` | App Tags |
| `iap` | In-App Alımları |
| `gameCenter` | Oyun Merkezi |
| `testflight` | TestFlight |
| `reviews` | Müşteri Yorumları |
| `privacy` | Gizlilik (netrition note) |
| `promoCodes` | Promosyon kodları |
| `webhooks` | Webhooks |

Örnek: `iappmanager://` ## Sidebar & araçları

| URL | Açar |
|-----|-------|
| `iappmanager://certificates` | Sertifikalar ve Identifiers |
| `iappmanager://users` | Kullanıcılar & Access |
| `iappmanager://reports` | Raporlar |
| `iappmanager://settings` | Ayarlar |
| `iappmanager://add-account` | API Key hesabı ekle |
| `iappmanager://about` | About About About About About About About About About About About About About About About About About About About About About About About About About About About About About About About About About About About About About About About About About About About About About About About About About About About About About About About About About About About About About About About About About About About About About About About About About About About About About About About About About About About About About About About About About About About About About About About About About About About About About About About About About About About About About About About About About About About About About About About About About About About About About About About About About About About About About About About About About About About About About About About About About About About About About About About About About About About About About About About About About About About About About About About About About About About About About About About About About About About About About About About About About About About About About About About About About About About About About About About About About About About About About About About About About About About About About About About About About About About About About About About About About About About About About About About About About About About About About About About About About About About About About About About About About About About About About About About About |
| `iappmanager://feedback` | Geri bildirim e-postası |
| `iappmanager://in-app-review` | Hız |

## In-app rehberleri

| URL | Guide |
|-----|-------|
| `iappmanager://feature-guide` | Özel tur |
| `iappmanager://usage-guide` | Kullanım kılavuzu |
| `iappmanager://widget-guide` | Widget kılavuzu |
| `iappmanager://shortcuts-guide` | Kısayol kılavuzu |
| `iappmanager://release-guide` | Duyuru |
| `iappmanager://iap-guide` | IAP & abonelikler |
| `iappmanager://testflight-guide` | TestFlight |
| `iappmanager://reports-guide` | Raporlar |

Soğuk ve sıcak havalimanları kısa bir süre önce bitirebilir. App niyetleri ayrıca belirli bir modülle yönetilen bir uygulama açabilir.

</section>
