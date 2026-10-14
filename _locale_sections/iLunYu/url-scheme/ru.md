iLunYu поддерживает ярлыки ** `ilunyu://` ** (схема URL). Холодный старт и ярлыки домашнего экрана доставляются через единый буфер, поэтому ссылки не открываются дважды после входа.

## Формат ссылки


```
ilunyu://{host}?{params}
```


## Главы и авторы

| URL | Открывает |
|-----|-------|
| `ilunyu://passage?id={id}` | Глава подробная |
| `ilunyu://couplet?id={id}` / `ilunyu://poem?id={id}` | Совместимость (Compatibility) |
| `ilunyu://author?id={id}` | Страница автора |
| `ilunyu://recite` | Режим чтения вслух |
| `ilunyu://recite?id={id}` | Открытая глава и автоцитирование |

## Обзор

| URL | Открывает |
|-----|-------|
| `ilunyu://home` | Вкладка «Главная» |
| `ilunyu://daily` | Ежедневный стих сегодня |
| `ilunyu://random` | Случайная глава |
| `ilunyu://favorites` | Избранное |
| `ilunyu://famous` | Знаменитые строки |
| `ilunyu://search` / `ilunyu://search?q={query}` | Поиск |
| `ilunyu://study` | Учебный класс |
| `ilunyu://hunt` | Охота (`); псевдонимы «охота за ключевыми словами» / «флайфлауэр» |
| `ilunyu://mastered` / `ilunyu://progress` | Мастеринг / Прогресс |
| `ilunyu://categories` / `ilunyu://categories?section=` | Обзор |
| `ilunyu://collection?id=lunyu` | Сборник книг (ссылки "книга" / "форма"; также "имя =") |
| `ilunyu://theme?id=` | Тема или объем (например, "junzi", "xue-er"; псевдонимы "suite"/"volume") |
| `ilunyu://last-read` | Последнее прочитанное |
| `ilunyu://reading-history` | История чтения |
| `ilunyu://notes` | Заметки |

## Настройки и руководства

| URL | Открывает |
|-----|-------|
| `ilunyu://settings` | Настройки |
| `ilunyu://usage-guide` | Руководство по использованию |
| `ilunyu://widget-guide` | Руководство по виджетам |
| `ilunyu://shortcuts-guide` | Руководство по «Командам» |
| `ilunyu://feature-guide` | Повторное знакомство |
| `ilunyu://feedback` | Письмо с отзывом |
| `ilunyu://in-app-review` | Отзыв в приложении / App Store |

## Примеры


```
ilunyu://daily
ilunyu://passage?id=1
ilunyu://recite?id=20
ilunyu://theme?id=junzi
ilunyu://study
ilunyu://hunt
```


Используйте их в приложении Shortcuts, быстрых действиях Home Screen, виджетах или Safari. См. также in-app **Settings → Shortcuts Guide**.


