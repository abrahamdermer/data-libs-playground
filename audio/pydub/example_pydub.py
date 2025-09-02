from pydub import AudioSegment
from pydub.generators import Sine

# generate 2 seconds of a tone and export
tone = Sine(440).to_audio_segment(duration=2000).apply_gain(-6)
tone.export("audio/pydub_tone.wav", format="wav")
print("Wrote audio/pydub_tone.wav")

# חיתוך

sound = AudioSegment.from_wav("audio/pydub_tone.wav")

# 0–1000 מילישניות = שנייה ראשונה
first_second = sound[:1000]

first_second.export("audio/first_second.wav", format="wav")
print("Saved first_second.wav")


# חיבור

tone_a = Sine(440).to_audio_segment(duration=1000)  # "לה"
tone_b = Sine(523).to_audio_segment(duration=1000)  # "דו"

combined = tone_a + tone_b
combined.export("audio/two_notes.wav", format="wav")
print("Saved two_notes.wav")

# משנה עוצמה
tone = Sine(440).to_audio_segment(duration=2000)

louder = tone + 6   # מגביר 6dB
softer = tone - 6   # מנמיך 6dB

louder.export("audio/louder.wav", format="wav")
softer.export("audio/softer.wav", format="wav")



# מתחיל ומסים נמוך
tone = Sine(440).to_audio_segment(duration=3000)
# הפרמטר הוא משך הזמן
faded = tone.fade_in(1000).fade_out(1000)
faded.export("audio/faded.wav", format="wav")
print("Saved faded.wav")

# # דוגמה לשינוי פורמט
# # WAV ,RAW , AIFF / AU

# sound = AudioSegment.from_wav("tone.wav")
# sound.export("tone.aiff", format="aiff")
# print("Saved tone.aiff")