iguanZhi รองรับ~ `iguanzhi://` BAR * ลิงก์ลัด (URL scheme) การเริ่มหน้าจอหน้าจอเย็นและหน้าจอบ้าน จะถูกส่งไปผ่านระบบบัฟเฟอร์แบบรวม ดังนั้นลิงก์จึงไม่ถูกเปิดสองครั้งหลังจากขึ้นเครื่อง

## รูปแบบลิงก์


```
iguanzhi://{host}?{params}
```


## ผู้เขียน

| URL | เปิด |
|-----|-------|
| `iguanzhi://passage?id={id}` | รายละเอียดข้อความ |
| `iguanzhi://saying?id={id}` / `iguanzhi://couplet?id={id}` / `iguanzhi://poem?id={id}` | เช่นเดียวกันกับเนื้อเรื่อง (ความเข้ากันได้) |
| `iguanzhi://passage?id={id}&card=1` | รายละเอียดและนามบัตร |
| `iguanzhi://card?id={id}` / `iguanzhi://share-card?id={id}` | ○ การ์ด |
| `iguanzhi://author?id={id}` | รายละเอียดผู้แต่ง |
| `iguanzhi://recite` / `iguanzhi://recite?id={id}` | โฟลว์การท่อง |

## การท่องเว็บ

| URL | เปิด |
|-----|-------|
| `iguanzhi://home` | หน้าแรก |
| `iguanzhi://daily` | คํา กล่าว ใน ปัจจุบัน |
| `iguanzhi://random` | ข้อความแบบสุ่ม |
| `iguanzhi://favorites` | รายการโปรด |
| `iguanzhi://famous` | บรรทัดขึ้นชื่อ |
| `iguanzhi://search` / `iguanzhi://search?q={query}` | ค้นหา |
| `iguanzhi://study` / `iguanzhi://study?id={id}` | การ ศึกษา แบบ คลาสสิก |
| `iguanzhi://hunt` | Esay Hunt ('คีย์เวิร์ด-ฮันต์' / 'ดอกไม้แมลงวัน') |
| `iguanzhi://handwriting` | สืบค้นเมื่อเขียนด้วยมือ ('เขียนเอง'; OS) |
| `iguanzhi://mastered` | สําเร็จการศึกษาแล้ว ('รุก') |
| `iguanzhi://categories` / `iguanzhi://categories?section=` | เรียกดู |
| `iguanzhi://collection?id=` | ชุดสะสม / หนังสือ |
| `iguanzhi://corpus` | ทุกช่อง (ทั้งหมด) |
| `iguanzhi://last-read` | รายการที่อ่านล่าสุด |
| `iguanzhi://reading-history` | ประวัติการอ่าน |
| `iguanzhi://notes` | บันทึก |
| `iguanzhi://fables` / `iguanzhi://allegories` / `iguanzhi://concepts` | ชั้นวางพิเศษเมื่อมี |

## การตั้งค่าและคู่มือ

| URL | เปิด |
|-----|-------|
| `iguanzhi://settings` | การตั้งค่า |
| `iguanzhi://usage-guide` | คู่มือการใช้งาน |
| `iguanzhi://widget-guide` | คู่มือวิดเจ็ต |
| `iguanzhi://shortcuts-guide` | คู่มือทางลัด |
| `iguanzhi://feature-guide` | เล่นทัวร์แนะนำอีกครั้ง |
| `iguanzhi://feedback` | อีเมลข้อเสนอแนะ |
| `iguanzhi://in-app-review` | รีวิวในแอป / App Store |

## ตัวอย่าง


```
iguanzhi://daily
iguanzhi://passage?id=1
iguanzhi://study
iguanzhi://hunt
```



