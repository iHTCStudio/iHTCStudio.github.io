ISSage รองรับ ** `isage://` BAR * ลิงก์ลัด (RUL scheme) การเริ่มหน้าจอหน้าจอเย็นและหน้าจอบ้าน จะถูกส่งไปผ่านระบบบัฟเฟอร์แบบรวม ดังนั้นลิงก์จึงไม่ถูกเปิดสองครั้งหลังจากขึ้นเครื่อง

## รูปแบบลิงก์


```
isage://{host}?{params}
```


## คําพูดและผู้เขียน

| URL | เปิด |
|-----|-------|
| `isage://passage?id={id}` | บอกรายละเอียด |
| `isage://saying?id={id}` / `isage://couplet?id={id}` / `isage://poem?id={id}` | เช่นเดียวกันกับเนื้อเรื่อง (ความเข้ากันได้) |
| `isage://passage?id={id}&card=1` | พูดถึงเรื่องรายละเอียดและไพ่เซจ |
| `isage://card?id={id}` / `isage://share-card?id={id}` | ไพ่เซจ |
| `isage://author?id={id}` | รายละเอียดผู้แต่ง |
| `isage://recite` / `isage://recite?id={id}` | โฟลว์การท่อง |

## การท่องเว็บ

| URL | เปิด |
|-----|-------|
| `isage://home` | หน้าแรก |
| `isage://daily` | สติ ปัญญา ใน ปัจจุบัน |
| `isage://random` | สุ่มพูดว่า |
| `isage://favorites` | รายการโปรด |
| `isage://famous` | บรรทัดขึ้นชื่อ |
| `isage://search` / `isage://search?q={query}` | ค้นหา |
| `isage://study` / `isage://study?id={id}` | โรงเรียนเซจ |
| `isage://hunt` | เซจ ฮันท์ ('คีย์เวิร์ด-ฮันต์' / 'ดอกไม้แมลงวัน') |
| `isage://handwriting` | สืบค้นเมื่อเขียนด้วยมือ ('เขียนเอง'; OS) |
| `isage://mastered` | สําเร็จการศึกษาแล้ว ('รุก') |
| `isage://categories` / `isage://categories?section=` | เรียกดู |
| `isage://collection?id=guxun` | Resension คลาสสิก ('Zo-sange' / woo-xia'; และยัง 'Book' / image') |
| `isage://corpus` | ทุกคําพูด (ทั้งหมด) |
| `isage://theme?id=conduct` | ธีม (e.g. สืบค้นเมื่อ: Urdin', attendin', oh House Hollowe', UNVRUMRURUMOUMRUMOUMRESCOUMRESCOUMRESCIORESEIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII ONTHCORESCIIIIIIIIIIIIIIIIIIIIIIIIII] |
| `isage://last-read` | รายการที่อ่านล่าสุด |
| `isage://reading-history` | ประวัติการอ่าน |
| `isage://notes` | บันทึก |

## การตั้งค่าและคู่มือ

| URL | เปิด |
|-----|-------|
| `isage://settings` | การตั้งค่า |
| `isage://usage-guide` | คู่มือการใช้งาน |
| `isage://widget-guide` | คู่มือวิดเจ็ต |
| `isage://shortcuts-guide` | คู่มือทางลัด |
| `isage://feature-guide` | เล่นทัวร์แนะนำอีกครั้ง |
| `isage://feedback` | อีเมลข้อเสนอแนะ |
| `isage://in-app-review` | รีวิวในแอป / App Store |

## ตัวอย่าง


```
isage://daily
isage://passage?id=1
isage://passage?id=1&card=1
isage://collection?id=guxun
isage://theme?id=conduct
isage://study
isage://hunt
isage://handwriting
```


## บันทึก

- พารามิเตอร์คือความไวของตัวเลข
- ไซรี, ทางลัด, วิดเจ็ต, และศูนย์ควบคุม ใช้เส้นทางลับเดียวกัน
- ดู In-appings-Cettings softs for the list ล่าสุด


