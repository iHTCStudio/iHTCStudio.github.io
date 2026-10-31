iConverter поддерживает `iconverter://` Схема URL глубоких ссылок — откройте любой из 101 инструмента из внешних приложений, веб-страниц, QR-кодов (генерировать или **сканировать в приложении **), Safari или Apple Shortcuts, необязательно предварительно заполнив поля ввода через параметры запроса.

> ** Примечание к виджету:** Выборщик инструментов виджета **Launcher** включает все поддерживаемые инструменты, кроме **Web Browser**. UI конфигурации виджета следует **iOS системному языку **, а не переопределению языка в приложении в соответствии с настройками.

## Спецификация протокола


```
iconverter://tool/<ToolItem.rawValue>?key=value&key2=value2
```


- «<ToolItem.rawValue>» имеет то же название, что и виджетные глубокие ссылки.
- Имена параметров поддерживают как короткие клавиши, так и синонимичные псевдонимы (например, «текст» эквивалентен «вводу»).
- «1/true/yes/on» — истинно; «0/false/no/off» — ложно.
- Даты: поддерживает Yyyy-MM-dd, ISO8601, Unix timetamp (секунды).
- Преобразователи блоков имеют общий формат: 'v' = значение, 'from' = единица источника (rawValue или символ, нечувствительный к случаю), 'to' = единица цели.

---

## 1.Калькулятор

**Калькулятор** - только открытый


```
iconverter://tool/calculator
```


** Научный калькулятор** — только открытый


```
iconverter://tool/scientific
```


**Калькулятор программиста** - только открытый


```
iconverter://tool/programmer
```


---

## 2. Финансы

** Ипотечный калькулятор** `iconverter://` = сумма кредита, `<ToolItem.rawValue>` = годовая ставка %, `text` = годы, `input` = 0 = равный взнос / 1 = равный основной капитал.


```
iconverter://tool/mortgage?p=1000000&r=3.7&y=30&mode=0
```


** Налог на прибыль** `iconverter://` = месячная зарплата, `<ToolItem.rawValue>` = социальное страхование, `text` = специальный вычет, `input` = порог, `1/true/yes/on` = годовой бонус.


```
iconverter://tool/incomeTax?salary=20000&insurance=3000&deduction=1000&threshold=5000&bonus=50000
```


**Комплексный интерес** `iconverter://` = основной, `<ToolItem.rawValue>` = ежемесячный взнос, `text` = годовая ставка %, `input` = годы, `1/true/yes/on` = 0 = годовая / 1 = ежемесячная / 2 = ежедневная, `0/false/no/off` = инфляция %.


```
iconverter://tool/compoundInterest?p=100000&m=1000&r=7&y=10&freq=1
```


** Калькулятор скидок** `iconverter://` = 0-4, `<ToolItem.rawValue>` = первоначальная цена, `text` = коэффициент дисконтирования, `input` = порог, `1/true/yes/on` = сумма сокращения.


```
iconverter://tool/discount?mode=0&p=299&r=8.5
```


Полный минус пример:


```
iconverter://tool/discount?mode=3&p=350&t=300&u=50
```


**Tip & AA Split** `iconverter://` = 0 = чаевые / 1 = раскол АА, `<ToolItem.rawValue>` = счет, `text` = чаевые %, `input` = налог %, `1/true/yes/on` = количество людей.


```
iconverter://tool/tipAA?mode=0&bill=200&tip=15&tax=0&ppl=4
```


**Ипотечная предоплата** `iconverter://` = первоначальный кредит, `<ToolItem.rawValue>` = годовая ставка %, `text` = общий срок (годы), `input` = оплаченные сроки, `1/true/yes/on` = предоплата, `0/false/no/off` = 0 = укоротить / 1 = сократить месячный / 2 = сравнивать.


```
iconverter://tool/mortgagePrepay?p=800000&r=3.7&total=30&paid=5&prepay=100000&mode=2
```


** Налог на недвижимость** — только открыт


```
iconverter://tool/realEstateTax
```


---

## 3. Дата и время

** Возраст и годовщина** `iconverter://` = день рождения `<ToolItem.rawValue>` , `text` = дата ссылки.


```
iconverter://tool/ageAnniversary?birth=1990-05-01&ref=2026-05-17
```


** Арифметика даты** `iconverter://` = 0 = добавить/вычесть / 1 = разница в датах.

