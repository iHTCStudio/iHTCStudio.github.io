---
layout: doc
title: iPrecepts — Shortcut Links
app_id: iPrecepts
doc_title_en: Shortcut Links
doc_title_zh_cn: 快捷链接说明
doc_title_zh_tw: 快捷連結說明
description: iprecepts:// deep links for iPrecepts — passage, daily, recite, study, hunt, collections, settings guides, and more.
---

<section lang="en" markdown="1">

iPrecepts supports **`iprecepts://`** shortcut links (URL scheme). Cold start and Home Screen shortcuts are delivered through a unified buffer so links are not opened twice after onboarding.

## Link format

```
iprecepts://{host}?{params}
```

## Passages & authors

| URL | Opens |
|-----|-------|
| `iprecepts://passage?id={id}` | Passage detail |
| `iprecepts://saying?id={id}` / `iprecepts://couplet?id={id}` / `iprecepts://poem?id={id}` | Same as passage (compatibility) |
| `iprecepts://passage?id={id}&card=1` | Passage detail and card sheet |
| `iprecepts://card?id={id}` / `iprecepts://share-card?id={id}` | Precept cards |
| `iprecepts://author?id={id}` | Author detail |
| `iprecepts://recite` / `iprecepts://recite?id={id}` | Recite flow |

## Discovery & practice

| URL | Opens |
|-----|-------|
| `iprecepts://home` | Home |
| `iprecepts://daily` | Daily Precept |
| `iprecepts://random` | Random passage |
| `iprecepts://favorites` | Favorites |
| `iprecepts://famous` | Famous lines |
| `iprecepts://search` / `iprecepts://search?q={query}` | Search |
| `iprecepts://study` / `iprecepts://study?id={id}` | Family Study |
| `iprecepts://hunt` | Precept Hunt (`keyword-hunt` / `flyflower`) |
| `iprecepts://handwriting` | Handwriting search (`handwrite`; iOS) |
| `iprecepts://mastered` | Mastered (`progress`) |
| `iprecepts://categories` / `iprecepts://categories?section=` | Browse |
| `iprecepts://collection?id=` | Collection / book (zhuxi / zhubailu / yanshi / zhuge / zeng / yuanshi / qian / tingxun / shortworks) |
| `iprecepts://corpus` | All passages (`all`) |
| `iprecepts://last-read` | Last read |
| `iprecepts://reading-history` | Reading history |
| `iprecepts://notes` | Notes |
| `iprecepts://compare` | Parallel compare |
| `iprecepts://theme?id=` | Theme |
| `iprecepts://authors` | Authors |

## Settings & guides

| URL | Opens |
|-----|-------|
| `iprecepts://settings` | Settings |
| `iprecepts://usage-guide` | Usage guide |
| `iprecepts://widget-guide` | Widget guide |
| `iprecepts://shortcuts-guide` | Shortcuts guide |
| `iprecepts://feature-guide` | Replay onboarding |
| `iprecepts://feedback` | Feedback email |
| `iprecepts://in-app-review` | In-app / Store review entry |

## Examples

```
iprecepts://daily
iprecepts://passage?id=1
iprecepts://passage?id=1&card=1
iprecepts://compare
iprecepts://collection?id=yanshi
iprecepts://study
iprecepts://hunt
```

## Notes

- Parameters are case-sensitive where IDs are numeric.
- Siri, Shortcuts, widgets, and Control Center controls use the same deep-link routes.
- See the in-app **Settings → Help** guides for the latest list.

</section>
<section lang="zh-CN" markdown="1">

爱家训支持 **`iprecepts://`** 快捷链接（URL Scheme）。冷启动与主屏快捷经统一缓冲投递，避免引导页结束后重复打开。

## 链接格式

```
iprecepts://{host}?{params}
```

## 篇目与作者

| URL | 打开 |
|-----|------|
| `iprecepts://passage?id={id}` | 篇目详情 |
| `iprecepts://saying?id={id}` / `iprecepts://couplet?id={id}` / `iprecepts://poem?id={id}` | 同详情（兼容别名） |
| `iprecepts://passage?id={id}&card=1` | 详情并弹出训卡 |
| `iprecepts://card?id={id}` / `iprecepts://share-card?id={id}` | 训卡 |
| `iprecepts://author?id={id}` | 作者详情 |
| `iprecepts://recite` / `iprecepts://recite?id={id}` | 诵读 |

