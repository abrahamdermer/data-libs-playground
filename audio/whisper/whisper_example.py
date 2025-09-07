

# Whisper example (עברית): תמלול אודיו → טקסט
# דרישות: openai-whisper, torch, ffmpeg (לקריאת פורמטים דחוסים)
import whisper
from pathlib import Path
import sys

# קובץ אודיו לבדיקה (שנה אם צריך)
AUDIO_PATH = Path("audio/voice_sample.wav")  # אפשר גם .mp3/.mp4/.ogg

if not AUDIO_PATH.exists():
    sys.exit(f"לא נמצא קובץ אודיו: {AUDIO_PATH}. שים קובץ בתיקייה 'audio/'.")

# בחרו דגם: tiny / base / small / medium / large
MODEL_NAME = "base"
print(f"Loading Whisper model: {MODEL_NAME} ...")
model = whisper.load_model(MODEL_NAME)  # רץ על CPU כברירת מחדל; אם יש CUDA וזמין, ישתמש בו

# קידוד/טעינה פנימית נעשית ע״י ffmpeg דרך whisper
print(f"Transcribing: {AUDIO_PATH}")
result = model.transcribe(str(AUDIO_PATH), language="he")  # שנו ל-"en" באנגלית, או השמיטו לזיהוי אוטומטי

text = result.get("text", "").strip()
print("\n--- Transcript ---\n")
print(text or "[לא זוהה טקסט]")

# שמירה לקובץ ליד האודיו
out_txt = AUDIO_PATH.with_suffix(".transcript.txt")
out_txt.write_text(text, encoding="utf-8")
print(f"\nנשמר תמלול: {out_txt.resolve()}")
