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


