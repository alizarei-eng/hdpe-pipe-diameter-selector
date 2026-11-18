# راهنمای استفاده از انتخاب‌گر قطر لوله HDPE

## معرفی

این برنامه یک ابزار خط فرمان پایتون برای انتخاب اولیه قطر لوله HDPE بر اساس دبی و سرعت هدف است. کاربر دبی و سرعت مجاز را وارد می‌کند؛ سپس گرید و SDR را از فهرست‌های شماره‌گذاری‌شده انتخاب می‌کند. برنامه کوچک‌ترین قطر خارجی موجود در بانک اطلاعاتی را پیشنهاد می‌دهد که سرعت محاسبه‌شده آن از سرعت هدف بیشتر نباشد.

## پیش‌نیاز و اجرا

- Python نسخه 3.10 یا جدیدتر
- بدون نیاز به نصب کتابخانه جانبی

در PowerShell و در مسیر پوشه پروژه اجرا کنید:

```powershell
python main.py
```

برای دریافت آخرین نسخه از GitHub:

```powershell
git pull origin main
python main.py
```

## مراحل کار با برنامه

### مرحله ۱ ـ ورود دبی

دبی را بر حسب مترمکعب بر ساعت وارد کنید:

`Flow rate (m3/h): 50`

### مرحله ۲ ـ ورود سرعت هدف

سرعت هدف را بر حسب متر بر ثانیه وارد کنید:

`Target velocity (m/s): 1.5`

### مرحله ۳ ـ انتخاب گرید

برنامه گریدهای موجود در بانک اطلاعاتی را شماره‌گذاری می‌کند. برای مثال:

```text
Available PE material grades:
  1) PE100
  2) PE80
Enter the number:
```

ترتیب گزینه‌ها از داده‌های موجود در فایل JSON خوانده می‌شود؛ بنابراین اگر در آینده گرید معتبر دیگری به بانک اضافه شود، در فهرست نیز ظاهر خواهد شد.

### مرحله ۴ ـ انتخاب SDR

پس از انتخاب گرید، فقط SDRهای ثبت‌شده برای همان گرید نمایش داده می‌شوند. برای نمونه، فهرست PE100:

```text
Available SDR values for PE100:
  1) SDR 7.4
  2) SDR 9
  3) SDR 11
  4) SDR 13.6
  5) SDR 17
  6) SDR 21
  7) SDR 26
  8) SDR 33
  9) SDR 41
Enter the number:
```

فهرست PE80 شامل SDRهای 6، 7.4، 9، 11، 13.6، 17، 21، 26، 33 و 41 است. SDR6 برای PE100 در این بانک تعریف نشده است؛ بنابراین به کاربر پیشنهاد نمی‌شود.

اگر عدد خارج از محدوده وارد شود، برنامه دوباره درخواست انتخاب می‌کند.

### مرحله ۵ ـ مشاهده نتیجه

خروجی شامل موارد زیر است:

- گرید ماده
- قطر خارجی اسمی (OD)
- مقدار SDR
- ضخامت اسمی دیواره
- قطر داخلی اسمی محاسبه‌شده
- فشار نامی مرجع (PN)
- سرعت محاسبه‌شده
- سرعت هدف
- جدول قطرهای جایگزین و وضعیت انطباق سرعت هرکدام

برنامه کوچک‌ترین OD موجود را که سرعت آن از سرعت هدف بیشتر نباشد انتخاب می‌کند. اگر هیچ سایزی این شرط را برآورده نکند، بزرگ‌ترین سایز موجود را نشان می‌دهد و هشدار می‌دهد که سرعت هدف تأمین نشده است.

## محدوده بانک اطلاعاتی

| مشخصه | محدوده |
|---|---|
| گریدها | PE80 و PE100 |
| قطر خارجی اسمی | 16 تا 3000 میلی‌متر |
| تعداد رکوردها | 506 |
| SDRهای PE80 | 6، 7.4، 9، 11، 13.6، 17، 21، 26، 33، 41 |
| SDRهای PE100 | 7.4، 9، 11، 13.6، 17، 21، 26، 33، 41 |

## روابط محاسباتی

تبدیل دبی:

`Q (m³/s) = Q (m³/h) / 3600`

قطر داخلی اسمی:

`ID = OD - 2e`

سطح مقطع داخلی:

`A = π × (ID / 1000)² / 4`

سرعت متوسط:

`V = Q / A`

