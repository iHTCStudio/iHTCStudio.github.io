---
layout: doc
title: iTer — URL Scheme Reference
app_id: iTer
doc_title_en: URL Scheme Reference
doc_title_zh_cn: URL Scheme 深度链接文档
doc_title_zh_tw: URL Scheme 深度連結文件
description: Complete reference for iTer:// deep links, widget links, and Home Screen Quick Actions on iPhone and iPad.
---

<section lang="en" markdown="1">

iTer supports the **`iTer://`** URL scheme on **iPhone and iPad**. Use it in Shortcuts, Safari, widgets, or other apps to open a question, the daily quiz, favourites, or the wrong-answer book.

**Home Screen Quick Actions** (long-press the app icon) reuse the same `type` strings. Choose up to **4** from **7** options in **Settings → Home Screen shortcuts**.

> **Note:** Deep links **navigate** inside the app. They do not change quiz settings or mark questions remotely. **Mac** does not register Home Screen Quick Actions; widgets and in-app navigation still work on Mac.

## Protocol

```
iTer://<host>[?query]
```

| Rule | Detail |
|------|--------|
| **Scheme** | `iTer` (case-insensitive) |
| **Question detail** | Host `question` — query **`id=<questionID>`** or **`q=<questionID>`** (required) |
| **Daily Quiz** | Host `quiz` |
| **Favourites** | Host `favorites` → Settings → Favourites list |
| **Wrong book** | Host `wrong`, `mistakes`, or `wrongquestions` — optional **`record=<UUID>`** opens one mistake |
| **Search** | Host `search` — Quick Action / shortcut only (opens global search tab) |
| **Categories** | Host `categories` — Quick Action / shortcut only (opens Categories tab) |
| **Feedback** | Host `feedback` — Quick Action only (mail compose or `mailto:` fallback) |
| **Rate app** | Host `review` — Quick Action only (StoreKit in-app review). Legacy types containing `star` also work. |

Paths such as `iTer://quiz` are accepted when the host is empty and the path segment matches.

## Examples

```
iTer://question?id=94c34bb2bdef11e6a0e100163e0021c8
iTer://quiz
iTer://favorites
iTer://wrong
iTer://wrong?record=550E8400-E29B-41D4-A716-446655440000
```

## Home Screen Quick Actions

| Type | Typical use |
|------|-------------|
| `iTer://search` | Global search |
| `iTer://quiz` | Daily Quiz tab |
| `iTer://favorites` | Favourites list |
| `iTer://wrong` | Wrong-answer book |
| `iTer://categories` | Categories tab |
| `iTer://feedback` | Send feedback |
| `iTer://review` | Rate the app (StoreKit) |

Default selection: Search, Quiz, Favourites, Feedback. Reorder or replace in **Settings → Home Screen shortcuts** (max 4). The app matches shortcut `type` strings with **contains**, so legacy variants that include these paths still route correctly.

## Widget deep links

| Widget | Typical URL |
|--------|-------------|
| Daily Question | `iTer://question?id=…` |
| Quiz Glance | `iTer://quiz` |
| Favourites Glance | `iTer://favorites` |
| Wrong Book Glance | `iTer://wrong` or `iTer://wrong?record=<UUID>` |

---

[Back to iTer Support](../) · [FAQ](../faq) · [Privacy Policy](../privacy)

</section>
<section lang="zh-CN" markdown="1">

爱技术支持 **`iTer://`** URL Scheme（**iPhone / iPad**）。可在快捷指令、Safari、小组件或其他 App 中打开题目、每日测验、收藏或错题本。

**主屏快捷指令**（长按图标）使用相同的 `type` 字符串。在 **设置 → 主屏快捷方式** 中从 **7 项**里最多选 **4 项**。

> **说明：** 深度链接仅用于**应用内跳转**，不会远程修改测验设置或题目标记。**Mac** 无主屏快捷指令；小组件与应用内导航在 Mac 上仍可用。

## 协议

```
iTer://<host>[?query]
```

