# راهنمای مهندسی انتخاب‌گر قطر HDPE

## بخش فارسی

### روش کار
دبی و سرعت هدف ورودی‌های اصلی هستند. برنامه گزینه‌های گرید و SDR را از بانک می‌خواند، ضخامت اسمی را استخراج می‌کند، قطر داخلی را از رابطه `ID=OD−2e` به دست می‌آورد و سرعت متوسط را محاسبه می‌کند.

### مثال
برای Q=50 m³/h و V=1.50 m/s قطر داخلی نظری حداقل 108.6 mm است. گزینه OD125 با ضخامت 11.4 mm سرعتی حدود 1.69 m/s دارد و رد می‌شود. گزینه OD140 با ضخامت 12.7 mm سرعتی حدود 1.35 m/s دارد و مناسب است. اعداد نمونه‌اند و نتیجه واقعی تابع رکورد بانک است.

### کاربردها
سایزینگ اولیه یک بخش لوله، مقایسه گرید و SDR و تهیه فهرست گزینه‌ها برای کنترل هیدرولیکی بعدی.

### محدودیت‌ها
این ابزار افت فشار، TDH، توان پمپ، ضربه قوچ، فشار مجاز دمایی یا بارهای سازه‌ای را محاسبه نمی‌کند. شبکه شاخه‌دار و مسیر چندقطری را مدل نمی‌کند. ابعاد اسمی و ضخامت‌های تخمینی باید با استاندارد و کاتالوگ سازنده کنترل شوند.

## English Section

### Method
The selector takes design flow and target velocity, filters the dimensional database by grade and SDR, calculates nominal ID from `ID=OD−2e`, and evaluates average velocity.

### Worked example
For Q=50 m³/h and V=1.50 m/s, the theoretical minimum ID is 108.6 mm. An OD125 record with 11.4 mm wall gives about 1.69 m/s and fails. An OD140 record with 12.7 mm wall gives about 1.35 m/s and complies. Values are illustrative; actual output depends on database records.

### Suitable applications
Preliminary sizing of one pipe segment, comparing grades and SDRs, and preparing candidate sizes for subsequent hydraulic checks.

### Limitations
The tool does not calculate pressure loss, TDH, pump power, water hammer, temperature-derated pressure rating or structural loads. It does not model branched networks or multi-diameter routes. Nominal dimensions and estimated wall thicknesses must be checked against standards and manufacturer catalogues.
