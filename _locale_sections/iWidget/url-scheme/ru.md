iWidget понимает **`iwidget://`** на **iPhone, iPad и Mac**. Safari, «Команды», другое приложение или QR. Голосовой лунный календарь без открытия приложения — Siri. Рабочий день — отдельный Workday Intent, не URL.

`iwidget://<host>[?query]` — неизвестные host игнорируются.

| Host | Открывает | Query |
|------|-----------|-------|
| `today` | Сегодня | — |
| `day` | Сегодня → день | `y` `m` `d` |
| `library` | Библиотека | `preset=` / `set=`, `detail=1` |
| `mine` | Мои виджеты | `design=` / `id=`, `preset=` / `set=` |
| `editor` | Редактор | `design=` / `id=` (иначе последний) |
| `import` | Импорт | — |
| `settings` | Настройки | `scroll=festivals` · `weather` · `editor` · `access` |
| `membership` | Членство | приостановленные виджеты открывают это |
| `launch` | Handoff ярлыка (iOS) | от виджета |

Примеры: `iwidget://today` · `iwidget://library?set=small.calendar&detail=1` · `iwidget://membership`

[К поддержке](../) · [FAQ](../faq) · [Членство](../membership) · [Конфиденциальность](../privacy)
