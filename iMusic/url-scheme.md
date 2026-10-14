---
layout: doc
title: iMusic — Shortcut Links
app_id: iMusic
doc_title_en: Shortcut Links
doc_title_zh_cn: 快捷链接说明
doc_title_zh_tw: 快捷連結說明
description: imusic:// deep links for iMusic — piece, daily, play, recognize, artists, collections, mood, settings guides, and more.
---

<section lang="en" markdown="1">

iMusic supports **`imusic://`** shortcut links. Cold start and Home Screen shortcuts go through a unified buffer so a link is not opened twice after onboarding.

## Link format

```
imusic://{host}?{params}
```

Scheme is **`imusic`** only.

## Home & today

| URL | Opens |
|-----|-------|
| `imusic://` / `imusic://home` | Home |
| `imusic://daily` / `imusic://today` | Daily Piece (queue is this track only) |
| `imusic://random` | Roam (whole-library shuffle) |
| `imusic://play` | Play |
| `imusic://last` / `imusic://lastheard` | Last heard |

## Pieces & artists

| URL | Opens |
|-----|-------|
| `imusic://piece?id={id}` | Piece guide (`passage` / `song` also accepted) |
| `imusic://artist?id={id}` / `imusic://artist?name={name}` | Artist desk |
| `imusic://artists` / `imusic://singers` | Artist directory |
| `imusic://famous` / `imusic://lines` | Famous lines |

A share-card footer may add `name=` (title · artist) for humans. Matching still uses **`id` only**.

## Browse, search & listen

| URL | Opens |
|-----|-------|
| `imusic://categories` / `imusic://browse` | Browse (`section=catalog` / `all` / `allpieces` → All Pieces) |
| `imusic://collection?id={id}` | Collection (`id=col-all` is the virtual All Pieces list) |
| `imusic://search` / `imusic://search?q={query}` | Search |
| `imusic://favorites` | Favorites |
| `imusic://later` | Favorites, scrolled to Later |
| `imusic://lists` / `imusic://listenlists` | Listen lists |
| `imusic://history` | History |
| `imusic://notes` | Notes |
| `imusic://mastered` | Finished |
| `imusic://streak` / `imusic://footprint` | Streak |

Opening a single piece, the mini bar, or Song ID **resets** the reading queue to that piece. Opening from a collection, search, or artist keeps that list so Next / Previous stay available.

## Song ID, school & mood

| URL | Opens |
|-----|-------|
| `imusic://recognize` / `imusic://shazam` | Song ID |
| `imusic://school` / `imusic://earschool` | Ear school |
| `imusic://timeline` / `imusic://corridor` | Era corridor |
| `imusic://compare` | Compare listening |
| `imusic://mood?id={id}` | Start that mood (`piece=` / `pieceId=` is the starting track only; the mood still matches `id`) |

## Settings & guides

| URL | Opens |
|-----|-------|
| `imusic://settings` | Settings |
| `imusic://usageguide` / `imusic://featureguide` | Usage / feature guide |
| `imusic://widgetguide` | Widget guide |
| `imusic://shortcutsguide` | Shortcuts guide |
| `imusic://feedback` | Feedback |
| `imusic://review` / `imusic://in-app-review` | In-app review (when the store listing is live) |

## Siri & Home Screen

Ask Siri for today’s piece, roam, search, or favorites after you add shortcuts. Configure Home Screen quick actions in **Settings → Shortcuts**. Full examples live in the in-app Shortcuts guide.

[FAQ](../faq) · [Privacy Policy](../privacy) · [Support](../)

</section>
<section lang="zh-CN" markdown="1">

爱音乐支持 **`imusic://`** 快捷链接。冷启动与主屏快捷会走统一缓冲，避免引导结束后同一条链接打开两次。

## 链接格式

```
imusic://{host}?{params}
```

Scheme **只接受** `imusic`。

## 首页与今日

| URL | 打开 |
|-----|------|
| `imusic://` / `imusic://home` | 首页 |
| `imusic://daily` / `imusic://today` | 今日一乐（阅读队列只含这一首） |
| `imusic://random` | 漫游（整库随机） |
| `imusic://play` | 播放 |
| `imusic://last` / `imusic://lastheard` | 最近在听 |

## 曲目与歌手

| URL | 打开 |
|-----|------|
| `imusic://piece?id={id}` | 赏析（也接受 `passage` / `song`） |
| `imusic://artist?id={id}` / `imusic://artist?name={name}` | 歌手志 |
| `imusic://artists` / `imusic://singers` | 歌手目录 |
| `imusic://famous` / `imusic://lines` | 名句 |

乐卡脚注可带 `name=`（曲名 · 艺人）给人读。匹配**只认 `id`**。

