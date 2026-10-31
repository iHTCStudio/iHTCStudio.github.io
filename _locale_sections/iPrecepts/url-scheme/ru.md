iPrecepts поддерживает ярлыки ** `iprecepts://` ** (схема URL). Холодный старт и ярлыки домашнего экрана доставляются через единый буфер, поэтому ссылки не открываются дважды после входа.

## Формат ссылки


```
iprecepts://{host}?{params}
```


## Проходы и авторы

| URL | Открывает |
|-----|-------|
| `iprecepts://passage?id={id}` | Страница отрывка |
| `iprecepts://saying?id={id}` / `iprecepts://couplet?id={id}` / `iprecepts://poem?id={id}` | Совместимость (Compatibility) |
| `iprecepts://passage?id={id}&card=1` | Детали проезда и карточный лист |
| `iprecepts://card?id={id}` / `iprecepts://share-card?id={id}` | Рецепт карты |
| `iprecepts://author?id={id}` | Страница автора |
| `iprecepts://recite` / `iprecepts://recite?id={id}` | Режим чтения вслух |

## Discovery & Practice

| URL | Открывает |
|-----|-------|
| `iprecepts://home` | Главная |
| `iprecepts://daily` | Ежедневные предписания |
| `iprecepts://random` | Случайный отрывок |
| `iprecepts://favorites` | Избранное |
| `iprecepts://famous` | Знаменитые строки |
| `iprecepts://search` / `iprecepts://search?q={query}` | Поиск |
| `iprecepts://study` / `iprecepts://study?id={id}` | Семейное исследование |
| `iprecepts://hunt` | Precept Hunt («охота за ключевыми словами» / «флайфлауэр») |
| `iprecepts://handwriting` | Поиск почерка («handwrite»; iOS) |
| `iprecepts://mastered` | Мастеринг («Прогресс») |
| `iprecepts://categories` / `iprecepts://categories?section=` | Обзор |
| `iprecepts://collection?id=` | Коллекция / книга (цхуси / жубайлу / янши / жуге / цэн / юаньши / цянь / тингсун / короткие работы) |
| `iprecepts://corpus` | Все пассажи («All») |
| `iprecepts://last-read` | Последнее прочитанное |
| `iprecepts://reading-history` | История чтения |
| `iprecepts://notes` | Заметки |
| `iprecepts://compare` | Параллельное сравнение |
| `iprecepts://theme?id=` | Тема |
| `iprecepts://authors` | авторы |

## Настройки и руководства

| URL | Открывает |
|-----|-------|
| `iprecepts://settings` | Настройки |
| `iprecepts://usage-guide` | Руководство по использованию |
| `iprecepts://widget-guide` | Руководство по виджетам |
| `iprecepts://shortcuts-guide` | Руководство по «Командам» |
| `iprecepts://feature-guide` | Повторное знакомство |
| `iprecepts://feedback` | Письмо с отзывом |
| `iprecepts://in-app-review` | Отзыв в приложении / App Store |

## Примеры


```
iprecepts://daily
iprecepts://passage?id=1
iprecepts://passage?id=1&card=1
iprecepts://compare
iprecepts://collection?id=yanshi
iprecepts://study
iprecepts://hunt
```


## Заметки

- Параметры чувствительны к регистру, где идентификаторы являются числовыми.
- Siri, ярлыки, виджеты и элементы управления Центра управления используют одни и те же маршруты глубокой связи.
- Смотрите в приложении ** Настройки → Справочные руководства ** для последнего списка.


