i Excel รองรับ} `iexcel://` BAR -~ ลิงก์ลัดสําหรับปุ่มพิมพ์ลัด, คั่นหน้า Safari, วิดเจ็ต และอัตโนมัติ

## รูปแบบลิงก์


```
iexcel://{host}?{params}
```


## การเรียนรู้

| URL | เปิด |
|-----|-------|
| `iexcel://playground` | พื้นเล่นสูตร |
| `iexcel://quiz` | ข้อสอบประเภท |
| `iexcel://item?kind=function&id=SUM` | รายละเอียดการทํางาน (เช่น Sum) |
| `iexcel://item?kind=tip&id={id}` | รายละเอียด |
| `iexcel://item?kind=lesson&id={id}` | รายละเอียดบทเรียน |
| `iexcel://item?kind=quiz&id={id}` | รายละเอียด Quiz |
| `iexcel://item?kind=shortcut&id={id}` | รายละเอียดปุ่มพิมพ์ลัด |

### เ พิ่มค่าของรายการ `iexcel://` BAR `iexcel://playground` C2                                                                  .

IDs มักเป็นชื่อตัวใหญ่ (เช่น `iexcel://` , `iexcel://playground` )

## เรียกดูและค้นหา

| URL | เปิด |
|-----|-------|
| `iexcel://home` | หน้าแรก |
| `iexcel://category?id=popular` | หมวดหมู่โดยหมายเลข |
| `iexcel://search` | ค้นหาในแท็บ |
| `iexcel://search?q=SUM` | ค้นหาพร้อมคำค้น |
| `iexcel://favorites` | แท็บโปรด |
| `iexcel://settings` | การตั้งค่า |

### หมายเลขหมวดหมู่ทั่วไป `iexcel://item?kind=function&id=SUM` ## ทิศทางการทํางาน

| URL | เปิด |
|-----|-------|
| `iexcel://feature-guide` | คุณสมบัติบน (เล่น) |
| `iexcel://widget-guide` | คู่มือวิดเจ็ต |
| `iexcel://shortcuts-guide` | คู่มือทางลัด |
| `iexcel://usage-guide` | คู่มือการใช้งาน |
| `iexcel://feedback` | อีเมลข้อเสนอแนะ |
| `iexcel://in-app-review` | ให้คะแนน App Store ในแอป |

## ปุ่มพิมพ์ลัดของ Siri & App

วลีที่ประกอบขึ้นเอง (อังกฤษ / 简体 / 繁體) พ.ศ.

| Action | วลีตัวอย่าง |
|--------|-----------------|
| Open Home | "เปิด IExchel" / "IExchel" / "IExchel" |
| Playground | “ เปิดสนามเด็กเล่นในไอเอ็กซ์เซล" / "IExchel 打开演练场" |
| Quiz | "เริ่มทดสอบใน iExchel" / "用 IExchel 开始测验" |
| Function | “ เปิดการทํางานใน iExchel" (จากนั้นให้ชื่อฟังก์ชัน) | `iexcel://` BAR มีการใช้งานเป็น App Infinting ในโปรแกรมปุ่มพิมพ์ลัด (ไม่มีรายการเป็นวลีปุ่มพิมพ์ลัดที่ใช้พูด)

## การกระทําด่วนของจอส่วนตัว

กดเมาส์แบบยาว:

| Action | ปลายทาง |
|--------|-------------|
| Home | แท็บหน้าแรก |
| Playground | พื้นเล่นสูตร |
| Quiz | ประเภท Quizes |
| Search | ค้นหา |


