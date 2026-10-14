---
layout: doc
title: iConverter — URL Scheme Reference
app_id: iConverter
doc_title_en: URL Scheme Reference
doc_title_zh_cn: URL Scheme 深度链接文档
doc_title_zh_tw: URL Scheme 深度連結文件
description: Complete reference of iconverter:// deep links supported by iConverter.
---

<section lang="en" markdown="1">

iConverter supports `iconverter://` URL scheme deep links — open any of the 101 tools from external apps, web pages, QR codes (generate or **scan in-app**), Safari, or Apple Shortcuts, optionally pre-filling input fields via query parameters.

> **Widget note:** The **Launcher** widget tool picker includes all supported tools except **Web Browser**. Widget configuration UI follows **iOS system language**, not the in-app language override under Settings.

## Protocol Specification

```
iconverter://tool/<ToolItem.rawValue>?key=value&key2=value2
```

- `<ToolItem.rawValue>` shares the same naming as widget deep links.
- Parameter names support both short keys and synonymous aliases (e.g. `text` is equivalent to `input`).
- Booleans: `1/true/yes/on` → true; `0/false/no/off` → false.
- Dates: supports `yyyy-MM-dd`, ISO8601, Unix timestamp (seconds).
- Unit converters share a common format: `v` = value, `from` = source unit (rawValue or symbol, case-insensitive), `to` = target unit.

---

## 1. Calculator

**Calculator** — open only

```
iconverter://tool/calculator
```

**Scientific Calculator** — open only

```
iconverter://tool/scientific
```

**Programmer Calculator** — open only

```
iconverter://tool/programmer
```

---

## 2. Finance

**Mortgage Calculator**
`p` = loan amount, `r` = annual rate %, `y` = years, `mode` = 0 = equal installment / 1 = equal principal.

```
iconverter://tool/mortgage?p=1000000&r=3.7&y=30&mode=0
```

**Income Tax**
`salary` = monthly salary, `insurance` = social insurance, `deduction` = special deduction, `threshold` = threshold, `bonus` = annual bonus.

```
iconverter://tool/incomeTax?salary=20000&insurance=3000&deduction=1000&threshold=5000&bonus=50000
```

**Compound Interest**
`p` = principal, `m` = monthly contribution, `r` = annual rate %, `y` = years, `freq` = 0 = annual / 1 = monthly / 2 = daily, `i` = inflation %.

```
iconverter://tool/compoundInterest?p=100000&m=1000&r=7&y=10&freq=1
```

**Discount Calculator**
`mode` = 0–4, `p` = original price, `r` = discount ratio, `t` = threshold, `u` = reduction amount.

```
iconverter://tool/discount?mode=0&p=299&r=8.5
```

Full-minus example:

```
iconverter://tool/discount?mode=3&p=350&t=300&u=50
```

**Tip & AA Split**
`mode` = 0 = tip / 1 = AA split, `bill` = bill, `tip` = tip %, `tax` = tax %, `ppl` = people count.

```
iconverter://tool/tipAA?mode=0&bill=200&tip=15&tax=0&ppl=4
```

**Mortgage Prepayment**
`p` = original loan, `r` = annual rate %, `total` = total term (years), `paid` = paid terms, `prepay` = prepay amount, `mode` = 0 = shorten / 1 = reduce monthly / 2 = compare.

```
iconverter://tool/mortgagePrepay?p=800000&r=3.7&total=30&paid=5&prepay=100000&mode=2
```

**Real Estate Tax** — open only

```
iconverter://tool/realEstateTax
```

---

## 3. Date & Time

**Age & Anniversary**
`birth` = birthday `yyyy-MM-dd`, `ref` = reference date.

```
iconverter://tool/ageAnniversary?birth=1990-05-01&ref=2026-05-17
```

**Date Arithmetic**
`mode` = 0 = add/subtract / 1 = date difference.

Add-subtract mode (`d1` = start date, `d` = ± days, `w` = ± weeks, `mo` = ± months, `y` = ± years):

```
iconverter://tool/dateArithmetic?mode=0&d1=2026-05-17&d=100
```

Difference mode (`d1` = date 1, `d2` = date 2):

```
iconverter://tool/dateArithmetic?mode=1&d1=2026-01-01&d2=2026-12-31
```

**Lunar Calendar**
`date` = Gregorian date `yyyy-MM-dd`.

```
iconverter://tool/lunarCalendar?date=2026-05-17
```

**Solar Terms** — open only

```
iconverter://tool/solarTerms
```

**Countdown**
`label` = event name, `target` = target date `yyyy-MM-dd`, `time` = include time `0/1`.

```
iconverter://tool/countdown?label=Holiday&target=2026-10-01&time=0
```

**Pregnancy Calculator**
`method` = 0 = LMP / 1 = conception / 2 = IVF, `ref` = reference date, `ivf` = IVF embryo day 0 = D3 / 1 = D5.

```
iconverter://tool/pregnancy?method=0&ref=2026-03-01
```

```
iconverter://tool/pregnancy?method=2&ref=2026-03-15&ivf=1
```

**Menstrual Cycle**
`lmp` = last menstrual period date, `cycle` = cycle days, `period` = period days.

```
iconverter://tool/menstrual?lmp=2026-05-01&cycle=28&period=5
```

**World Clock**
`q` = city search keyword, `now` = use current time `0/1`, `ref` = custom datetime.

```
iconverter://tool/worldClock?q=Tokyo
```

```
iconverter://tool/worldClock?now=0&ref=2026-05-17T20:00:00
```

**Zodiac** — open only

```
iconverter://tool/zodiac
```

---

## 4. Math

**Percentage Calculator**
`mode` = 0–4, `a` = value A, `b` = value B.

```
iconverter://tool/percentage?mode=0&a=75&b=120
```

**Fraction Calculator** — open only

```
iconverter://tool/fraction
```

**Prime Factorization** — open only

```
iconverter://tool/primeFactor
```

**Quadratic Solver** — open only

```
iconverter://tool/quadraticSolver
```

**Statistics**
`data` = dataset, separated by space / comma / semicolon.

```
iconverter://tool/statistics?data=1,2,3,4,5,6,7,8,9,10
```

**Combinations & Permutations** — open only

```
iconverter://tool/combinations
```

**Geometry**
`shape` = shape, `v1` / `v2` / `v3` = dimension parameters.

Available shapes: `rectangle` · `square` · `circle` · `triangle` · `triangleSSS` · `parallelogram` · `trapezoid` · `sector` · `ellipse` · `regularPolygon` · `sphere` · `hemisphere` · `cylinder` · `cone` · `frustum` · `cube` · `cuboid`.

Circle (`v1` = radius):

```
iconverter://tool/geometry?shape=circle&v1=5
```

Rectangle (`v1` = length, `v2` = width):

```
iconverter://tool/geometry?shape=rectangle&v1=10&v2=5
```

Sphere (`v1` = radius):

```
iconverter://tool/geometry?shape=sphere&v1=3
```

Cylinder (`v1` = radius, `v2` = height):

```
iconverter://tool/geometry?shape=cylinder&v1=4&v2=10
```

---

## 5. Encoding

**Roman Numeral**
`n` = Arabic number (1–3999); or `roman` = Roman numeral string.

```
iconverter://tool/roman?n=2026
```

```
iconverter://tool/roman?roman=MMXXVI
```

**Base64 Encoder / Decoder**
`mode` = encode/decode, `urlSafe` = URL-safe mode `0/1`, `text` = input text.

```
iconverter://tool/base64?mode=encode&text=Hello%2C+World!
```

```
iconverter://tool/base64?mode=decode&urlSafe=0&text=SGVsbG8sIFdvcmxkIQ%3D%3D
```

**URL Encoder / Decoder**
`mode` = encode/decode, `comp` = component mode 0 = full / 1 = query / 2 = path, `text` = input.

```
iconverter://tool/urlCoder?mode=encode&comp=0&text=https://example.com/path?q=hello world
```

```
iconverter://tool/urlCoder?mode=decode&text=https%3A%2F%2Fexample.com%2F%3Fq%3Dhello%20world
```

**Hash Calculator**
`text` = input, `algo` = md5/sha1/sha256/sha512, `upper` = uppercase `0/1`, `hmac` = enable HMAC `0/1`, `key` = HMAC key.

```
iconverter://tool/hashing?text=Hello+World&algo=sha256&upper=0
```

```
iconverter://tool/hashing?text=data&algo=md5&hmac=1&key=secret
```

**Word Count**
`text` = text to analyze.

```
iconverter://tool/wordCount?text=The+quick+brown+fox+jumps+over+the+lazy+dog.
```

**Color Converter**
`hex` = hex color; or `r` / `g` / `b` = RGB components (0–255).

```
iconverter://tool/colorConverter?hex=%23FF8800
```

```
iconverter://tool/colorConverter?r=255&g=136&b=0
```

**Color Palette** — open only

```
iconverter://tool/colorPalette
```

**QR Code**
`text` = content, `format` = `qr/aztec/code128/pdf417` etc., `ecc` = error correction level `L/M/Q/H`.

```
iconverter://tool/qrcode?text=https%3A%2F%2Fexample.com&ecc=H
```

```
iconverter://tool/qrcode?text=Hello+iConverter&format=qr&ecc=M
```

**JSON Formatter**
`text` = JSON string (URL-encoded), `indent` = indent spaces 2/4.

```
iconverter://tool/jsonFormatter?text=%7B%22name%22%3A%22Alice%22%2C%22age%22%3A30%7D&indent=2
```

**Timestamp**
`ts` = Unix timestamp (seconds), `u` = unit 0 = sec / 1 = ms; or `iso` = ISO8601 date string.

```
iconverter://tool/timestamp?ts=1747440000
```

```
iconverter://tool/timestamp?iso=2026-05-17T12:00:00
```

**Bank Card Validator**
`num` = card number.

```
iconverter://tool/bankCard?num=6214830172816734
```

**Text Case Converter**
`text` = input text.

```
iconverter://tool/textCase?text=hello+world+from+iConverter
```

**Text Diff** — open only

```
iconverter://tool/textDiff
```

**HTTP Request**
`url` = request URL, `method` = GET/POST/PUT/PATCH/DELETE, `body` = request body, `bodyKind` = `json/form/text`, `headers` = headers JSON.

```
iconverter://tool/httpRequest?url=https%3A%2F%2Fapi.example.com%2Fusers&method=GET
```

```
iconverter://tool/httpRequest?url=https%3A%2F%2Fapi.example.com%2Fusers&method=POST&body=%7B%22name%22%3A%22Alice%22%7D&bodyKind=json
```

**File Download**
`url` = download URL, `name` = filename (optional).

```
iconverter://tool/fileDownload?url=https%3A%2F%2Fexample.com%2Freport.pdf&name=report.pdf
```

**HTTP Status Codes**
`code` = status code; or `q` = search keyword.

```
iconverter://tool/httpStatusCodes?code=404
```

```
iconverter://tool/httpStatusCodes?q=redirect
```

**IP Utility**
`mode` = subnet/cidr/range, `ip` = IP address, `mask` = subnet mask; or `prefix` = CIDR prefix length.

```
iconverter://tool/ipUtility?mode=subnet&ip=192.168.1.0&mask=255.255.255.0
```

```
iconverter://tool/ipUtility?ip=10.0.0.0&prefix=24
```

**ASCII Table**
`dec` = decimal codepoint; or `hex` = hex codepoint; or `q` = search.

```
iconverter://tool/asciiTable?dec=65
```

```
iconverter://tool/asciiTable?q=space
```

**Password Generator**
`length` = length, `upper` = uppercase `0/1`, `lower` = lowercase `0/1`, `digits` = digits `0/1`, `symbols` = symbols `0/1`, `unambiguous` = no ambiguous chars `0/1`, `go` = generate immediately `1`.

```
iconverter://tool/passwordGenerator?length=20&upper=1&lower=1&digits=1&symbols=1&unambiguous=1&go=1
```

**Random Number Generator**
`min` = minimum, `max` = maximum, `n` = count, `decimals` = decimal places, `unique` = unique `0/1`, `sort` = 0 = none / 1 = asc / 2 = desc, `go` = generate immediately `1`.

```
iconverter://tool/randomNumber?min=1&max=100&n=10&unique=1&sort=1&go=1
```

```
iconverter://tool/randomNumber?min=0&max=1&n=5&decimals=4&go=1
```

**Morse Code**
`mode` = encode/decode, `text` = input text.

```
iconverter://tool/morseCode?mode=encode&text=SOS
```

```
iconverter://tool/morseCode?mode=decode&text=...+---+...
```

**JWT Decoder**
`token` = JWT token string.

```
iconverter://tool/jwtParser?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c
```

**Cron Expression Parser**
`expr` = Cron expression (spaces can be replaced with `+`).

```
iconverter://tool/cronParser?expr=0+9+*+*+1-5
```

```
iconverter://tool/cronParser?expr=0+0+*+*+*
```

**Regex Tester**
`pattern` = regex pattern (URL-encoded), `haystack` = test text, `replacement` = replacement, `i` = case-insensitive `0/1`, `m` = multiline `0/1`, `s` = dotall `0/1`.

```
iconverter://tool/regexTester?pattern=%5Cd%2B&haystack=abc123def456&i=0
```

```
iconverter://tool/regexTester?pattern=%28%5Cw%2B%29&haystack=hello+world&replacement=%5B%241%5D&i=1
```

**Web Browser**
`url` = open URL directly; or `q` = search query (uses default search engine).

```
iconverter://tool/webBrowser?url=https%3A%2F%2Fexample.com
```

```
iconverter://tool/webBrowser?q=SwiftUI+deep+link+2026
```

---

## 6. Lifestyle

**BMI Calculator**
`h` = height cm, `w` = weight kg, `std` = standard 0 = Chinese adult / 1 = WHO.

```
iconverter://tool/bmi?h=175&w=70&std=0
```

**BMR Calculator**
`h` = height cm, `w` = weight kg, `age` = age, `sex` = m = male / f = female, `act` = activity level 0–4, `formula` = 0 = Harris-Benedict / 1 = Mifflin-St Jeor.

```
iconverter://tool/bmr?h=175&w=70&age=30&sex=m&act=1&formula=1
```

**Clothing Size** — open only

```
iconverter://tool/clothingSize
```

**Ring Size** — open only

```
iconverter://tool/ringSize
```

**Height Converter** — open only

```
iconverter://tool/heightConverter
```

**Fuel Cost Calculator**
`unit` = 0 = metric / 1 = imperial, `d` = distance, `c` = consumption per 100 km, `p` = fuel price, `n` = people.

```
iconverter://tool/fuelCost?unit=0&d=500&c=8.5&p=7.8&n=1
```

**Shipping Fee Calculator**
`w` = actual weight kg, `fw` = first weight kg, `ff` = first-weight fee, `sw` = step weight kg, `sf` = step fee.

```
iconverter://tool/shippingFee?w=3.5&fw=1&ff=12&sw=1&sf=8
```

With volumetric weight (`vol` = enable `0/1`, `l` / `wd` / `h` = three sides cm, `div` = divisor):

```
iconverter://tool/shippingFee?w=2&vol=1&l=50&wd=40&h=30&div=6000&fw=1&ff=12&sw=1&sf=8
```

**Blood Alcohol Content (BAC)**
`sex` = m = male / f = female, `w` = weight kg, `v` = volume mL, `abv` = ABV %, `h` = hours since drinking.

```
iconverter://tool/alcoholBac?sex=m&w=70&v=500&abv=5&h=0.5
```

**Relationship**
`chain` = relationship chain (comma-separated), `sex` = ego sex 0 = male / 1 = female, `reverse` = show reverse `0/1`.

```
iconverter://tool/relationship?chain=f,os&sex=0&reverse=1
```

```
iconverter://tool/relationship?chain=m,ob&sex=1&reverse=0
```

**ID Card Parser**
`id` = ID card number.

```
iconverter://tool/idCard?id=110101199003073010
```

**Coin Flip** — open only

```
iconverter://tool/coinFlip
```

**Dice Roller** — open only

```
iconverter://tool/diceRoller
```

**Random Draw** — open only

```
iconverter://tool/randomDraw
```

**Spin Wheel** — open only

```
iconverter://tool/spinWheel
```

**Video Frame Export** — open only

```
iconverter://tool/videoFrameExport
```

---

## 7. Sensors

**Compass** — open only

```
iconverter://tool/compass
```

**Level** — open only

```
iconverter://tool/level
```

**Altitude** — open only

```
iconverter://tool/altitude
```

---

## 8. Chinese

**Chinese Number**
`n` = number.

```
iconverter://tool/chineseNumber?n=12345.67
```

**Chinese Number Reverse**
`text` = Chinese numeral string.

```
iconverter://tool/chineseNumberReverse?text=一万二千三百四十五
```

**Financial Amount**
`amount` = amount, `zheng` = append 整 `0/1`.

```
iconverter://tool/financialAmount?amount=12345.67&zheng=1
```

---

## 9. Unit Converters

General format: `v` = value, `from` = source unit (rawValue or symbol, case-insensitive), `to` = target unit.

---

**Length**
Common units: `meter` (m) · `kilometer` (km) · `centimeter` (cm) · `millimeter` (mm) · `foot` (ft) · `inch` (in) · `mile` (mi) · `yard` (yd) · `nauticalMile` (nmi) · `chineseLi` (里) · `chineseChi` (尺).

```
iconverter://tool/length?v=100&from=meter&to=foot
```

```
iconverter://tool/length?v=1&from=mile&to=kilometer
```

**Area**
Common units: `squareMeter` (m²) · `hectare` (ha) · `acre` (acre) · `squareFoot` (ft²) · `squareMile` (mile²) · `mu` (亩) · `squareKilometer` (km²).

```
iconverter://tool/area?v=1&from=hectare&to=mu
```

```
iconverter://tool/area?v=1&from=acre&to=squareMeter
```

**Volume**
Common units: `liter` (L) · `milliliter` (mL) · `cubicMeter` (m³) · `gallon` (gal) · `fluidOunce` (fl oz) · `cup` (cup) · `ukGallon` (gal UK) · `oilBarrel` (bbl).

```
iconverter://tool/volume?v=1&from=gallon&to=liter
```

```
iconverter://tool/volume?v=355&from=milliliter&to=fluidOunce
```

**Weight / Mass**
Common units: `kilogram` (kg) · `gram` (g) · `pound` (lb) · `ounce` (oz) · `tonne` (t) · `jin` (斤) · `liang` (两) · `carat` (ct).

```
iconverter://tool/weight?v=1&from=pound&to=kilogram
```

```
iconverter://tool/weight?v=1&from=jin&to=gram
```

**Temperature**
Units: `celsius` (°C) · `fahrenheit` (°F) · `kelvin` (K) · `rankine` (°R) · `reaumur` (°Re).

```
iconverter://tool/temperature?v=100&from=celsius&to=fahrenheit
```

```
iconverter://tool/temperature?v=37&from=celsius&to=kelvin
```

**Time**
Common units: `second` (s) · `minute` (min) · `hour` (h) · `day` (day) · `week` (wk) · `month` (mo) · `year` (yr) · `millisecond` (ms) · `microsecond` (μs).

```
iconverter://tool/time?v=1&from=hour&to=second
```

```
iconverter://tool/time?v=7&from=day&to=hour
```

**Speed**
Units: `meterPerSecond` (m/s) · `kmPerHour` (km/h) · `milePerHour` (mph) · `knot` (kn) · `mach` (Ma).

```
iconverter://tool/speed?v=100&from=kmPerHour&to=milePerHour
```

```
iconverter://tool/speed?v=1&from=mach&to=meterPerSecond
```

**Pressure**
Units: `pascal` (Pa) · `kilopascal` (kPa) · `bar` (bar) · `atmosphere` (atm) · `psi` (psi) · `mmHg` (mmHg).

```
iconverter://tool/pressure?v=1&from=atmosphere&to=kilopascal
```

```
iconverter://tool/pressure?v=120&from=mmHg&to=kilopascal
```

**Energy**
Units: `joule` (J) · `kilojoule` (kJ) · `calorie` (cal) · `kilocalorie` (kcal) · `kilowattHour` (kWh) · `btu` (BTU).

```
iconverter://tool/energy?v=1&from=kilowattHour&to=kilojoule
```

```
iconverter://tool/energy?v=500&from=kilocalorie&to=kilojoule
```

**Power**
Units: `watt` (W) · `kilowatt` (kW) · `hpMechanical` (hp) · `hpMetric` (PS) · `btuPerHour` (BTU/h).

```
iconverter://tool/power?v=1&from=hpMechanical&to=kilowatt
```

```
iconverter://tool/power?v=3000&from=watt&to=hpMetric
```

**Force**
Units: `newton` (N) · `kilonewton` (kN) · `kgf` (kgf) · `lbf` (lbf) · `dyne` (dyn).

```
iconverter://tool/force?v=9.8&from=newton&to=kgf
```

```
iconverter://tool/force?v=1&from=kilonewton&to=lbf
```

**Torque**
Units: `newtonMeter` (N·m) · `newtonCentimeter` (N·cm) · `kgfMeter` (kgf·m) · `footPound` (ft·lb) · `inchPound` (in·lb).

```
iconverter://tool/torque?v=100&from=newtonMeter&to=footPound
```

**Frequency**
Units: `hertz` (Hz) · `kilohertz` (kHz) · `megahertz` (MHz) · `gigahertz` (GHz) · `terahertz` (THz) · `rpm` (rpm).

```
iconverter://tool/frequency?v=2.4&from=gigahertz&to=megahertz
```

```
iconverter://tool/frequency?v=3000&from=rpm&to=hertz
```