| 规则 | 说明 |
|------|------|
| **Scheme** | `iTer`（大小写不敏感） |
| **题目详情** | Host `question` — 查询参数 **`id=<题目ID>`** 或 **`q=<题目ID>`**（必填） |
| **每日测验** | Host `quiz` |
| **收藏** | Host `favorites` → 设置 → 收藏列表 |
| **错题本** | Host `wrong` / `mistakes` / `wrongquestions` — 可选 **`record=<UUID>`** 打开单条错题 |
| **搜索** | Host `search` — 仅快捷指令（打开全局搜索 Tab） |
| **分类** | Host `categories` — 仅快捷指令（打开分类 Tab） |
| **反馈** | Host `feedback` — 仅快捷指令（邮件撰写或 `mailto:` 回退） |
| **评分** | Host `review` — 仅快捷指令（StoreKit 应用内评分）。含 `star` 的旧 type 仍兼容 |

## 示例

```
iTer://question?id=94c34bb2bdef11e6a0e100163e0021c8
iTer://quiz
iTer://favorites
iTer://wrong
iTer://wrong?record=550E8400-E29B-41D4-A716-446655440000
```

## 主屏快捷指令

| Type | 用途 |
|------|------|
| `iTer://search` | 全局搜索 |
| `iTer://quiz` | 每日测验 Tab |
| `iTer://favorites` | 收藏列表 |
| `iTer://wrong` | 错题本 |
| `iTer://categories` | 分类 Tab |
| `iTer://feedback` | 发送反馈 |
| `iTer://review` | 应用评分（StoreKit） |

默认：搜索、测验、收藏、反馈。可在 **设置 → 主屏快捷方式** 中排序或替换（最多 4 项）。应用以 **contains** 匹配 type，兼容包含上述路径的历史变体。

## 小组件深度链接

| 小组件 | 典型 URL |
|--------|----------|
| 每日一题 | `iTer://question?id=…` |
| 测验一览 | `iTer://quiz` |
| 收藏速览 | `iTer://favorites` |
| 错题速览 | `iTer://wrong` 或 `iTer://wrong?record=<UUID>` |

---

[返回爱技术支持页](../) · [常见问题](../faq) · [隐私政策](../privacy)

</section>
<section lang="zh-TW" markdown="1">

愛技術支援 **`iTer://`** URL Scheme（**iPhone / iPad**）。可在捷徑、Safari、小工具或其他 App 中開啟題目、每日測驗、收藏或錯題本。

**主畫面捷徑**（長按圖示）使用相同的 `type` 字串。在 **設定 → 主畫面捷徑** 中從 **7 項**裡最多選 **4 項**。

> **說明：** 深度連結僅用於**應用內跳轉**，不會遠端修改測驗設定或題目標記。**Mac** 無主畫面捷徑；小工具與應用內導覽在 Mac 上仍可用。

## 協定

```
iTer://<host>[?query]
```

| 規則 | 說明 |
|------|------|
| **Scheme** | `iTer`（大小寫不敏感） |
| **題目詳情** | Host `question` — 查詢參數 **`id=<題目ID>`** 或 **`q=<題目ID>`**（必填） |
| **每日測驗** | Host `quiz` |
| **收藏** | Host `favorites` → 設定 → 收藏列表 |
| **錯題本** | Host `wrong` / `mistakes` / `wrongquestions` — 可選 **`record=<UUID>`** 開啟單條錯題 |
| **搜尋** | Host `search` — 僅捷徑（開啟全域搜尋 Tab） |
| **分類** | Host `categories` — 僅捷徑（開啟分類 Tab） |
| **回饋** | Host `feedback` — 僅捷徑（郵件撰寫或 `mailto:` 回退） |
| **評分** | Host `review` — 僅捷徑（StoreKit 應用內評分）。含 `star` 的舊 type 仍相容 |

## 範例

```
iTer://question?id=94c34bb2bdef11e6a0e100163e0021c8
iTer://quiz
iTer://favorites
iTer://wrong
iTer://wrong?record=550E8400-E29B-41D4-A716-446655440000
```

## 主畫面捷徑

| Type | 用途 |
|------|------|
| `iTer://search` | 全域搜尋 |
| `iTer://quiz` | 每日測驗 Tab |
| `iTer://favorites` | 收藏列表 |
| `iTer://wrong` | 錯題本 |
| `iTer://categories` | 分類 Tab |
| `iTer://feedback` | 傳送回饋 |
| `iTer://review` | 應用評分（StoreKit） |

預設：搜尋、測驗、收藏、回饋。可在 **設定 → 主畫面捷徑** 中排序或替換（最多 4 項）。應用以 **contains** 匹配 type，相容包含上述路徑的歷史變體。

