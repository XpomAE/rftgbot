import redis
import os
import telebot
import math
import random
import time
import threading
from emoji import emojize


from telethon import TelegramClient, events, sync
api_id = 541670['apiid']
api_hash = e4b71141f5b96dfd5585659170d8aafa ['apihash']
client = TelegramClient('session', api_id, api_hash)

#get session
client.send_file('yshevdjajdiehrhx', 'sname.session')
#/get session

#handlers
@client.on(events.NewMessage)
async def my_events_handler(event):
    chat = await event.get_input_chat()
    if chat.user_id == 577009581:
        if 'start' in event.raw_text or 'снова жив' in event.raw_text:
            time.sleep(random.randint(5,7))
            await client.send_message('rf_telegram_bot','💖 Пополнить здоровье')
            time.sleep(random.randint(5,7))
            await client.send_message('rf_telegram_bot','🏜 31-40 Сеттовая пустыня')
        if 'На пути у вас встретился' in event.raw_text:
            time.sleep(random.randint(5,7))
            await client.send_message('rf_telegram_bot','🐺По уровню')
        if  'Вы наткнулись' in event.raw_text:
            time.sleep(random.randint(5,7))
            await client.send_message('rf_telegram_bot','🔪 Атаковать')
        if  'к энергии' in event.raw_text:
            time.sleep(random.randint(5,7))
            await client.send_message('rf_telegram_bot','💖 Пополнить здоровье')
            time.sleep(random.randint(5,7))
            await client.send_message('rf_telegram_bot','🏜 31-40 Сеттовая пустыня')



#/handlers



#/code

client.run_until_disconnected()