## 发现与学堂

| URL | 打开 |
|-----|------|
| `iprecepts://home` | 首页 |
| `iprecepts://daily` | 今日一训 |
| `iprecepts://random` | 随机篇目 |
| `iprecepts://favorites` | 收藏 |
| `iprecepts://famous` | 金句 |
| `iprecepts://search` / `iprecepts://search?q={query}` | 搜索 |
| `iprecepts://study` / `iprecepts://study?id={id}` | 家训学堂 |
| `iprecepts://hunt` | 寻训（`keyword-hunt` / `flyflower`） |
| `iprecepts://handwriting` | 手写搜索（`handwrite`；iOS） |
| `iprecepts://mastered` | 已掌握（`progress`） |
| `iprecepts://categories` / `iprecepts://categories?section=` | 分类浏览 |
| `iprecepts://collection?id=` | 合集 / 典籍（zhuxi / zhubailu / yanshi / zhuge / zeng / yuanshi / qian / tingxun / shortworks） |
| `iprecepts://corpus` | 全部篇目（`all`） |
| `iprecepts://last-read` | 最近阅读 |
| `iprecepts://reading-history` | 阅读历史 |
| `iprecepts://notes` | 笔记 |
| `iprecepts://compare` | 跨代对照 |
| `iprecepts://theme?id=` | 主题 |
| `iprecepts://authors` | 作者 |

## 设置与指南

| URL | 打开 |
|-----|------|
| `iprecepts://settings` | 设置 |
| `iprecepts://usage-guide` | 使用说明 |
| `iprecepts://widget-guide` | 小组件指南 |
| `iprecepts://shortcuts-guide` | 快捷指南 |
| `iprecepts://feature-guide` | 重播功能引导 |
| `iprecepts://feedback` | 反馈邮件 |
| `iprecepts://in-app-review` | 应用内评价入口 |

## 示例

```
iprecepts://daily
iprecepts://passage?id=1
iprecepts://passage?id=1&card=1
iprecepts://compare
iprecepts://collection?id=yanshi
iprecepts://study
iprecepts://hunt
```

## 说明

- 数字 ID 参数区分大小写。
- Siri、快捷指令、小组件与控制中心使用同一套深链。
- 最新列表见应用内 **设置 → 帮助**。

</section>
<section lang="zh-TW" markdown="1">

愛家訓支援 **`iprecepts://`** 快捷連結（URL Scheme）。冷啟動與主畫面捷徑經統一緩衝投遞，避免引導頁結束後重複打開。

## 連結格式

```
iprecepts://{host}?{params}
```

## 篇目與作者

| URL | 打開 |
|-----|------|
| `iprecepts://passage?id={id}` | 篇目詳情 |
| `iprecepts://saying?id={id}` / `iprecepts://couplet?id={id}` / `iprecepts://poem?id={id}` | 同詳情（相容別名） |
| `iprecepts://passage?id={id}&card=1` | 詳情並彈出訓卡 |
| `iprecepts://card?id={id}` / `iprecepts://share-card?id={id}` | 訓卡 |
| `iprecepts://author?id={id}` | 作者詳情 |
| `iprecepts://recite` / `iprecepts://recite?id={id}` | 誦讀 |

## 發現與學堂

| URL | 打開 |
|-----|------|
| `iprecepts://home` | 首頁 |
| `iprecepts://daily` | 今日一訓 |
| `iprecepts://random` | 隨機篇目 |
| `iprecepts://favorites` | 收藏 |
| `iprecepts://famous` | 金句 |
| `iprecepts://search` / `iprecepts://search?q={query}` | 搜尋 |
| `iprecepts://study` / `iprecepts://study?id={id}` | 家訓學堂 |
| `iprecepts://hunt` | 尋訓（`keyword-hunt` / `flyflower`） |
| `iprecepts://handwriting` | 手寫搜尋（`handwrite`；iOS） |
| `iprecepts://mastered` | 已掌握（`progress`） |
| `iprecepts://categories` / `iprecepts://categories?section=` | 分類瀏覽 |
| `iprecepts://collection?id=` | 合集 / 典籍（zhuxi / zhubailu / yanshi / zhuge / zeng / yuanshi / qian / tingxun / shortworks） |
| `iprecepts://corpus` | 全部篇目（`all`） |
| `iprecepts://last-read` | 最近閱讀 |
| `iprecepts://reading-history` | 閱讀歷史 |
| `iprecepts://notes` | 筆記 |
| `iprecepts://compare` | 跨代對照 |
| `iprecepts://theme?id=` | 主題 |
| `iprecepts://authors` | 作者 |

