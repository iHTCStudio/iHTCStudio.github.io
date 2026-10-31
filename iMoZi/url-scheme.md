---
layout: doc
title: iMoZi — Shortcut Links
app_id: iMoZi
doc_title_en: Shortcut Links
doc_title_zh_cn: 快捷链接说明
doc_title_zh_tw: 快捷連結說明
description: imozi:// deep links for iMoZi — passage, daily, recite, study, hunt, settings guides, and more.
---

<section lang="en" markdown="1">

iMoZi supports **`imozi://`** shortcut links (URL scheme). Cold start and Home Screen shortcuts are delivered through a unified buffer so links are not opened twice after onboarding.

## Link format

```
imozi://{host}?{params}
```

## Passages & authors

| URL | Opens |
|-----|-------|
| `imozi://passage?id={id}` | Passage detail |
| `imozi://saying?id={id}` / `imozi://couplet?id={id}` / `imozi://poem?id={id}` | Same as passage (compatibility) |
| `imozi://passage?id={id}&card=1` | Passage detail and card sheet |
| `imozi://card?id={id}` / `imozi://share-card?id={id}` | 墨 cards |
| `imozi://author?id={id}` | Author detail |
| `imozi://recite` / `imozi://recite?id={id}` | Recite flow |

## Discovery & practice

| URL | Opens |
|-----|-------|
| `imozi://home` | Home |
| `imozi://daily` | Today’s Mo |
| `imozi://random` | Random passage |
| `imozi://favorites` | Favorites |
| `imozi://famous` | Famous lines |
| `imozi://search` / `imozi://search?q={query}` | Search |
| `imozi://study` / `imozi://study?id={id}` | Mohism Study |
| `imozi://hunt` | Sentence Hunt (`keyword-hunt` / `flyflower`) |
| `imozi://handwriting` | Handwriting search (`handwrite`; iOS) |
| `imozi://mastered` | Mastered (`progress`) |
| `imozi://categories` / `imozi://categories?section=` | Browse |
| `imozi://collection?id=` | Collection / book |
| `imozi://corpus` | All passages (`all`) |
| `imozi://last-read` | Last read |
| `imozi://reading-history` | Reading history |
| `imozi://notes` | Notes |
| `imozi://ask` | Ask Mozi |
| `imozi://fables` / `imozi://allegories` / `imozi://concepts` | Specialty shelves when available |

## Settings & guides

| URL | Opens |
|-----|-------|
| `imozi://settings` | Settings |
| `imozi://usage-guide` | Usage guide |
| `imozi://widget-guide` | Widget guide |
| `imozi://shortcuts-guide` | Shortcuts guide |
| `imozi://feature-guide` | Replay onboarding |
| `imozi://feedback` | Feedback email |
| `imozi://in-app-review` | In-app / Store review entry |

## Examples

```
imozi://daily
imozi://passage?id=1
imozi://ask
imozi://study
imozi://hunt
```

</section>
<section lang="zh-CN" markdown="1">

爱墨子 支持 **`imozi://`** 快捷链接（URL Scheme）。冷启动与主屏幕快捷方式经统一缓冲投递，避免引导后重复打开。

## 链接格式

```
imozi://{host}?{params}
```

## 篇目与作者

| URL | 打开 |
|-----|------|
| `imozi://passage?id={id}` | 篇目详情 |
| `imozi://saying?id={id}` / `imozi://couplet?id={id}` / `imozi://poem?id={id}` | 同 passage（兼容） |
| `imozi://passage?id={id}&card=1` | 篇目详情并打开分享卡 |
| `imozi://card?id={id}` / `imozi://share-card?id={id}` | 墨卡 |
| `imozi://author?id={id}` | 作者详情 |
| `imozi://recite` / `imozi://recite?id={id}` | 诵读 |

## 发现与练习

