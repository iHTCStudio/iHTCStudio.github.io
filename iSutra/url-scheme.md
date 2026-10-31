---
layout: doc
title: iSutra — Shortcut Links
app_id: iSutra
doc_title_en: Shortcut Links
doc_title_zh_cn: 快捷链接说明
doc_title_zh_tw: 快捷連結說明
description: isutra:// deep links for iSutra — passage, daily, recite, study, hunt, chant, copy, practice, collections, themes, settings guides, and more.
---

<section lang="en" markdown="1">

iSutra supports **`isutra://`** shortcut links (URL scheme). Cold start and Home Screen shortcuts are delivered through a unified buffer so links are not opened twice after onboarding.

## Link format

```
isutra://{host}?{params}
```

## Sutras & authors

| URL | Opens |
|-----|-------|
| `isutra://passage?id={id}` | Sutra detail |
| `isutra://couplet?id={id}` / `isutra://poem?id={id}` | Same as passage (compatibility) |
| `isutra://author?id={id}` | Translator / author detail |
| `isutra://recite` / `isutra://recite?id={id}` | Recite flow |
| `isutra://large?id=diamond` / `isutra://large?id=dizang` | Large-book volume catalog |

## Discovery & practice

| URL | Opens |
|-----|-------|
| `isutra://home` | Home |
| `isutra://daily` | Today’s Daily Sutra |
| `isutra://random` | Random passage |
| `isutra://favorites` | Favorites |
| `isutra://famous` | Famous lines |
| `isutra://search` / `isutra://search?q={query}` | Search |
| `isutra://study` | Study Hall |
| `isutra://hunt` | Hunt (寻经); aliases `keyword-hunt` / `flyflower` |
| `isutra://count` | Wooden-fish chant (`chant` / `muyu` / `counter`) |
| `isutra://copy` / `isutra://copy?id={id}` | Copy-sutra (iOS) |
| `isutra://practice` | Morning / evening practice |
| `isutra://mastered` | Mastered |
| `isutra://categories` / `isutra://categories?section=` | Browse |
| `isutra://collection?id=` | Collection (e.g. `prajna`, `forty-two`; also `name=`) |
| `isutra://theme?id=` | Theme (e.g. `xingyuan`, `yaoshi`, `platform`) |
| `isutra://last-read` | Last read |
| `isutra://reading-history` | Reading history |
| `isutra://notes` | Notes |

## Settings & guides

| URL | Opens |
|-----|-------|
| `isutra://settings` | Settings |
| `isutra://usage-guide` | Usage guide |
| `isutra://widget-guide` | Widget guide |
| `isutra://shortcuts-guide` | Shortcuts guide |
| `isutra://feature-guide` | Replay onboarding |
| `isutra://privacy` | In-app privacy |
| `isutra://feedback` | Feedback email |
| `isutra://in-app-review` | In-app / Store review entry |

## Examples

```
isutra://daily
isutra://passage?id=1
isutra://large?id=diamond
isutra://count
isutra://copy?id=1
isutra://practice
isutra://collection?id=prajna
isutra://theme?id=xingyuan
isutra://study
isutra://hunt
```

Use these in the Shortcuts app, Home Screen quick actions, widgets, or Safari. See also in-app **Settings → Shortcuts Guide**.

</section>
<section lang="zh-CN" markdown="1">

爱佛经支持 **`isutra://`** 快捷链接（URL Scheme）。冷启动与主屏快捷经统一缓冲投递，避免引导后重复打开。

## 链接格式

```
isutra://{host}?{params}
```

## 经目与译者

| URL | 打开 |
|-----|------|
| `isutra://passage?id={id}` | 经文详情 |
| `isutra://couplet?id={id}` / `isutra://poem?id={id}` | 同上（兼容别名） |
| `isutra://author?id={id}` | 译者详情 |
| `isutra://recite` / `isutra://recite?id={id}` | 诵经 |
| `isutra://large?id=diamond` / `isutra://large?id=dizang` | 大部头分卷目录 |

