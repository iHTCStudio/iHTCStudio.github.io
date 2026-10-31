---
layout: doc
title: iThree — Shortcut Links
app_id: iThree
doc_title_en: Shortcut Links
doc_title_zh_cn: 快捷链接说明
doc_title_zh_tw: 快捷連結說明
description: ithree:// deep links for iThree — passage, daily, recite, study, hunt, stories, books, dynasties, settings guides, and more.
---

<section lang="en" markdown="1">

iThree supports **`ithree://`** shortcut links (URL scheme). Cold start and Home Screen shortcuts are delivered through a unified buffer so links are not opened twice after onboarding.

## Link format

```
ithree://{host}?{params}
```

## Passages & discovery

| URL | Opens |
|-----|-------|
| `ithree://home` | Home |
| `ithree://daily` | Today’s Daily Line |
| `ithree://random` | Random passage |
| `ithree://passage?id={id}` | Passage detail |
| `ithree://recite` / `ithree://recite?id={id}` | Recite flow |
| `ithree://favorites` | Favorites |
| `ithree://famous` | Famous lines |
| `ithree://search` / `ithree://search?q={query}` | Search |
| `ithree://study` | Study classroom |
| `ithree://quiz` | Today’s quiz |
| `ithree://hunt` | Hunt (寻句) |
| `ithree://mastered` | Mastered |
| `ithree://categories` | Browse |
| `ithree://chapter?id={id}` | Chapter |
| `ithree://stories` / `ithree://story?id={id}` | Stories / story detail |
| `ithree://books` / `ithree://book?id={id}` | Classic indexes / book |
| `ithree://dynasties` / `ithree://dynasty?id={id}` | Dynasties / dynasty |
| `ithree://collection?id=` / `?name=` | Collection (or books if empty) |
| `ithree://last-read` | Last read |
| `ithree://reading-history` | Reading history |
| `ithree://notes` | Notes |

> Note: `ithree://author?id=` is a compatibility alias and opens the matching **chapter**.

## Settings & guides

| URL | Opens |
|-----|-------|
| `ithree://settings` | Settings |
| `ithree://usage-guide` | Usage guide |
| `ithree://widget-guide` | Widget guide |
| `ithree://shortcuts-guide` | Shortcuts guide |
| `ithree://feature-guide` | Replay onboarding |
| `ithree://feedback` | Feedback email |
| `ithree://in-app-review` | In-app / Store review entry |
| `ithree://privacy` | In-app privacy |

## Examples

```
ithree://daily
ithree://passage?id=1
ithree://recite?id=1
ithree://study
ithree://hunt
ithree://quiz
ithree://stories
ithree://search?q=人之初
```

Use these in the Shortcuts app, Home Screen quick actions, widgets, Control Center, or Safari. See also in-app **Settings → Shortcuts Guide**.

</section>
<section lang="zh-CN" markdown="1">

爱三字经支持 **`ithree://`** 快捷链接（URL Scheme）。冷启动与主屏快捷经统一缓冲投递，避免引导后重复打开。

## 链接格式

```
ithree://{host}?{params}
```

## 段落与发现

| URL | 打开 |
|-----|------|
| `ithree://home` | 首页 |
| `ithree://daily` | 每日一句 |
| `ithree://random` | 随机 |
| `ithree://passage?id={id}` | 段落详情 |
| `ithree://recite` / `ithree://recite?id={id}` | 诵读 |
| `ithree://favorites` | 收藏 |
| `ithree://famous` | 名句 |
| `ithree://search` / `ithree://search?q={query}` | 搜索 |
| `ithree://study` | 蒙学学堂 |
| `ithree://quiz` | 今日测验 |
| `ithree://hunt` | 寻句 |
| `ithree://mastered` | 已掌握 |
| `ithree://categories` | 分类 |
| `ithree://chapter?id={id}` | 章节 |
| `ithree://stories` / `ithree://story?id={id}` | 典故 / 典故详情 |
| `ithree://books` / `ithree://book?id={id}` | 典籍 / 典籍详情 |
| `ithree://dynasties` / `ithree://dynasty?id={id}` | 朝代 / 朝代详情 |
| `ithree://collection?id=` / `?name=` | 合集（空参则进典籍） |
| `ithree://last-read` | 上次阅读 |
| `ithree://reading-history` | 浏览记录 |
| `ithree://notes` | 笔记 |

