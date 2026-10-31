---
layout: doc
title: iCouplet — Shortcut Links
app_id: iCouplet
doc_title_en: Shortcut Links
doc_title_zh_cn: 快捷链接说明
doc_title_zh_tw: 快捷連結說明
description: icouplet:// deep links for iCouplet — couplet, daily, recite, study, famous, settings guides, and more.
---

<section lang="en" markdown="1">

iCouplet supports **`icouplet://`** shortcut links (URL scheme). Cold start and Home Screen shortcuts are delivered through a unified buffer so links are not opened twice after onboarding.

## Link format

```
icouplet://{host}?{params}
```

## Couplets & authors

| URL | Opens |
|-----|-------|
| `icouplet://couplet?id={id}` | Couplet detail |
| `icouplet://poem?id={id}` | Same as couplet (compatibility alias) |
| `icouplet://author?id={id}` | Author (联家) detail |
| `icouplet://recite` | Recite flow (auto-speak when possible) |
| `icouplet://recite?id={id}` | Open couplet and auto-recite |

## Discovery

| URL | Opens |
|-----|-------|
| `icouplet://home` | Home tab |
| `icouplet://daily` | Today’s Daily Couplet |
| `icouplet://random` | Random couplet |
| `icouplet://favorites` | Favorites |
| `icouplet://famous` | Famous lines list |
| `icouplet://search` | Search |
| `icouplet://search?q={query}` | Search with query |
| `icouplet://study` | Study / 对对子 entry |
| `icouplet://categories` | Browse categories |
| `icouplet://categories?section=form` | Form (体裁) section |
| `icouplet://categories?section=theme` | Theme section |
| `icouplet://categories?section=author` | Author section |
| `icouplet://categories?section=famous` | Famous lines section |
| `icouplet://categories?section=corpus` | Collections / corpus |
| `icouplet://last-read` | Last read couplet |
| `icouplet://reading-history` | Reading history |

## Settings & guides

| URL | Opens |
|-----|-------|
| `icouplet://settings` | Settings root |
| `icouplet://usage-guide` | Usage guide |
| `icouplet://widget-guide` | Widget guide |
| `icouplet://shortcuts-guide` | Shortcuts guide |
| `icouplet://feature-guide` | Replay feature onboarding |
| `icouplet://feedback` | Feedback email |
| `icouplet://in-app-review` | In-app / Store review entry |

## Examples

```
icouplet://daily
icouplet://couplet?id=1
icouplet://recite?id=1
icouplet://search?q=春
icouplet://categories?section=famous
icouplet://widget-guide
```

Use these in the Shortcuts app, Home Screen quick actions, widgets, or Safari. See also in-app **Settings → Shortcuts Guide**.

</section>
<section lang="zh-CN" markdown="1">

爱对联支持 **`icouplet://`** 快捷链接。冷启动与主屏快捷经统一缓冲投递，避免引导结束后重复打开。

## 链接格式

```
icouplet://{host}?{params}
```

## 对联与联家

| 链接 | 打开 |
|------|------|
| `icouplet://couplet?id={id}` | 联详情 |
| `icouplet://poem?id={id}` | 同 couplet（兼容别名） |
| `icouplet://author?id={id}` | 联家详情 |
| `icouplet://recite` | 诵联流程（可自动开读） |
| `icouplet://recite?id={id}` | 打开指定联并自动诵联 |

## 发现

| 链接 | 打开 |
|------|------|
| `icouplet://home` | 首页 |
| `icouplet://daily` | 每日一联 |
| `icouplet://random` | 随机一联 |
| `icouplet://favorites` | 收藏 |
| `icouplet://famous` | 名句列表 |
| `icouplet://search` | 搜索 |
| `icouplet://search?q={query}` | 带关键词搜索 |
| `icouplet://study` | 对课 / 对对子入口 |
| `icouplet://categories` | 分类浏览 |
| `icouplet://categories?section=form` | 体裁 |
| `icouplet://categories?section=theme` | 主题 |
| `icouplet://categories?section=author` | 联家 |
| `icouplet://categories?section=famous` | 名句 |
| `icouplet://categories?section=corpus` | 合集 |
| `icouplet://last-read` | 最近阅读 |
| `icouplet://reading-history` | 浏览记录 |