## 小工具深度連結

| 小工具 | 典型 URL |
|--------|----------|
| 每日一題 | `iTer://question?id=…` |
| 測驗一覽 | `iTer://quiz` |
| 收藏速覽 | `iTer://favorites` |
| 錯題速覽 | `iTer://wrong` 或 `iTer://wrong?record=<UUID>` |

---

[返回愛技術支援頁](../) · [常見問題](../faq) · [隱私政策](../privacy)

</section>
<section lang="ja" markdown="1">

iTer は、**iPhone と iPad** の**     ** URLスキームをサポートしています。 ショートカット、Safari、ウィジェット、またはその他のアプリで質問、毎日のクイズ、お気に入り、または間違ったanswerブックを開きます。

**ホーム画面クイックアクション**(アプリアイコンを長押し)は、同じ `iTer://` 文字列を再利用します。 **7**オプションから**4**まで選択します。

> **注記:** アプリ内のディープリンク**navigate** クイズの設定を変更したり、質問をリモートでマークしたりすることはありません。 **Mac**はホーム画面のクイックアクションを登録しません。 ウィジェットとアプリ内ナビゲーションはMac上で動作します。

## プロトコル


```
iTer://<host>[?query]
```


| Rule | 詳細を見る |
|------|--------|
| **Scheme** | `iTer` (ケースインセンティブ) |
| **Question detail** | ホスト `question` — クエリ`id=<questionID>`** または**`q=<questionID>`** (必須) |
| **Daily Quiz** | ホスト `quiz` |
| **Favourites** | ホスト `favorites` → 設定 → お気に入りリスト |
| **Wrong book** | ホスト `wrong`、 `mistakes`、または `wrongquestions` — オプション **`record=<UID>`** 1つの間違いを開く |
| **Search** | ホスト `search` — クイックアクション / ショートカットのみ (グローバル検索タブを開きます) |
| **Categories** | ホスト `categories` — クイックアクション / ショートカットのみ (カテゴリタブを開く) |
| **Feedback** | ホスト `feedback` — クイックアクションのみ (メールコンポースまたは `mailto:` フォールバック) |
| **Rate app** | ホスト `review` — クイックアクションのみ (StoreKit アプリ内レビュー)。 `star` を含むレガシータイプも機能します。 |

ホストが空の場合、 `iTer://` などのパスが受け入れられ、パスセグメントがマッチします。

## 例


```
iTer://question?id=94c34bb2bdef11e6a0e100163e0021c8
iTer://quiz
iTer://favorites
iTer://wrong
iTer://wrong?record=550E8400-E29B-41D4-A716-446655440000
```


## ホーム スクリーンの速い行為

| Type | 典型的な使用 |
|------|-------------|
| `iTer://search` | グローバル検索 |
| `iTer://quiz` | 毎日のクイズタブ |
| `iTer://favorites` | お気に入りリスト |
| `iTer://wrong` | 間違ったanswerブック |
| `iTer://categories` | カテゴリー タブ |
| `iTer://feedback` | フィードバックを送信 |
| `iTer://review` | アプリのレート(StoreKit) |

デフォルト選択: 検索、クイズ、お気に入り、フィードバック。 *Settings → Home Screen Shortcuts** (max 4) で注文または交換します。 app は、**contains** でショートカット `iTer://` 文字列にマッチします。そのため、これらのパスを含むレガシーなバリアントは正しくルートされます。

## ウィジェットディープリンク

| Widget | 典型的な URL |
|--------|-------------|
| Daily Question | `iTer://question?id=...` |
| Quiz Glance | ツイート |
| Favourites Glance | お気に入り |
| Wrong Book Glance | `iTer://wrong` または `iTer://wrong?record=<UUID>` |

---

[iTerサポートに戻る](../)・ [FAQ](../faq)・ [プライバシーポリシー](../privacy)

</section>
<section lang="ko" markdown="1">

iTer는 ** `iTer://` ** URL 계획 **iPhone 및 iPad**를 지원합니다. Shortcuts, Safari, 위젯, 또는 다른 앱에서 질문을 열고, 매일 퀴즈, 즐겨 찾기, 또는 잘못된-answer 책.