| URL | 打开 |
|-----|------|
| `imozi://home` | 首页 |
| `imozi://daily` | 今日一墨 |
| `imozi://random` | 随机一篇 |
| `imozi://favorites` | 收藏 |
| `imozi://famous` | 名句 |
| `imozi://search` / `imozi://search?q={query}` | 搜索 |
| `imozi://study` / `imozi://study?id={id}` | 墨学学堂 |
| `imozi://hunt` | 寻句（`keyword-hunt` / `flyflower`） |
| `imozi://handwriting` | 手写寻句（`handwrite`；iOS） |
| `imozi://mastered` | 已掌握（`progress`） |
| `imozi://categories` / `imozi://categories?section=` | 浏览 |
| `imozi://collection?id=` | 合集／分册 |
| `imozi://corpus` | 全部篇目（`all`） |
| `imozi://last-read` | 上次阅读 |
| `imozi://reading-history` | 阅读历史 |
| `imozi://notes` | 笔记 |
| `imozi://ask` | 问墨子 |
| `imozi://fables` / `imozi://allegories` / `imozi://concepts` | 专属书架（如有） |

## 设置与指南

| URL | 打开 |
|-----|------|
| `imozi://settings` | 设置 |
| `imozi://usage-guide` | 使用说明 |
| `imozi://widget-guide` | 小组件说明 |
| `imozi://shortcuts-guide` | 快捷指令说明 |
| `imozi://feature-guide` | 重看功能导览 |
| `imozi://feedback` | 反馈邮件 |
| `imozi://in-app-review` | 应用内／商店评价入口 |

## 示例

```
imozi://daily
imozi://passage?id=1
imozi://ask
imozi://study
imozi://hunt
```

</section>
<section lang="zh-TW" markdown="1">

愛墨子 支援 **`imozi://`** 快捷連結（URL Scheme）。冷啟動與主畫面捷徑經統一緩衝投遞，避免引導後重複打開。

## 連結格式

```
imozi://{host}?{params}
```

## 篇目與作者

| URL | 打開 |
|-----|------|
| `imozi://passage?id={id}` | 篇目詳情 |
| `imozi://saying?id={id}` / `imozi://couplet?id={id}` / `imozi://poem?id={id}` | 同 passage（相容） |
| `imozi://passage?id={id}&card=1` | 篇目詳情並打開分享卡 |
| `imozi://card?id={id}` / `imozi://share-card?id={id}` | 墨卡 |
| `imozi://author?id={id}` | 作者詳情 |
| `imozi://recite` / `imozi://recite?id={id}` | 誦讀 |

## 探索與練習

| URL | 打開 |
|-----|------|
| `imozi://home` | 首頁 |
| `imozi://daily` | 今日一墨 |
| `imozi://random` | 隨機一篇 |
| `imozi://favorites` | 收藏 |
| `imozi://famous` | 名句 |
| `imozi://search` / `imozi://search?q={query}` | 搜尋 |
| `imozi://study` / `imozi://study?id={id}` | 墨學學堂 |
| `imozi://hunt` | 尋句（`keyword-hunt` / `flyflower`） |
| `imozi://handwriting` | 手寫尋句（`handwrite`；iOS） |
| `imozi://mastered` | 已掌握（`progress`） |
| `imozi://categories` / `imozi://categories?section=` | 瀏覽 |
| `imozi://collection?id=` | 合集／分冊 |
| `imozi://corpus` | 全部篇目（`all`） |
| `imozi://last-read` | 上次閱讀 |
| `imozi://reading-history` | 閱讀歷史 |
| `imozi://notes` | 筆記 |
| `imozi://ask` | 問墨子 |
| `imozi://fables` / `imozi://allegories` / `imozi://concepts` | 專屬書架（如有） |

## 設定與指南

| URL | 打開 |
|-----|------|
| `imozi://settings` | 設定 |
| `imozi://usage-guide` | 使用說明 |
| `imozi://widget-guide` | 小工具說明 |
| `imozi://shortcuts-guide` | 捷徑說明 |
| `imozi://feature-guide` | 重看功能導覽 |
| `imozi://feedback` | 回饋郵件 |
| `imozi://in-app-review` | 應用內／商店評價入口 |

## 範例

```
imozi://daily
imozi://passage?id=1
imozi://ask
imozi://study
imozi://hunt
```

