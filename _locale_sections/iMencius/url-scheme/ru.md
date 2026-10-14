iMencius поддерживает ярлыки ** `imencius://` ** (схема URL). Холодный старт и ярлыки домашнего экрана доставляются через единый буфер, поэтому ссылки не открываются дважды после входа.

## Формат ссылки


```
imencius://{host}?{params}
```


## Проходы и авторы

| URL | Открывает |
|-----|-------|
| `imencius://passage?id={id}` | Страница отрывка |
| `imencius://saying?id={id}` / `imencius://couplet?id={id}` / `imencius://poem?id={id}` | Совместимость (Compatibility) |
| `imencius://passage?id={id}&card=1` | Детали проезда и карточный лист |
| `imencius://card?id={id}` / `imencius://share-card?id={id}` | карты |
| `imencius://author?id={id}` | Страница автора |
| `imencius://recite` / `imencius://recite?id={id}` | Режим чтения вслух |

## Discovery & Practice

| URL | Открывает |
|-----|-------|
| `imencius://home` | Главная |
| `imencius://daily` | Ежедневные высказывания |
| `imencius://random` | Случайный отрывок |
| `imencius://favorites` | Избранное |
| `imencius://famous` | Знаменитые строки |
| `imencius://search` / `imencius://search?q={query}` | Поиск |
| `imencius://study` / `imencius://study?id={id}` | Обучение Qi Study |
| `imencius://hunt` | Yi Hunt («охота за ключевыми словами» / «флайфлауэр») |
| `imencius://handwriting` | Поиск почерка («handwrite»; iOS) |
| `imencius://mastered` | Мастеринг («Прогресс») |
| `imencius://categories` / `imencius://categories?section=` | Обзор |
| `imencius://collection?id=` | Коллекция / книга |
| `imencius://corpus` | Все пассажи («All») |
| `imencius://last-read` | Последнее прочитанное |
| `imencius://reading-history` | История чтения |
| `imencius://notes` | Заметки |
| `imencius://fables` / `imencius://allegories` / `imencius://concepts` | Специальные полки, когда они доступны |

## Настройки и руководства

| URL | Открывает |
|-----|-------|
| `imencius://settings` | Настройки |
| `imencius://usage-guide` | Руководство по использованию |
| `imencius://widget-guide` | Руководство по виджетам |
| `imencius://shortcuts-guide` | Руководство по «Командам» |
| `imencius://feature-guide` | Повторное знакомство |
| `imencius://feedback` | Письмо с отзывом |
| `imencius://in-app-review` | Отзыв в приложении / App Store |

## Примеры


```
imencius://daily
imencius://passage?id=1
imencius://study
imencius://hunt
```



