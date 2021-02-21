import time
import getdata
import schedule
import telegram_bot


def main():
    telegram_bot.telegram_bot_sendtext("__ Online __")
    print("Online")
    getdata.app("calculate")
    getdata.app("check")

    def calculate():
        return getdata.app("calculate")

    def check():
        return getdata.app("check")

    schedule.every(3).minutes.do(check)
    schedule.every(15).minutes.do(calculate)

    while True:
        schedule.run_pending()
        time.sleep(1)
