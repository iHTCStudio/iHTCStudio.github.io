---
layout: doc
title: iYijing — Shortcut Links
app_id: iYiJing
doc_title_en: Shortcut Links
doc_title_zh_cn: 快捷链接说明
doc_title_zh_tw: 快捷連結說明
description: iyijing:// deep links for iYijing — hexagram, daily, cast, study, hunt, Ten Wings, settings guides, and more.
---

<section lang="en" markdown="1">

iYijing supports **`iyijing://`** shortcut links (URL scheme). Cold start and Home Screen shortcuts are delivered through a unified buffer so links are not opened twice after onboarding.

## Link format

```
iyijing://{host}/{path}?{params}
```

## Hexagrams & discovery

| URL | Opens |
|-----|-------|
| `iyijing://home` | Home |
| `iyijing://daily` | Today’s Daily Hexagram |
| `iyijing://random` | Random hexagram |
| `iyijing://hexagram/{id}` | Hexagram detail (`gua/{id}` alias) |
| `iyijing://wing/{id}` | Ten Wings text (`yizhuan/{id}` alias) |
| `iyijing://trigram/{id}` | Trigram (`bagua/{id}` alias) |
| `iyijing://browse` | Browse |
| `iyijing://favorites` | Favorites |
| `iyijing://famous` | Famous lines |
| `iyijing://search` / `?q=` | Search |
| `iyijing://study` | Yijing Study |
| `iyijing://hunt` | Keyword hunt |
| `iyijing://divination` | Cultural casting (`qigua` / `cast`) |
| `iyijing://recite` / `recite/{id}` | Recitation |
| `iyijing://collection` | Hexagram list (`playlist` alias) |
| `iyijing://last-read` | Last read |
| `iyijing://reading-history` | Reading history |
| `iyijing://notes` | Notes |
| `iyijing://mastered` | Mastered |
| `iyijing://wrong-book` | Study wrong-book |
| `iyijing://recite-wrong` | Recite wrong-book |

## Settings & guides

| URL | Opens |
|-----|-------|
| `iyijing://settings` | Settings |
| `iyijing://usage-guide` | Usage guide |
| `iyijing://widget-guide` | Widget guide |
| `iyijing://shortcuts-guide` | Shortcuts guide |
| `iyijing://feature-guide` | Replay onboarding |
| `iyijing://feedback` | Feedback email |

## Examples

```
iyijing://daily
iyijing://hexagram/1
iyijing://wing/301
iyijing://divination
iyijing://study
iyijing://hunt
iyijing://famous
iyijing://search?q=乾
```

Use these in the Shortcuts app, Home Screen quick actions, widgets, Control Center, or Safari. See also in-app **Settings → Shortcuts Guide**.

</section>
<section lang="zh-CN" markdown="1">

爱周易支持 **`iyijing://`** 快捷链接（URL Scheme）。冷启动与主屏快捷经统一缓冲投递，避免引导后重复打开。

## 链接格式

```
iyijing://{host}/{path}?{params}
```

## 卦象与发现

| URL | 打开 |
|-----|------|
| `iyijing://home` | 首页 |
| `iyijing://daily` | 每日一卦 |
| `iyijing://random` | 随机 |
| `iyijing://hexagram/{id}` | 卦象详情（别名 `gua/{id}`） |
| `iyijing://wing/{id}` | 十翼（别名 `yizhuan/{id}`） |
| `iyijing://trigram/{id}` | 八卦（别名 `bagua/{id}`） |
| `iyijing://browse` | 分类 |
| `iyijing://favorites` | 收藏 |
| `iyijing://famous` | 名句 |
| `iyijing://search` / `?q=` | 搜索 |
| `iyijing://study` | 易学学堂 |
| `iyijing://hunt` | 识辞 |
| `iyijing://divination` | 文化起卦（`qigua` / `cast`） |
| `iyijing://recite` / `recite/{id}` | 诵读 |
| `iyijing://collection` | 卦单（别名 `playlist`） |
| `iyijing://last-read` | 上次阅读 |
| `iyijing://reading-history` | 浏览记录 |
| `iyijing://notes` | 笔记 |
| `iyijing://mastered` | 已精通 |
| `iyijing://wrong-book` | 错题本 |
| `iyijing://recite-wrong` | 诵读错题本 |

## 设置与教程

