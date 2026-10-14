iXin поддерживает ярлыки ** `ixin://` ** (схема URL). Холодный старт и ярлыки домашнего экрана доставляются через единый буфер, поэтому ссылки не открываются дважды после входа.

## Формат ссылки


```
ixin://{host}?{params}
```


## Проходы и авторы

| URL | Открывает |
|-----|-------|
| `ixin://passage?id={id}` | Страница отрывка |
| `ixin://saying?id={id}` / `ixin://couplet?id={id}` / `ixin://poem?id={id}` | Совместимость (Compatibility) |
| `ixin://passage?id={id}&card=1` | Детали проезда и карточный лист |
| `ixin://card?id={id}` / `ixin://share-card?id={id}` | Карты Insight |
| `ixin://author?id={id}` | Страница автора |
| `ixin://recite` / `ixin://recite?id={id}` | Режим чтения вслух |

## Discovery & Practice

| URL | Открывает |
|-----|-------|
| `ixin://home` | Главная |
| `ixin://daily` | Ежедневное понимание |
| `ixin://random` | Случайный отрывок |
| `ixin://favorites` | Избранное |
| `ixin://famous` | Знаменитые строки |
| `ixin://search` / `ixin://search?q={query}` | Поиск |
| `ixin://study` / `ixin://study?id={id}` | Школа сердца |
| `ixin://hunt` | Охота за сердцем ('keyword-hunt' / 'flyflower') |
| `ixin://handwriting` | Поиск почерка («handwrite»; iOS) |
| `ixin://mastered` | Мастеринг («Прогресс») |
| `ixin://categories` / `ixin://categories?section=` | Обзор |
| `ixin://collection?id=` | Коллекция/книга ('chuanxilu'/ 'daxuewen'/ 'jiaotiao'/ 'yilvwen'/стихи) |
| `ixin://corpus` | Все пассажи («All») |
| `ixin://last-read` | Последнее прочитанное |
| `ixin://reading-history` | История чтения |
| `ixin://notes` | Заметки |
| `ixin://journal` | Знающий журнал |
| `ixin://liangzhi` | Три вопроса о Лянжи |
| `ixin://graph` | Концептуальный граф |
| `ixin://timeline` | Анналы / хронология |
| `ixin://map` | Карта |
| `ixin://people` | Люди |
| `ixin://achievements` | Достижения |
| `ixin://theme?id=` | Тема |

## Настройки и руководства

| URL | Открывает |
|-----|-------|
| `ixin://settings` | Настройки |
| `ixin://usage-guide` | Руководство по использованию |
| `ixin://widget-guide` | Руководство по виджетам |
| `ixin://shortcuts-guide` | Руководство по «Командам» |
| `ixin://feature-guide` | Повторное знакомство |
| `ixin://feedback` | Письмо с отзывом |
| `ixin://in-app-review` | Отзыв в приложении / App Store |

## Примеры


```
ixin://daily
ixin://passage?id=1
ixin://journal
ixin://liangzhi
ixin://collection?id=chuanxilu
ixin://study
ixin://hunt
```


## Заметки

- Параметры чувствительны к регистру, где идентификаторы являются числовыми.
- Siri, ярлыки, виджеты и элементы управления Центра управления используют одни и те же маршруты глубокой связи.
- Смотрите в приложении ** Настройки → Справочные руководства ** для последнего списка.