## 发现与修习

| URL | 打开 |
|-----|------|
| `isutra://home` | 首页 |
| `isutra://daily` | 今日一经 |
| `isutra://random` | 随机经文 |
| `isutra://favorites` | 收藏 |
| `isutra://famous` | 法语 |
| `isutra://search` / `isutra://search?q={query}` | 搜索 |
| `isutra://study` | 持诵学堂 |
| `isutra://hunt` | 寻经（别名 `keyword-hunt` / `flyflower`） |
| `isutra://count` | 木鱼念诵（`chant` / `muyu` / `counter`） |
| `isutra://copy` / `isutra://copy?id={id}` | 抄经（iOS） |
| `isutra://practice` | 早晚功课 |
| `isutra://mastered` | 已掌握 |
| `isutra://categories` / `isutra://categories?section=` | 分类浏览 |
| `isutra://collection?id=` | 合集（如 `prajna`、`forty-two`；亦支持 `name=`） |
| `isutra://theme?id=` | 主题（如 `xingyuan`、`yaoshi`、`platform`） |
| `isutra://last-read` | 最近阅读 |
| `isutra://reading-history` | 浏览记录 |
| `isutra://notes` | 笔记 |

## 设置与指南

| URL | 打开 |
|-----|------|
| `isutra://settings` | 设置 |
| `isutra://usage-guide` | 使用说明 |
| `isutra://widget-guide` | 小组件指南 |
| `isutra://shortcuts-guide` | 快捷指南 |
| `isutra://feature-guide` | 重播功能引导 |
| `isutra://privacy` | 应用内隐私 |
| `isutra://feedback` | 反馈邮件 |
| `isutra://in-app-review` | 应用内 / 商店评价入口 |

## 示例

```
isutra://daily
isutra://passage?id=1
isutra://large?id=diamond
isutra://count
isutra://copy?id=1
isutra://practice
isutra://collection?id=prajna
isutra://theme?id=xingyuan
isutra://study
isutra://hunt
```

可在「快捷指令」、主屏快捷、小组件或 Safari 中使用。亦可参考应用内 **设置 → 快捷指南**。

</section>
<section lang="zh-TW" markdown="1">

愛佛經支援 **`isutra://`** 快捷連結（URL Scheme）。冷啟動與主畫面捷徑經統一緩衝投遞，避免引導後重複開啟。

## 連結格式

```
isutra://{host}?{params}
```

## 經目與譯者

| URL | 開啟 |
|-----|------|
| `isutra://passage?id={id}` | 經文詳情 |
| `isutra://couplet?id={id}` / `isutra://poem?id={id}` | 同上（相容別名） |
| `isutra://author?id={id}` | 譯者詳情 |
| `isutra://recite` / `isutra://recite?id={id}` | 誦經 |
| `isutra://large?id=diamond` / `isutra://large?id=dizang` | 大部頭分卷目錄 |

## 發現與修習

| URL | 開啟 |
|-----|------|
| `isutra://home` | 首頁 |
| `isutra://daily` | 今日一經 |
| `isutra://random` | 隨機經文 |
| `isutra://favorites` | 收藏 |
| `isutra://famous` | 法語 |
| `isutra://search` / `isutra://search?q={query}` | 搜尋 |
| `isutra://study` | 持誦學堂 |
| `isutra://hunt` | 尋經（別名 `keyword-hunt` / `flyflower`） |
| `isutra://count` | 木魚念誦（`chant` / `muyu` / `counter`） |
| `isutra://copy` / `isutra://copy?id={id}` | 抄經（iOS） |
| `isutra://practice` | 早晚功課 |
| `isutra://mastered` | 已掌握 |
| `isutra://categories` / `isutra://categories?section=` | 分類瀏覽 |
| `isutra://collection?id=` | 合集（如 `prajna`、`forty-two`；亦支援 `name=`） |
| `isutra://theme?id=` | 主題（如 `xingyuan`、`yaoshi`、`platform`） |
| `isutra://last-read` | 最近閱讀 |
| `isutra://reading-history` | 瀏覽記錄 |
| `isutra://notes` | 筆記 |