## 浏览、搜索与听单

| URL | 打开 |
|-----|------|
| `imusic://categories` / `imusic://browse` | 分类（`section=catalog` / `all` / `allpieces` → 全部曲目） |
| `imusic://collection?id={id}` | 合集（`id=col-all` 为虚拟全部曲目） |
| `imusic://search` / `imusic://search?q={query}` | 搜索 |
| `imusic://favorites` | 收藏 |
| `imusic://later` | 收藏并滚到稍后听 |
| `imusic://lists` / `imusic://listenlists` | 听单 |
| `imusic://history` | 历史 |
| `imusic://notes` | 笔记 |
| `imusic://mastered` | 已听完 |
| `imusic://streak` / `imusic://footprint` | 打卡 |

打开单曲、迷你条或识曲时，阅读队列会**重置**为这一首。从合集、搜索或歌手作品进入则保留该列表，赏析页可上一首 / 下一首。

## 识曲、小学与心情

| URL | 打开 |
|-----|------|
| `imusic://recognize` / `imusic://shazam` | 听歌识曲 |
| `imusic://school` / `imusic://earschool` | 听音小学 |
| `imusic://timeline` / `imusic://corridor` | 年代走廊 |
| `imusic://compare` | 对比听 |
| `imusic://mood?id={id}` | 从该心情起播（`piece=` 只作起点，匹配心情仍只读 `id`） |

## 设置与教程

| URL | 打开 |
|-----|------|
| `imusic://settings` | 设置 |
| `imusic://usageguide` / `imusic://featureguide` | 使用 / 功能引导 |
| `imusic://widgetguide` | 小组件指南 |
| `imusic://shortcutsguide` | 快捷指南 |
| `imusic://feedback` | 反馈 |
| `imusic://review` / `imusic://in-app-review` | 应用内评价（商店上架后） |

## Siri 与主屏

添加快捷指令后，可对 Siri 说今日一乐、漫游、搜索或收藏。主屏长按快捷在 **设置 → 快捷** 配置。完整示例见应用内快捷指南。

[常见问题](../faq) · [隐私政策](../privacy) · [支持页](../)

</section>
<section lang="zh-TW" markdown="1">

愛音樂支援 **`imusic://`** 快捷連結。冷啟動與主畫面捷徑會走統一緩衝，避免引導結束後同一條連結打開兩次。

## 連結格式

```
imusic://{host}?{params}
```

Scheme **只接受** `imusic`。

## 首頁與今日

| URL | 打開 |
|-----|------|
| `imusic://` / `imusic://home` | 首頁 |
| `imusic://daily` / `imusic://today` | 今日一樂（閱讀佇列只含這一首） |
| `imusic://random` | 漫遊（整庫隨機） |
| `imusic://play` | 播放 |
| `imusic://last` / `imusic://lastheard` | 最近在聽 |

## 曲目與歌手

| URL | 打開 |
|-----|------|
| `imusic://piece?id={id}` | 賞析（也接受 `passage` / `song`） |
| `imusic://artist?id={id}` / `imusic://artist?name={name}` | 歌手誌 |
| `imusic://artists` / `imusic://singers` | 歌手目錄 |
| `imusic://famous` / `imusic://lines` | 名句 |

樂卡腳註可帶 `name=`（曲名 · 藝人）給人讀。匹配**只認 `id`**。

## 瀏覽、搜尋與聽單

| URL | 打開 |
|-----|------|
| `imusic://categories` / `imusic://browse` | 分類（`section=catalog` / `all` / `allpieces` → 全部曲目） |
| `imusic://collection?id={id}` | 合集（`id=col-all` 為虛擬全部曲目） |
| `imusic://search` / `imusic://search?q={query}` | 搜尋 |
| `imusic://favorites` | 收藏 |
| `imusic://later` | 收藏並滾到稍後聽 |
| `imusic://lists` / `imusic://listenlists` | 聽單 |
| `imusic://history` | 歷史 |
| `imusic://notes` | 筆記 |
| `imusic://mastered` | 已聽完 |
| `imusic://streak` / `imusic://footprint` | 打卡 |

打開單曲、迷你條或識曲時，閱讀佇列會**重置**為這一首。從合集、搜尋或歌手作品進入則保留該列表，賞析頁可上一首 / 下一首。

## 識曲、小學與心情

| URL | 打開 |
|-----|------|
| `imusic://recognize` / `imusic://shazam` | 聽歌識曲 |
| `imusic://school` / `imusic://earschool` | 聽音小學 |
| `imusic://timeline` / `imusic://corridor` | 年代走廊 |
| `imusic://compare` | 對比聽 |
| `imusic://mood?id={id}` | 從該心情起播（`piece=` 只作起點，匹配心情仍只讀 `id`） |

