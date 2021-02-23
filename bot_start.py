import time
import getdata
import schedule
import telegram_bot


def main():
    telegram_bot.telegram_bot_sendtext("__ Online __")
    print("Online")

    def calculate():
        return getdata.app("calculate")

    def check():
        return getdata.app("check")

    schedule.every(2).minutes.do(check)
    schedule.every(15).minutes.do(calculate)

    while True:
        schedule.run_pending()
        time.sleep(1)


getdata.app("check")