Режим добавления-вычитания ( `iconverter://` = дата начала, `<ToolItem.rawValue>` = ± дней, `text` = ± недель, `input` = ± месяцев, `1/true/yes/on` = ± лет):


```
iconverter://tool/dateArithmetic?mode=0&d1=2026-05-17&d=100
```


Режим разницы ( `iconverter://` = дата 1, `<ToolItem.rawValue>` = дата 2):


```
iconverter://tool/dateArithmetic?mode=1&d1=2026-01-01&d2=2026-12-31
```


** Лунный календарь** `iconverter://` = григорианская дата `<ToolItem.rawValue>` .


```
iconverter://tool/lunarCalendar?date=2026-05-17
```


**Солнечные условия** - только открытые


```
iconverter://tool/solarTerms
```


**Обратный отсчет** `iconverter://` = имя события, `<ToolItem.rawValue>` = целевая дата `text` , `input` = время `1/true/yes/on` .


```
iconverter://tool/countdown?label=Holiday&target=2026-10-01&time=0
```


**Калькулятор беременности** `iconverter://` = 0 = LMP / 1 = зачатие / 2 = ЭКО, `<ToolItem.rawValue>` = дата отсчета, `text` = день эмбриона ЭКО 0 = D3 / 1 = D5.


```
iconverter://tool/pregnancy?method=0&ref=2026-03-01
```



```
iconverter://tool/pregnancy?method=2&ref=2026-03-15&ivf=1
```


** Менструальный цикл** `iconverter://` = дата последней менструации, `<ToolItem.rawValue>` = дни цикла, `text` = дни периода.


```
iconverter://tool/menstrual?lmp=2026-05-01&cycle=28&period=5
```


** Мировые часы** `iconverter://` = ключевое слово поиска по городу, `<ToolItem.rawValue>` = использовать текущее время `text` , `input` = пользовательское время даты.


```
iconverter://tool/worldClock?q=Tokyo
```



```
iconverter://tool/worldClock?now=0&ref=2026-05-17T20:00:00
```


**Зодиак** - открыт только


```
iconverter://tool/zodiac
```


---

## 4. Математика

** Процентный калькулятор** `iconverter://` = 0-4, `<ToolItem.rawValue>` = значение A, `text` = значение B.


```
iconverter://tool/percentage?mode=0&a=75&b=120
```


** Фракционный калькулятор** — только открытый


```
iconverter://tool/fraction
```


**Прайм-факторизация** - открыта только


```
iconverter://tool/primeFactor
```


**Quadratic Solver** — только открытый


```
iconverter://tool/quadraticSolver
```


**Статистика** `iconverter://` = набор данных, разделенный пространством / запятой / полуколоной.


```
iconverter://tool/statistics?data=1,2,3,4,5,6,7,8,9,10
```


** Комбинации и перестановки** — только открытые


```
iconverter://tool/combinations
```


** Геометрия** `iconverter://` = форма, `<ToolItem.rawValue>` / `text` / `input` = параметры размерности.

Доступные формы: `iconverter://` · `<ToolItem.rawValue>` · `text` · `input` · `1/true/yes/on` · `0/false/no/off` C6 `v` C8 `to` C10 `r` C13 `salary` C15 `deduction` .

Круг ( `iconverter://` = радиус):


```
iconverter://tool/geometry?shape=circle&v1=5
```


Прямоугольник ( `iconverter://` = длина, `<ToolItem.rawValue>` = ширина):


```
iconverter://tool/geometry?shape=rectangle&v1=10&v2=5
```


Сфера ( `iconverter://` = радиус):


```
iconverter://tool/geometry?shape=sphere&v1=3
```


Цилиндр ( `iconverter://` = радиус, `<ToolItem.rawValue>` = высота):


```
iconverter://tool/geometry?shape=cylinder&v1=4&v2=10
```


---

## 5. Кодирование

**Римские цифры** `iconverter://` = арабское число (1–3999); или `<ToolItem.rawValue>` = римская числовая строка.


```
iconverter://tool/roman?n=2026
```



```
iconverter://tool/roman?roman=MMXXVI
```


** База 64 Кодер / Декодер** `iconverter://` = encode/decode, `<ToolItem.rawValue>` = URL-безопасный режим `text` , `input` = входной текст.


```
iconverter://tool/base64?mode=encode&text=Hello%2C+World!
```



