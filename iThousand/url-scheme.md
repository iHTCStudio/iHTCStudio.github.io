---
layout: doc
title: iThousand — Shortcut Links
app_id: iThousand
doc_title_en: Shortcut Links
doc_title_zh_cn: 快捷链接说明
doc_title_zh_tw: 快捷連結說明
description: ithousand:// deep links for iThousand — passage, daily, recite, study, hunt, character cards, collections, themes, settings guides, and more.
---

<section lang="en" markdown="1">

iThousand supports **`ithousand://`** shortcut links (URL scheme). Cold start and Home Screen shortcuts are delivered through a unified buffer so links are not opened twice after onboarding.

## Link format

```
ithousand://{host}?{params}
```

## Passages, authors & characters

| URL | Opens |
|-----|-------|
| `ithousand://passage?id={id}` | Passage detail |
| `ithousand://passage?id={id}&open=study` | Passage → Primer Hall |
| `ithousand://passage?id={id}&open=characters` | Passage → character table |
| `ithousand://passage?id={id}&open=note` | Passage → note |
| `ithousand://author?id={id}` | Author detail |
| `ithousand://recite` / `ithousand://recite?id={id}` | Recite flow |
| `ithousand://characters` | Character library |
| `ithousand://character?char=天` | Focus a character card |
| `ithousand://characters?id={id}` | Character card by ID |
| `ithousand://saved-characters` | Saved Characters |
| `ithousand://saved-famous` | Saved famous lines |

## Discovery

| URL | Opens |
|-----|-------|
| `ithousand://home` | Home |
| `ithousand://daily` | Today’s Daily Line |
| `ithousand://random` | Random passage |
| `ithousand://favorites` | Favorites |
| `ithousand://list?id={uuid}` | A personal list (千单) |
| `ithousand://famous` | Famous lines |
| `ithousand://search` / `ithousand://search?q={query}` | Search |
| `ithousand://study` | Primer Hall |
| `ithousand://hunt` | Hunt (寻字); aliases `keyword-hunt` / `flyflower` |
| `ithousand://mastered` | Mastered |
| `ithousand://categories` / `ithousand://categories?section=` | Browse |
| `ithousand://collection?id=qianziwen` | Primer collection (`name=` also supported) |
| `ithousand://theme?id=dizigui-filial` | Theme |
| `ithousand://last-read` | Last read |
| `ithousand://reading-history` | Reading history |
| `ithousand://notes` | Notes |

## Settings & guides

| URL | Opens |
|-----|-------|
| `ithousand://settings` | Settings |
| `ithousand://privacy` | In-app privacy |
| `ithousand://usage-guide` | Usage guide |
| `ithousand://widget-guide` | Widget guide |
| `ithousand://shortcuts-guide` | Shortcuts guide |
| `ithousand://feature-guide` | Replay onboarding |
| `ithousand://feedback` | Feedback email |
| `ithousand://in-app-review` | In-app / Store review entry |

## Examples

```
ithousand://daily
ithousand://passage?id=1
ithousand://passage?id=1&open=characters
ithousand://character?char=天
ithousand://collection?id=qianziwen
ithousand://study
ithousand://hunt
ithousand://saved-characters
```

Use these in the Shortcuts app, Home Screen quick actions, widgets, or Safari. Prefer stable `id` parameters when available. See also in-app **Settings → Shortcuts Guide**.

</section>
<section lang="zh-CN" markdown="1">

爱千字文支持 **`ithousand://`** 快捷链接（URL Scheme）。冷启动与主屏快捷经统一缓冲投递，避免引导后重复打开。

## 链接格式

```
ithousand://{host}?{params}
```

## 篇目、作者与字卡

