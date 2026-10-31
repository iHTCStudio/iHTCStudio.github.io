iPrimer поддерживает ярлыки ** `iprimer://` ** (схема URL). Холодный старт и ярлыки домашнего экрана доставляются через единый буфер, поэтому ссылки не открываются дважды после входа.

## Формат ссылки


```
iprimer://{host}?{params}
```


## Главы и авторы

| URL | Открывает |
|-----|-------|
| `iprimer://chapter?id={id}` | Глава подробная |
| `iprimer://passage?id={id}` / `iprimer://poem?id={id}` | Совместимость (Compatibility) |
| `iprimer://author?id={id}` | Страница автора |
| `iprimer://recite` / `iprimer://recite?id={id}` | Режим чтения вслух |

## Обзор

| URL | Открывает |
|-----|-------|
| `iprimer://home` | Главная |
| `iprimer://daily` | Сегодняшнее ежедневное исследование |
| `iprimer://random` | Случайная глава |
| `iprimer://favorites` | Избранное |
| `iprimer://famous` | Знаменитые строки |
| `iprimer://search` / `iprimer://search?q={query}` | Поиск |
| `iprimer://study` | Изучение характера |
| `iprimer://meditation` | Список курсов медитации |
| `iprimer://meditation?slug={slug}&autostart=1` | Открытая сессия и автозапуск (на переднем плане) |
| `iprimer://guidance` | Руководство по жизни (журнал и привычки) |
| `iprimer://hunt` | Охота (`); псевдонимы «охота за ключевыми словами» / «флайфлауэр» |
| `iprimer://mastered` | Освоенные главы |
| `iprimer://categories` / `iprimer://categories?section=` | Обзор |
| `iprimer://collection?id=xiaoxue` | Коллекция Xiaoxue («имя =» также поддерживается) |
| `iprimer://theme?id=lijiao` | Объем / тема (также поддерживается «имя = )» или «Отношения») |
| `iprimer://last-read` | Последнее прочитанное |
| `iprimer://reading-history` | История чтения |
| `iprimer://notes` | Заметки |

## Настройки и руководства

| URL | Открывает |
|-----|-------|
| `iprimer://settings` | Настройки |
| `iprimer://usage-guide` | Руководство по использованию |
| `iprimer://widget-guide` | Руководство по виджетам |
| `iprimer://shortcuts-guide` | Руководство по «Командам» |
| `iprimer://feature-guide` | Повторное знакомство |
| `iprimer://feedback` | Письмо с отзывом |
| `iprimer://in-app-review` | Отзыв в приложении / App Store |

## Примеры


```
iprimer://daily
iprimer://chapter?id=3
iprimer://collection?id=xiaoxue
iprimer://theme?id=lijiao
iprimer://study
iprimer://meditation?slug=emotion_calm&autostart=1
iprimer://guidance
iprimer://hunt
```


Используйте их в приложении Shortcuts, быстрых действиях Home Screen, виджетах или Safari. Предпочитаю стабильные параметры `iprimer://` при наличии. См. также in-app **Settings → Shortcuts Guide**.