**홈 화면 Quick Actions** (앱 아이콘을 길게 누르십시오) `iTer://` 문자열을 재사용합니다. **7 ** 옵션 ** 설정 → 홈 화면 단축 **에서 ** 4**까지 선택하십시오.

> **참고:** 딥 링크 **navigate** 앱 내부. 그들은 퀴즈 설정을 변경하지 않거나 질문을 원격으로 표시하지 않습니다. **Mac**는 홈 화면 빠른 동작을 등록하지 않습니다. 위젯과 인앱 탐색은 여전히 Mac에서 작동합니다.

## 프로젝트


```
iTer://<host>[?query]
```


| Rule | 제품 정보 |
|------|--------|
| **Scheme** | `iTer` (case-insensitive)를 호출합니다. |
| **Question detail** | 호스트 `question` — 쿼리 **`id=<questionID>`** 또는 **`q=<questionID>`** (필수) |
| **Daily Quiz** | 호스트 `quiz` |
| **Favourites** | 호스트 `favorites` → 설정 → Favourites 목록 |
| **Wrong book** | 호스트 `wrong`, `mistakes`, 또는 `wrongquestions` — 옵션 **`record=<UUID>`**는 한 실수를 엽니다. |
| **Search** | Host `search` — Quick Action / 단축키 만 (글로벌 검색 탭 열기) |
| **Categories** | 호스트 `categories` — 빠른 행동 / 단축키 만 (카테고리 카테고리 탭 열기) |
| **Feedback** | 호스트 `feedback` - 빠른 행동 만 (이메일 compose 또는 `mailto:` fallback) |
| **Rate app** | 호스트 `review` — Quick Action only (StoreKit in-app review). 'star'도 일하는 레거시 유형. | `iTer://` 과 같은 경로는 호스트가 비어있을 때 허용됩니다.

## 예시


```
iTer://question?id=94c34bb2bdef11e6a0e100163e0021c8
iTer://quiz
iTer://favorites
iTer://wrong
iTer://wrong?record=550E8400-E29B-41D4-A716-446655440000
```


## 홈 화면 빠른 행동

| Type | 일반 사용 |
|------|-------------|
| `iTer://search` | 글로벌 검색 |
| `iTer://quiz` | 매일 퀴즈 탭 |
| `iTer://favorites` | Favourites 목록 |
| `iTer://wrong` | Wrong-answer 책 |
| `iTer://categories` | 카테고리 탭 |
| `iTer://feedback` | 견적 요청 |
| `iTer://review` | 앱 평가 (StoreKit) |

기본 선택: 검색, Quiz, Favourites, 피드백. 주문 또는 ** 설정 → 홈 화면 단축키 ** (최대 4). app match shortcut `iTer://` strings with**contains**, 이 경로는 여전히 올바른 경로가 포함 된 유산 변형.

## Widget 깊은 링크

| Widget | 일반적인 URL |
|--------|-------------|
| Daily Question | `iTer://question?id=...` |
| Quiz Glance | `iTer://quiz```````` |
| Favourites Glance | `iTer://favorites`````` |
| Wrong Book Glance | `iTer://wrong` 또는 `iTer://wrong?record=<UUID>` |

---

[iTer Support로 돌아가기](../) · [FAQ](../faq) · [Privacy Policy](../privacy)

</section>
<section lang="ru" markdown="1">

iTer поддерживает схему URL ** `iTer://` ** на **iPhone и iPad**. Используйте его в ярлыках, Safari, виджетах или других приложениях, чтобы открыть вопрос, ежедневную викторину, любимые или книгу с неправильным ответом.

**Home Screen Quick Actions** (долгое нажатие значка приложения) повторно использовать те же `iTer://` строки. Выберите до **4** из **7** вариантов в **Настройки → Ярлыки домашнего экрана **.

> **Примечание: ** Глубокие ссылки ** перемещаются ** внутри приложения. Они не меняют настройки викторины или помечают вопросы удаленно. Mac не регистрирует быстрые действия на домашнем экране; виджеты и навигация в приложении все еще работают на Mac.

## Протокол


```
iTer://<host>[?query]
```


