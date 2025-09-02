import pyaudio
p = pyaudio.PyAudio()
print("Devices:", p.get_device_count())
for i in range(p.get_device_count()):
    info = p.get_device_info_by_index(i)
    print(i, info.get("name"), int(info.get("maxInputChannels",0)), int(info.get("maxOutputChannels",0)))
p.terminate()
