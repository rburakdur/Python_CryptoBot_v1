import telegram_bot as tbot
import txt_db
import json
import numpy as np
from talib import EMA
import pytz
from datetime import datetime


def zaman():
    tz = pytz.timezone('Asia/Istanbul')
    time_now = datetime.now(tz).strftime("%d.%m.%Y %H:%M:%S")
    return str(time_now)


intervals = ["15m", "30m", "1h", "4h"]


def check(symbol, close):

    # GETTING CURRENT VALUE
    close_array = np.asarray(close)
    close_finished = close_array[:-1]
    current_val = float(close_array[-1])
    last = float(close_finished[-1])
    last_previous = float(close_finished[-2])

    # GETTING DATAS FROM DB
    db_data = txt_db.Get_data()

    # checking for ma conditions
    ma_check(db_data, symbol, last, last_previous, current_val, close_finished)

    # check for different time frames


def ma_check(db_data, symbol, last, last_previous, now, close_finished):
    ls = []
    for interval in intervals:
        # parsing
        try:
            pair = db_data[f"{symbol}"][0][f"{interval}"][0]
            resistance = float(pair["resistance"])
            support = float(pair["support"])
            stop = float(pair["stop"])
            ema14 = float(pair["ema14"])
            emaStop = float(pair["ema_stop"])

            buy = last > resistance and last_previous < resistance
            # sell = last < stop and last_previous < support

            if buy:
                if (resistance >= now and now >= support):
                    status = "Toplama Bölgesi"
                if (now > resistance):
                    status = "Al"
                if (now < support and now > stop):
                    status = "Dikkat"
                if (last < stop):
                    status = "!! STOP !!"

                ls.append([symbol, interval, status, now,
                           resistance, support, stop, ema14, emaStop])

        except:
            break

    if not (len(ls) == 0):

        ls_check(ls)


def ls_check(ls):

    tg = []
    for i in range(len(ls)):
        w = ls[i][0], ls[i][1], ls[i][4], ls[i][5], ls[i][6], ls[i][7], ls[i][3], ls[i][2], zaman()
        p1 = float(ls[i][3])
        p2 = float(ls[i][4])
        percent = round(((p1 - p2)*100/p2), 2)
        t = f"*{ls[i][0]}*" + "\t" + f"*{ls[i][1]}*\n" + "\n" + \
            f"__*{ls[i][2]}*__\n" + "\n" + \
            f"Now : {ls[i][3]}" + "\t" + f"(% {percent})\n" \
            f"Resistance : {ls[i][4]}\n" + \
            f"Support : {ls[i][5]}\n" + \
            f"Stop : {ls[i][6]}\n" + \
            f"Ema14 : {ls[i][7]}\n" + \
            f"Ema Stop : {ls[i][8]}"
        txt_db.update(w)
        tg.append(t)

    # to web
    to_telegram(tg)


def to_telegram(tg):
    print(tg)
    tbot.buy_message(tg)

    # add to ls
    # ls.append(resistance)
    # ls.append(support)
    # ls.append(stop)
# ma_check(db_data, ls, doge, 0.056, 0.055, 0.0549)


#profit = round(((last-resistance)*100/resistance), 2)
#                message = f"{symbol} {inter}\n% {profit} ile kapatıldı."
