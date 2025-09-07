# Whisper — מדריך קצר

**מה זה?**  
Whisper הוא מודל Speech-to-Text של OpenAI שעובד גם אוף־ליין (CPU/GPU). תומך בהרבה שפות, כולל עברית.

## למה להשתמש?
- תמלול מדויק יחסית גם ברעש/מבטאים.
- עובד בתוך Docker (עם ffmpeg).
- תומך בקבצים רבים (WAV/MP3/MP4/OGG וכו').

## התקנה מקומית (ללא Docker)
```bash
pip install openai-whisper torch --upgrade
# מומלץ: התקן ffmpeg במערכת כדי לקרוא MP3/MP4/OGG
