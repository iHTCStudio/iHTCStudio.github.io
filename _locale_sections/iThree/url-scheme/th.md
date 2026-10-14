IRC รองรับ... `ithree://` BAR ลิงก์ลัด (URL scheme) การเริ่มหน้าจอหน้าจอเย็นและหน้าจอบ้าน จะถูกส่งไปผ่านระบบบัฟเฟอร์แบบรวม ดังนั้นลิงก์จึงไม่ถูกเปิดสองครั้งหลังจากขึ้นเครื่อง

## รูปแบบลิงก์


```
ithree://{host}?{params}
```


## การติดตามและการค้นพบ

| URL | เปิด |
|-----|-------|
| `ithree://home` | หน้าแรก |
| `ithree://daily` | ข้อ คัมภีร์ ประจํา วัน |
| `ithree://random` | ข้อความแบบสุ่ม |
| `ithree://passage?id={id}` | รายละเอียดข้อความ |
| `ithree://recite` / `ithree://recite?id={id}` | โฟลว์การท่อง |
| `ithree://favorites` | รายการโปรด |
| `ithree://famous` | บรรทัดขึ้นชื่อ |
| `ithree://search` / `ithree://search?q={query}` | ค้นหา |
| `ithree://study` | ห้องเรียนเรียน |
| `ithree://quiz` | คํา ถาม ใน ปัจจุบัน |
| `ithree://hunt` | ล่า (寻句) |
| `ithree://mastered` | สําเร็จการศึกษาแล้ว |
| `ithree://categories` | เรียกดู |
| `ithree://chapter?id={id}` | บท |
| `ithree://stories` / `ithree://story?id={id}` | เรื่องเล่า / รายละเอียด |
| `ithree://books` / `ithree://book?id={id}` | ดัชนีคลาสสิค / หนังสือ |
| `ithree://dynasties` / `ithree://dynasty?id={id}` | ความ สําคัญ ของ ราชวงศ์ / ราชวงศ์ |
| `ithree://collection?id=` / `?name=` | ชุดสะสม (หรือหนังสือว่าง) |
| `ithree://last-read` | รายการที่อ่านล่าสุด |
| `ithree://reading-history` | ประวัติการอ่าน |
| `ithree://notes` | บันทึก |

> ควรทราบ: `ithree://` BAR เป็นนามแฝงที่เข้ากันได้และเปิดให้ตรงกัน~

## การตั้งค่าและคู่มือ

| URL | เปิด |
|-----|-------|
| `ithree://settings` | การตั้งค่า |
| `ithree://usage-guide` | คู่มือการใช้งาน |
| `ithree://widget-guide` | คู่มือวิดเจ็ต |
| `ithree://shortcuts-guide` | คู่มือทางลัด |
| `ithree://feature-guide` | เล่นทัวร์แนะนำอีกครั้ง |
| `ithree://feedback` | อีเมลข้อเสนอแนะ |
| `ithree://in-app-review` | รีวิวในแอป / App Store |
| `ithree://privacy` | ความเป็นส่วนตัว |

## ตัวอย่าง


```
ithree://daily
ithree://passage?id=1
ithree://recite?id=1
ithree://study
ithree://hunt
ithree://quiz
ithree://stories
ithree://search?q=人之初
```


ใช้เหล่านี้ในโปรแกรมปุ่มพิมพ์ลัด, การกระทําของหน้าจอส่วนตัวอย่างรวดเร็ว, วิดเจ็ต, ศูนย์ควบคุม, หรือซาฟารี ดูใน-apps ด้วย