## 設定與指南

| URL | 打開 |
|-----|------|
| `iprecepts://settings` | 設定 |
| `iprecepts://usage-guide` | 使用說明 |
| `iprecepts://widget-guide` | 小工具指南 |
| `iprecepts://shortcuts-guide` | 捷徑指南 |
| `iprecepts://feature-guide` | 重播功能引導 |
| `iprecepts://feedback` | 回饋郵件 |
| `iprecepts://in-app-review` | 應用內評價入口 |

## 範例

```
iprecepts://daily
iprecepts://passage?id=1
iprecepts://passage?id=1&card=1
iprecepts://compare
iprecepts://collection?id=yanshi
iprecepts://study
iprecepts://hunt
```

## 說明

- 數字 ID 參數區分大小寫。
- Siri、捷徑、小工具與控制中心使用同一套深鏈。
- 最新列表見應用內 **設定 → 說明**。

</section>
<section lang="ja" markdown="1">

iPreceptsは** `iprecepts://` **ショートカットリンク(URLスキーム)をサポートしています。 コールドスタートとホーム画面のショートカットは、統一されたバッファを介して配信されますので、リンクはオンボーディング後2回開いていません。

## リンク形式


```
iprecepts://{host}?{params}
```


## パスポートと著者

| URL | 開く画面 |
|-----|-------|
| `iprecepts://passage?id={id}` | 章句の詳細 |
| `iprecepts://saying?id={id}` / `iprecepts://couplet?id={id}` / `iprecepts://poem?id={id}` | 通路と同じ(互換性) |
| `iprecepts://passage?id={id}&card=1` | 通路の細部およびカード シート |
| `iprecepts://card?id={id}` / `iprecepts://share-card?id={id}` | クレジットカード |
| `iprecepts://author?id={id}` | 作者の詳細 |
| `iprecepts://recite` / `iprecepts://recite?id={id}` | 誦読フロー |

## ディスカバリー&プラクティス

| URL | 開く画面 |
|-----|-------|
| `iprecepts://home` | ホーム |
| `iprecepts://daily` | 毎日の受け入れ |
| `iprecepts://random` | ランダムな章句 |
| `iprecepts://favorites` | お気に入り |
| `iprecepts://famous` | 名句一覧 |
| `iprecepts://search` / `iprecepts://search?q={query}` | 検索 |
| `iprecepts://study` / `iprecepts://study?id={id}` | ファミリースタディ |
| `iprecepts://hunt` | チャント (`keyword-hunt`/`flyflower`) |
| `iprecepts://handwriting` | 手書き検索 (`handwrite`; iOS) |
| `iprecepts://mastered` | マスタード (`progress`) |
| `iprecepts://categories` / `iprecepts://categories?section=` | ブラウズ |
| `iprecepts://collection?id=` | コレクション / book(zhuxi / zhubailu / yanshi / zhuge / zeng / yuanshi / qian / tingxun / ショートワークス) |
| `iprecepts://corpus` | すべての通路 (`all`) |
| `iprecepts://last-read` | 最後に読んだ項目 |
| `iprecepts://reading-history` | 閲覧履歴 |
| `iprecepts://notes` | ノート |
| `iprecepts://compare` | 並列比較 |
| `iprecepts://theme?id=` | テーマ: |
| `iprecepts://authors` | プロフィール |

## 設定とガイド

| URL | 開く画面 |
|-----|-------|
| `iprecepts://settings` | 設定 |
| `iprecepts://usage-guide` | 使い方ガイド |
| `iprecepts://widget-guide` | ウィジェットガイド |
| `iprecepts://shortcuts-guide` | ショートカットガイド |
| `iprecepts://feature-guide` | オンボーディングの再生 |
| `iprecepts://feedback` | フィードバックメール |
| `iprecepts://in-app-review` | アプリ内／App Store レビュー |

## 例


```
iprecepts://daily
iprecepts://passage?id=1
iprecepts://passage?id=1&card=1
iprecepts://compare
iprecepts://collection?id=yanshi
iprecepts://study
iprecepts://hunt
```


## ノート

