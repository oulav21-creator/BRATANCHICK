import voice
import brain
import actions
import json


voice.record_audio("audio.wav")
text = voice.transcribe("audio.wav")
response = brain.ask(text)
try:
    data = json.loads(response)
    if data["action"] == "open_website":
        actions.open_website(data["url"])
    
except:
        print(response)

