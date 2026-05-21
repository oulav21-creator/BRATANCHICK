import voice

voice.record_audio("audio.wav")
text = voice.transcribe("audio.wav")
print(text)