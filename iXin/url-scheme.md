---
layout: doc
title: iXin — Shortcut Links
app_id: iXin
doc_title_en: Shortcut Links
doc_title_zh_cn: 快捷链接说明
doc_title_zh_tw: 快捷連結說明
description: ixin:// deep links for iXin — passage, daily, recite, study, hunt, collections, settings guides, and more.
---

<section lang="en" markdown="1">

iXin supports **`ixin://`** shortcut links (URL scheme). Cold start and Home Screen shortcuts are delivered through a unified buffer so links are not opened twice after onboarding.

## Link format

```
ixin://{host}?{params}
```

## Passages & authors

| URL | Opens |
|-----|-------|
| `ixin://passage?id={id}` | Passage detail |
| `ixin://saying?id={id}` / `ixin://couplet?id={id}` / `ixin://poem?id={id}` | Same as passage (compatibility) |
| `ixin://passage?id={id}&card=1` | Passage detail and card sheet |
| `ixin://card?id={id}` / `ixin://share-card?id={id}` | Insight cards |
| `ixin://author?id={id}` | Author detail |
| `ixin://recite` / `ixin://recite?id={id}` | Recite flow |

## Discovery & practice

| URL | Opens |
|-----|-------|
| `ixin://home` | Home |
| `ixin://daily` | Daily Insight |
| `ixin://random` | Random passage |
| `ixin://favorites` | Favorites |
| `ixin://famous` | Famous lines |
| `ixin://search` / `ixin://search?q={query}` | Search |
| `ixin://study` / `ixin://study?id={id}` | Heart School |
| `ixin://hunt` | Heart Hunt (`keyword-hunt` / `flyflower`) |
| `ixin://handwriting` | Handwriting search (`handwrite`; iOS) |
| `ixin://mastered` | Mastered (`progress`) |
| `ixin://categories` / `ixin://categories?section=` | Browse |
| `ixin://collection?id=` | Collection / book (`chuanxilu` / `daxuewen` / `jiaotiao` / `yilvwen` / poems) |
| `ixin://corpus` | All passages (`all`) |
| `ixin://last-read` | Last read |
| `ixin://reading-history` | Reading history |
| `ixin://notes` | Notes |
| `ixin://journal` | Knowing-Acting journal |
| `ixin://liangzhi` | Three Questions of Liangzhi |
| `ixin://graph` | Concept graph |
| `ixin://timeline` | Annals / timeline |
| `ixin://map` | Map |
| `ixin://people` | People |
| `ixin://achievements` | Achievements |
| `ixin://theme?id=` | Theme |

## Settings & guides

| URL | Opens |
|-----|-------|
| `ixin://settings` | Settings |
| `ixin://usage-guide` | Usage guide |
| `ixin://widget-guide` | Widget guide |
| `ixin://shortcuts-guide` | Shortcuts guide |
| `ixin://feature-guide` | Replay onboarding |
| `ixin://feedback` | Feedback email |
| `ixin://in-app-review` | In-app / Store review entry |

## Examples

```
ixin://daily
ixin://passage?id=1
ixin://journal
ixin://liangzhi
ixin://collection?id=chuanxilu
ixin://study
ixin://hunt
```

## Notes

- Parameters are case-sensitive where IDs are numeric.
- Siri, Shortcuts, widgets, and Control Center controls use the same deep-link routes.
- See the in-app **Settings → Help** guides for the latest list.

</section>
<section lang="zh-CN" markdown="1">

爱王阳明支持 **`ixin://`** 快捷链接（URL Scheme）。冷启动与主屏快捷经统一缓冲投递，避免引导页结束后重复打开。

## 链接格式

```
ixin://{host}?{params}
```

## 篇目与作者

| URL | 打开 |
|-----|------|
| `ixin://passage?id={id}` | 篇目详情 |
| `ixin://saying?id={id}` / `ixin://couplet?id={id}` / `ixin://poem?id={id}` | 同详情（兼容别名） |
| `ixin://passage?id={id}&card=1` | 详情并弹出心卡 |
| `ixin://card?id={id}` / `ixin://share-card?id={id}` | 心卡 |
| `ixin://author?id={id}` | 作者详情 |
| `ixin://recite` / `ixin://recite?id={id}` | 诵读 |

## 发现与学堂

