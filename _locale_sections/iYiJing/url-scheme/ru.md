iYijing поддерживает ярлыки ** `iyijing://` ** (схема URL). Холодный старт и ярлыки домашнего экрана доставляются через единый буфер, поэтому ссылки не открываются дважды после входа.

## Формат ссылки


```
iyijing://{host}/{path}?{params}
```


## Гексаграммы и открытия

| URL | Открывает |
|-----|-------|
| `iyijing://home` | Главная |
| `iyijing://daily` | Сегодняшняя ежедневная гексаграмма |
| `iyijing://random` | Случайная гексаграмма |
| `iyijing://hexagram/{id}` | Подробности гексаграммы ('gua/{id}' alias) |
| `iyijing://wing/{id}` | Ten Wings text ('yizhuan/{id}' alias) |
| `iyijing://trigram/{id}` | Триграмма ('bagua/{id}' alias) |
| `iyijing://browse` | Обзор |
| `iyijing://favorites` | Избранное |
| `iyijing://famous` | Знаменитые строки |
| `iyijing://search` / `?q=` | Поиск |
| `iyijing://study` | Ицзинское исследование |
| `iyijing://hunt` | Поиск ключевых слов |
| `iyijing://divination` | Культурный кастинг («цигуа» / «каст») |
| `iyijing://recite` / `recite/{id}` | декламация |
| `iyijing://collection` | Список гексаграмм ('playlist' alias) |
| `iyijing://last-read` | Последнее прочитанное |
| `iyijing://reading-history` | История чтения |
| `iyijing://notes` | Заметки |
| `iyijing://mastered` | мастеринг |
| `iyijing://wrong-book` | Неправильная книга |
| `iyijing://recite-wrong` | Неправильная книга |

## Настройки и руководства

| URL | Открывает |
|-----|-------|
| `iyijing://settings` | Настройки |
| `iyijing://usage-guide` | Руководство по использованию |
| `iyijing://widget-guide` | Руководство по виджетам |
| `iyijing://shortcuts-guide` | Руководство по «Командам» |
| `iyijing://feature-guide` | Повторное знакомство |
| `iyijing://feedback` | Письмо с отзывом |

## Примеры


```
iyijing://daily
iyijing://hexagram/1
iyijing://wing/301
iyijing://divination
iyijing://study
iyijing://hunt
iyijing://famous
iyijing://search?q=乾
```


Используйте их в приложении Shortcuts, быстрых действиях Home Screen, виджетах, Центре управления или Safari. См. также in-app **Settings → Shortcuts Guide**.