</section>
<section lang="ja" markdown="1">

iMoZiは** `imozi://` **ショートカットリンク(URLスキーム)をサポートしています。 コールドスタートとホーム画面のショートカットは、統一されたバッファを介して配信されますので、リンクはオンボーディング後2回開いていません。

## リンク形式


```
imozi://{host}?{params}
```


## パスポートと著者

| URL | 開く画面 |
|-----|-------|
| `imozi://passage?id={id}` | 章句の詳細 |
| `imozi://saying?id={id}` / `imozi://couplet?id={id}` / `imozi://poem?id={id}` | 通路と同じ(互換性) |
| `imozi://passage?id={id}&card=1` | 通路の細部およびカード シート |
| `imozi://card?id={id}` / `imozi://share-card?id={id}` | 墨カード |
| `imozi://author?id={id}` | 作者の詳細 |
| `imozi://recite` / `imozi://recite?id={id}` | 誦読フロー |

## ディスカバリー&プラクティス

| URL | 開く画面 |
|-----|-------|
| `imozi://home` | ホーム |
| `imozi://daily` | 今日のMo |
| `imozi://random` | ランダムな章句 |
| `imozi://favorites` | お気に入り |
| `imozi://famous` | 名句一覧 |
| `imozi://search` / `imozi://search?q={query}` | 検索 |
| `imozi://study` / `imozi://study?id={id}` | モヒズム研究 |
| `imozi://hunt` | センテンスハント (`keyword-hunt`/`flyflower`) |
| `imozi://handwriting` | 手書き検索 (`handwrite`; iOS) |
| `imozi://mastered` | マスタード (`progress`) |
| `imozi://categories` / `imozi://categories?section=` | ブラウズ |
| `imozi://collection?id=` | コレクション/書籍 |
| `imozi://corpus` | すべての通路 (`all`) |
| `imozi://last-read` | 最後に読んだ項目 |
| `imozi://reading-history` | 閲覧履歴 |
| `imozi://notes` | ノート |
| `imozi://ask` | Moziを依頼する |
| `imozi://fables` / `imozi://allegories` / `imozi://concepts` | 利用できる場合の特別な棚 |

## 設定とガイド

| URL | 開く画面 |
|-----|-------|
| `imozi://settings` | 設定 |
| `imozi://usage-guide` | 使い方ガイド |
| `imozi://widget-guide` | ウィジェットガイド |
| `imozi://shortcuts-guide` | ショートカットガイド |
| `imozi://feature-guide` | オンボーディングの再生 |
| `imozi://feedback` | フィードバックメール |
| `imozi://in-app-review` | アプリ内／App Store レビュー |

## 例


```
imozi://daily
imozi://passage?id=1
imozi://ask
imozi://study
imozi://hunt
```

</section>
<section lang="ko" markdown="1">

iMoZi는 ** `imozi://` ** 단축키 링크 (URL 계획)를 지원합니다. 콜드 시작 및 홈 화면 단축은 통합 버퍼를 통해 전달되므로 링크가 내장 된 후 두 번 열리지 않습니다.

## 링크 형식


```
imozi://{host}?{params}
```


## 책임 & 저자

| URL | 열리는 화면 |
|-----|-------|
| `imozi://passage?id={id}` | 구절 상세 |
| `imozi://saying?id={id}` / `imozi://couplet?id={id}` / `imozi://poem?id={id}` | 통행과 같 ( 겸용성) |
| `imozi://passage?id={id}&card=1` | 통행 세부사항과 카드 장 |
| `imozi://card?id={id}` / `imozi://share-card?id={id}` | 이름 * |
| `imozi://author?id={id}` | 작가 상세 |
| `imozi://recite` / `imozi://recite?id={id}` | 낭독 흐름 |

## 디스커버리 & 연습

