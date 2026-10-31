---
layout: doc
title: iMencius — Shortcut Links
app_id: iMencius
doc_title_en: Shortcut Links
doc_title_zh_cn: 快捷链接说明
doc_title_zh_tw: 快捷連結說明
description: imencius:// deep links for iMencius — passage, daily, recite, study, hunt, settings guides, and more.
---

<section lang="en" markdown="1">

iMencius supports **`imencius://`** shortcut links (URL scheme). Cold start and Home Screen shortcuts are delivered through a unified buffer so links are not opened twice after onboarding.

## Link format

```
imencius://{host}?{params}
```

## Passages & authors

| URL | Opens |
|-----|-------|
| `imencius://passage?id={id}` | Passage detail |
| `imencius://saying?id={id}` / `imencius://couplet?id={id}` / `imencius://poem?id={id}` | Same as passage (compatibility) |
| `imencius://passage?id={id}&card=1` | Passage detail and card sheet |
| `imencius://card?id={id}` / `imencius://share-card?id={id}` | 孟 cards |
| `imencius://author?id={id}` | Author detail |
| `imencius://recite` / `imencius://recite?id={id}` | Recite flow |

## Discovery & practice

| URL | Opens |
|-----|-------|
| `imencius://home` | Home |
| `imencius://daily` | Daily Saying |
| `imencius://random` | Random passage |
| `imencius://favorites` | Favorites |
| `imencius://famous` | Famous lines |
| `imencius://search` / `imencius://search?q={query}` | Search |
| `imencius://study` / `imencius://study?id={id}` | Nurturing Qi Study |
| `imencius://hunt` | Yi Hunt (`keyword-hunt` / `flyflower`) |
| `imencius://handwriting` | Handwriting search (`handwrite`; iOS) |
| `imencius://mastered` | Mastered (`progress`) |
| `imencius://categories` / `imencius://categories?section=` | Browse |
| `imencius://collection?id=` | Collection / book |
| `imencius://corpus` | All passages (`all`) |
| `imencius://last-read` | Last read |
| `imencius://reading-history` | Reading history |
| `imencius://notes` | Notes |
| `imencius://fables` / `imencius://allegories` / `imencius://concepts` | Specialty shelves when available |

## Settings & guides

| URL | Opens |
|-----|-------|
| `imencius://settings` | Settings |
| `imencius://usage-guide` | Usage guide |
| `imencius://widget-guide` | Widget guide |
| `imencius://shortcuts-guide` | Shortcuts guide |
| `imencius://feature-guide` | Replay onboarding |
| `imencius://feedback` | Feedback email |
| `imencius://in-app-review` | In-app / Store review entry |

## Examples

```
imencius://daily
imencius://passage?id=1
imencius://study
imencius://hunt
```

</section>
<section lang="zh-CN" markdown="1">

爱孟子 支持 **`imencius://`** 快捷链接（URL Scheme）。冷启动与主屏幕快捷方式经统一缓冲投递，避免引导后重复打开。

## 链接格式

```
imencius://{host}?{params}
```

## 篇目与作者

| URL | 打开 |
|-----|------|
| `imencius://passage?id={id}` | 篇目详情 |
| `imencius://saying?id={id}` / `imencius://couplet?id={id}` / `imencius://poem?id={id}` | 同 passage（兼容） |
| `imencius://passage?id={id}&card=1` | 篇目详情并打开分享卡 |
| `imencius://card?id={id}` / `imencius://share-card?id={id}` | 孟卡 |
| `imencius://author?id={id}` | 作者详情 |
| `imencius://recite` / `imencius://recite?id={id}` | 诵读 |

## 发现与练习

