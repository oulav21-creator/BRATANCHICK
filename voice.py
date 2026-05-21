import whisper
import sounddevice as sd
from scipy.io.wavfile import write

def record_audio(filename, duration=5, fs=41000):
    print("Recording...")
    recording = sd.rec(int(duration * fs), samplerate=fs, channels=2)
    sd.wait()
    write(filename, fs, recording)
    print("Recording complete.")

model = whisper.load_model("small", device="cuda")

def transcribe(filename):
    audio = whisper.load_audio(filename)
    result = model.transcribe(audio)
    return result["text"]
  