| URL | 打开 |
|-----|------|
| `iyijing://settings` | 设置 |
| `iyijing://usage-guide` | 使用说明 |
| `iyijing://widget-guide` | 小组件指南 |
| `iyijing://shortcuts-guide` | 快捷指南 |
| `iyijing://feature-guide` | 重播引导 |
| `iyijing://feedback` | 反馈邮件 |

## 示例

```
iyijing://daily
iyijing://hexagram/1
iyijing://wing/301
iyijing://divination
iyijing://study
iyijing://hunt
iyijing://famous
iyijing://search?q=乾
```

可在「快捷指令」、主屏快捷、小组件、控制中心或 Safari 中使用。也可查看应用内 **设置 → 快捷指南**。

</section>
<section lang="zh-TW" markdown="1">

愛周易支援 **`iyijing://`** 快捷連結（URL Scheme）。冷啟動與主畫面捷徑經統一緩衝投遞，避免引導後重複開啟。

## 連結格式

```
iyijing://{host}/{path}?{params}
```

## 卦象與發現

| URL | 開啟 |
|-----|------|
| `iyijing://home` | 首頁 |
| `iyijing://daily` | 每日一卦 |
| `iyijing://random` | 隨機 |
| `iyijing://hexagram/{id}` | 卦象詳情（別名 `gua/{id}`） |
| `iyijing://wing/{id}` | 十翼（別名 `yizhuan/{id}`） |
| `iyijing://trigram/{id}` | 八卦（別名 `bagua/{id}`） |
| `iyijing://browse` | 分類 |
| `iyijing://favorites` | 收藏 |
| `iyijing://famous` | 名句 |
| `iyijing://search` / `?q=` | 搜尋 |
| `iyijing://study` | 易學學堂 |
| `iyijing://hunt` | 識辭 |
| `iyijing://divination` | 文化起卦（`qigua` / `cast`） |
| `iyijing://recite` / `recite/{id}` | 誦讀 |
| `iyijing://collection` | 卦單（別名 `playlist`） |
| `iyijing://last-read` | 上次閱讀 |
| `iyijing://reading-history` | 瀏覽記錄 |
| `iyijing://notes` | 筆記 |
| `iyijing://mastered` | 已精通 |
| `iyijing://wrong-book` | 錯題本 |
| `iyijing://recite-wrong` | 誦讀錯題本 |

## 設定與教學

| URL | 開啟 |
|-----|------|
| `iyijing://settings` | 設定 |
| `iyijing://usage-guide` | 使用說明 |
| `iyijing://widget-guide` | 小工具指南 |
| `iyijing://shortcuts-guide` | 捷徑指南 |
| `iyijing://feature-guide` | 重播引導 |
| `iyijing://feedback` | 回饋郵件 |

## 範例

```
iyijing://daily
iyijing://hexagram/1
iyijing://wing/301
iyijing://divination
iyijing://study
iyijing://hunt
iyijing://famous
iyijing://search?q=乾
```

可在「捷徑」、主畫面捷徑、小工具、控制中心或 Safari 中使用。也可查看應用內 **設定 → 捷徑指南**。

</section>
<section lang="ja" markdown="1">

iYijingは** `iyijing://` **ショートカットリンク(URLスキーム)をサポートしています。 コールドスタートとホーム画面のショートカットは、統一されたバッファを介して配信されますので、リンクはオンボーディング後2回開いていません。

## リンク形式


```
iyijing://{host}/{path}?{params}
```


## ヘキサグラムと発見

| URL | 開く画面 |
|-----|-------|
| `iyijing://home` | ホーム |
| `iyijing://daily` | 今日の毎日のヘキサグラム |
| `iyijing://random` | ランダムヘキサグラム |
| `iyijing://hexagram/{id}` | ヘキサグラムの詳細(`グア/{id}`エイリアス) |
| `iyijing://wing/{id}` | テンウィングステキスト(`イジアン/{id}`エイリアス) |
| `iyijing://trigram/{id}` | トライグラム (`bagua/{id}` alias) |
| `iyijing://browse` | ブラウズ |
| `iyijing://favorites` | お気に入り |
| `iyijing://famous` | 名句一覧 |
| `iyijing://search` / `?q=` | 検索 |
| `iyijing://study` | イージング・スタディ |
| `iyijing://hunt` | キーワードハント |
| `iyijing://divination` | 文化キャスティング (`qigua`/`cast`) |
| `iyijing://recite` / `recite/{id}` | 新着情報 |
| `iyijing://collection` | ヘキサグラムリスト (`playlist` alias) |
| `iyijing://last-read` | 最後に読んだ項目 |
| `iyijing://reading-history` | 閲覧履歴 |
| `iyijing://notes` | ノート |
| `iyijing://mastered` | マスタード |
| `iyijing://wrong-book` | 間違った書籍を学ぶ |
| `iyijing://recite-wrong` | 間違った本を認めて下さい |