| URL | 打开 |
|-----|------|
| `imencius://home` | 首页 |
| `imencius://daily` | 每日一语 |
| `imencius://random` | 随机一篇 |
| `imencius://favorites` | 收藏 |
| `imencius://famous` | 名句 |
| `imencius://search` / `imencius://search?q={query}` | 搜索 |
| `imencius://study` / `imencius://study?id={id}` | 养气学堂 |
| `imencius://hunt` | 寻义（`keyword-hunt` / `flyflower`） |
| `imencius://handwriting` | 手写寻句（`handwrite`；iOS） |
| `imencius://mastered` | 已掌握（`progress`） |
| `imencius://categories` / `imencius://categories?section=` | 浏览 |
| `imencius://collection?id=` | 合集／分册 |
| `imencius://corpus` | 全部篇目（`all`） |
| `imencius://last-read` | 上次阅读 |
| `imencius://reading-history` | 阅读历史 |
| `imencius://notes` | 笔记 |
| `imencius://fables` / `imencius://allegories` / `imencius://concepts` | 专属书架（如有） |

## 设置与指南

| URL | 打开 |
|-----|------|
| `imencius://settings` | 设置 |
| `imencius://usage-guide` | 使用说明 |
| `imencius://widget-guide` | 小组件说明 |
| `imencius://shortcuts-guide` | 快捷指令说明 |
| `imencius://feature-guide` | 重看功能导览 |
| `imencius://feedback` | 反馈邮件 |
| `imencius://in-app-review` | 应用内／商店评价入口 |

## 示例

```
imencius://daily
imencius://passage?id=1
imencius://study
imencius://hunt
```

</section>
<section lang="zh-TW" markdown="1">

愛孟子 支援 **`imencius://`** 快捷連結（URL Scheme）。冷啟動與主畫面捷徑經統一緩衝投遞，避免引導後重複打開。

## 連結格式

```
imencius://{host}?{params}
```

## 篇目與作者

| URL | 打開 |
|-----|------|
| `imencius://passage?id={id}` | 篇目詳情 |
| `imencius://saying?id={id}` / `imencius://couplet?id={id}` / `imencius://poem?id={id}` | 同 passage（相容） |
| `imencius://passage?id={id}&card=1` | 篇目詳情並打開分享卡 |
| `imencius://card?id={id}` / `imencius://share-card?id={id}` | 孟卡 |
| `imencius://author?id={id}` | 作者詳情 |
| `imencius://recite` / `imencius://recite?id={id}` | 誦讀 |

## 探索與練習

| URL | 打開 |
|-----|------|
| `imencius://home` | 首頁 |
| `imencius://daily` | 每日一語 |
| `imencius://random` | 隨機一篇 |
| `imencius://favorites` | 收藏 |
| `imencius://famous` | 名句 |
| `imencius://search` / `imencius://search?q={query}` | 搜尋 |
| `imencius://study` / `imencius://study?id={id}` | 養氣學堂 |
| `imencius://hunt` | 尋義（`keyword-hunt` / `flyflower`） |
| `imencius://handwriting` | 手寫尋句（`handwrite`；iOS） |
| `imencius://mastered` | 已掌握（`progress`） |
| `imencius://categories` / `imencius://categories?section=` | 瀏覽 |
| `imencius://collection?id=` | 合集／分冊 |
| `imencius://corpus` | 全部篇目（`all`） |
| `imencius://last-read` | 上次閱讀 |
| `imencius://reading-history` | 閱讀歷史 |
| `imencius://notes` | 筆記 |
| `imencius://fables` / `imencius://allegories` / `imencius://concepts` | 專屬書架（如有） |

## 設定與指南

| URL | 打開 |
|-----|------|
| `imencius://settings` | 設定 |
| `imencius://usage-guide` | 使用說明 |
| `imencius://widget-guide` | 小工具說明 |
| `imencius://shortcuts-guide` | 捷徑說明 |
| `imencius://feature-guide` | 重看功能導覽 |
| `imencius://feedback` | 回饋郵件 |
| `imencius://in-app-review` | 應用內／商店評價入口 |

## 範例

```
imencius://daily
imencius://passage?id=1
imencius://study
imencius://hunt
```

</section>
<section lang="ja" markdown="1">