## 設定與指南

| URL | 開啟 |
|-----|------|
| `isutra://settings` | 設定 |
| `isutra://usage-guide` | 使用說明 |
| `isutra://widget-guide` | 小工具指南 |
| `isutra://shortcuts-guide` | 捷徑指南 |
| `isutra://feature-guide` | 重播功能引導 |
| `isutra://privacy` | 應用內隱私 |
| `isutra://feedback` | 回饋郵件 |
| `isutra://in-app-review` | 應用內 / 商店評價入口 |

## 範例

```
isutra://daily
isutra://passage?id=1
isutra://large?id=diamond
isutra://count
isutra://copy?id=1
isutra://practice
isutra://collection?id=prajna
isutra://theme?id=xingyuan
isutra://study
isutra://hunt
```

可在「捷徑」、主畫面捷徑、小工具或 Safari 中使用。亦可參考應用內 **設定 → 捷徑指南**。

</section>
<section lang="ja" markdown="1">

iSutraは** `isutra://` **ショートカットリンク(URLスキーム)をサポートしています。 コールドスタートとホーム画面のショートカットは、統一されたバッファを介して配信されますので、リンクはオンボーディング後2回開いていません。

## リンク形式


```
isutra://{host}?{params}
```


## Sutrasと著者

| URL | 開く画面 |
|-----|-------|
| `isutra://passage?id={id}` | ストラディテール |
| `isutra://couplet?id={id}` / `isutra://poem?id={id}` | 通路と同じ(互換性) |
| `isutra://author?id={id}` | トランスレーター/作者詳細 |
| `isutra://recite` / `isutra://recite?id={id}` | 誦読フロー |
| `isutra://large?id=diamond` / `isutra://large?id=dizang` | 大型書籍ボリュームカタログ |

## ディスカバリー&プラクティス

| URL | 開く画面 |
|-----|-------|
| `isutra://home` | ホーム |
| `isutra://daily` | 本日の日替わりスートラ |
| `isutra://random` | ランダムな章句 |
| `isutra://favorites` | お気に入り |
| `isutra://famous` | 名句一覧 |
| `isutra://search` / `isutra://search?q={query}` | 検索 |
| `isutra://study` | スタディホール |
| `isutra://hunt` | ハント (寻经); エイリアス `keyword-hunt`/`flyflower` |
| `isutra://count` | 木魚ちゃん (`chant`/`muyu`/`counter`) |
| `isutra://copy` / `isutra://copy?id={id}` | コピーストラ(iOS) |
| `isutra://practice` | 朝/夕方の練習 |
| `isutra://mastered` | マスタード |
| `isutra://categories` / `isutra://categories?section=` | ブラウズ |
| `isutra://collection?id=` | コレクション(例えば、`prajna`、`forty-two`;`name=`) |
| `isutra://theme?id=` | テーマ(例:`xingyuan`、`yaoshi`、`platform`) |
| `isutra://last-read` | 最後に読んだ項目 |
| `isutra://reading-history` | 閲覧履歴 |
| `isutra://notes` | ノート |

## 設定とガイド

| URL | 開く画面 |
|-----|-------|
| `isutra://settings` | 設定 |
| `isutra://usage-guide` | 使い方ガイド |
| `isutra://widget-guide` | ウィジェットガイド |
| `isutra://shortcuts-guide` | ショートカットガイド |
| `isutra://feature-guide` | オンボーディングの再生 |
| `isutra://privacy` | アプリ内プライバシー |
| `isutra://feedback` | フィードバックメール |
| `isutra://in-app-review` | アプリ内／App Store レビュー |

## 例


```
isutra://daily
isutra://passage?id=1
isutra://large?id=diamond
isutra://count
isutra://copy?id=1
isutra://practice
isutra://collection?id=prajna
isutra://theme?id=xingyuan
isutra://study
isutra://hunt
```


