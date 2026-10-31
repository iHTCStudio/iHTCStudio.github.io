iMoZi поддерживает ярлыки ** `imozi://` ** (схема URL). Холодный старт и ярлыки домашнего экрана доставляются через единый буфер, поэтому ссылки не открываются дважды после входа.

## Формат ссылки


```
imozi://{host}?{params}
```


## Проходы и авторы

| URL | Открывает |
|-----|-------|
| `imozi://passage?id={id}` | Страница отрывка |
| `imozi://saying?id={id}` / `imozi://couplet?id={id}` / `imozi://poem?id={id}` | Совместимость (Compatibility) |
| `imozi://passage?id={id}&card=1` | Детали проезда и карточный лист |
| `imozi://card?id={id}` / `imozi://share-card?id={id}` | карты |
| `imozi://author?id={id}` | Страница автора |
| `imozi://recite` / `imozi://recite?id={id}` | Режим чтения вслух |

## Discovery & Practice

| URL | Открывает |
|-----|-------|
| `imozi://home` | Главная |
| `imozi://daily` | Сегодняшний Мо |
| `imozi://random` | Случайный отрывок |
| `imozi://favorites` | Избранное |
| `imozi://famous` | Знаменитые строки |
| `imozi://search` / `imozi://search?q={query}` | Поиск |
| `imozi://study` / `imozi://study?id={id}` | Исследование мохизма |
| `imozi://hunt` | Охота за ключевыми словами / Flyflower |
| `imozi://handwriting` | Поиск почерка («handwrite»; iOS) |
| `imozi://mastered` | Мастеринг («Прогресс») |
| `imozi://categories` / `imozi://categories?section=` | Обзор |
| `imozi://collection?id=` | Коллекция / книга |
| `imozi://corpus` | Все пассажи («All») |
| `imozi://last-read` | Последнее прочитанное |
| `imozi://reading-history` | История чтения |
| `imozi://notes` | Заметки |
| `imozi://ask` | Спроси у Моцзы. |
| `imozi://fables` / `imozi://allegories` / `imozi://concepts` | Специальные полки, когда они доступны |

## Настройки и руководства

| URL | Открывает |
|-----|-------|
| `imozi://settings` | Настройки |
| `imozi://usage-guide` | Руководство по использованию |
| `imozi://widget-guide` | Руководство по виджетам |
| `imozi://shortcuts-guide` | Руководство по «Командам» |
| `imozi://feature-guide` | Повторное знакомство |
| `imozi://feedback` | Письмо с отзывом |
| `imozi://in-app-review` | Отзыв в приложении / App Store |

## Примеры


```
imozi://daily
imozi://passage?id=1
imozi://ask
imozi://study
imozi://hunt
```



