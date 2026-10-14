iAppManager поддерживает ссылки ** `iappmanager://` ** для ярлыков, виджетов, намерений приложений и действий на домашнем экране.

## Формат ссылки


```
iappmanager://{host}[/…]
```


## Приложения и модули

| URL | Открывает |
|-----|-------|
| `iappmanager://apps` | Мои приложения |
| `iappmanager://apps/{appleId}` | Специальное приложение (Overview) |
| `iappmanager://apps/{appleId}/{tab}` | Модуль детализации | `iappmanager://` - это идентификатор приложения App Store Connect / App Store. `iappmanager://apps` Примеры:

| Tab | модуль |
|-----|--------|
| `overview` | Обзор |
| `versions` | Версии |
| `builds` | строить |
| `backgroundAssets` | Справочная информация об активах |
| `encryption` | шифрование |
| `submissions` | Обзор представлений |
| `reviewDetail` | Подробная информация |
| `metadata` | Метаданные |
| `media` | Скриншоты и предварительные просмотры |
| `productPages` | Пользовательские страницы продукта |
| `appEvents` | События In-App |
| `appClips` | App Clips |
| `experiments` | Хранить эксперименты |
| `nominations` | Показаны номинанты |
| `availability` | наличие |
| `pricing` | цены |
| `ageRating` | Возрастной рейтинг |
| `accessibility` | Доступность |
| `appTags` | App Tags |
| `iap` | Покупки в приложении |
| `gameCenter` | Игровой центр |
| `testflight` | испытательный полет |
| `reviews` | Отзывы клиентов |
| `privacy` | Конфиденциальность (пищевая записка) |
| `promoCodes` | Промо-коды |
| `webhooks` | Вебхуки |

Пример: `iappmanager://` ## Sidebar и инструменты

| URL | Открывает |
|-----|-------|
| `iappmanager://certificates` | Сертификаты и идентификаторы |
| `iappmanager://users` | Пользователи и доступ |
| `iappmanager://reports` | Доклады |
| `iappmanager://settings` | Настройки |
| `iappmanager://add-account` | Добавить API Key Account |
| `iappmanager://about` | О нас |
| `iappmanager://feedback` | Письмо с отзывом |
| `iappmanager://in-app-review` | Быстрая ставка |

## Руководство для приложений

| URL | Guide |
|-----|-------|
| `iappmanager://feature-guide` | Особенности тура |
| `iappmanager://usage-guide` | Руководство по использованию |
| `iappmanager://widget-guide` | Руководство по виджетам |
| `iappmanager://shortcuts-guide` | Руководство по «Командам» |
| `iappmanager://release-guide` | Готовность к освобождению |
| `iappmanager://iap-guide` | IAP и подписки |
| `iappmanager://testflight-guide` | испытательный полет |
| `iappmanager://reports-guide` | Доклады |

Холодные и теплые запуски ненадолго буферизируют глубокие связи, поэтому посадка на борт может закончиться первой. App Intents также может открыть управляемое приложение с дополнительным модулем.