iMenciusは** `imencius://` **ショートカットリンク(URLスキーム)をサポートしています。 コールドスタートとホーム画面のショートカットは、統一されたバッファを介して配信されますので、リンクはオンボーディング後2回開いていません。

## リンク形式


```
imencius://{host}?{params}
```


## パスポートと著者

| URL | 開く画面 |
|-----|-------|
| `imencius://passage?id={id}` | 章句の詳細 |
| `imencius://saying?id={id}` / `imencius://couplet?id={id}` / `imencius://poem?id={id}` | 通路と同じ(互換性) |
| `imencius://passage?id={id}&card=1` | 通路の細部およびカード シート |
| `imencius://card?id={id}` / `imencius://share-card?id={id}` | カード |
| `imencius://author?id={id}` | 作者の詳細 |
| `imencius://recite` / `imencius://recite?id={id}` | 誦読フロー |

## ディスカバリー&プラクティス

| URL | 開く画面 |
|-----|-------|
| `imencius://home` | ホーム |
| `imencius://daily` | 日常の言うこと |
| `imencius://random` | ランダムな章句 |
| `imencius://favorites` | お気に入り |
| `imencius://famous` | 名句一覧 |
| `imencius://search` / `imencius://search?q={query}` | 検索 |
| `imencius://study` / `imencius://study?id={id}` | Qiの学習 |
| `imencius://hunt` | 李ハント (`keyword-hunt`/`flyflower`) |
| `imencius://handwriting` | 手書き検索 (`handwrite`; iOS) |
| `imencius://mastered` | マスタード (`progress`) |
| `imencius://categories` / `imencius://categories?section=` | ブラウズ |
| `imencius://collection?id=` | コレクション/書籍 |
| `imencius://corpus` | すべての通路 (`all`) |
| `imencius://last-read` | 最後に読んだ項目 |
| `imencius://reading-history` | 閲覧履歴 |
| `imencius://notes` | ノート |
| `imencius://fables` / `imencius://allegories` / `imencius://concepts` | 利用できる場合の特別な棚 |

## 設定とガイド

| URL | 開く画面 |
|-----|-------|
| `imencius://settings` | 設定 |
| `imencius://usage-guide` | 使い方ガイド |
| `imencius://widget-guide` | ウィジェットガイド |
| `imencius://shortcuts-guide` | ショートカットガイド |
| `imencius://feature-guide` | オンボーディングの再生 |
| `imencius://feedback` | フィードバックメール |
| `imencius://in-app-review` | アプリ内／App Store レビュー |

## 例


```
imencius://daily
imencius://passage?id=1
imencius://study
imencius://hunt
```

</section>
<section lang="ko" markdown="1">

iMencius는 ** `imencius://` ** 단축키 링크 (URL 계획)를 지원합니다. 콜드 시작 및 홈 화면 단축은 통합 버퍼를 통해 전달되므로 링크가 내장 된 후 두 번 열리지 않습니다.

## 링크 형식


```
imencius://{host}?{params}
```


## 책임 & 저자

| URL | 열리는 화면 |
|-----|-------|
| `imencius://passage?id={id}` | 구절 상세 |
| `imencius://saying?id={id}` / `imencius://couplet?id={id}` / `imencius://poem?id={id}` | 통행과 같 ( 겸용성) |
| `imencius://passage?id={id}&card=1` | 통행 세부사항과 카드 장 |
| `imencius://card?id={id}` / `imencius://share-card?id={id}` | 카드 종류 |
| `imencius://author?id={id}` | 작가 상세 |
| `imencius://recite` / `imencius://recite?id={id}` | 낭독 흐름 |

## 디스커버리 & 연습