## 设置与教程

| 链接 | 打开 |
|------|------|
| `icouplet://settings` | 设置根页 |
| `icouplet://usage-guide` | 使用说明 |
| `icouplet://widget-guide` | 小组件指南 |
| `icouplet://shortcuts-guide` | 快捷指南 |
| `icouplet://feature-guide` | 重播功能引导 |
| `icouplet://feedback` | 反馈邮件 |
| `icouplet://in-app-review` | 应用内评价入口 |

## 示例

```
icouplet://daily
icouplet://couplet?id=1
icouplet://recite?id=1
icouplet://search?q=春
icouplet://categories?section=famous
icouplet://widget-guide
```

可用于「快捷指令」、主屏长按、小组件或 Safari。详见 App 内 **设置 → 快捷指南**。

</section>
<section lang="zh-TW" markdown="1">

愛對聯支援 **`icouplet://`** 快捷連結。冷啟動與主畫面捷徑經統一緩衝投遞，避免引導結束後重複開啟。

## 連結格式

```
icouplet://{host}?{params}
```

## 對聯與聯家

| 連結 | 開啟 |
|------|------|
| `icouplet://couplet?id={id}` | 聯詳情 |
| `icouplet://poem?id={id}` | 同 couplet（相容別名） |
| `icouplet://author?id={id}` | 聯家詳情 |
| `icouplet://recite` | 誦聯流程（可自動開讀） |
| `icouplet://recite?id={id}` | 開啟指定聯並自動誦聯 |

## 發現

| 連結 | 開啟 |
|------|------|
| `icouplet://home` | 首頁 |
| `icouplet://daily` | 每日一聯 |
| `icouplet://random` | 隨機一聯 |
| `icouplet://favorites` | 收藏 |
| `icouplet://famous` | 名句列表 |
| `icouplet://search` | 搜尋 |
| `icouplet://search?q={query}` | 帶關鍵詞搜尋 |
| `icouplet://study` | 對課 / 對對子入口 |
| `icouplet://categories` | 分類瀏覽 |
| `icouplet://categories?section=form` | 體裁 |
| `icouplet://categories?section=theme` | 主題 |
| `icouplet://categories?section=author` | 聯家 |
| `icouplet://categories?section=famous` | 名句 |
| `icouplet://categories?section=corpus` | 合集 |
| `icouplet://last-read` | 最近閱讀 |
| `icouplet://reading-history` | 瀏覽紀錄 |

## 設定與教學

| 連結 | 開啟 |
|------|------|
| `icouplet://settings` | 設定根頁 |
| `icouplet://usage-guide` | 使用說明 |
| `icouplet://widget-guide` | 小工具指南 |
| `icouplet://shortcuts-guide` | 捷徑指南 |
| `icouplet://feature-guide` | 重播功能引導 |
| `icouplet://feedback` | 回饋郵件 |
| `icouplet://in-app-review` | 應用內評價入口 |

## 範例

```
icouplet://daily
icouplet://couplet?id=1
icouplet://recite?id=1
icouplet://search?q=春
icouplet://categories?section=famous
icouplet://widget-guide
```

可用於「捷徑」、主畫面長按、小工具或 Safari。詳見 App 內 **設定 → 捷徑指南**。

</section>
<section lang="ja" markdown="1">

iCoupletは** `icouplet://` **ショートカットリンク(URLスキーム)をサポートしています。 コールドスタートとホーム画面のショートカットは、統一されたバッファを介して配信されますので、リンクはオンボーディング後2回開いていません。

## リンク形式


```
icouplet://{host}?{params}
```


