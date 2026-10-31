iCangJie поддерживает ** `iCangJie://` ** URL-схема глубоких ссылок — открытый поиск в поиске, детали текста, Daily Quiz, Typing, Favorites, Wrong Book, Levels или Learn from Safari, другое приложение, QR-код, кран виджета или ярлыки Apple.

Параллельный набор **Home Screen Quick Actions** (иконка приложения с длинным нажатием) охватывает дополнительные направления, такие как поиск, обратная связь и скорость. Настройка до 4 ярлыков в ** Настройки → Настройки приложений → Настройки домашнего экрана **.

## Спецификация протокола


```
iCangJie://<host>[?query]
```


| Rule | Подробнее |
|------|--------|
| **Scheme** | «icangjie» / «iCangJie» — сравнительный случай |
| **Host routing** | Основным маршрутизатором является URL **host** |
| **Query aliases** | «q», «word» и «name» являются взаимозаменяемыми для хостов поиска/слова. |
| **Parser** | «ICangJieDeepLink.parse( :)» — потребляется через «onOpenURL» → «AppRouter.pendingDeepLink» |

** Три канала доставки**

| Channel | Handled by | Примеры |
|---------|------------|----------|
| **Universal deep link** (`onOpenURL`) | `ICangJieDeepLink.parse` → `RootTabView` | «поиск», «слово», «викторина», «типирование», «любимые», «неправильные», «уровни», «учиться» |
| **Home Screen Quick Action** | `ShortcutObserver.dispatch` | «поиск», «викторина», «любимые», «неправильные», «уровни», «обратная связь», «обзор» |
| **App Intents / Siri / Widget pending URL** | Writes `AppGroup.pendingDeepLinkURL` → `RootTabView.consumePendingDeepLinkFromAppGroup()` | Код поиска, начало викторины, открытый поиск |

Типы быстрого действия используют ** `iCangJie://` **, совпадающие по строке типа, поэтому как `icangjie` , так и унаследованные варианты все еще маршрутизируются правильно.

---

## 1.В поисках.

Откройте вкладку **Lookup**. Опционально заполните поле поиска.

| Parameter | Required | Описание |
|-----------|----------|-------------|
| `q` | No | Поисковый запрос (префикс кода, символ, пиньинь или Jyutping) |
| `word` | No | Синонимы к «q» |
| `name` | No | Синонимы к «q» |

Открытый поиск (Open Lookup)


```
iCangJie://search
```


**Поиск префикса кода `iCangJie://` **


```
iCangJie://search?q=ab
```


**Поиск персонажа **


```
iCangJie://search?q=颉
```


---

## 2. Подробнее

Откройте страницу деталей для одного персонажа. Требуется не пустой запрос.

| Parameter | Required | Описание |
|-----------|----------|-------------|
| `q` | One of `q` / `word` / `name` | Персонаж Target Han |
| `word` | One of `q` / `word` / `name` | Синонимы к «q» |
| `name` | One of `q` / `word` / `name` | Синонимы к «q» |

** Принимаемые хосты: ** `iCangJie://` , `icangjie` , `iCangJie` **Открытая деталь для  **


```
iCangJie://word?q=倉
```


Альтернативный хост:


```
iCangJie://character?word=颉
```


Если запрос ** пуст или символ не в словаре **, ссылка ** молча игнорируется **.

---

## 3. Daily Quiz

Прыгайте прямо в ежедневный квиз. Не запускает и не пропускает вопросы.


```
iCangJie://quiz
```


Алиасы: `iCangJie://` ---

## 4.Типирование

Откройте **Typing** tab hub.


```
iCangJie://typing
```


Алиасы: `iCangJie://` , `icangjie` ---

## 5. Любимые

Откройте список **Любимые **.


```
iCangJie://favorites
```


Алиас: `iCangJie://` ---

## 6.Неправильный ответ

### 6.1 Список

Откройте список «Книга неправильных ответов».


```
iCangJie://wrong
```


Алиасы: `iCangJie://` , `icangjie` ### 6.2 Единый рекорд

Когда `iCangJie://` является действительным UUID сохраненной записи с неверным ответом, приложение открывает детали слова записи (если запись все еще существует).

| Parameter | Required | Формат |
|-----------|----------|--------|
| `record` | Yes | струна UUID |
| `id` | Yes | Синонимы к «Record» |


```
iCangJie://wrong?record=550e8400-e29b-41d4-a716-446655440000
```


---

## 7. Уровни (длина кода)

Откройте вкладку **Levels**.


```
iCangJie://levels
```


Алиасы: `iCangJie://` , `icangjie` ---

## 8.Учитесь (курсивы)

Откройте центр **Learn**.


```
iCangJie://learn
```


Алиасы: `iCangJie://` ---

## 9. Обратная связь (только быстрое действие)

Откройте предварительно заполненный почтовый композитор обратной связи (или `iCangJie://` fallback).


```
iCangJie://feedback
```


Обрабатывается **Home Screen Quick Action** / `iCangJie://` , а не `icangjie` .

---

## 10. Обзор App Store (только для быстрого действия)

Запросить отзыв в App Store.


```
iCangJie://review
```


Alias matching также принимает `iCangJie://` в строке типа быстрого действия.

---

## 11. App Intents & Siri (iOS 16+)

Встроенные ярлыки **App появляются в приложении Shortcuts и Siri. Каждое намерение устанавливает `iCangJie://` в группе приложений; приложение потребляет его при запуске.

| Intent | Action | В ожидании URL |
|--------|--------|-------------|
| **Look up Cangjie code** | Opens word detail for the given character | iCangJie://word?q=<char> |
| **Start daily quiz** | Opens Daily Quiz | "iCangJie://quiz" |
| **Open lookup search** | Opens Lookup tab | "iCangJie://поиск" |

** Примеры фраз Siri (английский)**

- *"Поищите код Cangjie для   в iCangJie"*
- «Начать ежедневную викторину в iCangJie»
- «Поиск Канджи в iCangJie»

В **Shortcuts** добавьте действие из раздела приложения iCangJie. Намерение **Look up** требует параметра **Chinese character** ( `iCangJie://` ).

> Намерения приложений **iOS только **. macOS полагается на `iCangJie://` URL и навигацию по меню.

---

## Виджет Deep Links

Виджеты нажимают на те же `iCangJie://` URL. Примеры:

| Widget | Типичный URL |
|--------|-------------|
| Daily Character | iCangJie://word?q=<char> |
| Code Length | "iCangJie://levels" |
| Daily Quiz | "iCangJie://quiz" |
| Typing Glance | "iCangJie://typing" |
| Favorites | "iCangJie://favorites" |
| Wrong Book | "iCangJie://wrong" |
| Recent | "iCangJie://поиск" |
| Learning Progress | "iCangJie://learn" |

---

## Короткие примеры

** Открытая сегодня викторина**


```
iCangJie://quiz
```


**Посмотрите на персонажа из клипборда**

Используйте ярлыки **Get Clipboard** action, затем **Open URL** с:


```
iCangJie://word?q=[Clipboard]
```


**Практика набора текста**


```
iCangJie://typing
```


---

## Домой Экран Быстрые действия

Нажмите на иконку приложения iCangJie. Варианты по умолчанию (выберите до 4 в настройках):

| Action | URL |
|--------|-----|
| Search | "iCangJie://поиск" |
| Daily Quiz | "iCangJie://quiz" |
| Favorites | "iCangJie://favorites" |
| Wrong Book | "iCangJie://wrong" |
| Code Length | "iCangJie://levels" |
| Feedback | "iCangJie://feedback" |
| Rate App | "iCangJie://review" |


