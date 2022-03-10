import os

import telegram
from dotenv import load_dotenv


def main():
    load_dotenv()
    token = os.getenv("TELEGRAM_TOKEN")
    chat_id = os.getenv("CHAT_ID")
    bot = telegram.Bot(token=token)
    updates = bot.get_updates()
    bot.send_photo(chat_id=chat_id, photo=open('image/earth_3.png', 'rb'))


if __name__ == "__main__":
    main()
