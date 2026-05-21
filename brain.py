import ollama

def ask(text):
    
    response = ollama.chat(model = "llama3.2", messages=[
        {
                "role": "system", "content": "Ты голосовой ассистент по имени BRATANCHIK. Отвечай кратко и только на русском языке."      
                }
                ,
        {
            "role": "user", "content": text
            }   
    ])
    return response.message.content