در این روابط، OD قطر خارجی اسمی و e ضخامت اسمی دیواره است. قطر داخلی واقعی ممکن است به دلیل تلرانس‌های ساخت با مقدار محاسباتی تفاوت داشته باشد.

## اجرای تست‌ها

از مسیر اصلی پروژه اجرا کنید:

```powershell
python -m unittest discover -s tests -v
```

## محدودیت‌های مهندسی و کنترل داده‌ها

**این برنامه ابزار انتخاب اولیه بر اساس سرعت است و جایگزین طراحی کامل هیدرولیکی یا دیتاشیت سازنده نیست.**

- بانک 506 رکوردی یک مجموعه داده مرجع توسعه‌ای است، نه کاتالوگ تأییدشده یک تولیدکننده.
- سری قطر خارجی و نگاشت گرید/SDR بر اساس مرجع ISO 4427-2 تنظیم شده‌اند.
- به‌جز ضخامت‌های SDR11 حفظ‌شده برای ODهای 32 تا 630 میلی‌متر و اصلاح ضخامت SDR11 با OD20 به مقدار 2.0 میلی‌متر، بیشتر ضخامت‌ها از نسبت OD/SDR، با گردکردن به 0.1 میلی‌متر و اعمال حداقل ضخامت تولید شده‌اند. وضعیت نیازمند بررسی این رکوردها در فایل JSON مشخص شده است.
- ضخامت‌های مشتق‌شده باید پیش از خرید یا صدور نقشه اجرایی با نسخه کنترل‌شده استاندارد و دیتاشیت سازنده تطبیق داده شوند.
- PN نمایش‌داده‌شده مقدار مرجع است. اثر دما، ضریب طراحی، شرایط سرویس و الزامات پروژه باید جداگانه بررسی شوند.
- برنامه در نسخه فعلی افت فشار، منحنی پمپ، ضربه قوچ، سازگاری شیمیایی، شرایط نصب، بارهای سازه‌ای یا موجودی واقعی سازنده را کنترل نمی‌کند.

بنابراین خروجی را برای غربالگری اولیه گزینه‌ها استفاده کنید؛ تأیید نهایی قطر و کلاس فشاری باید با محاسبات هیدرولیکی و مدارک فنی پروژه انجام شود.


---

# English User Guide | راهنمای انگلیسی

## Purpose
This command-line application performs preliminary HDPE pipe sizing based on a user-specified flow rate and target average velocity. It filters the pipe database by PE grade and SDR, calculates nominal internal diameter from outside diameter and nominal wall thickness, and selects the smallest available OD that meets the velocity target.

## Run
```bash
python main.py
python -m unittest discover -s tests -v
```

## Input sequence
1. Enter flow rate in m³/h.
2. Enter target average velocity in m/s.
3. Enter EC in mS/cm (already compensated to 25°C) and actual water temperature in °C. These are optional fluid-property screening values in purpose, but the current CLI requests them. They do not affect the velocity-based diameter recommendation.
4. Select PE80 or PE100 from the database menu.
5. Select an SDR available for that grade.
6. Review the recommended pipe and ranked catalogue alternatives.

## Equations
`Q(m³/s)=Q(m³/h)/3600`
`ID(mm)=OD(mm)-2×wall thickness(mm)`
`A=π(ID/1000)²/4`
`V=Q/A`

The smallest available OD whose nominal calculated velocity is no greater than the target is selected. If no available record meets the target, the largest available record is returned with a warning.

## Database scope
The generic reference database currently contains 506 records, with PE80 and PE100 grade/SDR combinations and OD values extending to 3000 mm where records are available. The exact menu is read from the JSON database; not every grade has every SDR or OD.

## Suitable applications
Use the selector for preliminary sizing of one pipe segment at one design flow, comparing catalogue sizes and preparing alternatives for hydraulic verification.

## Limitations
- One flow and one candidate pipe bore are evaluated at a time; the tool does not assemble a multi-diameter route or branched network.
- It checks average velocity only. It does not calculate pressure loss, pump TDH, pump curves, energy, surge/water hammer or transient behaviour.
- It does not certify pressure class at operating temperature or include project-specific design factors, chemical compatibility, external loads, burial, supports, joining or manufacturer stock.
- Nominal ID is based on nominal dimensions. Several generic wall-thickness records are ratio-derived/estimated and must be verified against the controlled standard or the exact manufacturer's catalogue.
- EC-based fluid properties are estimates and do not change the velocity-only sizing result.

Treat the result as a preliminary catalogue shortlist, not an approved construction or procurement specification.
