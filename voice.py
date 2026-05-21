import whisper
import sounddevice as sd
from scipy.io.wavfile import write

def record_audio(filename, duration=10, fs=41000):
    print("Recording...")
    recording = sd.rec(int(duration * fs), samplerate=fs, channels=2)
    sd.wait()
    write(filename, fs, recording)
    print("Recording complete.")

def transcribe(filename):
    r = whisper.load_model("small", device="cuda")
    audio = whisper.load_audio(filename)
    result = r.transcribe(audio)
    return result["text"]
  