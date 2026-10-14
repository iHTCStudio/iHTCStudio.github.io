iThree поддерживает ярлыки ** `ithree://` ** (схема URL). Холодный старт и ярлыки домашнего экрана доставляются через единый буфер, поэтому ссылки не открываются дважды после входа.

## Формат ссылки


```
ithree://{host}?{params}
```


## Проходы и открытия

| URL | Открывает |
|-----|-------|
| `ithree://home` | Главная |
| `ithree://daily` | Ежедневная линия сегодня |
| `ithree://random` | Случайный отрывок |
| `ithree://passage?id={id}` | Страница отрывка |
| `ithree://recite` / `ithree://recite?id={id}` | Режим чтения вслух |
| `ithree://favorites` | Избранное |
| `ithree://famous` | Знаменитые строки |
| `ithree://search` / `ithree://search?q={query}` | Поиск |
| `ithree://study` | Учебный класс |
| `ithree://quiz` | Сегодняшняя викторина |
| `ithree://hunt` | Охота ()) |
| `ithree://mastered` | мастеринг |
| `ithree://categories` | Обзор |
| `ithree://chapter?id={id}` | Глава |
| `ithree://stories` / `ithree://story?id={id}` | Рассказы / Story Detail |
| `ithree://books` / `ithree://book?id={id}` | Классические индексы / книга |
| `ithree://dynasties` / `ithree://dynasty?id={id}` | Династии / Династия |
| `ithree://collection?id=` / `?name=` | Коллекция (или книги, если они пусты) |
| `ithree://last-read` | Последнее прочитанное |
| `ithree://reading-history` | История чтения |
| `ithree://notes` | Заметки |

> Примечание: `ithree://` является псевдонимом совместимости и открывает соответствующую **главу**.

## Настройки и руководства

| URL | Открывает |
|-----|-------|
| `ithree://settings` | Настройки |
| `ithree://usage-guide` | Руководство по использованию |
| `ithree://widget-guide` | Руководство по виджетам |
| `ithree://shortcuts-guide` | Руководство по «Командам» |
| `ithree://feature-guide` | Повторное знакомство |
| `ithree://feedback` | Письмо с отзывом |
| `ithree://in-app-review` | Отзыв в приложении / App Store |
| `ithree://privacy` | Приватность в приложении |

## Примеры


```
ithree://daily
ithree://passage?id=1
ithree://recite?id=1
ithree://study
ithree://hunt
ithree://quiz
ithree://stories
ithree://search?q=人之初
```


Используйте их в приложении Shortcuts, быстрых действиях Home Screen, виджетах, Центре управления или Safari. См. также in-app **Settings → Shortcuts Guide**.