- パラメータはIDが数値である場合感度です。
- シリ、ショートカット、ウィジェット、およびコントロールセンターコントロールは、同じディープリンクルートを使用します。
- 最新リストのアプリ内設定 → Help** ガイドを参照してください。

</section>
<section lang="ko" markdown="1">

iPrecepts 지원 ** `iprecepts://` ** 단축키 링크 (URL 계획). 콜드 시작 및 홈 화면 단축은 통합 버퍼를 통해 전달되므로 링크가 내장 된 후 두 번 열리지 않습니다.

## 링크 형식


```
iprecepts://{host}?{params}
```


## 책임 & 저자

| URL | 열리는 화면 |
|-----|-------|
| `iprecepts://passage?id={id}` | 구절 상세 |
| `iprecepts://saying?id={id}` / `iprecepts://couplet?id={id}` / `iprecepts://poem?id={id}` | 통행과 같 ( 겸용성) |
| `iprecepts://passage?id={id}&card=1` | 통행 세부사항과 카드 장 |
| `iprecepts://card?id={id}` / `iprecepts://share-card?id={id}` | 카드 제외 |
| `iprecepts://author?id={id}` | 작가 상세 |
| `iprecepts://recite` / `iprecepts://recite?id={id}` | 낭독 흐름 |

## 디스커버리 & 연습

| URL | 열리는 화면 |
|-----|-------|
| `iprecepts://home` | 홈 |
| `iprecepts://daily` | 매일 |
| `iprecepts://random` | 무작위 구절 |
| `iprecepts://favorites` | 즐겨찾기 |
| `iprecepts://famous` | 명구 목록 |
| `iprecepts://search` / `iprecepts://search?q={query}` | 검색 |
| `iprecepts://study` / `iprecepts://study?id={id}` | 가족 학습 |
| `iprecepts://hunt` | 헌트를 제외하고 (`keyword-hunt`/`flyflower`) |
| `iprecepts://handwriting` | Handwriting search (`handwrite`; iOS) |
| `iprecepts://mastered` | 마스터 (`progress`) |
| `iprecepts://categories` / `iprecepts://categories?section=` | 둘러보기 |
| `iprecepts://collection?id=` | 수집/책 (zhuxi/zhubailu/yanshi/zhuge/zeng/yuanshi/Qian/tingxun/shortworks) |
| `iprecepts://corpus` | 모든 통행 (`all`) |
| `iprecepts://last-read` | 마지막으로 읽은 항목 |
| `iprecepts://reading-history` | 읽기 기록 |
| `iprecepts://notes` | 메모 |
| `iprecepts://compare` | 병렬 비교 |
| `iprecepts://theme?id=` | 이름 * |
| `iprecepts://authors` | 이름 * |

## 설정 및 가이드

| URL | 열리는 화면 |
|-----|-------|
| `iprecepts://settings` | 설정 |
| `iprecepts://usage-guide` | 사용 가이드 |
| `iprecepts://widget-guide` | 위젯 가이드 |
| `iprecepts://shortcuts-guide` | 단축어 가이드 |
| `iprecepts://feature-guide` | 온보딩 다시 보기 |
| `iprecepts://feedback` | 피드백 이메일 |
| `iprecepts://in-app-review` | 앱 내 / App Store 리뷰 |

## 예시


```
iprecepts://daily
iprecepts://passage?id=1
iprecepts://passage?id=1&card=1
iprecepts://compare
iprecepts://collection?id=yanshi
iprecepts://study
iprecepts://hunt
```


## 메모

- 매개 변수는 ID가 숫자인지 여부를 감지합니다.
- Siri, Shortcuts, 위젯 및 제어 센터 제어는 동일한 딥 링크 루트를 사용합니다.
- in-app**Settings → 도움말** 최신 목록 안내

</section>
<section lang="ru" markdown="1">

iPrecepts поддерживает ярлыки ** `iprecepts://` ** (схема URL). Холодный старт и ярлыки домашнего экрана доставляются через единый буфер, поэтому ссылки не открываются дважды после входа.

## Формат ссылки


```
iprecepts://{host}?{params}
```


## Проходы и авторы

| URL | Открывает |
|-----|-------|
| `iprecepts://passage?id={id}` | Страница отрывка |
| `iprecepts://saying?id={id}` / `iprecepts://couplet?id={id}` / `iprecepts://poem?id={id}` | Совместимость (Compatibility) |
| `iprecepts://passage?id={id}&card=1` | Детали проезда и карточный лист |
| `iprecepts://card?id={id}` / `iprecepts://share-card?id={id}` | Рецепт карты |
| `iprecepts://author?id={id}` | Страница автора |
| `iprecepts://recite` / `iprecepts://recite?id={id}` | Режим чтения вслух |

