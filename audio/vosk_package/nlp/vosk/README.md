# Vosk — מדריך קצר

**מה זה?**  
Vosk היא ספריית Speech-to-Text קלה להרצה (אוף־ליין), מבוססת Kaldi. עובדת מהר על CPU ומתאימה להרצה בתוך Docker.

## למה להשתמש?
- תומך בהרבה פורמטים (WAV ישירות; MP3/OGG/MP4 דורש ffmpeg).
- ריצה אוף־ליין, בלי אינטרנט.
- קל לשלב בדוקר על CPU.

## התקנה מקומית
```bash
pip install vosk
```

## הורדת מודל עברית
הורד מודל מכאן: https://alphacephei.com/vosk/models  
מומלץ: `vosk-model-small-he-0.22`  
פרוס את התיקייה תחת `models/` כך שיהיה: `models/vosk-model-small-he-0.22/`

## הרצה
שימו קובץ אודיו ב-`audio/voice_sample.wav` (מומלץ WAV מונו 16kHz) והריצו:
```bash
python nlp/vosk/vosk_example.py
```

## Docker
בנו והריצו כך (מהשורש):
```bash
docker build -t vosk-stt -f nlp/vosk/Dockerfile .
# Windows PowerShell:
docker run --rm -v "$PWD/audio:/app/audio" -v "$PWD/models:/app/models" vosk-stt
# macOS/Linux:
# docker run --rm -v "$(pwd)/audio:/app/audio" -v "$(pwd)/models:/app/models" vosk-stt
```