これらをショートカットアプリ、ホーム画面のクイックアクション、ウィジェット、またはSafariで使用してください。 アプリ内設定 → ショートカットガイド** も参照してください。

</section>
<section lang="ko" markdown="1">

iSutra 지원 ** `isutra://` ** 단축키 링크 (URL 계획). 콜드 시작 및 홈 화면 단축은 통합 버퍼를 통해 전달되므로 링크가 내장 된 후 두 번 열리지 않습니다.

## 링크 형식


```
isutra://{host}?{params}
```


## Sutras & 저자

| URL | 열리는 화면 |
|-----|-------|
| `isutra://passage?id={id}` | Sutra 세부사항 |
| `isutra://couplet?id={id}` / `isutra://poem?id={id}` | 통행과 같 ( 겸용성) |
| `isutra://author?id={id}` | 번역 / 저자 세부 사항 |
| `isutra://recite` / `isutra://recite?id={id}` | 낭독 흐름 |
| `isutra://large?id=diamond` / `isutra://large?id=dizang` | 대용량 카탈로그 |

## 디스커버리 & 연습

| URL | 열리는 화면 |
|-----|-------|
| `isutra://home` | 홈 |
| `isutra://daily` | 오늘의 매일 Sutra |
| `isutra://random` | 무작위 구절 |
| `isutra://favorites` | 즐겨찾기 |
| `isutra://famous` | 명구 목록 |
| `isutra://search` / `isutra://search?q={query}` | 검색 |
| `isutra://study` | 연구 홀 |
| `isutra://hunt` | 헌트 (fly); aliases `keyword-hunt`/`flyflower` |
| `isutra://count` | 나무 물고기 (`chant`/`muyu`/`counter`) |
| `isutra://copy` / `isutra://copy?id={id}` | 복사-sutra (iOS) |
| `isutra://practice` | 아침 / 저녁 연습 |
| `isutra://mastered` | 인기있는 |
| `isutra://categories` / `isutra://categories?section=` | 둘러보기 |
| `isutra://collection?id=` | 컬렉션 (예: `prajna`, `forty-two`; 또한 `name=`) |
| `isutra://theme?id=` | 테마 (예 : `xingyuan`, `yaoshi`, `platform`) |
| `isutra://last-read` | 마지막으로 읽은 항목 |
| `isutra://reading-history` | 읽기 기록 |
| `isutra://notes` | 메모 |

## 설정 및 가이드

| URL | 열리는 화면 |
|-----|-------|
| `isutra://settings` | 설정 |
| `isutra://usage-guide` | 사용 가이드 |
| `isutra://widget-guide` | 위젯 가이드 |
| `isutra://shortcuts-guide` | 단축어 가이드 |
| `isutra://feature-guide` | 온보딩 다시 보기 |
| `isutra://privacy` | In-app 프라이버시 |
| `isutra://feedback` | 피드백 이메일 |
| `isutra://in-app-review` | 앱 내 / App Store 리뷰 |

## 예시


```
isutra://daily
isutra://passage?id=1
isutra://large?id=diamond
isutra://count
isutra://copy?id=1
isutra://practice
isutra://collection?id=prajna
isutra://theme?id=xingyuan
isutra://study
isutra://hunt
```


Shortcuts 앱, 홈 화면 빠른 행동, 위젯, 또는 사파리에서 이러한 사용. in-app**Settings → 단축키 가이드** 참조.

</section>
<section lang="ru" markdown="1">

iSutra поддерживает ярлыки ** `isutra://` ** (схема URL). Холодный старт и ярлыки домашнего экрана доставляются через единый буфер, поэтому ссылки не открываются дважды после входа.

## Формат ссылки


```
isutra://{host}?{params}
```


## Сутры и авторы

| URL | Открывает |
|-----|-------|
| `isutra://passage?id={id}` | Подробнее о Sutra |
| `isutra://couplet?id={id}` / `isutra://poem?id={id}` | Совместимость (Compatibility) |
| `isutra://author?id={id}` | Переводчик/автор подробно |
| `isutra://recite` / `isutra://recite?id={id}` | Режим чтения вслух |
| `isutra://large?id=diamond` / `isutra://large?id=dizang` | Большой книжный каталог |

