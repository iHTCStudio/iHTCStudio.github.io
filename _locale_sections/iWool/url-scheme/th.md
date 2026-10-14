ivol รองรับ~ `iwool://` BAR ~ ที่อยู่ URL กําหนดที่อยู่เชื่อมโยงแบบลึก — เปิดแท็บ, เริ่มการเรียกใช้งานโปรแกรมในการใช้งาน, หรือกระโดดไปยังกิจกรรมเฉพาะจากซาฟารี, ปุ่มพิมพ์ลัดของแอปเปิล, แท็บวิดเจ็ต, หรือการกระทําด่วนของหน้าจอส่วนตัว (ยาว- กดไอคอนโปรแกรม)

> ~! ~ เชื่อมโยงลึกเท่านั้น... .... พวกเขาไม่ได้สร้างการเชื่อมต่อของแม่ข่ายหรือปรับเทียบข้อมูลกับข้อมูลบนก้อนเมฆ

## การกําหนดโพรโทคอล


```
iwool://<path>[?query]
```


| Rule | รายละเอียด |
|------|--------|
| **Scheme** | 'Oiวูล' (ตัวอ่อน) |
| **Routing** | พาธในช่วงแรก (เครื่องหรือพาธ) เลือกปลายทาง |
| **Empty URL** | ~ไม่มีเส้นทาง~ |
| **Unknown paths** | ~ถูกเปิดโปง~ |
| **Parser** | 'I Woodl Deeplink.parse(:):'''OfftitleView. apply Deeplink' |

---

## 1. ปลายทางแท็บ

| URL | เปิด |
|-----|--------|---------|
| `iwool://home` | **Home** tab | — |
| `iwool://calendar` | **Calendar** tab | 'Cal' |
| `iwool://stats` | **Statistics** tab | อัลกอริอะฮ์ |
| `iwool://settings` | **Settings** tab | (จะมีคําบัญชาแก่มะลาอิกะฮฺว่า) จงนําเขาไป |

---

## 2. การกระทําในการเรียกใช้

เส้นทางเหล่านี้ตรงกัน ~Home screen securication ~ และเปิดแผ่นหรือหน้าย่อย:

| URL | เปิด |
|-----|--------|---------|
| `iwool://new` | **Create activity** sheet | จงสร้าง, จง, จง, จง, จง, จง... |
| `iwool://island` | **Quick Countdown** (Dynamic Island reminder) sheet | ISland-reminder', islandreminder', searchdown', queck-countdown ', queckclown' |
| `iwool://reminders` | **Scheduled local reminders** list (Settings) | 'reculted-reminders', "'recreduledminds',"','ประกาศประกาศ' |
| `iwool://scanner` | **QR / barcode scanner** (Settings → Tools) | 'Scan', 'Crcode', 'บาร์โค้ด' |
| `iwool://rate` | In-app **App Store rating** prompt | จงประกาศอย่างเปิดเผย |
| `iwool://feedback` | **Feedback** email compose | 'อีเมล' "ช่วยเหลือ' |

** พาธการตั้งค่าที่ฝังอยู่ **


```
iwool://settings/scanner
iwool://settings/reminders
iwool://settings/rate
iwool://settings/feedback
```


---

## 3. รายละเอียดกิจกรรม

เปิดกิจกรรมขนสัตว์เพียงตัวเดียวโดยใช้หมายเลขฐานข้อมูล

| Parameter | Required | คําอธิบาย |
|-----------|----------|-------------|
| Path `event/{id}` | One of path / query | หมายเลขประจํากิจกรรม (จํานวนเต็มบวก) |
| Query `id={id}` | One of path / query | เหมือนกับรูปแบบพาธ |
| Query `day={seconds}` | No | 2551 สําหรับกิจกรรมที่ตามมานี้ -- การเริ่มต้นของวันตามธรรมชาติคือ 'Timetervalue ตั้งแต่ปี ค.ศ. |

** เปิดกิจกรรม 42*


```
iwool://event/42
iwool://event?id=42
```


~ เกิดขึ้นอีกในวันพิเศษ~


```
iwool://event/42?day=189345600
```


เมื่อสร้างลิงก์สําหรับอนุกรมซ้ํา, ivol สามารถหา `iwool://` จากตรรกะเดียวกับรายการที่บ้าน ( `iwool` )

---

## 4. การกระทําด่วนของหน้าจอส่วนตัว (ไอOS)