| URL | 打开 |
|-----|------|
| `ithousand://passage?id={id}` | 篇目详情 |
| `ithousand://passage?id={id}&open=study` | 篇目 → 蒙学堂 |
| `ithousand://passage?id={id}&open=characters` | 篇目 → 本篇字表 |
| `ithousand://passage?id={id}&open=note` | 篇目 → 笔记 |
| `ithousand://author?id={id}` | 作者详情 |
| `ithousand://recite` / `ithousand://recite?id={id}` | 诵读 |
| `ithousand://characters` | 字库 |
| `ithousand://character?char=天` | 指定字卡 |
| `ithousand://saved-characters` | 生字本 |
| `ithousand://saved-famous` | 已收藏名句 |

## 发现与练习

| URL | 打开 |
|-----|------|
| `ithousand://home` | 首页 |
| `ithousand://daily` | 今日每日一句 |
| `ithousand://random` | 随机篇目 |
| `ithousand://favorites` | 收藏 |
| `ithousand://list?id={uuid}` | 指定千单 |
| `ithousand://famous` | 名句 |
| `ithousand://search` / `ithousand://search?q={关键词}` | 搜索 |
| `ithousand://study` | 蒙学堂 |
| `ithousand://hunt` | 寻字 |
| `ithousand://mastered` | 已掌握 |
| `ithousand://categories` | 分类浏览 |
| `ithousand://collection?id=qianziwen` | 千字文等合集 |
| `ithousand://theme?id=dizigui-filial` | 主题 |
| `ithousand://last-read` | 上次阅读 |
| `ithousand://reading-history` | 阅读历史 |
| `ithousand://notes` | 笔记 |

## 设置与引导

| URL | 打开 |
|-----|------|
| `ithousand://settings` | 设置 |
| `ithousand://privacy` | 应用内隐私政策 |
| `ithousand://usage-guide` | 使用说明 |
| `ithousand://widget-guide` | 小组件指南 |
| `ithousand://shortcuts-guide` | 快捷指南 |
| `ithousand://feature-guide` | 重播欢迎引导 |
| `ithousand://feedback` | 反馈邮件 |
| `ithousand://in-app-review` | 应用内评价入口 |

## 示例

```
ithousand://daily
ithousand://passage?id=1
ithousand://character?char=天
ithousand://study
ithousand://hunt
ithousand://saved-characters
```

可在快捷指令、主屏快捷、小组件或 Safari 中使用。建议优先使用稳定的 `id` 参数。详见应用内 **设置 → 快捷指南**。

</section>
<section lang="zh-TW" markdown="1">

愛千字文支援 **`ithousand://`** 快捷連結（URL Scheme）。冷啟動與主畫面捷徑經統一緩衝投遞，避免引導後重複開啟。

## 連結格式

```
ithousand://{host}?{params}
```

## 篇目、作者與字卡

| URL | 開啟 |
|-----|------|
| `ithousand://passage?id={id}` | 篇目詳情 |
| `ithousand://recite` / `ithousand://recite?id={id}` | 誦讀 |
| `ithousand://characters` | 字庫 |
| `ithousand://character?char=天` | 指定字卡 |
| `ithousand://saved-characters` | 生字本 |

## 發現與練習

| URL | 開啟 |
|-----|------|
| `ithousand://daily` | 今日每日一句 |
| `ithousand://study` | 蒙學堂 |
| `ithousand://hunt` | 尋字 |
| `ithousand://collection?id=qianziwen` | 千字文等合集 |
| `ithousand://theme?id=dizigui-filial` | 主題 |

## 設定與引導

`ithousand://settings` · `ithousand://privacy` · `ithousand://usage-guide` · `ithousand://widget-guide` · `ithousand://shortcuts-guide` · `ithousand://feature-guide` · `ithousand://feedback`

詳見應用內 **設定 → 捷徑指南**。

</section>
<section lang="ja" markdown="1">

iThousandは** `ithousand://` **ショートカットリンク(URLスキーム)をサポートしています。 コールドスタートとホーム画面のショートカットは、統一されたバッファを介して配信されますので、リンクはオンボーディング後2回開いていません。

## リンク形式


```
ithousand://{host}?{params}
```


## パス、著者、キャラクター

