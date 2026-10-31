iSage поддерживает ярлыки ** `isage://` ** (схема URL). Холодный старт и ярлыки домашнего экрана доставляются через единый буфер, поэтому ссылки не открываются дважды после входа.

## Формат ссылки


```
isage://{host}?{params}
```


## Слова и авторы

| URL | Открывает |
|-----|-------|
| `isage://passage?id={id}` | Говорить детали |
| `isage://saying?id={id}` / `isage://couplet?id={id}` / `isage://poem?id={id}` | Совместимость (Compatibility) |
| `isage://passage?id={id}&card=1` | Сказать детали и лист шалфея |
| `isage://card?id={id}` / `isage://share-card?id={id}` | Мудрая карта |
| `isage://author?id={id}` | Страница автора |
| `isage://recite` / `isage://recite?id={id}` | Режим чтения вслух |

## Discovery & Practice

| URL | Открывает |
|-----|-------|
| `isage://home` | Главная |
| `isage://daily` | Сегодняшняя мудрость |
| `isage://random` | Случайные слова |
| `isage://favorites` | Избранное |
| `isage://famous` | Знаменитые строки |
| `isage://search` / `isage://search?q={query}` | Поиск |
| `isage://study` / `isage://study?id={id}` | Академия Мудрецов |
| `isage://hunt` | «Охота на мудрецов» («keyword-hunt» / «flyflower») |
| `isage://handwriting` | Поиск почерка («handwrite»; iOS) |
| `isage://mastered` | Мастеринг («Прогресс») |
| `isage://categories` / `isage://categories?section=` | Обзор |
| `isage://collection?id=guxun` | Классическая рецензия ('zhou-shang' / 'zhou-xia'; также 'книга' / 'форма') |
| `isage://corpus` | Все слова («All») |
| `isage://theme?id=conduct` | Тема (например, "культивация", "обучение", "дружба", "домохозяйство", "богатство", "добродетель", "счастье", "речь", "лояльность", "усердие", "мир") |
| `isage://last-read` | Последнее прочитанное |
| `isage://reading-history` | История чтения |
| `isage://notes` | Заметки |

## Настройки и руководства

| URL | Открывает |
|-----|-------|
| `isage://settings` | Настройки |
| `isage://usage-guide` | Руководство по использованию |
| `isage://widget-guide` | Руководство по виджетам |
| `isage://shortcuts-guide` | Руководство по «Командам» |
| `isage://feature-guide` | Повторное знакомство |
| `isage://feedback` | Письмо с отзывом |
| `isage://in-app-review` | Отзыв в приложении / App Store |

## Примеры


```
isage://daily
isage://passage?id=1
isage://passage?id=1&card=1
isage://collection?id=guxun
isage://theme?id=conduct
isage://study
isage://hunt
isage://handwriting
```


## Заметки

- Параметры чувствительны к регистру, где идентификаторы являются числовыми.
- Siri, ярлыки, виджеты и элементы управления Центра управления используют одни и те же маршруты глубокой связи.
- Смотрите в приложении ** Настройки → Справочные руководства ** для последнего списка.


