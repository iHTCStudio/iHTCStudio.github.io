iCoder поддерживает ** `iLeetCoder://` ** (случайно-нечувствительные) глубокие ссылки - откройте проблему, ежедневную викторину, фавориты, неправильную книгу или фильтр по тегу / компании из Safari, Shortcuts, виджетов или другого приложения.

## Протокол

| Host | Opens | Запрос |
|------|-------|-------|
| `problem` | Problem detail | "leetId=" или "id=" (например, "1", "206") |
| `quiz` | Daily Quiz tab | — |
| `favorites` | Favourites list | — |
| `wrong`, `mistakes`, `wrongquestions` | Wrong book | «record=<UUID>» → связанная проблема |
| `tag` | Problems filtered by tag | Имя = |
| `company` | Problems filtered by company | Имя = |

## Примеры


```
iLeetCoder://problem?leetId=1
iLeetCoder://problem?id=206
iLeetCoder://quiz
iLeetCoder://tag?name=Array
iLeetCoder://company?name=Google
iLeetCoder://wrong?record=550E8400-E29B-41D4-A716-446655440000
```


## Домой Экран Быстрые действия

До **4** в **Настройки → Ярлыки домашнего экрана **: `iLeetCoder://` , `problem` , `leetId=` , `id=` , `1` , `206` , `quiz` . Поиск / категории / отзывы / обзор - это каналы быстрого действия.

[Назад к обзору] (..) · [FAQ] (../faq) · [Privacy] (../privacy)


