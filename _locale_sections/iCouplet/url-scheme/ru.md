iCouplet поддерживает ярлыки ** `icouplet://` ** (схема URL). Холодный старт и ярлыки домашнего экрана доставляются через единый буфер, поэтому ссылки не открываются дважды после входа.

## Формат ссылки


```
icouplet://{host}?{params}
```


## Куплеты и авторы

| URL | Открывает |
|-----|-------|
| `icouplet://couplet?id={id}` | Детали куплета |
| `icouplet://poem?id={id}` | Совместимость (compatibility alias) |
| `icouplet://author?id={id}` | Автор ( detail) Подробности |
| `icouplet://recite` | Поток речи (автоговор, когда это возможно) |
| `icouplet://recite?id={id}` | Открытый куплет и автоцит |

## Обзор

| URL | Открывает |
|-----|-------|
| `icouplet://home` | Вкладка «Главная» |
| `icouplet://daily` | Ежедневный куплет сегодня |
| `icouplet://random` | Случайная пара |
| `icouplet://favorites` | Избранное |
| `icouplet://famous` | Список знаменитых линий |
| `icouplet://search` | Поиск |
| `icouplet://search?q={query}` | Поиск с запросом |
| `icouplet://study` | Учеба /   Вступление |
| `icouplet://categories` | Просмотр категорий |
| `icouplet://categories?section=form` | Форма ( section) раздел |
| `icouplet://categories?section=theme` | Тематический раздел |
| `icouplet://categories?section=author` | Авторский раздел |
| `icouplet://categories?section=famous` | Знаменитая секция линий |
| `icouplet://categories?section=corpus` | Коллекции / корпус |
| `icouplet://last-read` | Последнее чтение Парт |
| `icouplet://reading-history` | История чтения |

## Настройки и руководства

| URL | Открывает |
|-----|-------|
| `icouplet://settings` | Настройка root |
| `icouplet://usage-guide` | Руководство по использованию |
| `icouplet://widget-guide` | Руководство по виджетам |
| `icouplet://shortcuts-guide` | Руководство по «Командам» |
| `icouplet://feature-guide` | Функция воспроизведения на борту |
| `icouplet://feedback` | Письмо с отзывом |
| `icouplet://in-app-review` | Отзыв в приложении / App Store |

## Примеры


```
icouplet://daily
icouplet://couplet?id=1
icouplet://recite?id=1
icouplet://search?q=春
icouplet://categories?section=famous
icouplet://widget-guide
```


Используйте их в приложении Shortcuts, быстрых действиях Home Screen, виджетах или Safari. См. также in-app **Settings → Shortcuts Guide**.


