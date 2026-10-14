iMusic поддерживает ярлыки ** `imusic://` **. Холодный старт и ярлыки Home Screen проходят через единый буфер, поэтому ссылка не открывается дважды после входа.

## Формат ссылки


```
imusic://{host}?{params}
```


Схема ** `imusic://` **.

## Home и сегодня

| URL | Открывает |
|-----|-------|
| `imusic://` / `imusic://home` | Главная |
| `imusic://daily` / `imusic://today` | Daily Piece (только этот трек) |
| `imusic://random` | Roam (полная перетасовка библиотек) |
| `imusic://play` | Играть |
| `imusic://last` / `imusic://lastheard` | Последнее слово |

## Исполнитель: Pieces & Artists

| URL | Открывает |
|-----|-------|
| `imusic://piece?id={id}` | Piece Guide («Переход» / «Песня» также принимается) |
| `imusic://artist?id={id}` / `imusic://artist?name={name}` | Рабочий стол |
| `imusic://artists` / `imusic://singers` | Художественный справочник |
| `imusic://famous` / `imusic://lines` | Знаменитые строки |

Нижний колонтитул может добавить `imusic://` (название художника) для людей. Матч по-прежнему использует ** `imusic` только **.

## Просмотр, поиск и прослушивание

| URL | Открывает |
|-----|-------|
| `imusic://categories` / `imusic://browse` | Browse ('section=catalog' / 'all' / 'allpieces' → All Pieces) |
| `imusic://collection?id={id}` | «id=col-all» — это виртуальный список «All Pieces». |
| `imusic://search` / `imusic://search?q={query}` | Поиск |
| `imusic://favorites` | Избранное |
| `imusic://later` | Любимые, прокрученные позже |
| `imusic://lists` / `imusic://listenlists` | Слушайте списки |
| `imusic://history` | История |
| `imusic://notes` | Заметки |
| `imusic://mastered` | Закончено |
| `imusic://streak` / `imusic://footprint` | полоса |

Открывая один кусок, мини-бар или идентификатор песни ** сбрасывает ** очередь чтения на этот кусок. Открытие из коллекции, поиска или художника сохраняет этот список таким образом, чтобы оставаться доступным.

## Песня ID, школа и настроение

| URL | Открывает |
|-----|-------|
| `imusic://recognize` / `imusic://shazam` | Песня ID |
| `imusic://school` / `imusic://earschool` | Ушная школа |
| `imusic://timeline` / `imusic://corridor` | Коридор эпохи |
| `imusic://compare` | Сравните прослушивание |
| `imusic://mood?id={id}` | Начните это настроение ('piece=' / 'pieceId=' - это только стартовый трек; настроение все еще соответствует 'id'). |

## Настройки и руководства

| URL | Открывает |
|-----|-------|
| `imusic://settings` | Настройки |
| `imusic://usageguide` / `imusic://featureguide` | Использование / Feature Guide |
| `imusic://widgetguide` | Руководство по виджетам |
| `imusic://shortcutsguide` | Руководство по «Командам» |
| `imusic://feedback` | обратная связь |
| `imusic://review` / `imusic://in-app-review` | Обзор в приложении (когда листинг магазина вживую) |

## Siri и домашний экран

Спросите Siri о сегодняшнем продукте, роуминге, поиске или фаворитах после добавления ярлыков. Настройте быстрые действия на домашнем экране в ** Настройки → Ярлыки **. Полные примеры живут в руководстве по ярлыкам в приложении.

[FAQ] (../faq) · [Политика конфиденциальности] (../privacy) · [Поддержка] (../)