**Angle**
Units: `degree` (°) · `radian` (rad) · `gradian` (grad) · `arcminute` (') · `arcsecond` (") · `turn` (turn).

```
iconverter://tool/angle?v=180&from=degree&to=radian
```

```
iconverter://tool/angle?v=1&from=turn&to=degree
```

**Data Storage**
Units: `byte` (B) · `kilobyte` (KB) · `megabyte` (MB) · `gigabyte` (GB) · `terabyte` (TB) · `kibibyte` (KiB) · `mebibyte` (MiB) · `gibibyte` (GiB).

```
iconverter://tool/dataStorage?v=1&from=gigabyte&to=mebibyte
```

```
iconverter://tool/dataStorage?v=512&from=mebibyte&to=gigabyte
```

**Data Rate**
Units: `bps` (bps) · `kbps` (Kbps) · `mbps` (Mbps) · `gbps` (Gbps) · `kBps` (KB/s) · `mBps` (MB/s) · `gBps` (GB/s).

```
iconverter://tool/dataRate?v=100&from=mbps&to=mBps
```

```
iconverter://tool/dataRate?v=1&from=gbps&to=mbps
```

**Illuminance**
Units: `lux` (lx) · `footCandle` (fc) · `phot` (ph) · `nox` (nx).

```
iconverter://tool/illuminance?v=500&from=lux&to=footCandle
```

**Magnetic Flux Density**
Units: `tesla` (T) · `millitesla` (mT) · `microtesla` (μT) · `gauss` (G) · `milligauss` (mG).

```
iconverter://tool/magneticFlux?v=1&from=tesla&to=gauss
```

**Radioactivity**
Units: `becquerel` (Bq) · `kilobecquerel` (kBq) · `megabecquerel` (MBq) · `curie` (Ci) · `millicurie` (mCi) · `microcurie` (μCi).

```
iconverter://tool/radioactivity?v=1&from=curie&to=megabecquerel
```

**Viscosity**
Units: `pascalSecond` (Pa·s) · `millipascalSecond` (mPa·s) · `poise` (P) · `centipoise` (cP).

```
iconverter://tool/viscosity?v=1&from=pascalSecond&to=centipoise
```

**Fuel Economy**
Units: `lPer100km` (L/100km) · `kmPerL` (km/L) · `mpgUS` (MPG US) · `mpgUK` (MPG UK).

```
iconverter://tool/fuelEconomy?v=8.5&from=lPer100km&to=kmPerL
```

```
iconverter://tool/fuelEconomy?v=30&from=mpgUS&to=lPer100km
```

**Flow Rate**
Units: `cubicMeterPerSecond` (m³/s) · `cubicMeterPerHour` (m³/h) · `literPerSecond` (L/s) · `literPerMinute` (L/min) · `literPerHour` (L/h) · `usGallonPerMinute` (gpm US) · `cubicFootPerMinute` (cfm).

```
iconverter://tool/flowRate?v=1&from=literPerMinute&to=cubicMeterPerHour
```

**Density**
Units: `kgPerCubicMeter` (kg/m³) · `gramPerCubicCentimeter` (g/cm³) · `gramPerLiter` (g/L) · `kgPerLiter` (kg/L) · `poundPerCubicFoot` (lb/ft³).

```
iconverter://tool/density?v=1&from=gramPerCubicCentimeter&to=kgPerCubicMeter
```

**Magnetic Flux (Wb)**
Units: `weber` (Wb) · `milliweber` (mWb) · `microweber` (μWb) · `kiloweber` (kWb) · `maxwell` (Mx).

```
iconverter://tool/magneticFluxTrue?v=1&from=weber&to=maxwell
```

**Absorbed Dose**
Units: `gray` (Gy) · `milligray` (mGy) · `microgray` (μGy) · `kilogray` (kGy) · `rad` (rad) · `millirad` (mrad).

```
iconverter://tool/absorbedDose?v=1&from=gray&to=rad
```

**Equivalent Dose**
Units: `sievert` (Sv) · `millisievert` (mSv) · `microsievert` (μSv) · `rem` (rem) · `millirem` (mrem).

```
iconverter://tool/equivalentDose?v=1&from=sievert&to=rem
```

```
iconverter://tool/equivalentDose?v=20&from=millisievert&to=microsievert
```

**Amount of Substance**
Units: `mole` (mol) · `millimole` (mmol) · `micromole` (μmol) · `kilomole` (kmol) · `nanomole` (nmol) · `picomole` (pmol).

```
iconverter://tool/amountOfSubstance?v=1&from=mole&to=millimole
```

```
iconverter://tool/amountOfSubstance?v=150&from=millimole&to=micromole
```

---

[Back to iConverter Support](../) &middot; [FAQ](../faq) &middot; [Privacy Policy](../privacy)

</section>
<section lang="zh-CN" markdown="1">

爱计算（iConverter）支持 `iconverter://` URL Scheme 深度链接——可从其他应用、网页、二维码（QR Code 工具内 **生成或扫描**）、Safari 或苹果快捷指令打开全部 101 个工具，并通过查询参数预填输入框。

> **小组件配置：** iOS 添加/编辑小组件时的工具选择器跟随 **设备系统语言**。**设置 → 语言** 中的 App 内语言不会改变小组件配置界面。

## 协议规范

```
iconverter://tool/<ToolItem.rawValue>?key=value&key2=value2
```

- `<ToolItem.rawValue>` 与小组件深度链接共用同一套命名。
- 参数键名支持短键与同义别名二选一，例如 `text` 与 `input` 等效。
- 布尔参数：`1/true/yes/on` → true；`0/false/no/off` → false。
- 日期参数：支持 `yyyy-MM-dd`、ISO8601、Unix 时间戳（秒）。
- 单位换算通用：`v` = 数值，`from` = 源单位（rawValue 或 symbol，大小写不敏感），`to` = 目标单位。

---

## 1. 计算器

**标准计算器** — 仅打开

```
iconverter://tool/calculator
```

**科学计算器** — 仅打开

```
iconverter://tool/scientific
```

**程序员计算器** — 仅打开

```
iconverter://tool/programmer
```

---

## 2. 财务

**房贷计算器**
`p` = 贷款金额，`r` = 年利率 %，`y` = 年数，`mode` = 还款方式 0 = 等额本息 / 1 = 等额本金。

```
iconverter://tool/mortgage?p=1000000&r=3.7&y=30&mode=0
```

**个人所得税**
`salary` = 月工资，`insurance` = 社保公积金，`deduction` = 专项扣除，`threshold` = 起征点，`bonus` = 年终奖。

```
iconverter://tool/incomeTax?salary=20000&insurance=3000&deduction=1000&threshold=5000&bonus=50000
```

**复利计算**
`p` = 本金，`m` = 月定投，`r` = 年利率 %，`y` = 年数，`freq` = 复利频率 0 = 年 / 1 = 月 / 2 = 日，`i` = 通胀率 %。

```
iconverter://tool/compoundInterest?p=100000&m=1000&r=7&y=10&freq=1
```

**折扣计算**
`mode` = 模式 0–4，`p` = 原价，`r` = 折扣率，`t` = 满减门槛，`u` = 减免金额。

```
iconverter://tool/discount?mode=0&p=299&r=8.5
```

满减示例：

```
iconverter://tool/discount?mode=3&p=350&t=300&u=50
```

**小费 / AA**
`mode` = 0 = 小费 / 1 = AA，`bill` = 账单，`tip` = 小费 %，`tax` = 税率 %，`ppl` = 人数。

```
iconverter://tool/tipAA?mode=0&bill=200&tip=15&tax=0&ppl=4
```

**提前还款**
`p` = 原贷款额，`r` = 年利率 %，`total` = 总期数（年），`paid` = 已还期数，`prepay` = 提前还款额，`mode` = 方案 0 = 缩期 / 1 = 减月供 / 2 = 对比。

```
iconverter://tool/mortgagePrepay?p=800000&r=3.7&total=30&paid=5&prepay=100000&mode=2
```

**二手房税费** — 仅打开

```
iconverter://tool/realEstateTax
```

---

## 3. 日期时间

**年龄 / 纪念日**
`birth` = 生日 `yyyy-MM-dd`，`ref` = 参考日期。

```
iconverter://tool/ageAnniversary?birth=1990-05-01&ref=2026-05-17
```

**日期计算**
`mode` = 0 = 日期加减 / 1 = 两日期差。

加减模式（`d1` = 起始日期，`d` = ± 天数，`w` = ± 周，`mo` = ± 月，`y` = ± 年）：

```
iconverter://tool/dateArithmetic?mode=0&d1=2026-05-17&d=100
```

差值模式（`d1` = 日期 1，`d2` = 日期 2）：

```
iconverter://tool/dateArithmetic?mode=1&d1=2026-01-01&d2=2026-12-31
```

**农历查询**
`date` = 公历日期 `yyyy-MM-dd`。

```
iconverter://tool/lunarCalendar?date=2026-05-17
```

**节气** — 仅打开

```
iconverter://tool/solarTerms
```

**倒计时**
`label` = 事件名，`target` = 目标日期 `yyyy-MM-dd`，`time` = 含时分 `0/1`。

```
iconverter://tool/countdown?label=Holiday&target=2026-10-01&time=0
```

**孕期计算**
`method` = 方式 0 = 末次月经 / 1 = 受孕日 / 2 = IVF，`ref` = 日期，`ivf` = IVF 胚胎天数 0 = D3 / 1 = D5。

```
iconverter://tool/pregnancy?method=0&ref=2026-03-01
```

```
iconverter://tool/pregnancy?method=2&ref=2026-03-15&ivf=1
```

**月经周期**
`lmp` = 末次月经日期，`cycle` = 周期天数，`period` = 行经天数。

```
iconverter://tool/menstrual?lmp=2026-05-01&cycle=28&period=5
```

**世界时钟**
`q` = 城市搜索关键词，`now` = 使用当前时间 `0/1`，`ref` = 自定义时间。

```
iconverter://tool/worldClock?q=Tokyo
```

```
iconverter://tool/worldClock?now=0&ref=2026-05-17T20:00:00
```

**星座** — 仅打开

```
iconverter://tool/zodiac
```

---

## 4. 数学

**百分比计算**
`mode` = 模式 0–4，`a` = 数值 A，`b` = 数值 B。

```
iconverter://tool/percentage?mode=0&a=75&b=120
```

**分数计算** — 仅打开

```
iconverter://tool/fraction
```

**质因数分解** — 仅打开

```
iconverter://tool/primeFactor
```

**一元二次方程** — 仅打开

```
iconverter://tool/quadraticSolver
```

**统计计算**
`data` = 数据集，空格 / 逗号 / 分号分隔。

```
iconverter://tool/statistics?data=1,2,3,4,5,6,7,8,9,10
```

**排列组合** — 仅打开

```
iconverter://tool/combinations
```

**几何计算**
`shape` = 形状，`v1` / `v2` / `v3` = 各边参数。

可选形状：`rectangle` · `square` · `circle` · `triangle` · `triangleSSS` · `parallelogram` · `trapezoid` · `sector` · `ellipse` · `regularPolygon` · `sphere` · `hemisphere` · `cylinder` · `cone` · `frustum` · `cube` · `cuboid`。

圆形（`v1` = 半径）：

```
iconverter://tool/geometry?shape=circle&v1=5
```

矩形（`v1` = 长，`v2` = 宽）：

```
iconverter://tool/geometry?shape=rectangle&v1=10&v2=5
```

球体（`v1` = 半径）：

```
iconverter://tool/geometry?shape=sphere&v1=3
```

圆柱（`v1` = 半径，`v2` = 高）：

```
iconverter://tool/geometry?shape=cylinder&v1=4&v2=10
```

---

## 5. 编码

**罗马数字**
`n` = 阿拉伯数字（1–3999）；或 `roman` = 罗马数字字符串。

```
iconverter://tool/roman?n=2026
```

```
iconverter://tool/roman?roman=MMXXVI
```

**Base64 编解码**
`mode` = encode/decode，`urlSafe` = URL 安全模式 `0/1`，`text` = 输入文本。

```
iconverter://tool/base64?mode=encode&text=Hello%2C+World!
```

```
iconverter://tool/base64?mode=decode&urlSafe=0&text=SGVsbG8sIFdvcmxkIQ%3D%3D
```

**URL 编解码**
`mode` = encode/decode，`comp` = 组件模式 0 = 全部 / 1 = 查询参数 / 2 = 路径，`text` = 输入。

```
iconverter://tool/urlCoder?mode=encode&comp=0&text=https://example.com/path?q=hello world
```

```
iconverter://tool/urlCoder?mode=decode&text=https%3A%2F%2Fexample.com%2F%3Fq%3Dhello%20world
```

**哈希计算**
`text` = 输入文本，`algo` = 算法 md5/sha1/sha256/sha512，`upper` = 大写输出 `0/1`，`hmac` = 启用 HMAC `0/1`，`key` = HMAC 密钥。

```
iconverter://tool/hashing?text=Hello+World&algo=sha256&upper=0
```

```
iconverter://tool/hashing?text=data&algo=md5&hmac=1&key=secret
```

**字数统计**
`text` = 待统计文本。

```
iconverter://tool/wordCount?text=The+quick+brown+fox+jumps+over+the+lazy+dog.
```

**颜色换算**
`hex` = 十六进制颜色；或 `r` / `g` / `b` = RGB 分量（0–255）。

```
iconverter://tool/colorConverter?hex=%23FF8800
```

```
iconverter://tool/colorConverter?r=255&g=136&b=0
```

**色板** — 仅打开

```
iconverter://tool/colorPalette
```

**二维码**
`text` = 内容，`format` = 格式 `qr/aztec/code128/pdf417` 等，`ecc` = 纠错级别 `L/M/Q/H`。

```
iconverter://tool/qrcode?text=https%3A%2F%2Fexample.com&ecc=H
```

```
iconverter://tool/qrcode?text=Hello+iConverter&format=qr&ecc=M
```

**JSON 格式化**
`text` = JSON 字符串（需 URL 编码），`indent` = 缩进空格数 2/4。

```
iconverter://tool/jsonFormatter?text=%7B%22name%22%3A%22Alice%22%2C%22age%22%3A30%7D&indent=2
```

**时间戳**
`ts` = Unix 时间戳（秒），`u` = 单位 0 = 秒 / 1 = 毫秒；或 `iso` = ISO8601 日期字符串。

```
iconverter://tool/timestamp?ts=1747440000
```

```
iconverter://tool/timestamp?iso=2026-05-17T12:00:00
```

**银行卡号**
`num` = 银行卡号。

```
iconverter://tool/bankCard?num=6214830172816734
```

**文本大小写**
`text` = 输入文本。

```
iconverter://tool/textCase?text=hello+world+from+iConverter
```

**文本对比** — 仅打开

```
iconverter://tool/textDiff
```

**HTTP 请求**
`url` = 请求 URL，`method` = GET/POST/PUT/PATCH/DELETE，`body` = 请求体，`bodyKind` = body 类型 `json/form/text`，`headers` = 请求头 JSON。

```
iconverter://tool/httpRequest?url=https%3A%2F%2Fapi.example.com%2Fusers&method=GET
```

```
iconverter://tool/httpRequest?url=https%3A%2F%2Fapi.example.com%2Fusers&method=POST&body=%7B%22name%22%3A%22Alice%22%7D&bodyKind=json
```

**文件下载**
`url` = 下载链接，`name` = 保存文件名（可选）。

```
iconverter://tool/fileDownload?url=https%3A%2F%2Fexample.com%2Freport.pdf&name=report.pdf
```

**HTTP 状态码**
`code` = 状态码；或 `q` = 搜索关键词。

```
iconverter://tool/httpStatusCodes?code=404
```

```
iconverter://tool/httpStatusCodes?q=redirect
```

**IP 工具**
`mode` = subnet/cidr/range，`ip` = IP 地址，`mask` = 子网掩码；或 `prefix` = CIDR 前缀长度。

```
iconverter://tool/ipUtility?mode=subnet&ip=192.168.1.0&mask=255.255.255.0
```

```
iconverter://tool/ipUtility?ip=10.0.0.0&prefix=24
```

**ASCII 码表**
`dec` = 十进制码点；或 `hex` = 十六进制；或 `q` = 搜索。

```
iconverter://tool/asciiTable?dec=65
```

```
iconverter://tool/asciiTable?q=space
```

**密码生成器**
`length` = 长度，`upper` = 大写 `0/1`，`lower` = 小写 `0/1`，`digits` = 数字 `0/1`，`symbols` = 符号 `0/1`，`unambiguous` = 排除歧义字符 `0/1`，`go` = 立即生成 `1`。

```
iconverter://tool/passwordGenerator?length=20&upper=1&lower=1&digits=1&symbols=1&unambiguous=1&go=1
```

**随机数生成**
`min` = 最小值，`max` = 最大值，`n` = 数量，`decimals` = 小数位，`unique` = 不重复 `0/1`，`sort` = 排序 0 = 不排 / 1 = 升序 / 2 = 降序，`go` = 立即生成 `1`。

```
iconverter://tool/randomNumber?min=1&max=100&n=10&unique=1&sort=1&go=1
```

```
iconverter://tool/randomNumber?min=0&max=1&n=5&decimals=4&go=1
```

**摩斯电码**
`mode` = encode/decode，`text` = 输入文本。

```
iconverter://tool/morseCode?mode=encode&text=SOS
```

```
iconverter://tool/morseCode?mode=decode&text=...+---+...
```

**JWT 解码**
`token` = JWT 令牌字符串。

```
iconverter://tool/jwtParser?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c
```

**Cron 表达式**
`expr` = Cron 表达式（空格可用 `+` 代替）。

```
iconverter://tool/cronParser?expr=0+9+*+*+1-5
```

```
iconverter://tool/cronParser?expr=0+0+*+*+*
```

**正则测试**
`pattern` = 正则表达式（需 URL 编码），`haystack` = 测试文本，`replacement` = 替换内容，`i` = 忽略大小写 `0/1`，`m` = 多行 `0/1`，`s` = 点匹配换行 `0/1`。

```
iconverter://tool/regexTester?pattern=%5Cd%2B&haystack=abc123def456&i=0
```

```
iconverter://tool/regexTester?pattern=%28%5Cw%2B%29&haystack=hello+world&replacement=%5B%241%5D&i=1
```

**网页工具**
`url` = 直接打开 URL；或 `q` = 搜索关键词（使用默认搜索引擎）。

```
iconverter://tool/webBrowser?url=https%3A%2F%2Fexample.com
```

```
iconverter://tool/webBrowser?q=SwiftUI+deep+link+2026
```

---

## 6. 生活

**BMI 计算**
`h` = 身高 cm，`w` = 体重 kg，`std` = 标准 0 = 中国成人 / 1 = WHO。

```
iconverter://tool/bmi?h=175&w=70&std=0
```

**基础代谢率**
`h` = 身高 cm，`w` = 体重 kg，`age` = 年龄，`sex` = 性别 m = 男 / f = 女，`act` = 活动指数 0–4，`formula` = 公式 0 = Harris-Benedict / 1 = Mifflin-St Jeor。

```
iconverter://tool/bmr?h=175&w=70&age=30&sex=m&act=1&formula=1
```

**服装尺码** — 仅打开

```
iconverter://tool/clothingSize
```

**戒指尺码** — 仅打开

```
iconverter://tool/ringSize
```

**身高换算** — 仅打开

```
iconverter://tool/heightConverter
```

**油费计算**
`unit` = 单位 0 = 公制 / 1 = 英制，`d` = 行驶距离，`c` = 百公里油耗,`p` = 油价，`n` = 人数。

```
iconverter://tool/fuelCost?unit=0&d=500&c=8.5&p=7.8&n=1
```

**运费计算**
`w` = 实重 kg，`fw` = 首重 kg，`ff` = 首重费用，`sw` = 续重步长 kg，`sf` = 续重费用。

```
iconverter://tool/shippingFee?w=3.5&fw=1&ff=12&sw=1&sf=8
```

含体积重（`vol` = 启用 `0/1`，`l` / `wd` / `h` = 三边 cm，`div` = 抛比）：

```
iconverter://tool/shippingFee?w=2&vol=1&l=50&wd=40&h=30&div=6000&fw=1&ff=12&sw=1&sf=8
```

**酒精血液浓度**
`sex` = 性别 m = 男 / f = 女，`w` = 体重 kg，`v` = 饮酒量 mL，`abv` = 酒精度 %，`h` = 饮酒后小时数。

```
iconverter://tool/alcoholBac?sex=m&w=70&v=500&abv=5&h=0.5
```

**亲戚称呼**
`chain` = 关系链逗号分隔，`sex` = 本人性别 0 = 男 / 1 = 女，`reverse` = 显示互称 `0/1`。

```
iconverter://tool/relationship?chain=f,os&sex=0&reverse=1
```

```
iconverter://tool/relationship?chain=m,ob&sex=1&reverse=0
```

**身份证查询**
`id` = 身份证号码。

```
iconverter://tool/idCard?id=110101199003073010
```

**抛硬币** — 仅打开

```
iconverter://tool/coinFlip
```

**骰子模拟** — 仅打开

```
iconverter://tool/diceRoller
```

**随机抽签** — 仅打开

```
iconverter://tool/randomDraw
```

**转盘抽奖** — 仅打开

```
iconverter://tool/spinWheel
```

**视频关键帧** — 仅打开

```
iconverter://tool/videoFrameExport
```

---

## 7. 传感器

**指南针** — 仅打开

```
iconverter://tool/compass
```

**水平仪** — 仅打开

```
iconverter://tool/level
```

**海拔仪** — 仅打开

```
iconverter://tool/altitude
```

---

## 8. 中文

**大写数字**
`n` = 阿拉伯数字。

```
iconverter://tool/chineseNumber?n=12345.67
```

**汉字数字反查**
`text` = 汉字数字字符串。

```
iconverter://tool/chineseNumberReverse?text=一万二千三百四十五
```

**金额大写**
`amount` = 金额，`zheng` = 末尾「整」`0/1`。

```
iconverter://tool/financialAmount?amount=12345.67&zheng=1
```

---

## 9. 单位换算

通用格式：`v` = 数值，`from` = 源单位（rawValue 或 symbol，大小写不敏感），`to` = 目标单位。

---

**长度**
常用单位：`meter`(m) · `kilometer`(km) · `centimeter`(cm) · `millimeter`(mm) · `foot`(ft) · `inch`(in) · `mile`(mi) · `yard`(yd) · `nauticalMile`(nmi) · `chineseLi`(里) · `chineseChi`(尺)。

```
iconverter://tool/length?v=100&from=meter&to=foot
```

```
iconverter://tool/length?v=1&from=mile&to=kilometer
```

**面积**
常用单位：`squareMeter`(m²) · `hectare`(ha) · `acre`(acre) · `squareFoot`(ft²) · `squareMile`(mile²) · `mu`(亩) · `squareKilometer`(km²)。

```
iconverter://tool/area?v=1&from=hectare&to=mu
```

```
iconverter://tool/area?v=1&from=acre&to=squareMeter
```

**体积**
常用单位：`liter`(L) · `milliliter`(mL) · `cubicMeter`(m³) · `gallon`(gal) · `fluidOunce`(fl oz) · `cup`(cup) · `ukGallon`(gal UK) · `oilBarrel`(bbl)。

```
iconverter://tool/volume?v=1&from=gallon&to=liter
```

```
iconverter://tool/volume?v=355&from=milliliter&to=fluidOunce
```

**重量 / 质量**
常用单位：`kilogram`(kg) · `gram`(g) · `pound`(lb) · `ounce`(oz) · `tonne`(t) · `jin`(斤) · `liang`(两) · `carat`(ct)。

```
iconverter://tool/weight?v=1&from=pound&to=kilogram
```

```
iconverter://tool/weight?v=1&from=jin&to=gram
```

**温度**
单位：`celsius`(°C) · `fahrenheit`(°F) · `kelvin`(K) · `rankine`(°R) · `reaumur`(°Re)。

```
iconverter://tool/temperature?v=100&from=celsius&to=fahrenheit
```

```
iconverter://tool/temperature?v=37&from=celsius&to=kelvin
```

**时间**
常用单位：`second`(s) · `minute`(min) · `hour`(h) · `day`(day) · `week`(wk) · `month`(mo) · `year`(yr) · `millisecond`(ms) · `microsecond`(μs)。

```
iconverter://tool/time?v=1&from=hour&to=second
```

```
iconverter://tool/time?v=7&from=day&to=hour
```

**速度**
单位：`meterPerSecond`(m/s) · `kmPerHour`(km/h) · `milePerHour`(mph) · `knot`(kn) · `mach`(Ma)。

```
iconverter://tool/speed?v=100&from=kmPerHour&to=milePerHour
```

```
iconverter://tool/speed?v=1&from=mach&to=meterPerSecond
```

**压强**
单位：`pascal`(Pa) · `kilopascal`(kPa) · `bar`(bar) · `atmosphere`(atm) · `psi`(psi) · `mmHg`(mmHg)。

```
iconverter://tool/pressure?v=1&from=atmosphere&to=kilopascal
```

```
iconverter://tool/pressure?v=120&from=mmHg&to=kilopascal
```

**能量**
单位：`joule`(J) · `kilojoule`(kJ) · `calorie`(cal) · `kilocalorie`(kcal) · `kilowattHour`(kWh) · `btu`(BTU)。

```
iconverter://tool/energy?v=1&from=kilowattHour&to=kilojoule
```

```
iconverter://tool/energy?v=500&from=kilocalorie&to=kilojoule
```

**功率**
单位：`watt`(W) · `kilowatt`(kW) · `hpMechanical`(hp) · `hpMetric`(PS) · `btuPerHour`(BTU/h)。

```
iconverter://tool/power?v=1&from=hpMechanical&to=kilowatt
```

```
iconverter://tool/power?v=3000&from=watt&to=hpMetric
```

**力**
单位：`newton`(N) · `kilonewton`(kN) · `kgf`(kgf) · `lbf`(lbf) · `dyne`(dyn)。

```
iconverter://tool/force?v=9.8&from=newton&to=kgf
```

```
iconverter://tool/force?v=1&from=kilonewton&to=lbf
```

**扭矩**
单位：`newtonMeter`(N·m) · `newtonCentimeter`(N·cm) · `kgfMeter`(kgf·m) · `footPound`(ft·lb) · `inchPound`(in·lb)。

```
iconverter://tool/torque?v=100&from=newtonMeter&to=footPound
```

**频率**
单位：`hertz`(Hz) · `kilohertz`(kHz) · `megahertz`(MHz) · `gigahertz`(GHz) · `terahertz`(THz) · `rpm`(rpm)。

```
iconverter://tool/frequency?v=2.4&from=gigahertz&to=megahertz
```

```
iconverter://tool/frequency?v=3000&from=rpm&to=hertz
```

**角度**
单位：`degree`(°) · `radian`(rad) · `gradian`(grad) · `arcminute`(') · `arcsecond`(") · `turn`(turn)。

```
iconverter://tool/angle?v=180&from=degree&to=radian
```

```
iconverter://tool/angle?v=1&from=turn&to=degree
```

**数据存储**
单位：`byte`(B) · `kilobyte`(KB) · `megabyte`(MB) · `gigabyte`(GB) · `terabyte`(TB) · `kibibyte`(KiB) · `mebibyte`(MiB) · `gibibyte`(GiB)。

```
iconverter://tool/dataStorage?v=1&from=gigabyte&to=mebibyte
```

```
iconverter://tool/dataStorage?v=512&from=mebibyte&to=gigabyte
```

**数据速率**
单位：`bps`(bps) · `kbps`(Kbps) · `mbps`(Mbps) · `gbps`(Gbps) · `kBps`(KB/s) · `mBps`(MB/s) · `gBps`(GB/s)。

```
iconverter://tool/dataRate?v=100&from=mbps&to=mBps
```

```
iconverter://tool/dataRate?v=1&from=gbps&to=mbps
```

**光照强度**
单位：`lux`(lx) · `footCandle`(fc) · `phot`(ph) · `nox`(nx)。

```
iconverter://tool/illuminance?v=500&from=lux&to=footCandle
```

**磁感应强度**
单位：`tesla`(T) · `millitesla`(mT) · `microtesla`(μT) · `gauss`(G) · `milligauss`(mG)。

```
iconverter://tool/magneticFlux?v=1&from=tesla&to=gauss
```

**放射性活度**
单位：`becquerel`(Bq) · `kilobecquerel`(kBq) · `megabecquerel`(MBq) · `curie`(Ci) · `millicurie`(mCi) · `microcurie`(μCi)。

```
iconverter://tool/radioactivity?v=1&from=curie&to=megabecquerel
```

**黏度**
单位：`pascalSecond`(Pa·s) · `millipascalSecond`(mPa·s) · `poise`(P) · `centipoise`(cP)。

```
iconverter://tool/viscosity?v=1&from=pascalSecond&to=centipoise
```

**燃油经济性**
单位：`lPer100km`(L/100km) · `kmPerL`(km/L) · `mpgUS`(MPG US) · `mpgUK`(MPG UK)。

```
iconverter://tool/fuelEconomy?v=8.5&from=lPer100km&to=kmPerL
```

```
iconverter://tool/fuelEconomy?v=30&from=mpgUS&to=lPer100km
```

**流量**
单位：`cubicMeterPerSecond`(m³/s) · `cubicMeterPerHour`(m³/h) · `literPerSecond`(L/s) · `literPerMinute`(L/min) · `literPerHour`(L/h) · `usGallonPerMinute`(gpm US) · `cubicFootPerMinute`(cfm)。

```
iconverter://tool/flowRate?v=1&from=literPerMinute&to=cubicMeterPerHour
```

**密度**
单位：`kgPerCubicMeter`(kg/m³) · `gramPerCubicCentimeter`(g/cm³) · `gramPerLiter`(g/L) · `kgPerLiter`(kg/L) · `poundPerCubicFoot`(lb/ft³)。

```
iconverter://tool/density?v=1&from=gramPerCubicCentimeter&to=kgPerCubicMeter
```

**磁通量**
单位：`weber`(Wb) · `milliweber`(mWb) · `microweber`(μWb) · `kiloweber`(kWb) · `maxwell`(Mx)。

```
iconverter://tool/magneticFluxTrue?v=1&from=weber&to=maxwell
```

**吸收剂量**
单位：`gray`(Gy) · `milligray`(mGy) · `microgray`(μGy) · `kilogray`(kGy) · `rad`(rad) · `millirad`(mrad)。

```
iconverter://tool/absorbedDose?v=1&from=gray&to=rad
```

**等效剂量**
单位：`sievert`(Sv) · `millisievert`(mSv) · `microsievert`(μSv) · `rem`(rem) · `millirem`(mrem)。

```
iconverter://tool/equivalentDose?v=1&from=sievert&to=rem
```

```
iconverter://tool/equivalentDose?v=20&from=millisievert&to=microsievert
```

**物质的量**
单位：`mole`(mol) · `millimole`(mmol) · `micromole`(μmol) · `kilomole`(kmol) · `nanomole`(nmol) · `picomole`(pmol)。

```
iconverter://tool/amountOfSubstance?v=1&from=mole&to=millimole
```

```
iconverter://tool/amountOfSubstance?v=150&from=millimole&to=micromole
```

---

[返回 iConverter 支持页](../) &middot; [常见问题](../faq) &middot; [隐私政策](../privacy)

</section>
<section lang="zh-TW" markdown="1">

愛計算（iConverter）支援 `iconverter://` URL Scheme 深度連結——可從其他應用、網頁、QR Code（QR Code 工具內 **產生或掃描**）、Safari 或 Apple 捷徑開啟全部 101 個工具，並透過查詢參數預填輸入框。

> **小工具設定：** iOS 新增/編輯小工具時的工具選擇器跟隨 **裝置系統語言**。**設定 → 語言** 中的 App 內語言不會改變小工具設定介面。

## 協議規範

```
iconverter://tool/<ToolItem.rawValue>?key=value&key2=value2
```

- `<ToolItem.rawValue>` 與小工具深度連結共用同一套命名。
- 參數鍵名支援短鍵與同義別名二選一，例如 `text` 與 `input` 等效。
- 布林參數：`1/true/yes/on` → true；`0/false/no/off` → false。
- 日期參數：支援 `yyyy-MM-dd`、ISO8601、Unix 時間戳（秒）。
- 單位換算通用：`v` = 數值，`from` = 來源單位（rawValue 或 symbol，大小寫不敏感），`to` = 目標單位。

---

## 1. 計算器

**標準計算器** — 僅開啟

```
iconverter://tool/calculator
```

**科學計算器** — 僅開啟

```
iconverter://tool/scientific
```

**程式設計師計算器** — 僅開啟

```
iconverter://tool/programmer
```

---

## 2. 財務

**房貸計算器**
`p` = 貸款金額，`r` = 年利率 %，`y` = 年數，`mode` = 還款方式 0 = 等額本息 / 1 = 等額本金。

```
iconverter://tool/mortgage?p=1000000&r=3.7&y=30&mode=0
```

**個人所得稅**
`salary` = 月薪，`insurance` = 社保公積金，`deduction` = 專項扣除，`threshold` = 起徵點，`bonus` = 年終獎。

```
iconverter://tool/incomeTax?salary=20000&insurance=3000&deduction=1000&threshold=5000&bonus=50000
```

**複利計算**
`p` = 本金，`m` = 月定投，`r` = 年利率 %，`y` = 年數，`freq` = 複利頻率 0 = 年 / 1 = 月 / 2 = 日,`i` = 通脹率 %。

```
iconverter://tool/compoundInterest?p=100000&m=1000&r=7&y=10&freq=1
```

**折扣計算**
`mode` = 模式 0–4，`p` = 原價，`r` = 折扣率，`t` = 滿減門檻,`u` = 減免金額。

```
iconverter://tool/discount?mode=0&p=299&r=8.5
```

滿減範例：

```
iconverter://tool/discount?mode=3&p=350&t=300&u=50
```

**小費 / AA**
`mode` = 0 = 小費 / 1 = AA，`bill` = 帳單，`tip` = 小費 %，`tax` = 稅率 %，`ppl` = 人數。

```
iconverter://tool/tipAA?mode=0&bill=200&tip=15&tax=0&ppl=4
```

**提前還款**
`p` = 原貸款額，`r` = 年利率 %，`total` = 總期數（年），`paid` = 已還期數，`prepay` = 提前還款額，`mode` = 方案 0 = 縮期 / 1 = 減月供 / 2 = 對比。

```
iconverter://tool/mortgagePrepay?p=800000&r=3.7&total=30&paid=5&prepay=100000&mode=2
```

**二手房稅費** — 僅開啟

```
iconverter://tool/realEstateTax
```

---

## 3. 日期時間

**年齡 / 紀念日**
`birth` = 生日 `yyyy-MM-dd`，`ref` = 參考日期。

```
iconverter://tool/ageAnniversary?birth=1990-05-01&ref=2026-05-17
```

**日期計算**
`mode` = 0 = 日期加減 / 1 = 兩日期差。

加減模式（`d1` = 起始日期，`d` = ± 天數，`w` = ± 週，`mo` = ± 月，`y` = ± 年）：

```
iconverter://tool/dateArithmetic?mode=0&d1=2026-05-17&d=100
```

差值模式（`d1` = 日期 1，`d2` = 日期 2）：

```
iconverter://tool/dateArithmetic?mode=1&d1=2026-01-01&d2=2026-12-31
```

**農曆查詢**
`date` = 公曆日期 `yyyy-MM-dd`。

```
iconverter://tool/lunarCalendar?date=2026-05-17
```

**節氣** — 僅開啟

```
iconverter://tool/solarTerms
```

**倒數日**
`label` = 事件名，`target` = 目標日期 `yyyy-MM-dd`，`time` = 含時分 `0/1`。

```
iconverter://tool/countdown?label=Holiday&target=2026-10-01&time=0
```

**孕期計算**
`method` = 方式 0 = 末次月經 / 1 = 受孕日 / 2 = IVF，`ref` = 日期,`ivf` = IVF 胚胎天數 0 = D3 / 1 = D5。

```
iconverter://tool/pregnancy?method=0&ref=2026-03-01
```

```
iconverter://tool/pregnancy?method=2&ref=2026-03-15&ivf=1
```

**月經週期**
`lmp` = 末次月經日期，`cycle` = 週期天數，`period` = 行經天數。

```
iconverter://tool/menstrual?lmp=2026-05-01&cycle=28&period=5
```

**世界時鐘**
`q` = 城市搜尋關鍵字，`now` = 使用目前時間 `0/1`，`ref` = 自訂時間。

```
iconverter://tool/worldClock?q=Tokyo
```

```
iconverter://tool/worldClock?now=0&ref=2026-05-17T20:00:00
```

**星座** — 僅開啟

```
iconverter://tool/zodiac
```

---

## 4. 數學

**百分比計算**
`mode` = 模式 0–4，`a` = 數值 A，`b` = 數值 B。

```
iconverter://tool/percentage?mode=0&a=75&b=120
```

**分數計算** — 僅開啟

```
iconverter://tool/fraction
```

**質因數分解** — 僅開啟

```
iconverter://tool/primeFactor
```

**一元二次方程** — 僅開啟

```
iconverter://tool/quadraticSolver
```

**統計計算**
`data` = 資料集，空格 / 逗號 / 分號分隔。

```
iconverter://tool/statistics?data=1,2,3,4,5,6,7,8,9,10
```

**排列組合** — 僅開啟

```
iconverter://tool/combinations
```

**幾何計算**
`shape` = 形狀，`v1` / `v2` / `v3` = 各邊參數。

可選形狀：`rectangle` · `square` · `circle` · `triangle` · `triangleSSS` · `parallelogram` · `trapezoid` · `sector` · `ellipse` · `regularPolygon` · `sphere` · `hemisphere` · `cylinder` · `cone` · `frustum` · `cube` · `cuboid`。

圓形（`v1` = 半徑）：

```
iconverter://tool/geometry?shape=circle&v1=5
```

矩形（`v1` = 長，`v2` = 寬）：

```
iconverter://tool/geometry?shape=rectangle&v1=10&v2=5
```

球體（`v1` = 半徑）：

```
iconverter://tool/geometry?shape=sphere&v1=3
```

圓柱（`v1` = 半徑，`v2` = 高）：

```
iconverter://tool/geometry?shape=cylinder&v1=4&v2=10
```

---

## 5. 編碼

**羅馬數字**
`n` = 阿拉伯數字（1–3999）；或 `roman` = 羅馬數字字串。

```
iconverter://tool/roman?n=2026
```

```
iconverter://tool/roman?roman=MMXXVI
```

**Base64 編解碼**
`mode` = encode/decode，`urlSafe` = URL 安全模式 `0/1`，`text` = 輸入文字。

```
iconverter://tool/base64?mode=encode&text=Hello%2C+World!
```

```
iconverter://tool/base64?mode=decode&urlSafe=0&text=SGVsbG8sIFdvcmxkIQ%3D%3D
```

**URL 編解碼**
`mode` = encode/decode，`comp` = 元件模式 0 = 全部 / 1 = 查詢參數 / 2 = 路徑，`text` = 輸入。

```
iconverter://tool/urlCoder?mode=encode&comp=0&text=https://example.com/path?q=hello world
```

```
iconverter://tool/urlCoder?mode=decode&text=https%3A%2F%2Fexample.com%2F%3Fq%3Dhello%20world
```

**雜湊計算**
`text` = 輸入文字，`algo` = 演算法 md5/sha1/sha256/sha512，`upper` = 大寫輸出 `0/1`，`hmac` = 啟用 HMAC `0/1`，`key` = HMAC 金鑰。

```
iconverter://tool/hashing?text=Hello+World&algo=sha256&upper=0
```

```
iconverter://tool/hashing?text=data&algo=md5&hmac=1&key=secret
```

**字數統計**
`text` = 待統計文字。

```
iconverter://tool/wordCount?text=The+quick+brown+fox+jumps+over+the+lazy+dog.
```

**顏色換算**
`hex` = 十六進制顏色；或 `r` / `g` / `b` = RGB 分量（0–255）。

```
iconverter://tool/colorConverter?hex=%23FF8800
```

```
iconverter://tool/colorConverter?r=255&g=136&b=0
```

**色板** — 僅開啟

```
iconverter://tool/colorPalette
```

**QR Code**
`text` = 內容，`format` = 格式 `qr/aztec/code128/pdf417` 等，`ecc` = 糾錯等級 `L/M/Q/H`。

```
iconverter://tool/qrcode?text=https%3A%2F%2Fexample.com&ecc=H
```

```
iconverter://tool/qrcode?text=Hello+iConverter&format=qr&ecc=M
```

**JSON 格式化**
`text` = JSON 字串（需 URL 編碼），`indent` = 縮排空格數 2/4。

```
iconverter://tool/jsonFormatter?text=%7B%22name%22%3A%22Alice%22%2C%22age%22%3A30%7D&indent=2
```

**時間戳**
`ts` = Unix 時間戳（秒），`u` = 單位 0 = 秒 / 1 = 毫秒；或 `iso` = ISO8601 日期字串。

```
iconverter://tool/timestamp?ts=1747440000
```

```
iconverter://tool/timestamp?iso=2026-05-17T12:00:00
```

**銀行卡號**
`num` = 銀行卡號。

```
iconverter://tool/bankCard?num=6214830172816734
```

**文字大小寫**
`text` = 輸入文字。

```
iconverter://tool/textCase?text=hello+world+from+iConverter
```

**文字比對** — 僅開啟

```
iconverter://tool/textDiff
```

**HTTP 請求**
`url` = 請求 URL，`method` = GET/POST/PUT/PATCH/DELETE，`body` = 請求體，`bodyKind` = body 類型 `json/form/text`，`headers` = 請求頭 JSON。

```
iconverter://tool/httpRequest?url=https%3A%2F%2Fapi.example.com%2Fusers&method=GET
```

```
iconverter://tool/httpRequest?url=https%3A%2F%2Fapi.example.com%2Fusers&method=POST&body=%7B%22name%22%3A%22Alice%22%7D&bodyKind=json
```

**檔案下載**
`url` = 下載連結，`name` = 儲存檔名（可選）。

```
iconverter://tool/fileDownload?url=https%3A%2F%2Fexample.com%2Freport.pdf&name=report.pdf
```

**HTTP 狀態碼**
`code` = 狀態碼；或 `q` = 搜尋關鍵字。

```
iconverter://tool/httpStatusCodes?code=404
```

```
iconverter://tool/httpStatusCodes?q=redirect
```

**IP 工具**
`mode` = subnet/cidr/range，`ip` = IP 位址，`mask` = 子網路遮罩；或 `prefix` = CIDR 前綴長度。

```
iconverter://tool/ipUtility?mode=subnet&ip=192.168.1.0&mask=255.255.255.0
```

```
iconverter://tool/ipUtility?ip=10.0.0.0&prefix=24
```

**ASCII 碼表**
`dec` = 十進制碼點；或 `hex` = 十六進制；或 `q` = 搜尋。

```
iconverter://tool/asciiTable?dec=65
```

```
iconverter://tool/asciiTable?q=space
```

**密碼產生器**
`length` = 長度，`upper` = 大寫 `0/1`，`lower` = 小寫 `0/1`，`digits` = 數字 `0/1`，`symbols` = 符號 `0/1`，`unambiguous` = 排除歧義字元 `0/1`，`go` = 立即產生 `1`。

```
iconverter://tool/passwordGenerator?length=20&upper=1&lower=1&digits=1&symbols=1&unambiguous=1&go=1
```

**亂數產生**
`min` = 最小值，`max` = 最大值，`n` = 數量，`decimals` = 小數位，`unique` = 不重複 `0/1`，`sort` = 排序 0 = 不排 / 1 = 升序 / 2 = 降序，`go` = 立即產生 `1`。

```
iconverter://tool/randomNumber?min=1&max=100&n=10&unique=1&sort=1&go=1
```

```
iconverter://tool/randomNumber?min=0&max=1&n=5&decimals=4&go=1
```

**摩斯電碼**
`mode` = encode/decode，`text` = 輸入文字。

```
iconverter://tool/morseCode?mode=encode&text=SOS
```

```
iconverter://tool/morseCode?mode=decode&text=...+---+...
```

**JWT 解碼**
`token` = JWT 令牌字串。

```
iconverter://tool/jwtParser?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c
```

**Cron 表達式**
`expr` = Cron 表達式（空格可用 `+` 代替）。

```
iconverter://tool/cronParser?expr=0+9+*+*+1-5
```

```
iconverter://tool/cronParser?expr=0+0+*+*+*
```

**正則測試**
`pattern` = 正則表達式（需 URL 編碼），`haystack` = 測試文字，`replacement` = 取代內容，`i` = 忽略大小寫 `0/1`，`m` = 多行 `0/1`，`s` = 點匹配換行 `0/1`。

```
iconverter://tool/regexTester?pattern=%5Cd%2B&haystack=abc123def456&i=0
```

```
iconverter://tool/regexTester?pattern=%28%5Cw%2B%29&haystack=hello+world&replacement=%5B%241%5D&i=1
```

**網頁工具**
`url` = 直接開啟 URL；或 `q` = 搜尋關鍵字（使用預設搜尋引擎）。

```
iconverter://tool/webBrowser?url=https%3A%2F%2Fexample.com
```

```
iconverter://tool/webBrowser?q=SwiftUI+deep+link+2026
```

---

## 6. 生活

**BMI 計算**
`h` = 身高 cm，`w` = 體重 kg，`std` = 標準 0 = 中國成人 / 1 = WHO。

```
iconverter://tool/bmi?h=175&w=70&std=0
```

**基礎代謝率**
`h` = 身高 cm，`w` = 體重 kg，`age` = 年齡，`sex` = 性別 m = 男 / f = 女，`act` = 活動指數 0–4，`formula` = 公式 0 = Harris-Benedict / 1 = Mifflin-St Jeor。

```
iconverter://tool/bmr?h=175&w=70&age=30&sex=m&act=1&formula=1
```

**服裝尺碼** — 僅開啟

```
iconverter://tool/clothingSize
```

**戒指尺碼** — 僅開啟

```
iconverter://tool/ringSize
```

**身高換算** — 僅開啟

```
iconverter://tool/heightConverter
```

**油費計算**
`unit` = 單位 0 = 公制 / 1 = 英制，`d` = 行駛距離，`c` = 每百公里油耗，`p` = 油價，`n` = 人數。

```
iconverter://tool/fuelCost?unit=0&d=500&c=8.5&p=7.8&n=1
```

**運費計算**
`w` = 實重 kg，`fw` = 首重 kg，`ff` = 首重費用，`sw` = 續重步長 kg，`sf` = 續重費用。

```
iconverter://tool/shippingFee?w=3.5&fw=1&ff=12&sw=1&sf=8
```

含體積重（`vol` = 啟用 `0/1`，`l` / `wd` / `h` = 三邊 cm，`div` = 拋比）：

```
iconverter://tool/shippingFee?w=2&vol=1&l=50&wd=40&h=30&div=6000&fw=1&ff=12&sw=1&sf=8
```

**酒精血液濃度**
`sex` = 性別 m = 男 / f = 女，`w` = 體重 kg，`v` = 飲酒量 mL，`abv` = 酒精度 %，`h` = 飲酒後小時數。

```
iconverter://tool/alcoholBac?sex=m&w=70&v=500&abv=5&h=0.5
```

**親戚稱呼**
`chain` = 關係鏈逗號分隔，`sex` = 本人性別 0 = 男 / 1 = 女，`reverse` = 顯示互稱 `0/1`。

```
iconverter://tool/relationship?chain=f,os&sex=0&reverse=1
```

```
iconverter://tool/relationship?chain=m,ob&sex=1&reverse=0
```

**身分證查詢**
`id` = 身分證號碼。

```
iconverter://tool/idCard?id=110101199003073010
```

**拋硬幣** — 僅開啟

```
iconverter://tool/coinFlip
```

**骰子模擬** — 僅開啟

```
iconverter://tool/diceRoller
```

**隨機抽籤** — 僅開啟

```
iconverter://tool/randomDraw
```

**轉盤抽獎** — 僅開啟

```
iconverter://tool/spinWheel
```

**影片關鍵幀** — 僅開啟

```
iconverter://tool/videoFrameExport
```

---

## 7. 感測器

**指南針** — 僅開啟

```
iconverter://tool/compass
```

**水平儀** — 僅開啟

```
iconverter://tool/level
```

**海拔儀** — 僅開啟

```
iconverter://tool/altitude
```

---

## 8. 中文

**大寫數字**
`n` = 阿拉伯數字。

```
iconverter://tool/chineseNumber?n=12345.67
```

**漢字數字反查**
`text` = 漢字數字字串。

```
iconverter://tool/chineseNumberReverse?text=一万二千三百四十五
```

**金額大寫**
`amount` = 金額，`zheng` = 末尾「整」`0/1`。

```
iconverter://tool/financialAmount?amount=12345.67&zheng=1
```

---

## 9. 單位換算

通用格式：`v` = 數值，`from` = 來源單位（rawValue 或 symbol，大小寫不敏感），`to` = 目標單位。

---

**長度**
常用單位：`meter`(m) · `kilometer`(km) · `centimeter`(cm) · `millimeter`(mm) · `foot`(ft) · `inch`(in) · `mile`(mi) · `yard`(yd) · `nauticalMile`(nmi) · `chineseLi`(里) · `chineseChi`(尺)。

```
iconverter://tool/length?v=100&from=meter&to=foot
```

```
iconverter://tool/length?v=1&from=mile&to=kilometer
```

**面積**
常用單位：`squareMeter`(m²) · `hectare`(ha) · `acre`(acre) · `squareFoot`(ft²) · `squareMile`(mile²) · `mu`(亩) · `squareKilometer`(km²)。

```
iconverter://tool/area?v=1&from=hectare&to=mu
```

```
iconverter://tool/area?v=1&from=acre&to=squareMeter
```

**體積**
常用單位：`liter`(L) · `milliliter`(mL) · `cubicMeter`(m³) · `gallon`(gal) · `fluidOunce`(fl oz) · `cup`(cup) · `ukGallon`(gal UK) · `oilBarrel`(bbl)。

```
iconverter://tool/volume?v=1&from=gallon&to=liter
```

```
iconverter://tool/volume?v=355&from=milliliter&to=fluidOunce
```

**重量 / 質量**
常用單位：`kilogram`(kg) · `gram`(g) · `pound`(lb) · `ounce`(oz) · `tonne`(t) · `jin`(斤) · `liang`(两) · `carat`(ct)。

```
iconverter://tool/weight?v=1&from=pound&to=kilogram
```

```
iconverter://tool/weight?v=1&from=jin&to=gram
```

**溫度**
單位：`celsius`(°C) · `fahrenheit`(°F) · `kelvin`(K) · `rankine`(°R) · `reaumur`(°Re)。

```
iconverter://tool/temperature?v=100&from=celsius&to=fahrenheit
```

```
iconverter://tool/temperature?v=37&from=celsius&to=kelvin
```

**時間**
常用單位：`second`(s) · `minute`(min) · `hour`(h) · `day`(day) · `week`(wk) · `month`(mo) · `year`(yr) · `millisecond`(ms) · `microsecond`(μs)。

```
iconverter://tool/time?v=1&from=hour&to=second
```

```
iconverter://tool/time?v=7&from=day&to=hour
```

**速度**
單位：`meterPerSecond`(m/s) · `kmPerHour`(km/h) · `milePerHour`(mph) · `knot`(kn) · `mach`(Ma)。

```
iconverter://tool/speed?v=100&from=kmPerHour&to=milePerHour
```

```
iconverter://tool/speed?v=1&from=mach&to=meterPerSecond
```

**壓強**
單位：`pascal`(Pa) · `kilopascal`(kPa) · `bar`(bar) · `atmosphere`(atm) · `psi`(psi) · `mmHg`(mmHg)。

```
iconverter://tool/pressure?v=1&from=atmosphere&to=kilopascal
```

```
iconverter://tool/pressure?v=120&from=mmHg&to=kilopascal
```

**能量**
單位：`joule`(J) · `kilojoule`(kJ) · `calorie`(cal) · `kilocalorie`(kcal) · `kilowattHour`(kWh) · `btu`(BTU)。

```
iconverter://tool/energy?v=1&from=kilowattHour&to=kilojoule
```

```
iconverter://tool/energy?v=500&from=kilocalorie&to=kilojoule
```

**功率**
單位：`watt`(W) · `kilowatt`(kW) · `hpMechanical`(hp) · `hpMetric`(PS) · `btuPerHour`(BTU/h)。

```
iconverter://tool/power?v=1&from=hpMechanical&to=kilowatt
```

```
iconverter://tool/power?v=3000&from=watt&to=hpMetric
```

**力**
單位：`newton`(N) · `kilonewton`(kN) · `kgf`(kgf) · `lbf`(lbf) · `dyne`(dyn)。

```
iconverter://tool/force?v=9.8&from=newton&to=kgf
```

```
iconverter://tool/force?v=1&from=kilonewton&to=lbf
```

**扭矩**
單位：`newtonMeter`(N·m) · `newtonCentimeter`(N·cm) · `kgfMeter`(kgf·m) · `footPound`(ft·lb) · `inchPound`(in·lb)。

```
iconverter://tool/torque?v=100&from=newtonMeter&to=footPound
```

**頻率**
單位：`hertz`(Hz) · `kilohertz`(kHz) · `megahertz`(MHz) · `gigahertz`(GHz) · `terahertz`(THz) · `rpm`(rpm)。

```
iconverter://tool/frequency?v=2.4&from=gigahertz&to=megahertz
```

```
iconverter://tool/frequency?v=3000&from=rpm&to=hertz
```

**角度**
單位：`degree`(°) · `radian`(rad) · `gradian`(grad) · `arcminute`(') · `arcsecond`(") · `turn`(turn)。

```
iconverter://tool/angle?v=180&from=degree&to=radian
```

```
iconverter://tool/angle?v=1&from=turn&to=degree
```

**資料儲存**
單位：`byte`(B) · `kilobyte`(KB) · `megabyte`(MB) · `gigabyte`(GB) · `terabyte`(TB) · `kibibyte`(KiB) · `mebibyte`(MiB) · `gibibyte`(GiB)。

```
iconverter://tool/dataStorage?v=1&from=gigabyte&to=mebibyte
```

```
iconverter://tool/dataStorage?v=512&from=mebibyte&to=gigabyte
```

**資料速率**
單位：`bps`(bps) · `kbps`(Kbps) · `mbps`(Mbps) · `gbps`(Gbps) · `kBps`(KB/s) · `mBps`(MB/s) · `gBps`(GB/s)。

```
iconverter://tool/dataRate?v=100&from=mbps&to=mBps
```

```
iconverter://tool/dataRate?v=1&from=gbps&to=mbps
```

**照度**
單位：`lux`(lx) · `footCandle`(fc) · `phot`(ph) · `nox`(nx)。

```
iconverter://tool/illuminance?v=500&from=lux&to=footCandle
```

**磁感應強度**
單位：`tesla`(T) · `millitesla`(mT) · `microtesla`(μT) · `gauss`(G) · `milligauss`(mG)。

```
iconverter://tool/magneticFlux?v=1&from=tesla&to=gauss
```

**放射性活度**
單位：`becquerel`(Bq) · `kilobecquerel`(kBq) · `megabecquerel`(MBq) · `curie`(Ci) · `millicurie`(mCi) · `microcurie`(μCi)。

```
iconverter://tool/radioactivity?v=1&from=curie&to=megabecquerel
```

**黏度**
單位：`pascalSecond`(Pa·s) · `millipascalSecond`(mPa·s) · `poise`(P) · `centipoise`(cP)。

```
iconverter://tool/viscosity?v=1&from=pascalSecond&to=centipoise
```

**燃油經濟性**
單位：`lPer100km`(L/100km) · `kmPerL`(km/L) · `mpgUS`(MPG US) · `mpgUK`(MPG UK)。

```
iconverter://tool/fuelEconomy?v=8.5&from=lPer100km&to=kmPerL
```

```
iconverter://tool/fuelEconomy?v=30&from=mpgUS&to=lPer100km
```

**流量**
單位：`cubicMeterPerSecond`(m³/s) · `cubicMeterPerHour`(m³/h) · `literPerSecond`(L/s) · `literPerMinute`(L/min) · `literPerHour`(L/h) · `usGallonPerMinute`(gpm US) · `cubicFootPerMinute`(cfm)。

```
iconverter://tool/flowRate?v=1&from=literPerMinute&to=cubicMeterPerHour
```

**密度**
單位：`kgPerCubicMeter`(kg/m³) · `gramPerCubicCentimeter`(g/cm³) · `gramPerLiter`(g/L) · `kgPerLiter`(kg/L) · `poundPerCubicFoot`(lb/ft³)。

```
iconverter://tool/density?v=1&from=gramPerCubicCentimeter&to=kgPerCubicMeter
```

**磁通量**
單位：`weber`(Wb) · `milliweber`(mWb) · `microweber`(μWb) · `kiloweber`(kWb) · `maxwell`(Mx)。

```
iconverter://tool/magneticFluxTrue?v=1&from=weber&to=maxwell
```

**吸收劑量**
單位：`gray`(Gy) · `milligray`(mGy) · `microgray`(μGy) · `kilogray`(kGy) · `rad`(rad) · `millirad`(mrad)。

```
iconverter://tool/absorbedDose?v=1&from=gray&to=rad
```

**等效劑量**
單位：`sievert`(Sv) · `millisievert`(mSv) · `microsievert`(μSv) · `rem`(rem) · `millirem`(mrem)。

```
iconverter://tool/equivalentDose?v=1&from=sievert&to=rem
```

```
iconverter://tool/equivalentDose?v=20&from=millisievert&to=microsievert
```

**物質的量**
單位：`mole`(mol) · `millimole`(mmol) · `micromole`(μmol) · `kilomole`(kmol) · `nanomole`(nmol) · `picomole`(pmol)。

```
iconverter://tool/amountOfSubstance?v=1&from=mole&to=millimole
```

```
iconverter://tool/amountOfSubstance?v=150&from=millimole&to=micromole
```

---

[返回 iConverter 支援頁](../) &middot; [常見問題](../faq) &middot; [隱私政策](../privacy)

</section>
<section lang="ja" markdown="1">

iConverter は `iconverter://` をサポート URLスキームのディープリンク — 外部アプリ、Webページ、QRコード(生成または**scan in-app**)、Safari、Apple Shortcuts、オプションで入力フィールドをクエリパラメータで埋め込むことができます。

> **ウィジェットノート:** **Launcher**ウィジェットツールピッカーは、**Webブラウザ**以外のすべてのサポートされているツールを含みます。 Widget の設定 UI は、**iOS システム言語** に従っており、アプリ内言語は設定下で上書きされます。

## プロトコル仕様


```
iconverter://tool/<ToolItem.rawValue>?key=value&key2=value2
```


- `<ToolItem.rawValue>` は、ウィジェットの深いリンクと同じ命名を共有します。
- パラメータ名は、短いキーと同義語のエイリアス(たとえば `text` は `input` と同等です)の両方をサポートします。
- Booleans: `1/true/yes/on` → true;`0/false/no/off` → false。
- 日付: `yyy-MM-dd`、ISO8601、Unixタイムスタンプ(秒)をサポートしています。
- 単位のコンバーターは共通のフォーマットを共有します:`v` = 値、`from` = ソース単位(rawValue か記号、場合の無感覚)、`to` = ターゲット単位。

---

## 1. 計算機

** 電卓** — のみ開く


```
iconverter://tool/calculator
```


**科学的な電卓** — のみ開く


```
iconverter://tool/scientific
```


**プログラマ 電卓** — のみ開く


```
iconverter://tool/programmer
```


---

## 2. ファイナンス

**住宅ローン計算機** `iconverter://` = 融資額、 `<ToolItem.rawValue>` = 年間レート%、 `text` = 年、 `input` = 0 = 等しいインストール/1 = 等しいプリンシパル。


```
iconverter://tool/mortgage?p=1000000&r=3.7&y=30&mode=0
```


**所得税** `iconverter://` = 毎月の給与、 `<ToolItem.rawValue>` = 社会保険、 `text` = 特別控除、 `input` = しきい値、 `1/true/yes/on` = 年間ボーナス。


```
iconverter://tool/incomeTax?salary=20000&insurance=3000&deduction=1000&threshold=5000&bonus=50000
```


**複合利息** `iconverter://` = プリンシパル、 `<ToolItem.rawValue>` = 毎月の貢献、 `text` = 年率%、 `input` =年、 `1/true/yes/on` = 0 =年/ 1 =月/ 2 =日、 `0/false/no/off` =インフレ%。


```
iconverter://tool/compoundInterest?p=100000&m=1000&r=7&y=10&freq=1
```


**割引計算機** `iconverter://` = 0–4、 `<ToolItem.rawValue>` = 元の価格、 `text` = 割引比、 `input` = しきい値、 `1/true/yes/on` = 削減量。


```
iconverter://tool/discount?mode=0&p=299&r=8.5
```


フルマイナス例:


```
iconverter://tool/discount?mode=3&p=350&t=300&u=50
```


**タイピング&AAスプリット** `iconverter://` = 0 = チップ / 1 = AA分割, `<ToolItem.rawValue>` = 請求, `text` = チップ%, `input` = 税 %, `1/true/yes/on` = 人件数.


```
iconverter://tool/tipAA?mode=0&bill=200&tip=15&tax=0&ppl=4
```


**住宅ローン前払い** `iconverter://` = 元のローン、 `<ToolItem.rawValue>` = 年間レート%、 `text` = 総期間(年)、 `input` = 支払条件、 `1/true/yes/on` = プリペイ量、 `0/false/no/off` = 0 = 短縮/ 1 = 月/ 2 = 比較を削減します。


```
iconverter://tool/mortgagePrepay?p=800000&r=3.7&total=30&paid=5&prepay=100000&mode=2
```


**不動産税** — 営業のみ


```
iconverter://tool/realEstateTax
```


---

## 3. 日付と時刻

**年齢&記念日** `iconverter://` = 誕生日 `<ToolItem.rawValue>` 、 `text` = 参照日。


```
iconverter://tool/ageAnniversary?birth=1990-05-01&ref=2026-05-17
```


**日時 Arithmetic** `iconverter://` = 0 = add/subtract / 1 = 日付の差。

Add-subtract モード( `iconverter://` = 開始日、 `<ToolItem.rawValue>` = ± 日、 `text` = ± 週間、 `input` = ± 月、 `1/true/yes/on` = ± 年):


```
iconverter://tool/dateArithmetic?mode=0&d1=2026-05-17&d=100
```


差分モード( `iconverter://` = 日付1、 `<ToolItem.rawValue>` =日付2):


```
iconverter://tool/dateArithmetic?mode=1&d1=2026-01-01&d2=2026-12-31
```


**月のカレンダー** `iconverter://` = グレゴリオンの日付 `<ToolItem.rawValue>` ```
iconverter://tool/lunarCalendar?date=2026-05-17
```


**Solar Terms** — のみオープン


```
iconverter://tool/solarTerms
```


**カウントダウン** `iconverter://` = イベント名, `<ToolItem.rawValue>` = 対象日 `text` , `input` = 時刻 `1/true/yes/on` ```
iconverter://tool/countdown?label=Holiday&target=2026-10-01&time=0
```


**妊娠電卓** `iconverter://` = 0 = LMP / 1 = 概念 / 2 = IVF、 `<ToolItem.rawValue>` = 参照日付、 `text` = IVF embryo 日 0 = D3 / 1 = D5。


```
iconverter://tool/pregnancy?method=0&ref=2026-03-01
```



```
iconverter://tool/pregnancy?method=2&ref=2026-03-15&ivf=1
```


**月経周期** `iconverter://` = 最後の月経の日付、 `<ToolItem.rawValue>` = サイクル日、 `text` = 期間日。


```
iconverter://tool/menstrual?lmp=2026-05-01&cycle=28&period=5
```


**ワールドクロック** `iconverter://` = 市検索キーワード, `<ToolItem.rawValue>` = 現在の時間を使用する `text` , `input` = カスタム日付時刻.


```
iconverter://tool/worldClock?q=Tokyo
```



```
iconverter://tool/worldClock?now=0&ref=2026-05-17T20:00:00
```


**Zodiac** — のみ開く


```
iconverter://tool/zodiac
```


---

## 4. 数学

**比率計算機** `iconverter://` = 0–4, `<ToolItem.rawValue>` = 値 A, `text` = 値 B


```
iconverter://tool/percentage?mode=0&a=75&b=120
```


**反応電卓** — のみ開く


```
iconverter://tool/fraction
```


**プライムファクショナライゼーション** — のみオープン


```
iconverter://tool/primeFactor
```


**Quadratic Solver** — のみ公開


```
iconverter://tool/quadraticSolver
```


**統計** `iconverter://` = スペース/コンマ/セミコロンで区切られたデータセット。


```
iconverter://tool/statistics?data=1,2,3,4,5,6,7,8,9,10
```


**コンビネーション&パーミュテーション** - のみ開く


```
iconverter://tool/combinations
```


**幾何学** `iconverter://` = 形状、 `<ToolItem.rawValue>` = 寸法パラメータ。

利用可能な形状: `iconverter://` サークル ( `iconverter://` = 半径):


```
iconverter://tool/geometry?shape=circle&v1=5
```


長方形( `iconverter://` =長さ、 `<ToolItem.rawValue>` =幅):


```
iconverter://tool/geometry?shape=rectangle&v1=10&v2=5
```


球( `iconverter://` = 半径):


```
iconverter://tool/geometry?shape=sphere&v1=3
```


シリンダー( `iconverter://` = 半径、 `<ToolItem.rawValue>` = 高さ):


```
iconverter://tool/geometry?shape=cylinder&v1=4&v2=10
```


---

## 5. エンコーディング

Roman Numeral(ローマ数字)** `iconverter://` = アラビア数字(1–3999); または `<ToolItem.rawValue>` = ローマ数字の文字列。


```
iconverter://tool/roman?n=2026
```



```
iconverter://tool/roman?roman=MMXXVI
```


**Base64エンコーダ/デコーダ** `iconverter://` = エンコーダ/デコード、 `<ToolItem.rawValue>` = URL セーフモード `text` 、 `input` = 入力テキスト。


```
iconverter://tool/base64?mode=encode&text=Hello%2C+World!
```



```
iconverter://tool/base64?mode=decode&urlSafe=0&text=SGVsbG8sIFdvcmxkIQ%3D%3D
```


**URLエンコーダ/デコーダ** `iconverter://` = エンコーダ/デコード、 `<ToolItem.rawValue>` = コンポーネントモード 0 = フル/ 1 = クエリ/ 2 = パス、 `text` = 入力。


```
iconverter://tool/urlCoder?mode=encode&comp=0&text=https://example.com/path?q=hello world
```



```
iconverter://tool/urlCoder?mode=decode&text=https%3A%2F%2Fexample.com%2F%3Fq%3Dhello%20world
```


**ハッシュ計算機** `iconverter://` = 入力, `<ToolItem.rawValue>` = md5/sha1/sha256/sha512, `text` = 上位ケース `input` , `1/true/yes/on` = HMAC `0/false/no/off` , `yyyy-MM-dd` = HMAC キーを有効にします。


```
iconverter://tool/hashing?text=Hello+World&algo=sha256&upper=0
```



```
iconverter://tool/hashing?text=data&algo=md5&hmac=1&key=secret
```


**単語数** `iconverter://` = 解析するテキスト


```
iconverter://tool/wordCount?text=The+quick+brown+fox+jumps+over+the+lazy+dog.
```


**カラーコンバータ** `iconverter://` = hex色; または `<ToolItem.rawValue>` ```
iconverter://tool/colorConverter?hex=%23FF8800
```



```
iconverter://tool/colorConverter?r=255&g=136&b=0
```


**カラーパレット** — のみ開く


```
iconverter://tool/colorPalette
```


**QRコード** `iconverter://` = 内容, `<ToolItem.rawValue>` = `text` 等, `input` = エラー補正レベル `1/true/yes/on` ```
iconverter://tool/qrcode?text=https%3A%2F%2Fexample.com&ecc=H
```



```
iconverter://tool/qrcode?text=Hello+iConverter&format=qr&ecc=M
```


**JSON フォーマッタ ** `iconverter://` = JSON 文字列 (URL-encoded), `<ToolItem.rawValue>` = インデントスペース 2/4.


```
iconverter://tool/jsonFormatter?text=%7B%22name%22%3A%22Alice%22%2C%22age%22%3A30%7D&indent=2
```


**タイムスタンプ** `iconverter://` = Unix タイムスタンプ (秒), `<ToolItem.rawValue>` = ユニット 0 = sec / 1 = ms; または `text` = ISO8601 日付文字列.


```
iconverter://tool/timestamp?ts=1747440000
```



```
iconverter://tool/timestamp?iso=2026-05-17T12:00:00
```


**銀行カードバリデータ** `iconverter://` = カード番号。


```
iconverter://tool/bankCard?num=6214830172816734
```


**テキストケースコンバーター** `iconverter://` = 入力テキスト。


```
iconverter://tool/textCase?text=hello+world+from+iConverter
```


**Text Diff** — のみ開く


```
iconverter://tool/textDiff
```


**HTTPリクエスト** `iconverter://` = リクエスト URL, `<ToolItem.rawValue>` = GET/POST/PUT/PATCH/DELETE, `text` = リクエスト ボディ, `input` , `0/false/no/off` = ヘッダー JSON.


```
iconverter://tool/httpRequest?url=https%3A%2F%2Fapi.example.com%2Fusers&method=GET
```



```
iconverter://tool/httpRequest?url=https%3A%2F%2Fapi.example.com%2Fusers&method=POST&body=%7B%22name%22%3A%22Alice%22%7D&bodyKind=json
```


**ファイルのダウンロード** `iconverter://` = URL、 `<ToolItem.rawValue>` =ファイル名(オプション)をダウンロードします。


```
iconverter://tool/fileDownload?url=https%3A%2F%2Fexample.com%2Freport.pdf&name=report.pdf
```


**HTTPステータスコード** `iconverter://` = ステータスコード; または `<ToolItem.rawValue>` = 検索キーワード。


```
iconverter://tool/httpStatusCodes?code=404
```



```
iconverter://tool/httpStatusCodes?q=redirect
```


**IP ユーティリティ** `iconverter://` = subnet/cidr/range, `<ToolItem.rawValue>` = IPアドレス, `text` = サブネットマスク; または `input` = CIDR接頭辞の長さ.


```
iconverter://tool/ipUtility?mode=subnet&ip=192.168.1.0&mask=255.255.255.0
```



```
iconverter://tool/ipUtility?ip=10.0.0.0&prefix=24
```


**アスキーテーブル** `iconverter://` = 初期のコードポイント; または `<ToolItem.rawValue>` = hex のコードポイント; または `text` = 検索します。


```
iconverter://tool/asciiTable?dec=65
```



```
iconverter://tool/asciiTable?q=space
```


**パスワードジェネレータ** `iconverter://` = 長, `<ToolItem.rawValue>` = 長ケース `text` , `input` = 長, `0/false/no/off` = 数字 `yyyy-MM-dd` , `v` = シンボル `from` , `to` = あいまいな文字 `p` ```
iconverter://tool/passwordGenerator?length=20&upper=1&lower=1&digits=1&symbols=1&unambiguous=1&go=1
```


**ランダムナンバージェネレータ** `iconverter://` = 最小値、 `<ToolItem.rawValue>` =最大値、 `text` = カウント、 `input` = 異常な場所、 `1/true/yes/on` = ユニーク `0/false/no/off` 、 `yyyy-MM-dd` = 0 = なし/ 1 = asc / 2 = desc、 `v` = すぐに生成 `from` ```
iconverter://tool/randomNumber?min=1&max=100&n=10&unique=1&sort=1&go=1
```



```
iconverter://tool/randomNumber?min=0&max=1&n=5&decimals=4&go=1
```


**モーニングコード** `iconverter://` = エンコーダ/デコード、 `<ToolItem.rawValue>` = 入力テキスト。


```
iconverter://tool/morseCode?mode=encode&text=SOS
```



```
iconverter://tool/morseCode?mode=decode&text=...+---+...
```


**JWTデコーダ** `iconverter://` = JWT トークン文字列。


```
iconverter://tool/jwtParser?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c
```


**Cron Expression Parser ** `iconverter://` = Cron 式( `<ToolItem.rawValue>` ```
iconverter://tool/cronParser?expr=0+9+*+*+1-5
```



```
iconverter://tool/cronParser?expr=0+0+*+*+*
```


**正規テスター** `iconverter://` = regex パターン (URL-encoded), `<ToolItem.rawValue>` = テストテキスト, `text` = 置換, `input` = ケースインセンティブ `1/true/yes/on` , `0/false/no/off` = 複数行 `yyyy-MM-dd` , `v` = 点all `from` ```
iconverter://tool/regexTester?pattern=%5Cd%2B&haystack=abc123def456&i=0
```



```
iconverter://tool/regexTester?pattern=%28%5Cw%2B%29&haystack=hello+world&replacement=%5B%241%5D&i=1
```


**Webブラウザ** `iconverter://` は、直接 URL を開くか、 `<ToolItem.rawValue>` = 検索クエリ(デフォルトの検索エンジンを使用する)。


```
iconverter://tool/webBrowser?url=https%3A%2F%2Fexample.com
```



```
iconverter://tool/webBrowser?q=SwiftUI+deep+link+2026
```


---

## 6. ライフスタイル

**BMI 電卓** `iconverter://` = 高さ cm, `<ToolItem.rawValue>` = 体重 kg, `text` = 標準 0 = 中国人成人 / 1 = WHO.


```
iconverter://tool/bmi?h=175&w=70&std=0
```


**BMR計算機** `iconverter://` = 高さ cm, `<ToolItem.rawValue>` = 体重 kg, `text` = 年齢, `input` = m = 男性/ f = 女性, `1/true/yes/on` = 活動レベル 0–4, `0/false/no/off` = 0 = ハリス・ベネディクト / 1 = Mifflin-St Jeor.


```
iconverter://tool/bmr?h=175&w=70&age=30&sex=m&act=1&formula=1
```


**クラッシングサイズ** — のみ開く


```
iconverter://tool/clothingSize
```


**リングサイズ** — のみ開く


```
iconverter://tool/ringSize
```


**Height Converter** — のみオープン


```
iconverter://tool/heightConverter
```


**燃料費計算機** `iconverter://` = 0 = メトリック/ 1 = 帝国、 `<ToolItem.rawValue>` = 距離、 `text` = 100 kmあたりの消費量、 `input` = 燃料価格、 `1/true/yes/on` = 人。


```
iconverter://tool/fuelCost?unit=0&d=500&c=8.5&p=7.8&n=1
```


**船積み料金の計算機** `iconverter://` = 実際の体重 kg、 `<ToolItem.rawValue>` = 最初の体重 kg、 `text` =最初の重量料金、 `input` =ステップ重量 kg、 `1/true/yes/on` =ステップ手数料。


```
iconverter://tool/shippingFee?w=3.5&fw=1&ff=12&sw=1&sf=8
```


体積重( `iconverter://` = `<ToolItem.rawValue>` ```
iconverter://tool/shippingFee?w=2&vol=1&l=50&wd=40&h=30&div=6000&fw=1&ff=12&sw=1&sf=8
```


**血液アルコール含有量(BAC)** `iconverter://` = m = 男性/ f = 女性、 `<ToolItem.rawValue>` = 体重 kg、 `text` = 体積 mL、 `input` = ABV %、 `1/true/yes/on` = 飲酒後の時間。


```
iconverter://tool/alcoholBac?sex=m&w=70&v=500&abv=5&h=0.5
```


**関係** `iconverter://` = 関係チェーン (コンマ区切り), `<ToolItem.rawValue>` = ego 性別 0 = 男性 / 1 = 女性, `text` = 逆表示 `input` .


```
iconverter://tool/relationship?chain=f,os&sex=0&reverse=1
```



```
iconverter://tool/relationship?chain=m,ob&sex=1&reverse=0
```


**IDカードパーサー** `iconverter://` = IDカード番号。


```
iconverter://tool/idCard?id=110101199003073010
```


**コインフリップ** — のみ開く


```
iconverter://tool/coinFlip
```


**ダイス ローラー** — のみ開く


```
iconverter://tool/diceRoller
```


**Random Draw** — のみ公開


```
iconverter://tool/randomDraw
```


**スピンホイール** — のみ開く


```
iconverter://tool/spinWheel
```


**ビデオフレームエクスポート** — のみ開く


```
iconverter://tool/videoFrameExport
```


---

## 7. センサー

**Compass** — のみ開く


```
iconverter://tool/compass
```


**レベル** — のみ開く


```
iconverter://tool/level
```


**高度** — のみ開く


```
iconverter://tool/altitude
```


---

## 8. 中国語

**中国語** `iconverter://` = 数値。


```
iconverter://tool/chineseNumber?n=12345.67
```


**中国番号の逆** `iconverter://` = 中国数字文字列。


```
iconverter://tool/chineseNumberReverse?text=一万二千三百四十五
```


**財務量** `iconverter://` = 値、 `<ToolItem.rawValue>` = 整数 `text` ```
iconverter://tool/financialAmount?amount=12345.67&zheng=1
```


---

## 9. 単位のコンバーター

一般的な形式: `iconverter://` = 値、 `<ToolItem.rawValue>` = ソースユニット(rawValueまたはシンボル、ケースインセンティブ)、 `text` = ターゲットユニット。

---

**長さ**
共通単位: `iconverter://` (m) · `<ToolItem.rawValue>` (km) · `text` (cm) · `input` (mm) · `1/true/yes/on` (ft) · `0/false/no/off` (in) · `yyyy-MM-dd` (mi) · `v` (yd) ·              (nmi)            (nmi)                (nmi           (nmi                               (n


```
iconverter://tool/length?v=100&from=meter&to=foot
```



```
iconverter://tool/length?v=1&from=mile&to=kilometer
```


**エリア**
共通単位: `iconverter://` (m2) · `<ToolItem.rawValue>` (ha) · `text` (acre) · `input` (ft2) · `1/true/yes/on` (mile2) · `0/false/no/off` (加算) · `yyyy-MM-dd` (km2)。


```
iconverter://tool/area?v=1&from=hectare&to=mu
```



```
iconverter://tool/area?v=1&from=acre&to=squareMeter
```


**ボリューム**
共通単位: `iconverter://` (L) · `<ToolItem.rawValue>` (mL) · `text` (m3) · `input` (gal) · `1/true/yes/on` (fl oz) · `0/false/no/off` (cup) · `yyyy-MM-dd` (gal UK) · `v` (bbl)。


```
iconverter://tool/volume?v=1&from=gallon&to=liter
```



```
iconverter://tool/volume?v=355&from=milliliter&to=fluidOunce
```


**重量/質量**
普通の単位: `iconverter://` (kg) · `<ToolItem.rawValue>` (g) · `text` (lb) · `input` (oz) · `1/true/yes/on` (t) · `0/false/no/off` () · `yyyy-MM-dd` (lb) · `v` (ct)。


```
iconverter://tool/weight?v=1&from=pound&to=kilogram
```



```
iconverter://tool/weight?v=1&from=jin&to=gram
```


**温度**
単位: `iconverter://` (°C) · `<ToolItem.rawValue>` (°F) · `text` (K) · `input` (°R) · `1/true/yes/on` (°Re)。


```
iconverter://tool/temperature?v=100&from=celsius&to=fahrenheit
```



```
iconverter://tool/temperature?v=37&from=celsius&to=kelvin
```


**時間**
共通単位: `iconverter://` (s) · `<ToolItem.rawValue>` (min) · `text` (h) · `input` (日) · `1/true/yes/on` (wk) · `0/false/no/off` (mo) · `yyyy-MM-dd` (yr) · `v` (ms) · `from` (μs)


```
iconverter://tool/time?v=1&from=hour&to=second
```



```
iconverter://tool/time?v=7&from=day&to=hour
```


**速度**
単位: `iconverter://` (m/s) · `<ToolItem.rawValue>` (km/h) · `text` (mph) · `input` (kn) · `1/true/yes/on` (Ma)。


```
iconverter://tool/speed?v=100&from=kmPerHour&to=milePerHour
```



```
iconverter://tool/speed?v=1&from=mach&to=meterPerSecond
```


**圧力**
単位: `iconverter://` (Pa) · `<ToolItem.rawValue>` (kPa) · `text` (bar) · `input` (atm) · `1/true/yes/on` (psi) · `0/false/no/off` (mmHg)。


```
iconverter://tool/pressure?v=1&from=atmosphere&to=kilopascal
```



```
iconverter://tool/pressure?v=120&from=mmHg&to=kilopascal
```


**エナジー**
単位: `iconverter://` (J) · `<ToolItem.rawValue>` (kJ) · `text` (cal) · `input` (kcal) · `1/true/yes/on` (kWh) · `0/false/no/off` (BTU)。


```
iconverter://tool/energy?v=1&from=kilowattHour&to=kilojoule
```



```
iconverter://tool/energy?v=500&from=kilocalorie&to=kilojoule
```


**電源**
単位: `iconverter://` (W)・ `<ToolItem.rawValue>` (kW)・ `text` (hp)・      (PS)・ `1/true/yes/on` (BTU/h)


```
iconverter://tool/power?v=1&from=hpMechanical&to=kilowatt
```



```
iconverter://tool/power?v=3000&from=watt&to=hpMetric
```


**強制**
単位: `iconverter://` (N)・ `<ToolItem.rawValue>` (kN)・ `text` (kgf)・ `input` (lbf)・ `1/true/yes/on` (dyn)。


```
iconverter://tool/force?v=9.8&from=newton&to=kgf
```



```
iconverter://tool/force?v=1&from=kilonewton&to=lbf
```


**トルク**
単位: `iconverter://` (N・m) · `<ToolItem.rawValue>` (N・cm) · `text` (kgf・m) · `input` (ft・lb) · `1/true/yes/on` (in・lb)。


```
iconverter://tool/torque?v=100&from=newtonMeter&to=footPound
```


**設備**
単位: `iconverter://` (Hz) · `<ToolItem.rawValue>` (kHz) · `text` (MHz) · `input` (GHz) · `1/true/yes/on` (THz) · `0/false/no/off` (rpm)


```
iconverter://tool/frequency?v=2.4&from=gigahertz&to=megahertz
```



```
iconverter://tool/frequency?v=3000&from=rpm&to=hertz
```


**アングル**
単位: `iconverter://` (°)・ `<ToolItem.rawValue>` (rad)・ `text` (grad)・ `input` (')・ `1/true/yes/on` (")・ `0/false/no/off` (turn)


```
iconverter://tool/angle?v=180&from=degree&to=radian
```



```
iconverter://tool/angle?v=1&from=turn&to=degree
```


**データストレージ**
単位: `iconverter://` (B) · `<ToolItem.rawValue>` (KB) · `text` (MB) · `input` (GB) · `1/true/yes/on` (TB) · `0/false/no/off` (KiB) · `yyyy-MM-dd` (MiB) · `v` (GiB)。


```
iconverter://tool/dataStorage?v=1&from=gigabyte&to=mebibyte
```



```
iconverter://tool/dataStorage?v=512&from=mebibyte&to=gigabyte
```


**データレート**
単位: `iconverter://` (bps) · `<ToolItem.rawValue>` (Kbps) · `text` (Mbps) · `input` (Gbps) · `1/true/yes/on` (KB/s) · `0/false/no/off` (MB/s) · `yyyy-MM-dd` (GB/s)


```
iconverter://tool/dataRate?v=100&from=mbps&to=mBps
```



```
iconverter://tool/dataRate?v=1&from=gbps&to=mbps
```


**照度**
単位: `iconverter://` (lx) · `<ToolItem.rawValue>` (fc) · `text` (ph) · `input` (nx)。


```
iconverter://tool/illuminance?v=500&from=lux&to=footCandle
```


**磁気変化密度**
単位: `iconverter://` (T) · `<ToolItem.rawValue>` (mT) · `text` (μT) · `input` (G) · `1/true/yes/on` (mG)。


```
iconverter://tool/magneticFlux?v=1&from=tesla&to=gauss
```


**放射能**
単位: `iconverter://` (Bq)· `<ToolItem.rawValue>` (kBq)·   (MBq)·      (Ci)· `1/true/yes/on` (mCi)·    (μCi)。


```
iconverter://tool/radioactivity?v=1&from=curie&to=megabecquerel
```


**粘度**
単位: `iconverter://` (Pa·s) · `<ToolItem.rawValue>` (mPa·s) · `text` (P) · `input` (cP)。


```
iconverter://tool/viscosity?v=1&from=pascalSecond&to=centipoise
```


**燃料経済**
単位: `iconverter://` (L/100km) · `<ToolItem.rawValue>` (km/L) · `text` (MPG 米国) · `input` (MPG英国)。


```
iconverter://tool/fuelEconomy?v=8.5&from=lPer100km&to=kmPerL
```



```
iconverter://tool/fuelEconomy?v=30&from=mpgUS&to=lPer100km
```


**流量**
単位: `iconverter://` (m3/s) · `<ToolItem.rawValue>` (m3/h) · `text` (L/s) · `input` (L/min) · `1/true/yes/on` (L/h) · `0/false/no/off` (gpm US) · `yyyy-MM-dd` (cfm)


```
iconverter://tool/flowRate?v=1&from=literPerMinute&to=cubicMeterPerHour
```


**密度**
単位: `iconverter://` (kg/m3) · `<ToolItem.rawValue>` (g/cm3) · `text` (g/L) · `input` (kg/L) · `1/true/yes/on` (lb/ft3)。


```
iconverter://tool/density?v=1&from=gramPerCubicCentimeter&to=kgPerCubicMeter
```


**磁気変化(Wb)**
単位: `iconverter://` (Wb) · `<ToolItem.rawValue>` (mWb) · `text` (μWb) · `input` (kWb) · `1/true/yes/on` (Mx)。


```
iconverter://tool/magneticFluxTrue?v=1&from=weber&to=maxwell
```


**吸収線量**
単位: `iconverter://` (Gy) · `<ToolItem.rawValue>` (mGy) · `text` (μGy) · `input` (kGy) · `1/true/yes/on` (rad) · `0/false/no/off` (mrad)


```
iconverter://tool/absorbedDose?v=1&from=gray&to=rad
```


**等価線量**
単位: `iconverter://` (Sv) · `<ToolItem.rawValue>` (mSv) · `text` (μSv) · `input` (rem) · `1/true/yes/on` (mrem)。


```
iconverter://tool/equivalentDose?v=1&from=sievert&to=rem
```



```
iconverter://tool/equivalentDose?v=20&from=millisievert&to=microsievert
```


**Substanceの量**
単位: `iconverter://` (mol) · `<ToolItem.rawValue>` (mmol) · `text` (μmol) · `input` (kmol) · `1/true/yes/on` (nmol) · `0/false/no/off` (pmol)。


```
iconverter://tool/amountOfSubstance?v=1&from=mole&to=millimole
```



```
iconverter://tool/amountOfSubstance?v=150&from=millimole&to=micromole
```


---

[iConverterサポートに戻る](./) &middot; [FAQ](../faq) &middot; [プライバシーポリシー](./privacy)

</section>
<section lang="ko" markdown="1">

iConverter 지원 `iconverter://` URL 계획 깊은 링크 — 외부 앱, 웹 페이지, QR 코드 (generate 또는 **scan in-app**), Safari, 또는 Apple Shortcuts에서 101 도구 중 하나를 열고, 쿼리 매개 변수를 통해 선택적으로 사전 작성 입력 필드.

> ** 위젯 노트:** **Launcher** 위젯 도구 선택기는 **Web Browser**를 제외한 모든 지원 도구를 포함합니다. Widget 구성 UI는 **iOS 시스템 언어 **, 설정 아래 앱 언어 무시.

## 프로토콜


```
iconverter://tool/<ToolItem.rawValue>?key=value&key2=value2
```


- `<ToolItem.rawValue>`는 위젯 딥 링크로 동일한 이름을 공유합니다.
- 매개변수 이름은 짧은 열쇠와 동시 별명을 둘 다 지원합니다 (예를들면 `text`는 `input`와 동일합니다).
- Booleans: `1/true/yes/on` → true; `0/false/no/off` → false.
- 날짜: 지원 `yyyy-MM-dd`, ISO8601, 유닉스 타임스탬프 (둘째로).
- 단위 변환기는 일반적인 형식을 공유합니다: `v` = value, `from` = source unit (rawValue or symbol, case-insensitive), `to` = target unit.

---

## 1. 계산기

**Calculator** - 만 개방


```
iconverter://tool/calculator
```


** 과학 계산기 ** - 만 개방


```
iconverter://tool/scientific
```


**Programmer Calculator ** - 만 개방


```
iconverter://tool/programmer
```


---

## 2. 금융

** 모기지 계산기 ** `iconverter://` = 대출 금액, `<ToolItem.rawValue>` = 연간 비율 %, `text` = 년, `input` = 0 = 동등한 설치 / 1 = 동등한 주.


```
iconverter://tool/mortgage?p=1000000&r=3.7&y=30&mode=0
```


** 소득세** `iconverter://` = 월급, `<ToolItem.rawValue>` = 사회 보험, `text` = 특별 감속, `input` = 임계값, `1/true/yes/on` = 연간 보너스.


```
iconverter://tool/incomeTax?salary=20000&insurance=3000&deduction=1000&threshold=5000&bonus=50000
```


**Compound 관심** `iconverter://` = 주, `<ToolItem.rawValue>` = 월별 기여, `text` = 연평균 %, `input` = 년, `1/true/yes/on` = 0 = 연중 / 1 = 월 / 2 = 일일, `0/false/no/off` = 인플레이션 %.


```
iconverter://tool/compoundInterest?p=100000&m=1000&r=7&y=10&freq=1
```


** 계산기 ** `iconverter://` = 0–4, `<ToolItem.rawValue>` = 원래 가격, `text` = 할인 비율, `input` = 임계값, `1/true/yes/on` = 감소 금액.


```
iconverter://tool/discount?mode=0&p=299&r=8.5
```


Full-minus 예제:


```
iconverter://tool/discount?mode=3&p=350&t=300&u=50
```


**Tip & AA 분할 ** `iconverter://` = 0 = 팁 / 1 = AA 분할, `<ToolItem.rawValue>` = 빌, `text` = 팁 %, `input` = 세금 %, `1/true/yes/on` = 사람들 수.


```
iconverter://tool/tipAA?mode=0&bill=200&tip=15&tax=0&ppl=4
```


** 모기지 선불 ** `iconverter://` = 원래 대출, `<ToolItem.rawValue>` = 연간 비율 %, `text` = 총 용어 (년), `input` = 유료 용어, `1/true/yes/on` = 선불 금액, `0/false/no/off` = 0 = 단기 / 1 = 월 / 2 = 비교를 감소.


```
iconverter://tool/mortgagePrepay?p=800000&r=3.7&total=30&paid=5&prepay=100000&mode=2
```


**부동산세** — 만개


```
iconverter://tool/realEstateTax
```


---

## 3. 날짜 & 시간

** 평균 및 기념일 ** `iconverter://` = 생일 `<ToolItem.rawValue>` , `text` = 참조 날짜.


```
iconverter://tool/ageAnniversary?birth=1990-05-01&ref=2026-05-17
```


** 날짜 Arithmetic ** `iconverter://` = 0 = add/subtract / 1 = 날짜 차이.

add-subtract 모드 ( `iconverter://` = 시작 날짜, `<ToolItem.rawValue>` = ± 일, `text` = ± 주, `input` = ± 개월, `1/true/yes/on` = ± 년) :


```
iconverter://tool/dateArithmetic?mode=0&d1=2026-05-17&d=100
```


차이 모드 ( `iconverter://` = 날짜 1, `<ToolItem.rawValue>` = 날짜 2):


```
iconverter://tool/dateArithmetic?mode=1&d1=2026-01-01&d2=2026-12-31
```


**루어 캘린더 ** `iconverter://` = 그리스 날짜 `<ToolItem.rawValue>` .


```
iconverter://tool/lunarCalendar?date=2026-05-17
```


**Solar Terms ** - 만 개방


```
iconverter://tool/solarTerms
```


** 카운터 다운 ** `iconverter://` = 이벤트 이름, `<ToolItem.rawValue>` = 대상 날짜 `text` , `input` = 포함 시간 `1/true/yes/on` .


```
iconverter://tool/countdown?label=Holiday&target=2026-10-01&time=0
```


** 임신 계산기 ** `iconverter://` = 0 = LMP / 1 = 개념 / 2 = IVF, `<ToolItem.rawValue>` = 참조 날짜, `text` = IVF 배아 일 0 = D3 / 1 = D5.


```
iconverter://tool/pregnancy?method=0&ref=2026-03-01
```



```
iconverter://tool/pregnancy?method=2&ref=2026-03-15&ivf=1
```


** 생리주기 ** `iconverter://` = 마지막 생리 기간 날짜, `<ToolItem.rawValue>` = 주기 일, `text` = 기간 일.


```
iconverter://tool/menstrual?lmp=2026-05-01&cycle=28&period=5
```


** 세계 시계 ** `iconverter://` = 도시 검색 키워드, `<ToolItem.rawValue>` = 사용 현재 시간 `text` , `input` = 사용자 정의 날짜 시간.


```
iconverter://tool/worldClock?q=Tokyo
```



```
iconverter://tool/worldClock?now=0&ref=2026-05-17T20:00:00
```


**Zodiac ** - 만 오픈


```
iconverter://tool/zodiac
```


---

## 4. 수학

** 비율 계산기 ** `iconverter://` = 0–4, `<ToolItem.rawValue>` = 값 A, `text` = 값 B.


```
iconverter://tool/percentage?mode=0&a=75&b=120
```


**Fraction Calculator ** - 만 개방


```
iconverter://tool/fraction
```


**Prime Factorization ** - 만 개방


```
iconverter://tool/primeFactor
```


**Quadratic Solver ** - 만 개방


```
iconverter://tool/quadraticSolver
```


** 통계 ** `iconverter://` = dataset, 공간 / comma / 반콜론에 의해 분리.


```
iconverter://tool/statistics?data=1,2,3,4,5,6,7,8,9,10
```


**조합 및 역 ** — 만 열립니다


```
iconverter://tool/combinations
```


**대칭 ** `iconverter://` = 모양, `<ToolItem.rawValue>` / `text` / `input` = 치수 매개 변수. `iconverter://` · `<ToolItem.rawValue>` · `text` · `input` · `1/true/yes/on` · `0/false/no/off` · `yyyy-MM-dd` · `v` · `from` · `to` · `p` · `r` · `y` · `mode` · `salary` C14 `deduction` 원 ( `iconverter://` = 반경):


```
iconverter://tool/geometry?shape=circle&v1=5
```


Rectangle ( `iconverter://` = 길이, `<ToolItem.rawValue>` = 폭) :


```
iconverter://tool/geometry?shape=rectangle&v1=10&v2=5
```


Sphere ( `iconverter://` = 반경) :


```
iconverter://tool/geometry?shape=sphere&v1=3
```


실린더 ( `iconverter://` = 반경, `<ToolItem.rawValue>` = 높이) :


```
iconverter://tool/geometry?shape=cylinder&v1=4&v2=10
```


---

## 5. 인코딩

**Roman Numeral ** `iconverter://` = 아랍 번호 (1–3999); 또는 `<ToolItem.rawValue>` = 로마 숫자 문자열.


```
iconverter://tool/roman?n=2026
```



```
iconverter://tool/roman?roman=MMXXVI
```


**Base64 인코더 / 암호** `iconverter://` = 인코딩/디코드, `<ToolItem.rawValue>` = URL-안전 모드 `text` , `input` = 입력 텍스트.


```
iconverter://tool/base64?mode=encode&text=Hello%2C+World!
```



```
iconverter://tool/base64?mode=decode&urlSafe=0&text=SGVsbG8sIFdvcmxkIQ%3D%3D
```


**URL 인코더 / 암호** `iconverter://` = encode/decode, `<ToolItem.rawValue>` = 구성 요소 모드 0 = 전체 / 1 = 쿼리 / 2 = 경로, `text` = 입력.


```
iconverter://tool/urlCoder?mode=encode&comp=0&text=https://example.com/path?q=hello world
```



```
iconverter://tool/urlCoder?mode=decode&text=https%3A%2F%2Fexample.com%2F%3Fq%3Dhello%20world
```


** 해시 계산기 ** `iconverter://` = 입력, `<ToolItem.rawValue>` = md5/sha1/sha256/sha512, `text` = uppercase `input` , `1/true/yes/on` = HMAC를 활성화 `0/false/no/off` , `yyyy-MM-dd` = HMAC 키.


```
iconverter://tool/hashing?text=Hello+World&algo=sha256&upper=0
```



```
iconverter://tool/hashing?text=data&algo=md5&hmac=1&key=secret
```


** 워드 카운트 ** `iconverter://` = 분석하는 텍스트.


```
iconverter://tool/wordCount?text=The+quick+brown+fox+jumps+over+the+lazy+dog.
```


** 색상 변환기 ** `iconverter://` = 육색; 또는 `<ToolItem.rawValue>` / `text` / `input` = RGB 구성 요소 (0-255).


```
iconverter://tool/colorConverter?hex=%23FF8800
```



```
iconverter://tool/colorConverter?r=255&g=136&b=0
```


**Color Palette ** - 만 오픈


```
iconverter://tool/colorPalette
```


**QR 코드** `iconverter://` = 내용, `<ToolItem.rawValue>` = `text` 등, `input` = 오류 수정 레벨 `1/true/yes/on` .


```
iconverter://tool/qrcode?text=https%3A%2F%2Fexample.com&ecc=H
```



```
iconverter://tool/qrcode?text=Hello+iConverter&format=qr&ecc=M
```


**JSON 형식 ** `iconverter://` = JSON 문자열 (URL 인코딩), `<ToolItem.rawValue>` = indent space 2/4.


```
iconverter://tool/jsonFormatter?text=%7B%22name%22%3A%22Alice%22%2C%22age%22%3A30%7D&indent=2
```


** 타임 스탬프 ** `iconverter://` = 유닉스 타임스탬프 (둘째), `<ToolItem.rawValue>` = 단위 0 = sec / 1 = ms; 또는 `text` = ISO8601 날짜 문자열.


```
iconverter://tool/timestamp?ts=1747440000
```



```
iconverter://tool/timestamp?iso=2026-05-17T12:00:00
```


** 은행 카드 Validator ** `iconverter://` = 카드 번호.


```
iconverter://tool/bankCard?num=6214830172816734
```


** 텍스트 케이스 변환기 ** `iconverter://` = 입력 텍스트.


```
iconverter://tool/textCase?text=hello+world+from+iConverter
```


**Text Diff** - 만 오픈


```
iconverter://tool/textDiff
```


**HTTP 요청** `iconverter://` = 요청 URL, `<ToolItem.rawValue>` = GET/POST/PUT/PATCH/DELETE, `text` = 요청 본문, `input` = `1/true/yes/on` , `0/false/no/off` = 헤더 JSON.


```
iconverter://tool/httpRequest?url=https%3A%2F%2Fapi.example.com%2Fusers&method=GET
```



```
iconverter://tool/httpRequest?url=https%3A%2F%2Fapi.example.com%2Fusers&method=POST&body=%7B%22name%22%3A%22Alice%22%7D&bodyKind=json
```


** 파일 다운로드 ** `iconverter://` = URL을 다운로드, `<ToolItem.rawValue>` = 파일명 (선택 사항).


```
iconverter://tool/fileDownload?url=https%3A%2F%2Fexample.com%2Freport.pdf&name=report.pdf
```


**HTTP 상태 코드** `iconverter://` = 상태 코드; 또는 `<ToolItem.rawValue>` = 검색 키워드.


```
iconverter://tool/httpStatusCodes?code=404
```



```
iconverter://tool/httpStatusCodes?q=redirect
```


**IP 유틸리티 ** `iconverter://` = subnet/cidr/range, `<ToolItem.rawValue>` = IP 주소, `text` = subnet 가면; 또는 `input` = CIDR 접두사 길이.


```
iconverter://tool/ipUtility?mode=subnet&ip=192.168.1.0&mask=255.255.255.0
```



```
iconverter://tool/ipUtility?ip=10.0.0.0&prefix=24
```


**ASCII 테이블 ** `iconverter://` = 소수점; 또는 `<ToolItem.rawValue>` = hex codepoint; 또는 `text` = 검색.


```
iconverter://tool/asciiTable?dec=65
```



```
iconverter://tool/asciiTable?q=space
```


** 비밀번호 생성기 ** `iconverter://` = length, `<ToolItem.rawValue>` = uppercase `text` , `input` = lowercase `1/true/yes/on` , `0/false/no/off` = digit `yyyy-MM-dd` , `v` = symbol `from` , `to` = noambiguous char `p` , `r` = 즉시 생성    C12.


```
iconverter://tool/passwordGenerator?length=20&upper=1&lower=1&digits=1&symbols=1&unambiguous=1&go=1
```


** 랜덤 번호 생성기 ** `iconverter://` = 최소, `<ToolItem.rawValue>` = 최대, `text` = 카운트, `input` = 소수점 장소, `1/true/yes/on` = 독특 `0/false/no/off` , `yyyy-MM-dd` = 0 = none / 1 = asc / 2 = desc, `v` = 즉시 생성 `from` .


```
iconverter://tool/randomNumber?min=1&max=100&n=10&unique=1&sort=1&go=1
```



```
iconverter://tool/randomNumber?min=0&max=1&n=5&decimals=4&go=1
```


** 위험 코드 ** `iconverter://` = encode/decode, `<ToolItem.rawValue>` = 입력 텍스트.


```
iconverter://tool/morseCode?mode=encode&text=SOS
```



```
iconverter://tool/morseCode?mode=decode&text=...+---+...
```


**JWT 디코더 ** `iconverter://` = JWT 토큰 문자열.


```
iconverter://tool/jwtParser?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c
```


**Cron Expression 파서 ** `iconverter://` = Cron expression (공간은 `<ToolItem.rawValue>` )로 대체 될 수 있습니다.


```
iconverter://tool/cronParser?expr=0+9+*+*+1-5
```



```
iconverter://tool/cronParser?expr=0+0+*+*+*
```


**Regex 테스터 ** `iconverter://` = regex 패턴 (URL 인코딩), `<ToolItem.rawValue>` = 테스트 텍스트, `text` = 교체, `input` = 경우 불균형 `1/true/yes/on` , `0/false/no/off` = 멀티 라인 `yyyy-MM-dd` , `v` = dotall `from` .


```
iconverter://tool/regexTester?pattern=%5Cd%2B&haystack=abc123def456&i=0
```



```
iconverter://tool/regexTester?pattern=%28%5Cw%2B%29&haystack=hello+world&replacement=%5B%241%5D&i=1
```


**웹 브라우저 ** `iconverter://` = 직접 URL을 엽니다; 또는 `<ToolItem.rawValue>` = 검색 쿼리 (기본 검색 엔진 사용).


```
iconverter://tool/webBrowser?url=https%3A%2F%2Fexample.com
```



```
iconverter://tool/webBrowser?q=SwiftUI+deep+link+2026
```


---

## 6. 생활

** BMI 계산기 ** `iconverter://` = 높이 cm, `<ToolItem.rawValue>` = 무게 kg, `text` = 표준 0 = 중국 성인 / 1 = WHO.


```
iconverter://tool/bmi?h=175&w=70&std=0
```


** BMR 계산기 ** `iconverter://` = 높이 cm, `<ToolItem.rawValue>` = 무게 kg, `text` = 나이, `input` = m = 남성 / f = 여성, `1/true/yes/on` = 활동 수준 0–4, `0/false/no/off` = 0 = Harris-Benedict / 1 = Mifflin-St Jeor.


```
iconverter://tool/bmr?h=175&w=70&age=30&sex=m&act=1&formula=1
```


**Clothing Size** - 만 오픈


```
iconverter://tool/clothingSize
```


**Ring Size** - 만 오픈


```
iconverter://tool/ringSize
```


**Height Converter** - 만 열림


```
iconverter://tool/heightConverter
```


** 연료 비용 계산기 ** `iconverter://` = 0 = 미터 / 1 = 제국, `<ToolItem.rawValue>` = 거리, `text` = 100km 당 소비, `input` = 연료 가격, `1/true/yes/on` = 사람들.


```
iconverter://tool/fuelCost?unit=0&d=500&c=8.5&p=7.8&n=1
```


** 배송료 계산기 ** `iconverter://` = 실제 중량 kg, `<ToolItem.rawValue>` = 첫 번째 무게 kg, `text` = 첫 중량 요금, `input` = 단계 무게 kg, `1/true/yes/on` = 단계 요금.


```
iconverter://tool/shippingFee?w=3.5&fw=1&ff=12&sw=1&sf=8
```


부피 측정 무게 ( `iconverter://` = 활성화 `<ToolItem.rawValue>` , `text` / `input` / `1/true/yes/on` = 세면 cm, `0/false/no/off` = 디바이저):


```
iconverter://tool/shippingFee?w=2&vol=1&l=50&wd=40&h=30&div=6000&fw=1&ff=12&sw=1&sf=8
```


** 혈액 알코올 함량 (BAC) ** `iconverter://` = m = 남성 / f = 여성, `<ToolItem.rawValue>` = 체중 kg, `text` = 볼륨 mL, `input` = ABV %, `1/true/yes/on` = 술 이후 시간.


```
iconverter://tool/alcoholBac?sex=m&w=70&v=500&abv=5&h=0.5
```


**관련** `iconverter://` = 관계 체인 (comma-separated), `<ToolItem.rawValue>` = 고 성 0 = 남성 / 1 = 여성, `text` = 쇼 반전 `input` .


```
iconverter://tool/relationship?chain=f,os&sex=0&reverse=1
```



```
iconverter://tool/relationship?chain=m,ob&sex=1&reverse=0
```


**ID 카드 파서 ** `iconverter://` = ID 카드 번호.


```
iconverter://tool/idCard?id=110101199003073010
```


** 코인 플립 ** - 만 개방


```
iconverter://tool/coinFlip
```


**Dice Roller ** - 만 개방


```
iconverter://tool/diceRoller
```


**Random Draw ** - 만 열립니다


```
iconverter://tool/randomDraw
```


** 스핀들 휠 ** - 만 개방


```
iconverter://tool/spinWheel
```


**비디오 프레임 내보내기 ** — 만 엽니 다


```
iconverter://tool/videoFrameExport
```


---

## 7. 감지기

**컴패스 ** — 만 오픈


```
iconverter://tool/compass
```


**Level** - 만 오픈


```
iconverter://tool/level
```


**Altitude** - 만 개방


```
iconverter://tool/altitude
```


---

## 8. 중국

**중국 ** `iconverter://` = 번호.


```
iconverter://tool/chineseNumber?n=12345.67
```


**중국 번호 역 ** `iconverter://` = 중국어 간체 문자열.


```
iconverter://tool/chineseNumberReverse?text=一万二千三百四十五
```


** 금융 금액 ** `iconverter://` = 금액, `<ToolItem.rawValue>` = append lodge `text` .


```
iconverter://tool/financialAmount?amount=12345.67&zheng=1
```


---

## 9. 단위 변환기

일반 형식 : `iconverter://` = 값, `<ToolItem.rawValue>` = 소스 단위 (rawValue 또는 기호, case-insensitive), `text` = 대상 단위.

---

** 길이**
일반 단위 : `iconverter://` (m) · `<ToolItem.rawValue>` (km) · `text` (cm) · `input` (mm) · `1/true/yes/on` (ft) · `0/false/no/off` (in) · `yyyy-MM-dd` (mi) · `v` (yd) · `from` (nmi) · `to` (里) `to` (里) `p` (C10)


```
iconverter://tool/length?v=100&from=meter&to=foot
```



```
iconverter://tool/length?v=1&from=mile&to=kilometer
```


**아레**
일반 단위 : `iconverter://` (m2) · `<ToolItem.rawValue>` (하) · `text` (에이커) · `input` (ft2) · `1/true/yes/on` (마일2) · `0/false/no/off` ()) · `yyyy-MM-dd` (km2).


```
iconverter://tool/area?v=1&from=hectare&to=mu
```



```
iconverter://tool/area?v=1&from=acre&to=squareMeter
```


** 볼륨**
일반 단위 : `iconverter://` (L) · `<ToolItem.rawValue>` (mL) · `text` (m3) · `input` (gal) · `1/true/yes/on` (fl oz) · `0/false/no/off` (cup) · `yyyy-MM-dd` (gal UK) · `v` (bbl).


```
iconverter://tool/volume?v=1&from=gallon&to=liter
```



```
iconverter://tool/volume?v=355&from=milliliter&to=fluidOunce
```


** 무게 / 질량 **
일반 단위 : `iconverter://` (kg) · `<ToolItem.rawValue>` (g) · `text` (lb) · `input` (oz) · `1/true/yes/on` (t) · `0/false/no/off` (火) · `yyyy-MM-dd` (火) · `v` (ct).


```
iconverter://tool/weight?v=1&from=pound&to=kilogram
```



```
iconverter://tool/weight?v=1&from=jin&to=gram
```


** 온도**
단위 : `iconverter://` (°C) · `<ToolItem.rawValue>` (°F) · `text` (K) · `input` (°R) · `1/true/yes/on` (°Re).


```
iconverter://tool/temperature?v=100&from=celsius&to=fahrenheit
```



```
iconverter://tool/temperature?v=37&from=celsius&to=kelvin
```


**시간**
일반 단위 : `iconverter://` (s) · `<ToolItem.rawValue>` (분) · `text` (h) · `input` (일) · `1/true/yes/on` (wk) · `0/false/no/off` (mo) · `yyyy-MM-dd` (일) · `v` (ms) · `from` (μs).


```
iconverter://tool/time?v=1&from=hour&to=second
```



```
iconverter://tool/time?v=7&from=day&to=hour
```


** 속도**
단위: `iconverter://` (m/s) · `<ToolItem.rawValue>` (km/h) · `text` (mph) · `input` (kn) · `1/true/yes/on` (Ma).


```
iconverter://tool/speed?v=100&from=kmPerHour&to=milePerHour
```



```
iconverter://tool/speed?v=1&from=mach&to=meterPerSecond
```


**압력**
단위 : `iconverter://` (Pa) · `<ToolItem.rawValue>` (kPa) · `text` (bar) · `input` (atm) · `1/true/yes/on` (psi) · `0/false/no/off` (mmHg).


```
iconverter://tool/pressure?v=1&from=atmosphere&to=kilopascal
```



```
iconverter://tool/pressure?v=120&from=mmHg&to=kilopascal
```


** 에너지 **
단위 : `iconverter://` (J) · `<ToolItem.rawValue>` (kJ) · `text` (칼) · `input` (kcal) · `1/true/yes/on` (kWh) · `0/false/no/off` (BTU).


```
iconverter://tool/energy?v=1&from=kilowattHour&to=kilojoule
```



```
iconverter://tool/energy?v=500&from=kilocalorie&to=kilojoule
```


** 파워 **
단위: `iconverter://` (W) · `<ToolItem.rawValue>` (kW) · `text` (hp) · `input` (PS) · `1/true/yes/on` (BTU/h).


```
iconverter://tool/power?v=1&from=hpMechanical&to=kilowatt
```



```
iconverter://tool/power?v=3000&from=watt&to=hpMetric
```


**포스 **
단위 : `iconverter://` (N) · `<ToolItem.rawValue>` (kN) · `text` (kgf) · `input` (lbf) · `1/true/yes/on` (dyn).


```
iconverter://tool/force?v=9.8&from=newton&to=kgf
```



```
iconverter://tool/force?v=1&from=kilonewton&to=lbf
```


** 터키 **
단위 : `iconverter://` (N·m) · `<ToolItem.rawValue>` (N·cm) · `text` (kgf·m) · `input` (ft·lb) · `1/true/yes/on` (in·lb).


```
iconverter://tool/torque?v=100&from=newtonMeter&to=footPound
```


** 주파수 **
단위: `iconverter://` (Hz) · `<ToolItem.rawValue>` (kHz) · `text` (MHz) · `input` (GHz) · `1/true/yes/on` (THz) · `0/false/no/off` (rpm).


```
iconverter://tool/frequency?v=2.4&from=gigahertz&to=megahertz
```



```
iconverter://tool/frequency?v=3000&from=rpm&to=hertz
```


**안글**
단위 : `iconverter://` (°) · `<ToolItem.rawValue>` (rad) · `text` (grad) · `input` (') · `1/true/yes/on` (") · `0/false/no/off` (턴).


```
iconverter://tool/angle?v=180&from=degree&to=radian
```



```
iconverter://tool/angle?v=1&from=turn&to=degree
```


** 데이터 저장 **
단위 : `iconverter://` (B) · `<ToolItem.rawValue>` (KB) · `text` (MB) · `input` (GB) · `1/true/yes/on` (TB) · `0/false/no/off` (KiB) · `yyyy-MM-dd` (MiB) · `v` (GiB).


```
iconverter://tool/dataStorage?v=1&from=gigabyte&to=mebibyte
```



```
iconverter://tool/dataStorage?v=512&from=mebibyte&to=gigabyte
```


**데이터 비율**
단위 : `iconverter://` (bps) · `<ToolItem.rawValue>` (Kbps) · `text` (Mbps) · `input` (Gbps) · `1/true/yes/on` (KB/s) · `0/false/no/off` (MB/s) · `yyyy-MM-dd` (GB/s).


```
iconverter://tool/dataRate?v=100&from=mbps&to=mBps
```



```
iconverter://tool/dataRate?v=1&from=gbps&to=mbps
```


**임금 **
단위 : `iconverter://` (lx) · `<ToolItem.rawValue>` (fc) · `text` (ph) · `input` (nx).


```
iconverter://tool/illuminance?v=500&from=lux&to=footCandle
```


**Magnetic Flux 밀도 **
단위 : `iconverter://` (T) · `<ToolItem.rawValue>` (mT) · `text` (μT) · `input` (G) · `1/true/yes/on` (mG).


```
iconverter://tool/magneticFlux?v=1&from=tesla&to=gauss
```


** 라디오 **
단위 : `iconverter://` (Bq) · `<ToolItem.rawValue>` (kBq) · `text` (MBq) · `input` (Ci) · `1/true/yes/on` (mCi) · `0/false/no/off` (μCi).


```
iconverter://tool/radioactivity?v=1&from=curie&to=megabecquerel
```


** 점성 **
단위 : `iconverter://` (Pa·s) · `<ToolItem.rawValue>` (mPa·s) · `text` (P) · `input` (cP).


```
iconverter://tool/viscosity?v=1&from=pascalSecond&to=centipoise
```


** 연료 경제 **
단위: `iconverter://` (L/100km) · `<ToolItem.rawValue>` (km/L) · `text` (MPG 미국) · `input` (MPG 영국).


```
iconverter://tool/fuelEconomy?v=8.5&from=lPer100km&to=kmPerL
```



```
iconverter://tool/fuelEconomy?v=30&from=mpgUS&to=lPer100km
```


**요금**
단위 : `iconverter://` (m3/s) · `<ToolItem.rawValue>` (m3/h) · `text` (L/s) · `input` (L/min) · `1/true/yes/on` (L/h) · `0/false/no/off` (gpm US) · `yyyy-MM-dd` (cfm).


```
iconverter://tool/flowRate?v=1&from=literPerMinute&to=cubicMeterPerHour
```


** 밀도 **
단위: `iconverter://` (kg/m3) · `<ToolItem.rawValue>` (g/cm3) · `text` (g/L) · `input` (kg/L) · `1/true/yes/on` (lb/ft3).


```
iconverter://tool/density?v=1&from=gramPerCubicCentimeter&to=kgPerCubicMeter
```


**매틱 플럭스 (Wb) **
단위 : `iconverter://` (Wb) · `<ToolItem.rawValue>` (mWb) · `text` (μWb) · `input` (kWb) · `1/true/yes/on` (Mx).


```
iconverter://tool/magneticFluxTrue?v=1&from=weber&to=maxwell
```


**침실 **
단위 : `iconverter://` (Gy) · `<ToolItem.rawValue>` (mGy) · `text` (μGy) · `input` (kGy) · `1/true/yes/on` (rad) · `0/false/no/off` (mrad).


```
iconverter://tool/absorbedDose?v=1&from=gray&to=rad
```


**유효한 복용량 **
단위 : `iconverter://` (Sv) · `<ToolItem.rawValue>` (mSv) · `text` (μSv) · `input` (rem) · `1/true/yes/on` (mrem).


```
iconverter://tool/equivalentDose?v=1&from=sievert&to=rem
```



```
iconverter://tool/equivalentDose?v=20&from=millisievert&to=microsievert
```


** 물질의 금액 **
단위 : `iconverter://` (mol) · `<ToolItem.rawValue>` (mmol) · `text` (μmol) · `input` (kmol) · `1/true/yes/on` (nmol) · `0/false/no/off` (pmol).


```
iconverter://tool/amountOfSubstance?v=1&from=mole&to=millimole
```



```
iconverter://tool/amountOfSubstance?v=150&from=millimole&to=micromole
```


---

[Back to iConverter Support](../) &middot; [FAQ](../faq) &middot; [개인정보 보호 정책](../privacy)

</section>
<section lang="ru" markdown="1">

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

</section>
<section lang="th" markdown="1">

ICverter รองรับ `iconverter://` BAR  ที่อยู่ URL วางรูปแบบลิงก์ลึก ๆ — เปิดเครื่องมือ 101 เครื่อง จากโปรแกรมภายนอก, หน้าเว็บ, QR รหัส (หลัก หรือ ~scan in-app~) Sarfari หรือ ปุ่มพิมพ์ลัดแอปเปิล, เลือกเพิ่มหน้าช่องป้อนข้อมูลก่อนเติมข้อมูลผ่านทางพารามิเตอร์การค้นหา

> ~คําเตือน: ~ The Launcher ~ เครื่องมือเลือกวิดเจ็ตรวมถึงเครื่องมือที่รองรับทั้งหมด ยกเว้น ~เว็บเบราว์เซอร์~ การปรับแต่งวิดเจ็ต UI ตามด้วยภาษาระบบ ~, ไม่ใช่การแทนที่ภาษาในโปรแกรมที่อยู่ใต้การตั้งค่า

## การกําหนดโพรโทคอล


```
iconverter://tool/<ToolItem.rawValue>?key=value&key2=value2
```


- Urnknown=======. สืบค้นเมื่อ:
- ชื่อพาราเมตรรองรับทั้งปุ่มสั้นและข้อความกํากับ (เช่น `ข้อความ' นั้นเทียบเท่ากับ 'input')
- Booleans: '1/ True/es/on' true; 02/false/no/off' False
- วันที่: รองรับ 'yyy-M- dd', ISO8601, Unix timetamp (วินาที).
- ตัวแปลงหน่วยมีรูปแบบร่วมกัน: 'v' = ค่า, 'จาก' = หน่วยต้นทาง (หรือสัญลักษณ์, เคสอินไดเรกชันต์), 'to' = หน่วยเป้าหมาย

---

## 1. เครื่องคิดเลข

~นักบิน ~ — เปิดเท่านั้น~


```
iconverter://tool/calculator
```


** เครื่องคิดเลขแบบวิทยาศาสตร์ ** — เปิดได้อย่างเดียว *


```
iconverter://tool/scientific
```


** เครื่องคิดเลข ** — เปิดได้เท่านั้น


```
iconverter://tool/programmer
```


---

## 2.

** เครื่องคิดเลข # `iconverter://` BAR  =ปริมาณเงินกู้ `<ToolItem.rawValue>` =อัตรารายปี% c2  =ปี  BAR `input` / = 0 =ระยะเยื้องเท่ากับ 1/1 =หลัก


```
iconverter://tool/mortgage?p=1000000&r=3.7&y=30&mode=0
```


~ภาษีที่เข้ามา~ `iconverter://` BAR  =เงินเดือนรายเดือน  BAR `<ToolItem.rawValue>` =ประกันสังคม   c2      =ค่าชดเชยพิเศษ, `input` =ค่าชดเชย,  BAR ค่าชดเชย, `1/true/yes/on` =โบนัสประจําปี


```
iconverter://tool/incomeTax?salary=20000&insurance=3000&deduction=1000&threshold=5000&bonus=50000
```


** สนใจมาก* `iconverter://` BAR - =หลัก BAR `<ToolItem.rawValue>` BAR  =การบริจาครายเดือน `text` r=อัตรารายปี%,  c3 s s s s s  BAR ปี, `1/true/yes/on` s=0/0 =รายเดือน/1 =รายเดือน/2 =รายวัน, c5    BAR     BAR     BAR     BAR    BAR    BAR          BAR      BAR   // BAR BAR  ///0 = 0 = 0/0 = 0 ปี/0/0/0 =รายเดือน/1/1/1/1 / 2 =รายเดือน / 2 =วัน/วัน/2 วัน, รายวัน, วัน,      BAR          BAR   BAR                          BAR  BAR


```
iconverter://tool/compoundInterest?p=100000&m=1000&r=7&y=10&freq=1
```


** เครื่องคิดเลข ~ `iconverter://` BAR = 0-14  BAR `<ToolItem.rawValue>` r=ราคาเดิม, c2    = discount อัตราส่วน,  c3    / = ขีดจํากัด, c4     =ปริมาณ


```
iconverter://tool/discount?mode=0&p=299&r=8.5
```


ตัวอย่างเต็มลบ:


```
iconverter://tool/discount?mode=3&p=350&t=300&u=50
```


~และแยก AA~ `iconverter://` BAR  =เคล็ดลับ /1 = เคล็ดลับ /1 = AA (AA) `<ToolItem.rawValue>` = บิล,  c2 s=เคล็ดลับ%,   BAR `input` =ภาษี%, `input` =ภาษี%, `1/true/yes/on` =นับคน.


```
iconverter://tool/tipAA?mode=0&bill=200&tip=15&tax=0&ppl=4
```


~เงินจ่ายล่วงหน้า~ `iconverter://` s    =เงินกู้เดิม `<ToolItem.rawValue>` =อัตรารายปี% c2    BAR เทอมรวม (ค.ศ.


```
iconverter://tool/mortgagePrepay?p=800000&r=3.7&total=30&paid=5&prepay=100000&mode=2
```


~ภาษีที่แท้จริง ~ — เปิดเท่านั้น~


```
iconverter://tool/realEstateTax
```


---

## 3. วันที่และเวลา

~และวันครบรอบ~ `iconverter://` BAR  =วันเกิด BAR `<ToolItem.rawValue>` BAR =วันที่อ้างอิง


```
iconverter://tool/ageAnniversary?birth=1990-05-01&ref=2026-05-17
```


~"อาริทเมติก~ `iconverter://` =0 = เพิ่ม/ย่อย 1 =ความแตกต่างของวันที่

โหมดการเพิ่มข้อมูล ( `iconverter://` BAR  =วันเริ่มต้น, `<ToolItem.rawValue>` =วัน,  c2     =สัปดาห์,   c3  =เดือน/เดือน `1/true/yes/on` =ปี:


```
iconverter://tool/dateArithmetic?mode=0&d1=2026-05-17&d=100
```


โหมดความแตกต่าง ( `iconverter://` BAR  =วันที่ 1, `<ToolItem.rawValue>` =วันที่ 2):


```
iconverter://tool/dateArithmetic?mode=1&d1=2026-01-01&d2=2026-12-31
```


~ปฏิทิน~ `iconverter://` BAR  =วันที่ Gregorian `<ToolItem.rawValue>` BAR


```
iconverter://tool/lunarCalendar?date=2026-05-17
```


♪ sular valts ♪ — เปิดเท่านั้น ♪


```
iconverter://tool/solarTerms
```


~ก้มลง~ `iconverter://` BAR ชื่อเหตุการณ์, BAR `<ToolItem.rawValue>` =วันที่เป้าหมาย   c2                  /3  =เวลารวม  BAR `1/true/yes/on` BAR         BAR   /     /  BAR     BAR                         ///  /     /  /  /  /  / /     /     /                     ก็รวมเวลา รวมเวลา รวมเวลา รวมเวลา รวมเวลา รวมเวลา รวมเวลาด้วยเวลาด้วย เวลาด้วย เวลาด้วย


```
iconverter://tool/countdown?label=Holiday&target=2026-10-01&time=0
```


** เครื่องคิดเลข ** `iconverter://` BAR  = 0 = LMP / 1 = ตั้งครรภ์ / 2 = IVF `<ToolItem.rawValue>` =วันที่อ้างอิง, `text` =วันที่ตัวอ่อน IVF 0 = D3 / 1 = D5


```
iconverter://tool/pregnancy?method=0&ref=2026-03-01
```



```
iconverter://tool/pregnancy?method=2&ref=2026-03-15&ivf=1
```


~ วัฏจักรทางประสาท~ `iconverter://` BAR  =วันที่เดือนสุดท้าย BAR `<ToolItem.rawValue>` BAR  =วันวน, `text` =ช่วงเวลา


```
iconverter://tool/menstrual?lmp=2026-05-01&cycle=28&period=5
```


~นาฬิกาโลก~ `iconverter://` BAR  =กุญแจค้นตัวเมือง, `<ToolItem.rawValue>` =ใช้เวลาปัจจุบัน `text` /C3  =วันที่กําหนดเอง


```
iconverter://tool/worldClock?q=Tokyo
```



```
iconverter://tool/worldClock?now=0&ref=2026-05-17T20:00:00
```


~ซัคคิวบัส เปิดได้อย่างเดียว~


```
iconverter://tool/zodiac
```


---

## 4. คณิตศาสตร์

** เครื่องคิดเลข ** `iconverter://` BAR  = 0-14  BAR `<ToolItem.rawValue>` =ค่า A `text` =ค่า B


```
iconverter://tool/percentage?mode=0&a=75&b=120
```


** เครื่องคิดเลขกระทํา ** — เปิดเท่านั้น


```
iconverter://tool/fraction
```


~Prime Pactization ~ — open เท่านั้น


```
iconverter://tool/primeFactor
```


~ตัวแก้ปัญหาของ Quadratic ~ เปิดได้อย่างเดียว~


```
iconverter://tool/quadraticSolver
```


~สถิติ~
ค.ศ.


```
iconverter://tool/statistics?data=1,2,3,4,5,6,7,8,9,10
```


** การควบรวมและการก่อความไม่สงบ* — เปิดเท่านั้น


```
iconverter://tool/combinations
```


~โอ้~ `iconverter://` BAR  =รูปร่าง, `<ToolItem.rawValue>` C2       /C3 =ตัวแปรมิติ

รูปทรงที่มีอยู่:  c0     BAR `<ToolItem.rawValue>` C3                                                                                                                      /

วงกลม ( `iconverter://` =รัศมี):


```
iconverter://tool/geometry?shape=circle&v1=5
```


สี่เหลี่ยม ( `iconverter://` BAR  =ความยาว, `<ToolItem.rawValue>` BAR  =ความกว้าง):


```
iconverter://tool/geometry?shape=rectangle&v1=10&v2=5
```


sphere ( `iconverter://` =รัศมี):


```
iconverter://tool/geometry?shape=sphere&v1=3
```


ซิลเดอร์ ( `iconverter://` =รัศมี, `<ToolItem.rawValue>` =ความสูง):


```
iconverter://tool/geometry?shape=cylinder&v1=4&v2=10
```


---

## 5 การเข้ารหัส

♪ ค่ําคืนอันยาวนาน ♪ `iconverter://` BAR  =เลขอารบิก (1–3991); หรือ `<ToolItem.rawValue>` =ข้อความตัวเลขโรมัน


```
iconverter://tool/roman?n=2026
```



```
iconverter://tool/roman?roman=MMXXVI
```


** ตัวเข้ารหัส/ ตัวถอดรหัส ** `iconverter://` BAR  =การเข้ารหัส/ Decode,   c1    =รูปแบบที่อยู่ URL-ปลอดภัย c2                             /C3  =ข้อความนําเข้า


```
iconverter://tool/base64?mode=encode&text=Hello%2C+World!
```



```
iconverter://tool/base64?mode=decode&urlSafe=0&text=SGVsbG8sIFdvcmxkIQ%3D%3D
```


~นักเข้ารหัส/ นักถอดรหัส~ `iconverter://` BAR  =การเข้ารหัส/ Decode,   c1   =โหมดองค์ประกอบ 0 =เต็ม / 1 =การค้นหา / 2 =เส้นทาง, `text` =การป้อนข้อมูล


```
iconverter://tool/urlCoder?mode=encode&comp=0&text=https://example.com/path?q=hello world
```



```
iconverter://tool/urlCoder?mode=decode&text=https%3A%2F%2Fexample.com%2F%3Fq%3Dhello%20world
```


** เครื่องคิดเลข ** `iconverter://` BAR  =การป้อนข้อมูล, `<ToolItem.rawValue>` = md5/shan1/chas256/ha512, c2    =อักษรพิมพ์ใหญ่   /C3                /C4 =เปิด HMAC C C  C                       /C        /C    /C  BAR      BAR คีย์


```
iconverter://tool/hashing?text=Hello+World&algo=sha256&upper=0
```



```
iconverter://tool/hashing?text=data&algo=md5&hmac=1&key=secret
```


~นับวัน~ `iconverter://` =ข้อความที่จะวิเคราะห์


```
iconverter://tool/wordCount?text=The+quick+brown+fox+jumps+over+the+lazy+dog.
```


** ตัวแปลงสี ** `iconverter://` =เฮ็กซ์สี หรือ `<ToolItem.rawValue>` C2 `input` =ส่วนประกอบ RGB (0-155).


```
iconverter://tool/colorConverter?hex=%23FF8800
```



```
iconverter://tool/colorConverter?r=255&g=136&b=0
```


♪จานสีน้ําเงิน -- เปิดเท่านั้น ♪


```
iconverter://tool/colorPalette
```


~~~~~~ ~รหัส~ `iconverter://` / =เนื้อหา, `<ToolItem.rawValue>` อื่น          /  =ระดับการแก้ไขผิดพลาด `1/true/yes/on` )


```
iconverter://tool/qrcode?text=https%3A%2F%2Fexample.com&ecc=H
```



```
iconverter://tool/qrcode?text=Hello+iConverter&format=qr&ecc=M
```


~รองเท้าสไตล์ของเจสัน~ `iconverter://` =ข้อความ Json (URL-encoded), `<ToolItem.rawValue>` =ช่องว่าง indent 2/4.


```
iconverter://tool/jsonFormatter?text=%7B%22name%22%3A%22Alice%22%2C%22age%22%3A30%7D&indent=2
```


~เวลา~ `iconverter://` BAR = Unix timetamp (วินาที),  c1   =หน่วย 0 =วินาที/1 = ms; หรือ `text` =ข้อความวันที่ ISO8601


```
iconverter://tool/timestamp?ts=1747440000
```



```
iconverter://tool/timestamp?iso=2026-05-17T12:00:00
```


~เครื่องตรวจความถูกต้องของการ์ด~ `iconverter://` =หมายเลขบัตร


```
iconverter://tool/bankCard?num=6214830172816734
```


** ตัวแปลงตัวพิมพ์เล็ก- ใหญ่* `iconverter://` =ข้อความนําเข้า


```
iconverter://tool/textCase?text=hello+world+from+iConverter
```


** เปิดเฉพาะเครื่อง **


```
iconverter://tool/textDiff
```


~ `iconverter://` BAR =ที่อยู่ URL ที่ร้องขอ , `<ToolItem.rawValue>` = get/POST/PUT/PAT/PATCH/DELETE,    c2    BAR ร้องขอร่างกาย, c3  s= `1/true/yes/on` /C5    = header Json


```
iconverter://tool/httpRequest?url=https%3A%2F%2Fapi.example.com%2Fusers&method=GET
```



```
iconverter://tool/httpRequest?url=https%3A%2F%2Fapi.example.com%2Fusers&method=POST&body=%7B%22name%22%3A%22Alice%22%7D&bodyKind=json
```


** ดาวน์โหลดแฟ้ม ** `iconverter://` =ที่อยู่ URL ที่ดาวน์โหลด, `<ToolItem.rawValue>` =ชื่อแฟ้ม (ตัวเลือก)


```
iconverter://tool/fileDownload?url=https%3A%2F%2Fexample.com%2Freport.pdf&name=report.pdf
```


** รหัสสถานะ HTP ** `iconverter://` /  =รหัสสถานะ หรือ `<ToolItem.rawValue>` =กุญแจค้นหา


```
iconverter://tool/httpStatusCodes?code=404
```



```
iconverter://tool/httpStatusCodes?q=redirect
```


~Officity~ `iconverter://` BAR = ซับเน็ต/ซิดเด้อ, `<ToolItem.rawValue>` =ที่อยู่ IP, `text` =หน้ากากซับเน็ต, หรือ `input` =ความยาวนําหน้า CIDR


```
iconverter://tool/ipUtility?mode=subnet&ip=192.168.1.0&mask=255.255.255.0
```



```
iconverter://tool/ipUtility?ip=10.0.0.0&prefix=24
```


~โต๊ะ~ `iconverter://` =จุดเคานต์ทศนิยม หรือ `<ToolItem.rawValue>` =เลขฐานสิบหก


```
iconverter://tool/asciiTable?dec=65
```



```
iconverter://tool/asciiTable?q=space
```


** เครื่องกําเนิดแสง~ `iconverter://` /            /          /     BAR                           BAR           BAR     BAR           BAR                     BAR        BAR


```
iconverter://tool/passwordGenerator?length=20&upper=1&lower=1&digits=1&symbols=1&unambiguous=1&go=1
```


~เครื่องหมายเลข Random~ `iconverter://` BAR น้อย= `<ToolItem.rawValue>` BAR - =สูงสุด          BAR จํานวน    BAR   BAR              BAR       BAR                                                                      สมพล= 1 = 1 /1 = 1 //C2 = 1 //C2/c= de   BAR                                                  BAR


```
iconverter://tool/randomNumber?min=1&max=100&n=10&unique=1&sort=1&go=1
```



```
iconverter://tool/randomNumber?min=0&max=1&n=5&decimals=4&go=1
```


~รหัสลม~ `iconverter://` BAR  =การเข้ารหัส/ Decode, `<ToolItem.rawValue>` =ข้อความนําเข้า


```
iconverter://tool/morseCode?mode=encode&text=SOS
```



```
iconverter://tool/morseCode?mode=decode&text=...+---+...
```


~JWT ถอดรหัส~ `iconverter://` =ข้อความสัญลักษณ์ JWT


```
iconverter://tool/jwtParser?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c
```


~Cron expresser~ `iconverter://` =นิพจน์ Cron (สามารถแทนได้)


```
iconverter://tool/cronParser?expr=0+9+*+*+1-5
```



```
iconverter://tool/cronParser?expr=0+0+*+*+*
```


~ ทดสอบอีกครั้ง~ `iconverter://` BAR  =รูปแบบ regric ex (URL-encoded) `<ToolItem.rawValue>` =ข้อความทดสอบ,  c2   s=ตัวแทน,  BAR `input` /deni                                   BAR     BAR     BAR    BAR   BAR   BAR       BAR   BAR   BAR BAR BAR BAR BAR //////////////   BAR                                         BAR                 BAR BAR BAR BAR


```
iconverter://tool/regexTester?pattern=%5Cd%2B&haystack=abc123def456&i=0
```



```
iconverter://tool/regexTester?pattern=%28%5Cw%2B%29&haystack=hello+world&replacement=%5B%241%5D&i=1
```


~เว็บเบราว์เซอร์~ `iconverter://` =ที่อยู่ URL เปิดโดยตรง หรือ `<ToolItem.rawValue>` =การค้นหา (ใช้กลไกการค้นหาปริยาย)


```
iconverter://tool/webBrowser?url=https%3A%2F%2Fexample.com
```



```
iconverter://tool/webBrowser?q=SwiftUI+deep+link+2026
```


---

## 6 ไลฟ์สไตล์

** เครื่องคิดเลข ~ `iconverter://` BAR  =ความสูง cmm, c1   =น้ําหนัก kg, c2     =มาตรฐาน 0=ผู้ใหญ่ชาวจีน / 1 = WHO


```
iconverter://tool/bmi?h=175&w=70&std=0
```


** เครื่องคิดเลข ** `iconverter://` =ความสูง Cml, c1     =น้ําหนัก kg,   c2       =อายุ, c3        =เพศชาย/d= f/f=ผู้หญิง,  c4  BAR   BAR                                       BAR    BAR        BAR    BAR    BAR     BAR  //// BAR    ///// BAR       BAR        BAR      BAR        BAR          BAR BAR   BAR BAR  BAR BAR BAR                         –ร่ร่


```
iconverter://tool/bmr?h=175&w=70&age=30&sex=m&act=1&formula=1
```


~ กว้างมาก~ — เปิดเท่านั้น


```
iconverter://tool/clothingSize
```


<i>"ขนาด"-เปิดเท่านั้น"


```
iconverter://tool/ringSize
```


** ตัวแปลงพลังงาน ** — เปิดเท่านั้น **


```
iconverter://tool/heightConverter
```


** เครื่องคิดเลข - **
c0             = 0 = เมทริก / 1 = จักรวรรดิ, `<ToolItem.rawValue>` =ระยะทาง,   c2    =การบริโภคต่อ 100 km,   c3     =ราคาเชื้อเพลิง, c4 s =คน.


```
iconverter://tool/fuelCost?unit=0&d=500&c=8.5&p=7.8&n=1
```


** จิบ เครื่องคิดเลข ** `iconverter://` BAR  =น้ําหนักจริง kgg,   c1     =น้ําหนัก 1 กิโลกรัม,  c2     BAR  =ค่าน้ํา หนัก 1 ปอนด์, c3   =น้ําหนักขั้น kgg, c4 s=ค่าธรรมเนียมขั้น.


```
iconverter://tool/shippingFee?w=3.5&fw=1&ff=12&sw=1&sf=8
```


ด้วยน้ําหนักปริมาตร ( `iconverter://` BAR  =การเปิดไ BAR `<ToolItem.rawValue>` C2                      /C4   =ด้าน 3 ซม. `0/false/no/off` =เนื้อร้อง:


```
iconverter://tool/shippingFee?w=2&vol=1&l=50&wd=40&h=30&div=6000&fw=1&ff=12&sw=1&sf=8
```


# การดื่มแอลกอฮอล์ตาย (BAC) ~
c0                    = m = en/f = ผู้หญิง, `<ToolItem.rawValue>` =น้ําหนัก kg,           =ปริมาตร mL,   c3                 /V%,                                   /     /     /              /                 .


```
iconverter://tool/alcoholBac?sex=m&w=70&v=500&abv=5&h=0.5
```


~ความสัมพันธ์~ `iconverter://` s    =ห่วงโซ่ความสัมพันธ์ (comma-kried),  c1  =อัตตา เซ็กซ์ 0 =เพศชาย / 1 =ผู้หญิง,          =แสดงย้อนกลับ `input` ```
iconverter://tool/relationship?chain=f,os&sex=0&reverse=1
```



```
iconverter://tool/relationship?chain=m,ob&sex=1&reverse=0
```


~D ไพ่พาร์เซอร์~ `iconverter://` m =เลขประจําตัว


```
iconverter://tool/idCard?id=110101199003073010
```


~เปิดแต่... ~


```
iconverter://tool/coinFlip
```


♪ โรลเลอร์ ♪ — เปิดเท่านั้น ♪


```
iconverter://tool/diceRoller
```


~Random วาด ~ — เปิดเท่านั้น~


```
iconverter://tool/randomDraw
```


♪ เปิดเพียง ♪


```
iconverter://tool/spinWheel
```


~ ภาพวิดีโอส่งออก~ — เปิดเท่านั้น


```
iconverter://tool/videoFrameExport
```


---

## ตัวตรวจจับ 7.

~เส้นทาง ~ — เปิดเท่านั้น~


```
iconverter://tool/compass
```


~Levil ~ — เปิดเท่านั้น~


```
iconverter://tool/level
```


** เปิดเท่านั้น **


```
iconverter://tool/altitude
```


---

## 8 ภาษาจีน

~หมายเลขเครื่อง~ `iconverter://` BAR  =หมายเลข


```
iconverter://tool/chineseNumber?n=12345.67
```


~ตัวเลขกลับกัน~
ค.ศ.


```
iconverter://tool/chineseNumberReverse?text=一万二千三百四十五
```


~ยอดเขา~ `iconverter://` BAR  =ปริมาณ, `<ToolItem.rawValue>` = instand 整 c2       .


```
iconverter://tool/financialAmount?amount=12345.67&zheng=1
```


---

## 9 หน่วยแปลง

รูปแบบทั่วไป: `iconverter://` =ค่า, `<ToolItem.rawValue>` =หน่วยแหล่งกําเนิด (ravue หรือสัญลักษณ์, obs-in/consient), `text` =หน่วยเป้าหมาย

---

~! ~
หน่วยรวม:  c2 s c0  BAR  m  BAR `<ToolItem.rawValue>` BAR


```
iconverter://tool/length?v=100&from=meter&to=foot
```



```
iconverter://tool/length?v=1&from=mile&to=kilometer
```


~~~~
หน่วยรวม:   c0       BAR  m2 m2 c1    BAR H c2   BAR   BAR `input` BAR            BAR                           BAR      BAR     BAR     BAR   BAR    BAR    BAR       BAR     BAR     BAR      BAR           BAR        BAR          BAR


```
iconverter://tool/area?v=1&from=hectare&to=mu
```



```
iconverter://tool/area?v=1&from=acre&to=squareMeter
```


~วูซูเมะ~
หน่วยรวม: `iconverter://` BAR    BAR `<ToolItem.rawValue>` BAR    BAR   BAR   BAR    BAR   BAR   BAR   BAR   BAR   BAR    BAR    BAR    BAR    BAR     BAR     BAR   BAR    BAR   BAR    BAR    BAR    BAR  BAR  BAR     BAR     BAR       BAR        BAR        BAR                 BAR                  BAR


```
iconverter://tool/volume?v=1&from=gallon&to=liter
```



```
iconverter://tool/volume?v=355&from=milliliter&to=fluidOunce
```


♪ ไวต์ / แมส!"
หน่วยรวม: `iconverter://` BAR /kg  BAR `<ToolItem.rawValue>` BAR    BAR    BAR `input` BAR    BAR    BAR                                                BAR                     BAR    BAR     BAR      BAR     BAR        BAR       BAR


```
iconverter://tool/weight?v=1&from=pound&to=kilogram
```



```
iconverter://tool/weight?v=1&from=jin&to=gram
```


~สภาพการณ์~
หน่วย: `iconverter://` BAR  C BAR C] BAR `<ToolItem.rawValue>` BAR    BAR `text` BAR   BAR K      BAR `input` BAR     BAR `1/true/yes/on` BAR   BAR    BAR   BAR     BAR     BAR    BAR     BAR   BAR     BAR    BAR       BAR     BAR       BAR                                                    )


```
iconverter://tool/temperature?v=100&from=celsius&to=fahrenheit
```



```
iconverter://tool/temperature?v=37&from=celsius&to=kelvin
```


~เวลา~
หน่วยรวม:   c0      BAR s BAR `0/false/no/off` BAR min            BAR    BAR   BAR   BAR    BAR    BAR   BAR    BAR   BAR   BAR     BAR                                              BAR    BAR    BAR      BAR      BAR        BAR                                                    BAR


```
iconverter://tool/time?v=1&from=hour&to=second
```



```
iconverter://tool/time?v=7&from=day&to=hour
```


~ถูกเก็บ~
หน่วย: `iconverter://` BAR  (m/s) `<ToolItem.rawValue>` BAR    BAR   BAR    BAR    BAR    BAR     BAR    BAR    BAR M.


```
iconverter://tool/speed?v=100&from=kmPerHour&to=milePerHour
```



```
iconverter://tool/speed?v=1&from=mach&to=meterPerSecond
```


~แน่ใจว่า~
หน่วย: `iconverter://` BAR   BAR PA BAR `<ToolItem.rawValue>` BAR /pa `text` BAR   BAR `input` BAR   BAR    BAR `1/true/yes/on` BAR    BAR          BAR            BAR                        BAR         BAR       BAR     BAR             BAR                                                                      F.


```
iconverter://tool/pressure?v=1&from=atmosphere&to=kilopascal
```



```
iconverter://tool/pressure?v=120&from=mmHg&to=kilopascal
```


~... ~
หน่วย: `iconverter://` BAR   BAR J BAR `1/true/yes/on` BAR /c  BAR `text` c   BAR `input` BAR    BAR     BAR     BAR    BAR   BAR     BAR                                      BAR               BAR        BAR    BAR                                                  สม.


```
iconverter://tool/energy?v=1&from=kilowattHour&to=kilojoule
```



```
iconverter://tool/energy?v=500&from=kilocalorie&to=kilojoule
```


~ส่ง~
หน่วย: `iconverter://` BAR  v BAR `<ToolItem.rawValue>` BAR `text` C3          BAR `1/true/yes/on` /                       BAR               BAR        BAR     BAR      BAR         BAR                                          F))


```
iconverter://tool/power?v=1&from=hpMechanical&to=kilowatt
```



```
iconverter://tool/power?v=3000&from=watt&to=hpMetric
```


~... ~
หน่วย: `iconverter://` BAR  N BAR `<ToolItem.rawValue>` BAR /N `text` C3      BAR                                         BAR                  BAR                BAR                                                                    .


```
iconverter://tool/force?v=9.8&from=newton&to=kgf
```



```
iconverter://tool/force?v=1&from=kilonewton&to=lbf
```


~ตางหาก~
หน่วย: `iconverter://` BAR `<ToolItem.rawValue>` C2 `input` BAR            BAR             BAR           BAR                                   .


```
iconverter://tool/torque?v=100&from=newtonMeter&to=footPound
```


~ความถี่~
หน่วย: `iconverter://` BAR    BAR Hz  BAR `<ToolItem.rawValue>` BAR    BAR     BAR      BAR     BAR    BAR    BAR    BAR     BAR    BAR        BAR         BAR


```
iconverter://tool/frequency?v=2.4&from=gigahertz&to=megahertz
```



```
iconverter://tool/frequency?v=3000&from=rpm&to=hertz
```


~เสียงรบกวน~
หน่วย: `iconverter://` BAR   BAR `1/true/yes/on` BAR  rl    c2             BAR   BAR ' BAR    BAR `input` BAR `1/true/yes/on` BAR ")      BAR    BAR   BAR  BAR   BAR  BAR BAR   BAR    BAR  BAR  BAR BAR    BAR   BAR      BAR    BAR   BAR   BAR      BAR      BAR     F.


```
iconverter://tool/angle?v=180&from=degree&to=radian
```



```
iconverter://tool/angle?v=1&from=turn&to=degree
```


~ช่องข้อมูล~
หน่วย: `iconverter://` BAR   BAR b BAR `<ToolItem.rawValue>` BAR KB   BAR `text` BAR `input` BAR   BAR   BAR   BAR      BAR         BAR   BAR     BAR     BAR b     BAR b    BAR b BAR b BAR b BAR b BAR b BAR b BAR  b BAR    BAR   BAR    BAR   BAR      BAR       BAR      /B)      /B)               /B)


```
iconverter://tool/dataStorage?v=1&from=gigabyte&to=mebibyte
```



```
iconverter://tool/dataStorage?v=512&from=mebibyte&to=gigabyte
```


~Datata rate~
หน่วย: `text` BAR   BAR  bps BAR `<ToolItem.rawValue>` BAR    BAR     BAR   BAR   BAR     BAR   BAR   BAR   BAR  BAR   BAR   BAR   BAR     BAR    BAR    BAR    BAR    BAR    BAR    BAR         BAR    BAR    BAR                               ///BAR


```
iconverter://tool/dataRate?v=100&from=mbps&to=mBps
```



```
iconverter://tool/dataRate?v=1&from=gbps&to=mbps
```


~ความไม่สงบ~
หน่วย: `iconverter://` BAR lx  BAR `<ToolItem.rawValue>` /fc                BAR /C3       /nx.


```
iconverter://tool/illuminance?v=500&from=lux&to=footCandle
```


~ฟลักซ์เอนซิตี~
หน่วย: `iconverter://` BAR   BAR T BAR `<ToolItem.rawValue>` BAR    BAR    BAR `input` BAR     BAR       BAR     BAR    BAR         BAR         BAR          BAR                                                                         F.


```
iconverter://tool/magneticFlux?v=1&from=tesla&to=gauss
```


~แสงสะท้อน~
หน่วย: `iconverter://` BAR   BAR  bq BAR `<ToolItem.rawValue>` BAR `text` BAR    BAR `input` BAR    BAR  Ci          Ci                            BAR     BAR      BAR    BAR     BAR           BAR     BAR Ci           /Ci                                      .


```
iconverter://tool/radioactivity?v=1&from=curie&to=megabecquerel
```


~โชคชะตา~
หน่วย: `iconverter://` BAR   BAR `input` BAR `text` BAR   BAR `input` BAR    BAR    BAR    BAR /cP.


```
iconverter://tool/viscosity?v=1&from=pascalSecond&to=centipoise
```


~โลกกว้าง~
หน่วย: `iconverter://` BAR   BAR L/100km) `<ToolItem.rawValue>` C2    BAR   BAR    BAR `input` BAR     BAR MPK).


```
iconverter://tool/fuelEconomy?v=8.5&from=lPer100km&to=kmPerL
```



```
iconverter://tool/fuelEconomy?v=30&from=mpgUS&to=lPer100km
```


** มีอัตราต่ํา~
หน่วย: `iconverter://` /s     BAR                                                                                                                                            .


```
iconverter://tool/flowRate?v=1&from=literPerMinute&to=cubicMeterPerHour
```


~ความโหดร้าย~
หน่วย: `iconverter://` BAR   BAR /m3   BAR `<ToolItem.rawValue>` C2 `input` //ft3


```
iconverter://tool/density?v=1&from=gramPerCubicCentimeter&to=kgPerCubicMeter
```


~ฟลักซ์ (Wb) ~
หน่วย: `iconverter://` BAR   BAR /vb BAR `<ToolItem.rawValue>` C2    BAR    BAR `input` BAR  /b BAR                              /                   /M    .


```
iconverter://tool/magneticFluxTrue?v=1&from=weber&to=maxwell
```


~"Dosorbed dose~
หน่วย: `iconverter://` BAR     BAR Cy BAR `<ToolItem.rawValue>` C2     BAR `input` BAR              BAR     BAR                   BAR        BAR         BAR                                                                      ))))))))))))


