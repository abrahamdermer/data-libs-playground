# Vosk example (עברית): תמלול אודיו → טקסט
# דרישות: vosk, ffmpeg (אם עובדים עם פורמטים דחוסים). ל-WAV לא חובה ffmpeg.
from vosk import Model, KaldiRecognizer
import wave, json, sys
from pathlib import Path

AUDIO_PATH = Path("audio/voice_sample.wav")
MODEL_PATH = Path("models/vosk-model-small-he-0.22")

if not AUDIO_PATH.exists():
    sys.exit(f"לא נמצא קובץ אודיו: {AUDIO_PATH}. שים קובץ בתיקייה 'audio/'.")
if not MODEL_PATH.exists():
    sys.exit(f"לא נמצא מודל: {MODEL_PATH}. הורד ושמור ב-'models/'.")

# פתיחת WAV (מומלץ 16kHz Mono, 16-bit PCM)
wf = wave.open(str(AUDIO_PATH), "rb")
if wf.getnchannels() != 1 or wf.getsampwidth() != 2:
    print("⚠️ מומלץ להמיר ל-WAV מונו 16-bit לפני שימוש (למשל עם ffmpeg).")

model = Model(str(MODEL_PATH))
rec = KaldiRecognizer(model, wf.getframerate())

lines = []
while True:
    data = wf.readframes(4000)
    if len(data) == 0:
        break
    if rec.AcceptWaveform(data):
        res = json.loads(rec.Result())
        lines.append(res.get("text", ""))

final_res = json.loads(rec.FinalResult()).get("text", "")
lines.append(final_res)

transcript = " ".join([x for x in lines if x]).strip()
print("\n--- Transcript ---\n")
print(transcript or "[לא זוהה טקסט]")

# שמירת תמלול ליד קובץ האודיו
out_txt = AUDIO_PATH.with_suffix(".transcript.txt")
out_txt.write_text(transcript, encoding="utf-8")
print(f"\nנשמר תמלול: {out_txt.resolve()}")