## 設定とガイド

| URL | 開く画面 |
|-----|-------|
| `iyijing://settings` | 設定 |
| `iyijing://usage-guide` | 使い方ガイド |
| `iyijing://widget-guide` | ウィジェットガイド |
| `iyijing://shortcuts-guide` | ショートカットガイド |
| `iyijing://feature-guide` | オンボーディングの再生 |
| `iyijing://feedback` | フィードバックメール |

## 例


```
iyijing://daily
iyijing://hexagram/1
iyijing://wing/301
iyijing://divination
iyijing://study
iyijing://hunt
iyijing://famous
iyijing://search?q=乾
```


これらをショートカットアプリ、ホーム画面のクイックアクション、ウィジェット、コントロールセンター、またはSafariで使用してください。 アプリ内設定 → ショートカットガイド** も参照してください。

</section>
<section lang="ko" markdown="1">

iYijing 지원 ** `iyijing://` ** 단축키 링크 (URL 계획). 콜드 시작 및 홈 화면 단축은 통합 버퍼를 통해 전달되므로 링크가 내장 된 후 두 번 열리지 않습니다.

## 링크 형식


```
iyijing://{host}/{path}?{params}
```


## Hexagrams 및 발견

| URL | 열리는 화면 |
|-----|-------|
| `iyijing://home` | 홈 |
| `iyijing://daily` | 오늘의 일일 Hexagram |
| `iyijing://random` | 무작위 6gram |
| `iyijing://hexagram/{id}` | Hexagram 세부 사항 (`gua/{id}`alias) |
| `iyijing://wing/{id}` | Ten Wings 텍스트 (`yizhuan/{id}`alias) |
| `iyijing://trigram/{id}` | 트리그램 (`bagua/{id}`alias) |
| `iyijing://browse` | 둘러보기 |
| `iyijing://favorites` | 즐겨찾기 |
| `iyijing://famous` | 명구 목록 |
| `iyijing://search` / `?q=` | 검색 |
| `iyijing://study` | Yijing 연구 |
| `iyijing://hunt` | 키워드 사냥 |
| `iyijing://divination` | 문화 주조 (`qigua`/`cast`) |
| `iyijing://recite` / `recite/{id}` | 견적 요청 |
| `iyijing://collection` | Hexagram 목록 (`playlist` 별칭) |
| `iyijing://last-read` | 마지막으로 읽은 항목 |
| `iyijing://reading-history` | 읽기 기록 |
| `iyijing://notes` | 메모 |
| `iyijing://mastered` | 인기있는 |
| `iyijing://wrong-book` | 연구 잘못된 책 |
| `iyijing://recite-wrong` | 잘못된 책 |

## 설정 및 가이드

| URL | 열리는 화면 |
|-----|-------|
| `iyijing://settings` | 설정 |
| `iyijing://usage-guide` | 사용 가이드 |
| `iyijing://widget-guide` | 위젯 가이드 |
| `iyijing://shortcuts-guide` | 단축어 가이드 |
| `iyijing://feature-guide` | 온보딩 다시 보기 |
| `iyijing://feedback` | 피드백 이메일 |

## 예시


```
iyijing://daily
iyijing://hexagram/1
iyijing://wing/301
iyijing://divination
iyijing://study
iyijing://hunt
iyijing://famous
iyijing://search?q=乾
```


Shortcuts 앱에서 이러한 사용, 홈 화면 빠른 행동, 위젯, 제어 센터, 또는 사파리. in-app**Settings → 단축키 가이드** 참조.

</section>
<section lang="ru" markdown="1">

iYijing поддерживает ярлыки ** `iyijing://` ** (схема URL). Холодный старт и ярлыки домашнего экрана доставляются через единый буфер, поэтому ссылки не открываются дважды после входа.

## Формат ссылки


```
iyijing://{host}/{path}?{params}
```


## Гексаграммы и открытия

