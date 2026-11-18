# راهنمای کاربر انتخاب‌گر قطر HDPE

## بخش فارسی

### ترتیب کار
۱. دبی را بر حسب m³/h وارد کنید.
۲. سرعت متوسط هدف را بر حسب m/s وارد کنید.
۳. EC جبران‌شده تا ۲۵°C و دمای واقعی آب را برای تخمین خواص وارد کنید.
۴. گرید PE80 یا PE100 را انتخاب کنید.
۵. SDR موجود برای گرید را انتخاب کنید.
۶. سایز پیشنهادی و گزینه‌های جایگزین را بررسی کنید.

### اجرا
```bash
python main.py
python -m unittest discover -s tests -v
```

### تفسیر و محدودیت
برنامه کوچک‌ترین OD موجود را که سرعت آن از هدف بیشتر نباشد انتخاب می‌کند. اگر هیچ سایزی شرط را برآورده نکند، بزرگ‌ترین گزینه همراه هشدار گزارش می‌شود. این خروجی انتخاب اولیه بر اساس سرعت است، نه تأیید فشار مجاز یا طراحی کامل خط.

## English Section

### Workflow
1. Enter flow rate in m³/h.
2. Enter target average velocity in m/s.
3. Enter EC compensated to 25°C and actual water temperature for fluid screening.
4. Select PE80 or PE100.
5. Select an SDR available for the chosen grade.
6. Review the recommended size and alternatives.

### Run
```bash
python main.py
python -m unittest discover -s tests -v
```

### Interpretation and limitation
The program selects the smallest available OD whose calculated velocity does not exceed the target. If no size complies, the largest available option is reported with a warning. This is a preliminary velocity-based selection, not pressure-rating verification or complete pipeline design.
