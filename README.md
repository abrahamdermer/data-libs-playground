# Data Libraries Playground — מדריך מרכזי

ריפו זה כולל דוגמאות לספריות פייתון חשובות לפי תחום: GIS, תמונה, אודיו וטקסט.  
בכל תיקייה תמצאו:
- קובץ `example_*.py` — דוגמאות להרצה
- קובץ `README.md` — הסבר קצר בעברית + תרגילים

## תחומים שכבר מוכנים
- 🌍 GIS → [GeoPandas](gis/geopandas/README.md)
- 🖼️ Image → [OpenCV](image/opencv/README.md)
- 🎵 Audio → [PyDub](audio/pydub/README.md)
- 📝 Text → [NLTK](nlp/nltk/README.md)

## התקנה והרצה
1. צרו סביבת עבודה:
```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt



2. הרצה של דוגמה (לדוגמה GeoPandas):
```powershell
python gis/geopandas/example_geopandas.py
```

אותו הדבר עובד גם לתיקיות `image/`, `audio/`, `nlp/`.
