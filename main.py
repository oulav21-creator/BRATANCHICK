import voice
import brain
import actions
import json


voice.record_audio("audio.wav")
text = voice.transcribe("audio.wav")
response = brain.ask(text)
try:
    data = json.loads(response)
    print(data)
    if data["action"] == "open_website":
        actions.open_website(data["url"])
    if data["action"] == "open_app":
        actions.open_app(data["app"])
    
except Exception as e:
    print(response)
    print(e)