```
iconverter://tool/absorbedDose?v=1&from=gray&to=rad
```


~ดูเซ~
หน่วย: `iconverter://` BAR   BAR /sv BAR `<ToolItem.rawValue>` C2    BAR    BAR `input` BAR      BAR      BAR     .


```
iconverter://tool/equivalentDose?v=1&from=sievert&to=rem
```



```
iconverter://tool/equivalentDose?v=20&from=millisievert&to=microsievert
```


~ยอดของพลัง~
หน่วย: `iconverter://` BAR  mol  BAR `<ToolItem.rawValue>` BAR      BAR `input` BAR    BAR                      BAR      BAR     BAR     BAR     BAR    BAR    BAR    BAR       BAR       BAR    BAR                                                                                          F.


```
iconverter://tool/amountOfSubstance?v=1&from=mole&to=millimole
```



```
iconverter://tool/amountOfSubstance?v=150&from=millimole&to=micromole
```


---

[การรองรับ iConverter](./) & middot; [FAQ](./figg) & middot; [นโยบายการรับสมัคร](./ princialvance)

</section>
<section lang="de" markdown="1">

iConverter unterstützt `iconverter://` URL-Schema Deep Links - Öffnen Sie eines der 101 Tools von externen Apps, Webseiten, QR-Codes (generieren oder **scannen in-App **), Safari oder Apple Shortcuts, optional Vorfüllen von Eingabefeldern über Abfrageparameter.