## 設定與教學

| URL | 打開 |
|-----|------|
| `imusic://settings` | 設定 |
| `imusic://usageguide` / `imusic://featureguide` | 使用 / 功能引導 |
| `imusic://widgetguide` | 小工具指南 |
| `imusic://shortcutsguide` | 捷徑指南 |
| `imusic://feedback` | 回饋 |
| `imusic://review` / `imusic://in-app-review` | 應用內評價（商店上架後） |

## Siri 與主畫面

加入捷徑後，可對 Siri 說今日一樂、漫遊、搜尋或收藏。主畫面長按捷徑在 **設定 → 快捷** 設定。完整示例見應用內捷徑指南。

[常見問題](../faq) · [隱私政策](../privacy) · [支援頁](../)

</section>
<section lang="ja" markdown="1">

iMusicは** `imusic://` **のショートカットリンクをサポートしています。 コールドスタートとホーム画面のショートカットは、統一されたバッファを通過するので、オンボーディング後にリンクが2回開くことはありません。

## リンク形式


```
imusic://{host}?{params}
```


スキームは** `imusic://` **のみです。

## ホーム&今日

| URL | 開く画面 |
|-----|-------|
| `imusic://` / `imusic://home` | ホーム |
| `imusic://daily` / `imusic://today` | デイリーピース(キューのみ) |
| `imusic://random` | ローム(全ライブラリシャッフル) |
| `imusic://play` | プレイ |
| `imusic://last` / `imusic://lastheard` | 最後に聞いて |

## ピース&アーティスト

| URL | 開く画面 |
|-----|-------|
| `imusic://piece?id={id}` | ピースガイド(「パッセージ」/「ソン」も可) |
| `imusic://artist?id={id}` / `imusic://artist?name={name}` | アーティストデスク |
| `imusic://artists` / `imusic://singers` | アーティストディレクトリ |
| `imusic://famous` / `imusic://lines` | 名句一覧 |

共有カードのフッターは、人のために `imusic://` (タイトル・アーティスト) を追加することができます。 マッチはまだ使用しています** `imusic` のみ**。

## ブラウズ、検索&リスニング

| URL | 開く画面 |
|-----|-------|
| `imusic://categories` / `imusic://browse` | 参照(`section=catalog`/`all`/`allpieces` → All Pieces) |
| `imusic://collection?id={id}` | コレクション (`id=col-all` は仮想オールピースリストです) |
| `imusic://search` / `imusic://search?q={query}` | 検索 |
| `imusic://favorites` | お気に入り |
| `imusic://later` | お気に入り、後でスクロール |
| `imusic://lists` / `imusic://listenlists` | リストを聴く |
| `imusic://history` | プロフィール |
| `imusic://notes` | ノート |
| `imusic://mastered` | 仕上げ |
| `imusic://streak` / `imusic://footprint` | ストール |

シングルピース、ミニバー、またはソング ID **resets** をその部分に読み込みます。 コレクション、検索、またはアーティストがそのリストを保持するので、次/前の滞在が利用可能になります。

## ソングID、学校&気分

| URL | 開く画面 |
|-----|-------|
| `imusic://recognize` / `imusic://shazam` | ソングID |
| `imusic://school` / `imusic://earschool` | イヤースクール |
| `imusic://timeline` / `imusic://corridor` | Eraの廊下 |
| `imusic://compare` | リスニングの比較 |
| `imusic://mood?id={id}` | 気分が始まります(`piece=`/`pieceId=` はスタートトラックのみです。気分は`id` と一致します) |

## 設定とガイド

| URL | 開く画面 |
|-----|-------|
| `imusic://settings` | 設定 |
| `imusic://usageguide` / `imusic://featureguide` | 使用法/特徴ガイド |
| `imusic://widgetguide` | ウィジェットガイド |
| `imusic://shortcutsguide` | ショートカットガイド |
| `imusic://feedback` | フィードバック |
| `imusic://review` / `imusic://in-app-review` | アプリ内レビュー(店舗リストがライブの場合) |

## シリとホーム画面

ショートカットを追加すると、今日のピース、ローム、検索、またはお気に入りを Siri に尋ねます。 **Settings → Shortcuts** でホーム画面のクイックアクションを設定します。 アプリ内ショートカットガイドにフルサンプルが搭載されています。

[FAQ](../faq)・[プライバシーポリシー](../privacy)・[サポート](./)

</section>
<section lang="ko" markdown="1">

iMusic 지원 ** `imusic://` ** 단축 링크. 콜드 시작 및 홈 화면 단축은 통합 버퍼를 통해 이동하므로 링크는 내장 후 두 번 열 수 없습니다.

## 링크 형식


```
imusic://{host}?{params}
```