## Discovery & Practice

| URL | Открывает |
|-----|-------|
| `isutra://home` | Главная |
| `isutra://daily` | Сегодняшняя ежедневная сутра |
| `isutra://random` | Случайный отрывок |
| `isutra://favorites` | Избранное |
| `isutra://famous` | Знаменитые строки |
| `isutra://search` / `isutra://search?q={query}` | Поиск |
| `isutra://study` | Учебный зал |
| `isutra://hunt` | Охота; псевдонимы «охота за ключевыми словами» / «флайфлауэр» |
| `isutra://count` | Песня деревянной рыбы ('chant' / 'muyu' / 'counter') |
| `isutra://copy` / `isutra://copy?id={id}` | Copy-sutra (iOS) |
| `isutra://practice` | Утренняя или вечерняя практика |
| `isutra://mastered` | мастеринг |
| `isutra://categories` / `isutra://categories?section=` | Обзор |
| `isutra://collection?id=` | Коллекция (например, "праджна", "сорок два"; также "имя =") |
| `isutra://theme?id=` | Тема (например, "xingyuan", "yaoshi", "платформа") |
| `isutra://last-read` | Последнее прочитанное |
| `isutra://reading-history` | История чтения |
| `isutra://notes` | Заметки |

## Настройки и руководства

| URL | Открывает |
|-----|-------|
| `isutra://settings` | Настройки |
| `isutra://usage-guide` | Руководство по использованию |
| `isutra://widget-guide` | Руководство по виджетам |
| `isutra://shortcuts-guide` | Руководство по «Командам» |
| `isutra://feature-guide` | Повторное знакомство |
| `isutra://privacy` | Приватность в приложении |
| `isutra://feedback` | Письмо с отзывом |
| `isutra://in-app-review` | Отзыв в приложении / App Store |

## Примеры


```
isutra://daily
isutra://passage?id=1
isutra://large?id=diamond
isutra://count
isutra://copy?id=1
isutra://practice
isutra://collection?id=prajna
isutra://theme?id=xingyuan
isutra://study
isutra://hunt
```


Используйте их в приложении Shortcuts, быстрых действиях Home Screen, виджетах или Safari. См. также in-app **Settings → Shortcuts Guide**.

</section>
<section lang="th" markdown="1">

isutrra รองรับ... `isutra://` BAR ลิงก์ลัด (URL scheme) การเริ่มหน้าจอหน้าจอเย็นและหน้าจอบ้าน จะถูกส่งไปผ่านระบบบัฟเฟอร์แบบรวม ดังนั้นลิงก์จึงไม่ถูกเปิดสองครั้งหลังจากขึ้นเครื่อง

## รูปแบบลิงก์


```
isutra://{host}?{params}
```


## ผู้เขียน

| URL | เปิด |
|-----|-------|
| `isutra://passage?id={id}` | รายละเอียด |
| `isutra://couplet?id={id}` / `isutra://poem?id={id}` | เช่นเดียวกันกับเนื้อเรื่อง (ความเข้ากันได้) |
| `isutra://author?id={id}` | รายละเอียดผู้แปล/ ผู้เขียน |
| `isutra://recite` / `isutra://recite?id={id}` | โฟลว์การท่อง |
| `isutra://large?id=diamond` / `isutra://large?id=dizang` | แคตตาล็อกระดับเสียงขนาดใหญ่ |

## การท่องเว็บ