## カップル&著者

| URL | 開く画面 |
|-----|-------|
| `icouplet://couplet?id={id}` | カップルディテール |
| `icouplet://poem?id={id}` | couplet と同じ (互換性エイリアス) |
| `icouplet://author?id={id}` | 著者(民家) |
| `icouplet://recite` | Recite の流れ(可能であれば自動ピーク) |
| `icouplet://recite?id={id}` | 開いた couplet および自動recite |

## 発見

| URL | 開く画面 |
|-----|-------|
| `icouplet://home` | ホームタブ |
| `icouplet://daily` | 今日の毎日のカップル |
| `icouplet://random` | ランダムカップル |
| `icouplet://favorites` | お気に入り |
| `icouplet://famous` | 有名なラインリスト |
| `icouplet://search` | 検索 |
| `icouplet://search?q={query}` | キーワード付き検索 |
| `icouplet://study` | 研究 / 子子エントリー |
| `icouplet://categories` | カテゴリーをブラウズ |
| `icouplet://categories?section=form` | フォーム(体裁)セクション |
| `icouplet://categories?section=theme` | テーマセクション |
| `icouplet://categories?section=author` | 著者セクション |
| `icouplet://categories?section=famous` | 有名なラインセクション |
| `icouplet://categories?section=corpus` | コレクション / コルパス |
| `icouplet://last-read` | 最終読み couplet |
| `icouplet://reading-history` | 閲覧履歴 |

## 設定とガイド

| URL | 開く画面 |
|-----|-------|
| `icouplet://settings` | 設定ルート |
| `icouplet://usage-guide` | 使い方ガイド |
| `icouplet://widget-guide` | ウィジェットガイド |
| `icouplet://shortcuts-guide` | ショートカットガイド |
| `icouplet://feature-guide` | 再生機能搭載 |
| `icouplet://feedback` | フィードバックメール |
| `icouplet://in-app-review` | アプリ内／App Store レビュー |

## 例


```
icouplet://daily
icouplet://couplet?id=1
icouplet://recite?id=1
icouplet://search?q=春
icouplet://categories?section=famous
icouplet://widget-guide
```


これらをショートカットアプリ、ホーム画面のクイックアクション、ウィジェット、またはSafariで使用してください。 アプリ内設定 → ショートカットガイド** も参照してください。

</section>
<section lang="ko" markdown="1">

iCouplet 지원 ** `icouplet://` ** 단축키 링크 (URL 계획). 콜드 시작 및 홈 화면 단축은 통합 버퍼를 통해 전달되므로 링크가 내장 된 후 두 번 열리지 않습니다.

## 링크 형식


```
icouplet://{host}?{params}
```


## 커플 & 저자

| URL | 열리는 화면 |
|-----|-------|
| `icouplet://couplet?id={id}` | 연결하기 |
| `icouplet://poem?id={id}` | couplet와 같 ( 겸용성 별) |
| `icouplet://author?id={id}` | Author (비밀) 상세 |
| `icouplet://recite` | Recite 흐름 (가능할 때 자동 소리) |
| `icouplet://recite?id={id}` | 커플 및 자동 인용 |

## 탐색

| URL | 열리는 화면 |
|-----|-------|
| `icouplet://home` | 홈 탭 |
| `icouplet://daily` | 오늘의 일일 커플 |
| `icouplet://random` | 무작위 커플 |
| `icouplet://favorites` | 즐겨찾기 |
| `icouplet://famous` | 유명한 라인 목록 |
| `icouplet://search` | 검색 |
| `icouplet://search?q={query}` | 검색어와 함께 검색 |
| `icouplet://study` | Study子 |
| `icouplet://categories` | 카테고리 |
| `icouplet://categories?section=form` | 양식 (体)) 섹션 |
| `icouplet://categories?section=theme` | 테마 섹션 |
| `icouplet://categories?section=author` | 저자 섹션 |
| `icouplet://categories?section=famous` | 유명한 선 단면도 |
| `icouplet://categories?section=corpus` | 컬렉션 / 코푸 |
| `icouplet://last-read` | 최근 읽지 않은 커플 |
| `icouplet://reading-history` | 읽기 기록 |