| URL | 열리는 화면 |
|-----|-------|
| `imencius://home` | 홈 |
| `imencius://daily` | 매일 말 |
| `imencius://random` | 무작위 구절 |
| `imencius://favorites` | 즐겨찾기 |
| `imencius://famous` | 명구 목록 |
| `imencius://search` / `imencius://search?q={query}` | 검색 |
| `imencius://study` / `imencius://study?id={id}` | Qi 연구 |
| `imencius://hunt` | 이헌 (`keyword-hunt`/`flyflower`) |
| `imencius://handwriting` | Handwriting search (`handwrite`; iOS) |
| `imencius://mastered` | 마스터 (`progress`) |
| `imencius://categories` / `imencius://categories?section=` | 둘러보기 |
| `imencius://collection?id=` | 컬렉션 / 책 |
| `imencius://corpus` | 모든 통행 (`all`) |
| `imencius://last-read` | 마지막으로 읽은 항목 |
| `imencius://reading-history` | 읽기 기록 |
| `imencius://notes` | 메모 |
| `imencius://fables` / `imencius://allegories` / `imencius://concepts` | 사용할 때 특수 선반 |

## 설정 및 가이드

| URL | 열리는 화면 |
|-----|-------|
| `imencius://settings` | 설정 |
| `imencius://usage-guide` | 사용 가이드 |
| `imencius://widget-guide` | 위젯 가이드 |
| `imencius://shortcuts-guide` | 단축어 가이드 |
| `imencius://feature-guide` | 온보딩 다시 보기 |
| `imencius://feedback` | 피드백 이메일 |
| `imencius://in-app-review` | 앱 내 / App Store 리뷰 |

## 예시


```
imencius://daily
imencius://passage?id=1
imencius://study
imencius://hunt
```

</section>
<section lang="ru" markdown="1">

iMencius поддерживает ярлыки ** `imencius://` ** (схема URL). Холодный старт и ярлыки домашнего экрана доставляются через единый буфер, поэтому ссылки не открываются дважды после входа.

## Формат ссылки


```
imencius://{host}?{params}
```


## Проходы и авторы

| URL | Открывает |
|-----|-------|
| `imencius://passage?id={id}` | Страница отрывка |
| `imencius://saying?id={id}` / `imencius://couplet?id={id}` / `imencius://poem?id={id}` | Совместимость (Compatibility) |
| `imencius://passage?id={id}&card=1` | Детали проезда и карточный лист |
| `imencius://card?id={id}` / `imencius://share-card?id={id}` | карты |
| `imencius://author?id={id}` | Страница автора |
| `imencius://recite` / `imencius://recite?id={id}` | Режим чтения вслух |

## Discovery & Practice

| URL | Открывает |
|-----|-------|
| `imencius://home` | Главная |
| `imencius://daily` | Ежедневные высказывания |
| `imencius://random` | Случайный отрывок |
| `imencius://favorites` | Избранное |
| `imencius://famous` | Знаменитые строки |
| `imencius://search` / `imencius://search?q={query}` | Поиск |
| `imencius://study` / `imencius://study?id={id}` | Обучение Qi Study |
| `imencius://hunt` | Yi Hunt («охота за ключевыми словами» / «флайфлауэр») |
| `imencius://handwriting` | Поиск почерка («handwrite»; iOS) |
| `imencius://mastered` | Мастеринг («Прогресс») |
| `imencius://categories` / `imencius://categories?section=` | Обзор |
| `imencius://collection?id=` | Коллекция / книга |
| `imencius://corpus` | Все пассажи («All») |
| `imencius://last-read` | Последнее прочитанное |
| `imencius://reading-history` | История чтения |
| `imencius://notes` | Заметки |
| `imencius://fables` / `imencius://allegories` / `imencius://concepts` | Специальные полки, когда они доступны |

## Настройки и руководства

| URL | Открывает |
|-----|-------|
| `imencius://settings` | Настройки |
| `imencius://usage-guide` | Руководство по использованию |
| `imencius://widget-guide` | Руководство по виджетам |
| `imencius://shortcuts-guide` | Руководство по «Командам» |
| `imencius://feature-guide` | Повторное знакомство |
| `imencius://feedback` | Письмо с отзывом |
| `imencius://in-app-review` | Отзыв в приложении / App Store |