Scheme은 ** `imusic://` **만 있습니다.

## 홈 & 오늘

| URL | 열리는 화면 |
|-----|-------|
| `imusic://` / `imusic://home` | 홈 |
| `imusic://daily` / `imusic://today` | 매일 조각 (쿼이 트랙 만) |
| `imusic://random` | Roam (전체 리브 shuffle) |
| `imusic://play` | 이름 * |
| `imusic://last` / `imusic://lastheard` | 마지막 듣기 |

## 조각 & 예술가

| URL | 열리는 화면 |
|-----|-------|
| `imusic://piece?id={id}` | 조각 가이드 (`passage` / `song`도 허용) |
| `imusic://artist?id={id}` / `imusic://artist?name={name}` | 아티스트 데스크 |
| `imusic://artists` / `imusic://singers` | 비밀번호 |
| `imusic://famous` / `imusic://lines` | 명구 목록 |

공유 카드 발러 추가 할 수 있습니다 `imusic://` (제목 · 작가) 인간의. 일치는 여전히 사용 ** `imusic` 만 **.

## 검색 및 듣기

| URL | 열리는 화면 |
|-----|-------|
| `imusic://categories` / `imusic://browse` | 검색 (`section=catalog`/`all`/`allpieces`→ 모든 조각) |
| `imusic://collection?id={id}` | 컬렉션 (`id=col-all`는 가상 모든 조각 목록입니다) |
| `imusic://search` / `imusic://search?q={query}` | 검색 |
| `imusic://favorites` | 즐겨찾기 |
| `imusic://later` | 즐겨찾기, 나중에 스크롤 |
| `imusic://lists` / `imusic://listenlists` | 자주 묻는 질문 |
| `imusic://history` | - 연혁 |
| `imusic://notes` | 메모 |
| `imusic://mastered` | 끝마친 |
| `imusic://streak` / `imusic://footprint` | 사이트맵 |

단일 조각, 미니 바, 또는 노래 ID ** 설정 ** 그 조각에 대한 독서 큐. 수집, 검색, 또는 예술가에서 열기는 다음 목록을 유지 / 이전 숙박 가능.

## 노래 ID, 학교 및 분위기

| URL | 열리는 화면 |
|-----|-------|
| `imusic://recognize` / `imusic://shazam` | 송 ID |
| `imusic://school` / `imusic://earschool` | 귀 학교 |
| `imusic://timeline` / `imusic://corridor` | Era 복도 |
| `imusic://compare` | 듣기 비교 |
| `imusic://mood?id={id}` | 그 기분을 시작하십시오 (`piece=` / `pieceId=`는 시작 트랙 만입니다. 기분은 여전히 `id`) |

## 설정 및 가이드

| URL | 열리는 화면 |
|-----|-------|
| `imusic://settings` | 설정 |
| `imusic://usageguide` / `imusic://featureguide` | 사용법/기능 가이드 |
| `imusic://widgetguide` | 위젯 가이드 |
| `imusic://shortcutsguide` | 단축어 가이드 |
| `imusic://feedback` | 이름 * |
| `imusic://review` / `imusic://in-app-review` | In-app review (점포 목록이 생길 때) |

## Siri & 홈 화면

오늘 조각, roam, 검색, 또는 당신이 단축키를 추가 한 후 즐겨 찾기에 대한 Siri에 문의하십시오. 홈 화면을 구성 ** 설정 → 단축키 **. 전체 예제 in-app Shortcuts 가이드에서 라이브.

[FAQ](../faq) · [개인정보 보호 정책](../privacy) · [지원](../)

</section>
<section lang="ru" markdown="1">

iMusic поддерживает ярлыки ** `imusic://` **. Холодный старт и ярлыки Home Screen проходят через единый буфер, поэтому ссылка не открывается дважды после входа.

## Формат ссылки


```
imusic://{host}?{params}
```


Схема ** `imusic://` **.

## Home и сегодня

| URL | Открывает |
|-----|-------|
| `imusic://` / `imusic://home` | Главная |
| `imusic://daily` / `imusic://today` | Daily Piece (только этот трек) |
| `imusic://random` | Roam (полная перетасовка библиотек) |
| `imusic://play` | Играть |
| `imusic://last` / `imusic://lastheard` | Последнее слово |

## Исполнитель: Pieces & Artists

| URL | Открывает |
|-----|-------|
| `imusic://piece?id={id}` | Piece Guide («Переход» / «Песня» также принимается) |
| `imusic://artist?id={id}` / `imusic://artist?name={name}` | Рабочий стол |
| `imusic://artists` / `imusic://singers` | Художественный справочник |
| `imusic://famous` / `imusic://lines` | Знаменитые строки |