## 설정 및 가이드

| URL | 열리는 화면 |
|-----|-------|
| `icouplet://settings` | 설정 루트 |
| `icouplet://usage-guide` | 사용 가이드 |
| `icouplet://widget-guide` | 위젯 가이드 |
| `icouplet://shortcuts-guide` | 단축어 가이드 |
| `icouplet://feature-guide` | Replay 기능 내장 |
| `icouplet://feedback` | 피드백 이메일 |
| `icouplet://in-app-review` | 앱 내 / App Store 리뷰 |

## 예시


```
icouplet://daily
icouplet://couplet?id=1
icouplet://recite?id=1
icouplet://search?q=春
icouplet://categories?section=famous
icouplet://widget-guide
```


Shortcuts 앱, 홈 화면 빠른 행동, 위젯, 또는 사파리에서 이러한 사용. in-app**Settings → 단축키 가이드** 참조.

</section>
<section lang="ru" markdown="1">

iCouplet поддерживает ярлыки ** `icouplet://` ** (схема URL). Холодный старт и ярлыки домашнего экрана доставляются через единый буфер, поэтому ссылки не открываются дважды после входа.

## Формат ссылки


```
icouplet://{host}?{params}
```


## Куплеты и авторы

| URL | Открывает |
|-----|-------|
| `icouplet://couplet?id={id}` | Детали куплета |
| `icouplet://poem?id={id}` | Совместимость (compatibility alias) |
| `icouplet://author?id={id}` | Автор ( detail) Подробности |
| `icouplet://recite` | Поток речи (автоговор, когда это возможно) |
| `icouplet://recite?id={id}` | Открытый куплет и автоцит |

## Обзор

| URL | Открывает |
|-----|-------|
| `icouplet://home` | Вкладка «Главная» |
| `icouplet://daily` | Ежедневный куплет сегодня |
| `icouplet://random` | Случайная пара |
| `icouplet://favorites` | Избранное |
| `icouplet://famous` | Список знаменитых линий |
| `icouplet://search` | Поиск |
| `icouplet://search?q={query}` | Поиск с запросом |
| `icouplet://study` | Учеба /   Вступление |
| `icouplet://categories` | Просмотр категорий |
| `icouplet://categories?section=form` | Форма ( section) раздел |
| `icouplet://categories?section=theme` | Тематический раздел |
| `icouplet://categories?section=author` | Авторский раздел |
| `icouplet://categories?section=famous` | Знаменитая секция линий |
| `icouplet://categories?section=corpus` | Коллекции / корпус |
| `icouplet://last-read` | Последнее чтение Парт |
| `icouplet://reading-history` | История чтения |

## Настройки и руководства

| URL | Открывает |
|-----|-------|
| `icouplet://settings` | Настройка root |
| `icouplet://usage-guide` | Руководство по использованию |
| `icouplet://widget-guide` | Руководство по виджетам |
| `icouplet://shortcuts-guide` | Руководство по «Командам» |
| `icouplet://feature-guide` | Функция воспроизведения на борту |
| `icouplet://feedback` | Письмо с отзывом |
| `icouplet://in-app-review` | Отзыв в приложении / App Store |

## Примеры


```
icouplet://daily
icouplet://couplet?id=1
icouplet://recite?id=1
icouplet://search?q=春
icouplet://categories?section=famous
icouplet://widget-guide
```


Используйте их в приложении Shortcuts, быстрых действиях Home Screen, виджетах или Safari. См. также in-app **Settings → Shortcuts Guide**.

</section>
<section lang="th" markdown="1">

