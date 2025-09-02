from pydub import AudioSegment
from pydub.generators import Sine

# generate 2 seconds of a tone and export
tone = Sine(440).to_audio_segment(duration=2000).apply_gain(-6)
tone.export("audio/pydub_tone.wav", format="wav")
print("Wrote audio/pydub_tone.wav")