| URL | 打开 |
|-----|------|
| `ixin://home` | 首页 |
| `ixin://daily` | 每日一心 |
| `ixin://random` | 随机篇目 |
| `ixin://favorites` | 收藏 |
| `ixin://famous` | 金句 |
| `ixin://search` / `ixin://search?q={query}` | 搜索 |
| `ixin://study` / `ixin://study?id={id}` | 心学堂 |
| `ixin://hunt` | 寻心（`keyword-hunt` / `flyflower`） |
| `ixin://handwriting` | 手写搜索（`handwrite`；iOS） |
| `ixin://mastered` | 已掌握（`progress`） |
| `ixin://categories` / `ixin://categories?section=` | 分类浏览 |
| `ixin://collection?id=` | 合集 / 典籍（`chuanxilu` / `daxuewen` / `jiaotiao` / `yilvwen` 等） |
| `ixin://corpus` | 全部篇目（`all`） |
| `ixin://last-read` | 最近阅读 |
| `ixin://reading-history` | 阅读历史 |
| `ixin://notes` | 笔记 |
| `ixin://journal` | 知行日记 |
| `ixin://liangzhi` | 良知三问 |
| `ixin://graph` | 概念图谱 |
| `ixin://timeline` | 年谱 |
| `ixin://map` | 地图 |
| `ixin://people` | 人物 |
| `ixin://achievements` | 成就 |
| `ixin://theme?id=` | 主题 |

## 设置与指南

| URL | 打开 |
|-----|------|
| `ixin://settings` | 设置 |
| `ixin://usage-guide` | 使用说明 |
| `ixin://widget-guide` | 小组件指南 |
| `ixin://shortcuts-guide` | 快捷指南 |
| `ixin://feature-guide` | 重播功能引导 |
| `ixin://feedback` | 反馈邮件 |
| `ixin://in-app-review` | 应用内评价入口 |

## 示例

```
ixin://daily
ixin://passage?id=1
ixin://journal
ixin://liangzhi
ixin://collection?id=chuanxilu
ixin://study
ixin://hunt
```

## 说明

- 数字 ID 参数区分大小写。
- Siri、快捷指令、小组件与控制中心使用同一套深链。
- 最新列表见应用内 **设置 → 帮助**。

</section>
<section lang="zh-TW" markdown="1">

愛王陽明支援 **`ixin://`** 快捷連結（URL Scheme）。冷啟動與主畫面捷徑經統一緩衝投遞，避免引導頁結束後重複打開。

## 連結格式

```
ixin://{host}?{params}
```

## 篇目與作者

| URL | 打開 |
|-----|------|
| `ixin://passage?id={id}` | 篇目詳情 |
| `ixin://saying?id={id}` / `ixin://couplet?id={id}` / `ixin://poem?id={id}` | 同詳情（相容別名） |
| `ixin://passage?id={id}&card=1` | 詳情並彈出心卡 |
| `ixin://card?id={id}` / `ixin://share-card?id={id}` | 心卡 |
| `ixin://author?id={id}` | 作者詳情 |
| `ixin://recite` / `ixin://recite?id={id}` | 誦讀 |

## 發現與學堂

| URL | 打開 |
|-----|------|
| `ixin://home` | 首頁 |
| `ixin://daily` | 每日一心 |
| `ixin://random` | 隨機篇目 |
| `ixin://favorites` | 收藏 |
| `ixin://famous` | 金句 |
| `ixin://search` / `ixin://search?q={query}` | 搜尋 |
| `ixin://study` / `ixin://study?id={id}` | 心學堂 |
| `ixin://hunt` | 尋心（`keyword-hunt` / `flyflower`） |
| `ixin://handwriting` | 手寫搜尋（`handwrite`；iOS） |
| `ixin://mastered` | 已掌握（`progress`） |
| `ixin://categories` / `ixin://categories?section=` | 分類瀏覽 |
| `ixin://collection?id=` | 合集 / 典籍（`chuanxilu` / `daxuewen` / `jiaotiao` / `yilvwen` 等） |
| `ixin://corpus` | 全部篇目（`all`） |
| `ixin://last-read` | 最近閱讀 |
| `ixin://reading-history` | 閱讀歷史 |
| `ixin://notes` | 筆記 |
| `ixin://journal` | 知行日記 |
| `ixin://liangzhi` | 良知三問 |
| `ixin://graph` | 概念圖譜 |
| `ixin://timeline` | 年譜 |
| `ixin://map` | 地圖 |
| `ixin://people` | 人物 |
| `ixin://achievements` | 成就 |
| `ixin://theme?id=` | 主題 |

