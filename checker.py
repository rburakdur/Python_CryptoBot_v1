import telegram_bot as tbot
import txt_db
import json
import numpy as np
from talib import EMA

ema1_val = 5
ema2_val = 13
intervals = ["15m", "30m", "1h", "4h"]


def check(symbol, close):

    # GETTING CURRENT VALUE
    close_array = np.asarray(close)
    close_finished = close_array[:-1]
    current_val = float(close_array[-1])
    last = float(close_array[:-1][-1])
    last_previous = float(close_array[:-1][-2])

    # GETTING DATAS FROM DB
    db_data = txt_db.Get_data()

    # checking for ma conditions
    ma_check(db_data, symbol, last, last_previous, current_val, close_finished)

    # check for different time frames


def sell_check(symbol, inter, resistance, close_finished, current_val):

    ema1 = EMA(close_finished, ema1_val)
    ema2 = EMA(close_finished, ema2_val)
    current1 = ema1[-1]
    current2 = ema2[-1]
    prev1 = ema1[-2]
    prev2 = ema2[-2]
    c1 = current1 < current2 and prev1 > prev2
    c2 = current_val > resistance
    if (c1 and c2):
        profit = round(((current_val-resistance)*100/resistance), 2)
        message = f"{symbol} {inter}\n% {profit} ile kapatıldı."

        tbot.profit_message(message)


def ma_check(db_data, symbol, last, last_previous, now, close_finished):
    ls = []
    for interval in intervals:
        # parsing
        try:
            pair = db_data[f"{symbol}{interval}"]
            resistance = float(pair[0].get("resistance"))
            support = float(pair[0].get("support"))
            stop = float(pair[0].get("stop"))

            buy = last > resistance and last_previous < resistance
            #sell = last < stop and last_previous < support
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
                           resistance, support, stop])

        except:
            break
        sell_check(symbol, interval, resistance, close_finished, now)

    if not (len(ls) == 0):
        ls_check(ls)


def ls_check(ls):
    tg = []
    for i in range(len(ls)):
        p1 = float(ls[i][3])
        p2 = float(ls[i][4])
        percent = round(((p1 - p2)*100/p2), 2)
        t = f"*{ls[i][0]}*" + "\t" + f"*{ls[i][1]}*\n" + "\n" + \
            f"__*{ls[i][2]}*__\n" + "\n" + \
            f"Now : {ls[i][3]}" + "\t" + f"(% {percent})\n" \
            f"Resistance : {ls[i][4]}\n" + \
            f"Support : {ls[i][5]}\n" + \
            f"Stop : {ls[i][6]}"
        tg.append(t)
    to_telegram(tg)


def to_telegram(tg):
    print(tg)
    tbot.buy_message(tg)

    # add to ls
    # ls.append(resistance)
    # ls.append(support)
    # ls.append(stop)
#ma_check(db_data, ls, doge, 0.056, 0.055, 0.0549)