| Rule | Подробнее |
|------|--------|
| **Scheme** | iTer (случайно нечувствительный) |
| **Question detail** | Ведущий "вопрос" - запрос **'id=<questionID>** или **'q=<questionID>** (обязательно) |
| **Daily Quiz** | Ведущий «Викторины» |
| **Favourites** | Host 'favorites' → Настройки → Список избранных |
| **Wrong book** | Ведущий «неправильный», «ошибки» или «неправильные вопросы» — необязательный **'record = <UUID>** открывает одну ошибку |
| **Search** | Host 'search' — Quick Action / shortcut only (открывает глобальную вкладку поиска) |
| **Categories** | Host 'categories' — Quick Action / shortcut only (открывает вкладку Категории) |
| **Feedback** | Host ‘feedback’ — Quick Action only (mail compose или ‘mailto:’ fallback) |
| **Rate app** | Host ‘review’ — Quick Action only (обзор в приложении). Наследственные типы, содержащие «звезду», также работают. |

Пути, такие как `iTer://` , принимаются, когда хост пуст и сегмент пути совпадает.

## Примеры


```
iTer://question?id=94c34bb2bdef11e6a0e100163e0021c8
iTer://quiz
iTer://favorites
iTer://wrong
iTer://wrong?record=550E8400-E29B-41D4-A716-446655440000
```


## Домой Экран Быстрые действия

| Type | Типичное использование |
|------|-------------|
| `iTer://search` | Глобальный поиск |
| `iTer://quiz` | Ежедневная вкладка Quiz |
| `iTer://favorites` | Любимый список |
| `iTer://wrong` | Книга неправильных ответов |
| `iTer://categories` | Закладка категорий |
| `iTer://feedback` | Отправить отзыв |
| `iTer://review` | Оценить приложение (StoreKit) |

Выбор по умолчанию: Поиск, Quiz, Фавориты, Обратная связь. Переупорядочение или замена в **Настройки → Ярлыки домашнего экрана ** (макс 4). Приложение соответствует ярлыку `iTer://` строк с **содержит **, поэтому устаревшие варианты, которые включают эти пути, все еще правильно маршрутизируются.

## Виджеты Deep Links

| Widget | Типичный URL |
|--------|-------------|
| Daily Question | ITer://question?id=... |
| Quiz Glance | "iTer://quiz" |
| Favourites Glance | "iTer://favorites" |
| Wrong Book Glance | «iTer://wrong» или «iTer://wrong?record» |

---

[Назад в поддержку iTer] (../) · [FAQ] (../faq) · [Политика конфиденциальности] (../privacy)

</section>
<section lang="th" markdown="1">

iTer รองรับรูปแบบแฟ้ม ~ `iTer://` BAR ~ ที่อยู่ URL บน ~ โทรศัพท์และไอแพด~. ใช้ในทางลัด, ซาฟารี, วิดเจ็ต หรือแอพอื่นๆ เพื่อเปิดคําถาม, ข้อสอบประจําวัน, ของโปรด, หรือหนังสือเล่มอื่น

~Home screen application] ~ (กดดันไอคอนแอพมานาน) เรียกคืน BAR ข้อความเดิม เลือกขึ้นไปจนถึง ~4 ~ ~ จาก < 7~ ~ ตัวเลือกใน~. การตั้งค่า หน้าจอจอหลัก ~.

> ~ ข้อสังเกต: ~ ลิงก์ลึก~ พวก เขา ไม่ เปลี่ยน รูป แบบ การ ตั้ง คํา ถาม หรือ ทํา เครื่องหมาย คํา ถาม ที่ อยู่ ห่าง ไกล. ~Mac~ ไม่ได้ลงทะเบียนการกระทําด่วนของหน้าจอบ้าน; วิดเจ็ตและการนําร่องภายในยังคงทํางานได้บน Mac

## โพรโทคอล


```
iTer://<host>[?query]
```


| Rule | รายละเอียด |
|------|--------|
| **Scheme** | 'ITER' (ถ้าอ่อนไหว) |
| **Question detail** | โฮสต์ "คําถาม" — สืบค้น- |
| **Daily Quiz** | โฮสต์ |
| **Favourites** | โฮสต์ |
| **Wrong book** | โฮสต์ 'ผิดพลาด' หรือ 'ความผิดพลาด' -- October=[UUUUID] 'เปิดโอกาสแห่งความผิดพลาด' |
| **Search** | โฮสต์ `การค้นหา' — การกระทําด่วน / ปุ่มพิมพ์ลัด (เปิดแท็บ การค้นหาทั่วโลก) |
| **Categories** | เครื่องโฮสต์ |
| **Feedback** | โฮสต์ 'ป้อนข้อมูล' — การกระทําด่วนเท่านั้น (เขียนจดหมายหรือ `mail to:' ถอยกลับ) |
| **Rate app** | โฮสต์ 'review' — การกระทําด่วนเท่านั้น (การทบทวนข้อมูล). ประเภทมรดกที่บรรจุ 'ดาว' ด้วยการทํางาน |

