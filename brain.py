import ollama

def ask(text):
    
    response = ollama.chat(model = "llama3.2", messages=[
        {
                "role": "system", "content": """Ты голосовой ассистент по имени BRATANCHIK. 
                Если пользователь просит выполнить какое-то действие на компьютере - отвечай в формате JSON. 
                Доступные действия:
                open_website - открыть сайт в браузере, принимает параметр url
                Пример ответа для команды: {"action": "open_website", "url": "vk.com"}
                Если пользователь просит открыть программу установленную на компьютере — используй open_app
                Пример ответа для команды: {"action": "open_app", "app": "notepad.exe"} 
                Если просит открыть сайт в интернете — используй open_website
                Если пользователь просто задаёт вопрос - отвечай текстом"""     
                }
                ,
        {
            "role": "user", "content": text
            }   
    ])
    return response.message.content