Нижний колонтитул может добавить `imusic://` (название художника) для людей. Матч по-прежнему использует ** `imusic` только **.

## Просмотр, поиск и прослушивание

| URL | Открывает |
|-----|-------|
| `imusic://categories` / `imusic://browse` | Browse ('section=catalog' / 'all' / 'allpieces' → All Pieces) |
| `imusic://collection?id={id}` | «id=col-all» — это виртуальный список «All Pieces». |
| `imusic://search` / `imusic://search?q={query}` | Поиск |
| `imusic://favorites` | Избранное |
| `imusic://later` | Любимые, прокрученные позже |
| `imusic://lists` / `imusic://listenlists` | Слушайте списки |
| `imusic://history` | История |
| `imusic://notes` | Заметки |
| `imusic://mastered` | Закончено |
| `imusic://streak` / `imusic://footprint` | полоса |

Открывая один кусок, мини-бар или идентификатор песни ** сбрасывает ** очередь чтения на этот кусок. Открытие из коллекции, поиска или художника сохраняет этот список таким образом, чтобы оставаться доступным.

## Песня ID, школа и настроение

| URL | Открывает |
|-----|-------|
| `imusic://recognize` / `imusic://shazam` | Песня ID |
| `imusic://school` / `imusic://earschool` | Ушная школа |
| `imusic://timeline` / `imusic://corridor` | Коридор эпохи |
| `imusic://compare` | Сравните прослушивание |
| `imusic://mood?id={id}` | Начните это настроение ('piece=' / 'pieceId=' - это только стартовый трек; настроение все еще соответствует 'id'). |

## Настройки и руководства

| URL | Открывает |
|-----|-------|
| `imusic://settings` | Настройки |
| `imusic://usageguide` / `imusic://featureguide` | Использование / Feature Guide |
| `imusic://widgetguide` | Руководство по виджетам |
| `imusic://shortcutsguide` | Руководство по «Командам» |
| `imusic://feedback` | обратная связь |
| `imusic://review` / `imusic://in-app-review` | Обзор в приложении (когда листинг магазина вживую) |

## Siri и домашний экран

Спросите Siri о сегодняшнем продукте, роуминге, поиске или фаворитах после добавления ярлыков. Настройте быстрые действия на домашнем экране в ** Настройки → Ярлыки **. Полные примеры живут в руководстве по ярлыкам в приложении.

[FAQ] (../faq) · [Политика конфиденциальности] (../privacy) · [Поддержка] (../)

</section>
<section lang="th" markdown="1">

iMusic รองรับ} `imusic://` BAR ลิงก์ลัด เริ่มต้นแบบเย็นและแสดงทางลัดหน้าจอบ้าน ผ่านการรวมกันของบัฟเฟอร์ ดังนั้นการเชื่อมโยงจึงไม่ถูกเปิดสองครั้งหลังจากขึ้นเครื่อง

## รูปแบบลิงก์


```
imusic://{host}?{params}
```


ชุดสีคือ ~ BAR `imusic://` BAR เท่านั้น

## ส่วนตัวและวันนี้

| URL | เปิด |
|-----|-------|
| `imusic://` / `imusic://home` | หน้าแรก |
| `imusic://daily` / `imusic://today` | Daily Bart (เป็นเพลงของเพลงเท่านั้น) |
| `imusic://random` | รอม (ใคร) |
| `imusic://play` | เล่น |
| `imusic://last` / `imusic://lastheard` | ได้ยินครั้งสุดท้าย |

## ชิ้นส่วนและศิลปิน

| URL | เปิด |
|-----|-------|
| `imusic://piece?id={id}` | ไกด์ชิ้น ('passage' / 'song' ก็ตอบรับด้วย) |
| `imusic://artist?id={id}` / `imusic://artist?name={name}` | โต๊ะศิลปิน |
| `imusic://artists` / `imusic://singers` | ไดเรกทอรีศิลปิน |
| `imusic://famous` / `imusic://lines` | บรรทัดขึ้นชื่อ |

เครื่องวางไพ่ร่วมอาจเพิ่ม c0     (ชื่อศิลปิน) สําหรับมนุษย์ การจับคู่ยังคงใช้~ `imusic` BAR อย่างเดียว ~

## เรียกดู, ค้นหาและรับฟัง

| URL | เปิด |
|-----|-------|
| `imusic://categories` / `imusic://browse` | เรียกดู (รายการ) |
| `imusic://collection?id={id}` | ชุดสะสม ('id=colall' is the return all bits list) |
| `imusic://search` / `imusic://search?q={query}` | ค้นหา |
| `imusic://favorites` | รายการโปรด |
| `imusic://later` | รายการโปรด, เลื่อนไปทีหลัง |
| `imusic://lists` / `imusic://listenlists` | ชื่อรายการ: |
| `imusic://history` | ประวัติ |
| `imusic://notes` | บันทึก |
| `imusic://mastered` | เรียบร้อยแล้ว |
| `imusic://streak` / `imusic://footprint` | สไตรก |

