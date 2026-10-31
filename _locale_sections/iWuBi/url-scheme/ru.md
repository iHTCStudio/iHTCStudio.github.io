iWuBi поддерживает ** `iWuBi://` ** (схема `iwubi` ) глубокие ссылки - открытый поиск, ежедневная викторина, фавориты, неправильная книга, уровни длины кода, хаб обучения или практика набора текста из Safari, ярлыки, виджеты или другое приложение.

## Протокол


```
iWuBi://<host>[?query]
iWuBi:///path-style   ← host empty; first path segment is the action
```


| Host / action | Opens | Запрос |
|---------------|-------|-------|
| `search` | Lookup tab, focus search | "q", "word" или "name" pre-fills |
| `word`, `char`, `character` | Word detail (or search if query empty) | «q» / «слово» / «имя» = символ |
| `quiz`, `test` | Learn → Daily Quiz | — |
| `favorites`, `favorite` | Settings → Favourites | — |
| `wrong`, `mistakes`, `wrongbook` | Wrong book | «record=<UUID>» — одна запись |
| `levels`, `level`, `codes` | Levels tab | — |
| `learn`, `study` | Learn tab | — |
| `typing`, `type`, `practice` | Typing tab | — |

## Примеры


```
iWuBi://search?q=你好
iWuBi://word?q=好
iWuBi://quiz
iWuBi://wrong?record=550E8400-E29B-41D4-A716-446655440000
iWuBi://levels
iWuBi://typing
```


## Домой Экран Быстрые действия

До **4** в **Настройки → Ярлыки домашнего экрана **: `iWuBi://` , `iwubi` , `search` , `q` , `word` , `name` , `word` . **Обратная связь** и **обзор** являются только быстрыми действиями.

[Назад к обзору] (..) · [FAQ] (../faq) · [Privacy] (../privacy)