> 说明：`ithree://author?id=` 为兼容别名，会打开对应**章节**。

## 设置与教程

| URL | 打开 |
|-----|------|
| `ithree://settings` | 设置 |
| `ithree://usage-guide` | 使用说明 |
| `ithree://widget-guide` | 小组件指南 |
| `ithree://shortcuts-guide` | 快捷指南 |
| `ithree://feature-guide` | 重播引导 |
| `ithree://feedback` | 反馈邮件 |
| `ithree://in-app-review` | 应用内 / 商店评价入口 |
| `ithree://privacy` | 应用内隐私说明 |

## 示例

```
ithree://daily
ithree://passage?id=1
ithree://recite?id=1
ithree://study
ithree://hunt
ithree://quiz
ithree://stories
ithree://search?q=人之初
```

可在「快捷指令」、主屏快捷、小组件、控制中心或 Safari 中使用。也可查看应用内 **设置 → 快捷指南**。

</section>
<section lang="zh-TW" markdown="1">

愛三字經支援 **`ithree://`** 快捷連結（URL Scheme）。冷啟動與主畫面捷徑經統一緩衝投遞，避免引導後重複開啟。

## 連結格式

```
ithree://{host}?{params}
```

## 段落與發現

| URL | 開啟 |
|-----|------|
| `ithree://home` | 首頁 |
| `ithree://daily` | 每日一句 |
| `ithree://random` | 隨機 |
| `ithree://passage?id={id}` | 段落詳情 |
| `ithree://recite` / `ithree://recite?id={id}` | 誦讀 |
| `ithree://favorites` | 收藏 |
| `ithree://famous` | 名句 |
| `ithree://search` / `ithree://search?q={query}` | 搜尋 |
| `ithree://study` | 蒙學學堂 |
| `ithree://quiz` | 今日測驗 |
| `ithree://hunt` | 尋句 |
| `ithree://mastered` | 已掌握 |
| `ithree://categories` | 分類 |
| `ithree://chapter?id={id}` | 章節 |
| `ithree://stories` / `ithree://story?id={id}` | 典故 / 典故詳情 |
| `ithree://books` / `ithree://book?id={id}` | 典籍 / 典籍詳情 |
| `ithree://dynasties` / `ithree://dynasty?id={id}` | 朝代 / 朝代詳情 |
| `ithree://collection?id=` / `?name=` | 合集（空參則進典籍） |
| `ithree://last-read` | 上次閱讀 |
| `ithree://reading-history` | 瀏覽記錄 |
| `ithree://notes` | 筆記 |

> 說明：`ithree://author?id=` 為相容別名，會開啟對應**章節**。

## 設定與教學

| URL | 開啟 |
|-----|------|
| `ithree://settings` | 設定 |
| `ithree://usage-guide` | 使用說明 |
| `ithree://widget-guide` | 小工具指南 |
| `ithree://shortcuts-guide` | 捷徑指南 |
| `ithree://feature-guide` | 重播引導 |
| `ithree://feedback` | 回饋郵件 |
| `ithree://in-app-review` | App 內 / 商店評價入口 |
| `ithree://privacy` | App 內隱私說明 |

## 範例

```
ithree://daily
ithree://passage?id=1
ithree://recite?id=1
ithree://study
ithree://hunt
ithree://quiz
ithree://stories
ithree://search?q=人之初
```

可在「捷徑」、主畫面捷徑、小工具、控制中心或 Safari 中使用。也可查看應用內 **設定 → 捷徑指南**。

</section>
<section lang="ja" markdown="1">