พาธต่าง ๆ เช่น   c0    ยอมรับเมื่อเครื่องว่าง และพาธที่ตรงกัน

## ตัวอย่าง


```
iTer://question?id=94c34bb2bdef11e6a0e100163e0021c8
iTer://quiz
iTer://favorites
iTer://wrong
iTer://wrong?record=550E8400-E29B-41D4-A716-446655440000
```


## การกระทําด่วนของจอส่วนตัว

| Type | ปกติ |
|------|-------------|
| `iTer://search` | การค้นหาทั่วไป |
| `iTer://quiz` | แท็บของเดลี่ Quiz |
| `iTer://favorites` | รายการโปรด |
| `iTer://wrong` | สมุดที่อยู่ไม่ถูกต้อง |
| `iTer://categories` | แท็บหมวดหมู่ |
| `iTer://feedback` | ส่งการตอบกลับ |
| `iTer://review` | จัดอันดับโปรแกรม (หยุดชั่วคราว) |

เลือกรายการปริยาย: สืบค้น, สืบค้น, Quiz, Februarys, Footback จัดลําดับหรือแทนที่ใน~ เซตเซตส์ หน้าจอส่วนตัว ~ (Max 4). แอพพลิเคชันนี้ตรงกับปุ่มพิมพ์ลัด `iTer://` สตริงพร้อมกับ ~passwords ~ ดังนั้นข้อมูลมรดกที่รวมเส้นทางเหล่านี้ยังคงไม่ถูกต้อง

## ส่วนเชื่อมโยงลึกของวิดเจ็ต

| Widget | ที่อยู่ URL ปกติ |
|--------|-------------|
| Daily Question | ที่ปรึกษา 'The Ter Tailion? id=...' |
| Quiz Glance | ~โอ้~ |
| Favourites Glance | ~คนสวย~ |
| Wrong Book Glance | บันทึก = (UUUID)' |

---

[การรองรับ iTer] [./] [FAQ] [./faq]

</section>
<section lang="de" markdown="1">

iTer unterstützt das URL-Schema ** `iTer://` ** auf **iPhone und iPad**. Verwenden sie es in shortcuts, safari, widgets oder anderen apps, um eine frage, das tägliche quiz, favoriten oder das falsche antwortbuch zu öffnen.

** Quick Actions** (langes Drücken des App-Symbols) verwenden die gleichen `iTer://` -Strings wieder. Wählen Sie bis zu **4** aus **7** Optionen in **Einstellungen → Home Screen Shortcuts **.

> **Hinweis:** Deep Links **navigate** innerhalb der App. Sie ändern keine Quizeinstellungen oder markieren Fragen aus der Ferne. **Mac** registriert keine Quick Actions für den Startbildschirm; Widgets und In-App-Navigation funktionieren weiterhin auf dem Mac.

## Protokoll


```
iTer://<host>[?query]
```


| Rule | Einzelheiten |
|------|--------|
| **Scheme** | "iTer" (fallunempfindlich) |
| **Question detail** | Host `question` — abfrage **`id=<questionID>`** oder **`q=<questionID>`** (erforderlich) |
| **Daily Quiz** | Host "Quiz" |
| **Favourites** | Host `Favoriten` → Einstellungen → Favoritenliste |
| **Wrong book** | Host `falsch`, `Fehler` oder `falsche Fragen` — optional **`record=<UUID>`** öffnet einen Fehler |
| **Search** | Host `search` — Quick Action / Shortcut only (öffnet globale Such-Tab) |
| **Categories** | Host `categories` — Quick Action / shortcut only (öffnet die Registerkarte Kategorien) |
| **Feedback** | Host `Feedback` — Quick Action only (mail compose oder `mailto:` fallback) |
| **Rate app** | Host `review` — Quick Action only (StoreKit in-app review). Legacy-Typen, die "Sterne" enthalten, funktionieren ebenfalls. |