| URL | 열리는 화면 |
|-----|-------|
| `imozi://home` | 홈 |
| `imozi://daily` | 오늘의 모 |
| `imozi://random` | 무작위 구절 |
| `imozi://favorites` | 즐겨찾기 |
| `imozi://famous` | 명구 목록 |
| `imozi://search` / `imozi://search?q={query}` | 검색 |
| `imozi://study` / `imozi://study?id={id}` | Mohism 연구 |
| `imozi://hunt` | 문장 사냥 (`keyword-hunt`/`flyflower`) |
| `imozi://handwriting` | Handwriting search (`handwrite`; iOS) |
| `imozi://mastered` | 마스터 (`progress`) |
| `imozi://categories` / `imozi://categories?section=` | 둘러보기 |
| `imozi://collection?id=` | 컬렉션 / 책 |
| `imozi://corpus` | 모든 통행 (`all`) |
| `imozi://last-read` | 마지막으로 읽은 항목 |
| `imozi://reading-history` | 읽기 기록 |
| `imozi://notes` | 메모 |
| `imozi://ask` | Mozi 소개 |
| `imozi://fables` / `imozi://allegories` / `imozi://concepts` | 사용할 때 특수 선반 |

## 설정 및 가이드

| URL | 열리는 화면 |
|-----|-------|
| `imozi://settings` | 설정 |
| `imozi://usage-guide` | 사용 가이드 |
| `imozi://widget-guide` | 위젯 가이드 |
| `imozi://shortcuts-guide` | 단축어 가이드 |
| `imozi://feature-guide` | 온보딩 다시 보기 |
| `imozi://feedback` | 피드백 이메일 |
| `imozi://in-app-review` | 앱 내 / App Store 리뷰 |

## 예시


```
imozi://daily
imozi://passage?id=1
imozi://ask
imozi://study
imozi://hunt
```

</section>
<section lang="ru" markdown="1">

iMoZi поддерживает ярлыки ** `imozi://` ** (схема URL). Холодный старт и ярлыки домашнего экрана доставляются через единый буфер, поэтому ссылки не открываются дважды после входа.

## Формат ссылки


```
imozi://{host}?{params}
```


## Проходы и авторы

| URL | Открывает |
|-----|-------|
| `imozi://passage?id={id}` | Страница отрывка |
| `imozi://saying?id={id}` / `imozi://couplet?id={id}` / `imozi://poem?id={id}` | Совместимость (Compatibility) |
| `imozi://passage?id={id}&card=1` | Детали проезда и карточный лист |
| `imozi://card?id={id}` / `imozi://share-card?id={id}` | карты |
| `imozi://author?id={id}` | Страница автора |
| `imozi://recite` / `imozi://recite?id={id}` | Режим чтения вслух |

## Discovery & Practice

| URL | Открывает |
|-----|-------|
| `imozi://home` | Главная |
| `imozi://daily` | Сегодняшний Мо |
| `imozi://random` | Случайный отрывок |
| `imozi://favorites` | Избранное |
| `imozi://famous` | Знаменитые строки |
| `imozi://search` / `imozi://search?q={query}` | Поиск |
| `imozi://study` / `imozi://study?id={id}` | Исследование мохизма |
| `imozi://hunt` | Охота за ключевыми словами / Flyflower |
| `imozi://handwriting` | Поиск почерка («handwrite»; iOS) |
| `imozi://mastered` | Мастеринг («Прогресс») |
| `imozi://categories` / `imozi://categories?section=` | Обзор |
| `imozi://collection?id=` | Коллекция / книга |
| `imozi://corpus` | Все пассажи («All») |
| `imozi://last-read` | Последнее прочитанное |
| `imozi://reading-history` | История чтения |
| `imozi://notes` | Заметки |
| `imozi://ask` | Спроси у Моцзы. |
| `imozi://fables` / `imozi://allegories` / `imozi://concepts` | Специальные полки, когда они доступны |

## Настройки и руководства

| URL | Открывает |
|-----|-------|
| `imozi://settings` | Настройки |
| `imozi://usage-guide` | Руководство по использованию |
| `imozi://widget-guide` | Руководство по виджетам |
| `imozi://shortcuts-guide` | Руководство по «Командам» |
| `imozi://feature-guide` | Повторное знакомство |
| `imozi://feedback` | Письмо с отзывом |
| `imozi://in-app-review` | Отзыв в приложении / App Store |