> **Widget Note:** Der **Launcher ** Widget Tool Picker enthält alle unterstützten Tools außer **Web Browser **. Widget-Konfigurations-Benutzeroberfläche folgt ** iOS-Systemsprache **, nicht die In-App-Sprache überschreibt unter Einstellungen.

## Protokollspezifikation


```
iconverter://tool/<ToolItem.rawValue>?key=value&key2=value2
```


- „<ToolItem.rawValue> teilt die gleiche Benennung wie Widget Deep Links.
- Parameternamen unterstützen sowohl kurze Schlüssel als auch synonyme Aliase (z. B. `text` entspricht `input`).
- Booleaner: `1/true/yes/on` → true; `0/false/no/off` → false.
- Daten: unterstützt `yyyy-MM-dd`, ISO8601, Unix-Zeitstempel (Sekunden).
- Einheitenkonverter haben ein gemeinsames Format: `v` = Wert, `from` = Quelleinheit (rawValue oder Symbol, case-insensitive), `to` = Zieleinheit.

---

## 1. Rechner

**Rechner** — nur geöffnet


```
iconverter://tool/calculator
```


**Wissenschaftlicher Rechner** — nur geöffnet


```
iconverter://tool/scientific
```


**Programmer Calculator** — nur geöffnet


```
iconverter://tool/programmer
```


