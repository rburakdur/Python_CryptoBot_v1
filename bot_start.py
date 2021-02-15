import time
import getdata
import schedule
import telegram_bot


if __name__ == "__main__":
    telegram_bot.telegram_bot_sendtext("__ Online __")

    def calculate():
        return getdata.app("calculate")

    def check():
        return getdata.app("check")

    schedule.every(5).minutes.do(check)
    schedule.every(15).minutes.do(calculate)

    while True:
        schedule.run_pending()
        time.sleep(1)
