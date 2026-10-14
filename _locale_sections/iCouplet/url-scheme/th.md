ICuplet รองรับ} `icouplet://` BAR * ลิงก์ลัด (URL scheme) การเริ่มหน้าจอหน้าจอเย็นและหน้าจอบ้าน จะถูกส่งไปผ่านระบบบัฟเฟอร์แบบรวม ดังนั้นลิงก์จึงไม่ถูกเปิดสองครั้งหลังจากขึ้นเครื่อง

## รูปแบบลิงก์


```
icouplet://{host}?{params}
```


## ผู้เขียนคู่

| URL | เปิด |
|-----|-------|
| `icouplet://couplet?id={id}` | รายละเอียดคู่ |
| `icouplet://poem?id={id}` | แบบคู่เดียวกัน (ชื่อแฟ้มที่เข้ากันได้) |
| `icouplet://author?id={id}` | ผู้เขียน (联家) รายละเอียด |
| `icouplet://recite` | การไหลของเสียง (อัตโนมัติเมื่อเป็นไปได้) |
| `icouplet://recite?id={id}` | เปิดคู่คู่และรีเซ็ตอัตโนมัติ |

## ค้นพบ

| URL | เปิด |
|-----|-------|
| `icouplet://home` | แท็บหน้าแรก |
| `icouplet://daily` | ทุก วัน นี้ |
| `icouplet://random` | สุ่มคู่ |
| `icouplet://favorites` | รายการโปรด |
| `icouplet://famous` | รายการบรรทัดที่มีชื่อเสียง |
| `icouplet://search` | ค้นหา |
| `icouplet://search?q={query}` | ค้นหาพร้อมคำค้น |
| `icouplet://study` | การ ศึกษา / ○ การ เข้า ร่วม |
| `icouplet://categories` | ประเภทการเรียกดู |
| `icouplet://categories?section=form` | Form (体裁) ตอน |
| `icouplet://categories?section=theme` | หัวข้อชุดตกแต่ง |
| `icouplet://categories?section=author` | ส่วนของผู้เขียน |
| `icouplet://categories?section=famous` | ส่วนบรรทัดที่มีชื่อเสียง |
| `icouplet://categories?section=corpus` | ชุดสะสม / คอร์ปัส |
| `icouplet://last-read` | คู่ที่อ่านล่าสุด |
| `icouplet://reading-history` | ประวัติการอ่าน |

## การตั้งค่าและคู่มือ

| URL | เปิด |
|-----|-------|
| `icouplet://settings` | ตั้งค่าราก |
| `icouplet://usage-guide` | คู่มือการใช้งาน |
| `icouplet://widget-guide` | คู่มือวิดเจ็ต |
| `icouplet://shortcuts-guide` | คู่มือทางลัด |
| `icouplet://feature-guide` | แสดงคุณสมบัติบนระบบอีกครั้ง |
| `icouplet://feedback` | อีเมลข้อเสนอแนะ |
| `icouplet://in-app-review` | รีวิวในแอป / App Store |

## ตัวอย่าง


```
icouplet://daily
icouplet://couplet?id=1
icouplet://recite?id=1
icouplet://search?q=春
icouplet://categories?section=famous
icouplet://widget-guide
```


ใช้เหล่านี้ในโปรแกรมปุ่มพิมพ์ลัด, การกระทําของหน้าจอส่วนตัวอย่างรวดเร็ว, วิดเจ็ต, หรือ Saveri ดูใน-apps ด้วย


