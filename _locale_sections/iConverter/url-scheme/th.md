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