iThreeは** `ithree://` **ショートカットリンク(URLスキーム)をサポートしています。 コールドスタートとホーム画面のショートカットは、統一されたバッファを介して配信されますので、リンクはオンボーディング後2回開いていません。

## リンク形式


```
ithree://{host}?{params}
```


## パッセージと発見

| URL | 開く画面 |
|-----|-------|
| `ithree://home` | ホーム |
| `ithree://daily` | 今日の毎日ライン |
| `ithree://random` | ランダムな章句 |
| `ithree://passage?id={id}` | 章句の詳細 |
| `ithree://recite` / `ithree://recite?id={id}` | 誦読フロー |
| `ithree://favorites` | お気に入り |
| `ithree://famous` | 名句一覧 |
| `ithree://search` / `ithree://search?q={query}` | 検索 |
| `ithree://study` | 学習教室 |
| `ithree://quiz` | 今日のクイズ |
| `ithree://hunt` | 寻 (句) |
| `ithree://mastered` | マスタード |
| `ithree://categories` | ブラウズ |
| `ithree://chapter?id={id}` | トピックス |
| `ithree://stories` / `ithree://story?id={id}` | ストーリー/ストーリー詳細 |
| `ithree://books` / `ithree://book?id={id}` | クラシックインデックス/書籍 |
| `ithree://dynasties` / `ithree://dynasty?id={id}` | ダイナスティ / ダイナスティ |
| `ithree://collection?id=` / `?name=` | コレクション(または空の書籍) |
| `ithree://last-read` | 最後に読んだ項目 |
| `ithree://reading-history` | 閲覧履歴 |
| `ithree://notes` | ノート |

> Note: `ithree://` は互換性のあるエイリアスで、マッチング **chapter** を開きます。

## 設定とガイド

| URL | 開く画面 |
|-----|-------|
| `ithree://settings` | 設定 |
| `ithree://usage-guide` | 使い方ガイド |
| `ithree://widget-guide` | ウィジェットガイド |
| `ithree://shortcuts-guide` | ショートカットガイド |
| `ithree://feature-guide` | オンボーディングの再生 |
| `ithree://feedback` | フィードバックメール |
| `ithree://in-app-review` | アプリ内／App Store レビュー |
| `ithree://privacy` | アプリ内プライバシー |

## 例


```
ithree://daily
ithree://passage?id=1
ithree://recite?id=1
ithree://study
ithree://hunt
ithree://quiz
ithree://stories
ithree://search?q=人之初
```


これらをショートカットアプリ、ホーム画面のクイックアクション、ウィジェット、コントロールセンター、またはSafariで使用してください。 アプリ内設定 → ショートカットガイド** も参照してください。

</section>
<section lang="ko" markdown="1">

iThree 지원 ** `ithree://` ** 단축키 링크 (URL 계획). 콜드 시작 및 홈 화면 단축은 통합 버퍼를 통해 전달되므로 링크가 내장 된 후 두 번 열리지 않습니다.

## 링크 형식


```
ithree://{host}?{params}
```


## 책임 및 발견

| URL | 열리는 화면 |
|-----|-------|
| `ithree://home` | 홈 |
| `ithree://daily` | 오늘의 일일 라인 |
| `ithree://random` | 무작위 구절 |
| `ithree://passage?id={id}` | 구절 상세 |
| `ithree://recite` / `ithree://recite?id={id}` | 낭독 흐름 |
| `ithree://favorites` | 즐겨찾기 |
| `ithree://famous` | 명구 목록 |
| `ithree://search` / `ithree://search?q={query}` | 검색 |
| `ithree://study` | 학습 교실 |
| `ithree://quiz` | 오늘의 퀴즈 |
| `ithree://hunt` | Hunt ()) |
| `ithree://mastered` | 인기있는 |
| `ithree://categories` | 둘러보기 |
| `ithree://chapter?id={id}` | 이름 * |
| `ithree://stories` / `ithree://story?id={id}` | 스토리 / 스토리 |
| `ithree://books` / `ithree://book?id={id}` | 클래식 인덱스 / 책 |
| `ithree://dynasties` / `ithree://dynasty?id={id}` | 다이나믹스 / dynasty |
| `ithree://collection?id=` / `?name=` | 수집(비어 있는 경우 책) |
| `ithree://last-read` | 마지막으로 읽은 항목 |
| `ithree://reading-history` | 읽기 기록 |
| `ithree://notes` | 메모 |

