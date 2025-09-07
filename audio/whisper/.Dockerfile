FROM python:3.12-slim

# ffmpeg לנגינת/קריאת פורמטים דחוסים (mp3/mp4/ogg וכו')
RUN apt-get update && apt-get install -y --no-install-recommends ffmpeg \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app
# התקנת דרישות (Whisper + Torch)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# העתקת קוד + נשאיר למשתמש להעתיק קבצי אודיו החוצה
COPY . .

# פקודת ברירת מחדל: תמלול הדוגמה
CMD ["python", "nlp/whisper/whisper_example.py"]
