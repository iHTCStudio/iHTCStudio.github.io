IXin รองรับ ** `ixin://` BAR * ลิงก์ลัด (RUL scheme) การเริ่มหน้าจอหน้าจอเย็นและหน้าจอบ้าน จะถูกส่งไปผ่านระบบบัฟเฟอร์แบบรวม ดังนั้นลิงก์จึงไม่ถูกเปิดสองครั้งหลังจากขึ้นเครื่อง

## รูปแบบลิงก์


```
ixin://{host}?{params}
```


## ผู้เขียน

| URL | เปิด |
|-----|-------|
| `ixin://passage?id={id}` | รายละเอียดข้อความ |
| `ixin://saying?id={id}` / `ixin://couplet?id={id}` / `ixin://poem?id={id}` | เช่นเดียวกันกับเนื้อเรื่อง (ความเข้ากันได้) |
| `ixin://passage?id={id}&card=1` | รายละเอียดและนามบัตร |
| `ixin://card?id={id}` / `ixin://share-card?id={id}` | ไพ่สําหรับ หยั่ง เห็น |
| `ixin://author?id={id}` | รายละเอียดผู้แต่ง |
| `ixin://recite` / `ixin://recite?id={id}` | โฟลว์การท่อง |

## การท่องเว็บ

| URL | เปิด |
|-----|-------|
| `ixin://home` | หน้าแรก |
| `ixin://daily` | การ หยั่ง เห็น เข้าใจ ทุก วัน |
| `ixin://random` | ข้อความแบบสุ่ม |
| `ixin://favorites` | รายการโปรด |
| `ixin://famous` | บรรทัดขึ้นชื่อ |
| `ixin://search` / `ixin://search?q={query}` | ค้นหา |
| `ixin://study` / `ixin://study?id={id}` | โรงเรียนหัวใจ |
| `ixin://hunt` | หัวใจล่า ('คําพยัญชนะ' / 'ดอกไม้แมลงวัน') |
| `ixin://handwriting` | สืบค้นเมื่อเขียนด้วยมือ ('เขียนเอง'; OS) |
| `ixin://mastered` | สําเร็จการศึกษาแล้ว ('รุก') |
| `ixin://categories` / `ixin://categories?section=` | เรียกดู |
| `ixin://collection?id=` | เครื่องราชอิสริยาภรณ์ / หนังสือ (อังกฤษ) |
| `ixin://corpus` | ทุกช่อง (ทั้งหมด) |
| `ixin://last-read` | รายการที่อ่านล่าสุด |
| `ixin://reading-history` | ประวัติการอ่าน |
| `ixin://notes` | บันทึก |
| `ixin://journal` | บันทึกประจําวันที่ใช้ร่วม |
| `ixin://liangzhi` | คํา ถาม สาม ข้อ ของ ลี ยง ซิ |
| `ixin://graph` | เส้นพริ้วไหว |
| `ixin://timeline` | เส้นต่อเนื่อง / เส้นเวลา |
| `ixin://map` | แผนที่ |
| `ixin://people` | ผู้คน |
| `ixin://achievements` | คุณสมบัติต่าง ๆ |
| `ixin://theme?id=` | ชุดตกแต่ง |

## การตั้งค่าและคู่มือ

| URL | เปิด |
|-----|-------|
| `ixin://settings` | การตั้งค่า |
| `ixin://usage-guide` | คู่มือการใช้งาน |
| `ixin://widget-guide` | คู่มือวิดเจ็ต |
| `ixin://shortcuts-guide` | คู่มือทางลัด |
| `ixin://feature-guide` | เล่นทัวร์แนะนำอีกครั้ง |
| `ixin://feedback` | อีเมลข้อเสนอแนะ |
| `ixin://in-app-review` | รีวิวในแอป / App Store |

## ตัวอย่าง


```
ixin://daily
ixin://passage?id=1
ixin://journal
ixin://liangzhi
ixin://collection?id=chuanxilu
ixin://study
ixin://hunt
```


## บันทึก

- พารามิเตอร์คือความไวของตัวเลข
- ไซรี, ทางลัด, วิดเจ็ต, และศูนย์ควบคุม ใช้เส้นทางลับเดียวกัน
- ดู In-appings-Cettings softs for the list ล่าสุด