## Discovery & Practice

| URL | Открывает |
|-----|-------|
| `iprecepts://home` | Главная |
| `iprecepts://daily` | Ежедневные предписания |
| `iprecepts://random` | Случайный отрывок |
| `iprecepts://favorites` | Избранное |
| `iprecepts://famous` | Знаменитые строки |
| `iprecepts://search` / `iprecepts://search?q={query}` | Поиск |
| `iprecepts://study` / `iprecepts://study?id={id}` | Семейное исследование |
| `iprecepts://hunt` | Precept Hunt («охота за ключевыми словами» / «флайфлауэр») |
| `iprecepts://handwriting` | Поиск почерка («handwrite»; iOS) |
| `iprecepts://mastered` | Мастеринг («Прогресс») |
| `iprecepts://categories` / `iprecepts://categories?section=` | Обзор |
| `iprecepts://collection?id=` | Коллекция / книга (цхуси / жубайлу / янши / жуге / цэн / юаньши / цянь / тингсун / короткие работы) |
| `iprecepts://corpus` | Все пассажи («All») |
| `iprecepts://last-read` | Последнее прочитанное |
| `iprecepts://reading-history` | История чтения |
| `iprecepts://notes` | Заметки |
| `iprecepts://compare` | Параллельное сравнение |
| `iprecepts://theme?id=` | Тема |
| `iprecepts://authors` | авторы |

## Настройки и руководства

| URL | Открывает |
|-----|-------|
| `iprecepts://settings` | Настройки |
| `iprecepts://usage-guide` | Руководство по использованию |
| `iprecepts://widget-guide` | Руководство по виджетам |
| `iprecepts://shortcuts-guide` | Руководство по «Командам» |
| `iprecepts://feature-guide` | Повторное знакомство |
| `iprecepts://feedback` | Письмо с отзывом |
| `iprecepts://in-app-review` | Отзыв в приложении / App Store |

## Примеры


```
iprecepts://daily
iprecepts://passage?id=1
iprecepts://passage?id=1&card=1
iprecepts://compare
iprecepts://collection?id=yanshi
iprecepts://study
iprecepts://hunt
```


## Заметки

- Параметры чувствительны к регистру, где идентификаторы являются числовыми.
- Siri, ярлыки, виджеты и элементы управления Центра управления используют одни и те же маршруты глубокой связи.
- Смотрите в приложении ** Настройки → Справочные руководства ** для последнего списка.

</section>
<section lang="th" markdown="1">

iPresids รองรับ ** c0 BAR * ลิงก์ลัด (RUL scheme) การเริ่มหน้าจอหน้าจอเย็นและหน้าจอบ้าน จะถูกส่งไปผ่านระบบบัฟเฟอร์แบบรวม ดังนั้นลิงก์จึงไม่ถูกเปิดสองครั้งหลังจากขึ้นเครื่อง

## รูปแบบลิงก์


```
iprecepts://{host}?{params}
```


## ผู้เขียน

| URL | เปิด |
|-----|-------|
| `iprecepts://passage?id={id}` | รายละเอียดข้อความ |
| `iprecepts://saying?id={id}` / `iprecepts://couplet?id={id}` / `iprecepts://poem?id={id}` | เช่นเดียวกันกับเนื้อเรื่อง (ความเข้ากันได้) |
| `iprecepts://passage?id={id}&card=1` | รายละเอียดและนามบัตร |
| `iprecepts://card?id={id}` / `iprecepts://share-card?id={id}` | ไพ่สําเร็จรูป |
| `iprecepts://author?id={id}` | รายละเอียดผู้แต่ง |
| `iprecepts://recite` / `iprecepts://recite?id={id}` | โฟลว์การท่อง |

## การท่องเว็บ