Pfade wie `iTer://` werden akzeptiert, wenn der Host leer ist und das Pfadsegment übereinstimmt.

## Beispiele


```
iTer://question?id=94c34bb2bdef11e6a0e100163e0021c8
iTer://quiz
iTer://favorites
iTer://wrong
iTer://wrong?record=550E8400-E29B-41D4-A716-446655440000
```


## Home Bildschirm Schnelle Aktionen

| Type | Typische Verwendung |
|------|-------------|
| `iTer://search` | Globale Suche |
| `iTer://quiz` | Täglicher Quiz Tab |
| `iTer://favorites` | Favoritenliste |
| `iTer://wrong` | Falsches Antwortbuch |
| `iTer://categories` | Tab Kategorien |
| `iTer://feedback` | Feedback senden |
| `iTer://review` | Bewerten Sie die App (StoreKit) |

Standardauswahl: Suche, Quiz, Favoriten, Feedback. Bestellen oder ersetzen Sie in ** Einstellungen → Home Screen Shortcuts ** (max 4). Die App passt die Verknüpfung `iTer://` Strings mit **enthält **, so dass Legacy-Varianten, die diese Pfade enthalten, immer noch korrekt routen.

## Widget Deep Links

| Widget | Typische URL |
|--------|-------------|
| Daily Question | „iTer://question?id=... |
| Quiz Glance | „iTer://quiz |
| Favourites Glance | „iTer://favorites |
| Wrong Book Glance | `iTer://wrong` oder `iTer://wrong?record=<UUID>` |

---

[Zurück zu iTer Support](../) · [FAQ](../faq) · [Privacy Policy](../Privacy)

</section>
<section lang="fr" markdown="1">

iTer supporte le schéma d'URL ** `iTer://` ** sur **iPhone et iPad**. Utilisez-le dans Raccourcis, Safari, Widgets, ou d'autres applications pour ouvrir une question, le quiz quotidien, les favoris, ou le livre de mauvaise réponse.

**Actions rapides à l'écran d'accueil** (appuyer sur l'icône de l'application) réutiliser les mêmes chaînes `iTer://` . Choisissez jusqu'à **4** parmi **7** options dans **Paramètres → raccourcis d'écran d'accueil**.

> **Note:** Liens profonds **navigate** dans l'application. Ils ne changent pas les paramètres du quiz ou ne marquent pas les questions à distance. **Mac** ne enregistre pas Home Screen Quick Actions; les widgets et la navigation dans l'application fonctionnent toujours sur Mac.

## Protocole


```
iTer://<host>[?query]
```


