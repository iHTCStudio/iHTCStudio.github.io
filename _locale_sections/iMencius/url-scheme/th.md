iMencius รองรับ ** `imencius://` BAR * ลิงก์ลัด (URL scheme). การเริ่มหน้าจอหน้าจอเย็นและหน้าจอบ้าน จะถูกส่งไปผ่านระบบบัฟเฟอร์แบบรวม ดังนั้นลิงก์จึงไม่ถูกเปิดสองครั้งหลังจากขึ้นเครื่อง

## รูปแบบลิงก์


```
imencius://{host}?{params}
```


## ผู้เขียน

| URL | เปิด |
|-----|-------|
| `imencius://passage?id={id}` | รายละเอียดข้อความ |
| `imencius://saying?id={id}` / `imencius://couplet?id={id}` / `imencius://poem?id={id}` | เช่นเดียวกันกับเนื้อเรื่อง (ความเข้ากันได้) |
| `imencius://passage?id={id}&card=1` | รายละเอียดและนามบัตร |
| `imencius://card?id={id}` / `imencius://share-card?id={id}` | ○ การ์ด |
| `imencius://author?id={id}` | รายละเอียดผู้แต่ง |
| `imencius://recite` / `imencius://recite?id={id}` | โฟลว์การท่อง |

## การท่องเว็บ

| URL | เปิด |
|-----|-------|
| `imencius://home` | หน้าแรก |
| `imencius://daily` | ทุก วัน |
| `imencius://random` | ข้อความแบบสุ่ม |
| `imencius://favorites` | รายการโปรด |
| `imencius://famous` | บรรทัดขึ้นชื่อ |
| `imencius://search` / `imencius://search?q={query}` | ค้นหา |
| `imencius://study` / `imencius://study?id={id}` | การ ศึกษา พระ คัมภีร์ |
| `imencius://hunt` | ยีฮันท์ ('คีย์เวิร์ด-ฮันต์' / 'ดอกไม้แมลงวัน') |
| `imencius://handwriting` | สืบค้นเมื่อเขียนด้วยมือ ('เขียนเอง'; OS) |
| `imencius://mastered` | สําเร็จการศึกษาแล้ว ('รุก') |
| `imencius://categories` / `imencius://categories?section=` | เรียกดู |
| `imencius://collection?id=` | ชุดสะสม / หนังสือ |
| `imencius://corpus` | ทุกช่อง (ทั้งหมด) |
| `imencius://last-read` | รายการที่อ่านล่าสุด |
| `imencius://reading-history` | ประวัติการอ่าน |
| `imencius://notes` | บันทึก |
| `imencius://fables` / `imencius://allegories` / `imencius://concepts` | ชั้นวางพิเศษเมื่อมี |

## การตั้งค่าและคู่มือ

| URL | เปิด |
|-----|-------|
| `imencius://settings` | การตั้งค่า |
| `imencius://usage-guide` | คู่มือการใช้งาน |
| `imencius://widget-guide` | คู่มือวิดเจ็ต |
| `imencius://shortcuts-guide` | คู่มือทางลัด |
| `imencius://feature-guide` | เล่นทัวร์แนะนำอีกครั้ง |
| `imencius://feedback` | อีเมลข้อเสนอแนะ |
| `imencius://in-app-review` | รีวิวในแอป / App Store |

## ตัวอย่าง


```
imencius://daily
imencius://passage?id=1
imencius://study
imencius://hunt
```