เปิดชิ้นเดียว, มินิบาร์, หรือ ID ของเพลง ~ ลําดับการอ่านคิวของชิ้นส่วนนั้น การเปิดจากชุดสะสม, สืบค้น หรือศิลปิน จะคงรายการดังกล่าวไว้ต่อไปและก่อนหน้าจะยังคงอยู่

## หมายเลขเพลง, อารมณ์ของโรงเรียน

| URL | เปิด |
|-----|-------|
| `imusic://recognize` / `imusic://shazam` | หมายเลขเพลง |
| `imusic://school` / `imusic://earschool` | โรงเรียนหู |
| `imusic://timeline` / `imusic://corridor` | เส้นพริ้วไหว |
| `imusic://compare` | เปรียบ เทียบ การ ฟัง |
| `imusic://mood?id={id}` | เริ่มที่อารมณ์ ('part=' / 'partid=' เป็นร่องเริ่มต้นเท่านั้น; อารมณ์ยังคงตรงกับ 'id') |

## การตั้งค่าและคู่มือ

| URL | เปิด |
|-----|-------|
| `imusic://settings` | การตั้งค่า |
| `imusic://usageguide` / `imusic://featureguide` | คํา แนะ นํา ที่ ใช้ ได้ จริง |
| `imusic://widgetguide` | คู่มือวิดเจ็ต |
| `imusic://shortcutsguide` | คู่มือทางลัด |
| `imusic://feedback` | แหล่งป้อน |
| `imusic://review` / `imusic://in-app-review` | In-app review (เมื่อรายการร้านค้าสด) |

## หน้าจอส่วนตัว

จง ถาม ซีรี สําหรับ งาน ประจํา วัน, การ ท่อง เที่ยว, การ ค้น หา, หรือ สิ่ง ที่ คุณ ชอบ หลัง จาก คุณ เพิ่ม ทางลัด. ปรับแต่งการกระทําอย่างรวดเร็วของหน้าจอส่วนตัวใน~. ตั้งค่าปุ่มพิมพ์ลัด~ ตัวอย่างเต็มรูปแบบ อาศัยอยู่ในคู่มือทางลัด

[FAQ](./faq). สืบค้นเมื่อ 20 พฤษภาคม พ.ศ.

</section>
<section lang="de" markdown="1">

iMusic unterstützt ** `imusic://` ** Shortcut Links. Kaltstart und Home Screen Shortcuts durchlaufen einen einheitlichen Puffer, so dass ein Link nicht zweimal nach dem Onboarding geöffnet wird.

## Linkformat


```
imusic://{host}?{params}
```


Schema ist nur ** `imusic://` **.

## Home & Heute

| URL | Öffnet |
|-----|-------|
| `imusic://` / `imusic://home` | Startseite |
| `imusic://daily` / `imusic://today` | Daily Piece (Warteschlange ist nur dieser Track) |
| `imusic://random` | Roam (Ganzbibliothek shuffle) |
| `imusic://play` | Spiel |
| `imusic://last` / `imusic://lastheard` | Zuletzt gehört |

## Stücke und Künstler

| URL | Öffnet |
|-----|-------|
| `imusic://piece?id={id}` | Piece Guide (`passage` / `song` auch akzeptiert) |
| `imusic://artist?id={id}` / `imusic://artist?name={name}` | Artist Desk |
| `imusic://artists` / `imusic://singers` | Künstlerverzeichnis |
| `imusic://famous` / `imusic://lines` | Berühmte Zeilen |

Eine Share-Card-Fußzeile kann `imusic://` (Titel · Künstler) für Menschen hinzufügen. Matching verwendet immer noch nur ** `imusic` **.

## Browsen, Suchen & Hören

| URL | Öffnet |
|-----|-------|
| `imusic://categories` / `imusic://browse` | Browse (`section=catalog` / `all` / `allpieces` → All Pieces) |
| `imusic://collection?id={id}` | Collection (`id=col-all` ist die virtuelle All Pieces Liste) |
| `imusic://search` / `imusic://search?q={query}` | Suche |
| `imusic://favorites` | Favoriten |
| `imusic://later` | Favoriten, gescrollt nach Später |
| `imusic://lists` / `imusic://listenlists` | Listenlisten |
| `imusic://history` | Geschichte |
| `imusic://notes` | Notizen |
| `imusic://mastered` | fertig |
| `imusic://streak` / `imusic://footprint` | Streifen |

