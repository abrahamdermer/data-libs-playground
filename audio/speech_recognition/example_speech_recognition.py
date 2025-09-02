# Requires: microphone + internet for Google recognizer
import speech_recognition as sr
r = sr.Recognizer()
with sr.Microphone() as source:
    print("Say something...")
    audio = r.listen(source, timeout=5)
print("You said:", r.recognize_google(audio, language="en-US"))