## Примеры


```
imencius://daily
imencius://passage?id=1
imencius://study
imencius://hunt
```

</section>
<section lang="th" markdown="1">

iMencius รองรับ ** `imencius://` BAR * ลิงก์ลัด (URL scheme). การเริ่มหน้าจอหน้าจอเย็นและหน้าจอบ้าน จะถูกส่งไปผ่านระบบบัฟเฟอร์แบบรวม ดังนั้นลิงก์จึงไม่ถูกเปิดสองครั้งหลังจากขึ้นเครื่อง

## รูปแบบลิงก์


```
imencius://{host}?{params}
```


## ผู้เขียน

| URL | เปิด |
|-----|-------|
| `imencius://passage?id={id}` | รายละเอียดข้อความ |
| `imencius://saying?id={id}` / `imencius://couplet?id={id}` / `imencius://poem?id={id}` | เช่นเดียวกันกับเนื้อเรื่อง (ความเข้ากันได้) |
| `imencius://passage?id={id}&card=1` | รายละเอียดและนามบัตร |
| `imencius://card?id={id}` / `imencius://share-card?id={id}` | ○ การ์ด |
| `imencius://author?id={id}` | รายละเอียดผู้แต่ง |
| `imencius://recite` / `imencius://recite?id={id}` | โฟลว์การท่อง |

## การท่องเว็บ

| URL | เปิด |
|-----|-------|
| `imencius://home` | หน้าแรก |
| `imencius://daily` | ทุก วัน |
| `imencius://random` | ข้อความแบบสุ่ม |
| `imencius://favorites` | รายการโปรด |
| `imencius://famous` | บรรทัดขึ้นชื่อ |
| `imencius://search` / `imencius://search?q={query}` | ค้นหา |
| `imencius://study` / `imencius://study?id={id}` | การ ศึกษา พระ คัมภีร์ |
| `imencius://hunt` | ยีฮันท์ ('คีย์เวิร์ด-ฮันต์' / 'ดอกไม้แมลงวัน') |
| `imencius://handwriting` | สืบค้นเมื่อเขียนด้วยมือ ('เขียนเอง'; OS) |
| `imencius://mastered` | สําเร็จการศึกษาแล้ว ('รุก') |
| `imencius://categories` / `imencius://categories?section=` | เรียกดู |
| `imencius://collection?id=` | ชุดสะสม / หนังสือ |
| `imencius://corpus` | ทุกช่อง (ทั้งหมด) |
| `imencius://last-read` | รายการที่อ่านล่าสุด |
| `imencius://reading-history` | ประวัติการอ่าน |
| `imencius://notes` | บันทึก |
| `imencius://fables` / `imencius://allegories` / `imencius://concepts` | ชั้นวางพิเศษเมื่อมี |

## การตั้งค่าและคู่มือ

| URL | เปิด |
|-----|-------|
| `imencius://settings` | การตั้งค่า |
| `imencius://usage-guide` | คู่มือการใช้งาน |
| `imencius://widget-guide` | คู่มือวิดเจ็ต |
| `imencius://shortcuts-guide` | คู่มือทางลัด |
| `imencius://feature-guide` | เล่นทัวร์แนะนำอีกครั้ง |
| `imencius://feedback` | อีเมลข้อเสนอแนะ |
| `imencius://in-app-review` | รีวิวในแอป / App Store |

## ตัวอย่าง


```
imencius://daily
imencius://passage?id=1
imencius://study
imencius://hunt
```

</section>
<section lang="de" markdown="1">

iMencius unterstützt ** `imencius://` ** Shortcut Links (URL-Schema). Kaltstart- und Home Screen-Verknüpfungen werden über einen einheitlichen Puffer geliefert, so dass Links nach dem Onboarding nicht zweimal geöffnet werden.

## Linkformat


```
imencius://{host}?{params}
```


## Passagen & Autoren

