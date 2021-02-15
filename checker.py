import telegram_bot as tbot
import txt_db
import json
import numpy as np


intervals = ["15m"]  # , "30m", "1h", "4h"]

kkk = []


def check(symbol, close):
    ls = []
    # GETTING CURRENT VALUE
    close_array = np.asarray(close)
    now = float(close_array[-1])
    last = float(close_array[:-1][-1])

    # GETTING DATAS FROM DB
    db_data = txt_db.Get_data()

    # check for different time frames
    for interval in intervals:
        # parsing
        try:
            pair = db_data[f"{symbol}{interval}"]
            resistance = float(pair[0].get("resistance"))
            support = float(pair[0].get("support"))
            stop = float(pair[0].get("stop"))

            buy = last > resistance
            sell = last < support
            if buy:
                if (now > resistance):
                    status = "Al"
                if (resistance > now > support):
                    "Toplama Bölgesi"
                if (now < support):
                    "Sat"
                tbot.telegram_bot_sendtext(symbol=symbol, interval=interval,  current=now,
                                           resistance=resistance, support=support, stop=stop, status=status)
        except:
            pass
        # add to ls
        # ls.append(resistance)
        # ls.append(support)
        # ls.append(stop)