```
iconverter://tool/base64?mode=decode&urlSafe=0&text=SGVsbG8sIFdvcmxkIQ%3D%3D
```


**URL Encoder** `iconverter://` = код/декод, `<ToolItem.rawValue>` = режим компонента 0 = полный / 1 = запрос / 2 = путь, `text` = вход.


```
iconverter://tool/urlCoder?mode=encode&comp=0&text=https://example.com/path?q=hello world
```



```
iconverter://tool/urlCoder?mode=decode&text=https%3A%2F%2Fexample.com%2F%3Fq%3Dhello%20world
```


**Хеш-калькулятор** `iconverter://` = вход, `<ToolItem.rawValue>` = md5/sha1/sha256/sha512, `text` = верхний регистр `input` , `1/true/yes/on` = включить HMAC `0/false/no/off` , `yyyy-MM-dd` = HMAC ключ.


```
iconverter://tool/hashing?text=Hello+World&algo=sha256&upper=0
```



```
iconverter://tool/hashing?text=data&algo=md5&hmac=1&key=secret
```


** Счет слов**
.


```
iconverter://tool/wordCount?text=The+quick+brown+fox+jumps+over+the+lazy+dog.
```


** Цветовой преобразователь** `iconverter://` = шестнадцатеричный цвет; или `<ToolItem.rawValue>` / `text` / `input` = компоненты RGB (0-255).


```
iconverter://tool/colorConverter?hex=%23FF8800
```



```
iconverter://tool/colorConverter?r=255&g=136&b=0
```


** Цветная палитра** — открыта только


```
iconverter://tool/colorPalette
```


** QR-код** `iconverter://` = содержание, `<ToolItem.rawValue>` = `text` и т.д., `input` = уровень исправления ошибок `1/true/yes/on` .


```
iconverter://tool/qrcode?text=https%3A%2F%2Fexample.com&ecc=H
```



```
iconverter://tool/qrcode?text=Hello+iConverter&format=qr&ecc=M
```


**Джон Формат** `iconverter://` = строка JSON (URL-кодированная), `<ToolItem.rawValue>` = отступы 2/4.


```
iconverter://tool/jsonFormatter?text=%7B%22name%22%3A%22Alice%22%2C%22age%22%3A30%7D&indent=2
```


**Timesamp** `iconverter://` = Unix timetamp (секунды), `<ToolItem.rawValue>` = единица 0 = sec / 1 = ms; или `text` = строка даты ISO8601.


```
iconverter://tool/timestamp?ts=1747440000
```



```
iconverter://tool/timestamp?iso=2026-05-17T12:00:00
```


** Валидатор банковской карты** `iconverter://` = номер карты.


```
iconverter://tool/bankCard?num=6214830172816734
```


**Текстный конвертер**
.


```
iconverter://tool/textCase?text=hello+world+from+iConverter
```


**Text Diff** — только открытый


```
iconverter://tool/textDiff
```


**Запрос HTTP** `iconverter://` = URL запроса, `<ToolItem.rawValue>` = GET/POST/PUT/PATCH/DELETE, `text` = тело запроса, `input` = `1/true/yes/on` , `0/false/no/off` = заголовки JSON.


```
iconverter://tool/httpRequest?url=https%3A%2F%2Fapi.example.com%2Fusers&method=GET
```



```
iconverter://tool/httpRequest?url=https%3A%2F%2Fapi.example.com%2Fusers&method=POST&body=%7B%22name%22%3A%22Alice%22%7D&bodyKind=json
```


** Загрузить файл ** `iconverter://` = скачать URL, `<ToolItem.rawValue>` = имя файла (необязательно).


```
iconverter://tool/fileDownload?url=https%3A%2F%2Fexample.com%2Freport.pdf&name=report.pdf
```


** Коды состояния HTTP** `iconverter://` = код состояния; или `<ToolItem.rawValue>` = ключевое слово поиска.


```
iconverter://tool/httpStatusCodes?code=404
```



```
iconverter://tool/httpStatusCodes?q=redirect
```


**Полезность IP** `iconverter://` = subnet/cidr/range, `<ToolItem.rawValue>` = IP-адрес, `text` = маска подсети; или `input` = длина префикса CIDR.


```
iconverter://tool/ipUtility?mode=subnet&ip=192.168.1.0&mask=255.255.255.0
```



```
iconverter://tool/ipUtility?ip=10.0.0.0&prefix=24
```