| URL | Öffnet |
|-----|-------|
| `imencius://passage?id={id}` | Passagen-Detail |
| `imencius://saying?id={id}` / `imencius://couplet?id={id}` / `imencius://poem?id={id}` | Wie Passage (Kompatibilität) |
| `imencius://passage?id={id}&card=1` | Angaben zum Durchgang und Kartenblatt |
| `imencius://card?id={id}` / `imencius://share-card?id={id}` | 孟 Karten |
| `imencius://author?id={id}` | Autorendetail |
| `imencius://recite` / `imencius://recite?id={id}` | Rezitationsablauf |

## Entdeckung und Praxis

| URL | Öffnet |
|-----|-------|
| `imencius://home` | Startseite |
| `imencius://daily` | Tägliches Sagen |
| `imencius://random` | Zufällige Passage |
| `imencius://favorites` | Favoriten |
| `imencius://famous` | Berühmte Zeilen |
| `imencius://search` / `imencius://search?q={query}` | Suche |
| `imencius://study` / `imencius://study?id={id}` | Qi-Studie fördern |
| `imencius://hunt` | Yi Hunt (`keyword-hunt` / `flyflower`) |
| `imencius://handwriting` | Handschriftsuche (`handwrite`; iOS) |
| `imencius://mastered` | gemeistert („Fortschritt) |
| `imencius://categories` / `imencius://categories?section=` | Durchsuchen |
| `imencius://collection?id=` | Sammlung/Buch |
| `imencius://corpus` | Alle Passagen (`all`) |
| `imencius://last-read` | Zuletzt gelesen |
| `imencius://reading-history` | Leseverlauf |
| `imencius://notes` | Notizen |
| `imencius://fables` / `imencius://allegories` / `imencius://concepts` | Spezialregale, wenn verfügbar |

## Einstellungen & Anleitungen

| URL | Öffnet |
|-----|-------|
| `imencius://settings` | Einstellungen |
| `imencius://usage-guide` | Nutzungsanleitung |
| `imencius://widget-guide` | Widget-Anleitung |
| `imencius://shortcuts-guide` | Kurzbefehle-Anleitung |
| `imencius://feature-guide` | Einführung erneut abspielen |
| `imencius://feedback` | Feedback-E-Mail |
| `imencius://in-app-review` | In-App- / App-Store-Bewertung |

## Beispiele


```
imencius://daily
imencius://passage?id=1
imencius://study
imencius://hunt
```

</section>
<section lang="fr" markdown="1">

iMencius prend en charge les liens de raccourci ** `imencius://` ** (schéma URL). Les raccourcis de démarrage à froid et d'écran d'accueil sont livrés via un tampon unifié de sorte que les liens ne sont pas ouverts deux fois après l'embarquement.

## Format de lien


```
imencius://{host}?{params}
```


## Passages et auteurs

| URL | Ouvre |
|-----|-------|
| `imencius://passage?id={id}` | Détail du passage |
| `imencius://saying?id={id}` / `imencius://couplet?id={id}` / `imencius://poem?id={id}` | Même chose que le passage (compatibilité) |
| `imencius://passage?id={id}&card=1` | Détails du passage et feuille de carte |
| `imencius://card?id={id}` / `imencius://share-card?id={id}` | Cartes |
| `imencius://author?id={id}` | Détail de l’auteur |
| `imencius://recite` / `imencius://recite?id={id}` | Flux de récitation |

## Découverte et pratique

| URL | Ouvre |
|-----|-------|
| `imencius://home` | Accueil |
| `imencius://daily` | Dire quotidiennement |
| `imencius://random` | Passage aléatoire |
| `imencius://favorites` | Favoris |
| `imencius://famous` | Vers célèbres |
| `imencius://search` / `imencius://search?q={query}` | Recherche |
| `imencius://study` / `imencius://study?id={id}` | Favoriser l'étude du Qi |
| `imencius://hunt` | Yi Hunt (chasse de mots clés / flyflower) |
| `imencius://handwriting` | Recherche d'écriture (`handwrite`; iOS) |
| `imencius://mastered` | Maîtrise ('progrès') |
| `imencius://categories` / `imencius://categories?section=` | Parcourir |
| `imencius://collection?id=` | Collection / livre |
| `imencius://corpus` | Tous les passages |
| `imencius://last-read` | Dernière lecture |
| `imencius://reading-history` | Historique de lecture |
| `imencius://notes` | Notes |
| `imencius://fables` / `imencius://allegories` / `imencius://concepts` | Étagères spéciales lorsque disponibles |

