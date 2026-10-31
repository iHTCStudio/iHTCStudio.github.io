iLvShi поддерживает ярлыки ** `ilvshi://` ** (схема URL). Холодный старт и ярлыки домашнего экрана доставляются через единый буфер, поэтому ссылки не открываются дважды после входа.

## Формат ссылки


```
ilvshi://{host}?{params}
```


## Проходы и авторы

| URL | Открывает |
|-----|-------|
| `ilvshi://passage?id={id}` | Страница отрывка |
| `ilvshi://saying?id={id}` / `ilvshi://couplet?id={id}` / `ilvshi://poem?id={id}` | Совместимость (Compatibility) |
| `ilvshi://passage?id={id}&card=1` | Детали проезда и карточный лист |
| `ilvshi://card?id={id}` / `ilvshi://share-card?id={id}` | карты |
| `ilvshi://author?id={id}` | Страница автора |
| `ilvshi://recite` / `ilvshi://recite?id={id}` | Режим чтения вслух |

## Discovery & Practice

| URL | Открывает |
|-----|-------|
| `ilvshi://home` | Главная |
| `ilvshi://daily` | Ежедневный проход |
| `ilvshi://random` | Случайный отрывок |
| `ilvshi://favorites` | Избранное |
| `ilvshi://famous` | Знаменитые строки |
| `ilvshi://search` / `ilvshi://search?q={query}` | Поиск |
| `ilvshi://study` / `ilvshi://study?id={id}` | Весеннее-осеннее исследование |
| `ilvshi://hunt` | Осенняя охота («охота за ключевыми словами» / «флайфлауэр») |
| `ilvshi://handwriting` | Поиск почерка («handwrite»; iOS) |
| `ilvshi://mastered` | Мастеринг («Прогресс») |
| `ilvshi://categories` / `ilvshi://categories?section=` | Обзор |
| `ilvshi://collection?id=` | Коллекция / книга |
| `ilvshi://corpus` | Все пассажи («All») |
| `ilvshi://last-read` | Последнее прочитанное |
| `ilvshi://reading-history` | История чтения |
| `ilvshi://notes` | Заметки |
| `ilvshi://fables` / `ilvshi://allegories` / `ilvshi://concepts` | Специальные полки, когда они доступны |

## Настройки и руководства

| URL | Открывает |
|-----|-------|
| `ilvshi://settings` | Настройки |
| `ilvshi://usage-guide` | Руководство по использованию |
| `ilvshi://widget-guide` | Руководство по виджетам |
| `ilvshi://shortcuts-guide` | Руководство по «Командам» |
| `ilvshi://feature-guide` | Повторное знакомство |
| `ilvshi://feedback` | Письмо с отзывом |
| `ilvshi://in-app-review` | Отзыв в приложении / App Store |

## Примеры


```
ilvshi://daily
ilvshi://passage?id=1
ilvshi://study
ilvshi://hunt
```