| URL | เปิด |
|-----|-------|
| `isutra://home` | หน้าแรก |
| `isutra://daily` | ทุก วัน นี้ |
| `isutra://random` | ข้อความแบบสุ่ม |
| `isutra://favorites` | รายการโปรด |
| `isutra://famous` | บรรทัดขึ้นชื่อ |
| `isutra://search` / `isutra://search?q={query}` | ค้นหา |
| `isutra://study` | หอ ประชุม ศึกษา |
| `isutra://hunt` | ล่า (寻经; สืบค้นเมื่อ 'คีย์เวิร์ด-ฮันต์' / 'ดอกไม้แมลงวัน' |
| `isutra://count` | เสียงร้องของปลาวู้ดเซ่น ('Chant' / 'Muuu' /'ผู้นับ') |
| `isutra://copy` / `isutra://copy?id={id}` | คัดลอก- สุตรา (ไอOS) |
| `isutra://practice` | เช้า / ฝึก ตอน เย็น |
| `isutra://mastered` | สําเร็จการศึกษาแล้ว |
| `isutra://categories` / `isutra://categories?section=` | เรียกดู |
| `isutra://collection?id=` | ชุดสะสม (e.g. `rajna', 'porty-2'; และชื่อด้วย'=') |
| `isutra://theme?id=` | ชุดตกแต่ง (e.g. สืบค้นเมื่อ '%sing yoan', asaishi', `partiform') |
| `isutra://last-read` | รายการที่อ่านล่าสุด |
| `isutra://reading-history` | ประวัติการอ่าน |
| `isutra://notes` | บันทึก |

## การตั้งค่าและคู่มือ

| URL | เปิด |
|-----|-------|
| `isutra://settings` | การตั้งค่า |
| `isutra://usage-guide` | คู่มือการใช้งาน |
| `isutra://widget-guide` | คู่มือวิดเจ็ต |
| `isutra://shortcuts-guide` | คู่มือทางลัด |
| `isutra://feature-guide` | เล่นทัวร์แนะนำอีกครั้ง |
| `isutra://privacy` | ความเป็นส่วนตัว |
| `isutra://feedback` | อีเมลข้อเสนอแนะ |
| `isutra://in-app-review` | รีวิวในแอป / App Store |

## ตัวอย่าง


```
isutra://daily
isutra://passage?id=1
isutra://large?id=diamond
isutra://count
isutra://copy?id=1
isutra://practice
isutra://collection?id=prajna
isutra://theme?id=xingyuan
isutra://study
isutra://hunt
```


ใช้เหล่านี้ในโปรแกรมปุ่มพิมพ์ลัด, การกระทําของหน้าจอส่วนตัวอย่างรวดเร็ว, วิดเจ็ต, หรือ Saveri ดูใน-apps ด้วย

</section>
<section lang="de" markdown="1">

iSutra unterstützt ** `isutra://` ** Shortcut Links (URL-Schema). Kaltstart- und Home Screen-Verknüpfungen werden über einen einheitlichen Puffer geliefert, so dass Links nach dem Onboarding nicht zweimal geöffnet werden.

## Linkformat


```
isutra://{host}?{params}
```


## Sutras & Autoren

| URL | Öffnet |
|-----|-------|
| `isutra://passage?id={id}` | Sutra-Detail |
| `isutra://couplet?id={id}` / `isutra://poem?id={id}` | Wie Passage (Kompatibilität) |
| `isutra://author?id={id}` | Übersetzer / Autorendetail |
| `isutra://recite` / `isutra://recite?id={id}` | Rezitationsablauf |
| `isutra://large?id=diamond` / `isutra://large?id=dizang` | Large-Book Volumenkatalog |

## Entdeckung und Praxis

| URL | Öffnet |
|-----|-------|
| `isutra://home` | Startseite |
| `isutra://daily` | Das heutige tägliche Sutra |
| `isutra://random` | Zufällige Passage |
| `isutra://favorites` | Favoriten |
| `isutra://famous` | Berühmte Zeilen |
| `isutra://search` / `isutra://search?q={query}` | Suche |
| `isutra://study` | Studienhalle |
| `isutra://hunt` | Jagd (寻经); alias `keyword-hunt` / `flyflower` |
| `isutra://count` | Gesang aus Holz (`chant` / `muyu` / `counter`) |
| `isutra://copy` / `isutra://copy?id={id}` | Kopiersutra (iOS) |
| `isutra://practice` | Morgens/Abendpraxis |
| `isutra://mastered` | Beherrscht |
| `isutra://categories` / `isutra://categories?section=` | Durchsuchen |
| `isutra://collection?id=` | Sammlung (z.B. `prajna`, `zweiundvierzig`; auch `name=`) |
| `isutra://theme?id=` | Thema (z.B. `xingyuan`, `yaoshi`, `Plattform`) |
| `isutra://last-read` | Zuletzt gelesen |
| `isutra://reading-history` | Leseverlauf |
| `isutra://notes` | Notizen |

## Einstellungen & Anleitungen

| URL | Öffnet |
|-----|-------|
| `isutra://settings` | Einstellungen |
| `isutra://usage-guide` | Nutzungsanleitung |
| `isutra://widget-guide` | Widget-Anleitung |
| `isutra://shortcuts-guide` | Kurzbefehle-Anleitung |
| `isutra://feature-guide` | Einführung erneut abspielen |
| `isutra://privacy` | In-App Datenschutz |
| `isutra://feedback` | Feedback-E-Mail |
| `isutra://in-app-review` | In-App- / App-Store-Bewertung |

## Beispiele


```
isutra://daily
isutra://passage?id=1
isutra://large?id=diamond
isutra://count
isutra://copy?id=1
isutra://practice
isutra://collection?id=prajna
isutra://theme?id=xingyuan
isutra://study
isutra://hunt
```


Verwenden Sie diese in der Shortcuts-App, den Schnellaktionen für den Startbildschirm, den Widgets oder Safari. Siehe auch In-App **Settings → Shortcuts Guide**.

</section>
<section lang="fr" markdown="1">

iSutra prend en charge les liens raccourcis **      ** (schéma URL). Les raccourcis de démarrage à froid et d'écran d'accueil sont livrés via un tampon unifié de sorte que les liens ne sont pas ouverts deux fois après l'embarquement.

## Format de lien


```
isutra://{host}?{params}
```


## Sutras & auteurs

| URL | Ouvre |
|-----|-------|
| `isutra://passage?id={id}` | Détail Sutra |
| `isutra://couplet?id={id}` / `isutra://poem?id={id}` | Même chose que le passage (compatibilité) |
| `isutra://author?id={id}` | Traducteur / détail de l'auteur |
| `isutra://recite` / `isutra://recite?id={id}` | Flux de récitation |
| `isutra://large?id=diamond` / `isutra://large?id=dizang` | Catalogue grand volume de livres |

## Découverte et pratique

| URL | Ouvre |
|-----|-------|
| `isutra://home` | Accueil |
| `isutra://daily` | Aujourd'hui |
| `isutra://random` | Passage aléatoire |
| `isutra://favorites` | Favoris |
| `isutra://famous` | Vers célèbres |
| `isutra://search` / `isutra://search?q={query}` | Recherche |
| `isutra://study` | Salle d'étude |
| `isutra://hunt` | Chasse; alias « chasse aux mots clés » / « fleurs volantes » |
| `isutra://count` | Chant de poisson en bois (`chant` / `muyu` / `counter`) |
| `isutra://copy` / `isutra://copy?id={id}` | Copie-sutra (iOS) |
| `isutra://practice` | Entraînement matin / soir |
| `isutra://mastered` | Maîtrise |
| `isutra://categories` / `isutra://categories?section=` | Parcourir |
| `isutra://collection?id=` | Collecte (par exemple, "prajna", "quarante-deux"; aussi "nom=") |
| `isutra://theme?id=` | Thème (par exemple "xingyuan", "yaoshi", "plateforme") |
| `isutra://last-read` | Dernière lecture |
| `isutra://reading-history` | Historique de lecture |
| `isutra://notes` | Notes |

## Réglages et guides

| URL | Ouvre |
|-----|-------|
| `isutra://settings` | Réglages |
| `isutra://usage-guide` | Guide d'utilisation |
| `isutra://widget-guide` | Guide des widgets |
| `isutra://shortcuts-guide` | Guide Raccourcis |
| `isutra://feature-guide` | Rejouer l’accueil |
| `isutra://privacy` | Confidentialité dans l'application |
| `isutra://feedback` | E-mail de commentaires |
| `isutra://in-app-review` | Avis in-app / App Store |

## Exemples


```
isutra://daily
isutra://passage?id=1
isutra://large?id=diamond
isutra://count
isutra://copy?id=1
isutra://practice
isutra://collection?id=prajna
isutra://theme?id=xingyuan
isutra://study
isutra://hunt
```


Utilisez-les dans l'application Raccourcis, les actions rapides Home Screen, les widgets ou Safari. Voir aussi dans l'application **Paramètres → Guide des raccourcis**.

</section>
<section lang="tr" markdown="1">

iSutra, ** `isutra://` ** kısayol bağlantıları (URL planı). Soğuk başlangıç ve Ev Ekran kısayolları birleşik bir tampon aracılığıyla teslim edilir, bu yüzden bağlantılar gemiden sonra iki kez açılmaz.

## Bağlantı biçimi


```
isutra://{host}?{params}
```


## Sutras & Yazarlar

| URL | Açar |
|-----|-------|
| `isutra://passage?id={id}` | Sutra detayı |
| `isutra://couplet?id={id}` / `isutra://poem?id={id}` | Aynı geçiş (compatability) |
| `isutra://author?id={id}` | Translator / yazar detay |
| `isutra://recite` / `isutra://recite?id={id}` | Okuma akışı |
| `isutra://large?id=diamond` / `isutra://large?id=dizang` | Büyük Kitap Kataloğu |

## Discovery & practice

| URL | Açar |
|-----|-------|
| `isutra://home` | Ana sayfa |
| `isutra://daily` | Bugünün Günlük Sutra |
| `isutra://random` | Rastgele pasaj |
| `isutra://favorites` | Favoriler |
| `isutra://famous` | Ünlü dizeler |
| `isutra://search` / `isutra://search?q={query}` | Ara |
| `isutra://study` | Çalışma Salonu |
| `isutra://hunt` | Hunt (fly); alias "keyword-hunt" / "flyflower" |
| `isutra://count` | Balık avant ('chant' / "muyu' / "karşılık") |
| `isutra://copy` / `isutra://copy?id={id}` | Copy-sutra (iOS) |
| `isutra://practice` | Sabah / akşam pratik |
| `isutra://mastered` | Mastered |
| `isutra://categories` / `isutra://categories?section=` | Gözat |
| `isutra://collection?id=` | Koleksiyon (e.g. "prajna", "forty-iki"; aynı zamanda "isim=") |
| `isutra://theme?id=` | Tema (e.g. "xingyuan", "yaoshi", " platform") |
| `isutra://last-read` | Son okunan |
| `isutra://reading-history` | Okuma geçmişi |
| `isutra://notes` | Notlar |

## Ayarlar ve kılavuzlar

| URL | Açar |
|-----|-------|
| `isutra://settings` | Ayarlar |
| `isutra://usage-guide` | Kullanım kılavuzu |
| `isutra://widget-guide` | Widget kılavuzu |
| `isutra://shortcuts-guide` | Kısayol kılavuzu |
| `isutra://feature-guide` | Tanıtımı yeniden oynat |
| `isutra://privacy` | In-app gizlilik |
| `isutra://feedback` | Geri bildirim e-postası |
| `isutra://in-app-review` | Uygulama içi / App Store değerlendirme |

## Örnekler


```
isutra://daily
isutra://passage?id=1
isutra://large?id=diamond
isutra://count
isutra://copy?id=1
isutra://practice
isutra://collection?id=prajna
isutra://theme?id=xingyuan
isutra://study
isutra://hunt
```


Bunları kısa kesimlerde kullanın, Home Ekran hızlı eylemleri, widgets veya Safari. Ayrıca bakınız **Settings → Kısayollar Kılavuzu**.

</section>
