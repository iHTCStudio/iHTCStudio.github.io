ILvShi รองรับ~ `ilvshi://` BAR * ลิงก์ลัด (URL scheme) การเริ่มหน้าจอหน้าจอเย็นและหน้าจอบ้าน จะถูกส่งไปผ่านระบบบัฟเฟอร์แบบรวม ดังนั้นลิงก์จึงไม่ถูกเปิดสองครั้งหลังจากขึ้นเครื่อง

## รูปแบบลิงก์


```
ilvshi://{host}?{params}
```


## ผู้เขียน

| URL | เปิด |
|-----|-------|
| `ilvshi://passage?id={id}` | รายละเอียดข้อความ |
| `ilvshi://saying?id={id}` / `ilvshi://couplet?id={id}` / `ilvshi://poem?id={id}` | เช่นเดียวกันกับเนื้อเรื่อง (ความเข้ากันได้) |
| `ilvshi://passage?id={id}&card=1` | รายละเอียดและนามบัตร |
| `ilvshi://card?id={id}` / `ilvshi://share-card?id={id}` | ○ การ์ด |
| `ilvshi://author?id={id}` | รายละเอียดผู้แต่ง |
| `ilvshi://recite` / `ilvshi://recite?id={id}` | โฟลว์การท่อง |

## การท่องเว็บ

| URL | เปิด |
|-----|-------|
| `ilvshi://home` | หน้าแรก |
| `ilvshi://daily` | แบบพาเนลทุกวัน |
| `ilvshi://random` | ข้อความแบบสุ่ม |
| `ilvshi://favorites` | รายการโปรด |
| `ilvshi://famous` | บรรทัดขึ้นชื่อ |
| `ilvshi://search` / `ilvshi://search?q={query}` | ค้นหา |
| `ilvshi://study` / `ilvshi://study?id={id}` | ฤดูใบไม้ผลิ- Autumn การศึกษา |
| `ilvshi://hunt` | Outlook Hunt ('คีย์เวิร์ด-ฮันต์' / 'ดอกไม้แมลงวัน') |
| `ilvshi://handwriting` | สืบค้นเมื่อเขียนด้วยมือ ('เขียนเอง'; OS) |
| `ilvshi://mastered` | สําเร็จการศึกษาแล้ว ('รุก') |
| `ilvshi://categories` / `ilvshi://categories?section=` | เรียกดู |
| `ilvshi://collection?id=` | ชุดสะสม / หนังสือ |
| `ilvshi://corpus` | ทุกช่อง (ทั้งหมด) |
| `ilvshi://last-read` | รายการที่อ่านล่าสุด |
| `ilvshi://reading-history` | ประวัติการอ่าน |
| `ilvshi://notes` | บันทึก |
| `ilvshi://fables` / `ilvshi://allegories` / `ilvshi://concepts` | ชั้นวางพิเศษเมื่อมี |

## การตั้งค่าและคู่มือ

| URL | เปิด |
|-----|-------|
| `ilvshi://settings` | การตั้งค่า |
| `ilvshi://usage-guide` | คู่มือการใช้งาน |
| `ilvshi://widget-guide` | คู่มือวิดเจ็ต |
| `ilvshi://shortcuts-guide` | คู่มือทางลัด |
| `ilvshi://feature-guide` | เล่นทัวร์แนะนำอีกครั้ง |
| `ilvshi://feedback` | อีเมลข้อเสนอแนะ |
| `ilvshi://in-app-review` | รีวิวในแอป / App Store |

## ตัวอย่าง


```
ilvshi://daily
ilvshi://passage?id=1
ilvshi://study
ilvshi://hunt
```



