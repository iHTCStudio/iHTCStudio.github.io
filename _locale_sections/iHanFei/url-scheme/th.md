iHanfai สนับสนุน~ `ihanfei://` BAR * ลิงก์ลัด (URL scheme). การเริ่มหน้าจอหน้าจอเย็นและหน้าจอบ้าน จะถูกส่งไปผ่านระบบบัฟเฟอร์แบบรวม ดังนั้นลิงก์จึงไม่ถูกเปิดสองครั้งหลังจากขึ้นเครื่อง

## รูปแบบลิงก์


```
ihanfei://{host}?{params}
```


## ผู้เขียน

| URL | เปิด |
|-----|-------|
| `ihanfei://passage?id={id}` | รายละเอียดข้อความ |
| `ihanfei://saying?id={id}` / `ihanfei://couplet?id={id}` / `ihanfei://poem?id={id}` | เช่นเดียวกันกับเนื้อเรื่อง (ความเข้ากันได้) |
| `ihanfei://passage?id={id}&card=1` | รายละเอียดและนามบัตร |
| `ihanfei://card?id={id}` / `ihanfei://share-card?id={id}` | ○ การ์ด |
| `ihanfei://author?id={id}` | รายละเอียดผู้แต่ง |
| `ihanfei://recite` / `ihanfei://recite?id={id}` | โฟลว์การท่อง |

## การท่องเว็บ

| URL | เปิด |
|-----|-------|
| `ihanfei://home` | หน้าแรก |
| `ihanfei://daily` | ตารางเวลาประจําวัน |
| `ihanfei://random` | ข้อความแบบสุ่ม |
| `ihanfei://favorites` | รายการโปรด |
| `ihanfei://famous` | บรรทัดขึ้นชื่อ |
| `ihanfei://search` / `ihanfei://search?q={query}` | ค้นหา |
| `ihanfei://study` / `ihanfei://study?id={id}` | การ ศึกษา ด้าน กฎหมาย |
| `ihanfei://hunt` | Law Hunt ('คีย์เวิร์ด-ฮันต์' / 'ดอกไม้แมลงวัน') |
| `ihanfei://handwriting` | สืบค้นเมื่อเขียนด้วยมือ ('เขียนเอง'; OS) |
| `ihanfei://mastered` | สําเร็จการศึกษาแล้ว ('รุก') |
| `ihanfei://categories` / `ihanfei://categories?section=` | เรียกดู |
| `ihanfei://collection?id=` | ชุดสะสม / หนังสือ |
| `ihanfei://corpus` | ทุกช่อง (ทั้งหมด) |
| `ihanfei://last-read` | รายการที่อ่านล่าสุด |
| `ihanfei://reading-history` | ประวัติการอ่าน |
| `ihanfei://notes` | บันทึก |
| `ihanfei://fables` / `ihanfei://allegories` / `ihanfei://concepts` | ชั้นวางพิเศษเมื่อมี |

## การตั้งค่าและคู่มือ

| URL | เปิด |
|-----|-------|
| `ihanfei://settings` | การตั้งค่า |
| `ihanfei://usage-guide` | คู่มือการใช้งาน |
| `ihanfei://widget-guide` | คู่มือวิดเจ็ต |
| `ihanfei://shortcuts-guide` | คู่มือทางลัด |
| `ihanfei://feature-guide` | เล่นทัวร์แนะนำอีกครั้ง |
| `ihanfei://feedback` | อีเมลข้อเสนอแนะ |
| `ihanfei://in-app-review` | รีวิวในแอป / App Store |

## ตัวอย่าง


```
ihanfei://daily
ihanfei://passage?id=1
ihanfei://study
ihanfei://hunt
```



