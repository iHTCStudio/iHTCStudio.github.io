iStore поддерживает ярлыки ** `istore://` **. Используйте их в **Shortcuts**, закладках Safari или от **widgets**, **Control Center**, **Spotlight** и **Share Extension** до **switch a region**, **re-switch your last region**, **open a tab**, или **jump to a guide**.

## Формат ссылки


```
istore://{host}?{params}
```


Хозяева нечувствительны к делу. Коды регионов используют стандартные значения **Alpha-2** ( `istore://` , `us` , `cn` , `jp` , `hk` , ...).

| What you want | Ссылка |
|---------------|------|
| Switch to a region | 'istore://switch?region={code} |
| Switch to your last region | "istore://switch-last" |
| Open the Store / Favorites / Settings tab | "istore://store" · "istore://favorites" · "istore://settings" |
| Open App Availability | "история://доступность" |

---

## Переключитесь на регион

Запрашивает переключение на данный регион (направляется через подтверждение в приложении, если включено).


```
istore://switch?region={code}
```


| Parameter | Required | Описание |
|-----------|----------|-------------|
| `region` | **Yes** | Код региона, например "us", "cn", "jp", "hk", "tw" |

**Пример **


```
istore://switch?region=us
```


Используются: **интерактивные виджеты**, **Spotlight** и **Shortcuts/Siri**.

---

## Переключитесь на последний регион


```
istore://switch-last
```


Прочтите свою последнюю цель переключения и переключитесь на нее снова. Управляет **Switch Last** Control Center control (iOS 18+) и соответствующим действием Shortcut/Siri.

---

## Вкладки и страницы (без запроса)

| URL | Открывает |
|-----|-------|
| `istore://store` | Закладка магазина |
| `istore://favorites` | Любимая вкладка |
| `istore://settings` | Настройка вкладки |
| `istore://availability` | Настройки → Доступность приложений (также используется расширением акций) |
| `istore://switch-history` | Переключение истории |
| `istore://quick-regions` | Быстрые настройки регионов |
| `istore://feature-guide` | Обзор функций |
| `istore://widget-guide` | Руководство по виджетам |
| `istore://shortcuts-guide` | Руководство по «Командам» |
| `istore://usage-guide` | Руководство по использованию |
| `istore://feedback` | Письмо с отзывом |
| `istore://in-app-review` | Оценка в App Store из приложения |

---

## Виджеты, Центр управления и Spotlight

Они генерируют ссылки `istore://` автоматически при нажатии:

| Source | Tap target | Эффект |
|--------|------------|--------|
| **Quick Regions / Recent / Custom widget** | A region tile | "istore://switch?region=..." |
| **Switch Last control** (iOS 18+) | The control | "istore://switch-last" |
| **Spotlight** | A region result | "istore://switch?region=..." |

Интерактивное переключение с виджетов и Центра управления открывает приложение для завершения официального перенаправления App Store.

---

## Расширение доли

Поделитесь любой ссылкой ** App Store** в iStore. Share Extension проверяет доступность в популярных регионах, а затем может открыть приложение через `istore://` , чтобы вы могли просмотреть результат и переключиться.

---

## Siri и Shortcuts

Найдите встроенные действия в приложении **Shortcuts** или спросите **Siri**. Названия и фразы локализованы на английском языке / .中. / .中..

| Action | What you can set | Эффект |
|--------|------------------|--------|
| Switch region | Region | Переключается на этот регион |
| Switch last region | — | Переключайтесь на последнюю цель |
| Switch favorite region | A favorite | Переход в любимый регион |
| Open store | — | Открытие iStore |
| Check availability | App link or ID | Проверьте, где приложение доступно |

---

## Коды регионов в ссылках

Глубокие ссылки и URL-адреса, генерируемые виджетами, всегда используют стабильные коды **региона ** ( `istore://` , `us` , `cn` , `jp` , ...) — не локализованные имена дисплеев.

**Примеры**


```
istore://switch?region=jp
istore://switch?region=hk
```


[Назад к обзору] (..) · [FAQ] (../faq) · [Privacy] (../privacy)