## 設定與指南

| URL | 打開 |
|-----|------|
| `ixin://settings` | 設定 |
| `ixin://usage-guide` | 使用說明 |
| `ixin://widget-guide` | 小工具指南 |
| `ixin://shortcuts-guide` | 捷徑指南 |
| `ixin://feature-guide` | 重播功能引導 |
| `ixin://feedback` | 回饋郵件 |
| `ixin://in-app-review` | 應用內評價入口 |

## 範例

```
ixin://daily
ixin://passage?id=1
ixin://journal
ixin://liangzhi
ixin://collection?id=chuanxilu
ixin://study
ixin://hunt
```

## 說明

- 數字 ID 參數區分大小寫。
- Siri、捷徑、小工具與控制中心使用同一套深鏈。
- 最新列表見應用內 **設定 → 說明**。

</section>
<section lang="ja" markdown="1">

iXinは** `ixin://` **ショートカットリンク(URLスキーム)をサポートしています。 コールドスタートとホーム画面のショートカットは、統一されたバッファを介して配信されますので、リンクはオンボーディング後2回開いていません。

## リンク形式


```
ixin://{host}?{params}
```


## パスポートと著者

| URL | 開く画面 |
|-----|-------|
| `ixin://passage?id={id}` | 章句の詳細 |
| `ixin://saying?id={id}` / `ixin://couplet?id={id}` / `ixin://poem?id={id}` | 通路と同じ(互換性) |
| `ixin://passage?id={id}&card=1` | 通路の細部およびカード シート |
| `ixin://card?id={id}` / `ixin://share-card?id={id}` | インサイトカード |
| `ixin://author?id={id}` | 作者の詳細 |
| `ixin://recite` / `ixin://recite?id={id}` | 誦読フロー |

## ディスカバリー&プラクティス

| URL | 開く画面 |
|-----|-------|
| `ixin://home` | ホーム |
| `ixin://daily` | デイリーインサイト |
| `ixin://random` | ランダムな章句 |
| `ixin://favorites` | お気に入り |
| `ixin://famous` | 名句一覧 |
| `ixin://search` / `ixin://search?q={query}` | 検索 |
| `ixin://study` / `ixin://study?id={id}` | ハートスクール |
| `ixin://hunt` | ハートハント (`keyword-hunt`/`flyflower`) |
| `ixin://handwriting` | 手書き検索 (`handwrite`; iOS) |
| `ixin://mastered` | マスタード (`progress`) |
| `ixin://categories` / `ixin://categories?section=` | ブラウズ |
| `ixin://collection?id=` | 収蔵品/書籍(「チュアンシルー」/「ダクセン」/「ジオチオ」/「イヴン」/詩」) |
| `ixin://corpus` | すべての通路 (`all`) |
| `ixin://last-read` | 最後に読んだ項目 |
| `ixin://reading-history` | 閲覧履歴 |
| `ixin://notes` | ノート |
| `ixin://journal` | 知能ジャーナル |
| `ixin://liangzhi` | Liangzhiの3つの質問 |
| `ixin://graph` | コンセプトグラフ |
| `ixin://timeline` | アナルス/タイムライン |
| `ixin://map` | サイトマップ |
| `ixin://people` | スタッフ |
| `ixin://achievements` | 実績紹介 |
| `ixin://theme?id=` | テーマ: |

## 設定とガイド

| URL | 開く画面 |
|-----|-------|
| `ixin://settings` | 設定 |
| `ixin://usage-guide` | 使い方ガイド |
| `ixin://widget-guide` | ウィジェットガイド |
| `ixin://shortcuts-guide` | ショートカットガイド |
| `ixin://feature-guide` | オンボーディングの再生 |
| `ixin://feedback` | フィードバックメール |
| `ixin://in-app-review` | アプリ内／App Store レビュー |

## 例


```
ixin://daily
ixin://passage?id=1
ixin://journal
ixin://liangzhi
ixin://collection?id=chuanxilu
ixin://study
ixin://hunt
```


## ノート

- パラメータはIDが数値である場合感度です。
- シリ、ショートカット、ウィジェット、およびコントロールセンターコントロールは、同じディープリンクルートを使用します。
- 最新リストのアプリ内設定 → Help** ガイドを参照してください。