---

## 2. Finanzen

**Hypothekenrechner** `iconverter://` = Kreditbetrag, `<ToolItem.rawValue>` = Jahreszinssatz %, `text` = Jahre, `input` = 0 = gleiche Rate / 1 = gleiches Kapital.


```
iconverter://tool/mortgage?p=1000000&r=3.7&y=30&mode=0
```


**Einkommensteuer** `iconverter://` = Monatsgehalt, `<ToolItem.rawValue>` = Sozialversicherung, `text` = Sonderabzug, `input` = Schwelle, `1/true/yes/on` = Jahresbonus.


```
iconverter://tool/incomeTax?salary=20000&insurance=3000&deduction=1000&threshold=5000&bonus=50000
```


**Zinssatz** `iconverter://` = Hauptforderung, `<ToolItem.rawValue>` = monatlicher Beitrag, `text` = Jahreszinssatz %, `input` = Jahre, `1/true/yes/on` = 0 = jährlich / 1 = monatlich / 2 = täglich, `0/false/no/off` = Inflation %.


```
iconverter://tool/compoundInterest?p=100000&m=1000&r=7&y=10&freq=1
```


**Rabattrechner** `iconverter://` = 0-4, `<ToolItem.rawValue>` = Originalpreis, `text` = Abzinsungsverhältnis, `input` = Schwellenwert, `1/true/yes/on` = Minderungsbetrag.


