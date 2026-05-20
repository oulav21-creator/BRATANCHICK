import whisper
import sounddevice as sd
from scipy.io.wavfile import write

def record_audio(filename, duration = 5, fs = 41000):
    print("Recording...")
    recording = sd.rec(int(duration * fs), samplerate=fs, channels=2)
    sd.wait()
    write(filename, fs, recording)
    print("Recording complete.")

record_audio("audio.wav")
r = whisper.load_model("base")
audio = whisper.load_audio("audio.wav")
result = r.transcribe(audio)
print(result["text"])