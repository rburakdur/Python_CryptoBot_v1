import time
import getdata
import schedule


if __name__ == "__main__":
    def calculate():
        return getdata.app("calculate")

    def check():
        return getdata.app("check")

    schedule.every(5).minutes.do(check)
    schedule.every(15).minutes.do(calculate)

    while True:
        schedule.run_pending()
        time.sleep(1)
