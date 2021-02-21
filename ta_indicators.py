import talib as ta
import numpy as np
import txt_db


class TechnicalAnylysis:
    ma1_value = 9
    ma2_value = 34
    stop_space = 1  # %
    current_i = 0
    back_check = 15
    ema_val = 14
    stop_tol = 2  # %
    ######################################################################################################

    def __init__(self, symbol1, interval, open, high, low, close):
        self.symbol = symbol1
        self.interval = interval
        self.open = open
        self.high = high
        self.low = low
        self.close = close

        self.main(self.symbol, self.interval, self.open,
                  self.high, self.low, self.close)

    def main(self, symbol, interval, open, high, low, close):
        # close
        close_array = np.asarray(close)
        close_finished = close_array[:-1]
        # open
        open_array = np.asarray(open)
        open_finished = open_array[:-1]
        # high
        high_array = np.asarray(high)
        high_finished = high_array[:-1]
        # low
        low_array = np.asarray(low)
        low_finished = low_array[:-1]

        ################################################################################################################################################

        av1 = self.ma_check(close_finished, high_finished,
                            low_finished, close_array, symbol, interval)
        av2 = self.most(close_finished)
        if not (av1 == None):
            av1.extend(av2)
            txt_db.New_data(av1[0], av1[1], av1[2],
                            av1[3], av1[4], av1[5], av1[6])
        ################################################################################################################################################

    def ma_check(self, close_finished, high_finished, low_finished, close_array, symbol, interval):
        ma1 = ta.SMA(close_finished, self.ma1_value)
        ma2 = ta.SMA(close_finished, self.ma2_value)
        for i in range(1, self.back_check):
            last_ma1 = ma1[-1*i]
            last_ma2 = ma2[-1*i]
            prev_ma1 = ma1[-1*(i+1)]
            prev_ma2 = ma2[-1*(i+1)]
            ma_cross_up = last_ma1 > last_ma2 and prev_ma1 < prev_ma2
            if ma_cross_up:
                current_i = -1*i
                resistance_level = high_finished[current_i]
                support_level = low_finished[current_i]
                stop_level = support_level*(1.00 - self.stop_space/100)

                # TO DATABASE
                av1 = [symbol, interval, resistance_level,
                       support_level, stop_level]
                return av1
            else:
                pass  # bulamazsa ne yapsın?

    def to_db(self, av):
        txt_db.New_data(av)

    def most(self, close_finished):
        ema = ta.EMA(close_finished, self.ema_val)
        last_ema = round(ema[-1], 7)
        ema_stop = last_ema * (1-self.stop_tol/100)

        av2 = [last_ema, ema_stop]
        return av2

# if (ma_stop > ema_stop):
#                main_stop = ma_stop
#            elif (ema_stop > ma_stop):
#                main_stop = ema_stop