</section>
<section lang="ko" markdown="1">

iXin은 ** `ixin://` ** 단축키 링크 (URL 계획)를 지원합니다. 콜드 시작 및 홈 화면 단축은 통합 버퍼를 통해 전달되므로 링크가 내장 된 후 두 번 열리지 않습니다.

## 링크 형식


```
ixin://{host}?{params}
```


## 책임 & 저자

| URL | 열리는 화면 |
|-----|-------|
| `ixin://passage?id={id}` | 구절 상세 |
| `ixin://saying?id={id}` / `ixin://couplet?id={id}` / `ixin://poem?id={id}` | 통행과 같 ( 겸용성) |
| `ixin://passage?id={id}&card=1` | 통행 세부사항과 카드 장 |
| `ixin://card?id={id}` / `ixin://share-card?id={id}` | Insight 카드 |
| `ixin://author?id={id}` | 작가 상세 |
| `ixin://recite` / `ixin://recite?id={id}` | 낭독 흐름 |

## 디스커버리 & 연습

| URL | 열리는 화면 |
|-----|-------|
| `ixin://home` | 홈 |
| `ixin://daily` | 매일 통찰력 |
| `ixin://random` | 무작위 구절 |
| `ixin://favorites` | 즐겨찾기 |
| `ixin://famous` | 명구 목록 |
| `ixin://search` / `ixin://search?q={query}` | 검색 |
| `ixin://study` / `ixin://study?id={id}` | 심장 학교 |
| `ixin://hunt` | 하트 헌트 (`keyword-hunt`/`flyflower`) |
| `ixin://handwriting` | Handwriting search (`handwrite`; iOS) |
| `ixin://mastered` | 마스터 (`progress`) |
| `ixin://categories` / `ixin://categories?section=` | 둘러보기 |
| `ixin://collection?id=` | 컬렉션 / 책 (`chuanxilu`/`daxuewen`/`jiaotiao`/`yilvwen`/시) |
| `ixin://corpus` | 모든 통행 (`all`) |
| `ixin://last-read` | 마지막으로 읽은 항목 |
| `ixin://reading-history` | 읽기 기록 |
| `ixin://notes` | 메모 |
| `ixin://journal` | Knowing-Acting 저널 |
| `ixin://liangzhi` | Liangzhi의 세 가지 질문 |
| `ixin://graph` | 컨셉 그래프 |
| `ixin://timeline` | 연락처 |
| `ixin://map` | 지도보기 |
| `ixin://people` | 이름 * |
| `ixin://achievements` | 회사연혁 |
| `ixin://theme?id=` | 이름 * |

## 설정 및 가이드

| URL | 열리는 화면 |
|-----|-------|
| `ixin://settings` | 설정 |
| `ixin://usage-guide` | 사용 가이드 |
| `ixin://widget-guide` | 위젯 가이드 |
| `ixin://shortcuts-guide` | 단축어 가이드 |
| `ixin://feature-guide` | 온보딩 다시 보기 |
| `ixin://feedback` | 피드백 이메일 |
| `ixin://in-app-review` | 앱 내 / App Store 리뷰 |

## 예시


```
ixin://daily
ixin://passage?id=1
ixin://journal
ixin://liangzhi
ixin://collection?id=chuanxilu
ixin://study
ixin://hunt
```


## 메모

- 매개 변수는 ID가 숫자인지 여부를 감지합니다.
- Siri, Shortcuts, 위젯 및 제어 센터 제어는 동일한 딥 링크 루트를 사용합니다.
- in-app**Settings → 도움말** 최신 목록 안내

</section>
<section lang="ru" markdown="1">

iXin поддерживает ярлыки ** `ixin://` ** (схема URL). Холодный старт и ярлыки домашнего экрана доставляются через единый буфер, поэтому ссылки не открываются дважды после входа.

## Формат ссылки


```
ixin://{host}?{params}
```


## Проходы и авторы

| URL | Открывает |
|-----|-------|
| `ixin://passage?id={id}` | Страница отрывка |
| `ixin://saying?id={id}` / `ixin://couplet?id={id}` / `ixin://poem?id={id}` | Совместимость (Compatibility) |
| `ixin://passage?id={id}&card=1` | Детали проезда и карточный лист |
| `ixin://card?id={id}` / `ixin://share-card?id={id}` | Карты Insight |
| `ixin://author?id={id}` | Страница автора |
| `ixin://recite` / `ixin://recite?id={id}` | Режим чтения вслух |