> 참고 : `ithree://` 는 호환성 별명이며 일치 ** 차터**를 엽니다.

## 설정 및 가이드

| URL | 열리는 화면 |
|-----|-------|
| `ithree://settings` | 설정 |
| `ithree://usage-guide` | 사용 가이드 |
| `ithree://widget-guide` | 위젯 가이드 |
| `ithree://shortcuts-guide` | 단축어 가이드 |
| `ithree://feature-guide` | 온보딩 다시 보기 |
| `ithree://feedback` | 피드백 이메일 |
| `ithree://in-app-review` | 앱 내 / App Store 리뷰 |
| `ithree://privacy` | In-app 프라이버시 |

## 예시


```
ithree://daily
ithree://passage?id=1
ithree://recite?id=1
ithree://study
ithree://hunt
ithree://quiz
ithree://stories
ithree://search?q=人之初
```


Shortcuts 앱에서 이러한 사용, 홈 화면 빠른 행동, 위젯, 제어 센터, 또는 사파리. in-app**Settings → 단축키 가이드** 참조.

</section>
<section lang="ru" markdown="1">

iThree поддерживает ярлыки ** `ithree://` ** (схема URL). Холодный старт и ярлыки домашнего экрана доставляются через единый буфер, поэтому ссылки не открываются дважды после входа.

## Формат ссылки


```
ithree://{host}?{params}
```


## Проходы и открытия

| URL | Открывает |
|-----|-------|
| `ithree://home` | Главная |
| `ithree://daily` | Ежедневная линия сегодня |
| `ithree://random` | Случайный отрывок |
| `ithree://passage?id={id}` | Страница отрывка |
| `ithree://recite` / `ithree://recite?id={id}` | Режим чтения вслух |
| `ithree://favorites` | Избранное |
| `ithree://famous` | Знаменитые строки |
| `ithree://search` / `ithree://search?q={query}` | Поиск |
| `ithree://study` | Учебный класс |
| `ithree://quiz` | Сегодняшняя викторина |
| `ithree://hunt` | Охота ()) |
| `ithree://mastered` | мастеринг |
| `ithree://categories` | Обзор |
| `ithree://chapter?id={id}` | Глава |
| `ithree://stories` / `ithree://story?id={id}` | Рассказы / Story Detail |
| `ithree://books` / `ithree://book?id={id}` | Классические индексы / книга |
| `ithree://dynasties` / `ithree://dynasty?id={id}` | Династии / Династия |
| `ithree://collection?id=` / `?name=` | Коллекция (или книги, если они пусты) |
| `ithree://last-read` | Последнее прочитанное |
| `ithree://reading-history` | История чтения |
| `ithree://notes` | Заметки |

> Примечание: `ithree://` является псевдонимом совместимости и открывает соответствующую **главу**.

## Настройки и руководства

| URL | Открывает |
|-----|-------|
| `ithree://settings` | Настройки |
| `ithree://usage-guide` | Руководство по использованию |
| `ithree://widget-guide` | Руководство по виджетам |
| `ithree://shortcuts-guide` | Руководство по «Командам» |
| `ithree://feature-guide` | Повторное знакомство |
| `ithree://feedback` | Письмо с отзывом |
| `ithree://in-app-review` | Отзыв в приложении / App Store |
| `ithree://privacy` | Приватность в приложении |

## Примеры


```
ithree://daily
ithree://passage?id=1
ithree://recite?id=1
ithree://study
ithree://hunt
ithree://quiz
ithree://stories
ithree://search?q=人之初
```


Используйте их в приложении Shortcuts, быстрых действиях Home Screen, виджетах, Центре управления или Safari. См. также in-app **Settings → Shortcuts Guide**.

