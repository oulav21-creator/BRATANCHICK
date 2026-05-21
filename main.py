import voice
import brain

voice.record_audio("audio.wav")
text = voice.transcribe("audio.wav")
response = brain.ask(text)
print(response)