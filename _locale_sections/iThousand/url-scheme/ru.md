iThousand поддерживает ярлыки ** `ithousand://` ** (схема URL). Холодный старт и ярлыки домашнего экрана доставляются через единый буфер, поэтому ссылки не открываются дважды после входа.

## Формат ссылки


```
ithousand://{host}?{params}
```


## Проходы, авторы и персонажи

| URL | Открывает |
|-----|-------|
| `ithousand://passage?id={id}` | Страница отрывка |
| `ithousand://passage?id={id}&open=study` | Оригинальное название: Primer Hall |
| `ithousand://passage?id={id}&open=characters` | Прохождение: Character Table |
| `ithousand://passage?id={id}&open=note` | Прохождение Note |
| `ithousand://author?id={id}` | Страница автора |
| `ithousand://recite` / `ithousand://recite?id={id}` | Режим чтения вслух |
| `ithousand://characters` | Библиотека персонажей |
| `ithousand://character?char=天` | Сосредоточьте карту персонажа |
| `ithousand://characters?id={id}` | Карточка персонажа ID |
| `ithousand://saved-characters` | Спасенные персонажи |
| `ithousand://saved-famous` | Сохранились знаменитые линии |

## Обзор

| URL | Открывает |
|-----|-------|
| `ithousand://home` | Главная |
| `ithousand://daily` | Ежедневная линия сегодня |
| `ithousand://random` | Случайный отрывок |
| `ithousand://favorites` | Избранное |
| `ithousand://list?id={uuid}` | Личный список ()) |
| `ithousand://famous` | Знаменитые строки |
| `ithousand://search` / `ithousand://search?q={query}` | Поиск |
| `ithousand://study` | Праймер Холл |
| `ithousand://hunt` | Охота (`); псевдонимы «охота за ключевыми словами» / «флайфлауэр» |
| `ithousand://mastered` | мастеринг |
| `ithousand://categories` / `ithousand://categories?section=` | Обзор |
| `ithousand://collection?id=qianziwen` | Primer Collection (также поддерживается) |
| `ithousand://theme?id=dizigui-filial` | Тема |
| `ithousand://last-read` | Последнее прочитанное |
| `ithousand://reading-history` | История чтения |
| `ithousand://notes` | Заметки |

## Настройки и руководства

| URL | Открывает |
|-----|-------|
| `ithousand://settings` | Настройки |
| `ithousand://privacy` | Приватность в приложении |
| `ithousand://usage-guide` | Руководство по использованию |
| `ithousand://widget-guide` | Руководство по виджетам |
| `ithousand://shortcuts-guide` | Руководство по «Командам» |
| `ithousand://feature-guide` | Повторное знакомство |
| `ithousand://feedback` | Письмо с отзывом |
| `ithousand://in-app-review` | Отзыв в приложении / App Store |

## Примеры


```
ithousand://daily
ithousand://passage?id=1
ithousand://passage?id=1&open=characters
ithousand://character?char=天
ithousand://collection?id=qianziwen
ithousand://study
ithousand://hunt
ithousand://saved-characters
```


Используйте их в приложении Shortcuts, быстрых действиях Home Screen, виджетах или Safari. Предпочитаю стабильные параметры `ithousand://` при наличии. См. также in-app **Settings → Shortcuts Guide**.