| Rule | Détail |
|------|--------|
| **Scheme** | `iTer` (insensible aux cas) |
| **Question detail** | Question de l'hôte — requête **`id=<questionID>`** ou **`q=<questionID>`** (obligatoire) |
| **Daily Quiz** | Hébergement "quiz" |
| **Favourites** | Hôte `favorites` → Paramètres → Liste des favoris |
| **Wrong book** | Hôte `wrong`, `mistakes` ou `wrongquestions` — optionnel **`record=<UUID>`** ouvre une erreur |
| **Search** | Host `search` — Action rapide / raccourci uniquement (ouvre l'onglet recherche globale) |
| **Categories** | Hôte `category` — Action rapide / raccourci uniquement (ouvre l'onglet Catégories) |
| **Feedback** | Hôte `feedback` — Action rapide seulement (le courriel compose ou `mailto:` repli) |
| **Rate app** | Host `review` — Action rapide seulement (StoreKit in-app review). Les types d'héritage contenant "star" fonctionnent également. |

Des chemins tels que `iTer://` sont acceptés lorsque l'hôte est vide et que le segment de chemin correspond.

## Exemples


```
iTer://question?id=94c34bb2bdef11e6a0e100163e0021c8
iTer://quiz
iTer://favorites
iTer://wrong
iTer://wrong?record=550E8400-E29B-41D4-A716-446655440000
```


## Actions rapides de l'écran d'accueil

| Type | Utilisation typique |
|------|-------------|
| `iTer://search` | Recherche mondiale |
| `iTer://quiz` | Onglet Quiz quotidien |
| `iTer://favorites` | Liste des favoris |
| `iTer://wrong` | Livre de réponses erronées |
| `iTer://categories` | Onglet Catégories |
| `iTer://feedback` | Envoyer des commentaires |
| `iTer://review` | Noter l'application (StoreKit) |

Sélection par défaut : Recherche, Quiz, Favoris, Commentaires. Réorganiser ou remplacer **Paramètres → raccourcis d'écran d'accueil** (maximum 4). L'application correspond à des chaînes de raccourci `iTer://` avec **contient**, de sorte que les variantes héritées qui incluent ces chemins suivent toujours correctement.

## Widget liens profonds

| Widget | URL typique |
|--------|-------------|
| Daily Question | `iTer://question?id=...` |
| Quiz Glance | 'iTer://quiz' |
| Favourites Glance | `iTer://favorites` |
| Wrong Book Glance | `iTer://wrong` ou `iTer://wrong?record=<UUID>` |

---

[Retour à iTer Support](../) · [FAQ](../faq) · [Politique de confidentialité](../privacy)

</section>
<section lang="tr" markdown="1">

iTer, ** `iTer://` ** URL programı **iPhone ve iPad** üzerinde destekler. Kısayollarda, Safari, widgets veya bir soru açmak için diğer uygulamalar, günlük sınav, favoriler veya yanlış cevap kitabı.

**Home Ekran Hızlı Eylemler ** (Uygulama ikonunu uzun baskı) aynı `iTer://` dizeleri tekrarlayın. **4 **'ye kadar seçin **7** seçeneklerinden **Sings → Ev Ekran kısayolları**.

> **Not: ** Deep Links **navigate** in the app. Test ayarlarını değiştirmiyor veya uzaktan soru işaret ediyor. **Mac**, Home Ekran Hızlı Eylemleri kaydetmez; widgets ve in-app navigation hala Mac üzerinde çalışır.

## Protokol Protokolü


```
iTer://<host>[?query]
```


| Rule | Detaylı Bilgi |
|------|--------|
| **Scheme** | "iTer" (case-in sensitive) |
| **Question detail** | Host "question" - query **'id=<questionID>' ** veya **'q=<questionID>'** (required) |
| **Daily Quiz** | Host "quiz" |
| **Favourites** | Host ‘favorites’ → Ayarlar |
| **Wrong book** | Host "wrong", "mistakes", ya da "wrongquestions" - Seçmeli **'record =<UID>"** bir hata açar |
| **Search** | Host "search" - Quick Action / kısayol sadece (yalnızca küresel arama sekmesini açın) |
| **Categories** | Host "categories" - Quick Action / kısayol sadece (opens Kategoriler sekme) |
| **Feedback** | Host "Liveback" – Quick Action sadece (mail oluşturma veya "mailto:' fallback) |
| **Rate app** | Host "Rekre" - Quick Action sadece (oyunKit in-app review). “star” da içeren Legacy türleri. |

Ev sahibi boş ve yol segment maçlarında `iTer://` gibi yollar kabul edilir.

## Örnekler


```
iTer://question?id=94c34bb2bdef11e6a0e100163e0021c8
iTer://quiz
iTer://favorites
iTer://wrong
iTer://wrong?record=550E8400-E29B-41D4-A716-446655440000
```


## Home Screen Quick Actions

| Type | Tipik kullanım kullanımı |
|------|-------------|
| `iTer://search` | Global arama |
| `iTer://quiz` | Daily Quiz sekmesi |
| `iTer://favorites` | Favourites listesi |
| `iTer://wrong` | Yanlış cevap kitabı |
| `iTer://categories` | Kategoriler sekmesi |
| `iTer://feedback` | Geri bildirimler gönder |
| `iTer://review` | Uygulamayı paylaşın ( MağazaKit) |

Varsayılan seçim: Arama, Quiz, Favourites, Feedback. Reorder veya **Settings → Home Ekran kısayolları** (max 4). Uygulama maçları, ** ile kısayollar ile kısayollar **, bu yolları hala doğru rotayı içeren bu tür değişiklikler.

## Widget derin bağlantılar

| Widget | Tipik URL URL URL |
|--------|-------------|
| Daily Question | "iTer http://question?id=" |
| Quiz Glance | "iTer httpquiz" |
| Favourites Glance | "iTer https://favorites" |
| Wrong Book Glance | "iTer httpwrong" veya "iTer http://wrong?record=<UID>" |

---

[Geride iTer Support](./) · [FAQ](./faq) · [Privacy Policy](./privacy)

</section>
