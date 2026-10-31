Iclient รองรับ} `ibible://` BAR * ทางลัดลิงก์สําหรับปุ่มพิมพ์ลัด, วิดเจ็ต, Siri และการกระทําหน้าจอส่วนตัว

## รูปแบบลิงก์


```
ibible://{host}?{params}
```


## การอ่านทุกวัน

| URL | เปิด |
|-----|-------|
| `ibible://today` or `ibible://daily` | ข้อ คัมภีร์ ใน ปัจจุบัน |
| `ibible://random` | สุ่มข้อความ |
| `ibible://verse?b=43&c=3&v=16` | ข้อ คัมภีร์ เฉพาะ (หนังสือ / บท / ข้อ) |
| `ibible://chapter?b=43&c=3` | โปรแกรมอ่านบท |
| `ibible://read` | เริ่มอ่านได้ (วันนี้ถ้าไม่มีท่อน) |
| `ibible://read?b=19&c=23&v=1` | อ่าน ออก เสียง ข้อ |
| `ibible://last-read` | ทําต่อไปในบทสุดท้าย |
| `ibible://reading-history` | ประวัติการอ่าน |

## เรียกดูการศึกษา

| URL | เปิด |
|-----|-------|
| `ibible://book?id=43` | หนังสือ (1–66) |
| `ibible://topics` | หัวข้อทั้งหมด |
| `ibible://topic?id=love` | แสดงรายละเอียด |
| `ibible://famous` | ข้อ คัมภีร์ ที่ มี ชื่อ เสียง |
| `ibible://plans` | กําลังอ่านแผน |
| `ibible://plan?id=beginner7` | แผนเฉพาะ |
| `ibible://favorites` | รายการโปรด |
| `ibible://search?q=love` | ค้นหา |

## การตั้งค่าและคู่มือ

| URL | เปิด |
|-----|-------|
| `ibible://home` | หน้าแรก |
| `ibible://settings` | การตั้งค่า |
| `ibible://usage-guide` | คู่มือการใช้งาน |
| `ibible://widget-guide` | คู่มือวิดเจ็ต |
| `ibible://shortcuts-guide` | คู่มือทางลัด |
| `ibible://feature-guide` | การเดินทัวร์แบบธรรมชาติ |
| `ibible://feedback` | แหล่งป้อน |

จํานวนหนังสือเป็นไปตามระเบียบของโปรเตสแตนต์ (1 = เยเน ซิศ... 66 =พระธรรมวิวรณ์).


