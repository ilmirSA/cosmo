import os
import random
import time

import telegram
from dotenv import load_dotenv


def main():
    load_dotenv()
    token = os.getenv("TELEGRAM_TOKEN")
    chat_id = os.getenv("CHAT_ID")
    seconds_of_time = int(os.getenv("TIME"))

    bot = telegram.Bot(token=token)

    full_paths_to_images = []

    for pathdirs, dirs, filename in os.walk("image"):

        for img in filename:
            path = os.path.join(pathdirs, img)
            full_paths_to_images.append(path)

    while True:
        for image in random.choices(full_paths_to_images, k=1):
            with open(image,"rb") as img:
                bot.send_photo(chat_id=chat_id, photo=img)
        time.sleep(seconds_of_time)


if __name__ == "__main__":
    main()