| URL | 開く画面 |
|-----|-------|
| `ithousand://passage?id={id}` | 章句の詳細 |
| `ithousand://passage?id={id}&open=study` | パッセージ → プライマーホール |
| `ithousand://passage?id={id}&open=characters` | パッセージ→キャラクターテーブル |
| `ithousand://passage?id={id}&open=note` | パッセージ → ノート |
| `ithousand://author?id={id}` | 作者の詳細 |
| `ithousand://recite` / `ithousand://recite?id={id}` | 誦読フロー |
| `ithousand://characters` | キャラクターライブラリ |
| `ithousand://character?char=天` | キャラクターカードをフォーカス |
| `ithousand://characters?id={id}` | IDによるキャラクターカード |
| `ithousand://saved-characters` | 保存されたキャラクター |
| `ithousand://saved-famous` | 有名なラインを保存 |

## 発見

| URL | 開く画面 |
|-----|-------|
| `ithousand://home` | ホーム |
| `ithousand://daily` | 今日の毎日ライン |
| `ithousand://random` | ランダムな章句 |
| `ithousand://favorites` | お気に入り |
| `ithousand://list?id={uuid}` | 個人的なリスト (千人) |
| `ithousand://famous` | 名句一覧 |
| `ithousand://search` / `ithousand://search?q={query}` | 検索 |
| `ithousand://study` | プライマーホール |
| `ithousand://hunt` | Hunt(漢字)。aliases`keyword-hunt`/`flyflower` |
| `ithousand://mastered` | マスタード |
| `ithousand://categories` / `ithousand://categories?section=` | ブラウズ |
| `ithousand://collection?id=qianziwen` | プライマーコレクション(`name=` もサポート) |
| `ithousand://theme?id=dizigui-filial` | テーマ: |
| `ithousand://last-read` | 最後に読んだ項目 |
| `ithousand://reading-history` | 閲覧履歴 |
| `ithousand://notes` | ノート |

## 設定とガイド

| URL | 開く画面 |
|-----|-------|
| `ithousand://settings` | 設定 |
| `ithousand://privacy` | アプリ内プライバシー |
| `ithousand://usage-guide` | 使い方ガイド |
| `ithousand://widget-guide` | ウィジェットガイド |
| `ithousand://shortcuts-guide` | ショートカットガイド |
| `ithousand://feature-guide` | オンボーディングの再生 |
| `ithousand://feedback` | フィードバックメール |
| `ithousand://in-app-review` | アプリ内／App Store レビュー |

## 例


```
ithousand://daily
ithousand://passage?id=1
ithousand://passage?id=1&open=characters
ithousand://character?char=天
ithousand://collection?id=qianziwen
ithousand://study
ithousand://hunt
ithousand://saved-characters
```


これらをショートカットアプリ、ホーム画面のクイックアクション、ウィジェット、またはSafariで使用してください。 利用できる場合の優先順位の安定した `ithousand://` 変数。 アプリ内設定 → ショートカットガイド** も参照してください。

</section>
<section lang="ko" markdown="1">

iThousand support** `ithousand://` ** 단축키 링크 (URL 계획). 콜드 시작 및 홈 화면 단축은 통합 버퍼를 통해 전달되므로 링크가 내장 된 후 두 번 열리지 않습니다.

## 링크 형식


```
ithousand://{host}?{params}
```


## Passages, 저자 및 문자

| URL | 열리는 화면 |
|-----|-------|
| `ithousand://passage?id={id}` | 구절 상세 |
| `ithousand://passage?id={id}&open=study` | Passage → 프라임 홀 |
| `ithousand://passage?id={id}&open=characters` | Passage → 문자 테이블 |
| `ithousand://passage?id={id}&open=note` | Passage → 참고 |
| `ithousand://author?id={id}` | 작가 상세 |
| `ithousand://recite` / `ithousand://recite?id={id}` | 낭독 흐름 |
| `ithousand://characters` | 캐릭터 라이브러리 |
| `ithousand://character?char=天` | 캐릭터 카드 초점 |
| `ithousand://characters?id={id}` | ID로 문자 카드 |
| `ithousand://saved-characters` | 저장된 문자 |
| `ithousand://saved-famous` | 저장된 유명한 선 |