## Примеры


```
imozi://daily
imozi://passage?id=1
imozi://ask
imozi://study
imozi://hunt
```

</section>
<section lang="th" markdown="1">

iMozi รองรับ} BAR `imozi://` BAR BAR ลิงก์ลัด (RUL scheme) การเริ่มหน้าจอหน้าจอเย็นและหน้าจอบ้าน จะถูกส่งไปผ่านระบบบัฟเฟอร์แบบรวม ดังนั้นลิงก์จึงไม่ถูกเปิดสองครั้งหลังจากขึ้นเครื่อง

## รูปแบบลิงก์


```
imozi://{host}?{params}
```


## ผู้เขียน

| URL | เปิด |
|-----|-------|
| `imozi://passage?id={id}` | รายละเอียดข้อความ |
| `imozi://saying?id={id}` / `imozi://couplet?id={id}` / `imozi://poem?id={id}` | เช่นเดียวกันกับเนื้อเรื่อง (ความเข้ากันได้) |
| `imozi://passage?id={id}&card=1` | รายละเอียดและนามบัตร |
| `imozi://card?id={id}` / `imozi://share-card?id={id}` | ○ การ์ด |
| `imozi://author?id={id}` | รายละเอียดผู้แต่ง |
| `imozi://recite` / `imozi://recite?id={id}` | โฟลว์การท่อง |

## การท่องเว็บ

| URL | เปิด |
|-----|-------|
| `imozi://home` | หน้าแรก |
| `imozi://daily` | โม ใน ปัจจุบัน |
| `imozi://random` | ข้อความแบบสุ่ม |
| `imozi://favorites` | รายการโปรด |
| `imozi://famous` | บรรทัดขึ้นชื่อ |
| `imozi://search` / `imozi://search?q={query}` | ค้นหา |
| `imozi://study` / `imozi://study?id={id}` | การ ศึกษา วิจัย ของ โม ฮิม |
| `imozi://hunt` | หมายเหตุล่า ('คีย์เวิร์ด-ฮันต์' / 'ดอกไม้แมลงวัน') |
| `imozi://handwriting` | สืบค้นเมื่อเขียนด้วยมือ ('เขียนเอง'; OS) |
| `imozi://mastered` | สําเร็จการศึกษาแล้ว ('รุก') |
| `imozi://categories` / `imozi://categories?section=` | เรียกดู |
| `imozi://collection?id=` | ชุดสะสม / หนังสือ |
| `imozi://corpus` | ทุกช่อง (ทั้งหมด) |
| `imozi://last-read` | รายการที่อ่านล่าสุด |
| `imozi://reading-history` | ประวัติการอ่าน |
| `imozi://notes` | บันทึก |
| `imozi://ask` | ถามมอสซี่ดูสิ |
| `imozi://fables` / `imozi://allegories` / `imozi://concepts` | ชั้นวางพิเศษเมื่อมี |

## การตั้งค่าและคู่มือ

| URL | เปิด |
|-----|-------|
| `imozi://settings` | การตั้งค่า |
| `imozi://usage-guide` | คู่มือการใช้งาน |
| `imozi://widget-guide` | คู่มือวิดเจ็ต |
| `imozi://shortcuts-guide` | คู่มือทางลัด |
| `imozi://feature-guide` | เล่นทัวร์แนะนำอีกครั้ง |
| `imozi://feedback` | อีเมลข้อเสนอแนะ |
| `imozi://in-app-review` | รีวิวในแอป / App Store |

## ตัวอย่าง


```
imozi://daily
imozi://passage?id=1
imozi://ask
imozi://study
imozi://hunt
```

</section>
<section lang="de" markdown="1">

iMoZi unterstützt ** `imozi://` ** Shortcut Links (URL-Schema). Kaltstart- und Home Screen-Verknüpfungen werden über einen einheitlichen Puffer geliefert, so dass Links nach dem Onboarding nicht zweimal geöffnet werden.

## Linkformat


```
imozi://{host}?{params}
```


## Passagen & Autoren

