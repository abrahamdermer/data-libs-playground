import librosa, numpy as np
import soundfile as sf

# Generate a 1-second sine wave (440 Hz) so we don't need an audio file
sr = 22050
t = np.linspace(0,1,sr,False)
y = 0.2*np.sin(2*np.pi*440*t)
sf.write("audio/tone.wav", y, sr)

y2, sr2 = librosa.load("audio/tone.wav", sr=None)
tempo, _ = librosa.beat.beat_track(y=y2, sr=sr2)
print("Estimated tempo:", float(tempo))
