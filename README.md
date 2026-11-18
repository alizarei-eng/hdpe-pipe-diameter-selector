# HDPE Pipe Diameter Selector | انتخاب‌گر قطر لوله HDPE

**FA — فارسی:** ابزار انتخاب اولیه قطر اسمی لوله پلی‌اتیلن بر اساس دبی، سرعت هدف، گرید PE و SDR، با استفاده از بانک ابعادی مستند.

**EN — English:** A preliminary HDPE pipe-size selection tool based on flow rate, target velocity, PE grade, SDR, and a documented dimensional database.

## Purpose | هدف
- **FA:** دبی و سرعت هدف را دریافت می‌کند؛ گرید و SDR از فهرست انتخاب می‌شوند؛ سپس کوچک‌ترین OD موجود را انتخاب می‌کند که سرعت محاسبه‌شده آن از سرعت هدف بیشتر نباشد.
- **EN:** The tool accepts flow and target velocity, lets the user select a PE grade and SDR, and selects the smallest available outside diameter whose calculated velocity does not exceed the target.

## Features | قابلیت‌ها
- PE80 and PE100 grade menus | انتخاب گرید PE80 و PE100
- Grade-specific SDR options | نمایش SDRهای موجود برای هر گرید
- OD, nominal wall thickness and calculated nominal ID | قطر خارجی، ضخامت اسمی و محاسبه قطر داخلی
- Recommended catalogue size and ranked alternatives | سایز پیشنهادی و جدول گزینه‌های جایگزین
- Optional EC-based screening estimates for TDS, density and viscosity | تخمین غربالگری TDS، چگالی و ویسکوزیته از EC
- Manufacturer-specific pipe and fitting catalogue datasets | بانک کاتالوگ اختصاصی لوله و اتصالات سازنده

## Installation and run | نصب و اجرا
Python 3.10 or newer is recommended. No third-party package is required for the core selector.

```bash
git clone https://github.com/alizarei-eng/hdpe-pipe-diameter-selector.git
cd hdpe-pipe-diameter-selector
python main.py
python -m unittest discover -s tests -v
```

## Input workflow | ترتیب ورود اطلاعات
1. **Flow rate (m³/h) | دبی:** enter a positive volumetric flow rate.
2. **Target velocity (m/s) | سرعت هدف:** enter the maximum preferred average velocity.
3. **EC (mS/cm) and water temperature (°C) | EC و دمای آب:** optional fluid-property screening inputs in the current CLI; EC must already be compensated to 25°C.
4. **PE grade | گرید:** select PE80 or PE100 from the available menu.
5. **SDR | نسبت ابعادی:** select only an SDR available for the selected grade.
6. **Results | نتایج:** review the recommended pipe and all catalogue alternatives.

## Calculation method | روش محاسبه
`Q_s = Q_h / 3600`

`ID = OD - 2e`

`A = π ID² / 4`

`V = Q_s / A`

Here, OD and wall thickness e are in metres in the area calculation. The selector chooses the smallest catalogue OD satisfying V ≤ Vtarget. If no size meets the target, it reports the largest available size and raises a warning.

در این روابط، قطر و ضخامت در محاسبه سطح مقطع بر حسب متر هستند. برنامه کوچک‌ترین قطر خارجی موجود را انتخاب می‌کند که شرط سرعت را برآورده کند. اگر هیچ سایزی مناسب نباشد، بزرگ‌ترین سایز موجود همراه هشدار نمایش داده می‌شود.

## Worked example | مثال کامل
**Inputs | ورودی‌ها**
- Flow rate = 50 m³/h
- Target velocity = 1.50 m/s
- Grade = PE100
- SDR = 11

Required internal diameter from the target velocity:

`Q = 50/3600 = 0.013889 m³/s`

`A_required = Q/V = 0.009259 m²`

`ID_required = √(4A/π) ≈ 108.6 mm`

For illustration, a PE100 SDR11 catalogue record at OD 125 mm has a nominal wall near 11.4 mm, giving ID ≈ 102.2 mm and velocity ≈ 1.69 m/s: it does not meet the target. An OD 140 mm record with nominal wall near 12.7 mm gives ID ≈ 114.6 mm and velocity ≈ 1.35 m/s: it meets the target. The program selects the smallest compliant available record in its actual database.

**تفسیر فارسی:** قطر داخلی لازم حدود ۱۰۸٫۶ میلی‌متر است. سایز OD125 در این مثال سرعتی بالاتر از هدف می‌دهد؛ OD140 سرعتی حدود ۱٫۳۵ متر بر ثانیه دارد و شرط را برآورده می‌کند. خروجی واقعی دقیقاً تابع رکوردهای موجود در بانک برنامه است.

## Fluid-property estimate | تخمین خواص سیال
EC-based TDS, density and viscosity are screening estimates only. EC alone cannot determine individual ion concentrations. The optional natural-seawater profile assumes standard seawater ionic ratios and must not be applied to groundwater or RO concentrate without laboratory confirmation.

تخمین خواص از EC صرفاً برای غربالگری است. EC به‌تنهایی غلظت یون‌های منفرد را مشخص نمی‌کند. پروفایل آب دریای طبیعی نیز بر اساس نسبت‌های استاندارد فرضی است و بدون آزمایش نباید برای آب زیرزمینی یا کنسانتره RO استفاده شود.

## Data sources and limitations | منابع داده و محدودیت‌ها
- Generic dimensions: `databases/pipe_standards.json`.
- Manufacturer-specific GF PE100 water pipe and fittings: `databases/manufacturer_catalogues/`.
- Hydraulic fitting K references: `databases/hydraulic_fittings.json`.
- Source register: `sources/source_register.json`.

Nominal ID is calculated from nominal OD and wall thickness; actual bore varies with manufacturing tolerances. Some generic wall values are ratio-derived estimates and must be verified against a controlled standard or the selected manufacturer's datasheet. PN is a reference at its stated basis and does not include project-specific temperature derating or design factors. This tool does not calculate pressure loss, pump duty, water hammer, structural loads, chemical compatibility or stock availability.

قطر داخلی محاسباتی اسمی است و تلرانس ساخت را لحاظ نمی‌کند. بخشی از ضخامت‌ها تخمینی/نسبت‌محورند و باید با استاندارد کنترل‌شده یا کاتالوگ سازنده تطبیق داده شوند. PN مرجع است و اثر دما و ضرایب طراحی پروژه را لحاظ نمی‌کند. این ابزار افت فشار، نقطه کار پمپ، ضربه قوچ، بارهای سازه‌ای، سازگاری شیمیایی یا موجودی بازار را محاسبه نمی‌کند.

## Documentation | مستندات
See [the bilingual engineering guide](docs/ENGINEERING_GUIDE_FA_EN.md) and the supporting documents in `docs/`.

راهنمای جامع دوزبانه و فایل‌های آموزشی تکمیلی در پوشه `docs` قرار دارند.
