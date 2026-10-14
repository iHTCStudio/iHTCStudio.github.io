iMozi รองรับ} BAR `imozi://` BAR BAR ลิงก์ลัด (RUL scheme) การเริ่มหน้าจอหน้าจอเย็นและหน้าจอบ้าน จะถูกส่งไปผ่านระบบบัฟเฟอร์แบบรวม ดังนั้นลิงก์จึงไม่ถูกเปิดสองครั้งหลังจากขึ้นเครื่อง

## รูปแบบลิงก์


```
imozi://{host}?{params}
```


## ผู้เขียน

| URL | เปิด |
|-----|-------|
| `imozi://passage?id={id}` | รายละเอียดข้อความ |
| `imozi://saying?id={id}` / `imozi://couplet?id={id}` / `imozi://poem?id={id}` | เช่นเดียวกันกับเนื้อเรื่อง (ความเข้ากันได้) |
| `imozi://passage?id={id}&card=1` | รายละเอียดและนามบัตร |
| `imozi://card?id={id}` / `imozi://share-card?id={id}` | ○ การ์ด |
| `imozi://author?id={id}` | รายละเอียดผู้แต่ง |
| `imozi://recite` / `imozi://recite?id={id}` | โฟลว์การท่อง |

## การท่องเว็บ

| URL | เปิด |
|-----|-------|
| `imozi://home` | หน้าแรก |
| `imozi://daily` | โม ใน ปัจจุบัน |
| `imozi://random` | ข้อความแบบสุ่ม |
| `imozi://favorites` | รายการโปรด |
| `imozi://famous` | บรรทัดขึ้นชื่อ |
| `imozi://search` / `imozi://search?q={query}` | ค้นหา |
| `imozi://study` / `imozi://study?id={id}` | การ ศึกษา วิจัย ของ โม ฮิม |
| `imozi://hunt` | หมายเหตุล่า ('คีย์เวิร์ด-ฮันต์' / 'ดอกไม้แมลงวัน') |
| `imozi://handwriting` | สืบค้นเมื่อเขียนด้วยมือ ('เขียนเอง'; OS) |
| `imozi://mastered` | สําเร็จการศึกษาแล้ว ('รุก') |
| `imozi://categories` / `imozi://categories?section=` | เรียกดู |
| `imozi://collection?id=` | ชุดสะสม / หนังสือ |
| `imozi://corpus` | ทุกช่อง (ทั้งหมด) |
| `imozi://last-read` | รายการที่อ่านล่าสุด |
| `imozi://reading-history` | ประวัติการอ่าน |
| `imozi://notes` | บันทึก |
| `imozi://ask` | ถามมอสซี่ดูสิ |
| `imozi://fables` / `imozi://allegories` / `imozi://concepts` | ชั้นวางพิเศษเมื่อมี |

## การตั้งค่าและคู่มือ

| URL | เปิด |
|-----|-------|
| `imozi://settings` | การตั้งค่า |
| `imozi://usage-guide` | คู่มือการใช้งาน |
| `imozi://widget-guide` | คู่มือวิดเจ็ต |
| `imozi://shortcuts-guide` | คู่มือทางลัด |
| `imozi://feature-guide` | เล่นทัวร์แนะนำอีกครั้ง |
| `imozi://feedback` | อีเมลข้อเสนอแนะ |
| `imozi://in-app-review` | รีวิวในแอป / App Store |

## ตัวอย่าง


```
imozi://daily
imozi://passage?id=1
imozi://ask
imozi://study
imozi://hunt
```



