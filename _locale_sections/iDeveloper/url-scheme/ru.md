iDeveloper поддерживает ярлыки ** `ideveloper://` ** (схема URL). Холодный старт и ярлыки домашнего экрана доставляются через единый буфер, поэтому ссылки не открываются дважды после входа.

## Формат ссылки


```
ideveloper://{host}?{params}
```


## Инструменты & Browse

| URL | Открывает |
|-----|-------|
| `ideveloper://home` | Главная |
| `ideveloper://tool?id={id}` | Детали инструмента (например, "json", "base64", "timestamp") |
| `ideveloper://category?id={id}` | Категория (например, "кодирование") |
| `ideveloper://search` / `ideveloper://search?q={query}` | Поиск |
| `ideveloper://favorites` | Избранное |
| `ideveloper://history` | История операции |
| `ideveloper://reference` / `ideveloper://reference?id={id}` | Справочный центр / вход |
| `ideveloper://new-snippet` | Новый фрагмент |
| `ideveloper://focus` | Фокус таймер / Live Activity |
| `ideveloper://share?tool={id}` | Открытая передача Share в инструмент (работает с расширением Share + полезной нагрузкой App Group) |

## Настройки и руководства

| URL | Открывает |
|-----|-------|
| `ideveloper://settings` | Настройки |
| `ideveloper://usage-guide` | Руководство по использованию |
| `ideveloper://widget-guide` | Руководство по виджетам |
| `ideveloper://shortcuts-guide` | Руководство по «Командам» |
| `ideveloper://feature-guide` | Повторное знакомство |
| `ideveloper://feedback` | Письмо с отзывом |
| `ideveloper://in-app-review` | Отзыв в приложении / App Store |

## Примеры


```
ideveloper://tool?id=json
ideveloper://search?q=base64
ideveloper://reference?id=http-200
ideveloper://favorites
ideveloper://focus
ideveloper://share?tool=json
ideveloper://category?id=encoding
```


Используйте их в приложении Shortcuts, быстрых действиях Home Screen, виджетах, Центре управления или Safari. См. также in-app **Settings → Shortcuts Guide**.