Das Öffnen eines einzelnen Stücks, der Minibar oder der Song ID setzt die Lesewarteschlange auf dieses Stück zurück. Das Öffnen aus einer Sammlung, einer Suche oder einem Künstler führt diese Liste, sodass Next / Previous verfügbar bleibt.

## Song ID, Schule & Stimmung

| URL | Öffnet |
|-----|-------|
| `imusic://recognize` / `imusic://shazam` | Song ID |
| `imusic://school` / `imusic://earschool` | Ohrschule |
| `imusic://timeline` / `imusic://corridor` | Era-Korridor |
| `imusic://compare` | Vergleichen Sie das Zuhören |
| `imusic://mood?id={id}` | Starten Sie diese Stimmung (`piece=` / `pieceId=` ist nur der Starttrack; die Stimmung stimmt immer noch mit `id` überein) |

## Einstellungen & Anleitungen

| URL | Öffnet |
|-----|-------|
| `imusic://settings` | Einstellungen |
| `imusic://usageguide` / `imusic://featureguide` | Verwendung/Feature Guide |
| `imusic://widgetguide` | Widget-Anleitung |
| `imusic://shortcutsguide` | Kurzbefehle-Anleitung |
| `imusic://feedback` | Feedback |
| `imusic://review` / `imusic://in-app-review` | In-App-Überprüfung (wenn der Store-Eintrag live ist) |

## Siri & Home Bildschirm

Fragen Sie Siri nach dem heutigen Stück, dem Roaming, der Suche oder den Favoriten, nachdem Sie Verknüpfungen hinzugefügt haben. Schnelle Aktionen für den Startbildschirm in **Settings → Shortcuts** konfigurieren. Vollständige Beispiele live im In-App Shortcuts Guide.

[FAQ](../faq) · [Privacy Policy](../Privacy) · [Support](../)

</section>
<section lang="fr" markdown="1">

iMusic supporte les liens de raccourci ** `imusic://` **. Cold start et Home Screen raccourcis passent par un tampon unifié de sorte qu'un lien n'est pas ouvert deux fois après l'embarquement.

## Format de lien


```
imusic://{host}?{params}
```


Le schéma est ** `imusic://` ** seulement.

## Accueil et aujourd'hui

| URL | Ouvre |
|-----|-------|
| `imusic://` / `imusic://home` | Accueil |
| `imusic://daily` / `imusic://today` | Daily Piece (queue est cette piste seulement) |
| `imusic://random` | Roam (bibliothèque entière) |
| `imusic://play` | Jouer |
| `imusic://last` / `imusic://lastheard` | Dernières nouvelles |

## Pièces & artistes

| URL | Ouvre |
|-----|-------|
| `imusic://piece?id={id}` | Guide de pièce (`passage` / `song` également accepté) |
| `imusic://artist?id={id}` / `imusic://artist?name={name}` | Bureau d'artiste |
| `imusic://artists` / `imusic://singers` | Répertoire des artistes |
| `imusic://famous` / `imusic://lines` | Vers célèbres |

Un pied de page de carte de partage peut ajouter `imusic://` (titre · artiste) pour les humains. La correspondance utilise toujours ** `imusic` seulement**.

## Parcourir, rechercher et écouter

| URL | Ouvre |
|-----|-------|
| `imusic://categories` / `imusic://browse` | Parcourir (`section=catalog` / `all` / `allpieces` → Toutes les pièces) |
| `imusic://collection?id={id}` | Collection (`id=col-all` est la liste virtuelle de toutes les pièces) |
| `imusic://search` / `imusic://search?q={query}` | Recherche |
| `imusic://favorites` | Favoris |
| `imusic://later` | Favoris, défilé à Plus tard |
| `imusic://lists` / `imusic://listenlists` | Listes d'écoute |
| `imusic://history` | Historique |
| `imusic://notes` | Notes |
| `imusic://mastered` | Terminé |
| `imusic://streak` / `imusic://footprint` | Streak |

Ouverture d'une seule pièce, la mini-bar, ou Song ID **resets** la file de lecture de cette pièce. Ouverture à partir d'une collection, d'une recherche, ou d'un artiste conserve cette liste si Prochain / Précédent séjour disponible.

## ID de chanson, école & humeur

