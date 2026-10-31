iRhyme รองรับ~ `irhyme://` BAR * ลิงก์ลัด (URL scheme) การเริ่มหน้าจอหน้าจอเย็นและหน้าจอบ้าน จะถูกส่งไปผ่านระบบบัฟเฟอร์แบบรวม ดังนั้นลิงก์จึงไม่ถูกเปิดสองครั้งหลังจากขึ้นเครื่อง

## รูปแบบลิงก์


```
irhyme://{host}?{params}
```


## ผู้เขียน

| URL | เปิด |
|-----|-------|
| `irhyme://passage?id={id}` | รายละเอียดข้อความ |
| `irhyme://saying?id={id}` / `irhyme://couplet?id={id}` / `irhyme://poem?id={id}` | เช่นเดียวกันกับเนื้อเรื่อง (ความเข้ากันได้) |
| `irhyme://passage?id={id}&card=1` | รายละเอียดและนามบัตร |
| `irhyme://card?id={id}` / `irhyme://share-card?id={id}` | ไพ่ Ryme |
| `irhyme://author?id={id}` | รายละเอียดผู้แต่ง |
| `irhyme://recite` / `irhyme://recite?id={id}` | โฟลว์การท่อง |

## การท่องเว็บ

| URL | เปิด |
|-----|-------|
| `irhyme://home` | หน้าแรก |
| `irhyme://daily` | ไรม์ ใน ปัจจุบัน |
| `irhyme://random` | ข้อความแบบสุ่ม |
| `irhyme://favorites` | รายการโปรด |
| `irhyme://famous` | บรรทัดขึ้นชื่อ |
| `irhyme://search` / `irhyme://search?q={query}` | ค้นหา |
| `irhyme://study` / `irhyme://study?id={id}` | โรงเรียน Rayme |
| `irhyme://hunt` | Rayme Hunt ('คีย์เวิร์ด-ฮันต์' / 'ดอกไม้แมลงวัน') |
| `irhyme://handwriting` | สืบค้นเมื่อเขียนด้วยมือ ('เขียนเอง'; OS) |
| `irhyme://mastered` | สําเร็จการศึกษาแล้ว ('รุก') |
| `irhyme://categories` / `irhyme://categories?section=` | เรียกดู |
| `irhyme://collection?id=` | คอลเลกชัน / หนังสือ (อังกฤษ) |
| `irhyme://corpus` | ทุกช่อง (ทั้งหมด) |
| `irhyme://last-read` | รายการที่อ่านล่าสุด |
| `irhyme://reading-history` | ประวัติการอ่าน |
| `irhyme://notes` | บันทึก |
| `irhyme://pair` | ฝึกความเหลื่อมล้ํา |
| `irhyme://prosody` | โต๊ะพรอโซดี้ |
| `irhyme://rhyme?id=dong` | คลาสกลอนหนึ่ง |
| `irhyme://compare?rhyme=dong` | เปรียบเทียบขนาดเท่าเดิม |
| `irhyme://glossary?id=` | อภิธานศัพท์ |

## การตั้งค่าและคู่มือ

| URL | เปิด |
|-----|-------|
| `irhyme://settings` | การตั้งค่า |
| `irhyme://usage-guide` | คู่มือการใช้งาน |
| `irhyme://widget-guide` | คู่มือวิดเจ็ต |
| `irhyme://shortcuts-guide` | คู่มือทางลัด |
| `irhyme://feature-guide` | เล่นทัวร์แนะนำอีกครั้ง |
| `irhyme://feedback` | อีเมลข้อเสนอแนะ |
| `irhyme://in-app-review` | รีวิวในแอป / App Store |

## ตัวอย่าง


```
irhyme://daily
irhyme://passage?id=1001
irhyme://pair
irhyme://compare?rhyme=dong
irhyme://collection?id=shenglv
irhyme://study
irhyme://hunt
```


## บันทึก

- พารามิเตอร์คือความไวของตัวเลข
- ไซรี, ทางลัด, วิดเจ็ต, และศูนย์ควบคุม ใช้เส้นทางลับเดียวกัน
- ดู In-appings-Cettings softs for the list ล่าสุด