</section>
<section lang="th" markdown="1">

IRC รองรับ... `ithree://` BAR ลิงก์ลัด (URL scheme) การเริ่มหน้าจอหน้าจอเย็นและหน้าจอบ้าน จะถูกส่งไปผ่านระบบบัฟเฟอร์แบบรวม ดังนั้นลิงก์จึงไม่ถูกเปิดสองครั้งหลังจากขึ้นเครื่อง

## รูปแบบลิงก์


```
ithree://{host}?{params}
```


## การติดตามและการค้นพบ

| URL | เปิด |
|-----|-------|
| `ithree://home` | หน้าแรก |
| `ithree://daily` | ข้อ คัมภีร์ ประจํา วัน |
| `ithree://random` | ข้อความแบบสุ่ม |
| `ithree://passage?id={id}` | รายละเอียดข้อความ |
| `ithree://recite` / `ithree://recite?id={id}` | โฟลว์การท่อง |
| `ithree://favorites` | รายการโปรด |
| `ithree://famous` | บรรทัดขึ้นชื่อ |
| `ithree://search` / `ithree://search?q={query}` | ค้นหา |
| `ithree://study` | ห้องเรียนเรียน |
| `ithree://quiz` | คํา ถาม ใน ปัจจุบัน |
| `ithree://hunt` | ล่า (寻句) |
| `ithree://mastered` | สําเร็จการศึกษาแล้ว |
| `ithree://categories` | เรียกดู |
| `ithree://chapter?id={id}` | บท |
| `ithree://stories` / `ithree://story?id={id}` | เรื่องเล่า / รายละเอียด |
| `ithree://books` / `ithree://book?id={id}` | ดัชนีคลาสสิค / หนังสือ |
| `ithree://dynasties` / `ithree://dynasty?id={id}` | ความ สําคัญ ของ ราชวงศ์ / ราชวงศ์ |
| `ithree://collection?id=` / `?name=` | ชุดสะสม (หรือหนังสือว่าง) |
| `ithree://last-read` | รายการที่อ่านล่าสุด |
| `ithree://reading-history` | ประวัติการอ่าน |
| `ithree://notes` | บันทึก |

> ควรทราบ: `ithree://` BAR เป็นนามแฝงที่เข้ากันได้และเปิดให้ตรงกัน~

## การตั้งค่าและคู่มือ

| URL | เปิด |
|-----|-------|
| `ithree://settings` | การตั้งค่า |
| `ithree://usage-guide` | คู่มือการใช้งาน |
| `ithree://widget-guide` | คู่มือวิดเจ็ต |
| `ithree://shortcuts-guide` | คู่มือทางลัด |
| `ithree://feature-guide` | เล่นทัวร์แนะนำอีกครั้ง |
| `ithree://feedback` | อีเมลข้อเสนอแนะ |
| `ithree://in-app-review` | รีวิวในแอป / App Store |
| `ithree://privacy` | ความเป็นส่วนตัว |

## ตัวอย่าง


```
ithree://daily
ithree://passage?id=1
ithree://recite?id=1
ithree://study
ithree://hunt
ithree://quiz
ithree://stories
ithree://search?q=人之初
```


ใช้เหล่านี้ในโปรแกรมปุ่มพิมพ์ลัด, การกระทําของหน้าจอส่วนตัวอย่างรวดเร็ว, วิดเจ็ต, ศูนย์ควบคุม, หรือซาฟารี ดูใน-apps ด้วย

</section>
<section lang="de" markdown="1">

iThree unterstützt ** `ithree://` ** Shortcut Links (URL-Schema). Kaltstart- und Home Screen-Verknüpfungen werden über einen einheitlichen Puffer geliefert, so dass Links nach dem Onboarding nicht zweimal geöffnet werden.

## Linkformat


```
ithree://{host}?{params}
```


## Passages & Discovery