| URL | Öffnet |
|-----|-------|
| `imozi://passage?id={id}` | Passagen-Detail |
| `imozi://saying?id={id}` / `imozi://couplet?id={id}` / `imozi://poem?id={id}` | Wie Passage (Kompatibilität) |
| `imozi://passage?id={id}&card=1` | Angaben zum Durchgang und Kartenblatt |
| `imozi://card?id={id}` / `imozi://share-card?id={id}` | 墨 Karten |
| `imozi://author?id={id}` | Autorendetail |
| `imozi://recite` / `imozi://recite?id={id}` | Rezitationsablauf |

## Entdeckung und Praxis

| URL | Öffnet |
|-----|-------|
| `imozi://home` | Startseite |
| `imozi://daily` | Der heutige Mo |
| `imozi://random` | Zufällige Passage |
| `imozi://favorites` | Favoriten |
| `imozi://famous` | Berühmte Zeilen |
| `imozi://search` / `imozi://search?q={query}` | Suche |
| `imozi://study` / `imozi://study?id={id}` | Mohismus-Studie |
| `imozi://hunt` | Sentence Hunt (`keyword-hunt` / `flyflower`) |
| `imozi://handwriting` | Handschriftsuche (`handwrite`; iOS) |
| `imozi://mastered` | gemeistert („Fortschritt) |
| `imozi://categories` / `imozi://categories?section=` | Durchsuchen |
| `imozi://collection?id=` | Sammlung/Buch |
| `imozi://corpus` | Alle Passagen (`all`) |
| `imozi://last-read` | Zuletzt gelesen |
| `imozi://reading-history` | Leseverlauf |
| `imozi://notes` | Notizen |
| `imozi://ask` | Fragen Sie Mozi |
| `imozi://fables` / `imozi://allegories` / `imozi://concepts` | Spezialregale, wenn verfügbar |

## Einstellungen & Anleitungen

| URL | Öffnet |
|-----|-------|
| `imozi://settings` | Einstellungen |
| `imozi://usage-guide` | Nutzungsanleitung |
| `imozi://widget-guide` | Widget-Anleitung |
| `imozi://shortcuts-guide` | Kurzbefehle-Anleitung |
| `imozi://feature-guide` | Einführung erneut abspielen |
| `imozi://feedback` | Feedback-E-Mail |
| `imozi://in-app-review` | In-App- / App-Store-Bewertung |

## Beispiele


```
imozi://daily
imozi://passage?id=1
imozi://ask
imozi://study
imozi://hunt
```

</section>
<section lang="fr" markdown="1">

iMoZi prend en charge ** `imozi://` ** liens de raccourci (schéma URL). Les raccourcis de démarrage à froid et d'écran d'accueil sont livrés via un tampon unifié de sorte que les liens ne sont pas ouverts deux fois après l'embarquement.

## Format de lien


```
imozi://{host}?{params}
```


## Passages et auteurs

| URL | Ouvre |
|-----|-------|
| `imozi://passage?id={id}` | Détail du passage |
| `imozi://saying?id={id}` / `imozi://couplet?id={id}` / `imozi://poem?id={id}` | Même chose que le passage (compatibilité) |
| `imozi://passage?id={id}&card=1` | Détails du passage et feuille de carte |
| `imozi://card?id={id}` / `imozi://share-card?id={id}` | Cartes |
| `imozi://author?id={id}` | Détail de l’auteur |
| `imozi://recite` / `imozi://recite?id={id}` | Flux de récitation |

## Découverte et pratique

| URL | Ouvre |
|-----|-------|
| `imozi://home` | Accueil |
| `imozi://daily` | Aujourd'hui |
| `imozi://random` | Passage aléatoire |
| `imozi://favorites` | Favoris |
| `imozi://famous` | Vers célèbres |
| `imozi://search` / `imozi://search?q={query}` | Recherche |
| `imozi://study` / `imozi://study?id={id}` | Étude sur le mohisme |
| `imozi://hunt` | Chasse à la peine ( ' chasse aux mots clés ' / ' fleurs volantes ') |
| `imozi://handwriting` | Recherche d'écriture (`handwrite`; iOS) |
| `imozi://mastered` | Maîtrise ('progrès') |
| `imozi://categories` / `imozi://categories?section=` | Parcourir |
| `imozi://collection?id=` | Collection / livre |
| `imozi://corpus` | Tous les passages |
| `imozi://last-read` | Dernière lecture |
| `imozi://reading-history` | Historique de lecture |
| `imozi://notes` | Notes |
| `imozi://ask` | Demandez à Mozi |
| `imozi://fables` / `imozi://allegories` / `imozi://concepts` | Étagères spéciales lorsque disponibles |

