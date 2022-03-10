import os

import telegram
from dotenv import load_dotenv


def main():
    load_dotenv()
    token = os.getenv("TELEGRAM_TOKEN")

    bot = telegram.Bot(token=token)

    updates = bot.get_updates()
    #print(updates[0])
    bot.send_message(text='Привет пользователи!', chat_id=-1001783746663)


if __name__ == "__main__":
    main()