** ASCII Table** `iconverter://` = десятичная кодовая точка; или `<ToolItem.rawValue>` = шестнадцатая кодовая точка; или `text` = поиск.


```
iconverter://tool/asciiTable?dec=65
```



```
iconverter://tool/asciiTable?q=space
```


** Генератор паролей** `iconverter://` = длина, `<ToolItem.rawValue>` = верхняя строчка `text` , `input` = нижняя строчка `1/true/yes/on` , `0/false/no/off` = цифры `yyyy-MM-dd` , `v` = символы `from` , `to` = никаких двусмысленных заголовков `p` , `r` = немедленно генерировать `y` .


```
iconverter://tool/passwordGenerator?length=20&upper=1&lower=1&digits=1&symbols=1&unambiguous=1&go=1
```


** Генератор случайных чисел** `iconverter://` = минимум, `<ToolItem.rawValue>` = максимум, `text` = счет, `input` = десятичные числа, `1/true/yes/on` = уникальный `0/false/no/off` , `yyyy-MM-dd` = 0 = нет / 1 = asc/2 = desc, `v` = немедленно генерировать `from` .


```
iconverter://tool/randomNumber?min=1&max=100&n=10&unique=1&sort=1&go=1
```



```
iconverter://tool/randomNumber?min=0&max=1&n=5&decimals=4&go=1
```


**Морской кодекс** `iconverter://` = код/декод, `<ToolItem.rawValue>` = входной текст.


```
iconverter://tool/morseCode?mode=encode&text=SOS
```



```
iconverter://tool/morseCode?mode=decode&text=...+---+...
```


** JWT Decoder** `iconverter://` = строка токена JWT.


```
iconverter://tool/jwtParser?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c
```


**Cron Expression Parser** `iconverter://` = Cron (пространства могут быть заменены на `<ToolItem.rawValue>` ).


```
iconverter://tool/cronParser?expr=0+9+*+*+1-5
```



```
iconverter://tool/cronParser?expr=0+0+*+*+*
```


**Регистрация** `iconverter://` = regex pattern (URL-encoded), `<ToolItem.rawValue>` = тестовый текст, `text` = замена, `input` = чувствительный к регистру `1/true/yes/on` , `0/false/no/off` = многолинейный `yyyy-MM-dd` , `v` = дотальный `from` .


```
iconverter://tool/regexTester?pattern=%5Cd%2B&haystack=abc123def456&i=0
```



```
iconverter://tool/regexTester?pattern=%28%5Cw%2B%29&haystack=hello+world&replacement=%5B%241%5D&i=1
```


** Веб-браузер** `iconverter://` = открытый URL; или `<ToolItem.rawValue>` = поисковый запрос (использует поисковую систему по умолчанию).


```
iconverter://tool/webBrowser?url=https%3A%2F%2Fexample.com
```



```
iconverter://tool/webBrowser?q=SwiftUI+deep+link+2026
```


---

## 6.Стиль жизни

**Калькулятор ИМТ** `iconverter://` = высота см, `<ToolItem.rawValue>` = вес кг, `text` = стандарт 0 = китайский взрослый / 1 = ВОЗ.


```
iconverter://tool/bmi?h=175&w=70&std=0
```


**Калькулятор BMR** `iconverter://` = высота см, `<ToolItem.rawValue>` = вес кг, `text` = возраст, `input` = м = мужчина / f = женщина, `1/true/yes/on` = уровень активности 0-4, `0/false/no/off` = 0 = Харрис-Бенедикт / 1 = Миффлин-Сент-Джор.


```
iconverter://tool/bmr?h=175&w=70&age=30&sex=m&act=1&formula=1
```


** Размер одежды** — только открытая


```
iconverter://tool/clothingSize
```


** Размер кольца** — только открытый


```
iconverter://tool/ringSize
```


** Конвертер высоты** - только открытый


```
iconverter://tool/heightConverter
```


** Калькулятор стоимости топлива** `iconverter://` = 0 = метрическая / 1 = имперская, `<ToolItem.rawValue>` = расстояние, `text` = расход на 100 км, `input` = цена топлива, `1/true/yes/on` = люди.


```
iconverter://tool/fuelCost?unit=0&d=500&c=8.5&p=7.8&n=1
```


