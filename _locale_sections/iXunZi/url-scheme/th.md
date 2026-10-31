IXunZi รองรับ~ `ixunzi://` BAR * ลิงก์ลัด (URL scheme) การเริ่มหน้าจอหน้าจอเย็นและหน้าจอบ้าน จะถูกส่งไปผ่านระบบบัฟเฟอร์แบบรวม ดังนั้นลิงก์จึงไม่ถูกเปิดสองครั้งหลังจากขึ้นเครื่อง

## รูปแบบลิงก์


```
ixunzi://{host}?{params}
```


## ผู้เขียน

| URL | เปิด |
|-----|-------|
| `ixunzi://passage?id={id}` | รายละเอียดข้อความ |
| `ixunzi://saying?id={id}` / `ixunzi://couplet?id={id}` / `ixunzi://poem?id={id}` | เช่นเดียวกันกับเนื้อเรื่อง (ความเข้ากันได้) |
| `ixunzi://passage?id={id}&card=1` | รายละเอียดและนามบัตร |
| `ixunzi://card?id={id}` / `ixunzi://share-card?id={id}` | ○ การ์ด |
| `ixunzi://author?id={id}` | รายละเอียดผู้แต่ง |
| `ixunzi://recite` / `ixunzi://recite?id={id}` | โฟลว์การท่อง |

## การท่องเว็บ

| URL | เปิด |
|-----|-------|
| `ixunzi://home` | หน้าแรก |
| `ixunzi://daily` | Name=หน้าต่างComment |
| `ixunzi://random` | ข้อความแบบสุ่ม |
| `ixunzi://favorites` | รายการโปรด |
| `ixunzi://famous` | บรรทัดขึ้นชื่อ |
| `ixunzi://search` / `ixunzi://search?q={query}` | ค้นหา |
| `ixunzi://study` / `ixunzi://study?id={id}` | โรงเรียนเพื่อส่งเสริมการเรียนรู้ |
| `ixunzi://hunt` | Sun Hunt ('คีย์เวิร์ด-ฮันต์' / 'ดอกไม้แมลงวัน') |
| `ixunzi://handwriting` | สืบค้นเมื่อเขียนด้วยมือ ('เขียนเอง'; OS) |
| `ixunzi://mastered` | สําเร็จการศึกษาแล้ว ('รุก') |
| `ixunzi://categories` / `ixunzi://categories?section=` | เรียกดู |
| `ixunzi://collection?id=` | ชุดสะสม / หนังสือ |
| `ixunzi://corpus` | ทุกช่อง (ทั้งหมด) |
| `ixunzi://last-read` | รายการที่อ่านล่าสุด |
| `ixunzi://reading-history` | ประวัติการอ่าน |
| `ixunzi://notes` | บันทึก |
| `ixunzi://ask` | ถาม Xunzi |
| `ixunzi://fables` / `ixunzi://allegories` / `ixunzi://concepts` | ชั้นวางพิเศษเมื่อมี |

## การตั้งค่าและคู่มือ

| URL | เปิด |
|-----|-------|
| `ixunzi://settings` | การตั้งค่า |
| `ixunzi://usage-guide` | คู่มือการใช้งาน |
| `ixunzi://widget-guide` | คู่มือวิดเจ็ต |
| `ixunzi://shortcuts-guide` | คู่มือทางลัด |
| `ixunzi://feature-guide` | เล่นทัวร์แนะนำอีกครั้ง |
| `ixunzi://feedback` | อีเมลข้อเสนอแนะ |
| `ixunzi://in-app-review` | รีวิวในแอป / App Store |

## ตัวอย่าง


```
ixunzi://daily
ixunzi://passage?id=1
ixunzi://ask
ixunzi://study
ixunzi://hunt
```



