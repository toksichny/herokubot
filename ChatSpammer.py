from pyrogram import Client
from datetime import datetime 
import asyncio
import shelve
import random
import time

#api_id = 8228878
#api_hash = "8a948f28b11e4146c9e233aa2b2f121d"
#phone_number = '+79630616024'


#print("Введите путь до txt файла с чатами")
dir = "chats.txt" #input()

with open(dir) as file:
    PUBLIC =  [row.strip() for row in file]

#print("Введите путь до txt файла с фразами")
phrase = "phrase.txt" #input()

with open(phrase,encoding='utf-8') as file:
    TEXT =  [row.strip() for row in file]


app = Client("chelik")#, api_id, api_hash,
             #phone_number=phone_number)


successsSend = 0
successsSendUserReplay = 0
async def main():
   async with app:
        
        while True:
            successsSend = 0
            successsSendUserReplay = 0

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
            
            processed_message = await shelve.open('processed_userID.db', writeback=True)
            chat_id = await app.get_dialogs()
            for i in range(len(chat_id)):
                try:  
                    uid = chat_id[i]["chat"]["id"]
                    if(str(uid)[0] != '-'):
                        name = chat_id[i]["chat"]["first_name"]
                        if str(uid) in processed_message:
                            print(f'Пропускаем уже обработанного пользователя ={uid}')
                            continue
                        processed_message[str(uid)] = True
                        await app.send_message(uid,"Привет, я уже запустила для тебя прриватную трансляцию, хочу тебе показать себя. Переходи быстрее, а то мне одной скучно) Вот ссылка на мою трансляцию: http://dtgfm.com/BKyK")
                        print(f"Сообщемние было отправленно USER_ID:{uid}, имя {name}")
                        successsSendUserReplay = successsSendUserReplay + 1
                    await asyncio.sleep(30)
                except:
                    print(f"Исключение KeyError. Скорее всего пользователю нельзя писать!")
            
            print(f"{current_time} Работа по всем чатам выполнена ухожу в слип на 1 часа\nУспешных сообщений отправлено {successsSend}\nУспешных реплаев {successsSendUserReplay}")
            await asyncio.sleep(3600)
        

app.run(main())