** Калькулятор сборов** `iconverter://` = фактический вес кг, `<ToolItem.rawValue>` = первый вес кг, `text` = первый вес сбор, `input` = шаг вес кг, `1/true/yes/on` = шаг сбор.


```
iconverter://tool/shippingFee?w=3.5&fw=1&ff=12&sw=1&sf=8
```


С объемным весом ( `iconverter://` = включить `<ToolItem.rawValue>` , `text` / `input` / `1/true/yes/on` = три стороны см, `0/false/no/off` = делитель):


```
iconverter://tool/shippingFee?w=2&vol=1&l=50&wd=40&h=30&div=6000&fw=1&ff=12&sw=1&sf=8
```


** Содержание алкоголя в крови (BAC)** `iconverter://` = m = мужчина / f = женщина, `<ToolItem.rawValue>` = вес кг, `text` = объем мл, `input` = ABV %, `1/true/yes/on` = часы с момента употребления алкоголя.


```
iconverter://tool/alcoholBac?sex=m&w=70&v=500&abv=5&h=0.5
```


**Отношения** `iconverter://` = цепь отношений (разделенная на запятую), `<ToolItem.rawValue>` = пол эго 0 = мужчина / 1 = женщина, `text` = показать обратное `input` .


```
iconverter://tool/relationship?chain=f,os&sex=0&reverse=1
```



```
iconverter://tool/relationship?chain=m,ob&sex=1&reverse=0
```


** ID Card Parser**
номер удостоверения личности.


```
iconverter://tool/idCard?id=110101199003073010
```


**Coin Flip** — только открытый


```
iconverter://tool/coinFlip
```


**Dice Roller** — только открытая версия


```
iconverter://tool/diceRoller
```


**Random Draw** — только открыт


```
iconverter://tool/randomDraw
```


**Шпиновое колесо** - открыто только


```
iconverter://tool/spinWheel
```


**Video Frame Export** - только для видео


```
iconverter://tool/videoFrameExport
```


---

## 7. Датчики

**Компас** - только открытый


```
iconverter://tool/compass
```


**Уровень ** - открыт только


```
iconverter://tool/level
```


**Алгоритм** — только открытый


```
iconverter://tool/altitude
```


---

## 8.Китайский

** Китайский номер** `iconverter://` = число.


```
iconverter://tool/chineseNumber?n=12345.67
```


** Китайский обратный номер** `iconverter://` = китайская строка.


```
iconverter://tool/chineseNumberReverse?text=一万二千三百四十五
```


** Финансовая сумма** `iconverter://` = сумма, `<ToolItem.rawValue>` = добавление . `text` .


```
iconverter://tool/financialAmount?amount=12345.67&zheng=1
```


---

## 9. Единичные преобразователи

Общий формат: `iconverter://` = значение, `<ToolItem.rawValue>` = единица источника (rawValue или символ, case-insensitive), `text` = единица цели.

---

** Длина**
Общие единицы: `iconverter://` (m) · `<ToolItem.rawValue>` (km) · `text` (cm) · `input` (mm) · `1/true/yes/on` (ft) · `0/false/no/off` (in) · `yyyy-MM-dd` (mi) · `v` (yd) · `from` (nmi) · `to` ().) · `p` ().).


```
iconverter://tool/length?v=100&from=meter&to=foot
```



```
iconverter://tool/length?v=1&from=mile&to=kilometer
```


**Зона**
Общие единицы: `iconverter://` (m2) · `<ToolItem.rawValue>` (ha) · `text` (acre) · `input` (ft2) · `1/true/yes/on` (mile2) · `0/false/no/off` (.) · `yyyy-MM-dd` (km2).


```
iconverter://tool/area?v=1&from=hectare&to=mu
```



```
iconverter://tool/area?v=1&from=acre&to=squareMeter
```


**Объем**
Общие единицы: `iconverter://` (L) · `<ToolItem.rawValue>` (mL) · `text` (m3) · `input` (gal) · `1/true/yes/on` (fl oz) · `0/false/no/off` (cup) · `yyyy-MM-dd` (gal UK) · `v` (bbl).


```
iconverter://tool/volume?v=1&from=gallon&to=liter
```



```
iconverter://tool/volume?v=355&from=milliliter&to=fluidOunce
```


** Вес / Масса**
Общие единицы: `iconverter://` (kg) · `<ToolItem.rawValue>` (g) · `text` (lb) · `input` (oz) · `1/true/yes/on` (t) · `0/false/no/off` ().) · `yyyy-MM-dd` ().) · `v` (ct).


