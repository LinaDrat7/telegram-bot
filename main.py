
import os
import time
import random
from telegram import Bot

TOKEN = os.environ.get("TOKEN")
CHAT_IDS = os.environ.get("CHAT_IDS", "").split(",")
TEXTS = os.environ.get("TEXTS", "").split("||")

bot = Bot(token=TOKEN)

while True:
    text = random.choice(TEXTS).strip()
    for chat_id in CHAT_IDS:
        try:
            bot.send_message(chat_id=chat_id.strip(), text=text)
        except Exception as e:
            print(f"Error sending to {chat_id}: {e}")
    time.sleep(300)