ICuplet รองรับ} `icouplet://` BAR * ลิงก์ลัด (URL scheme) การเริ่มหน้าจอหน้าจอเย็นและหน้าจอบ้าน จะถูกส่งไปผ่านระบบบัฟเฟอร์แบบรวม ดังนั้นลิงก์จึงไม่ถูกเปิดสองครั้งหลังจากขึ้นเครื่อง

## รูปแบบลิงก์


```
icouplet://{host}?{params}
```


## ผู้เขียนคู่

| URL | เปิด |
|-----|-------|
| `icouplet://couplet?id={id}` | รายละเอียดคู่ |
| `icouplet://poem?id={id}` | แบบคู่เดียวกัน (ชื่อแฟ้มที่เข้ากันได้) |
| `icouplet://author?id={id}` | ผู้เขียน (联家) รายละเอียด |
| `icouplet://recite` | การไหลของเสียง (อัตโนมัติเมื่อเป็นไปได้) |
| `icouplet://recite?id={id}` | เปิดคู่คู่และรีเซ็ตอัตโนมัติ |

## ค้นพบ

| URL | เปิด |
|-----|-------|
| `icouplet://home` | แท็บหน้าแรก |
| `icouplet://daily` | ทุก วัน นี้ |
| `icouplet://random` | สุ่มคู่ |
| `icouplet://favorites` | รายการโปรด |
| `icouplet://famous` | รายการบรรทัดที่มีชื่อเสียง |
| `icouplet://search` | ค้นหา |
| `icouplet://search?q={query}` | ค้นหาพร้อมคำค้น |
| `icouplet://study` | การ ศึกษา / ○ การ เข้า ร่วม |
| `icouplet://categories` | ประเภทการเรียกดู |
| `icouplet://categories?section=form` | Form (体裁) ตอน |
| `icouplet://categories?section=theme` | หัวข้อชุดตกแต่ง |
| `icouplet://categories?section=author` | ส่วนของผู้เขียน |
| `icouplet://categories?section=famous` | ส่วนบรรทัดที่มีชื่อเสียง |
| `icouplet://categories?section=corpus` | ชุดสะสม / คอร์ปัส |
| `icouplet://last-read` | คู่ที่อ่านล่าสุด |
| `icouplet://reading-history` | ประวัติการอ่าน |

## การตั้งค่าและคู่มือ

| URL | เปิด |
|-----|-------|
| `icouplet://settings` | ตั้งค่าราก |
| `icouplet://usage-guide` | คู่มือการใช้งาน |
| `icouplet://widget-guide` | คู่มือวิดเจ็ต |
| `icouplet://shortcuts-guide` | คู่มือทางลัด |
| `icouplet://feature-guide` | แสดงคุณสมบัติบนระบบอีกครั้ง |
| `icouplet://feedback` | อีเมลข้อเสนอแนะ |
| `icouplet://in-app-review` | รีวิวในแอป / App Store |

## ตัวอย่าง


```
icouplet://daily
icouplet://couplet?id=1
icouplet://recite?id=1
icouplet://search?q=春
icouplet://categories?section=famous
icouplet://widget-guide
```


ใช้เหล่านี้ในโปรแกรมปุ่มพิมพ์ลัด, การกระทําของหน้าจอส่วนตัวอย่างรวดเร็ว, วิดเจ็ต, หรือ Saveri ดูใน-apps ด้วย

</section>
<section lang="de" markdown="1">

iCouplet unterstützt ** `icouplet://` ** Shortcut Links (URL-Schema). Kaltstart- und Home Screen-Verknüpfungen werden über einen einheitlichen Puffer geliefert, so dass Links nach dem Onboarding nicht zweimal geöffnet werden.

## Linkformat


```
icouplet://{host}?{params}
```


## Couplets & Autoren