```
iconverter://tool/discount?mode=0&p=299&r=8.5
```


Voll minus Beispiel:


```
iconverter://tool/discount?mode=3&p=350&t=300&u=50
```


**Tipp & AA Split** `iconverter://` = 0 = Spitze / 1 = AA Split, `<ToolItem.rawValue>` = Rechnung, `text` = Spitze %, `input` = Steuer %, `1/true/yes/on` = Menschen zählen.


```
iconverter://tool/tipAA?mode=0&bill=200&tip=15&tax=0&ppl=4
```


** Hypothekenzahlung** `iconverter://` = ursprüngliches Darlehen, `<ToolItem.rawValue>` = Jahreszinssatz %, `text` = Gesamtlaufzeit (Jahre), `input` = bezahlte Konditionen, `1/true/yes/on` = Vorauszahlungsbetrag, `0/false/no/off` = 0 = Verkürzung / 1 = monatliche Reduzierung / 2 = vergleichen.


```
iconverter://tool/mortgagePrepay?p=800000&r=3.7&total=30&paid=5&prepay=100000&mode=2
```


**Immobiliensteuer** - nur offen


```
iconverter://tool/realEstateTax
```


---

## 3. Datum und Uhrzeit

** Alter & Jubiläum ** `iconverter://` = Geburtstag `<ToolItem.rawValue>` , `text` = Stichtag.


```
iconverter://tool/ageAnniversary?birth=1990-05-01&ref=2026-05-17
```


**Datum Arithmetik** `iconverter://` = 0 = add/subtract / 1 = Datumsdifferenz.

Add-Subtraktionsmodus ( `iconverter://` = Startdatum, `<ToolItem.rawValue>` = ± Tage, `text` = ± Wochen, `input` = ± Monate, `1/true/yes/on` = ± Jahre):


```
iconverter://tool/dateArithmetic?mode=0&d1=2026-05-17&d=100
```


Differenzmodus ( `iconverter://` = Datum 1, `<ToolItem.rawValue>` = Datum 2):


```
iconverter://tool/dateArithmetic?mode=1&d1=2026-01-01&d2=2026-12-31
```


** Mondkalender** `iconverter://` = Gregorianisches Datum `<ToolItem.rawValue>` .


```
iconverter://tool/lunarCalendar?date=2026-05-17
```


**Solar Terms** — nur offen


```
iconverter://tool/solarTerms
```


**Countdown** `iconverter://` = Ereignisname, `<ToolItem.rawValue>` = Zieldatum `text` , `input` = Einschlusszeit `1/true/yes/on` .


```
iconverter://tool/countdown?label=Holiday&target=2026-10-01&time=0
```


**Schwangerschaftsrechner** `iconverter://` = 0 = LMP / 1 = Konzeption / 2 = IVF, `<ToolItem.rawValue>` = Stichtag, `text` = IVF-Embryotag 0 = D3 / 1 = D5.


```
iconverter://tool/pregnancy?method=0&ref=2026-03-01
```



```
iconverter://tool/pregnancy?method=2&ref=2026-03-15&ivf=1
```


**Menstrueller Zyklus** `iconverter://` = Datum der letzten Menstruation, `<ToolItem.rawValue>` = Zyklustage, `text` = Periodentage.


```
iconverter://tool/menstrual?lmp=2026-05-01&cycle=28&period=5
```


** Weltuhr** `iconverter://` = city search keyword, `<ToolItem.rawValue>` = use current time `text` , `input` = custom datetime.


```
iconverter://tool/worldClock?q=Tokyo
```



```
iconverter://tool/worldClock?now=0&ref=2026-05-17T20:00:00
```


** Tierkreis** — nur geöffnet


```
iconverter://tool/zodiac
```


---

## 4. Mathe

**Prozentsatzrechner** `iconverter://` = 0-4, `<ToolItem.rawValue>` = Wert A, `text` = Wert B.


```
iconverter://tool/percentage?mode=0&a=75&b=120
```


**Fraktionsrechner** — nur geöffnet


```
iconverter://tool/fraction
```


**Prime Factorization** — nur offen


```
iconverter://tool/primeFactor
```


**Quadratischer Solver** – nur offen


```
iconverter://tool/quadraticSolver
```


**Statistik** `iconverter://` = Datensatz, getrennt durch Leerzeichen / Komma / Semikolon.


```
iconverter://tool/statistics?data=1,2,3,4,5,6,7,8,9,10
```


**Kombinationen & Permutationen** – nur offen


```
iconverter://tool/combinations
```


**Geometrie** `iconverter://` = Form, `<ToolItem.rawValue>` / `text` / `input` = Dimensionsparameter.

Verfügbare Formen: `iconverter://` · `<ToolItem.rawValue>` · `text` · `input` · `1/true/yes/on` · `0/false/no/off` · `yyyy-MM-dd` · `v` · `from` · `to` · `r` · `y` · `mode` · `salary` · `insurance` · `deduction` .

Kreis ( `iconverter://` = Radius):


```
iconverter://tool/geometry?shape=circle&v1=5
```


Rechteck ( `iconverter://` = Länge, `<ToolItem.rawValue>` = Breite):


```
iconverter://tool/geometry?shape=rectangle&v1=10&v2=5
```


Kugel ( `iconverter://` = Radius):


```
iconverter://tool/geometry?shape=sphere&v1=3
```


Zylinder ( `iconverter://` = Radius, `<ToolItem.rawValue>` = Höhe):


```
iconverter://tool/geometry?shape=cylinder&v1=4&v2=10
```


---

## 5. Kodierung

**Roman Numeral** `iconverter://` = arabische Zahl (1-3999); oder `<ToolItem.rawValue>` = römische Zahlenfolge.


```
iconverter://tool/roman?n=2026
```



```
iconverter://tool/roman?roman=MMXXVI
```


**Base64 Encoder / Decoder** `iconverter://` = Code/Decode, `<ToolItem.rawValue>` = URL-sicherer Modus `text` , `input` = Eingabetext.


```
iconverter://tool/base64?mode=encode&text=Hello%2C+World!
```



```
iconverter://tool/base64?mode=decode&urlSafe=0&text=SGVsbG8sIFdvcmxkIQ%3D%3D
```


**URL Encoder / Decoder** `iconverter://` = encode/decode, `<ToolItem.rawValue>` = Component Mode 0 = full / 1 = query / 2 = path, `text` = input.


```
iconverter://tool/urlCoder?mode=encode&comp=0&text=https://example.com/path?q=hello world
```



```
iconverter://tool/urlCoder?mode=decode&text=https%3A%2F%2Fexample.com%2F%3Fq%3Dhello%20world
```


**Hash Calculator** `iconverter://` = Input, `<ToolItem.rawValue>` = md5/sha1/sha256/sha512, `text` = Großbuchstaben `input` , `1/true/yes/on` = HMAC `0/false/no/off` , `yyyy-MM-dd` = HMAC-Schlüssel aktivieren.


```
iconverter://tool/hashing?text=Hello+World&algo=sha256&upper=0
```



```
iconverter://tool/hashing?text=data&algo=md5&hmac=1&key=secret
```


**Word Count** `iconverter://` = Text zur Analyse.


```
iconverter://tool/wordCount?text=The+quick+brown+fox+jumps+over+the+lazy+dog.
```


**Farbwandler ** `iconverter://` = Hexfarbe; oder `<ToolItem.rawValue>` / / `text` / `input` = RGB-Komponenten (0–255).


```
iconverter://tool/colorConverter?hex=%23FF8800
```



```
iconverter://tool/colorConverter?r=255&g=136&b=0
```


**Farbpalette** — nur geöffnet


```
iconverter://tool/colorPalette
```


**QR-Code** `iconverter://` = Inhalt, `<ToolItem.rawValue>` = `text` usw., `input` = Fehlerkorrekturgrad `1/true/yes/on` .


```
iconverter://tool/qrcode?text=https%3A%2F%2Fexample.com&ecc=H
```



```
iconverter://tool/qrcode?text=Hello+iConverter&format=qr&ecc=M
```


**JSON Formatter `iconverter://` = JSON-Zeichenfolge (URL-codiert), `<ToolItem.rawValue>` = Einrückräume 2/4.


```
iconverter://tool/jsonFormatter?text=%7B%22name%22%3A%22Alice%22%2C%22age%22%3A30%7D&indent=2
```


**Zeitstempel ** `iconverter://` = Unix-Zeitstempel (Sekunden), `<ToolItem.rawValue>` = Einheit 0 = sec / 1 = ms; oder `text` = ISO8601-Datumszeichenfolge.


```
iconverter://tool/timestamp?ts=1747440000
```



```
iconverter://tool/timestamp?iso=2026-05-17T12:00:00
```


**Bank Card Validator** `iconverter://` = Kartennummer.


```
iconverter://tool/bankCard?num=6214830172816734
```


**Text Case Converter** `iconverter://` = Eingangstext.


```
iconverter://tool/textCase?text=hello+world+from+iConverter
```


**Text Diff** – nur geöffnet


```
iconverter://tool/textDiff
```


**HTTP Request** `iconverter://` = Request URL, `<ToolItem.rawValue>` = GET/POST/PUT/PATCH/DELETE, `text` = Request Body, `input` = `1/true/yes/on` , `0/false/no/off` = Header JSON.


```
iconverter://tool/httpRequest?url=https%3A%2F%2Fapi.example.com%2Fusers&method=GET
```



```
iconverter://tool/httpRequest?url=https%3A%2F%2Fapi.example.com%2Fusers&method=POST&body=%7B%22name%22%3A%22Alice%22%7D&bodyKind=json
```


**File Download** `iconverter://` = URL herunterladen, `<ToolItem.rawValue>` = Dateiname (optional).


```
iconverter://tool/fileDownload?url=https%3A%2F%2Fexample.com%2Freport.pdf&name=report.pdf
```


**HTTP-Statuscodes** `iconverter://` = Statuscode; oder `<ToolItem.rawValue>` = Suchschlüsselwort.


```
iconverter://tool/httpStatusCodes?code=404
```



```
iconverter://tool/httpStatusCodes?q=redirect
```


**IP Utility** `iconverter://` = Subnetz/Cidr/Bereich, `<ToolItem.rawValue>` = IP-Adresse, `text` = Subnetzmaske oder `input` = CIDR-Präfixlänge.


```
iconverter://tool/ipUtility?mode=subnet&ip=192.168.1.0&mask=255.255.255.0
```



```
iconverter://tool/ipUtility?ip=10.0.0.0&prefix=24
```


**ASCII-Tabelle** `iconverter://` = Dezimalcodepunkt; oder `<ToolItem.rawValue>` = Hexcodepunkt; oder `text` = Suche.


```
iconverter://tool/asciiTable?dec=65
```



```
iconverter://tool/asciiTable?q=space
```


** Passwortgenerator** `iconverter://` = Länge, `<ToolItem.rawValue>` = Großbuchstaben `text` , `input` = Kleinbuchstaben `1/true/yes/on` , `0/false/no/off` = Ziffern `yyyy-MM-dd` , `v` = Symbole `from` , `to` = keine mehrdeutigen Zeichen `p` , `r` = erzeugen sofort `y` .


```
iconverter://tool/passwordGenerator?length=20&upper=1&lower=1&digits=1&symbols=1&unambiguous=1&go=1
```


**Random Number Generator** `iconverter://` = minimum, `<ToolItem.rawValue>` = maximum, `text` = count, `input` = Dezimalstellen, `1/true/yes/on` = unique `0/false/no/off` , `yyyy-MM-dd` = 0 = none / 1 = asc / 2 = desc, `v` = erzeugen sofort `from` .


```
iconverter://tool/randomNumber?min=1&max=100&n=10&unique=1&sort=1&go=1
```



```
iconverter://tool/randomNumber?min=0&max=1&n=5&decimals=4&go=1
```


**Mehr Code** `iconverter://` = Kodierung/Dekodierung, `<ToolItem.rawValue>` = Eingangstext.


```
iconverter://tool/morseCode?mode=encode&text=SOS
```



```
iconverter://tool/morseCode?mode=decode&text=...+---+...
```


JWT Decoder `iconverter://` = JWT-Token-String.


```
iconverter://tool/jwtParser?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c
```


**Cron Expression Parser** `iconverter://` = Cron-Ausdruck (Leerzeichen können durch `<ToolItem.rawValue>` ersetzt werden).


```
iconverter://tool/cronParser?expr=0+9+*+*+1-5
```



```
iconverter://tool/cronParser?expr=0+0+*+*+*
```


**Regex Tester** `iconverter://` = Regexmuster (URL-codiert), `<ToolItem.rawValue>` = Testtext, `text` = Ersatz, `input` = case-insensitive `1/true/yes/on` , `0/false/no/off` = Multiline `yyyy-MM-dd` , `v` = dotall `from` .


```
iconverter://tool/regexTester?pattern=%5Cd%2B&haystack=abc123def456&i=0
```



```
iconverter://tool/regexTester?pattern=%28%5Cw%2B%29&haystack=hello+world&replacement=%5B%241%5D&i=1
```


**Web Browser** `iconverter://` = direkt offene URL; oder `<ToolItem.rawValue>` = Suchabfrage (verwendet eine Standard-Suchmaschine).


```
iconverter://tool/webBrowser?url=https%3A%2F%2Fexample.com
```



```
iconverter://tool/webBrowser?q=SwiftUI+deep+link+2026
```


---

## 6. Lebensstil

**BMI-Rechner** `iconverter://` = Höhe cm, `<ToolItem.rawValue>` = Gewicht kg, `text` = Standard 0 = chinesischer Erwachsener / 1 = WHO.


```
iconverter://tool/bmi?h=175&w=70&std=0
```


**BMR-Rechner** `iconverter://` = Höhe cm, `<ToolItem.rawValue>` = Gewicht kg, `text` = Alter, `input` = m = männlich / f = weiblich, `1/true/yes/on` = Aktivitätsstufe 0-4, `0/false/no/off` = 0 = Harris-Benedict / 1 = Mifflin-St Jeor.


```
iconverter://tool/bmr?h=175&w=70&age=30&sex=m&act=1&formula=1
```


**Kleidungsgröße** — nur geöffnet


```
iconverter://tool/clothingSize
```


**Ringgröße** — nur geöffnet


```
iconverter://tool/ringSize
```


**Höhenwandler** — nur geöffnet


```
iconverter://tool/heightConverter
```


**Kraftstoffkostenrechner** `iconverter://` = 0 = metrisch / 1 = imperial, `<ToolItem.rawValue>` = Entfernung, `text` = Verbrauch pro 100 km, `input` = Kraftstoffpreis, `1/true/yes/on` = Menschen.


```
iconverter://tool/fuelCost?unit=0&d=500&c=8.5&p=7.8&n=1
```


**Versandkostenrechner** `iconverter://` = tatsächliches Gewicht kg, `<ToolItem.rawValue>` = erstes Gewicht kg, `text` = Gebühr für das erste Gewicht, `input` = Stufengewicht kg, `1/true/yes/on` = Stufengebühren.


```
iconverter://tool/shippingFee?w=3.5&fw=1&ff=12&sw=1&sf=8
```


Mit Volumengewicht ( `iconverter://` = enable `<ToolItem.rawValue>` , `text` / `input` / `1/true/yes/on` = drei Seiten cm, `0/false/no/off` = Teiler):


```
iconverter://tool/shippingFee?w=2&vol=1&l=50&wd=40&h=30&div=6000&fw=1&ff=12&sw=1&sf=8
```


**Blutalkoholgehalt (BAC)** `iconverter://` = m = männlich / f = weiblich, `<ToolItem.rawValue>` = Gewicht kg, `text` = Volumen mL, `input` = ABV %, `1/true/yes/on` = Stunden seit dem Trinken.


```
iconverter://tool/alcoholBac?sex=m&w=70&v=500&abv=5&h=0.5
```


**Beziehung** `iconverter://` = Beziehungskette (kommagetrennt), `<ToolItem.rawValue>` = Ego Sex 0 = männlich / 1 = weiblich, `text` = umgekehrt zeigen `input` .


```
iconverter://tool/relationship?chain=f,os&sex=0&reverse=1
```



```
iconverter://tool/relationship?chain=m,ob&sex=1&reverse=0
```


** ID Card Parser** `iconverter://` = ID-Kartennummer.


```
iconverter://tool/idCard?id=110101199003073010
```


**Coin Flip** - nur geöffnet


```
iconverter://tool/coinFlip
```


**Dice Roller** — nur geöffnet


```
iconverter://tool/diceRoller
```


**Random Draw** – nur geöffnet


```
iconverter://tool/randomDraw
```


**Spin Wheel** — nur geöffnet


```
iconverter://tool/spinWheel
```


** Video Frame Export** – nur geöffnet


```
iconverter://tool/videoFrameExport
```


---

## 7. Sensoren

**Compass** — nur offen


```
iconverter://tool/compass
```


**Niveau** — nur offen


```
iconverter://tool/level
```


** Höhenlage** — nur geöffnet


```
iconverter://tool/altitude
```


---

## 8. Chinesisch

**Chinesische Nummer** `iconverter://` = Zahl.


```
iconverter://tool/chineseNumber?n=12345.67
```


**Chinesische Zahl umgekehrt ** `iconverter://` = Chinesische Zahlenfolge.


```
iconverter://tool/chineseNumberReverse?text=一万二千三百四十五
```


**Finanzbetrag** `iconverter://` = Betrag, `<ToolItem.rawValue>` = Anhang 整 `text` .


```
iconverter://tool/financialAmount?amount=12345.67&zheng=1
```


---

## 9. Konverter

Allgemeines Format: `iconverter://` = Wert, `<ToolItem.rawValue>` = Quelleinheit (rawValue oder Symbol, case-insensitive), `text` = Zieleinheit.

---

** Länge **
Gemeinsame Einheiten: `iconverter://` (m) · `<ToolItem.rawValue>` (km) · `text` (cm) · `input` (mm) · `1/true/yes/on` (ft) · `0/false/no/off` (in) · `yyyy-MM-dd` (mi) · `v` (yd) · `from` (nmi) · `to` (里) · `p` (尺).


```
iconverter://tool/length?v=100&from=meter&to=foot
```



```
iconverter://tool/length?v=1&from=mile&to=kilometer
```


**Area**
Gemeinsame Einheiten: `iconverter://` (m2) · `<ToolItem.rawValue>` (ha) · `text` (acre) · `input` (ft2) · `1/true/yes/on` (mile2) · `0/false/no/off` (亩) · `yyyy-MM-dd` (km2).


```
iconverter://tool/area?v=1&from=hectare&to=mu
```



```
iconverter://tool/area?v=1&from=acre&to=squareMeter
```


**Volumen**
Gemeinsame Einheiten: `iconverter://` (L) · `<ToolItem.rawValue>` (mL) · `text` (m3) · `input` (gal) · `1/true/yes/on` (fl oz) · `0/false/no/off` (cup) · `yyyy-MM-dd` (gal UK) · `v` (bbl).


```
iconverter://tool/volume?v=1&from=gallon&to=liter
```



```
iconverter://tool/volume?v=355&from=milliliter&to=fluidOunce
```


**Gewicht/Masse**
Gemeinsame Einheiten: `iconverter://` (kg) · `<ToolItem.rawValue>` (g) · `text` (lb) · `input` (oz) · `1/true/yes/on` (t) · `0/false/no/off` (斤) · `yyyy-MM-dd` (两) · `v` (ct).


```
iconverter://tool/weight?v=1&from=pound&to=kilogram
```



```
iconverter://tool/weight?v=1&from=jin&to=gram
```


**Temperatur**
Einheiten: `iconverter://` (°C) · `<ToolItem.rawValue>` (°F) · `text` (K) · `input` (°R) · `1/true/yes/on` (°Re).


```
iconverter://tool/temperature?v=100&from=celsius&to=fahrenheit
```



```
iconverter://tool/temperature?v=37&from=celsius&to=kelvin
```


**Zeit **
Gemeinsame Einheiten: `iconverter://` (s) · `<ToolItem.rawValue>` (min) · `text` (h) · `input` (Tag) · `1/true/yes/on` (wk) · `0/false/no/off` (mo) · `yyyy-MM-dd` (yr) · `v` (ms) · `from` (μs).


```
iconverter://tool/time?v=1&from=hour&to=second
```