| URL | เปิด |
|-----|-------|
| `iprecepts://home` | หน้าแรก |
| `iprecepts://daily` | ทุก ๆ วัน |
| `iprecepts://random` | ข้อความแบบสุ่ม |
| `iprecepts://favorites` | รายการโปรด |
| `iprecepts://famous` | บรรทัดขึ้นชื่อ |
| `iprecepts://search` / `iprecepts://search?q={query}` | ค้นหา |
| `iprecepts://study` / `iprecepts://study?id={id}` | การ ศึกษา ประจํา ครอบครัว |
| `iprecepts://hunt` | Precept Hunt ('คีย์เวิร์ด-ฮันต์' / 'ดอกไม้แมลงวัน') |
| `iprecepts://handwriting` | สืบค้นเมื่อเขียนด้วยมือ ('เขียนเอง'; OS) |
| `iprecepts://mastered` | สําเร็จการศึกษาแล้ว ('รุก') |
| `iprecepts://categories` / `iprecepts://categories?section=` | เรียกดู |
| `iprecepts://collection?id=` | คอลเลคชั่น / หนังสือ (ซูซี่ / ซูบัยลู / หยวนชี / ชุจ / ซ็องจี / หยวนชี / เจียวชิ / เจียน / ติงซ็อง / งานสั้น) |
| `iprecepts://corpus` | ทุกช่อง (ทั้งหมด) |
| `iprecepts://last-read` | รายการที่อ่านล่าสุด |
| `iprecepts://reading-history` | ประวัติการอ่าน |
| `iprecepts://notes` | บันทึก |
| `iprecepts://compare` | เปรียบเทียบด้านเท่า |
| `iprecepts://theme?id=` | ชุดตกแต่ง |
| `iprecepts://authors` | ผู้เขียน |

## การตั้งค่าและคู่มือ

| URL | เปิด |
|-----|-------|
| `iprecepts://settings` | การตั้งค่า |
| `iprecepts://usage-guide` | คู่มือการใช้งาน |
| `iprecepts://widget-guide` | คู่มือวิดเจ็ต |
| `iprecepts://shortcuts-guide` | คู่มือทางลัด |
| `iprecepts://feature-guide` | เล่นทัวร์แนะนำอีกครั้ง |
| `iprecepts://feedback` | อีเมลข้อเสนอแนะ |
| `iprecepts://in-app-review` | รีวิวในแอป / App Store |

## ตัวอย่าง


```
iprecepts://daily
iprecepts://passage?id=1
iprecepts://passage?id=1&card=1
iprecepts://compare
iprecepts://collection?id=yanshi
iprecepts://study
iprecepts://hunt
```


## บันทึก

- พารามิเตอร์คือความไวของตัวเลข
- ไซรี, ทางลัด, วิดเจ็ต, และศูนย์ควบคุม ใช้เส้นทางลับเดียวกัน
- ดู In-appings-Cettings softs for the list ล่าสุด

</section>
<section lang="de" markdown="1">

iPrecepts unterstützt ** `iprecepts://` ** Shortcut Links (URL-Schema). Kaltstart- und Home Screen-Verknüpfungen werden über einen einheitlichen Puffer geliefert, so dass Links nach dem Onboarding nicht zweimal geöffnet werden.

## Linkformat


```
iprecepts://{host}?{params}
```


## Passagen & Autoren

| URL | Öffnet |
|-----|-------|
| `iprecepts://passage?id={id}` | Passagen-Detail |
| `iprecepts://saying?id={id}` / `iprecepts://couplet?id={id}` / `iprecepts://poem?id={id}` | Wie Passage (Kompatibilität) |
| `iprecepts://passage?id={id}&card=1` | Angaben zum Durchgang und Kartenblatt |
| `iprecepts://card?id={id}` / `iprecepts://share-card?id={id}` | Rezeptkarten |
| `iprecepts://author?id={id}` | Autorendetail |
| `iprecepts://recite` / `iprecepts://recite?id={id}` | Rezitationsablauf |

## Entdeckung und Praxis

| URL | Öffnet |
|-----|-------|
| `iprecepts://home` | Startseite |
| `iprecepts://daily` | Tägliches Rezept |
| `iprecepts://random` | Zufällige Passage |
| `iprecepts://favorites` | Favoriten |
| `iprecepts://famous` | Berühmte Zeilen |
| `iprecepts://search` / `iprecepts://search?q={query}` | Suche |
| `iprecepts://study` / `iprecepts://study?id={id}` | Familienstudie |
| `iprecepts://hunt` | Precept Hunt (`keyword-hunt` / `flyflower`) |
| `iprecepts://handwriting` | Handschriftsuche (`handwrite`; iOS) |
| `iprecepts://mastered` | gemeistert („Fortschritt) |
| `iprecepts://categories` / `iprecepts://categories?section=` | Durchsuchen |
| `iprecepts://collection?id=` | Sammlung / Buch (zhuxi / zhubailu / yanshi / zhuge / zeng / yuanshi / qian / tingxun / shortworks) |
| `iprecepts://corpus` | Alle Passagen (`all`) |
| `iprecepts://last-read` | Zuletzt gelesen |
| `iprecepts://reading-history` | Leseverlauf |
| `iprecepts://notes` | Notizen |
| `iprecepts://compare` | Parallelvergleich |
| `iprecepts://theme?id=` | Thema |
| `iprecepts://authors` | Autoren |