## Discovery & Practice

| URL | Открывает |
|-----|-------|
| `ixin://home` | Главная |
| `ixin://daily` | Ежедневное понимание |
| `ixin://random` | Случайный отрывок |
| `ixin://favorites` | Избранное |
| `ixin://famous` | Знаменитые строки |
| `ixin://search` / `ixin://search?q={query}` | Поиск |
| `ixin://study` / `ixin://study?id={id}` | Школа сердца |
| `ixin://hunt` | Охота за сердцем ('keyword-hunt' / 'flyflower') |
| `ixin://handwriting` | Поиск почерка («handwrite»; iOS) |
| `ixin://mastered` | Мастеринг («Прогресс») |
| `ixin://categories` / `ixin://categories?section=` | Обзор |
| `ixin://collection?id=` | Коллекция/книга ('chuanxilu'/ 'daxuewen'/ 'jiaotiao'/ 'yilvwen'/стихи) |
| `ixin://corpus` | Все пассажи («All») |
| `ixin://last-read` | Последнее прочитанное |
| `ixin://reading-history` | История чтения |
| `ixin://notes` | Заметки |
| `ixin://journal` | Знающий журнал |
| `ixin://liangzhi` | Три вопроса о Лянжи |
| `ixin://graph` | Концептуальный граф |
| `ixin://timeline` | Анналы / хронология |
| `ixin://map` | Карта |
| `ixin://people` | Люди |
| `ixin://achievements` | Достижения |
| `ixin://theme?id=` | Тема |

## Настройки и руководства

| URL | Открывает |
|-----|-------|
| `ixin://settings` | Настройки |
| `ixin://usage-guide` | Руководство по использованию |
| `ixin://widget-guide` | Руководство по виджетам |
| `ixin://shortcuts-guide` | Руководство по «Командам» |
| `ixin://feature-guide` | Повторное знакомство |
| `ixin://feedback` | Письмо с отзывом |
| `ixin://in-app-review` | Отзыв в приложении / App Store |

## Примеры


```
ixin://daily
ixin://passage?id=1
ixin://journal
ixin://liangzhi
ixin://collection?id=chuanxilu
ixin://study
ixin://hunt
```


## Заметки

- Параметры чувствительны к регистру, где идентификаторы являются числовыми.
- Siri, ярлыки, виджеты и элементы управления Центра управления используют одни и те же маршруты глубокой связи.
- Смотрите в приложении ** Настройки → Справочные руководства ** для последнего списка.

</section>
<section lang="th" markdown="1">

IXin รองรับ ** `ixin://` BAR * ลิงก์ลัด (RUL scheme) การเริ่มหน้าจอหน้าจอเย็นและหน้าจอบ้าน จะถูกส่งไปผ่านระบบบัฟเฟอร์แบบรวม ดังนั้นลิงก์จึงไม่ถูกเปิดสองครั้งหลังจากขึ้นเครื่อง

## รูปแบบลิงก์


```
ixin://{host}?{params}
```


## ผู้เขียน

| URL | เปิด |
|-----|-------|
| `ixin://passage?id={id}` | รายละเอียดข้อความ |
| `ixin://saying?id={id}` / `ixin://couplet?id={id}` / `ixin://poem?id={id}` | เช่นเดียวกันกับเนื้อเรื่อง (ความเข้ากันได้) |
| `ixin://passage?id={id}&card=1` | รายละเอียดและนามบัตร |
| `ixin://card?id={id}` / `ixin://share-card?id={id}` | ไพ่สําหรับ หยั่ง เห็น |
| `ixin://author?id={id}` | รายละเอียดผู้แต่ง |
| `ixin://recite` / `ixin://recite?id={id}` | โฟลว์การท่อง |

## การท่องเว็บ

