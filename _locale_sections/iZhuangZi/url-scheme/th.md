i Zhuang Zi รองรับ~ `izhuangzi://` BAR * ลิงก์ลัด (URL scheme) การเริ่มหน้าจอหน้าจอเย็นและหน้าจอบ้าน จะถูกส่งไปผ่านระบบบัฟเฟอร์แบบรวม ดังนั้นลิงก์จึงไม่ถูกเปิดสองครั้งหลังจากขึ้นเครื่อง

## รูปแบบลิงก์


```
izhuangzi://{host}?{params}
```


## ผู้เขียน

| URL | เปิด |
|-----|-------|
| `izhuangzi://passage?id={id}` | รายละเอียดข้อความ |
| `izhuangzi://saying?id={id}` / `izhuangzi://couplet?id={id}` / `izhuangzi://poem?id={id}` | เช่นเดียวกันกับเนื้อเรื่อง (ความเข้ากันได้) |
| `izhuangzi://passage?id={id}&card=1` | รายละเอียดและนามบัตร |
| `izhuangzi://card?id={id}` / `izhuangzi://share-card?id={id}` | ○ การ์ด |
| `izhuangzi://author?id={id}` | รายละเอียดผู้แต่ง |
| `izhuangzi://recite` / `izhuangzi://recite?id={id}` | โฟลว์การท่อง |

## การท่องเว็บ

| URL | เปิด |
|-----|-------|
| `izhuangzi://home` | หน้าแรก |
| `izhuangzi://daily` | เดลีซ็องซี |
| `izhuangzi://random` | ข้อความแบบสุ่ม |
| `izhuangzi://favorites` | รายการโปรด |
| `izhuangzi://famous` | บรรทัดขึ้นชื่อ |
| `izhuangzi://search` / `izhuangzi://search?q={query}` | ค้นหา |
| `izhuangzi://study` / `izhuangzi://study?id={id}` | การ ศึกษา |
| `izhuangzi://hunt` | Zhuung Hunt ('คีย์เวิร์ด-ฮันต์' / 'ดอกไม้แมลงวัน') |
| `izhuangzi://handwriting` | สืบค้นเมื่อเขียนด้วยมือ ('เขียนเอง'; OS) |
| `izhuangzi://mastered` | สําเร็จการศึกษาแล้ว ('รุก') |
| `izhuangzi://categories` / `izhuangzi://categories?section=` | เรียกดู |
| `izhuangzi://collection?id=` | คอลเลคชั่น / หนังสือ (อังกฤษ) |
| `izhuangzi://corpus` | ทุกช่อง (ทั้งหมด) |
| `izhuangzi://last-read` | รายการที่อ่านล่าสุด |
| `izhuangzi://reading-history` | ประวัติการอ่าน |
| `izhuangzi://notes` | บันทึก |
| `izhuangzi://ask` | ถามซ็องซี |
| `izhuangzi://allegories` | สี่เหลี่ยม |
| `izhuangzi://concepts` | จับภาพ |
| `izhuangzi://theme?id=neipian` | ภายใน / ภายนอก / เบ็ดเตล็ด |

## การตั้งค่าและคู่มือ

| URL | เปิด |
|-----|-------|
| `izhuangzi://settings` | การตั้งค่า |
| `izhuangzi://usage-guide` | คู่มือการใช้งาน |
| `izhuangzi://widget-guide` | คู่มือวิดเจ็ต |
| `izhuangzi://shortcuts-guide` | คู่มือทางลัด |
| `izhuangzi://feature-guide` | เล่นทัวร์แนะนำอีกครั้ง |
| `izhuangzi://feedback` | อีเมลข้อเสนอแนะ |
| `izhuangzi://in-app-review` | รีวิวในแอป / App Store |

## ตัวอย่าง


```
izhuangzi://daily
izhuangzi://passage?id=1
izhuangzi://ask
izhuangzi://allegories
izhuangzi://collection?id=neipian
izhuangzi://study
izhuangzi://hunt
```


## บันทึก

- พารามิเตอร์คือความไวของตัวเลข
- ไซรี, ทางลัด, วิดเจ็ต, และศูนย์ควบคุม ใช้เส้นทางลับเดียวกัน
- ดู In-appings-Cettings softs for the list ล่าสุด