## Einstellungen & Anleitungen

| URL | Öffnet |
|-----|-------|
| `iprecepts://settings` | Einstellungen |
| `iprecepts://usage-guide` | Nutzungsanleitung |
| `iprecepts://widget-guide` | Widget-Anleitung |
| `iprecepts://shortcuts-guide` | Kurzbefehle-Anleitung |
| `iprecepts://feature-guide` | Einführung erneut abspielen |
| `iprecepts://feedback` | Feedback-E-Mail |
| `iprecepts://in-app-review` | In-App- / App-Store-Bewertung |

## Beispiele


```
iprecepts://daily
iprecepts://passage?id=1
iprecepts://passage?id=1&card=1
iprecepts://compare
iprecepts://collection?id=yanshi
iprecepts://study
iprecepts://hunt
```


## Notizen

- Parameter sind fallsensibel, wo IDs numerisch sind.
- Siri, Shortcuts, Widgets und Control Center-Steuerelemente verwenden die gleichen Deep-Link-Routen.
- Sehen Sie sich die In-App **Einstellungen → Hilfe ** Anleitungen für die neueste Liste an.

</section>
<section lang="fr" markdown="1">

iPrecepts prend en charge les liens de raccourci ** `iprecepts://` ** (schéma URL). Les raccourcis de démarrage à froid et d'écran d'accueil sont livrés via un tampon unifié de sorte que les liens ne sont pas ouverts deux fois après l'embarquement.

## Format de lien


```
iprecepts://{host}?{params}
```


## Passages et auteurs

| URL | Ouvre |
|-----|-------|
| `iprecepts://passage?id={id}` | Détail du passage |
| `iprecepts://saying?id={id}` / `iprecepts://couplet?id={id}` / `iprecepts://poem?id={id}` | Même chose que le passage (compatibilité) |
| `iprecepts://passage?id={id}&card=1` | Détails du passage et feuille de carte |
| `iprecepts://card?id={id}` / `iprecepts://share-card?id={id}` | Cartes préceptes |
| `iprecepts://author?id={id}` | Détail de l’auteur |
| `iprecepts://recite` / `iprecepts://recite?id={id}` | Flux de récitation |

## Découverte et pratique

| URL | Ouvre |
|-----|-------|
| `iprecepts://home` | Accueil |
| `iprecepts://daily` | Précepte quotidien |
| `iprecepts://random` | Passage aléatoire |
| `iprecepts://favorites` | Favoris |
| `iprecepts://famous` | Vers célèbres |
| `iprecepts://search` / `iprecepts://search?q={query}` | Recherche |
| `iprecepts://study` / `iprecepts://study?id={id}` | Étude familiale |
| `iprecepts://hunt` | Chasse au précepte ( ' chasse au mot clé ' / ' flyflower ') |
| `iprecepts://handwriting` | Recherche d'écriture (`handwrite`; iOS) |
| `iprecepts://mastered` | Maîtrise ('progrès') |
| `iprecepts://categories` / `iprecepts://categories?section=` | Parcourir |
| `iprecepts://collection?id=` | Collection / livre (zhuxi / zhubailu / yanshi / zuge / yuanshi / qian / tingxun / shortworks) |
| `iprecepts://corpus` | Tous les passages |
| `iprecepts://last-read` | Dernière lecture |
| `iprecepts://reading-history` | Historique de lecture |
| `iprecepts://notes` | Notes |
| `iprecepts://compare` | Comparaison parallèle |
| `iprecepts://theme?id=` | Thème |
| `iprecepts://authors` | Auteurs |

## Réglages et guides

