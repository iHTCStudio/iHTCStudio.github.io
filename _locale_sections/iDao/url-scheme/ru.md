iDao поддерживает ярлыки ** `idao://` ** (схема URL). Холодный старт и ярлыки домашнего экрана доставляются через единый буфер, поэтому ссылки не открываются дважды после входа.

## Формат ссылки


```
idao://{host}?{params}
```


## Главы и открытия

| URL | Открывает |
|-----|-------|
| `idao://home` | Главная |
| `idao://daily` | Сегодняшняя ежедневная глава |
| `idao://random` | Случайная глава |
| `idao://chapter?id={id}` | Глава подробная |
| `idao://recite` / `idao://recite?id={id}` | Режим чтения вслух |
| `idao://favorites` | Избранное |
| `idao://famous` | Знаменитые строки |
| `idao://search` / `idao://search?q={query}` | Поиск |
| `idao://study` | Учебный зал |
| `idao://hunt` | Ищите Дао ()) |
| `idao://mastered` | мастеринг |
| `idao://categories` / `?section=` | Браузер (необязательный раздел) |
| `idao://book?id=` | Коллекция книг ('ddj' / 'qingjing' / 'yinfu') |
| `idao://author` | Вступление Лаоци |
| `idao://last-read` | Последнее прочитанное |
| `idao://reading-history` | История чтения |
| `idao://notes` | Заметки |

> Совместимость: `idao://` / `idao://home` → глава; `idao://daily` → исследование; `idao://random` → охота; `idao://chapter?id={id}` → автор; `idao://recite` → раздел категорий; `idao://recite?id={id}` → категории.

## Настройки и руководства

| URL | Открывает |
|-----|-------|
| `idao://settings` | Настройки |
| `idao://usage-guide` | Руководство по использованию |
| `idao://widget-guide` | Руководство по виджетам |
| `idao://shortcuts-guide` | Руководство по «Командам» |
| `idao://feature-guide` | Повторное знакомство |
| `idao://feedback` | Письмо с отзывом |
| `idao://in-app-review` | Отзыв в приложении / App Store |

## Примеры


```
idao://daily
idao://chapter?id=1
idao://recite?id=1
idao://study
idao://hunt
idao://famous
idao://book?id=ddj
idao://author
idao://search?q=上善若水
```


Используйте их в приложении Shortcuts, быстрых действиях Home Screen, виджетах, Центре управления или Safari. См. также in-app **Settings → Shortcuts Guide**.