| URL | Открывает |
|-----|-------|
| `iyijing://home` | Главная |
| `iyijing://daily` | Сегодняшняя ежедневная гексаграмма |
| `iyijing://random` | Случайная гексаграмма |
| `iyijing://hexagram/{id}` | Подробности гексаграммы ('gua/{id}' alias) |
| `iyijing://wing/{id}` | Ten Wings text ('yizhuan/{id}' alias) |
| `iyijing://trigram/{id}` | Триграмма ('bagua/{id}' alias) |
| `iyijing://browse` | Обзор |
| `iyijing://favorites` | Избранное |
| `iyijing://famous` | Знаменитые строки |
| `iyijing://search` / `?q=` | Поиск |
| `iyijing://study` | Ицзинское исследование |
| `iyijing://hunt` | Поиск ключевых слов |
| `iyijing://divination` | Культурный кастинг («цигуа» / «каст») |
| `iyijing://recite` / `recite/{id}` | декламация |
| `iyijing://collection` | Список гексаграмм ('playlist' alias) |
| `iyijing://last-read` | Последнее прочитанное |
| `iyijing://reading-history` | История чтения |
| `iyijing://notes` | Заметки |
| `iyijing://mastered` | мастеринг |
| `iyijing://wrong-book` | Неправильная книга |
| `iyijing://recite-wrong` | Неправильная книга |

## Настройки и руководства

| URL | Открывает |
|-----|-------|
| `iyijing://settings` | Настройки |
| `iyijing://usage-guide` | Руководство по использованию |
| `iyijing://widget-guide` | Руководство по виджетам |
| `iyijing://shortcuts-guide` | Руководство по «Командам» |
| `iyijing://feature-guide` | Повторное знакомство |
| `iyijing://feedback` | Письмо с отзывом |

## Примеры


```
iyijing://daily
iyijing://hexagram/1
iyijing://wing/301
iyijing://divination
iyijing://study
iyijing://hunt
iyijing://famous
iyijing://search?q=乾
```


Используйте их в приложении Shortcuts, быстрых действиях Home Screen, виджетах, Центре управления или Safari. См. также in-app **Settings → Shortcuts Guide**.

</section>
<section lang="th" markdown="1">

การรองรับ iYjuing ~ `iyijing://` BAR * ลิงก์ลัด (RUL scheme) การเริ่มหน้าจอหน้าจอเย็นและหน้าจอบ้าน จะถูกส่งไปผ่านระบบบัฟเฟอร์แบบรวม ดังนั้นลิงก์จึงไม่ถูกเปิดสองครั้งหลังจากขึ้นเครื่อง

## รูปแบบลิงก์


```
iyijing://{host}/{path}?{params}
```


## & ค้นพบ