| URL | เปิด |
|-----|-------|
| `ixin://home` | หน้าแรก |
| `ixin://daily` | การ หยั่ง เห็น เข้าใจ ทุก วัน |
| `ixin://random` | ข้อความแบบสุ่ม |
| `ixin://favorites` | รายการโปรด |
| `ixin://famous` | บรรทัดขึ้นชื่อ |
| `ixin://search` / `ixin://search?q={query}` | ค้นหา |
| `ixin://study` / `ixin://study?id={id}` | โรงเรียนหัวใจ |
| `ixin://hunt` | หัวใจล่า ('คําพยัญชนะ' / 'ดอกไม้แมลงวัน') |
| `ixin://handwriting` | สืบค้นเมื่อเขียนด้วยมือ ('เขียนเอง'; OS) |
| `ixin://mastered` | สําเร็จการศึกษาแล้ว ('รุก') |
| `ixin://categories` / `ixin://categories?section=` | เรียกดู |
| `ixin://collection?id=` | เครื่องราชอิสริยาภรณ์ / หนังสือ (อังกฤษ) |
| `ixin://corpus` | ทุกช่อง (ทั้งหมด) |
| `ixin://last-read` | รายการที่อ่านล่าสุด |
| `ixin://reading-history` | ประวัติการอ่าน |
| `ixin://notes` | บันทึก |
| `ixin://journal` | บันทึกประจําวันที่ใช้ร่วม |
| `ixin://liangzhi` | คํา ถาม สาม ข้อ ของ ลี ยง ซิ |
| `ixin://graph` | เส้นพริ้วไหว |
| `ixin://timeline` | เส้นต่อเนื่อง / เส้นเวลา |
| `ixin://map` | แผนที่ |
| `ixin://people` | ผู้คน |
| `ixin://achievements` | คุณสมบัติต่าง ๆ |
| `ixin://theme?id=` | ชุดตกแต่ง |

## การตั้งค่าและคู่มือ

| URL | เปิด |
|-----|-------|
| `ixin://settings` | การตั้งค่า |
| `ixin://usage-guide` | คู่มือการใช้งาน |
| `ixin://widget-guide` | คู่มือวิดเจ็ต |
| `ixin://shortcuts-guide` | คู่มือทางลัด |
| `ixin://feature-guide` | เล่นทัวร์แนะนำอีกครั้ง |
| `ixin://feedback` | อีเมลข้อเสนอแนะ |
| `ixin://in-app-review` | รีวิวในแอป / App Store |

## ตัวอย่าง


```
ixin://daily
ixin://passage?id=1
ixin://journal
ixin://liangzhi
ixin://collection?id=chuanxilu
ixin://study
ixin://hunt
```


## บันทึก

- พารามิเตอร์คือความไวของตัวเลข
- ไซรี, ทางลัด, วิดเจ็ต, และศูนย์ควบคุม ใช้เส้นทางลับเดียวกัน
- ดู In-appings-Cettings softs for the list ล่าสุด

</section>
<section lang="de" markdown="1">

iXin unterstützt ** `ixin://` ** Shortcut Links (URL-Schema). Kaltstart- und Home Screen-Verknüpfungen werden über einen einheitlichen Puffer geliefert, so dass Links nach dem Onboarding nicht zweimal geöffnet werden.

## Linkformat


```
ixin://{host}?{params}
```


## Passagen & Autoren

| URL | Öffnet |
|-----|-------|
| `ixin://passage?id={id}` | Passagen-Detail |
| `ixin://saying?id={id}` / `ixin://couplet?id={id}` / `ixin://poem?id={id}` | Wie Passage (Kompatibilität) |
| `ixin://passage?id={id}&card=1` | Angaben zum Durchgang und Kartenblatt |
| `ixin://card?id={id}` / `ixin://share-card?id={id}` | Insightkarten |
| `ixin://author?id={id}` | Autorendetail |
| `ixin://recite` / `ixin://recite?id={id}` | Rezitationsablauf |

## Entdeckung und Praxis

| URL | Öffnet |
|-----|-------|
| `ixin://home` | Startseite |
| `ixin://daily` | Tägliche Einsicht |
| `ixin://random` | Zufällige Passage |
| `ixin://favorites` | Favoriten |
| `ixin://famous` | Berühmte Zeilen |
| `ixin://search` / `ixin://search?q={query}` | Suche |
| `ixin://study` / `ixin://study?id={id}` | Herzschule |
| `ixin://hunt` | Heart Hunt (`keyword-hunt` / `flyflower`) |
| `ixin://handwriting` | Handschriftsuche (`handwrite`; iOS) |
| `ixin://mastered` | gemeistert („Fortschritt) |
| `ixin://categories` / `ixin://categories?section=` | Durchsuchen |
| `ixin://collection?id=` | Sammlung / Buch (`chuanxilu` / `daxuewen` / `jiaotiao` / `yilvwen` / Gedichte) |
| `ixin://corpus` | Alle Passagen (`all`) |
| `ixin://last-read` | Zuletzt gelesen |
| `ixin://reading-history` | Leseverlauf |
| `ixin://notes` | Notizen |
| `ixin://journal` | Knowing-Acting Journal |
| `ixin://liangzhi` | Drei Fragen von Liangzhi |
| `ixin://graph` | Konzeptgrafik |
| `ixin://timeline` | Annalen / Timeline |
| `ixin://map` | Karte |
| `ixin://people` | Menschen |
| `ixin://achievements` | Erfolge |
| `ixin://theme?id=` | Thema |

