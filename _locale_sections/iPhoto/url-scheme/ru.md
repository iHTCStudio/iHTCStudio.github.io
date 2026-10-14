iPhoto поддерживает ** `iphoto://` ** глубокие ссылки и **App Intents / Siri Shortcuts**. Ссылки перемещаются только внутри приложения — они не загружают данные.

## схема


```
iphoto://<host>[?query]
```


| Rule | Подробнее |
|------|--------|
| Scheme | "Ифото" |
| Empty | Открывает вкладку по умолчанию приложения |
| Unknown hosts | Безопасно игнорируется |

---

## Вкладки и навигация

| URL | Открывает |
|-----|-------|
| `iphoto://library` | Закладка библиотеки |
| `iphoto://capture` | Захват вкладки |
| `iphoto://settings` | Настройка вкладки |
| `iphoto://search` | Поисковая вкладка (iOS 18+) |
| `iphoto://recent-projects` | Библиотека посвящена недавней работе |

---

## редактор

| URL | Открывает |
|-----|-------|
| `iphoto://editor?id=<projectID>` | Редактор для данного проекта id |

---

## Руководство и действия

| URL | Открывает |
|-----|-------|
| `iphoto://usage-guide` | Руководство по использованию |
| `iphoto://widget-guide` | Руководство по виджетам |
| `iphoto://shortcuts-guide` | Руководство по «Командам» |
| `iphoto://feature-guide` | Изображение / onboarding replay |
| `iphoto://export-presets` | Условия, связанные с экспортом |
| `iphoto://feedback` | Письмо с отзывом |
| `iphoto://in-app-review` | Быстрый обзор в приложении |

---

## Siri и Shortcuts

Встроенные намерения включают в себя:

- Открытый захват
- Открытая библиотека
- Импорт фотографий
- Открытые настройки

Добавьте их в приложение Shortcuts или вызовите Siri, используя фразы, показанные в Shortcuts.

## Примеры


```
iphoto://capture
iphoto://library
iphoto://editor?id=YOUR-PROJECT-ID
iphoto://widget-guide
```


[FAQ] (../faq) · [Политика конфиденциальности] (../privacy) · [Назад к iPhoto] (../)