| URL | Öffnet |
|-----|-------|
| `icouplet://couplet?id={id}` | Einzelheiten der Kupplung |
| `icouplet://poem?id={id}` | Gleiches wie Couplet (Kompatibilitätsalias) |
| `icouplet://author?id={id}` | Angaben zum Autor (联家) |
| `icouplet://recite` | Recite Flow (Auto-Sprache, wenn möglich) |
| `icouplet://recite?id={id}` | Open Couplet und Auto-Recite |

## Entdecken

| URL | Öffnet |
|-----|-------|
| `icouplet://home` | Register „Start“ |
| `icouplet://daily` | Das heutige tägliche Paar |
| `icouplet://random` | Zufallspaar |
| `icouplet://favorites` | Favoriten |
| `icouplet://famous` | Berühmte Linienliste |
| `icouplet://search` | Suche |
| `icouplet://search?q={query}` | Suche mit Suchbegriff |
| `icouplet://study` | Studie / 对对子 Eintrag |
| `icouplet://categories` | Kategorien durchsuchen |
| `icouplet://categories?section=form` | Formular (体裁) Abschnitt |
| `icouplet://categories?section=theme` | Themenbereich |
| `icouplet://categories?section=author` | Autorenteil |
| `icouplet://categories?section=famous` | Berühmter Streckenabschnitt |
| `icouplet://categories?section=corpus` | Sammlungen/Corpus |
| `icouplet://last-read` | Zuletzt gelesenes Paar |
| `icouplet://reading-history` | Leseverlauf |

## Einstellungen & Anleitungen

| URL | Öffnet |
|-----|-------|
| `icouplet://settings` | Grundeinstellungen |
| `icouplet://usage-guide` | Nutzungsanleitung |
| `icouplet://widget-guide` | Widget-Anleitung |
| `icouplet://shortcuts-guide` | Kurzbefehle-Anleitung |
| `icouplet://feature-guide` | Wiedergabefunktion Onboarding |
| `icouplet://feedback` | Feedback-E-Mail |
| `icouplet://in-app-review` | In-App- / App-Store-Bewertung |

## Beispiele


```
icouplet://daily
icouplet://couplet?id=1
icouplet://recite?id=1
icouplet://search?q=春
icouplet://categories?section=famous
icouplet://widget-guide
```


Verwenden Sie diese in der Shortcuts-App, den Schnellaktionen für den Startbildschirm, den Widgets oder Safari. Siehe auch In-App **Settings → Shortcuts Guide**.

</section>
<section lang="fr" markdown="1">

iCouplet prend en charge les liens de raccourci ** `icouplet://` ** (schéma URL). Les raccourcis de démarrage à froid et d'écran d'accueil sont livrés via un tampon unifié de sorte que les liens ne sont pas ouverts deux fois après l'embarquement.

## Format de lien


```
icouplet://{host}?{params}
```


## Couplets & auteurs

| URL | Ouvre |
|-----|-------|
| `icouplet://couplet?id={id}` | Détail du couple |
| `icouplet://poem?id={id}` | Même chose que couplet (alias de compatibilité) |
| `icouplet://author?id={id}` | Description de l'auteur |
| `icouplet://recite` | Débit de récitation (parler automatiquement si possible) |
| `icouplet://recite?id={id}` | Ouvrir le couplet et la lecture automatique |

## Découverte

| URL | Ouvre |
|-----|-------|
| `icouplet://home` | Onglet Accueil |
| `icouplet://daily` | Aujourd'hui est le couplet quotidien |
| `icouplet://random` | Couplet aléatoire |
| `icouplet://favorites` | Favoris |
| `icouplet://famous` | Liste des lignes célèbres |
| `icouplet://search` | Recherche |
| `icouplet://search?q={query}` | Recherche avec requête |
| `icouplet://study` | Étude / Entrée |
| `icouplet://categories` | Parcourir les catégories |
| `icouplet://categories?section=form` | Section du formulaire |
| `icouplet://categories?section=theme` | Section thématique |
| `icouplet://categories?section=author` | Section d'auteur |
| `icouplet://categories?section=famous` | Section des lignes célèbres |
| `icouplet://categories?section=corpus` | Collections / corpus |
| `icouplet://last-read` | Dernière lecture couplet |
| `icouplet://reading-history` | Historique de lecture |