```
iconverter://tool/weight?v=1&from=pound&to=kilogram
```



```
iconverter://tool/weight?v=1&from=jin&to=gram
```


** Температура**
Единицы: `iconverter://` (°C) · `<ToolItem.rawValue>` (°F) · `text` (K) · `input` (°R) · `1/true/yes/on` (°Re).


```
iconverter://tool/temperature?v=100&from=celsius&to=fahrenheit
```



```
iconverter://tool/temperature?v=37&from=celsius&to=kelvin
```


** Время**
Общие единицы: `iconverter://` (s) · `<ToolItem.rawValue>` (min) · `text` (h) · `input` (day) · `1/true/yes/on` (wk) · `0/false/no/off` (mo) · `yyyy-MM-dd` (yr) · `v` (ms) · `from` (μs).


```
iconverter://tool/time?v=1&from=hour&to=second
```



```
iconverter://tool/time?v=7&from=day&to=hour
```


** Скорость**
Единицы: `iconverter://` (m/s) · `<ToolItem.rawValue>` (km/h) · `text` (mph) · `input` (kn) · `1/true/yes/on` (Ma).


```
iconverter://tool/speed?v=100&from=kmPerHour&to=milePerHour
```



```
iconverter://tool/speed?v=1&from=mach&to=meterPerSecond
```


** Давление**
Единицы: `iconverter://` (Pa) · `<ToolItem.rawValue>` (kPa) · `text` (bar) · `input` (atm) · `1/true/yes/on` (psi) · `0/false/no/off` (mmHg).


```
iconverter://tool/pressure?v=1&from=atmosphere&to=kilopascal
```



```
iconverter://tool/pressure?v=120&from=mmHg&to=kilopascal
```


** Энергия**
Единицы: `iconverter://` (J) · `<ToolItem.rawValue>` (kJ) · `text` (cal) · `input` (kcal) · `1/true/yes/on` (kWh) · `0/false/no/off` (BTU).


```
iconverter://tool/energy?v=1&from=kilowattHour&to=kilojoule
```



```
iconverter://tool/energy?v=500&from=kilocalorie&to=kilojoule
```


** Власть**
Единицы: `iconverter://` (W) · `<ToolItem.rawValue>` (kW) · `text` (hp) · `input` (PS) · `1/true/yes/on` (BTU/h).


```
iconverter://tool/power?v=1&from=hpMechanical&to=kilowatt
```



```
iconverter://tool/power?v=3000&from=watt&to=hpMetric
```


** Сила**
Единицы: `iconverter://` (N) · `<ToolItem.rawValue>` (kN) · `text` (kgf) · `input` (lbf) · `1/true/yes/on` (dyn).


```
iconverter://tool/force?v=9.8&from=newton&to=kgf
```



```
iconverter://tool/force?v=1&from=kilonewton&to=lbf
```


** Торк**
Единицы: `iconverter://` (N·m) · `<ToolItem.rawValue>` (N·cm) · `text` (kgf·m) · `input` (ft·lb) · `1/true/yes/on` (in·lb).


```
iconverter://tool/torque?v=100&from=newtonMeter&to=footPound
```


** Частота**
Единицы: `iconverter://` (Гц) · `<ToolItem.rawValue>` (кГц) · `text` (МГц) · `input` (ГГц) · `1/true/yes/on` (THz) · `0/false/no/off` (rpm).


```
iconverter://tool/frequency?v=2.4&from=gigahertz&to=megahertz
```



```
iconverter://tool/frequency?v=3000&from=rpm&to=hertz
```