## Einstellungen & Anleitungen

| URL | Öffnet |
|-----|-------|
| `ixin://settings` | Einstellungen |
| `ixin://usage-guide` | Nutzungsanleitung |
| `ixin://widget-guide` | Widget-Anleitung |
| `ixin://shortcuts-guide` | Kurzbefehle-Anleitung |
| `ixin://feature-guide` | Einführung erneut abspielen |
| `ixin://feedback` | Feedback-E-Mail |
| `ixin://in-app-review` | In-App- / App-Store-Bewertung |

## Beispiele


```
ixin://daily
ixin://passage?id=1
ixin://journal
ixin://liangzhi
ixin://collection?id=chuanxilu
ixin://study
ixin://hunt
```


## Notizen

- Parameter sind fallsensibel, wo IDs numerisch sind.
- Siri, Shortcuts, Widgets und Control Center-Steuerelemente verwenden die gleichen Deep-Link-Routen.
- Sehen Sie sich die In-App **Einstellungen → Hilfe ** Anleitungen für die neueste Liste an.

</section>
<section lang="fr" markdown="1">

iXin prend en charge ** `ixin://` ** liens de raccourci (schéma URL). Les raccourcis de démarrage à froid et d'écran d'accueil sont livrés via un tampon unifié de sorte que les liens ne sont pas ouverts deux fois après l'embarquement.

## Format de lien


```
ixin://{host}?{params}
```


## Passages et auteurs

| URL | Ouvre |
|-----|-------|
| `ixin://passage?id={id}` | Détail du passage |
| `ixin://saying?id={id}` / `ixin://couplet?id={id}` / `ixin://poem?id={id}` | Même chose que le passage (compatibilité) |
| `ixin://passage?id={id}&card=1` | Détails du passage et feuille de carte |
| `ixin://card?id={id}` / `ixin://share-card?id={id}` | Cartes d'affichage |
| `ixin://author?id={id}` | Détail de l’auteur |
| `ixin://recite` / `ixin://recite?id={id}` | Flux de récitation |

## Découverte et pratique

| URL | Ouvre |
|-----|-------|
| `ixin://home` | Accueil |
| `ixin://daily` | Aperçu quotidien |
| `ixin://random` | Passage aléatoire |
| `ixin://favorites` | Favoris |
| `ixin://famous` | Vers célèbres |
| `ixin://search` / `ixin://search?q={query}` | Recherche |
| `ixin://study` / `ixin://study?id={id}` | École de cardiologie |
| `ixin://hunt` | Chasse au cœur ( ' chasse au mot clé ' / ' flyflower ') |
| `ixin://handwriting` | Recherche d'écriture (`handwrite`; iOS) |
| `ixin://mastered` | Maîtrise ('progrès') |
| `ixin://categories` / `ixin://categories?section=` | Parcourir |
| `ixin://collection?id=` | Collection / livre (`chuanxilu` / `daxuewen` / `jiaotiao` / `yilvwen` / poèmes) |
| `ixin://corpus` | Tous les passages |
| `ixin://last-read` | Dernière lecture |
| `ixin://reading-history` | Historique de lecture |
| `ixin://notes` | Notes |
| `ixin://journal` | Journal de connaissance-action |
| `ixin://liangzhi` | Trois questions de Liangzhi |
| `ixin://graph` | Graphique conceptuel |
| `ixin://timeline` | Annales / chronologie |
| `ixin://map` | Carte |
| `ixin://people` | Personnes |
| `ixin://achievements` | Réalisations |
| `ixin://theme?id=` | Thème |

## Réglages et guides

