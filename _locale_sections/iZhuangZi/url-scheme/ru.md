iZhuangZi поддерживает ярлыки ** `izhuangzi://` ** (схема URL). Холодный старт и ярлыки домашнего экрана доставляются через единый буфер, поэтому ссылки не открываются дважды после входа.

## Формат ссылки


```
izhuangzi://{host}?{params}
```


## Проходы и авторы

| URL | Открывает |
|-----|-------|
| `izhuangzi://passage?id={id}` | Страница отрывка |
| `izhuangzi://saying?id={id}` / `izhuangzi://couplet?id={id}` / `izhuangzi://poem?id={id}` | Совместимость (Compatibility) |
| `izhuangzi://passage?id={id}&card=1` | Детали проезда и карточный лист |
| `izhuangzi://card?id={id}` / `izhuangzi://share-card?id={id}` | карты |
| `izhuangzi://author?id={id}` | Страница автора |
| `izhuangzi://recite` / `izhuangzi://recite?id={id}` | Режим чтения вслух |

## Discovery & Practice

| URL | Открывает |
|-----|-------|
| `izhuangzi://home` | Главная |
| `izhuangzi://daily` | Daily Zhuangzi |
| `izhuangzi://random` | Случайный отрывок |
| `izhuangzi://favorites` | Избранное |
| `izhuangzi://famous` | Знаменитые строки |
| `izhuangzi://search` / `izhuangzi://search?q={query}` | Поиск |
| `izhuangzi://study` / `izhuangzi://study?id={id}` | Исследование Дао |
| `izhuangzi://hunt` | Чжуан Хант («охота за ключевыми словами» / «флайфлауэр») |
| `izhuangzi://handwriting` | Поиск почерка («handwrite»; iOS) |
| `izhuangzi://mastered` | Мастеринг («Прогресс») |
| `izhuangzi://categories` / `izhuangzi://categories?section=` | Обзор |
| `izhuangzi://collection?id=` | Коллекция/книга ('neipian'/ 'waipian'/'zapian') |
| `izhuangzi://corpus` | Все пассажи («All») |
| `izhuangzi://last-read` | Последнее прочитанное |
| `izhuangzi://reading-history` | История чтения |
| `izhuangzi://notes` | Заметки |
| `izhuangzi://ask` | Спроси у Чжуанци. |
| `izhuangzi://allegories` | Притчи |
| `izhuangzi://concepts` | Концепции |
| `izhuangzi://theme?id=neipian` | Внутренний / Внешний / Разное |

## Настройки и руководства

| URL | Открывает |
|-----|-------|
| `izhuangzi://settings` | Настройки |
| `izhuangzi://usage-guide` | Руководство по использованию |
| `izhuangzi://widget-guide` | Руководство по виджетам |
| `izhuangzi://shortcuts-guide` | Руководство по «Командам» |
| `izhuangzi://feature-guide` | Повторное знакомство |
| `izhuangzi://feedback` | Письмо с отзывом |
| `izhuangzi://in-app-review` | Отзыв в приложении / App Store |

## Примеры


```
izhuangzi://daily
izhuangzi://passage?id=1
izhuangzi://ask
izhuangzi://allegories
izhuangzi://collection?id=neipian
izhuangzi://study
izhuangzi://hunt
```


## Заметки

- Параметры чувствительны к регистру, где идентификаторы являются числовыми.
- Siri, ярлыки, виджеты и элементы управления Центра управления используют одни и те же маршруты глубокой связи.
- Смотрите в приложении ** Настройки → Справочные руководства ** для последнего списка.