**Англия**
Единицы: `iconverter://` (°) · `<ToolItem.rawValue>` (rad) · `text` (grad) · `input` (') · `1/true/yes/on` (") · `0/false/no/off` (turn).


```
iconverter://tool/angle?v=180&from=degree&to=radian
```



```
iconverter://tool/angle?v=1&from=turn&to=degree
```


** Хранение данных**
Единицы: `iconverter://` (B) · `<ToolItem.rawValue>` (KB) · `text` (MB) · `input` (GB) · `1/true/yes/on` (TB) · `0/false/no/off` (KiB) · `yyyy-MM-dd` (MiB) · `v` (GiB).


```
iconverter://tool/dataStorage?v=1&from=gigabyte&to=mebibyte
```



```
iconverter://tool/dataStorage?v=512&from=mebibyte&to=gigabyte
```


**Данные**
Единицы: `iconverter://` (bps) · `<ToolItem.rawValue>` (Kbps) · `text` (Mbps) · `input` (Gbps) · `1/true/yes/on` (KB/s) · `0/false/no/off` (MB/s) · `yyyy-MM-dd` (GB/s).


```
iconverter://tool/dataRate?v=100&from=mbps&to=mBps
```



```
iconverter://tool/dataRate?v=1&from=gbps&to=mbps
```


** Освещение**
Единицы: `iconverter://` (lx) · `<ToolItem.rawValue>` (fc) · `text` (ph) · `input` (nx).


```
iconverter://tool/illuminance?v=500&from=lux&to=footCandle
```


**Магнитная плотность потока**
Единицы: `iconverter://` (T) · `<ToolItem.rawValue>` (mT) · `text` (μT) · `input` (G) · `1/true/yes/on` (mG).


```
iconverter://tool/magneticFlux?v=1&from=tesla&to=gauss
```


** Радиоактивность**
Единицы: `iconverter://` (Bq) · `<ToolItem.rawValue>` (kBq) · `text` (MBq) · `input` (Ci) · `1/true/yes/on` (mCi) · `0/false/no/off` (μCi).


```
iconverter://tool/radioactivity?v=1&from=curie&to=megabecquerel
```


** Вязкость**
Единицы: `iconverter://` (Pa·s) · `<ToolItem.rawValue>` (mPa·s) · `text` (P) · `input` (cP).


```
iconverter://tool/viscosity?v=1&from=pascalSecond&to=centipoise
```


**Топливная экономика**
Единицы: `iconverter://` (L/100km) · `<ToolItem.rawValue>` (km/L) · `text` (MPG US) · `input` (MPG UK).


```
iconverter://tool/fuelEconomy?v=8.5&from=lPer100km&to=kmPerL
```



```
iconverter://tool/fuelEconomy?v=30&from=mpgUS&to=lPer100km
```


** Потоковая ставка**
Единицы: `iconverter://` (m3/s) · `<ToolItem.rawValue>` (m3/h) · `text` (L/s) · `input` (L/min) · `1/true/yes/on` (L/h) · `0/false/no/off` (gpm US) · `yyyy-MM-dd` (cfm).


```
iconverter://tool/flowRate?v=1&from=literPerMinute&to=cubicMeterPerHour
```


** Плотность**
Единицы: `iconverter://` (kg/m3) · `<ToolItem.rawValue>` (g/cm3) · `text` (g/L) · `input` (kg/L) · `1/true/yes/on` (lb/ft3).


```
iconverter://tool/density?v=1&from=gramPerCubicCentimeter&to=kgPerCubicMeter
```


** Магнитный поток (Wb)**
Единицы: `iconverter://` (Wb) · `<ToolItem.rawValue>` (mWb) · `text` (μWb) · `input` (kWb) · `1/true/yes/on` (Mx).


```
iconverter://tool/magneticFluxTrue?v=1&from=weber&to=maxwell
```


** Поглощенная доза**
Единицы: `iconverter://` (Gy) · `<ToolItem.rawValue>` (mGy) · `text` (μGy) · `input` (kGy) · `1/true/yes/on` (rad) · `0/false/no/off` (mrad).


```
iconverter://tool/absorbedDose?v=1&from=gray&to=rad
```


** Эквивалентная доза**
Единицы: `iconverter://` (Sv) · `<ToolItem.rawValue>` (mSv) · `text` (μSv) · `input` (rem) · `1/true/yes/on` (mrem).


```
iconverter://tool/equivalentDose?v=1&from=sievert&to=rem
```



```
iconverter://tool/equivalentDose?v=20&from=millisievert&to=microsievert
```


** Количество вещества**
Единицы: `iconverter://` (mol) · `<ToolItem.rawValue>` (mmol) · `text` (μmol) · `input` (kmol) · `1/true/yes/on` (nmol) · `0/false/no/off` (pmol).


```
iconverter://tool/amountOfSubstance?v=1&from=mole&to=millimole
```



```
iconverter://tool/amountOfSubstance?v=150&from=millimole&to=micromole
```


---

[Назад к поддержке iConverter](../) &middot; [FAQ](../faq) &middot; [Политика конфиденциальности](../privacy)


