# Engineering Guide | راهنمای مهندسی
## HDPE Pipe Diameter Selector | انتخاب‌گر قطر لوله HDPE

## 1. Scope and intended use | دامنه و کاربرد
**EN:** This application performs preliminary velocity-based sizing of PE pressure pipes using documented OD, SDR and nominal wall-thickness records. It is a screening and learning tool, not a complete pipeline design package.

**FA:** این برنامه انتخاب اولیه لوله‌های فشاری پلی‌اتیلن را بر اساس سرعت انجام می‌دهد و از رکوردهای مستند OD، SDR و ضخامت اسمی استفاده می‌کند. ابزار غربالگری و آموزشی است، نه نرم‌افزار کامل طراحی خط لوله.

## 2. Required inputs | ورودی‌های لازم
- Flow rate in m³/h | دبی بر حسب مترمکعب بر ساعت
- Target average velocity in m/s | سرعت متوسط هدف بر حسب متر بر ثانیه
- PE grade (PE80/PE100) | گرید ماده
- SDR available for that grade | SDR موجود برای گرید انتخابی
- Optional EC and operating temperature for fluid screening | EC و دمای آب برای تخمین خواص سیال

The current command-line interface asks for EC and temperature as part of the optional estimate. These values do not alter the velocity-only diameter selection for a specified flow rate and bore.

در نسخه فعلی CLI، EC و دما برای تخمین خواص پرسیده می‌شوند؛ اما برای دبی و قطر داخلی مشخص، در انتخاب قطر مبتنی بر سرعت نقشی ندارند.

## 3. Geometry and equations | هندسه و روابط
`ID = OD - 2e`; `A = π ID²/4`; `V = (Q/3600)/A`.

OD and e must use the same length unit. Convert millimetres to metres before calculating area. The database supplies nominal wall thickness; the program does not infer actual measured bore.

قطر خارجی و ضخامت باید هم‌واحد باشند. پیش از محاسبه سطح مقطع، میلی‌متر به متر تبدیل می‌شود. ضخامت از بانک خوانده می‌شود و قطر داخلی واقعی اندازه‌گیری نمی‌شود.

## 4. Selection logic | منطق انتخاب
**EN:** Candidate records are filtered by grade and SDR, sorted by OD, and evaluated. The first (smallest) candidate with velocity ≤ target is selected. If none complies, the largest candidate is returned with a warning.

**FA:** رکوردها بر اساس گرید و SDR فیلتر و بر اساس OD مرتب می‌شوند. کوچک‌ترین گزینه‌ای که سرعت آن از هدف بیشتر نباشد انتخاب می‌شود. اگر هیچ گزینه‌ای منطبق نباشد، بزرگ‌ترین سایز همراه هشدار گزارش می‌شود.

## 5. Worked example | مثال مرحله‌به‌مرحله
Given Q=50 m³/h and Vtarget=1.50 m/s:
- Q = 50/3600 = 0.013889 m³/s
- Required area = 0.013889/1.50 = 0.009259 m²
- Required ID = √(4×0.009259/π) ≈ 0.1086 m = 108.6 mm

برای PE100 SDR11، فرض کنید رکورد OD125 دارای ضخامت اسمی حدود 11.4 mm باشد: ID≈102.2 mm و V≈1.69 m/s، پس مردود است. رکورد OD140 با ضخامت حدود 12.7 mm: ID≈114.6 mm و V≈1.35 m/s، پس قابل قبول است. انتخاب نهایی باید از رکورد واقعی موجود در فایل بانک گرفته شود.

## 6. Understanding the output | تفسیر خروجی
- Grade and SDR identify the selected material/dimensional series | گرید و SDR مشخصات ماده و سری ابعادی را نشان می‌دهند.
- OD and wall thickness are nominal catalogue values | OD و ضخامت، مقادیر اسمی کاتالوگ‌اند.
- ID is calculated nominal bore | ID قطر داخلی اسمی محاسبه‌شده است.
- Calculated velocity is the average bulk velocity | سرعت، سرعت متوسط جریان است.
- PN is a reference pressure class, not a complete pressure-design approval | PN کلاس فشاری مرجع است، نه تأیید نهایی طراحی فشار.

## 7. Data quality and engineering cautions | کیفیت داده و ملاحظات
The generic dataset contains 506 records. Some wall thicknesses are ratio-derived or rounded estimates. Check records marked for review against ISO 4427-2 and the controlled manufacturer catalogue. Manufacturer-specific GF catalogue records are separate from generic reference records; do not mix their tolerances or fitting data without checking the source.

بانک عمومی شامل ۵۰۶ رکورد است. بعضی ضخامت‌ها از نسبت SDR استخراج یا گرد شده‌اند. رکوردهای نیازمند بررسی باید با ISO 4427-2 و کاتالوگ کنترل‌شده سازنده تطبیق داده شوند. داده‌های اختصاصی GF از داده‌های عمومی جدا هستند؛ تلرانس‌ها و اتصالات این دو منبع را بدون بررسی منبع با هم ترکیب نکنید.

## 8. Worked example interpretation | جمع‌بندی مثال
The 108.6 mm value is the theoretical minimum bore for the selected flow and target velocity. The selected catalogue bore must be at least this large. A larger bore lowers velocity but may affect cost, availability, fittings and hydraulic operating conditions. The final selection should also be checked for pressure class, temperature, surge, installation and economic constraints.

قطر ۱۰۸٫۶ میلی‌متر حداقل قطر داخلی نظری برای دبی و سرعت هدف است. قطر داخلی اسمی گزینه انتخابی باید حداقل به این مقدار برسد. قطر بزرگ‌تر سرعت را کم می‌کند، اما هزینه، دسترسی، اتصالات و شرایط هیدرولیکی را نیز تغییر می‌دهد. کلاس فشار، دما، ضربه قوچ، نصب و اقتصاد پروژه باید جداگانه بررسی شوند.

## 9. Tests | آزمون‌ها
Run from the repository root:
```bash
python -m unittest discover -s tests -v
```
Tests validate implemented software logic; they do not certify a manufacturer's product or replace engineering review.