| URL | Ouvre |
|-----|-------|
| `iprecepts://settings` | Réglages |
| `iprecepts://usage-guide` | Guide d'utilisation |
| `iprecepts://widget-guide` | Guide des widgets |
| `iprecepts://shortcuts-guide` | Guide Raccourcis |
| `iprecepts://feature-guide` | Rejouer l’accueil |
| `iprecepts://feedback` | E-mail de commentaires |
| `iprecepts://in-app-review` | Avis in-app / App Store |

## Exemples


```
iprecepts://daily
iprecepts://passage?id=1
iprecepts://passage?id=1&card=1
iprecepts://compare
iprecepts://collection?id=yanshi
iprecepts://study
iprecepts://hunt
```


## Notes

- Les paramètres sont sensibles aux cas où les ID sont numériques.
- Les commandes Siri, Shortcuts, Widgets et Control Center utilisent les mêmes itinéraires de liaison profonde.
- Voir la page d'application **Paramètres → Aide** pour la dernière liste.

</section>
<section lang="tr" markdown="1">

IPrecepts ** `iprecepts://` ** kısayol bağlantıları (URL planı). Soğuk başlangıç ve Ev Ekran kısayolları birleşik bir tampon aracılığıyla teslim edilir, bu yüzden bağlantılar gemiden sonra iki kez açılmaz.

## Bağlantı biçimi


```
iprecepts://{host}?{params}
```


## Geçişler ve yazarlar

| URL | Açar |
|-----|-------|
| `iprecepts://passage?id={id}` | Pasaj ayrıntısı |
| `iprecepts://saying?id={id}` / `iprecepts://couplet?id={id}` / `iprecepts://poem?id={id}` | Aynı geçiş (compatability) |
| `iprecepts://passage?id={id}&card=1` | Pasaj detay ve kart sayfası |
| `iprecepts://card?id={id}` / `iprecepts://share-card?id={id}` | Precept kartları |
| `iprecepts://author?id={id}` | Yazar ayrıntısı |
| `iprecepts://recite` / `iprecepts://recite?id={id}` | Okuma akışı |

## Discovery & practice

| URL | Açar |
|-----|-------|
| `iprecepts://home` | Ana sayfa |
| `iprecepts://daily` | Daily Precept |
| `iprecepts://random` | Rastgele pasaj |
| `iprecepts://favorites` | Favoriler |
| `iprecepts://famous` | Ünlü dizeler |
| `iprecepts://search` / `iprecepts://search?q={query}` | Ara |
| `iprecepts://study` / `iprecepts://study?id={id}` | Aile Çalışması |
| `iprecepts://hunt` | Precept Hunt ('keyword-hunt' / "flyflower") |
| `iprecepts://handwriting` | Hand writing search ('handwrite'; iOS) |
| `iprecepts://mastered` | Mastered ('progress') |
| `iprecepts://categories` / `iprecepts://categories?section=` | Gözat |
| `iprecepts://collection?id=` | Koleksiyon / kitap (zhuxi / zhubailu / yanshi / zhuge / zeng / yuanshi / qian / tingxun / kısa çalışmalar) |
| `iprecepts://corpus` | Bütün geçitler ('all') |
| `iprecepts://last-read` | Son okunan |
| `iprecepts://reading-history` | Okuma geçmişi |
| `iprecepts://notes` | Notlar |
| `iprecepts://compare` | Paralel karşılaştırma |
| `iprecepts://theme?id=` | Tema |
| `iprecepts://authors` | Yazarlar |

## Ayarlar ve kılavuzlar

| URL | Açar |
|-----|-------|
| `iprecepts://settings` | Ayarlar |
| `iprecepts://usage-guide` | Kullanım kılavuzu |
| `iprecepts://widget-guide` | Widget kılavuzu |
| `iprecepts://shortcuts-guide` | Kısayol kılavuzu |
| `iprecepts://feature-guide` | Tanıtımı yeniden oynat |
| `iprecepts://feedback` | Geri bildirim e-postası |
| `iprecepts://in-app-review` | Uygulama içi / App Store değerlendirme |

## Örnekler


```
iprecepts://daily
iprecepts://passage?id=1
iprecepts://passage?id=1&card=1
iprecepts://compare
iprecepts://collection?id=yanshi
iprecepts://study
iprecepts://hunt
```


## Notlar

- Parametreler, kimliklerin sayısal olduğu durumlarda hassastır.
- Siri, Shortcuts, widgets ve Control Center kontrolleri aynı derin bağlantı yollarını kullanır.
- In-app **Settings → Yardım** en son liste için kılavuzlar.

</section>