## 탐색

| URL | 열리는 화면 |
|-----|-------|
| `ithousand://home` | 홈 |
| `ithousand://daily` | 오늘의 일일 라인 |
| `ithousand://random` | 무작위 구절 |
| `ithousand://favorites` | 즐겨찾기 |
| `ithousand://list?id={uuid}` | 개인 목록 ()) |
| `ithousand://famous` | 명구 목록 |
| `ithousand://search` / `ithousand://search?q={query}` | 검색 |
| `ithousand://study` | 프라임 홀 |
| `ithousand://hunt` | 헌트 (fly); aliases `keyword-hunt`/`flyflower` |
| `ithousand://mastered` | 인기있는 |
| `ithousand://categories` / `ithousand://categories?section=` | 둘러보기 |
| `ithousand://collection?id=qianziwen` | Primer 컬렉션 (`name=`도 지원) |
| `ithousand://theme?id=dizigui-filial` | 이름 * |
| `ithousand://last-read` | 마지막으로 읽은 항목 |
| `ithousand://reading-history` | 읽기 기록 |
| `ithousand://notes` | 메모 |

## 설정 및 가이드

| URL | 열리는 화면 |
|-----|-------|
| `ithousand://settings` | 설정 |
| `ithousand://privacy` | In-app 프라이버시 |
| `ithousand://usage-guide` | 사용 가이드 |
| `ithousand://widget-guide` | 위젯 가이드 |
| `ithousand://shortcuts-guide` | 단축어 가이드 |
| `ithousand://feature-guide` | 온보딩 다시 보기 |
| `ithousand://feedback` | 피드백 이메일 |
| `ithousand://in-app-review` | 앱 내 / App Store 리뷰 |

## 예시


```
ithousand://daily
ithousand://passage?id=1
ithousand://passage?id=1&open=characters
ithousand://character?char=天
ithousand://collection?id=qianziwen
ithousand://study
ithousand://hunt
ithousand://saved-characters
```


Shortcuts 앱, 홈 화면 빠른 행동, 위젯, 또는 사파리에서 이러한 사용. Prefer stable `ithousand://` 사용할 때 매개 변수. in-app**Settings → 단축키 가이드** 참조.

</section>
<section lang="ru" markdown="1">

iThousand поддерживает ярлыки ** `ithousand://` ** (схема URL). Холодный старт и ярлыки домашнего экрана доставляются через единый буфер, поэтому ссылки не открываются дважды после входа.

## Формат ссылки


```
ithousand://{host}?{params}
```


## Проходы, авторы и персонажи

| URL | Открывает |
|-----|-------|
| `ithousand://passage?id={id}` | Страница отрывка |
| `ithousand://passage?id={id}&open=study` | Оригинальное название: Primer Hall |
| `ithousand://passage?id={id}&open=characters` | Прохождение: Character Table |
| `ithousand://passage?id={id}&open=note` | Прохождение Note |
| `ithousand://author?id={id}` | Страница автора |
| `ithousand://recite` / `ithousand://recite?id={id}` | Режим чтения вслух |
| `ithousand://characters` | Библиотека персонажей |
| `ithousand://character?char=天` | Сосредоточьте карту персонажа |
| `ithousand://characters?id={id}` | Карточка персонажа ID |
| `ithousand://saved-characters` | Спасенные персонажи |
| `ithousand://saved-famous` | Сохранились знаменитые линии |

## Обзор