กดยาวไอคอน ivill ถึง 4 การกระทํา ปรับค่าเองใน ~ ตั้งค่าเครื่องมือ ○ จอภาพส่วนตัว ~ (9 ตัวเลือก, ลากเพื่อทําการเรียงใหม่, ตั้งใหม่เป็นค่าปริยาย)

| Option | ที่อยู่ URL |
|--------|-----|
| Home | บ้าน |
| Calendar | ~โอ้~ |
| Statistics | ~โอ้วววว~ |
| Quick Countdown | ~~~~~~~ ~โอ~ |
| New Activity | ~โอ้~ |
| Scheduled Reminders | 'Oivolreminders' |
| Scanner | ~ฮู้วววว~ |
| Rate App | ~โอ้~ |
| Feedback | 'เอาอาหารกลับมา' |

~Deflobal on the first ติดตั้ง: ~ปฏิทิน Home althythys atsized ethody lognown.

ทําเร็ว `iwool://` สตริง ใช้  c1 th thath thath ath ath ath พาธและเส้นทางผ่าน  c2  p       /C3   th on cold start.

---

## 5. วิดเจ็ตลิงก์ลึก

เสียงเคาะของวิดเจ็ตใช้ที่อยู่ URL แบบเดียวกัน `iwool://` BAR :

| Widget | Tap target | ที่อยู่ URL |
|--------|------------|-----|
| Today Active / Today All / Today Upcoming / All Events | Home | บ้าน |
| Stats Overview / Earnings / Top Platforms | Statistics | ~โอ้วววว~ |
| Glance | First event or Home | 'Offict=////////////////////////////////////ค่ะ |
| Lock Screen accessories | First event or Home | 'Offict=////////////////////////////////////ค่ะ |
| List row (iOS 17+) | Activity detail | ~ |

Office Tountown Life ใช้เฉพาะที่อยู่ URL แบบย่อเท่านั้น -- ~ ไม่แยกที่อยู่ URL * เพื่อเริ่มการนับถอยหลังของเกาะจากด้านนอกโปรแกรม (ใช้  c0     เพื่อเปิดแผ่นการสร้าง)

---

## ตัวอย่างปุ่มพิมพ์ลัดของแอปเปิล

~สถิติเปิด! ~


```
iwool://stats
```


~ จงสร้างกิจกรรมใหม่~


```
iwool://new
```


~ เปิดแผ่นงานด่วน~


```
iwool://island
```


** เปิดกิจกรรม หลังจากคัดลอกหมายเลข **


```
iwool://event?id=42
```


---

## เรียกใช้พฤติกรรม

| Scenario | ลื่นไถล |
|----------|------|
| **Widget / Shortcuts `onOpenURL`** | 'AppRouter' →'Apply Deep เชื่อมโยง |
| **Cold start — Quick Action** | 'SepteneDeledge' ''''''''hending Proughs Broffer' ~'helpter' |
| **Warm start — Quick Action** | ฉากเรียกกลับ → สืบค้นเมื่อ 'OHE' |
| **Feedback / Rate (cold start)** | หน่วงเวลาสั้นดังนั้นตารางจดหมาย / ร้านค้า kit มีหน้าต่างที่ทํางานอยู่ |
| **Invalid event ID** | ลิ้งค์ ถูก ละเลย — ไม่ มี การ ตื่น ตัว |

---

## การยิงปัญหา

| Issue | จะตรวจอะไร |
|-------|----------------|
| Link opens app but nothing happens | พาธต้องตรงกับเส้นทางที่รองรับ; พาธที่ไม่รู้จักไม่ได้หันไปบ้าน |
| `event` link shows wrong occurrence | เพิ่ม '%? วัน=' สําหรับกิจกรรมที่เกิดขึ้นซ้ํา |
| Quick Action does nothing on cold launch | รอ ~0. 4 s หรือลองใหม่; การแจ้งข้อมูล/ peri ต้องการเวลาแบบ UI |
| `iwool://island` does not start countdown automatically | เปิดแผ่นอาหาร -- ยืนยันระยะเวลาและการเคาะเริ่มต้นภายในแอพ |
| Quick Countdown requires iOS 16.2+ | Event Life Office ต้องการ OS 16.1+; การนับถอยหลังของเกาะเดี่ยวต้องการ 16.2+ |

---

[การรองรับ iWoll] [. ] [FAQ] (./faq) สืบค้นเมื่อ 27 พฤษภาคม พ.ศ.