| URL | Öffnet |
|-----|-------|
| `ithree://home` | Startseite |
| `ithree://daily` | Die heutige tägliche Linie |
| `ithree://random` | Zufällige Passage |
| `ithree://passage?id={id}` | Passagen-Detail |
| `ithree://recite` / `ithree://recite?id={id}` | Rezitationsablauf |
| `ithree://favorites` | Favoriten |
| `ithree://famous` | Berühmte Zeilen |
| `ithree://search` / `ithree://search?q={query}` | Suche |
| `ithree://study` | Studienraum |
| `ithree://quiz` | Das heutige Quiz |
| `ithree://hunt` | Jagd (寻句) |
| `ithree://mastered` | Beherrscht |
| `ithree://categories` | Durchsuchen |
| `ithree://chapter?id={id}` | Kapitel |
| `ithree://stories` / `ithree://story?id={id}` | Geschichten / Story Detail |
| `ithree://books` / `ithree://book?id={id}` | Klassische Indizes / Buch |
| `ithree://dynasties` / `ithree://dynasty?id={id}` | Dynastien/Dynastie |
| `ithree://collection?id=` / `?name=` | Sammlung (oder Bücher, wenn leer) |
| `ithree://last-read` | Zuletzt gelesen |
| `ithree://reading-history` | Leseverlauf |
| `ithree://notes` | Notizen |

> Hinweis: `ithree://` ist ein Kompatibilitätsalias und öffnet das passende **Kapitel**.

## Einstellungen & Anleitungen

| URL | Öffnet |
|-----|-------|
| `ithree://settings` | Einstellungen |
| `ithree://usage-guide` | Nutzungsanleitung |
| `ithree://widget-guide` | Widget-Anleitung |
| `ithree://shortcuts-guide` | Kurzbefehle-Anleitung |
| `ithree://feature-guide` | Einführung erneut abspielen |
| `ithree://feedback` | Feedback-E-Mail |
| `ithree://in-app-review` | In-App- / App-Store-Bewertung |
| `ithree://privacy` | In-App Datenschutz |

## Beispiele


```
ithree://daily
ithree://passage?id=1
ithree://recite?id=1
ithree://study
ithree://hunt
ithree://quiz
ithree://stories
ithree://search?q=人之初
```


Verwenden Sie diese in der Shortcuts-App, den Schnellaktionen für den Startbildschirm, den Widgets, dem Control Center oder Safari. Siehe auch In-App **Settings → Shortcuts Guide**.

</section>
<section lang="fr" markdown="1">

iTrois prend en charge les liens de raccourci ** `ithree://` ** (schéma URL). Les raccourcis de démarrage à froid et d'écran d'accueil sont livrés via un tampon unifié de sorte que les liens ne sont pas ouverts deux fois après l'embarquement.

## Format de lien


```
ithree://{host}?{params}
```


## Passages & découverte

| URL | Ouvre |
|-----|-------|
| `ithree://home` | Accueil |
| `ithree://daily` | Aujourd'hui Ligne quotidienne |
| `ithree://random` | Passage aléatoire |
| `ithree://passage?id={id}` | Détail du passage |
| `ithree://recite` / `ithree://recite?id={id}` | Flux de récitation |
| `ithree://favorites` | Favoris |
| `ithree://famous` | Vers célèbres |
| `ithree://search` / `ithree://search?q={query}` | Recherche |
| `ithree://study` | Cours |
| `ithree://quiz` | Quizz d'aujourd'hui |
| `ithree://hunt` | Chasse |
| `ithree://mastered` | Maîtrise |
| `ithree://categories` | Parcourir |
| `ithree://chapter?id={id}` | Chapitre |
| `ithree://stories` / `ithree://story?id={id}` | Histoires / détails de l'histoire |
| `ithree://books` / `ithree://book?id={id}` | Index classique / livre |
| `ithree://dynasties` / `ithree://dynasty?id={id}` | Dynasties / dynastie |
| `ithree://collection?id=` / `?name=` | Collection (ou livres si vide) |
| `ithree://last-read` | Dernière lecture |
| `ithree://reading-history` | Historique de lecture |
| `ithree://notes` | Notes |

