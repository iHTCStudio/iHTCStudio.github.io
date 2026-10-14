iXunZi поддерживает ярлыки ** `ixunzi://` ** (схема URL). Холодный старт и ярлыки домашнего экрана доставляются через единый буфер, поэтому ссылки не открываются дважды после входа.

## Формат ссылки


```
ixunzi://{host}?{params}
```


## Проходы и авторы

| URL | Открывает |
|-----|-------|
| `ixunzi://passage?id={id}` | Страница отрывка |
| `ixunzi://saying?id={id}` / `ixunzi://couplet?id={id}` / `ixunzi://poem?id={id}` | Совместимость (Compatibility) |
| `ixunzi://passage?id={id}&card=1` | Детали проезда и карточный лист |
| `ixunzi://card?id={id}` / `ixunzi://share-card?id={id}` | карты |
| `ixunzi://author?id={id}` | Страница автора |
| `ixunzi://recite` / `ixunzi://recite?id={id}` | Режим чтения вслух |

## Discovery & Practice

| URL | Открывает |
|-----|-------|
| `ixunzi://home` | Главная |
| `ixunzi://daily` | Ежедневный Сун |
| `ixunzi://random` | Случайный отрывок |
| `ixunzi://favorites` | Избранное |
| `ixunzi://famous` | Знаменитые строки |
| `ixunzi://search` / `ixunzi://search?q={query}` | Поиск |
| `ixunzi://study` / `ixunzi://study?id={id}` | Поощрение Академии обучения |
| `ixunzi://hunt` | Xun Hunt («охота за ключевыми словами» / «флайфлауэр») |
| `ixunzi://handwriting` | Поиск почерка («handwrite»; iOS) |
| `ixunzi://mastered` | Мастеринг («Прогресс») |
| `ixunzi://categories` / `ixunzi://categories?section=` | Обзор |
| `ixunzi://collection?id=` | Коллекция / книга |
| `ixunzi://corpus` | Все пассажи («All») |
| `ixunzi://last-read` | Последнее прочитанное |
| `ixunzi://reading-history` | История чтения |
| `ixunzi://notes` | Заметки |
| `ixunzi://ask` | Спроси у Ксунзи. |
| `ixunzi://fables` / `ixunzi://allegories` / `ixunzi://concepts` | Специальные полки, когда они доступны |

## Настройки и руководства

| URL | Открывает |
|-----|-------|
| `ixunzi://settings` | Настройки |
| `ixunzi://usage-guide` | Руководство по использованию |
| `ixunzi://widget-guide` | Руководство по виджетам |
| `ixunzi://shortcuts-guide` | Руководство по «Командам» |
| `ixunzi://feature-guide` | Повторное знакомство |
| `ixunzi://feedback` | Письмо с отзывом |
| `ixunzi://in-app-review` | Отзыв в приложении / App Store |

## Примеры


```
ixunzi://daily
ixunzi://passage?id=1
ixunzi://ask
ixunzi://study
ixunzi://hunt
```



