from pyrogram import Client
from datetime import datetime 
import keyboard
import asyncio
import shelve
import random
import time

#print("Введите путь до txt файла с чатами")
dir = "chats.txt" #input()

with open(dir) as file:
    PUBLIC =  [row.strip() for row in file]

#print("Введите путь до txt файла с фразами")
phrase = "phrase.txt"#input()

with open(phrase,encoding='utf-8') as file:
    TEXT =  [row.strip() for row in file]

app = Client("chelik")#, api_id, api_hash,
             #phone_number=phone_number)



async def main():
   async with app:
        
        while True:
            successsSend = 0
            for i in range(len(PUBLIC)):
                now = datetime.now() 
                current_time = now.strftime("%H:%M:%S")
                try:
                    await app.join_chat(PUBLIC[i])
                    public = await app.get_chat(PUBLIC[i])
                    chat = public
                    text = random.choice(TEXT)
                    await app.send_message(chat.id, text)
                    successsSend = successsSend + 1
                    print(f"{current_time} Сообщение {text} отправлено в чат {PUBLIC[i]}\n{current_time} Ухожу в откат на 5 минут")
                    await asyncio.sleep(300)
                    
                except:
                    print(f"{current_time} Исключение KeyError. Не смог найти чат {PUBLIC[i]}\n")
                    await asyncio.sleep(2)
                else:
                    print(f"{current_time} Успех! Ошибок не возникло!")
                
            print(f"{current_time} Работа по всем чатам выполнена ухожу в слип на 1 часа\nУспешных сообщений отправлено {successsSend}")
            await asyncio.sleep(3600)
            

app.run(main())
