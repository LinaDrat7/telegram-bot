import os
import time
import random
from telegram import Bot

TOKEN = os.getenv("TOKEN")
CHAT_IDS = os.getenv("CHAT_IDS").split(",")
TEXTS = os.getenv("TEXTS").split("|")

bot = Bot(token=TOKEN)

def send_messages():
    while True:
        text = random.choice(TEXTS)
        for chat_id in CHAT_IDS:
            try:
                bot.send_message(chat_id=chat_id.strip(), text=text)
            except Exception as e:
                print(f"Failed to send to {chat_id}: {e}")
        time.sleep(300)

if __name__ == "__main__":
    send_messages()