## Réglages et guides

| URL | Ouvre |
|-----|-------|
| `imozi://settings` | Réglages |
| `imozi://usage-guide` | Guide d'utilisation |
| `imozi://widget-guide` | Guide des widgets |
| `imozi://shortcuts-guide` | Guide Raccourcis |
| `imozi://feature-guide` | Rejouer l’accueil |
| `imozi://feedback` | E-mail de commentaires |
| `imozi://in-app-review` | Avis in-app / App Store |

## Exemples


```
imozi://daily
imozi://passage?id=1
imozi://ask
imozi://study
imozi://hunt
```

</section>
<section lang="tr" markdown="1">

iMoZi, ** `imozi://` ** kısayol bağlantıları (URL planı). Soğuk başlangıç ve Ev Ekran kısayolları birleşik bir tampon aracılığıyla teslim edilir, bu yüzden bağlantılar gemiden sonra iki kez açılmaz.

## Bağlantı biçimi


```
imozi://{host}?{params}
```


## Geçişler ve yazarlar

| URL | Açar |
|-----|-------|
| `imozi://passage?id={id}` | Pasaj ayrıntısı |
| `imozi://saying?id={id}` / `imozi://couplet?id={id}` / `imozi://poem?id={id}` | Aynı geçiş (compatability) |
| `imozi://passage?id={id}&card=1` | Pasaj detay ve kart sayfası |
| `imozi://card?id={id}` / `imozi://share-card?id={id}` | kartları |
| `imozi://author?id={id}` | Yazar ayrıntısı |
| `imozi://recite` / `imozi://recite?id={id}` | Okuma akışı |

## Discovery & practice

| URL | Açar |
|-----|-------|
| `imozi://home` | Ana sayfa |
| `imozi://daily` | Bugünün Moları |
| `imozi://random` | Rastgele pasaj |
| `imozi://favorites` | Favoriler |
| `imozi://famous` | Ünlü dizeler |
| `imozi://search` / `imozi://search?q={query}` | Ara |
| `imozi://study` / `imozi://study?id={id}` | Mohizm Çalışması |
| `imozi://hunt` | Sentence Hunt ('keyword-hunt' / 'flyflower') |
| `imozi://handwriting` | Hand writing search ('handwrite'; iOS) |
| `imozi://mastered` | Mastered ('progress') |
| `imozi://categories` / `imozi://categories?section=` | Gözat |
| `imozi://collection?id=` | Koleksiyon / kitap |
| `imozi://corpus` | Bütün geçitler ('all') |
| `imozi://last-read` | Son okunan |
| `imozi://reading-history` | Okuma geçmişi |
| `imozi://notes` | Notlar |
| `imozi://ask` | Mozi |
| `imozi://fables` / `imozi://allegories` / `imozi://concepts` | Mevcut özel raflar |

## Ayarlar ve kılavuzlar

| URL | Açar |
|-----|-------|
| `imozi://settings` | Ayarlar |
| `imozi://usage-guide` | Kullanım kılavuzu |
| `imozi://widget-guide` | Widget kılavuzu |
| `imozi://shortcuts-guide` | Kısayol kılavuzu |
| `imozi://feature-guide` | Tanıtımı yeniden oynat |
| `imozi://feedback` | Geri bildirim e-postası |
| `imozi://in-app-review` | Uygulama içi / App Store değerlendirme |

## Örnekler


```
imozi://daily
imozi://passage?id=1
imozi://ask
imozi://study
imozi://hunt
```

</section>
