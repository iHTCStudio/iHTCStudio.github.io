iPresids รองรับ ** c0 BAR * ลิงก์ลัด (RUL scheme) การเริ่มหน้าจอหน้าจอเย็นและหน้าจอบ้าน จะถูกส่งไปผ่านระบบบัฟเฟอร์แบบรวม ดังนั้นลิงก์จึงไม่ถูกเปิดสองครั้งหลังจากขึ้นเครื่อง

## รูปแบบลิงก์


```
iprecepts://{host}?{params}
```


## ผู้เขียน

| URL | เปิด |
|-----|-------|
| `iprecepts://passage?id={id}` | รายละเอียดข้อความ |
| `iprecepts://saying?id={id}` / `iprecepts://couplet?id={id}` / `iprecepts://poem?id={id}` | เช่นเดียวกันกับเนื้อเรื่อง (ความเข้ากันได้) |
| `iprecepts://passage?id={id}&card=1` | รายละเอียดและนามบัตร |
| `iprecepts://card?id={id}` / `iprecepts://share-card?id={id}` | ไพ่สําเร็จรูป |
| `iprecepts://author?id={id}` | รายละเอียดผู้แต่ง |
| `iprecepts://recite` / `iprecepts://recite?id={id}` | โฟลว์การท่อง |

## การท่องเว็บ

| URL | เปิด |
|-----|-------|
| `iprecepts://home` | หน้าแรก |
| `iprecepts://daily` | ทุก ๆ วัน |
| `iprecepts://random` | ข้อความแบบสุ่ม |
| `iprecepts://favorites` | รายการโปรด |
| `iprecepts://famous` | บรรทัดขึ้นชื่อ |
| `iprecepts://search` / `iprecepts://search?q={query}` | ค้นหา |
| `iprecepts://study` / `iprecepts://study?id={id}` | การ ศึกษา ประจํา ครอบครัว |
| `iprecepts://hunt` | Precept Hunt ('คีย์เวิร์ด-ฮันต์' / 'ดอกไม้แมลงวัน') |
| `iprecepts://handwriting` | สืบค้นเมื่อเขียนด้วยมือ ('เขียนเอง'; OS) |
| `iprecepts://mastered` | สําเร็จการศึกษาแล้ว ('รุก') |
| `iprecepts://categories` / `iprecepts://categories?section=` | เรียกดู |
| `iprecepts://collection?id=` | คอลเลคชั่น / หนังสือ (ซูซี่ / ซูบัยลู / หยวนชี / ชุจ / ซ็องจี / หยวนชี / เจียวชิ / เจียน / ติงซ็อง / งานสั้น) |
| `iprecepts://corpus` | ทุกช่อง (ทั้งหมด) |
| `iprecepts://last-read` | รายการที่อ่านล่าสุด |
| `iprecepts://reading-history` | ประวัติการอ่าน |
| `iprecepts://notes` | บันทึก |
| `iprecepts://compare` | เปรียบเทียบด้านเท่า |
| `iprecepts://theme?id=` | ชุดตกแต่ง |
| `iprecepts://authors` | ผู้เขียน |

## การตั้งค่าและคู่มือ

| URL | เปิด |
|-----|-------|
| `iprecepts://settings` | การตั้งค่า |
| `iprecepts://usage-guide` | คู่มือการใช้งาน |
| `iprecepts://widget-guide` | คู่มือวิดเจ็ต |
| `iprecepts://shortcuts-guide` | คู่มือทางลัด |
| `iprecepts://feature-guide` | เล่นทัวร์แนะนำอีกครั้ง |
| `iprecepts://feedback` | อีเมลข้อเสนอแนะ |
| `iprecepts://in-app-review` | รีวิวในแอป / App Store |

## ตัวอย่าง


```
iprecepts://daily
iprecepts://passage?id=1
iprecepts://passage?id=1&card=1
iprecepts://compare
iprecepts://collection?id=yanshi
iprecepts://study
iprecepts://hunt
```


## บันทึก

- พารามิเตอร์คือความไวของตัวเลข
- ไซรี, ทางลัด, วิดเจ็ต, และศูนย์ควบคุม ใช้เส้นทางลับเดียวกัน
- ดู In-appings-Cettings softs for the list ล่าสุด


