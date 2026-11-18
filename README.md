# HDPE Pipe Diameter Selector

## فارسی

### معرفی و قابلیت‌ها
این ابزار برای انتخاب اولیه قطر لوله پلی‌اتیلن بر اساس دبی و سرعت متوسط هدف است. کاربر PE80 یا PE100 و SDR موجود را انتخاب می‌کند؛ برنامه ضخامت اسمی را از بانک می‌خواند، قطر داخلی را از رابطه `ID=OD-2e` محاسبه می‌کند و کوچک‌ترین OD منطبق با سرعت هدف را پیشنهاد می‌دهد.

### نصب و اجرا
```bash
git clone https://github.com/alizarei-eng/hdpe-pipe-diameter-selector.git
cd hdpe-pipe-diameter-selector
python main.py
python -m unittest discover -s tests -v
```

### روابط
`Q_s=Q_h/3600`
`ID=OD-2e`
`A=πID²/4`
`V=Q_s/A`

### مثال
برای Q=50 m³/h و سرعت هدف 1.50 m/s، قطر داخلی نظری حداقل حدود 108.6 mm است. در مثال PE100 SDR11، OD125 با ضخامت تقریبی 11.4 mm سرعت حدود 1.69 m/s می‌دهد و مناسب نیست؛ OD140 با ضخامت تقریبی 12.7 mm سرعت حدود 1.35 m/s می‌دهد و شرط را برآورده می‌کند. خروجی واقعی تابع رکوردهای بانک است.

### موارد کاربرد
سایزینگ اولیه یک بخش لوله، مقایسه گرید و SDR و تهیه فهرست گزینه‌ها برای بررسی هیدرولیکی و اقتصادی بعدی.

### محدودیت‌ها
افت فشار، TDH، توان پمپ، ضربه قوچ، فشار مجاز در دمای کارکرد، بارهای سازه‌ای، دفن، روش اتصال و موجودی بازار محاسبه نمی‌شوند. مسیر چندقطری و شبکه شاخه‌دار نیز مدل نمی‌شود. بعضی ضخامت‌های بانک عمومی تخمینی یا نسبت‌محورند و باید با استاندارد یا کاتالوگ سازنده تطبیق داده شوند.

## English

### Overview and features
This tool performs preliminary HDPE pipe sizing based on design flow and target average velocity. The user selects PE80 or PE100 and an available SDR. The program reads nominal wall thickness from its database, calculates internal diameter using `ID=OD-2e`, and recommends the smallest OD that satisfies the velocity target.

### Installation and run
```bash
git clone https://github.com/alizarei-eng/hdpe-pipe-diameter-selector.git
cd hdpe-pipe-diameter-selector
python main.py
python -m unittest discover -s tests -v
```

### Equations
`Q_s=Q_h/3600`
`ID=OD-2e`
`A=πID²/4`
`V=Q_s/A`

### Worked example
For Q=50 m³/h and target velocity 1.50 m/s, the theoretical minimum internal diameter is approximately 108.6 mm. In an illustrative PE100 SDR11 case, OD125 with nominal wall thickness near 11.4 mm gives velocity near 1.69 m/s and does not comply; OD140 with wall thickness near 12.7 mm gives velocity near 1.35 m/s and complies. Actual output depends on database records.

### Suitable applications
Preliminary sizing of one pipe segment, comparison of grades and SDRs, and preparation of candidate sizes for subsequent hydraulic and economic review.

### Limitations
Pressure loss, TDH, pump power, water hammer, pressure rating at operating temperature, structural loads, burial, joining method and market availability are not evaluated. Multi-diameter routes and branched networks are not modelled. Some generic wall-thickness records are estimated or ratio-derived and must be verified against standards or manufacturer catalogues.