| URL | Открывает |
|-----|-------|
| `ithousand://home` | Главная |
| `ithousand://daily` | Ежедневная линия сегодня |
| `ithousand://random` | Случайный отрывок |
| `ithousand://favorites` | Избранное |
| `ithousand://list?id={uuid}` | Личный список ()) |
| `ithousand://famous` | Знаменитые строки |
| `ithousand://search` / `ithousand://search?q={query}` | Поиск |
| `ithousand://study` | Праймер Холл |
| `ithousand://hunt` | Охота (`); псевдонимы «охота за ключевыми словами» / «флайфлауэр» |
| `ithousand://mastered` | мастеринг |
| `ithousand://categories` / `ithousand://categories?section=` | Обзор |
| `ithousand://collection?id=qianziwen` | Primer Collection (также поддерживается) |
| `ithousand://theme?id=dizigui-filial` | Тема |
| `ithousand://last-read` | Последнее прочитанное |
| `ithousand://reading-history` | История чтения |
| `ithousand://notes` | Заметки |

## Настройки и руководства

| URL | Открывает |
|-----|-------|
| `ithousand://settings` | Настройки |
| `ithousand://privacy` | Приватность в приложении |
| `ithousand://usage-guide` | Руководство по использованию |
| `ithousand://widget-guide` | Руководство по виджетам |
| `ithousand://shortcuts-guide` | Руководство по «Командам» |
| `ithousand://feature-guide` | Повторное знакомство |
| `ithousand://feedback` | Письмо с отзывом |
| `ithousand://in-app-review` | Отзыв в приложении / App Store |

## Примеры


```
ithousand://daily
ithousand://passage?id=1
ithousand://passage?id=1&open=characters
ithousand://character?char=天
ithousand://collection?id=qianziwen
ithousand://study
ithousand://hunt
ithousand://saved-characters
```


Используйте их в приложении Shortcuts, быстрых действиях Home Screen, виджетах или Safari. Предпочитаю стабильные параметры `ithousand://` при наличии. См. также in-app **Settings → Shortcuts Guide**.

</section>
<section lang="th" markdown="1">

igusand รองรับ~ `ithousand://` BAR ลิงก์ลัด (RUL scheme) การเริ่มหน้าจอหน้าจอเย็นและหน้าจอบ้าน จะถูกส่งไปผ่านระบบบัฟเฟอร์แบบรวม ดังนั้นลิงก์จึงไม่ถูกเปิดสองครั้งหลังจากขึ้นเครื่อง

## รูปแบบลิงก์


```
ithousand://{host}?{params}
```


## Passage, ผู้เขียนและอักขระ

| URL | เปิด |
|-----|-------|
| `ithousand://passage?id={id}` | รายละเอียดข้อความ |
| `ithousand://passage?id={id}&open=study` | Passage → ไพรเซอร์ฮอลล์ |
| `ithousand://passage?id={id}&open=characters` | Passage → ตารางอักขระ |
| `ithousand://passage?id={id}&open=note` | Passage log |
| `ithousand://author?id={id}` | รายละเอียดผู้แต่ง |
| `ithousand://recite` / `ithousand://recite?id={id}` | โฟลว์การท่อง |
| `ithousand://characters` | ไลบรารีอักขระ |
| `ithousand://character?char=天` | โฟกัสไพ่อักขระ |
| `ithousand://characters?id={id}` | บัตรอักขระโดยหมายเลข |
| `ithousand://saved-characters` | บันทึกอักขระ |
| `ithousand://saved-famous` | บันทึกบรรทัดที่มีชื่อเสียง |

## ค้นพบ

| URL | เปิด |
|-----|-------|
| `ithousand://home` | หน้าแรก |
| `ithousand://daily` | ข้อ คัมภีร์ ประจํา วัน |
| `ithousand://random` | ข้อความแบบสุ่ม |
| `ithousand://favorites` | รายการโปรด |
| `ithousand://list?id={uuid}` | รายชื่อส่วนตัว (千单) |
| `ithousand://famous` | บรรทัดขึ้นชื่อ |
| `ithousand://search` / `ithousand://search?q={query}` | ค้นหา |
| `ithousand://study` | ห้องโถงหลัก |
| `ithousand://hunt` | ล่า (寻字; สืบค้นเมื่อ 'คีย์เวิร์ด-ฮันต์' / 'ดอกไม้แมลงวัน' |
| `ithousand://mastered` | สําเร็จการศึกษาแล้ว |
| `ithousand://categories` / `ithousand://categories?section=` | เรียกดู |
| `ithousand://collection?id=qianziwen` | คอลเลกชันของไพรม์เซอร์ (ชื่อ=' รองรับด้วย) |
| `ithousand://theme?id=dizigui-filial` | ชุดตกแต่ง |
| `ithousand://last-read` | รายการที่อ่านล่าสุด |
| `ithousand://reading-history` | ประวัติการอ่าน |
| `ithousand://notes` | บันทึก |

## การตั้งค่าและคู่มือ

| URL | เปิด |
|-----|-------|
| `ithousand://settings` | การตั้งค่า |
| `ithousand://privacy` | ความเป็นส่วนตัว |
| `ithousand://usage-guide` | คู่มือการใช้งาน |
| `ithousand://widget-guide` | คู่มือวิดเจ็ต |
| `ithousand://shortcuts-guide` | คู่มือทางลัด |
| `ithousand://feature-guide` | เล่นทัวร์แนะนำอีกครั้ง |
| `ithousand://feedback` | อีเมลข้อเสนอแนะ |
| `ithousand://in-app-review` | รีวิวในแอป / App Store |

## ตัวอย่าง


```
ithousand://daily
ithousand://passage?id=1
ithousand://passage?id=1&open=characters
ithousand://character?char=天
ithousand://collection?id=qianziwen
ithousand://study
ithousand://hunt
ithousand://saved-characters
```


ใช้เหล่านี้ในโปรแกรมปุ่มพิมพ์ลัด, การกระทําของหน้าจอส่วนตัวอย่างรวดเร็ว, วิดเจ็ต, หรือ Saveri ค่าคงที่ `ithousand://` พารามิเตอร์เมื่อใช้ได้ ดูใน-apps ด้วย

</section>
<section lang="de" markdown="1">

iThousand unterstützt ** `ithousand://` ** Shortcut Links (URL-Schema). Kaltstart- und Home Screen-Verknüpfungen werden über einen einheitlichen Puffer geliefert, so dass Links nach dem Onboarding nicht zweimal geöffnet werden.

## Linkformat


```
ithousand://{host}?{params}
```


## Passagen, Autoren & Charaktere

| URL | Öffnet |
|-----|-------|
| `ithousand://passage?id={id}` | Passagen-Detail |
| `ithousand://passage?id={id}&open=study` | Passage: Primer Hall |
| `ithousand://passage?id={id}&open=characters` | Passage → Charaktertabelle |
| `ithousand://passage?id={id}&open=note` | Passage → Note |
| `ithousand://author?id={id}` | Autorendetail |
| `ithousand://recite` / `ithousand://recite?id={id}` | Rezitationsablauf |
| `ithousand://characters` | Charakterbibliothek |
| `ithousand://character?char=天` | Fokussieren einer Charakterkarte |
| `ithousand://characters?id={id}` | Zeichenkarte nach ID |
| `ithousand://saved-characters` | Gespeicherte Charaktere |
| `ithousand://saved-famous` | Berühmte Linien gerettet |

## Entdecken

| URL | Öffnet |
|-----|-------|
| `ithousand://home` | Startseite |
| `ithousand://daily` | Die heutige tägliche Linie |
| `ithousand://random` | Zufällige Passage |
| `ithousand://favorites` | Favoriten |
| `ithousand://list?id={uuid}` | Eine persönliche Liste (千单) |
| `ithousand://famous` | Berühmte Zeilen |
| `ithousand://search` / `ithousand://search?q={query}` | Suche |
| `ithousand://study` | Primer Hall |
| `ithousand://hunt` | Jagd (寻�); alias `keyword-hunt` / `flyflower` |
| `ithousand://mastered` | Beherrscht |
| `ithousand://categories` / `ithousand://categories?section=` | Durchsuchen |
| `ithousand://collection?id=qianziwen` | Primer Collection (`name=` wird ebenfalls unterstützt) |
| `ithousand://theme?id=dizigui-filial` | Thema |
| `ithousand://last-read` | Zuletzt gelesen |
| `ithousand://reading-history` | Leseverlauf |
| `ithousand://notes` | Notizen |

## Einstellungen & Anleitungen

| URL | Öffnet |
|-----|-------|
| `ithousand://settings` | Einstellungen |
| `ithousand://privacy` | In-App Datenschutz |
| `ithousand://usage-guide` | Nutzungsanleitung |
| `ithousand://widget-guide` | Widget-Anleitung |
| `ithousand://shortcuts-guide` | Kurzbefehle-Anleitung |
| `ithousand://feature-guide` | Einführung erneut abspielen |
| `ithousand://feedback` | Feedback-E-Mail |
| `ithousand://in-app-review` | In-App- / App-Store-Bewertung |

## Beispiele


```
ithousand://daily
ithousand://passage?id=1
ithousand://passage?id=1&open=characters
ithousand://character?char=天
ithousand://collection?id=qianziwen
ithousand://study
ithousand://hunt
ithousand://saved-characters
```


Verwenden Sie diese in der Shortcuts-App, den Schnellaktionen für den Startbildschirm, den Widgets oder Safari. Bevorzugt stabile `ithousand://` -Parameter, wenn verfügbar. Siehe auch In-App **Settings → Shortcuts Guide**.

</section>
<section lang="fr" markdown="1">

iMille supporte les liens de raccourci ** `ithousand://` ** (schéma URL). Les raccourcis de démarrage à froid et d'écran d'accueil sont livrés via un tampon unifié de sorte que les liens ne sont pas ouverts deux fois après l'embarquement.

## Format de lien


```
ithousand://{host}?{params}
```


## Passages, auteurs et personnages

| URL | Ouvre |
|-----|-------|
| `ithousand://passage?id={id}` | Détail du passage |
| `ithousand://passage?id={id}&open=study` | Passage → Salle des Primers |
| `ithousand://passage?id={id}&open=characters` | Passage → table de caractères |
| `ithousand://passage?id={id}&open=note` | Passage → note |
| `ithousand://author?id={id}` | Détail de l’auteur |
| `ithousand://recite` / `ithousand://recite?id={id}` | Flux de récitation |
| `ithousand://characters` | Bibliothèque de caractères |
| `ithousand://character?char=天` | Concentrez une carte de caractères |
| `ithousand://characters?id={id}` | Carte de caractère par ID |
| `ithousand://saved-characters` | Personnages sauvegardés |
| `ithousand://saved-famous` | Sauvé des lignes célèbres |

## Découverte

| URL | Ouvre |
|-----|-------|
| `ithousand://home` | Accueil |
| `ithousand://daily` | Aujourd'hui Ligne quotidienne |
| `ithousand://random` | Passage aléatoire |
| `ithousand://favorites` | Favoris |
| `ithousand://list?id={uuid}` | Une liste personnelle |
| `ithousand://famous` | Vers célèbres |
| `ithousand://search` / `ithousand://search?q={query}` | Recherche |
| `ithousand://study` | Salle d'introduction |
| `ithousand://hunt` | Chasse () ; alias « chasse aux mots clés » / « fleurs volantes » |
| `ithousand://mastered` | Maîtrise |
| `ithousand://categories` / `ithousand://categories?section=` | Parcourir |
| `ithousand://collection?id=qianziwen` | Primer collection (`nom=` également supporté) |
| `ithousand://theme?id=dizigui-filial` | Thème |
| `ithousand://last-read` | Dernière lecture |
| `ithousand://reading-history` | Historique de lecture |
| `ithousand://notes` | Notes |

## Réglages et guides

| URL | Ouvre |
|-----|-------|
| `ithousand://settings` | Réglages |
| `ithousand://privacy` | Confidentialité dans l'application |
| `ithousand://usage-guide` | Guide d'utilisation |
| `ithousand://widget-guide` | Guide des widgets |
| `ithousand://shortcuts-guide` | Guide Raccourcis |
| `ithousand://feature-guide` | Rejouer l’accueil |
| `ithousand://feedback` | E-mail de commentaires |
| `ithousand://in-app-review` | Avis in-app / App Store |

## Exemples


```
ithousand://daily
ithousand://passage?id=1
ithousand://passage?id=1&open=characters
ithousand://character?char=天
ithousand://collection?id=qianziwen
ithousand://study
ithousand://hunt
ithousand://saved-characters
```


Utilisez-les dans l'application Raccourcis, les actions rapides Home Screen, les widgets ou Safari. Préférez les paramètres stables `ithousand://` lorsque disponibles. Voir aussi dans l'application **Paramètres → Guide des raccourcis**.

</section>
<section lang="tr" markdown="1">

iThousand ** `ithousand://` ** kısayol bağlantıları (URL planı). Soğuk başlangıç ve Ev Ekran kısayolları birleşik bir tampon aracılığıyla teslim edilir, bu yüzden bağlantılar gemiden sonra iki kez açılmaz.

## Bağlantı biçimi


```
ithousand://{host}?{params}
```


## Pasajlar, yazarlar ve karakterler

| URL | Açar |
|-----|-------|
| `ithousand://passage?id={id}` | Pasaj ayrıntısı |
| `ithousand://passage?id={id}&open=study` | Passage → Primer Hall |
| `ithousand://passage?id={id}&open=characters` | Passage → karakter masası |
| `ithousand://passage?id={id}&open=note` | Pasaj → not |
| `ithousand://author?id={id}` | Yazar ayrıntısı |
| `ithousand://recite` / `ithousand://recite?id={id}` | Okuma akışı |
| `ithousand://characters` | Karakter kütüphanesi |
| `ithousand://character?char=天` | Bir karakter kartı |
| `ithousand://characters?id={id}` | Karakter kartı ID |
| `ithousand://saved-characters` | Saved Characters |
| `ithousand://saved-famous` | Kaydeten ünlü hatları |

## Keşfet

| URL | Açar |
|-----|-------|
| `ithousand://home` | Ana sayfa |
| `ithousand://daily` | Bugünün Günlük Hattı |
| `ithousand://random` | Rastgele pasaj |
| `ithousand://favorites` | Favoriler |
| `ithousand://list?id={uuid}` | Kişisel bir liste (千单) |
| `ithousand://famous` | Ünlü dizeler |
| `ithousand://search` / `ithousand://search?q={query}` | Ara |
| `ithousand://study` | Primer Hall |
| `ithousand://hunt` | Hunt (fly); alias "keyword-hunt" / "flyflower" |
| `ithousand://mastered` | Mastered |
| `ithousand://categories` / `ithousand://categories?section=` | Gözat |
| `ithousand://collection?id=qianziwen` | Primer koleksiyonu (isim='un da desteklenen) |
| `ithousand://theme?id=dizigui-filial` | Tema |
| `ithousand://last-read` | Son okunan |
| `ithousand://reading-history` | Okuma geçmişi |
| `ithousand://notes` | Notlar |

## Ayarlar ve kılavuzlar

| URL | Açar |
|-----|-------|
| `ithousand://settings` | Ayarlar |
| `ithousand://privacy` | In-app gizlilik |
| `ithousand://usage-guide` | Kullanım kılavuzu |
| `ithousand://widget-guide` | Widget kılavuzu |
| `ithousand://shortcuts-guide` | Kısayol kılavuzu |
| `ithousand://feature-guide` | Tanıtımı yeniden oynat |
| `ithousand://feedback` | Geri bildirim e-postası |
| `ithousand://in-app-review` | Uygulama içi / App Store değerlendirme |

## Örnekler


```
ithousand://daily
ithousand://passage?id=1
ithousand://passage?id=1&open=characters
ithousand://character?char=天
ithousand://collection?id=qianziwen
ithousand://study
ithousand://hunt
ithousand://saved-characters
```


Bunları kısa kesimlerde kullanın, Home Ekran hızlı eylemleri, widgets veya Safari. Mevcut olduğunda istikrarlı `ithousand://` parametreleri tercih edin. Ayrıca bakınız **Settings → Kısayollar Kılavuzu**.

</section>
