idevolloper รองรับ~ c0 BAR * ลิงก์ลัด (URL scheme) การเริ่มหน้าจอหน้าจอเย็นและหน้าจอบ้าน จะถูกส่งไปผ่านระบบบัฟเฟอร์แบบรวม ดังนั้นลิงก์จึงไม่ถูกเปิดสองครั้งหลังจากขึ้นเครื่อง

## รูปแบบลิงก์


```
ideveloper://{host}?{params}
```


## เครื่องมือเรียกดู

| URL | เปิด |
|-----|-------|
| `ideveloper://home` | หน้าแรก |
| `ideveloper://tool?id={id}` | รายละเอียดเครื่องมือ (e.g. `jon', 'เบส64', 'เวลา') |
| `ideveloper://category?id={id}` | หมวดหมู่ (e.g. สืบค้นเมื่อ) |
| `ideveloper://search` / `ideveloper://search?q={query}` | ค้นหา |
| `ideveloper://favorites` | รายการโปรด |
| `ideveloper://history` | ประวัติการปฏิบัติการ |
| `ideveloper://reference` / `ideveloper://reference?id={id}` | ศูนย์อ้างอิง / รายการ |
| `ideveloper://new-snippet` | ชิ้นส่วนตัวใหม่ |
| `ideveloper://focus` | โฟกัสตัวจับเวลา / ถ่ายทอดสด |
| `ideveloper://share?tool={id}` | เปิดการใช้งานร่วมกันเป็นเครื่องมือ (ทํางานกับนามสกุลใช้งานร่วมกัน + App Group) |

## การตั้งค่าและคู่มือ

| URL | เปิด |
|-----|-------|
| `ideveloper://settings` | การตั้งค่า |
| `ideveloper://usage-guide` | คู่มือการใช้งาน |
| `ideveloper://widget-guide` | คู่มือวิดเจ็ต |
| `ideveloper://shortcuts-guide` | คู่มือทางลัด |
| `ideveloper://feature-guide` | เล่นทัวร์แนะนำอีกครั้ง |
| `ideveloper://feedback` | อีเมลข้อเสนอแนะ |
| `ideveloper://in-app-review` | รีวิวในแอป / App Store |

## ตัวอย่าง


```
ideveloper://tool?id=json
ideveloper://search?q=base64
ideveloper://reference?id=http-200
ideveloper://favorites
ideveloper://focus
ideveloper://share?tool=json
ideveloper://category?id=encoding
```


ใช้เหล่านี้ในโปรแกรมปุ่มพิมพ์ลัด, การกระทําของหน้าจอส่วนตัวอย่างรวดเร็ว, วิดเจ็ต, ศูนย์ควบคุม, หรือซาฟารี ดูใน-apps ด้วย