> Note : `ithree://` est un alias de compatibilité et ouvre la correspondance **chapitre**.

## Réglages et guides

| URL | Ouvre |
|-----|-------|
| `ithree://settings` | Réglages |
| `ithree://usage-guide` | Guide d'utilisation |
| `ithree://widget-guide` | Guide des widgets |
| `ithree://shortcuts-guide` | Guide Raccourcis |
| `ithree://feature-guide` | Rejouer l’accueil |
| `ithree://feedback` | E-mail de commentaires |
| `ithree://in-app-review` | Avis in-app / App Store |
| `ithree://privacy` | Confidentialité dans l'application |

## Exemples


```
ithree://daily
ithree://passage?id=1
ithree://recite?id=1
ithree://study
ithree://hunt
ithree://quiz
ithree://stories
ithree://search?q=人之初
```


Utilisez-les dans l'application Raccourcis, Actions rapides Home Screen, Widgets, Control Center ou Safari. Voir aussi dans l'application **Paramètres → Guide des raccourcis**.

</section>
<section lang="tr" markdown="1">

I Three support ** `ithree://` ** kısayol bağlantıları (URL planı). Soğuk başlangıç ve Ev Ekran kısayolları birleşik bir tampon aracılığıyla teslim edilir, bu yüzden bağlantılar gemiden sonra iki kez açılmaz.

## Bağlantı biçimi


```
ithree://{host}?{params}
```


## Pasajlar ve keşif

| URL | Açar |
|-----|-------|
| `ithree://home` | Ana sayfa |
| `ithree://daily` | Bugünün Günlük Hattı |
| `ithree://random` | Rastgele pasaj |
| `ithree://passage?id={id}` | Pasaj ayrıntısı |
| `ithree://recite` / `ithree://recite?id={id}` | Okuma akışı |
| `ithree://favorites` | Favoriler |
| `ithree://famous` | Ünlü dizeler |
| `ithree://search` / `ithree://search?q={query}` | Ara |
| `ithree://study` | Çalışma sınıfı |
| `ithree://quiz` | Bugünün sınav |
| `ithree://hunt` | Hunt ( Hunt) |
| `ithree://mastered` | Mastered |
| `ithree://categories` | Gözat |
| `ithree://chapter?id={id}` | Bölüm Bölüm Bölüm |
| `ithree://stories` / `ithree://story?id={id}` | Hikayeler / hikaye detay |
| `ithree://books` / `ithree://book?id={id}` | Klasik indeksler / kitap |
| `ithree://dynasties` / `ithree://dynasty?id={id}` | Dynas / Hanedan |
| `ithree://collection?id=` / `?name=` | Koleksiyon (veya kitaplar boşsa) |
| `ithree://last-read` | Son okunan |
| `ithree://reading-history` | Okuma geçmişi |
| `ithree://notes` | Notlar |

> Not: `ithree://` bir uyumluluk alias ve eşleşen **chapter** açıyor.

## Ayarlar ve kılavuzlar

| URL | Açar |
|-----|-------|
| `ithree://settings` | Ayarlar |
| `ithree://usage-guide` | Kullanım kılavuzu |
| `ithree://widget-guide` | Widget kılavuzu |
| `ithree://shortcuts-guide` | Kısayol kılavuzu |
| `ithree://feature-guide` | Tanıtımı yeniden oynat |
| `ithree://feedback` | Geri bildirim e-postası |
| `ithree://in-app-review` | Uygulama içi / App Store değerlendirme |
| `ithree://privacy` | In-app gizlilik |

## Örnekler


```
ithree://daily
ithree://passage?id=1
ithree://recite?id=1
ithree://study
ithree://hunt
ithree://quiz
ithree://stories
ithree://search?q=人之初
```


Bunları kısa kesimlerde kullanın, Home Ekran hızlı eylemleri, widgets, Control Center veya Safari. Ayrıca bakınız **Settings → Kısayollar Kılavuzu**.

</section>
