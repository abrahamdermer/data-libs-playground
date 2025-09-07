
import speech_recognition as sr

# צור אובייקט Recognizer
r = sr.Recognizer()

# שימוש במיקרופון כהקלטה
with sr.Microphone() as source:
    print("אנא דבר עכשיו...")
    r.adjust_for_ambient_noise(source)  # התאמת רעש רקע
    audio = r.listen(source, phrase_time_limit=10)  # הקלטה

# ניסיון להמיר את ההקלטה לטקסט
try:
    text = r.recognize_google(audio, language="he-IL")
    print("תמלול:", text)
except sr.UnknownValueError:
    print("לא הצליח להבין את האודיו")
except sr.RequestError as e:
    print("שגיאת רשת; פרטים:", e)
