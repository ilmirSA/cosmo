import os
import random
import time

import telegram
from dotenv import load_dotenv


def main():
    load_dotenv()
    token = os.getenv("TELEGRAM_TOKEN")

    t = int(os.getenv("TIME"))

    bot = telegram.Bot(token=token)
    updates = bot.get_updates()
    chat_id = updates[0]["channel_post"]["chat"]["id"]


    path_f = []

    for d, dirs, files in os.walk("image"):
        for f in files:
            path = os.path.join(d, f)
            path_f.append(path)

    while True:
        for fi in random.choices(path_f, k=1):
            bot.send_photo(chat_id=chat_id, photo=open(fi, 'rb'))
        time.sleep(t)


if __name__ == "__main__":
    main()
