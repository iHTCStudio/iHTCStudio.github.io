iSutra поддерживает ярлыки ** `isutra://` ** (схема URL). Холодный старт и ярлыки домашнего экрана доставляются через единый буфер, поэтому ссылки не открываются дважды после входа.

## Формат ссылки


```
isutra://{host}?{params}
```


## Сутры и авторы

| URL | Открывает |
|-----|-------|
| `isutra://passage?id={id}` | Подробнее о Sutra |
| `isutra://couplet?id={id}` / `isutra://poem?id={id}` | Совместимость (Compatibility) |
| `isutra://author?id={id}` | Переводчик/автор подробно |
| `isutra://recite` / `isutra://recite?id={id}` | Режим чтения вслух |
| `isutra://large?id=diamond` / `isutra://large?id=dizang` | Большой книжный каталог |

## Discovery & Practice

| URL | Открывает |
|-----|-------|
| `isutra://home` | Главная |
| `isutra://daily` | Сегодняшняя ежедневная сутра |
| `isutra://random` | Случайный отрывок |
| `isutra://favorites` | Избранное |
| `isutra://famous` | Знаменитые строки |
| `isutra://search` / `isutra://search?q={query}` | Поиск |
| `isutra://study` | Учебный зал |
| `isutra://hunt` | Охота; псевдонимы «охота за ключевыми словами» / «флайфлауэр» |
| `isutra://count` | Песня деревянной рыбы ('chant' / 'muyu' / 'counter') |
| `isutra://copy` / `isutra://copy?id={id}` | Copy-sutra (iOS) |
| `isutra://practice` | Утренняя или вечерняя практика |
| `isutra://mastered` | мастеринг |
| `isutra://categories` / `isutra://categories?section=` | Обзор |
| `isutra://collection?id=` | Коллекция (например, "праджна", "сорок два"; также "имя =") |
| `isutra://theme?id=` | Тема (например, "xingyuan", "yaoshi", "платформа") |
| `isutra://last-read` | Последнее прочитанное |
| `isutra://reading-history` | История чтения |
| `isutra://notes` | Заметки |

## Настройки и руководства

| URL | Открывает |
|-----|-------|
| `isutra://settings` | Настройки |
| `isutra://usage-guide` | Руководство по использованию |
| `isutra://widget-guide` | Руководство по виджетам |
| `isutra://shortcuts-guide` | Руководство по «Командам» |
| `isutra://feature-guide` | Повторное знакомство |
| `isutra://privacy` | Приватность в приложении |
| `isutra://feedback` | Письмо с отзывом |
| `isutra://in-app-review` | Отзыв в приложении / App Store |

## Примеры


```
isutra://daily
isutra://passage?id=1
isutra://large?id=diamond
isutra://count
isutra://copy?id=1
isutra://practice
isutra://collection?id=prajna
isutra://theme?id=xingyuan
isutra://study
isutra://hunt
```


Используйте их в приложении Shortcuts, быстрых действиях Home Screen, виджетах или Safari. См. также in-app **Settings → Shortcuts Guide**.


