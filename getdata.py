# https: // www.onbirkod.com/python-ile-kripto-para-al-sat-botu-yazalim-trading-bot/
from binance.client import Client
import ta_indicators
import checker
import time


class BinanceConnection:
    def __init__(self, file):
        self.connect(file)

    # Binance Client
    def connect(self, file):
        lines = [line.rstrip("\n") for line in open(file)]
        key = lines[0]
        secret = lines[1]
        self.client = Client(key, secret)


def app(mission):
    filename = "config.txt"
    connection = BinanceConnection(filename)
    coins = [coin.rstrip("\n") for coin in open("coin_list.txt")]
    intervals = ["15m"]  # , "30m", "1h", "4h"]

    # while True:
    #    time.sleep(50)  # seconds

    # Searching coins
    if mission == "calculate":
        for current_interval in intervals:
            for current_coin in coins:

                # Check for every coins in coin_list.txt
                symbol = current_coin
                interval = current_interval
                limit = 200

                try:  # get data for coin
                    klines = connection.client.get_klines(
                        symbol=symbol, interval=interval, limit=limit)
                except Exception as exp:
                    print(exp.status_code, flush=True)
                    print(exp.message, flush=True)

                    # Coin values
                op = [float(entry[1]) for entry in klines]
                high = [float(entry[2]) for entry in klines]
                low = [float(entry[3]) for entry in klines]
                close = [float(entry[4]) for entry in klines]

             # Calculate Supports, Resistances
                ta_indicators.TechnicalAnylysis(
                    symbol, interval, op, high, low, close)
            print(f"{current_interval} Calculated.")

    elif mission == "check":
        for current_coin in coins:
            symbol = current_coin
            interval = "15m"
            limit = 200

            try:  # get data for coin
                klines = connection.client.get_klines(
                    symbol=symbol, interval=interval, limit=limit)
            except Exception as exp:
                print(exp.status_code, flush=True)
                print(exp.message, flush=True)

            # GETTING LAST VALUE
            close = [float(entry[4]) for entry in klines]
            checker.check(symbol, close)
        print("check complete.")


if __name__ == "__main__":
    app()
