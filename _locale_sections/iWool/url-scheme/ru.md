iWool поддерживает ** `iwool://` ** Схема URL глубоких ссылок - откройте вкладку, начните действие в приложении или перейдите к определенной деятельности из Safari, ярлыков Apple, нажатия виджета или быстрого действия на домашнем экране (нажмите значок приложения).

> ** Важно:** Глубокие ссылки ** перемещаются внутри iWool**. Они не создают подключения к серверу и не синхронизируют данные с облаком.

## Спецификация протокола


```
iwool://<path>[?query]
```


| Rule | Подробнее |
|------|--------|
| **Scheme** | "iwool" (случайно нечувствительный) |
| **Routing** | Первый сегмент пути (хозяин или путь) выбирает пункт назначения. |
| **Empty URL** | «Iwool://» (без дорожки) |
| **Unknown paths** | **Игнорированный** (без молчаливого возвращения домой) |
| **Parser** | «IWoolDeepLink.parse( :)» → «ContentView.applyDeepLink» |

---

## 1. Пункты назначения вкладок

| URL | Открывает |
|-----|--------|---------|
| `iwool://home` | **Home** tab | — |
| `iwool://calendar` | **Calendar** tab | "каль" |
| `iwool://stats` | **Statistics** tab | "статистика", "статистика" |
| `iwool://settings` | **Settings** tab | "установка", "предпочтения" |

---

## 2. Действия в приложении

Эти маршруты соответствуют **Home Screen Quick Actions** и открытым листам или подстраницам:

| URL | Открывает |
|-----|--------|---------|
| `iwool://new` | **Create activity** sheet | «создать», «добавить», «новое событие», «новое событие» |
| `iwool://island` | **Quick Countdown** (Dynamic Island reminder) sheet | "остров-напоминание", "остров-напоминание", "отсчет", "быстрый отсчет", "быстрый отсчет" |
| `iwool://reminders` | **Scheduled local reminders** list (Settings) | "плановые напоминания", "плановые напоминания", "плановые напоминания" |
| `iwool://scanner` | **QR / barcode scanner** (Settings → Tools) | «scan», «qrcode», «barcode» |
| `iwool://rate` | In-app **App Store rating** prompt | «рейтинг», «обзор», «rate-in-app», «rateinapp» |
| `iwool://feedback` | **Feedback** email compose | "почта", "поддержка", "контакт" |

** Настроенные пути настроек** (те же действия):


```
iwool://settings/scanner
iwool://settings/reminders
iwool://settings/rate
iwool://settings/feedback
```


---

## 3. Детали деятельности

Откройте одну шерстяную активность по идентификатору базы данных.

| Parameter | Required | Описание |
|-----------|----------|-------------|
| Path `event/{id}` | One of path / query | Идентификатор активности (положительное целое число) |
| Query `id={id}` | One of path / query | Как и форма пути |
| Query `day={seconds}` | No | Для ** повторяющихся** действий — естественный день начинается как «timeIntervalSince1970» |

** Открытая деятельность 42**


```
iwool://event/42
iwool://event?id=42
```


** Повторяющиеся события в определенный день**


```
iwool://event/42?day=189345600
```


При создании ссылок для повторяющихся серий iWool может вывести `iwool://` из той же логики, что и домашний список ( `iwool` ).

---

## 4. Быстрые действия (iOS)

Длительное нажатие иконки iWool → до **4** действий. Настройка в **Настройки → Инструменты → Ярлыки домашнего экрана** (9 опций, перетащите на переупорядочение, сбросьте на по умолчанию).

| Option | URL |
|--------|-----|
| Home | "iwool://home" |
| Calendar | "iwool://calendar" |
| Statistics | "iwool://stats" |
| Quick Countdown | "iwool://island" |
| New Activity | "iwool://new" |
| Scheduled Reminders | "iwool://reminders" |
| Scanner | "iwool://scanner" |
| Rate App | "iwool://rate" |
| Feedback | "iwool://feedback" |

** Дефолт при первой установке: ** Домой · Календарь · Статистика · Быстрый обратный отсчет.

Струны быстрого действия `iwool://` используют те же пути `iwool` и маршрут через `iwool://` → `IWoolDeepLink.parse(_:)` на холодном старте.

---

## 5. Виджеты глубоких связей

Виджеты используют те же `iwool://` URL:

| Widget | Tap target | URL |
|--------|------------|-----|
| Today Active / Today All / Today Upcoming / All Events | Home | "iwool://home" |
| Stats Overview / Earnings / Top Platforms | Statistics | "iwool://stats" |
| Glance | First event or Home | "iwool://event/{id}" или "iwool://home" |
| Lock Screen accessories | First event or Home | "iwool://event/{id}" или "iwool://home" |
| List row (iOS 17+) | Activity detail | "iwool://event/{id}" |

Quick Countdown Live Activities использует только пользовательский интерфейс в приложении — ** нет отдельного URL**, чтобы начать обратный отсчет острова из-за пределов приложения (используйте `iwool://` , чтобы открыть лист создания).

---

## Примеры Apple Shortcuts

** Открытая статистика**


```
iwool://stats
```


**Создать новый проект**


```
iwool://new
```


** Быстрый обратный отсчет **


```
iwool://island
```


** Открытая деятельность после копирования ID**


```
iwool://event?id=42
```


---

## Запускное поведение

| Scenario | Поток |
|----------|------|
| **Widget / Shortcuts `onOpenURL`** | «AppRouter» — «applyDeep» Ссылка |
| **Cold start — Quick Action** | «ShortcutSceneDelegate» → «PendingShortcutBuffer» → «ShortcutObserver» |
| **Warm start — Quick Action** | Обратный вызов сцены → уведомление → «ShortcutObserver» |
| **Feedback / Rate (cold start)** | Короткая задержка, поэтому почтовый лист / StoreKit имеет активную сцену окна |
| **Invalid event ID** | Ссылка проигнорирована — нет предупреждения |

---

## устранение неполадок

| Issue | Что проверить |
|-------|----------------|
| Link opens app but nothing happens | Путь должен соответствовать поддерживаемому маршруту; неизвестные пути не перенаправлены на Домой |
| `event` link shows wrong occurrence | Добавить «?day=» для повторяющихся действий |
| Quick Action does nothing on cold launch | Подождите ~0,4 с или повторите; обратная связь / скорость требует времени установки пользовательского интерфейса |
| `iwool://island` does not start countdown automatically | Открывает **креационный лист ** — подтверждает продолжительность и нажимает Старт внутри приложения |
| Quick Countdown requires iOS 16.2+ | Event Live Activities требуется iOS 16.1+; автономный отсчет времени на острове требует 16.2+ |

---

[Назад в поддержку iWool] (..) · [FAQ] (../faq) · [Политика конфиденциальности] (../privacy)