| URL | เปิด |
|-----|-------|
| `iyijing://home` | หน้าแรก |
| `iyijing://daily` | วี ดิ ทัศน์ |
| `iyijing://random` | หมุน & 90 |
| `iyijing://hexagram/{id}` | รายละเอียด เฮกซาแกรม ('gua/ {iid) |
| `iyijing://wing/{id}` | ข้อความสิบปีก ('yzhuan/ {iid) |
| `iyijing://trigram/{id}` | Trigram ('bagua/{id) นามแฝง |
| `iyijing://browse` | เรียกดู |
| `iyijing://favorites` | รายการโปรด |
| `iyijing://famous` | บรรทัดขึ้นชื่อ |
| `iyijing://search` / `?q=` | ค้นหา |
| `iyijing://study` | การ ศึกษา |
| `iyijing://hunt` | ค้นหาคําค้น |
| `iyijing://divination` | นักแสดงทางวัฒนธรรม (อังกฤษ) |
| `iyijing://recite` / `recite/{id}` | การบันทึก |
| `iyijing://collection` | รายการ Hexagram ('playlist' name) |
| `iyijing://last-read` | รายการที่อ่านล่าสุด |
| `iyijing://reading-history` | ประวัติการอ่าน |
| `iyijing://notes` | บันทึก |
| `iyijing://mastered` | สําเร็จการศึกษาแล้ว |
| `iyijing://wrong-book` | การเรียนไม่ถูกต้อง |
| `iyijing://recite-wrong` | การอ่านผิดพลาด |

## การตั้งค่าและคู่มือ

| URL | เปิด |
|-----|-------|
| `iyijing://settings` | การตั้งค่า |
| `iyijing://usage-guide` | คู่มือการใช้งาน |
| `iyijing://widget-guide` | คู่มือวิดเจ็ต |
| `iyijing://shortcuts-guide` | คู่มือทางลัด |
| `iyijing://feature-guide` | เล่นทัวร์แนะนำอีกครั้ง |
| `iyijing://feedback` | อีเมลข้อเสนอแนะ |

## ตัวอย่าง


```
iyijing://daily
iyijing://hexagram/1
iyijing://wing/301
iyijing://divination
iyijing://study
iyijing://hunt
iyijing://famous
iyijing://search?q=乾
```


ใช้เหล่านี้ในโปรแกรมปุ่มพิมพ์ลัด, การกระทําของหน้าจอส่วนตัวอย่างรวดเร็ว, วิดเจ็ต, ศูนย์ควบคุม, หรือซาฟารี ดูใน-apps ด้วย

</section>
<section lang="de" markdown="1">

iYijing unterstützt ** `iyijing://` ** Shortcut Links (URL-Schema). Kaltstart- und Home Screen-Verknüpfungen werden über einen einheitlichen Puffer geliefert, so dass Links nach dem Onboarding nicht zweimal geöffnet werden.

## Linkformat


```
iyijing://{host}/{path}?{params}
```


## Hexagramme & Entdeckung

| URL | Öffnet |
|-----|-------|
| `iyijing://home` | Startseite |
| `iyijing://daily` | Das heutige tägliche Hexagramm |
| `iyijing://random` | Zufallshexagramm |
| `iyijing://hexagram/{id}` | Hexagrammdetail (`gua/{id}` alias) |
| `iyijing://wing/{id}` | Zehn Flügel (`yizhuan/{id}` alias) |
| `iyijing://trigram/{id}` | Trigram (`bagua/{id}alias) |
| `iyijing://browse` | Durchsuchen |
| `iyijing://favorites` | Favoriten |
| `iyijing://famous` | Berühmte Zeilen |
| `iyijing://search` / `?q=` | Suche |
| `iyijing://study` | Yijing-Studie |
| `iyijing://hunt` | Stichwortsuche |
| `iyijing://divination` | kulturelles Casting (`qigua` / `cast`) |
| `iyijing://recite` / `recite/{id}` | Rezitation |
| `iyijing://collection` | Hexagram-Liste („Playlist-Alias) |
| `iyijing://last-read` | Zuletzt gelesen |
| `iyijing://reading-history` | Leseverlauf |
| `iyijing://notes` | Notizen |
| `iyijing://mastered` | Beherrscht |
| `iyijing://wrong-book` | Studie falsches Buch |
| `iyijing://recite-wrong` | Falsches Buch rezitieren |

## Einstellungen & Anleitungen

| URL | Öffnet |
|-----|-------|
| `iyijing://settings` | Einstellungen |
| `iyijing://usage-guide` | Nutzungsanleitung |
| `iyijing://widget-guide` | Widget-Anleitung |
| `iyijing://shortcuts-guide` | Kurzbefehle-Anleitung |
| `iyijing://feature-guide` | Einführung erneut abspielen |
| `iyijing://feedback` | Feedback-E-Mail |

## Beispiele


```
iyijing://daily
iyijing://hexagram/1
iyijing://wing/301
iyijing://divination
iyijing://study
iyijing://hunt
iyijing://famous
iyijing://search?q=乾
```


Verwenden Sie diese in der Shortcuts-App, den Schnellaktionen für den Startbildschirm, den Widgets, dem Control Center oder Safari. Siehe auch In-App **Settings → Shortcuts Guide**.

</section>
<section lang="fr" markdown="1">

iYijing prend en charge les liens de raccourci ** `iyijing://` ** (schéma URL). Les raccourcis de démarrage à froid et d'écran d'accueil sont livrés via un tampon unifié de sorte que les liens ne sont pas ouverts deux fois après l'embarquement.

## Format de lien


```
iyijing://{host}/{path}?{params}
```


## Hexagrammes & découverte

| URL | Ouvre |
|-----|-------|
| `iyijing://home` | Accueil |
| `iyijing://daily` | Aujourd'hui hexagramme quotidien |
| `iyijing://random` | hexagramme aléatoire |
| `iyijing://hexagram/{id}` | Détail de l'hexagramme (alias «gua/{id}») |
| `iyijing://wing/{id}` | Texte de dix ailes (alizhuan/{id}` alias) |
| `iyijing://trigram/{id}` | Trigramme («bagua/{id}» alias) |
| `iyijing://browse` | Parcourir |
| `iyijing://favorites` | Favoris |
| `iyijing://famous` | Vers célèbres |
| `iyijing://search` / `?q=` | Recherche |
| `iyijing://study` | Étude de Yijing |
| `iyijing://hunt` | Chasse par mots clés |
| `iyijing://divination` | Casting culturel (qigua) |
| `iyijing://recite` / `recite/{id}` | Récitation |
| `iyijing://collection` | Liste des hexagrammes (alias « playlist ») |
| `iyijing://last-read` | Dernière lecture |
| `iyijing://reading-history` | Historique de lecture |
| `iyijing://notes` | Notes |
| `iyijing://mastered` | Maîtrise |
| `iyijing://wrong-book` | Étudier le mauvais livre |
| `iyijing://recite-wrong` | Réciter le mauvais livre |

## Réglages et guides

| URL | Ouvre |
|-----|-------|
| `iyijing://settings` | Réglages |
| `iyijing://usage-guide` | Guide d'utilisation |
| `iyijing://widget-guide` | Guide des widgets |
| `iyijing://shortcuts-guide` | Guide Raccourcis |
| `iyijing://feature-guide` | Rejouer l’accueil |
| `iyijing://feedback` | E-mail de commentaires |

## Exemples


```
iyijing://daily
iyijing://hexagram/1
iyijing://wing/301
iyijing://divination
iyijing://study
iyijing://hunt
iyijing://famous
iyijing://search?q=乾
```


Utilisez-les dans l'application Raccourcis, Actions rapides Home Screen, Widgets, Control Center ou Safari. Voir aussi dans l'application **Paramètres → Guide des raccourcis**.

</section>
<section lang="tr" markdown="1">

iYijing, ** `iyijing://` ** kısayol bağlantıları (URL planı). Soğuk başlangıç ve Ev Ekran kısayolları birleşik bir tampon aracılığıyla teslim edilir, bu yüzden bağlantılar gemiden sonra iki kez açılmaz.

## Bağlantı biçimi


```
iyijing://{host}/{path}?{params}
```


## Hexagrams & keşif

| URL | Açar |
|-----|-------|
| `iyijing://home` | Ana sayfa |
| `iyijing://daily` | Bugünün Günlük Hexagram |
| `iyijing://random` | Random hexagram |
| `iyijing://hexagram/{id}` | Hexagram detay ('gua/{id}' alias) |
| `iyijing://wing/{id}` | Ten Wings text ('yizhuan/{id} alias) |
| `iyijing://trigram/{id}` | Trigram ('bagua/{id}' alias) |
| `iyijing://browse` | Gözat |
| `iyijing://favorites` | Favoriler |
| `iyijing://famous` | Ünlü dizeler |
| `iyijing://search` / `?q=` | Ara |
| `iyijing://study` | Yijing Study |
| `iyijing://hunt` | Anahtar Kelime avı avlanma |
| `iyijing://divination` | Kültürel döküm ('qigua' / 'cast') |
| `iyijing://recite` / `recite/{id}` | Recitation |
| `iyijing://collection` | Hexagram listesi ('playlist' alias) |
| `iyijing://last-read` | Son okunan |
| `iyijing://reading-history` | Okuma geçmişi |
| `iyijing://notes` | Notlar |
| `iyijing://mastered` | Mastered |
| `iyijing://wrong-book` | Yanlış-kitap Çalışması |
| `iyijing://recite-wrong` | Yanlış kitap |

## Ayarlar ve kılavuzlar

| URL | Açar |
|-----|-------|
| `iyijing://settings` | Ayarlar |
| `iyijing://usage-guide` | Kullanım kılavuzu |
| `iyijing://widget-guide` | Widget kılavuzu |
| `iyijing://shortcuts-guide` | Kısayol kılavuzu |
| `iyijing://feature-guide` | Tanıtımı yeniden oynat |
| `iyijing://feedback` | Geri bildirim e-postası |

## Örnekler


```
iyijing://daily
iyijing://hexagram/1
iyijing://wing/301
iyijing://divination
iyijing://study
iyijing://hunt
iyijing://famous
iyijing://search?q=乾
```


Bunları kısa kesimlerde kullanın, Home Ekran hızlı eylemleri, widgets, Control Center veya Safari. Ayrıca bakınız **Settings → Kısayollar Kılavuzu**.

</section>