| URL | Ouvre |
|-----|-------|
| `ixin://settings` | Réglages |
| `ixin://usage-guide` | Guide d'utilisation |
| `ixin://widget-guide` | Guide des widgets |
| `ixin://shortcuts-guide` | Guide Raccourcis |
| `ixin://feature-guide` | Rejouer l’accueil |
| `ixin://feedback` | E-mail de commentaires |
| `ixin://in-app-review` | Avis in-app / App Store |

## Exemples


```
ixin://daily
ixin://passage?id=1
ixin://journal
ixin://liangzhi
ixin://collection?id=chuanxilu
ixin://study
ixin://hunt
```


## Notes

- Les paramètres sont sensibles aux cas où les ID sont numériques.
- Les commandes Siri, Shortcuts, Widgets et Control Center utilisent les mêmes itinéraires de liaison profonde.
- Voir la page d'application **Paramètres → Aide** pour la dernière liste.

</section>
<section lang="tr" markdown="1">

iXin, ** `ixin://` ** kısayol bağlantıları (URL planı). Soğuk başlangıç ve Ev Ekran kısayolları birleşik bir tampon aracılığıyla teslim edilir, bu yüzden bağlantılar gemiden sonra iki kez açılmaz.

## Bağlantı biçimi


```
ixin://{host}?{params}
```


## Geçişler ve yazarlar

| URL | Açar |
|-----|-------|
| `ixin://passage?id={id}` | Pasaj ayrıntısı |
| `ixin://saying?id={id}` / `ixin://couplet?id={id}` / `ixin://poem?id={id}` | Aynı geçiş (compatability) |
| `ixin://passage?id={id}&card=1` | Pasaj detay ve kart sayfası |
| `ixin://card?id={id}` / `ixin://share-card?id={id}` | İçgörü kartları |
| `ixin://author?id={id}` | Yazar ayrıntısı |
| `ixin://recite` / `ixin://recite?id={id}` | Okuma akışı |

## Discovery & practice

| URL | Açar |
|-----|-------|
| `ixin://home` | Ana sayfa |
| `ixin://daily` | Günlük Bilgi |
| `ixin://random` | Rastgele pasaj |
| `ixin://favorites` | Favoriler |
| `ixin://famous` | Ünlü dizeler |
| `ixin://search` / `ixin://search?q={query}` | Ara |
| `ixin://study` / `ixin://study?id={id}` | Kalp Okulu |
| `ixin://hunt` | Heart Hunt ('keyword-hunt' / 'flyflower') |
| `ixin://handwriting` | Hand writing search ('handwrite'; iOS) |
| `ixin://mastered` | Mastered ('progress') |
| `ixin://categories` / `ixin://categories?section=` | Gözat |
| `ixin://collection?id=` | Koleksiyon / kitap ('chuanxilu' / "daxuewen' / "jiaotiao" / "yilvwen" / şiirler) |
| `ixin://corpus` | Bütün geçitler ('all') |
| `ixin://last-read` | Son okunan |
| `ixin://reading-history` | Okuma geçmişi |
| `ixin://notes` | Notlar |
| `ixin://journal` | Know-Acting |
| `ixin://liangzhi` | Liangzhi'nın Üç Soru |
| `ixin://graph` | Kavram grafiği |
| `ixin://timeline` | Annals / zaman çizelgesi |
| `ixin://map` | Map Map Map Map Map Map |
| `ixin://people` | İnsanlar |
| `ixin://achievements` | Başarılar Başarılar |
| `ixin://theme?id=` | Tema |

## Ayarlar ve kılavuzlar

| URL | Açar |
|-----|-------|
| `ixin://settings` | Ayarlar |
| `ixin://usage-guide` | Kullanım kılavuzu |
| `ixin://widget-guide` | Widget kılavuzu |
| `ixin://shortcuts-guide` | Kısayol kılavuzu |
| `ixin://feature-guide` | Tanıtımı yeniden oynat |
| `ixin://feedback` | Geri bildirim e-postası |
| `ixin://in-app-review` | Uygulama içi / App Store değerlendirme |

## Örnekler


```
ixin://daily
ixin://passage?id=1
ixin://journal
ixin://liangzhi
ixin://collection?id=chuanxilu
ixin://study
ixin://hunt
```


## Notlar

- Parametreler, kimliklerin sayısal olduğu durumlarda hassastır.
- Siri, Shortcuts, widgets ve Control Center kontrolleri aynı derin bağlantı yollarını kullanır.
- In-app **Settings → Yardım** en son liste için kılavuzlar.

</section>
