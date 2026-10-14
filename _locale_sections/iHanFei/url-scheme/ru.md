iHanFei поддерживает ярлыки ** `ihanfei://` ** (схема URL). Холодный старт и ярлыки домашнего экрана доставляются через единый буфер, поэтому ссылки не открываются дважды после входа.

## Формат ссылки


```
ihanfei://{host}?{params}
```


## Проходы и авторы

| URL | Открывает |
|-----|-------|
| `ihanfei://passage?id={id}` | Страница отрывка |
| `ihanfei://saying?id={id}` / `ihanfei://couplet?id={id}` / `ihanfei://poem?id={id}` | Совместимость (Compatibility) |
| `ihanfei://passage?id={id}&card=1` | Детали проезда и карточный лист |
| `ihanfei://card?id={id}` / `ihanfei://share-card?id={id}` | карточки |
| `ihanfei://author?id={id}` | Страница автора |
| `ihanfei://recite` / `ihanfei://recite?id={id}` | Режим чтения вслух |

## Discovery & Practice

| URL | Открывает |
|-----|-------|
| `ihanfei://home` | Главная |
| `ihanfei://daily` | Daily Stratagem |
| `ihanfei://random` | Случайный отрывок |
| `ihanfei://favorites` | Избранное |
| `ihanfei://famous` | Знаменитые строки |
| `ihanfei://search` / `ihanfei://search?q={query}` | Поиск |
| `ihanfei://study` / `ihanfei://study?id={id}` | Исследование легализма |
| `ihanfei://hunt` | «Охота за ключевыми словами» / «Flyflower» |
| `ihanfei://handwriting` | Поиск почерка («handwrite»; iOS) |
| `ihanfei://mastered` | Мастеринг («Прогресс») |
| `ihanfei://categories` / `ihanfei://categories?section=` | Обзор |
| `ihanfei://collection?id=` | Коллекция / книга |
| `ihanfei://corpus` | Все пассажи («All») |
| `ihanfei://last-read` | Последнее прочитанное |
| `ihanfei://reading-history` | История чтения |
| `ihanfei://notes` | Заметки |
| `ihanfei://fables` / `ihanfei://allegories` / `ihanfei://concepts` | Специальные полки, когда они доступны |

## Настройки и руководства

| URL | Открывает |
|-----|-------|
| `ihanfei://settings` | Настройки |
| `ihanfei://usage-guide` | Руководство по использованию |
| `ihanfei://widget-guide` | Руководство по виджетам |
| `ihanfei://shortcuts-guide` | Руководство по «Командам» |
| `ihanfei://feature-guide` | Повторное знакомство |
| `ihanfei://feedback` | Письмо с отзывом |
| `ihanfei://in-app-review` | Отзыв в приложении / App Store |

## Примеры


```
ihanfei://daily
ihanfei://passage?id=1
ihanfei://study
ihanfei://hunt
```



