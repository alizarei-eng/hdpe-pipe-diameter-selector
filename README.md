# HDPE Pipe Diameter Selector

## فارسی

### معرفی
این ابزار برای انتخاب اولیه قطر لوله پلی‌اتیلن بر اساس دبی طراحی و سرعت متوسط هدف ساخته شده است. کاربر گرید PE80 یا PE100 و SDR موجود را انتخاب می‌کند؛ برنامه ضخامت اسمی را از بانک می‌خواند، قطر داخلی را محاسبه می‌کند و کوچک‌ترین OD منطبق با سرعت هدف را پیشنهاد می‌دهد.

### قابلیت‌ها
- انتخاب گرید و SDR از گزینه‌های موجود در بانک
- محاسبه ID از OD و ضخامت اسمی
- محاسبه سرعت متوسط برای سایزهای کاتالوگی
- نمایش سایز پیشنهادی و گزینه‌های جایگزین
- تخمین غربالگری برخی خواص سیال بر اساس EC

### نصب و اجرا
```bash
git clone https://github.com/alizarei-eng/hdpe-pipe-diameter-selector.git
cd hdpe-pipe-diameter-selector
python main.py
python -m unittest discover -s tests -v
```

### روش محاسبه
`Q_s=Q_h/3600`
`ID=OD-2e`
`A=πID²/4`
`V=Q_s/A`

### مثال
برای Q=50 m³/h و سرعت هدف 1.50 m/s، قطر داخلی نظری حداقل حدود 108.6 mm است. در مثال کاتالوگی PE100 SDR11، OD125 با ضخامت تقریبی 11.4 mm سرعت حدود 1.69 m/s می‌دهد و مناسب نیست؛ OD140 با ضخامت تقریبی 12.7 mm سرعت حدود 1.35 m/s می‌دهد و شرط را برآورده می‌کند. انتخاب نهایی تابع رکوردهای واقعی بانک است.

### موارد کاربرد
- سایزینگ اولیه یک بخش لوله با دبی مشخص
- مقایسه گرید، SDR و ODهای موجود
- تهیه فهرست گزینه‌ها برای بررسی هیدرولیکی و اقتصادی بعدی

### محدودیت‌ها
این برنامه افت فشار، TDH، توان پمپ، ضربه قوچ، فشار مجاز در دمای کارکرد، بارهای سازه‌ای، دفن، روش اتصال یا موجودی بازار را بررسی نمی‌کند. مسیر چندقطری و شبکه شاخه‌دار را نیز مدل نمی‌کند. بعضی ضخامت‌های بانک عمومی تخمینی یا نسبت‌محورند و باید با استاندارد کنترل‌شده یا کاتالوگ سازنده تطبیق داده شوند.

راهنمای تفصیلی در پوشه docs قرار دارد.

---

## English

### Overview
This tool performs preliminary HDPE pipe sizing based on design flow and target average velocity. The user selects PE80 or PE100 and an available SDR. The program reads nominal wall thickness from its database, calculates internal diameter and recommends the smallest outside diameter that satisfies the velocity target.

### Features
- Grade and SDR selection from available database records
- Internal-diameter calculation from OD and nominal wall thickness
- Average-velocity calculation for catalogue sizes
- Recommended size and alternative options
- EC-based screening estimates for selected fluid properties

### Installation and run
```bash
git clone https://github.com/alizarei-eng/hdpe-pipe-diameter-selector.git
cd hdpe-pipe-diameter-selector
python main.py
python -m unittest discover -s tests -v
```

### Calculation method
`Q_s=Q_h/3600`
`ID=OD-2e`
`A=πID²/4`
`V=Q_s/A`

### Worked example
For Q=50 m³/h and target velocity 1.50 m/s, the theoretical minimum internal diameter is approximately 108.6 mm. In an illustrative PE100 SDR11 catalogue example, OD125 with nominal wall thickness near 11.4 mm gives velocity near 1.69 m/s and does not comply; OD140 with wall thickness near 12.7 mm gives velocity near 1.35 m/s and complies. The actual recommendation depends on the database records.

### Suitable applications
- Preliminary sizing of one pipe segment at a specified flow
- Comparing available grades, SDRs and outside diameters
- Preparing a shortlist for subsequent hydraulic and economic review

### Limitations
The program does not calculate pressure loss, TDH, pump power, water hammer, pressure rating at operating temperature, structural loads, burial, joining method or market availability. It does not model multi-diameter routes or branched networks. Some generic wall-thickness records are estimated or ratio-derived and must be verified against the controlled standard or manufacturer's catalogue.

Detailed guides are available in the docs directory.