```
iconverter://tool/time?v=7&from=day&to=hour
```


** Geschwindigkeit **
Einheiten: `iconverter://` (m/s) · `<ToolItem.rawValue>` (km/h) · `text` (mph) · `input` (kn) · `1/true/yes/on` (Ma).


```
iconverter://tool/speed?v=100&from=kmPerHour&to=milePerHour
```



```
iconverter://tool/speed?v=1&from=mach&to=meterPerSecond
```


**Druck**
Einheiten: `iconverter://` (Pa) · `<ToolItem.rawValue>` (kPa) · `text` (bar) · `input` (atm) · `1/true/yes/on` (psi) · `0/false/no/off` (mmHg).


```
iconverter://tool/pressure?v=1&from=atmosphere&to=kilopascal
```



```
iconverter://tool/pressure?v=120&from=mmHg&to=kilopascal
```


** Energie**
Einheiten: `iconverter://` (J) · `<ToolItem.rawValue>` (kJ) · `text` (cal) · `input` (kcal) · `1/true/yes/on` (kWh) · `0/false/no/off` (BTU).


```
iconverter://tool/energy?v=1&from=kilowattHour&to=kilojoule
```



```
iconverter://tool/energy?v=500&from=kilocalorie&to=kilojoule
```


** Power**
Einheiten: `iconverter://` (W) · `<ToolItem.rawValue>` (kW) · `text` (hp) · `input` (PS) · `1/true/yes/on` (BTU/h).


```
iconverter://tool/power?v=1&from=hpMechanical&to=kilowatt
```



```
iconverter://tool/power?v=3000&from=watt&to=hpMetric
```


** Stärke **
Einheiten: `iconverter://` (N) · `<ToolItem.rawValue>` (kN) · `text` (kgf) · `input` (lbf) · `1/true/yes/on` (dyn).


```
iconverter://tool/force?v=9.8&from=newton&to=kgf
```



```
iconverter://tool/force?v=1&from=kilonewton&to=lbf
```


**Torque**
Einheiten: `iconverter://` (N·m) · `<ToolItem.rawValue>` (N·cm) · `text` (kgf·m) · `input` (ft·lb) · `1/true/yes/on` (in·lb).


```
iconverter://tool/torque?v=100&from=newtonMeter&to=footPound
```


**Häufigkeit**
Einheiten: `iconverter://` (Hz) · `<ToolItem.rawValue>` (kHz) · `text` (MHz) · `input` (GHz) · `1/true/yes/on` (THz) · `0/false/no/off` (rpm).


```
iconverter://tool/frequency?v=2.4&from=gigahertz&to=megahertz
```



```
iconverter://tool/frequency?v=3000&from=rpm&to=hertz
```