## Réglages et guides

| URL | Ouvre |
|-----|-------|
| `icouplet://settings` | Configuration racine |
| `icouplet://usage-guide` | Guide d'utilisation |
| `icouplet://widget-guide` | Guide des widgets |
| `icouplet://shortcuts-guide` | Guide Raccourcis |
| `icouplet://feature-guide` | Fonction de replay à bord |
| `icouplet://feedback` | E-mail de commentaires |
| `icouplet://in-app-review` | Avis in-app / App Store |

## Exemples


```
icouplet://daily
icouplet://couplet?id=1
icouplet://recite?id=1
icouplet://search?q=春
icouplet://categories?section=famous
icouplet://widget-guide
```


Utilisez-les dans l'application Raccourcis, les actions rapides Home Screen, les widgets ou Safari. Voir aussi dans l'application **Paramètres → Guide des raccourcis**.

</section>
<section lang="tr" markdown="1">

iCouplet ** `icouplet://` ** kısayol bağlantıları (URL planı). Soğuk başlangıç ve Ev Ekran kısayolları birleşik bir tampon aracılığıyla teslim edilir, bu yüzden bağlantılar gemiden sonra iki kez açılmaz.

## Bağlantı biçimi


```
icouplet://{host}?{params}
```


## Couplets & Yazarlar

| URL | Açar |
|-----|-------|
| `icouplet://couplet?id={id}` | Couplet detay |
| `icouplet://poem?id={id}` | Aynısı çift olarak |
| `icouplet://author?id={id}` | Yazar (联家) detay |
| `icouplet://recite` | Recite akışı (oto-speak mümkün olduğunda) |
| `icouplet://recite?id={id}` | Açık çift ve oto-recite |

## Keşfet

| URL | Açar |
|-----|-------|
| `icouplet://home` | Ana sayfa sekmesi |
| `icouplet://daily` | Bugünün Günlük Çiftleri |
| `icouplet://random` | Random çiftt |
| `icouplet://favorites` | Favoriler |
| `icouplet://famous` | Ünlü çizgi listesi listesi |
| `icouplet://search` | Ara |
| `icouplet://search?q={query}` | Sorgu ile arama |
| `icouplet://study` | Çalışma / 对对子 giriş |
| `icouplet://categories` | Göz kategoriler |
| `icouplet://categories?section=form` | Form (体裁) Bölüm |
| `icouplet://categories?section=theme` | Tema bölümü |
| `icouplet://categories?section=author` | Author section |
| `icouplet://categories?section=famous` | Ünlü çizgi bölüm |
| `icouplet://categories?section=corpus` | Koleksiyonlar / Korpus |
| `icouplet://last-read` | Son oku çiftt |
| `icouplet://reading-history` | Okuma geçmişi |

## Ayarlar ve kılavuzlar

| URL | Açar |
|-----|-------|
| `icouplet://settings` | Ayarlar |
| `icouplet://usage-guide` | Kullanım kılavuzu |
| `icouplet://widget-guide` | Widget kılavuzu |
| `icouplet://shortcuts-guide` | Kısayol kılavuzu |
| `icouplet://feature-guide` | Replay özelliği onboarding |
| `icouplet://feedback` | Geri bildirim e-postası |
| `icouplet://in-app-review` | Uygulama içi / App Store değerlendirme |

## Örnekler


```
icouplet://daily
icouplet://couplet?id=1
icouplet://recite?id=1
icouplet://search?q=春
icouplet://categories?section=famous
icouplet://widget-guide
```


Bunları kısa kesimlerde kullanın, Home Ekran hızlı eylemleri, widgets veya Safari. Ayrıca bakınız **Settings → Kısayollar Kılavuzu**.

</section>
