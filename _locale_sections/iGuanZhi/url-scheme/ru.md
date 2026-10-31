iGuanZhi поддерживает ярлыки ** `iguanzhi://` ** (схема URL). Холодный старт и ярлыки домашнего экрана доставляются через единый буфер, поэтому ссылки не открываются дважды после входа.

## Формат ссылки


```
iguanzhi://{host}?{params}
```


## Проходы и авторы

| URL | Открывает |
|-----|-------|
| `iguanzhi://passage?id={id}` | Страница отрывка |
| `iguanzhi://saying?id={id}` / `iguanzhi://couplet?id={id}` / `iguanzhi://poem?id={id}` | Совместимость (Compatibility) |
| `iguanzhi://passage?id={id}&card=1` | Детали проезда и карточный лист |
| `iguanzhi://card?id={id}` / `iguanzhi://share-card?id={id}` | карты |
| `iguanzhi://author?id={id}` | Страница автора |
| `iguanzhi://recite` / `iguanzhi://recite?id={id}` | Режим чтения вслух |

## Discovery & Practice

| URL | Открывает |
|-----|-------|
| `iguanzhi://home` | Главная |
| `iguanzhi://daily` | Сегодняшнее эссе |
| `iguanzhi://random` | Случайный отрывок |
| `iguanzhi://favorites` | Избранное |
| `iguanzhi://famous` | Знаменитые строки |
| `iguanzhi://search` / `iguanzhi://search?q={query}` | Поиск |
| `iguanzhi://study` / `iguanzhi://study?id={id}` | Изучение классики |
| `iguanzhi://hunt` | Эссе Хант («охота за ключевыми словами» / «флайфлауэр») |
| `iguanzhi://handwriting` | Поиск почерка («handwrite»; iOS) |
| `iguanzhi://mastered` | Мастеринг («Прогресс») |
| `iguanzhi://categories` / `iguanzhi://categories?section=` | Обзор |
| `iguanzhi://collection?id=` | Коллекция / книга |
| `iguanzhi://corpus` | Все пассажи («All») |
| `iguanzhi://last-read` | Последнее прочитанное |
| `iguanzhi://reading-history` | История чтения |
| `iguanzhi://notes` | Заметки |
| `iguanzhi://fables` / `iguanzhi://allegories` / `iguanzhi://concepts` | Специальные полки, когда они доступны |

## Настройки и руководства

| URL | Открывает |
|-----|-------|
| `iguanzhi://settings` | Настройки |
| `iguanzhi://usage-guide` | Руководство по использованию |
| `iguanzhi://widget-guide` | Руководство по виджетам |
| `iguanzhi://shortcuts-guide` | Руководство по «Командам» |
| `iguanzhi://feature-guide` | Повторное знакомство |
| `iguanzhi://feedback` | Письмо с отзывом |
| `iguanzhi://in-app-review` | Отзыв в приложении / App Store |

## Примеры


```
iguanzhi://daily
iguanzhi://passage?id=1
iguanzhi://study
iguanzhi://hunt
```