| URL | Ouvre |
|-----|-------|
| `imusic://recognize` / `imusic://shazam` | ID de la chanson |
| `imusic://school` / `imusic://earschool` | École d'oreille |
| `imusic://timeline` / `imusic://corridor` | Corridor Era |
| `imusic://compare` | Comparer l'écoute |
| `imusic://mood?id={id}` | Démarrer cette humeur (`piece=` / `pieceId=` est la seule piste de départ; l'humeur correspond toujours `id`) |

## Réglages et guides

| URL | Ouvre |
|-----|-------|
| `imusic://settings` | Réglages |
| `imusic://usageguide` / `imusic://featureguide` | Guide d'utilisation / fonctionnalités |
| `imusic://widgetguide` | Guide des widgets |
| `imusic://shortcutsguide` | Guide Raccourcis |
| `imusic://feedback` | Commentaires |
| `imusic://review` / `imusic://in-app-review` | Revue de l'application (lorsque la liste des magasins est en direct) |

## Siri & Écran d'accueil

Demandez Siri pour aujourd'hui morceau, errez, recherchez, ou favoris après avoir ajouté des raccourcis. Configurez les actions rapides de l'écran d'accueil dans **Paramètres → Raccourcis**. Des exemples complets vivent dans le guide de raccourcis in-app.

[FAQ](../faq) · [Politique de confidentialité](../privacité) · [Soutien](../)

</section>
<section lang="tr" markdown="1">

IMüzik ** `imusic://` ** kısayollarını destekler. Soğuk başlangıç ve Ev Ekran kısayolları birleşik bir tampon üzerinden geçer, böylece bir bağlantı dolaptan sonra iki kez açılmaz.

## Bağlantı biçimi


```
imusic://{host}?{params}
```


Scheme ** `imusic://` ** sadece.

## Ev & Bugün

| URL | Açar |
|-----|-------|
| `imusic://` / `imusic://home` | Ana sayfa |
| `imusic://daily` / `imusic://today` | Daily Piece (queue sadece bu yolda) |
| `imusic://random` | Roam (ve-library shuffle) |
| `imusic://play` | Play Play Play |
| `imusic://last` / `imusic://lastheard` | Son duydum |

## Takımlar & sanatçılar

| URL | Açar |
|-----|-------|
| `imusic://piece?id={id}` | Parça kılavuzu ('passage' / 'song' da kabul edildi) |
| `imusic://artist?id={id}` / `imusic://artist?name={name}` | Sanatçı |
| `imusic://artists` / `imusic://singers` | Sanatçı |
| `imusic://famous` / `imusic://lines` | Ünlü dizeler |

Bir pay kartı ayağı, insanlar için `imusic://` (title · sanatçı) ekleyebilir. Maç hala kullanır ** `imusic` sadece**.

## Göze, arama ve dinlemek

| URL | Açar |
|-----|-------|
| `imusic://categories` / `imusic://browse` | Gözyaş (bölüm =catalog' / "all" / "all parça" → All Pieces) |
| `imusic://collection?id={id}` | Koleksiyon ('id=col-all'ın hepsi Sanal Tüm Parçalar listesi) |
| `imusic://search` / `imusic://search?q={query}` | Ara |
| `imusic://favorites` | Favoriler |
| `imusic://later` | Favoriler, daha sonra kaydırıldı |
| `imusic://lists` / `imusic://listenlists` | Dinle listeleri |
| `imusic://history` | Tarih Tarihi |
| `imusic://notes` | Notlar |
| `imusic://mastered` | Bitmiş Bitti |
| `imusic://streak` / `imusic://footprint` | Streak |

Tek bir parça açın, mini bar veya Song ID **resets ** okuma kuyruğunu bu parçaya döndürür. Bir koleksiyondan başlayarak, arama veya sanatçı bu listeyi tutar, böylece Next / Previous kullanılabilir.

## Song ID, school & mood

| URL | Açar |
|-----|-------|
| `imusic://recognize` / `imusic://shazam` | Song ID ID |
| `imusic://school` / `imusic://earschool` | Ear school |
| `imusic://timeline` / `imusic://corridor` | Era koridor |
| `imusic://compare` | Dinle |
| `imusic://mood?id={id}` | O ruh haliye başlayın (bölüm=' / "partId=" sadece başlangıç pistidir; ruh hala "id') |

## Ayarlar ve kılavuzlar

| URL | Açar |
|-----|-------|
| `imusic://settings` | Ayarlar |
| `imusic://usageguide` / `imusic://featureguide` | Kullanım / özellik kılavuzu |
| `imusic://widgetguide` | Widget kılavuzu |
| `imusic://shortcutsguide` | Kısayol kılavuzu |
| `imusic://feedback` | Geri bildirim |
| `imusic://review` / `imusic://in-app-review` | In-app review ( Mağaza listesi canlı olduğunda) |

## Siri & Home Ekran

Siri'ye bugün parça için sorun, roam, arama, ya da kısayollar ekledikten sonra favoriler. Configure Home Ekran **Settings → Kısakesler**. Tam örnekler in-app Shortcuts kılavuzunda yaşarlar.

[FAQ](./faq) · [Privacy Policy](./privacy)

</section>