**Winkel**
Einheiten: `iconverter://` (°) · `<ToolItem.rawValue>` (rad) · `text` (grad) · `input` (') · `1/true/yes/on` () · `0/false/no/off` (turn).


```
iconverter://tool/angle?v=180&from=degree&to=radian
```



```
iconverter://tool/angle?v=1&from=turn&to=degree
```


**Datenspeicherung**
Einheiten: `iconverter://` (B) · `<ToolItem.rawValue>` (KB) · `text` (MB) · `input` (GB) · `1/true/yes/on` (TB) · `0/false/no/off` (KiB) · `yyyy-MM-dd` (MiB) · `v` (GiB).


```
iconverter://tool/dataStorage?v=1&from=gigabyte&to=mebibyte
```



```
iconverter://tool/dataStorage?v=512&from=mebibyte&to=gigabyte
```


**Datensatz**
Einheiten: `iconverter://` (bps) · `<ToolItem.rawValue>` (Kbps) · `text` (Mbps) · `input` (Gbps) · `1/true/yes/on` (KB/s) · `0/false/no/off` (MB/s) · `yyyy-MM-dd` (GB/s).


```
iconverter://tool/dataRate?v=100&from=mbps&to=mBps
```



```
iconverter://tool/dataRate?v=1&from=gbps&to=mbps
```


**Beleuchtung**
Einheiten: `iconverter://` (lx) · `<ToolItem.rawValue>` (fc) · `text` (ph) · `input` (nx).


```
iconverter://tool/illuminance?v=500&from=lux&to=footCandle
```


**Magnetische Flussdichte**
Einheiten: `iconverter://` (T) · `<ToolItem.rawValue>` (mT) · `text` (μT) · `input` (G) · `1/true/yes/on` (mG).


```
iconverter://tool/magneticFlux?v=1&from=tesla&to=gauss
```


**Radioaktivität**
Einheiten: `iconverter://` (Bq) · `<ToolItem.rawValue>` (kBq) · `text` (MBq) · `input` (Ci) · `1/true/yes/on` (mCi) · `0/false/no/off` (μCi).


```
iconverter://tool/radioactivity?v=1&from=curie&to=megabecquerel
```


**Viskosität**
Einheiten: `iconverter://` (Pa·s) · `<ToolItem.rawValue>` (mPa·s) · `text` (P) · `input` (cP).


```
iconverter://tool/viscosity?v=1&from=pascalSecond&to=centipoise
```


**Kraftstoffwirtschaft**
Einheiten: `iconverter://` (L/100km) · `<ToolItem.rawValue>` (km/L) · `text` (MPG US) · `input` (MPG UK).


```
iconverter://tool/fuelEconomy?v=8.5&from=lPer100km&to=kmPerL
```



```
iconverter://tool/fuelEconomy?v=30&from=mpgUS&to=lPer100km
```


**Flow Rate**
Einheiten: `iconverter://` (m3/s) · `<ToolItem.rawValue>` (m3/h) · `text` (L/s) · `input` (L/min) · `1/true/yes/on` (L/h) · `0/false/no/off` (gpm US) · `yyyy-MM-dd` (cfm).


```
iconverter://tool/flowRate?v=1&from=literPerMinute&to=cubicMeterPerHour
```


**Dichte**
Einheiten: `iconverter://` (kg/m3) · `<ToolItem.rawValue>` (g/cm3) · `text` (g/L) · `input` (kg/L) · `1/true/yes/on` (lb/ft3).


```
iconverter://tool/density?v=1&from=gramPerCubicCentimeter&to=kgPerCubicMeter
```


**Magnetischer Fluss (Wb)**
Einheiten: `iconverter://` (Wb) · `<ToolItem.rawValue>` (mWb) · `text` (μWb) · `input` (kWb) · `1/true/yes/on` (Mx).


```
iconverter://tool/magneticFluxTrue?v=1&from=weber&to=maxwell
```


**Absorbierte Dosis**
Einheiten: `iconverter://` (Gy) · `<ToolItem.rawValue>` (mGy) · `text` (μGy) · `input` (kGy) · `1/true/yes/on` (rad) · `0/false/no/off` (mrad).


```
iconverter://tool/absorbedDose?v=1&from=gray&to=rad
```


** Äquivalente Dosis**
Einheiten: `iconverter://` (Sv) · `<ToolItem.rawValue>` (mSv) · `text` (μSv) · `input` (rem) · `1/true/yes/on` (mrem).


```
iconverter://tool/equivalentDose?v=1&from=sievert&to=rem
```



```
iconverter://tool/equivalentDose?v=20&from=millisievert&to=microsievert
```


**Stoffmenge**
Einheiten: `iconverter://` (mol) · `<ToolItem.rawValue>` (mmol) · `text` (μmol) · `input` (kmol) · `1/true/yes/on` (nmol) · `0/false/no/off` (pmol).


```
iconverter://tool/amountOfSubstance?v=1&from=mole&to=millimole
```



```
iconverter://tool/amountOfSubstance?v=150&from=millimole&to=micromole
```


---

[Zurück zum iConverter Support](../) &middot; [FAQ](../faq) &middot; [Privacy Policy](../privacy]

</section>
<section lang="fr" markdown="1">

iConverter prend en charge `iconverter://` Des liens profonds du schéma d'URL – ouvrez l'un des 101 outils des applications externes, des pages web, des codes QR (générés ou **scan dans l'application**), Safari ou des raccourcis Apple, en option pré-remplissant les champs d'entrée via les paramètres de requête.

> **Note générale:** Le sélectionneur d'outils de widget **Launcher** inclut tous les outils pris en charge, sauf **Browser Web**. L'interface utilisateur de configuration Widget suit **iOS language système**, et non la langue in-app sous Paramètres.

## Spécification du protocole


```
iconverter://tool/<ToolItem.rawValue>?key=value&key2=value2
```


- `<ToolItem.rawValue>` partage le même nom que widget deep links.
- Les noms de paramètres supportent à la fois les clés courtes et les alias synonymes (par exemple `text` est équivalent à `input`).
- Booléens: `1/true/yes/on` → true; `0/false/no/off` → false.
- Dates: prend en charge `aaaa-MM-dd`, ISO8601, Unix timestamp (secondes).
- Les convertisseurs d'unités partagent un format commun: `v` = valeur, `from` = unité source (rawValue ou symbole, insensible à la casse), `to` = unité cible.

---

## 1. Calculatrice

**Calculateur** — ouvert uniquement


```
iconverter://tool/calculator
```


**Calculatrice scientifique** — ouvert uniquement


```
iconverter://tool/scientific
```


** Calculatrice de programme** – ouverte uniquement


```
iconverter://tool/programmer
```


---

## 2. Financement

** Calculatrice de masse** `iconverter://` = montant du prêt, `<ToolItem.rawValue>` = taux annuel %, `text` = années, `input` = 0 = montant égal / 1 = principal égal.


```
iconverter://tool/mortgage?p=1000000&r=3.7&y=30&mode=0
```


** Impôt sur le revenu** `iconverter://` = salaire mensuel, `<ToolItem.rawValue>` = assurance sociale, `text` = déduction spéciale, `input` = seuil, `1/true/yes/on` = prime annuelle.


```
iconverter://tool/incomeTax?salary=20000&insurance=3000&deduction=1000&threshold=5000&bonus=50000
```


** Intérêts composés** `iconverter://` = principal, `<ToolItem.rawValue>` = cotisation mensuelle, `text` = taux annuel %, `input` = années, `1/true/yes/on` = 0 = annuel / 1 = mensuel / 2 = quotidien, `0/false/no/off` = inflation %.


```
iconverter://tool/compoundInterest?p=100000&m=1000&r=7&y=10&freq=1
```


** Calculatrice de réduction** `iconverter://` = 0–4, `<ToolItem.rawValue>` = prix initial, `text` = taux d'actualisation, `input` = seuil, `1/true/yes/on` = montant de réduction.


```
iconverter://tool/discount?mode=0&p=299&r=8.5
```


Exemple complet:


```
iconverter://tool/discount?mode=3&p=350&t=300&u=50
```


**Conseil & AA Split** `iconverter://` = 0 = pointe / 1 = AA fractionné, `<ToolItem.rawValue>` = facture, `text` = pointe %, `input` = taxe %, `1/true/yes/on` = nombre de personnes.


```
iconverter://tool/tipAA?mode=0&bill=200&tip=15&tax=0&ppl=4
```


**Prépaiement anticipé** `iconverter://` = prêt initial, `<ToolItem.rawValue>` = taux annuel %, `text` = durée totale (années), `input` = durées payées, `1/true/yes/on` = montant prépayé, `0/false/no/off` = 0 = raccourci / 1 = réduction mensuelle / 2 = comparaison.


```
iconverter://tool/mortgagePrepay?p=800000&r=3.7&total=30&paid=5&prepay=100000&mode=2
```


**Impôt immobilier** — ouvert uniquement


```
iconverter://tool/realEstateTax
```


---

## 3. Date et heure

**Âge et anniversaire** `iconverter://` = anniversaire `<ToolItem.rawValue>` , `text` = date de référence.


```
iconverter://tool/ageAnniversary?birth=1990-05-01&ref=2026-05-17
```


**Date Arithmétique** `iconverter://` = 0 = addition/soustraction / 1 = différence de date.

Mode de sous-traction ( `iconverter://` = date de début, `<ToolItem.rawValue>` = ± jours, `text` = ± semaines, `input` = ± mois, `1/true/yes/on` = ± années):


```
iconverter://tool/dateArithmetic?mode=0&d1=2026-05-17&d=100
```


Mode de différence ( `iconverter://` = date 1, `<ToolItem.rawValue>` = date 2) :


```
iconverter://tool/dateArithmetic?mode=1&d1=2026-01-01&d2=2026-12-31
```


** Calendrier lunaire** `iconverter://` = date grégorien `<ToolItem.rawValue>` ```
iconverter://tool/lunarCalendar?date=2026-05-17
```


**Conditions solaires** — ouvert uniquement


```
iconverter://tool/solarTerms
```


** Compte à rebours** `iconverter://` = nom de l'événement, `<ToolItem.rawValue>` = date cible `text` , `input` = indiquer l'heure `1/true/yes/on` .


```
iconverter://tool/countdown?label=Holiday&target=2026-10-01&time=0
```


** Calculatrice de grossesse** `iconverter://` = 0 = PMT / 1 = conception / 2 = FIV, `<ToolItem.rawValue>` = date de référence, `text` = FIV embryon jour 0 = D3 / 1 = D5.


```
iconverter://tool/pregnancy?method=0&ref=2026-03-01
```



```
iconverter://tool/pregnancy?method=2&ref=2026-03-15&ivf=1
```


** Cycle menstruel** `iconverter://` = date de la dernière période menstruelle, `<ToolItem.rawValue>` = jours de cycle, `text` = jours de période.


```
iconverter://tool/menstrual?lmp=2026-05-01&cycle=28&period=5
```


** Horloge mondiale** `iconverter://` = mot clé de la recherche de ville, `<ToolItem.rawValue>` ```
iconverter://tool/worldClock?q=Tokyo
```



```
iconverter://tool/worldClock?now=0&ref=2026-05-17T20:00:00
```


**Zodiac** – ouvert uniquement


```
iconverter://tool/zodiac
```


---

## 4. Mathématiques

** Calculatrice du pourcentage** `iconverter://` = 0–4, `<ToolItem.rawValue>` = valeur A, `text` = valeur B.


```
iconverter://tool/percentage?mode=0&a=75&b=120
```


** Calculatrice de fraction** — ouverte uniquement


```
iconverter://tool/fraction
```


** Factorisation primaire** — ouvert uniquement


```
iconverter://tool/primeFactor
```


** SolveurQuadratique** — ouvert uniquement


```
iconverter://tool/quadraticSolver
```


**Statistiques** `iconverter://` = ensemble de données, séparé par espace / virgule / point-virgule.


```
iconverter://tool/statistics?data=1,2,3,4,5,6,7,8,9,10
```


**Combinations et permutations** — ouvert uniquement


```
iconverter://tool/combinations
```


**Géométrie** `iconverter://` = forme, `<ToolItem.rawValue>` / `text` / `input` = paramètres de dimension.

Formes disponibles : `iconverter://` · `<ToolItem.rawValue>` · `text` · `input` · `1/true/yes/on` · `0/false/no/off` · `yyyy-MM-dd` · `v` · `from` · `to` · `p` · `r` · `y` · `mode` · `salary` · `insurance` · `deduction` .

Circle (   C     = rayon):


```
iconverter://tool/geometry?shape=circle&v1=5
```


Rectangle ( `iconverter://` = longueur, `<ToolItem.rawValue>` = largeur):


```
iconverter://tool/geometry?shape=rectangle&v1=10&v2=5
```


Sphère ( `iconverter://` = rayon):


```
iconverter://tool/geometry?shape=sphere&v1=3
```


Cylindre ( `iconverter://` = rayon, `<ToolItem.rawValue>` = hauteur):


```
iconverter://tool/geometry?shape=cylinder&v1=4&v2=10
```


---

## 5. Codage

**Numéro romain** `iconverter://` = numéro arabe (1–3999); ou `<ToolItem.rawValue>` = chaîne de chiffres romains.


```
iconverter://tool/roman?n=2026
```



```
iconverter://tool/roman?roman=MMXXVI
```


**Encodeur / décoder de base64** `iconverter://` = encode/décode, `<ToolItem.rawValue>` = mode sans danger pour l'URL `text` , `input` = texte d'entrée.


```
iconverter://tool/base64?mode=encode&text=Hello%2C+World!
```



```
iconverter://tool/base64?mode=decode&urlSafe=0&text=SGVsbG8sIFdvcmxkIQ%3D%3D
```


**Encodeur URL / Décoder** `iconverter://` = encode/décode, `<ToolItem.rawValue>` = mode composant 0 = complet / 1 = requête / 2 = chemin, `text` = entrée.


```
iconverter://tool/urlCoder?mode=encode&comp=0&text=https://example.com/path?q=hello world
```



```
iconverter://tool/urlCoder?mode=decode&text=https%3A%2F%2Fexample.com%2F%3Fq%3Dhello%20world
```


** Calculatrice de masse** `iconverter://` ```
iconverter://tool/hashing?text=Hello+World&algo=sha256&upper=0
```



```
iconverter://tool/hashing?text=data&algo=md5&hmac=1&key=secret
```


**Teneur de mots** `iconverter://` = texte à analyser.


```
iconverter://tool/wordCount?text=The+quick+brown+fox+jumps+over+the+lazy+dog.
```


**Convertisseur de couleurs** `iconverter://` = couleur hexagonale; ou `<ToolItem.rawValue>` / `text` / `input` = composants RGB (0–255).


```
iconverter://tool/colorConverter?hex=%23FF8800
```



```
iconverter://tool/colorConverter?r=255&g=136&b=0
```


**Couleur Palette** – ouvert uniquement


```
iconverter://tool/colorPalette
```


**Code RRQ** `iconverter://` = contenu, `<ToolItem.rawValue>` = `text` , etc., `input` = niveau de correction des erreurs `1/true/yes/on` .


```
iconverter://tool/qrcode?text=https%3A%2F%2Fexample.com&ecc=H
```



```
iconverter://tool/qrcode?text=Hello+iConverter&format=qr&ecc=M
```


**JSON Matière** `iconverter://` = chaîne JSON (encodée par l'URL), `<ToolItem.rawValue>` = espaces de tirets 2/4.


```
iconverter://tool/jsonFormatter?text=%7B%22name%22%3A%22Alice%22%2C%22age%22%3A30%7D&indent=2
```


**Horodatage** `iconverter://` = Unix timestamp (secondes), `<ToolItem.rawValue>` = unité 0 = sec / 1 = ms; ou `text` = chaîne de date ISO8601.


```
iconverter://tool/timestamp?ts=1747440000
```



```
iconverter://tool/timestamp?iso=2026-05-17T12:00:00
```


**Validateur de carte bancaire** `iconverter://` = numéro de carte.


```
iconverter://tool/bankCard?num=6214830172816734
```


**Convertisseur de cas de texte** `iconverter://` = texte d'entrée.


```
iconverter://tool/textCase?text=hello+world+from+iConverter
```


**Diffuseur de texte** – ouvert uniquement


```
iconverter://tool/textDiff
```


** Demande de PTTS** `iconverter://` = URL de la requête, `<ToolItem.rawValue>` = GET/POST/PUT/PATCH/DELETE, `text` = corps de la requête, `input` = `1/true/yes/on` , `0/false/no/off` = en-têtes JSON.


```
iconverter://tool/httpRequest?url=https%3A%2F%2Fapi.example.com%2Fusers&method=GET
```



```
iconverter://tool/httpRequest?url=https%3A%2F%2Fapi.example.com%2Fusers&method=POST&body=%7B%22name%22%3A%22Alice%22%7D&bodyKind=json
```


**Télécharger le fichier** `iconverter://` = URL de téléchargement, `<ToolItem.rawValue>` = nom de fichier (facultatif).


```
iconverter://tool/fileDownload?url=https%3A%2F%2Fexample.com%2Freport.pdf&name=report.pdf
```


**Codes de statut du PTTS** `iconverter://` = code d'état; ou `<ToolItem.rawValue>` = mot-clé de recherche.


```
iconverter://tool/httpStatusCodes?code=404
```



```
iconverter://tool/httpStatusCodes?q=redirect
```


**Utilitaire IP** `iconverter://` = sous-net/cidr/range, `<ToolItem.rawValue>` = adresse IP, `text` = masque subnet; ou `input` = longueur du préfixe du CIDR.


```
iconverter://tool/ipUtility?mode=subnet&ip=192.168.1.0&mask=255.255.255.0
```



```
iconverter://tool/ipUtility?ip=10.0.0.0&prefix=24
```


**Tableau ASCII** `iconverter://` = point de code décimal; ou `<ToolItem.rawValue>` = point de code hexagonal; ou `text` = recherche.


```
iconverter://tool/asciiTable?dec=65
```



```
iconverter://tool/asciiTable?q=space
```


** Générateur de mots de passe** `iconverter://` = longueur, `<ToolItem.rawValue>` = majuscule, `text` , `input` = minuscule, `1/true/yes/on` , `0/false/no/off` = chiffres, `yyyy-MM-dd` , `v` = symboles, `from` , `to` = pas d'ombles ambigus, `p` , `r` = générer immédiatement, `y` .


```
iconverter://tool/passwordGenerator?length=20&upper=1&lower=1&digits=1&symbols=1&unambiguous=1&go=1
```


** Générateur de nombre de randos** `iconverter://` = minimum, `<ToolItem.rawValue>` = maximum, `text` = nombre, `input` = décimales, `1/true/yes/on` = unique `0/false/no/off` , `yyyy-MM-dd` = 0 = aucun / 1 = asc / 2 = desc, `v` = générer immédiatement `from` .


```
iconverter://tool/randomNumber?min=1&max=100&n=10&unique=1&sort=1&go=1
```



```
iconverter://tool/randomNumber?min=0&max=1&n=5&decimals=4&go=1
```


**Code principal** `iconverter://` = encode/décode, `<ToolItem.rawValue>` = texte d'entrée.


```
iconverter://tool/morseCode?mode=encode&text=SOS
```



```
iconverter://tool/morseCode?mode=decode&text=...+---+...
```


**Décoder JWT** `iconverter://` = chaîne de jeton JWT.


```
iconverter://tool/jwtParser?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c
```


**Essayez l'expression en direct** `iconverter://` = Expression Cron (les espaces peuvent être remplacés par `<ToolItem.rawValue>` ).


```
iconverter://tool/cronParser?expr=0+9+*+*+1-5
```



```
iconverter://tool/cronParser?expr=0+0+*+*+*
```


** Testeur Regex** `iconverter://` = motif régex (encodé par l'URL), `<ToolItem.rawValue>` = texte d'essai, `text` = remplacement, `input` = insensible à la casse, `1/true/yes/on` , `0/false/no/off` = multiligne, `yyyy-MM-dd` , `v` = dotall, `from` .


```
iconverter://tool/regexTester?pattern=%5Cd%2B&haystack=abc123def456&i=0
```



```
iconverter://tool/regexTester?pattern=%28%5Cw%2B%29&haystack=hello+world&replacement=%5B%241%5D&i=1
```


** Navigateur Web** `iconverter://` = ouvrir l'URL directement; ou `<ToolItem.rawValue>` = requête de recherche (utilise le moteur de recherche par défaut).


```
iconverter://tool/webBrowser?url=https%3A%2F%2Fexample.com
```



```
iconverter://tool/webBrowser?q=SwiftUI+deep+link+2026
```


---

## 6. Mode de vie

** Calculatrice de l'IMC** `iconverter://` = hauteur cm, `<ToolItem.rawValue>` = poids kg, `text` = norme 0 = Chinois adulte / 1 = OMS.


```
iconverter://tool/bmi?h=175&w=70&std=0
```


** Calculatrice BMR** `iconverter://` = hauteur cm, `<ToolItem.rawValue>` = poids kg, `text` = âge, `input` = m = mâle / f = femelle, `1/true/yes/on` = niveau d'activité 0–4, `0/false/no/off` = 0 = Harris-Benedict / 1 = Mifflin-St Jeor.


```
iconverter://tool/bmr?h=175&w=70&age=30&sex=m&act=1&formula=1
```


**Taille du vêtement** — ouvert uniquement


```
iconverter://tool/clothingSize
```


** Taille de la bague** — ouvert uniquement


```
iconverter://tool/ringSize
```


**Convertisseur de hauteur** — ouvert uniquement


```
iconverter://tool/heightConverter
```


** Calculatrice du coût du carburant** `iconverter://` = 0 = métrique / 1 = impérial, `<ToolItem.rawValue>` = distance, `text` = consommation par 100 km, `input` = prix du carburant, `1/true/yes/on` = personnes.


```
iconverter://tool/fuelCost?unit=0&d=500&c=8.5&p=7.8&n=1
```


** Calculatrice des frais d'expédition** `iconverter://` = poids réel kg, `<ToolItem.rawValue>` = premier poids kg, `text` = prix de premier poids, `input` = poids d'échelon kg, `1/true/yes/on` = prix d'échelon.


```
iconverter://tool/shippingFee?w=3.5&fw=1&ff=12&sw=1&sf=8
```


Avec le poids volumétrique ( `iconverter://` = activer `<ToolItem.rawValue>` , `text` / `input` / `1/true/yes/on` = trois côtés cm, `0/false/no/off` = diviseur):


```
iconverter://tool/shippingFee?w=2&vol=1&l=50&wd=40&h=30&div=6000&fw=1&ff=12&sw=1&sf=8
```


** Teneur en alcool (BAC)** `iconverter://` = m = mâle / f = femelle, `<ToolItem.rawValue>` = poids kg, `text` = volume mL, `input` = ABV %, `1/true/yes/on` = heures depuis la consommation.


```
iconverter://tool/alcoholBac?sex=m&w=70&v=500&abv=5&h=0.5
```


**Relations** `iconverter://` = chaîne de relations (séparée par un coma), `<ToolItem.rawValue>` = sexe ego 0 = mâle / 1 = femelle, `text` = afficher l'inverse `input` .


```
iconverter://tool/relationship?chain=f,os&sex=0&reverse=1
```



```
iconverter://tool/relationship?chain=m,ob&sex=1&reverse=0
```


**Parseur de cartes d'identité** `iconverter://` = numéro de carte d'identité.


```
iconverter://tool/idCard?id=110101199003073010
```


**Flip de monnaie** – ouvert uniquement


```
iconverter://tool/coinFlip
```


**Rouleau de dés** – ouvert uniquement


```
iconverter://tool/diceRoller
```


**Random Draw** – ouvert uniquement


```
iconverter://tool/randomDraw
```


**Spin Wheel** – ouvert uniquement


```
iconverter://tool/spinWheel
```


**Exportation de cadres vidéo** — ouvert uniquement


```
iconverter://tool/videoFrameExport
```


---

## 7. Capteurs

**Compas** – ouvert uniquement


```
iconverter://tool/compass
```


**Niveau** – ouvert uniquement


```
iconverter://tool/level
```


**Altitude** – ouvert uniquement


```
iconverter://tool/altitude
```


---

## 8. Chinois

** Numéro chinois** `iconverter://` = nombre.


```
iconverter://tool/chineseNumber?n=12345.67
```


** Numéro chinois inversé** `iconverter://` = chaîne de chiffres chinois.


```
iconverter://tool/chineseNumberReverse?text=一万二千三百四十五
```


**Montant financier** `iconverter://` = montant, `<ToolItem.rawValue>` = annexe, `text` ```
iconverter://tool/financialAmount?amount=12345.67&zheng=1
```


---

## 9. Convertisseurs d'unités

Format général : `iconverter://` = valeur, `<ToolItem.rawValue>` = unité source (rawValue ou symbole, insensible à la casse), `text` = unité cible.

---

**Durée**
Unités communes : `iconverter://` (m) · `<ToolItem.rawValue>` (km) · `text` (cm) · `input` (mm) · `1/true/yes/on` (pi) · `0/false/no/off` (in) · `yyyy-MM-dd` (mi) · `v` (yd) · `from` (nmi) · `to` (=) · `p` (=).


```
iconverter://tool/length?v=100&from=meter&to=foot
```



```
iconverter://tool/length?v=1&from=mile&to=kilometer
```


**Zone**
Unités communes : `iconverter://` (m2) · `<ToolItem.rawValue>` (ha) · `text` (acre) · `input` (ft2) · `1/true/yes/on` (mille2) · `0/false/no/off` (-) · `yyyy-MM-dd` (km2).


```
iconverter://tool/area?v=1&from=hectare&to=mu
```



```
iconverter://tool/area?v=1&from=acre&to=squareMeter
```


**Volume**
Unités communes : `iconverter://` (L) · `<ToolItem.rawValue>` (mL) · `text` (m3) · `input` (gal) · `1/true/yes/on` (fl oz) · `0/false/no/off` (cup) · `yyyy-MM-dd` (gal UK) · `v` (bbl).


```
iconverter://tool/volume?v=1&from=gallon&to=liter
```



```
iconverter://tool/volume?v=355&from=milliliter&to=fluidOunce
```


**Poids/masse**
Unités communes: `iconverter://` (kg) · `<ToolItem.rawValue>` (g) · `text` (lb) · `input` (oz) · `1/true/yes/on` (t) · `0/false/no/off` (-) · `yyyy-MM-dd` (-) · `v` (ct).


```
iconverter://tool/weight?v=1&from=pound&to=kilogram
```



```
iconverter://tool/weight?v=1&from=jin&to=gram
```


**Température**
Unités : `iconverter://` (°C) · `<ToolItem.rawValue>` (°F) · `text` (K) · `input` (°R) · `1/true/yes/on` (°Re).


```
iconverter://tool/temperature?v=100&from=celsius&to=fahrenheit
```



```
iconverter://tool/temperature?v=37&from=celsius&to=kelvin
```


**Heure**
Unités communes : `iconverter://` (s) · `<ToolItem.rawValue>` (min) · `text` (h) · `input` (jour) · `1/true/yes/on` (wk) · `0/false/no/off` (mo) · `yyyy-MM-dd` (an) · `v` (ms) · `from` (μs).


```
iconverter://tool/time?v=1&from=hour&to=second
```



```
iconverter://tool/time?v=7&from=day&to=hour
```


**Speed**
Unités : `iconverter://` (m/s) · `<ToolItem.rawValue>` (km/h) · `text` (mph) · `input` (kn) · `1/true/yes/on` (Ma).


```
iconverter://tool/speed?v=100&from=kmPerHour&to=milePerHour
```



```
iconverter://tool/speed?v=1&from=mach&to=meterPerSecond
```


**Pression**
Unités : `iconverter://` (Pa) · `<ToolItem.rawValue>` (kPa) · `text` (bar) · `input` (atm) · `1/true/yes/on` (psi) · `0/false/no/off` (mmHg).


```
iconverter://tool/pressure?v=1&from=atmosphere&to=kilopascal
```



```
iconverter://tool/pressure?v=120&from=mmHg&to=kilopascal
```


**Énergie**
Unités : `iconverter://` (J) · `<ToolItem.rawValue>` (kJ) · `text` (cal) · `input` (kcal) · `1/true/yes/on` (kWh) · `0/false/no/off` (BTU).


```
iconverter://tool/energy?v=1&from=kilowattHour&to=kilojoule
```



```
iconverter://tool/energy?v=500&from=kilocalorie&to=kilojoule
```


** Puissance**
Unités : `iconverter://` (W) · `<ToolItem.rawValue>` (kW) · `text` (hp) · `input` (PS) · `1/true/yes/on` (BTU/h).


```
iconverter://tool/power?v=1&from=hpMechanical&to=kilowatt
```



```
iconverter://tool/power?v=3000&from=watt&to=hpMetric
```


**Force**
Unités : `iconverter://` (N) · `<ToolItem.rawValue>` (kN) · `text` (kgf) · `input` (lbf) · `1/true/yes/on` (dyn).


```
iconverter://tool/force?v=9.8&from=newton&to=kgf
```



```
iconverter://tool/force?v=1&from=kilonewton&to=lbf
```


**Torque**
Unités: `iconverter://` (N·m) · `<ToolItem.rawValue>` (N·cm) · `text` (kgf·m) · `input` (ft·lb) · `1/true/yes/on` (in·lb).


```
iconverter://tool/torque?v=100&from=newtonMeter&to=footPound
```


** Fréquence**
Unités : `iconverter://` (Hz) · `<ToolItem.rawValue>` (kHz) · `text` (MHz) · `input` (GHz) · `1/true/yes/on` (THz) · `0/false/no/off` (rpm).


```
iconverter://tool/frequency?v=2.4&from=gigahertz&to=megahertz
```



```
iconverter://tool/frequency?v=3000&from=rpm&to=hertz
```


**Angle**
Unités : `iconverter://` (°) · `<ToolItem.rawValue>` (rad) · `text` (grade) · `input` (') · `1/true/yes/on` (") · `0/false/no/off` (tour).


```
iconverter://tool/angle?v=180&from=degree&to=radian
```



```
iconverter://tool/angle?v=1&from=turn&to=degree
```


** Stockage des données**
Unités : `iconverter://` (B) · `<ToolItem.rawValue>` (KB) · `text` (MB) · `input` (GB) · `1/true/yes/on` (TB) · `0/false/no/off` (KiB) · `yyyy-MM-dd` (MiB) · `v` (GiB).


```
iconverter://tool/dataStorage?v=1&from=gigabyte&to=mebibyte
```



```
iconverter://tool/dataStorage?v=512&from=mebibyte&to=gigabyte
```


** Taux de données**
Unités : `iconverter://` (bps) · `<ToolItem.rawValue>` (Kbps) · `text` (Mbps) · `input` (Gbps) · `1/true/yes/on` (KB/s) · `0/false/no/off` (MB/s) · `yyyy-MM-dd` (GB/s).


```
iconverter://tool/dataRate?v=100&from=mbps&to=mBps
```



```
iconverter://tool/dataRate?v=1&from=gbps&to=mbps
```


**Illuminance**
Unités : `iconverter://` (lx) · `<ToolItem.rawValue>` (fc) · `text` (ph) · `input` (nx).


```
iconverter://tool/illuminance?v=500&from=lux&to=footCandle
```


** Densité de flux magnétique**
Unités : `iconverter://` (T) · `<ToolItem.rawValue>` (mT) · `text` (μT) · `input` (G) · `1/true/yes/on` (mG).


```
iconverter://tool/magneticFlux?v=1&from=tesla&to=gauss
```


** Radioactivité**
Unités : `iconverter://` (Bq) · `<ToolItem.rawValue>` (kBq) · `text` (MBq) · `input` (Ci) · `1/true/yes/on` (mCi) · `0/false/no/off` (μCi).


```
iconverter://tool/radioactivity?v=1&from=curie&to=megabecquerel
```


**Viscosité**
Unités: `iconverter://` (Pa·s) · `<ToolItem.rawValue>` (mPa·s) · `text` (P) · `input` (cP).


```
iconverter://tool/viscosity?v=1&from=pascalSecond&to=centipoise
```


**Économie des combustibles**
Unités : `iconverter://` (L/100km) · `<ToolItem.rawValue>` (km/L) · `text` (MPG US) · `input` (MPG UK).


```
iconverter://tool/fuelEconomy?v=8.5&from=lPer100km&to=kmPerL
```



```
iconverter://tool/fuelEconomy?v=30&from=mpgUS&to=lPer100km
```


**Taux d'émission**
Unités : `iconverter://` (m3/s) · `<ToolItem.rawValue>` (m3/h) · `text` (L/s) · `input` (L/min) · `1/true/yes/on` (L/h) · `0/false/no/off` (gpm US) · `yyyy-MM-dd` (cfm).


```
iconverter://tool/flowRate?v=1&from=literPerMinute&to=cubicMeterPerHour
```


**Densité**
Unités : `iconverter://` (kg/m3) · `<ToolItem.rawValue>` (g/cm3) · `text` (g/L) · `input` (kg/L) · `1/true/yes/on` (lb/ft3).


```
iconverter://tool/density?v=1&from=gramPerCubicCentimeter&to=kgPerCubicMeter
```


**Flux magnétique (Wb)**
Unités : `iconverter://` (Wb) · `<ToolItem.rawValue>` (mWb) · `text` (μWb) · `input` (kWb) · `1/true/yes/on` (Mx).


```
iconverter://tool/magneticFluxTrue?v=1&from=weber&to=maxwell
```


**Dose absorbée**
Unités : `iconverter://` (Gy) · `<ToolItem.rawValue>` (mGy) · `text` (μGy) · `input` (kGy) · `1/true/yes/on` (rad) · `0/false/no/off` (mrad).


```
iconverter://tool/absorbedDose?v=1&from=gray&to=rad
```


**Dose équivalente**
Unités : `iconverter://` (Sv) · `<ToolItem.rawValue>` (mSv) · `text` (μSv) · `input` (rem) · `1/true/yes/on` (mrem).


```
iconverter://tool/equivalentDose?v=1&from=sievert&to=rem
```



```
iconverter://tool/equivalentDose?v=20&from=millisievert&to=microsievert
```


**Nombre de matières**
Unités : `iconverter://` (mol) · `<ToolItem.rawValue>` (mmol) · `text` (μmol) · `input` (kmol) · `1/true/yes/on` (nmol) · `0/false/no/off` (pmol).


```
iconverter://tool/amountOfSubstance?v=1&from=mole&to=millimole
```



```
iconverter://tool/amountOfSubstance?v=150&from=millimole&to=micromole
```


---

[Retour à iConverter Support](../) &middot; [FAQ](../faq) &middot; [Politique de confidentialité](../privacy)

</section>
<section lang="tr" markdown="1">

iConverter, `iconverter://` URL planı derin bağlantıları - dış uygulamalardan 101 araç herhangi birini açın, web sayfaları, QR kodları (generate veya **scan in-app**), Safari veya Apple Shortcuts, opsiyonel olarak önceden teslimat giriş alanları sorgu parametreleri aracılığıyla.

> **Widget notu:** **Launcher** widget aracı seçici, **Web Browser** dışında tüm desteklenen araçları içerir. Widget yapılandırma UI, **iOS sistemi dilini takip eder, ayarlar altında in-app dilinde değil.

## Protokol Doğrulaması


```
iconverter://tool/<ToolItem.rawValue>?key=value&key2=value2
```


- "<ToolItem.rawValue>", aynı ismi widget derin bağlantıları olarak paylaşıyor.
- Parametre isimleri hem kısa anahtarlar hem de eş anlamlı aliazlar (e.g. "text" 'input'a eşdeğerdir).
- Booleans: "1 / gerçek /evet /on" → gerçek; "0/false/no/off' → false.
- Tarihler: "yy.-MM-dd", ISO8601, Unix zamanıtamp (saniyeler).
- Unit dönüştürücüler ortak bir format paylaşıyor: “v’ = değer, “= kaynak ünitesinden (rawValue veya sembolü, case-in sensitive), “to’ = hedef ünitesi.

---

## 1.

**Calculator** - sadece açık sadece


```
iconverter://tool/calculator
```


**Bilimsel Hesaplama** - sadece açık


```
iconverter://tool/scientific
```


**Programmer Hesap** - sadece açık


```
iconverter://tool/programmer
```


---

## 2. Finans

**Mortgage Computing `iconverter://` = kredi miktarı, `<ToolItem.rawValue>` = yıllık oranı %, `text` = 0 = eşit taksit / 1 = eşit ana.


```
iconverter://tool/mortgage?p=1000000&r=3.7&y=30&mode=0
```


**Income Tax** `iconverter://` = aylık maaş, `<ToolItem.rawValue>` = sosyal sigorta, `text` = özel kesinti, `input` = eş, `1/true/yes/on` = yıllık bonus.


```
iconverter://tool/incomeTax?salary=20000&insurance=3000&deduction=1000&threshold=5000&bonus=50000
```


**Compound Interest** `iconverter://` = ana, `<ToolItem.rawValue>` = aylık katkı, `text` = yıllık oranı %, `input` = 0 = yıllık / 1 = aylık / 2 = günlük, `0/false/no/off` =% =%


```
iconverter://tool/compoundInterest?p=100000&m=1000&r=7&y=10&freq=1
```


**Discount `iconverter://` = 0-4, `<ToolItem.rawValue>` = orijinal fiyat, `text` = indirim oranı, `input` = eş, `1/true/yes/on` = azaltma miktarı.


```
iconverter://tool/discount?mode=0&p=299&r=8.5
```


Full-minus örneği:


```
iconverter://tool/discount?mode=3&p=350&t=300&u=50
```


**Tip & AA Split** `iconverter://` = 0 = ipucu / 1 = AA bölünmüş, `<ToolItem.rawValue>` = fatura, `text` = ipucu, `input` = vergi%, `1/true/yes/on` = insanlar say.


```
iconverter://tool/tipAA?mode=0&bill=200&tip=15&tax=0&ppl=4
```


**Mortgage Prevac** `iconverter://` = orijinal kredi, `<ToolItem.rawValue>` = yıllık oran%, `text` = toplam terim (yıllar), `input` = ücretli terimler, `1/true/yes/on` = prepay miktar, `0/false/no/off` = 0 = kısa = 1 = 1 = aylık / 2 = karşılaştırma.


```
iconverter://tool/mortgagePrepay?p=800000&r=3.7&total=30&paid=5&prepay=100000&mode=2
```


**Real Estate Tax** - sadece açık


```
iconverter://tool/realEstateTax
```


---

## 3. Tarih & Zaman

**Age & Yıldönümü** `iconverter://` = doğum günü `<ToolItem.rawValue>` , `text` = referans tarihi.


```
iconverter://tool/ageAnniversary?birth=1990-05-01&ref=2026-05-17
```


**Date Arithmetic** `iconverter://` = 0 = Add /subtract / 1 = tarih farkı.

Add-subtract modu ( `iconverter://` = başlangıç tarihi, `<ToolItem.rawValue>` = ± days, `text` = ± haftalar, `input` = ± ay, `1/true/yes/on` = ± yıl):


```
iconverter://tool/dateArithmetic?mode=0&d1=2026-05-17&d=100
```


Fark modu ( `iconverter://` = tarih 1, `<ToolItem.rawValue>` = tarih 2):


```
iconverter://tool/dateArithmetic?mode=1&d1=2026-01-01&d2=2026-12-31
```


**Lunar Takvim** `iconverter://` = Gregorian date `<ToolItem.rawValue>` .


```
iconverter://tool/lunarCalendar?date=2026-05-17
```


**Solar Şartlar** - sadece açık


```
iconverter://tool/solarTerms
```


**Countdown** `iconverter://` = event name, `<ToolItem.rawValue>` = hedef tarih `text` , `input` = zaman `1/true/yes/on` ```
iconverter://tool/countdown?label=Holiday&target=2026-10-01&time=0
```


**Pregnancy `iconverter://` = 0 = LMP / 1 = konsept / 2 = IVF, `<ToolItem.rawValue>` = referans tarihi, `text` = IVF embriyo günü 0 = D3 / 1 = D5.


```
iconverter://tool/pregnancy?method=0&ref=2026-03-01
```



```
iconverter://tool/pregnancy?method=2&ref=2026-03-15&ivf=1
```


**Erkeklertrual Cycle** `iconverter://` = son menajer dönem tarihi, `<ToolItem.rawValue>` = döngü günleri, `text` = dönem günleri.


```
iconverter://tool/menstrual?lmp=2026-05-01&cycle=28&period=5
```


**World Clock** `iconverter://` = şehir arama anahtar kelime, `<ToolItem.rawValue>` = mevcut zaman `text` , `input` = custom datetime.


```
iconverter://tool/worldClock?q=Tokyo
```



```
iconverter://tool/worldClock?now=0&ref=2026-05-17T20:00:00
```


**Zodiyak** - sadece açık


```
iconverter://tool/zodiac
```


---

## 4. Matematik 4.

**Percentage Computing** `iconverter://` = 0-4, `<ToolItem.rawValue>` = değer A, `text` = değer B.


```
iconverter://tool/percentage?mode=0&a=75&b=120
```


**Fraction Computing - sadece açık


```
iconverter://tool/fraction
```


**Prime Factorization** - sadece açık


```
iconverter://tool/primeFactor
```


**Quadratic Solver** - sadece açık


```
iconverter://tool/quadraticSolver
```


**Statistics** `iconverter://` = dataset, space / comma / yarıkol tarafından ayrı.


```
iconverter://tool/statistics?data=1,2,3,4,5,6,7,8,9,10
```


**Combinations & Permutations** - sadece açık


```
iconverter://tool/combinations
```


**Geometry** `iconverter://` = şekli, `<ToolItem.rawValue>` / `text` / `input` = boyut parametreleri.

Mevcut şekiller: `iconverter://` · `<ToolItem.rawValue>` · `text` · `1/true/yes/on` · `yyyy-MM-dd` · `v` · `v` · `to` ·  C  · `p` C   C `r` · `y` · `salary` Circle ( `iconverter://` = yarıçap):


```
iconverter://tool/geometry?shape=circle&v1=5
```


Rect Fukushima ( `iconverter://` = uzunluk, `<ToolItem.rawValue>` = genişlik):


```
iconverter://tool/geometry?shape=rectangle&v1=10&v2=5
```


Sphere ( `iconverter://` = yarıçap):


```
iconverter://tool/geometry?shape=sphere&v1=3
```


Silindir ( `iconverter://` = yarıçap, `<ToolItem.rawValue>` = yükseklik):


```
iconverter://tool/geometry?shape=cylinder&v1=4&v2=10
```


---

## 5.

**Roman Numeral** `iconverter://` = Arapça sayı (1-3999); veya `<ToolItem.rawValue>` = Roman numeral dize.


```
iconverter://tool/roman?n=2026
```



```
iconverter://tool/roman?roman=MMXXVI
```


**Base64 Encoder / Decoder** `iconverter://` = encode/decode, `<ToolItem.rawValue>` = URL-güven mod `text` , `input` = giriş text.


```
iconverter://tool/base64?mode=encode&text=Hello%2C+World!
```



```
iconverter://tool/base64?mode=decode&urlSafe=0&text=SGVsbG8sIFdvcmxkIQ%3D%3D
```


**URL Encoder / Decoder** `iconverter://` = encode/decode, `<ToolItem.rawValue>` = bileşen modu 0 = tam / 1 = sorgu / 2 = yol, `text` = giriş.


```
iconverter://tool/urlCoder?mode=encode&comp=0&text=https://example.com/path?q=hello world
```



```
iconverter://tool/urlCoder?mode=decode&text=https%3A%2F%2Fexample.com%2F%3Fq%3Dhello%20world
```


**Hash Hesaplaması** `iconverter://` = giriş, `<ToolItem.rawValue>` = md5/sha1/sha256/sha512, `text` = üstcase `input` , `1/true/yes/on` = HMAC    C  C  5               ,    C  = HMAC anahtar.


```
iconverter://tool/hashing?text=Hello+World&algo=sha256&upper=0
```



```
iconverter://tool/hashing?text=data&algo=md5&hmac=1&key=secret
```


**Word Count** `iconverter://` = analiz etmek için metin.


```
iconverter://tool/wordCount?text=The+quick+brown+fox+jumps+over+the+lazy+dog.
```


**Renk paketi ** `iconverter://` = hex color; veya `<ToolItem.rawValue>` / `text` / `input` = RGB bileşenleri (0-255).


```
iconverter://tool/colorConverter?hex=%23FF8800
```



```
iconverter://tool/colorConverter?r=255&g=136&b=0
```


**Renk Yakıtı** - sadece açık


```
iconverter://tool/colorPalette
```


**QR Kodu** `iconverter://` = içerik, `<ToolItem.rawValue>` = `text` vs., `input` = hata düzeltme seviyesi `1/true/yes/on` .


```
iconverter://tool/qrcode?text=https%3A%2F%2Fexample.com&ecc=H
```



```
iconverter://tool/qrcode?text=Hello+iConverter&format=qr&ecc=M
```


**JSON Formatter** `iconverter://` = JSON dize (URL-encoded), `<ToolItem.rawValue>` = indent Space 2/4.


```
iconverter://tool/jsonFormatter?text=%7B%22name%22%3A%22Alice%22%2C%22age%22%3A30%7D&indent=2
```


**Timestamp** `iconverter://` = Unix timestamp (saniyeler), `<ToolItem.rawValue>` = ünite 0 = gizli / 1 = ms; veya `text` = ISO8601 tarih dizesi.


```
iconverter://tool/timestamp?ts=1747440000
```



```
iconverter://tool/timestamp?iso=2026-05-17T12:00:00
```


**Bank Card Validator** `iconverter://` = kart numarası.


```
iconverter://tool/bankCard?num=6214830172816734
```


**Text Case Converter `iconverter://` = giriş metni.


```
iconverter://tool/textCase?text=hello+world+from+iConverter
```


**Text Diff ** - sadece açık


```
iconverter://tool/textDiff
```


**HTTP Request** `iconverter://` = istek URL, `<ToolItem.rawValue>` = GET/POST/PUT/PATCH/DELETE, `text` = istek vücut, `input` = `1/true/yes/on` , `0/false/no/off` = Başlıklar JSON.


```
iconverter://tool/httpRequest?url=https%3A%2F%2Fapi.example.com%2Fusers&method=GET
```



```
iconverter://tool/httpRequest?url=https%3A%2F%2Fapi.example.com%2Fusers&method=POST&body=%7B%22name%22%3A%22Alice%22%7D&bodyKind=json
```


**File Download** `iconverter://` = URL indir, `<ToolItem.rawValue>` = dosya adı (isteğe bağlı).


```
iconverter://tool/fileDownload?url=https%3A%2F%2Fexample.com%2Freport.pdf&name=report.pdf
```


**HTTP Durum Kodu** `iconverter://` = durum kodu; veya `<ToolItem.rawValue>` = arama anahtar kelime.


```
iconverter://tool/httpStatusCodes?code=404
```



```
iconverter://tool/httpStatusCodes?q=redirect
```


** `iconverter://` = subnet/cid/range, `<ToolItem.rawValue>` = IP adresi, `text` = subnet maskesi; veya `input` = CIDR prefix uzunluğu.


```
iconverter://tool/ipUtility?mode=subnet&ip=192.168.1.0&mask=255.255.255.0
```



```
iconverter://tool/ipUtility?ip=10.0.0.0&prefix=24
```


**ASCII Table** `iconverter://` = decimal codepoint; veya `<ToolItem.rawValue>` = hex codepoint; veya `text` = arama.


```
iconverter://tool/asciiTable?dec=65
```



```
iconverter://tool/asciiTable?q=space
```


**Password Jeneratör** `iconverter://` = uzunluk, `<ToolItem.rawValue>` = üstcase `text` , `input` = altcase `1/true/yes/on` , `0/false/no/off` = basamaklar `yyyy-MM-dd` C7       sembolleri = `to` = no ambiguous chars `to` = `to` = hemen `y` ```
iconverter://tool/passwordGenerator?length=20&upper=1&lower=1&digits=1&symbols=1&unambiguous=1&go=1
```


**Random Number Jeneratör ** `iconverter://` = minimum, `<ToolItem.rawValue>` = maksimum, `text` = say, `input` = decimal yerler, `1/true/yes/on` = eşsiz `yyyy-MM-dd` = 0 = 0 = 0 = 1 = asc / 2 = desc, `v` = hemen `from` = 0 = 0 = 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 = 0 0 0 = 1 = 1 = 1 = 1 = 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0


```
iconverter://tool/randomNumber?min=1&max=100&n=10&unique=1&sort=1&go=1
```



```
iconverter://tool/randomNumber?min=0&max=1&n=5&decimals=4&go=1
```


**Morse Code** `iconverter://` = encode/decode, `<ToolItem.rawValue>` = giriş metni.


```
iconverter://tool/morseCode?mode=encode&text=SOS
```



```
iconverter://tool/morseCode?mode=decode&text=...+---+...
```


**JWT Decoder** `iconverter://` = JWT token string.


```
iconverter://tool/jwtParser?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c
```


**Cron Expression Parser** `iconverter://` = Cron ifadesi (spaces, `<ToolItem.rawValue>` ile değiştirilebilir).


```
iconverter://tool/cronParser?expr=0+9+*+*+1-5
```



```
iconverter://tool/cronParser?expr=0+0+*+*+*
```


**Regex Tester** `iconverter://` = regex pattern (URL-encoded), `<ToolItem.rawValue>` = test text, `text` = değiştirme, `input` = case-in sensitive `1/true/yes/on` , `0/false/no/off` = multiline `v` = dotall    C `from` .


```
iconverter://tool/regexTester?pattern=%5Cd%2B&haystack=abc123def456&i=0
```



```
iconverter://tool/regexTester?pattern=%28%5Cw%2B%29&haystack=hello+world&replacement=%5B%241%5D&i=1
```


**Web Browser** `iconverter://` = open URL direkt olarak; veya `<ToolItem.rawValue>` = arama sorgusu (olas varsayılan arama motoru).


```
iconverter://tool/webBrowser?url=https%3A%2F%2Fexample.com
```



```
iconverter://tool/webBrowser?q=SwiftUI+deep+link+2026
```


---

## 6. Yaşam tarzı

**BMI Hesaplayıcısı `iconverter://` = yükseklik cm, `<ToolItem.rawValue>` = ağırlık kg, `text` = standart 0 = Çin yetişkin / 1 = WHO.


```
iconverter://tool/bmi?h=175&w=70&std=0
```


**BMR Hesaplaması** `iconverter://` = yükseklik cm, `<ToolItem.rawValue>` = ağırlık kg, `text` = yaş, `input` = m = erkek / f = kadın, `1/true/yes/on` = aktivite seviyesi 0-4, `0/false/no/off` = 0 = 0 = Harris-Benedict / 1 = Mifflin-St.


```
iconverter://tool/bmr?h=175&w=70&age=30&sex=m&act=1&formula=1
```


**Clothing Boyut** - sadece açık


```
iconverter://tool/clothingSize
```


**Ring Dimension** – sadece açık


```
iconverter://tool/ringSize
```


**Height Converter** - sadece açık


```
iconverter://tool/heightConverter
```


**Fuel Maliyet Hesaplayıcısı** `iconverter://` = 0 = metric / 1 = emperyal, `<ToolItem.rawValue>` = mesafe, `text` = 100 km, `input` = yakıt fiyatı, `1/true/yes/on` = insanlar.


```
iconverter://tool/fuelCost?unit=0&d=500&c=8.5&p=7.8&n=1
```


**Shipping Fee `iconverter://` = gerçek ağırlık kg, `<ToolItem.rawValue>` = ilk ağırlık kg, `text` = ilk ağırlık ücreti, `input` = adım ağırlık kg, `1/true/yes/on` = step ücreti.


```
iconverter://tool/shippingFee?w=3.5&fw=1&ff=12&sw=1&sf=8
```


volumetrik ağırlık ( `iconverter://` = `<ToolItem.rawValue>` , `text` / `input` / `1/true/yes/on` = 3 side cm, `0/false/no/off` = divisor):


```
iconverter://tool/shippingFee?w=2&vol=1&l=50&wd=40&h=30&div=6000&fw=1&ff=12&sw=1&sf=8
```


**Kan Alkol İçerik (BAC)** `iconverter://` = m = erkek / f = kadın, `<ToolItem.rawValue>` = ağırlık kg, `text` = hacim mL, `input` = ABV%, `1/true/yes/on` = saatler çünkü içki.


```
iconverter://tool/alcoholBac?sex=m&w=70&v=500&abv=5&h=0.5
```


**Relationship** `iconverter://` = ilişki zinciri (comma-separated), `<ToolItem.rawValue>` = ego seks 0 = erkek / 1 = kadın, `text` = şovu ters `input` ```
iconverter://tool/relationship?chain=f,os&sex=0&reverse=1
```



```
iconverter://tool/relationship?chain=m,ob&sex=1&reverse=0
```


**ID Card Parser** `iconverter://` = kimlik kartı numarası.


```
iconverter://tool/idCard?id=110101199003073010
```


**Coin Flip** - sadece açık


```
iconverter://tool/coinFlip
```


**Dice Roller** - sadece açık


```
iconverter://tool/diceRoller
```


**Random Draw** – sadece açık


```
iconverter://tool/randomDraw
```


**Spin Wheel** - sadece açık


```
iconverter://tool/spinWheel
```


**Video Frame Export** - sadece açık


```
iconverter://tool/videoFrameExport
```


---

## 7. Sensörler

**Compass** - sadece açık


```
iconverter://tool/compass
```


**Level** - sadece açık


```
iconverter://tool/level
```


**Altitude** - sadece açık


```
iconverter://tool/altitude
```


---

## 8. Çin Çin

**Çin Sayısı ** `iconverter://` = sayı.


```
iconverter://tool/chineseNumber?n=12345.67
```


** Çin Sayıları Ters** `iconverter://` = Çin numeral dize.


```
iconverter://tool/chineseNumberReverse?text=一万二千三百四十五
```


** Amount $** `iconverter://` = miktar, `<ToolItem.rawValue>` = append . `text` .


```
iconverter://tool/financialAmount?amount=12345.67&zheng=1
```


---

## 9. Unit Converter

Genel format: `iconverter://` = değer, `<ToolItem.rawValue>` = kaynak ünitesi (rawValue veya sembolü, case-in sensitive), `text` = hedef ünitesi.

---

**Length**
Ortak birimler: `iconverter://` (m) · `<ToolItem.rawValue>` (km) · `v` (yd) ·    C  (nmi) · `to` (ft)


```
iconverter://tool/length?v=100&from=meter&to=foot
```



```
iconverter://tool/length?v=1&from=mile&to=kilometer
```


** Area**
Ortak birimler: `iconverter://` (m2) · `<ToolItem.rawValue>` (ha) · `text` (acre) · `input` (ft2)


```
iconverter://tool/area?v=1&from=hectare&to=mu
```



```
iconverter://tool/area?v=1&from=acre&to=squareMeter
```


**Volume**
Ortak birimler: `iconverter://` (L) · `<ToolItem.rawValue>` (mL) · `text` (m3) · `input` (gal) · `1/true/yes/on` (fl oz)


```
iconverter://tool/volume?v=1&from=gallon&to=liter
```



```
iconverter://tool/volume?v=355&from=milliliter&to=fluidOunce
```


**Weight / Mass**
Ortak birimler: `iconverter://` (kg) · `<ToolItem.rawValue>` (g) · `text` (lb) · `input` (oz) · `1/true/yes/on` (t) · `0/false/no/off` (斤)


```
iconverter://tool/weight?v=1&from=pound&to=kilogram
```



```
iconverter://tool/weight?v=1&from=jin&to=gram
```


**Temperature**
Birimler: `iconverter://` (°C) · `<ToolItem.rawValue>` (°F) · `text` (K) · `input` (°R)


```
iconverter://tool/temperature?v=100&from=celsius&to=fahrenheit
```



```
iconverter://tool/temperature?v=37&from=celsius&to=kelvin
```


**Time**
Ortak birimler: `iconverter://` (s) · `<ToolItem.rawValue>` (min) · `text` (h) · `input` (gün) · `1/true/yes/on` (wk) · `0/false/no/off` (mo) · `yyyy-MM-dd` C7  (yr)


```
iconverter://tool/time?v=1&from=hour&to=second
```



```
iconverter://tool/time?v=7&from=day&to=hour
```


**Speed**
Birimler: `iconverter://` (m/s) · `<ToolItem.rawValue>` (km/h) · `text` (mph) · `input` (kn)


```
iconverter://tool/speed?v=100&from=kmPerHour&to=milePerHour
```



```
iconverter://tool/speed?v=1&from=mach&to=meterPerSecond
```


**Basın
Birimler: `iconverter://` (Pa) · `<ToolItem.rawValue>` (kPa) · `text` (bar) · `input` (atm) · `1/true/yes/on` (psi)


```
iconverter://tool/pressure?v=1&from=atmosphere&to=kilopascal
```



```
iconverter://tool/pressure?v=120&from=mmHg&to=kilopascal
```


**Energy**
Birimler: `iconverter://` (J) · `<ToolItem.rawValue>` (kJ) · `text` (cal) · `1/true/yes/on` (kWh) · `0/false/no/off` (BTU).


```
iconverter://tool/energy?v=1&from=kilowattHour&to=kilojoule
```



```
iconverter://tool/energy?v=500&from=kilocalorie&to=kilojoule
```


**Power**
Birimler: `iconverter://` (W) · `<ToolItem.rawValue>` (kW) · `text` (hp) · `input` (PS) · `1/true/yes/on` (BTU/h).


```
iconverter://tool/power?v=1&from=hpMechanical&to=kilowatt
```



```
iconverter://tool/power?v=3000&from=watt&to=hpMetric
```


**Force**
Birimler: `iconverter://` (N) · `<ToolItem.rawValue>` (kN) · `text` (kgf) · `input` (lbf) · `1/true/yes/on` (dyn).


```
iconverter://tool/force?v=9.8&from=newton&to=kgf
```



```
iconverter://tool/force?v=1&from=kilonewton&to=lbf
```


**Torque**
Birimler: `iconverter://` (N·m) · `<ToolItem.rawValue>` (N·cm) · `text` (kgf·m)


```
iconverter://tool/torque?v=100&from=newtonMeter&to=footPound
```


**Frequency**
Birimler: `iconverter://` (Hz) · `<ToolItem.rawValue>` (kHz) · `text` (fil) · `input` (gir) · `1/true/yes/on` (THz)


```
iconverter://tool/frequency?v=2.4&from=gigahertz&to=megahertz
```



```
iconverter://tool/frequency?v=3000&from=rpm&to=hertz
```


**Angle**
Birimler: `iconverter://` (°) · `<ToolItem.rawValue>` (rad) · `text` (grad) · `input` () · `1/true/yes/on` ()


```
iconverter://tool/angle?v=180&from=degree&to=radian
```



```
iconverter://tool/angle?v=1&from=turn&to=degree
```


**Data Storage**
Birimler: `iconverter://` (B) · `<ToolItem.rawValue>` (KB) · `text` (MB) · `input` (GB) · `1/true/yes/on` (TB)


```
iconverter://tool/dataStorage?v=1&from=gigabyte&to=mebibyte
```



```
iconverter://tool/dataStorage?v=512&from=mebibyte&to=gigabyte
```


**Data Rate**
Birimler: `iconverter://` (bps) · `<ToolItem.rawValue>` C2    (Mbps) · `input` (Gbps) · `1/true/yes/on` (KB/ `0/false/no/off` )


```
iconverter://tool/dataRate?v=100&from=mbps&to=mBps
```



```
iconverter://tool/dataRate?v=1&from=gbps&to=mbps
```


**Illuminance**
Birimler: `iconverter://` (lx) · `<ToolItem.rawValue>` (fc) · `text` (ph) · `input` (nx).


```
iconverter://tool/illuminance?v=500&from=lux&to=footCandle
```


**Magnetic Flux Mechanic**
Birimler: `iconverter://` (T) · `<ToolItem.rawValue>` (mT) · `text` (μT) · `input` (G) · `1/true/yes/on` ```
iconverter://tool/magneticFlux?v=1&from=tesla&to=gauss
```


** Radyoaktivite**
Birimler: `iconverter://` (Bq) · `<ToolItem.rawValue>` (kBq) · `text` C3    (Ci) · `1/true/yes/on` (mC)


```
iconverter://tool/radioactivity?v=1&from=curie&to=megabecquerel
```


**Viscosity**
Birimler: `iconverter://` (Pa·s) · `<ToolItem.rawValue>` (mPa·s) · `text` (P) · `input` (cP).


```
iconverter://tool/viscosity?v=1&from=pascalSecond&to=centipoise
```


**Fuel Ekonomisi**
Birimler: `iconverter://` (L/100km) · `<ToolItem.rawValue>` (km/L) · `text` (MPG US) · `input` (MPG UK).


```
iconverter://tool/fuelEconomy?v=8.5&from=lPer100km&to=kmPerL
```



```
iconverter://tool/fuelEconomy?v=30&from=mpgUS&to=lPer100km
```


**Flow Oranı**
Birimler: `iconverter://` (m3/s) · `<ToolItem.rawValue>` C2    (L/s) · `input` (L/min)


```
iconverter://tool/flowRate?v=1&from=literPerMinute&to=cubicMeterPerHour
```


**Density**
Birimler: `iconverter://` (kg/m3) · `<ToolItem.rawValue>` (g/cm3) · `text` (g/L) · `input` (kg/L)


```
iconverter://tool/density?v=1&from=gramPerCubicCentimeter&to=kgPerCubicMeter
```


**Magnetic Flux (Wb)**
Birimler: `iconverter://` (Wb) · `<ToolItem.rawValue>` (mWb)


```
iconverter://tool/magneticFluxTrue?v=1&from=weber&to=maxwell
```


**Absorbed Dose**
Birimler: `iconverter://` (Gy) · `<ToolItem.rawValue>` (mGy) · `text` (μGy) · `input` (kGy)


```
iconverter://tool/absorbedDose?v=1&from=gray&to=rad
```


**Equivalent Dose**
Birimler: `iconverter://` (Sv) · `<ToolItem.rawValue>` (mSv) · `text` (μSv) · `input` (rem)


```
iconverter://tool/equivalentDose?v=1&from=sievert&to=rem
```



```
iconverter://tool/equivalentDose?v=20&from=millisievert&to=microsievert
```


** Substance**
Birimler: `iconverter://` (mol) · `<ToolItem.rawValue>` (mmol) · `text` (μmol) · `1/true/yes/on` (nmol)


```
iconverter://tool/amountOfSubstance?v=1&from=mole&to=millimole
```



```
iconverter://tool/amountOfSubstance?v=150&from=millimole&to=micromole
```


---

[Back to iConverter Support](./) &middot; [FAQ](./faq) &middot; [Privacy Policy](./privacy)

</section>
