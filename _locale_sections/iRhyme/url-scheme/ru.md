iRhyme поддерживает ярлыки ** `irhyme://` ** (схема URL). Холодный старт и ярлыки домашнего экрана доставляются через единый буфер, поэтому ссылки не открываются дважды после входа.

## Формат ссылки


```
irhyme://{host}?{params}
```


## Проходы и авторы

| URL | Открывает |
|-----|-------|
| `irhyme://passage?id={id}` | Страница отрывка |
| `irhyme://saying?id={id}` / `irhyme://couplet?id={id}` / `irhyme://poem?id={id}` | Совместимость (Compatibility) |
| `irhyme://passage?id={id}&card=1` | Детали проезда и карточный лист |
| `irhyme://card?id={id}` / `irhyme://share-card?id={id}` | Карты ритма |
| `irhyme://author?id={id}` | Страница автора |
| `irhyme://recite` / `irhyme://recite?id={id}` | Режим чтения вслух |

## Discovery & Practice

| URL | Открывает |
|-----|-------|
| `irhyme://home` | Главная |
| `irhyme://daily` | Сегодняшний ритм |
| `irhyme://random` | Случайный отрывок |
| `irhyme://favorites` | Избранное |
| `irhyme://famous` | Знаменитые строки |
| `irhyme://search` / `irhyme://search?q={query}` | Поиск |
| `irhyme://study` / `irhyme://study?id={id}` | Академия Rhyme |
| `irhyme://hunt` | Rhyme Hunt («охота за ключевыми словами» / «флайфлауэр») |
| `irhyme://handwriting` | Поиск почерка («handwrite»; iOS) |
| `irhyme://mastered` | Мастеринг («Прогресс») |
| `irhyme://categories` / `irhyme://categories?section=` | Обзор |
| `irhyme://collection?id=` | Коллекция/книга ('shenglv'/'liweng'/'qianjia'/'youxue') |
| `irhyme://corpus` | Все пассажи («All») |
| `irhyme://last-read` | Последнее прочитанное |
| `irhyme://reading-history` | История чтения |
| `irhyme://notes` | Заметки |
| `irhyme://pair` | Практика параллелизма |
| `irhyme://prosody` | Стол для просодия |
| `irhyme://rhyme?id=dong` | Один класс рифмы |
| `irhyme://compare?rhyme=dong` | Сравнение одной и той же рифмы |
| `irhyme://glossary?id=` | Глоссарий |

## Настройки и руководства

| URL | Открывает |
|-----|-------|
| `irhyme://settings` | Настройки |
| `irhyme://usage-guide` | Руководство по использованию |
| `irhyme://widget-guide` | Руководство по виджетам |
| `irhyme://shortcuts-guide` | Руководство по «Командам» |
| `irhyme://feature-guide` | Повторное знакомство |
| `irhyme://feedback` | Письмо с отзывом |
| `irhyme://in-app-review` | Отзыв в приложении / App Store |

## Примеры


```
irhyme://daily
irhyme://passage?id=1001
irhyme://pair
irhyme://compare?rhyme=dong
irhyme://collection?id=shenglv
irhyme://study
irhyme://hunt
```


## Заметки

- Параметры чувствительны к регистру, где идентификаторы являются числовыми.
- Siri, ярлыки, виджеты и элементы управления Центра управления используют одни и те же маршруты глубокой связи.
- Смотрите в приложении ** Настройки → Справочные руководства ** для последнего списка.