## Réglages et guides

| URL | Ouvre |
|-----|-------|
| `imencius://settings` | Réglages |
| `imencius://usage-guide` | Guide d'utilisation |
| `imencius://widget-guide` | Guide des widgets |
| `imencius://shortcuts-guide` | Guide Raccourcis |
| `imencius://feature-guide` | Rejouer l’accueil |
| `imencius://feedback` | E-mail de commentaires |
| `imencius://in-app-review` | Avis in-app / App Store |

## Exemples


```
imencius://daily
imencius://passage?id=1
imencius://study
imencius://hunt
```

</section>
<section lang="tr" markdown="1">

iMencius, ** `imencius://` ** kısayol bağlantıları (URL planı). Soğuk başlangıç ve Ev Ekran kısayolları birleşik bir tampon aracılığıyla teslim edilir, bu yüzden bağlantılar gemiden sonra iki kez açılmaz.

## Bağlantı biçimi


```
imencius://{host}?{params}
```


## Geçişler ve yazarlar

| URL | Açar |
|-----|-------|
| `imencius://passage?id={id}` | Pasaj ayrıntısı |
| `imencius://saying?id={id}` / `imencius://couplet?id={id}` / `imencius://poem?id={id}` | Aynı geçiş (compatability) |
| `imencius://passage?id={id}&card=1` | Pasaj detay ve kart sayfası |
| `imencius://card?id={id}` / `imencius://share-card?id={id}` | kartları |
| `imencius://author?id={id}` | Yazar ayrıntısı |
| `imencius://recite` / `imencius://recite?id={id}` | Okuma akışı |

## Discovery & practice

| URL | Açar |
|-----|-------|
| `imencius://home` | Ana sayfa |
| `imencius://daily` | Daily Saying |
| `imencius://random` | Rastgele pasaj |
| `imencius://favorites` | Favoriler |
| `imencius://famous` | Ünlü dizeler |
| `imencius://search` / `imencius://search?q={query}` | Ara |
| `imencius://study` / `imencius://study?id={id}` | Nurturing Qi Study |
| `imencius://hunt` | Yi Hunt ('keyword-hunt' / 'flyflower') |
| `imencius://handwriting` | Hand writing search ('handwrite'; iOS) |
| `imencius://mastered` | Mastered ('progress') |
| `imencius://categories` / `imencius://categories?section=` | Gözat |
| `imencius://collection?id=` | Koleksiyon / kitap |
| `imencius://corpus` | Bütün geçitler ('all') |
| `imencius://last-read` | Son okunan |
| `imencius://reading-history` | Okuma geçmişi |
| `imencius://notes` | Notlar |
| `imencius://fables` / `imencius://allegories` / `imencius://concepts` | Mevcut özel raflar |

## Ayarlar ve kılavuzlar

| URL | Açar |
|-----|-------|
| `imencius://settings` | Ayarlar |
| `imencius://usage-guide` | Kullanım kılavuzu |
| `imencius://widget-guide` | Widget kılavuzu |
| `imencius://shortcuts-guide` | Kısayol kılavuzu |
| `imencius://feature-guide` | Tanıtımı yeniden oynat |
| `imencius://feedback` | Geri bildirim e-postası |
| `imencius://in-app-review` | Uygulama içi / App Store değerlendirme |

## Örnekler


```
imencius://daily
imencius://passage?id=1
imencius://study
imencius://hunt
```

</section>
