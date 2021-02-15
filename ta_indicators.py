import talib as ta
import numpy as np
import txt_db


class TechnicalAnylysis:

    ma1_value = 9
    ma2_value = 34
    stop_space = 1  # %
    current_i = 0
    back_check = 8
    ######################################################################################################

    def __init__(self, symbol1, interval, open, high, low, close):
        self.symbol = symbol1
        self.interval = interval
        self.open = open
        self.high = high
        self.low = low
        self.close = close

        self.indicators(self.symbol, self.interval, self.open,
                        self.high, self.low, self.close)

    def indicators(self, symbol, interval, open, high, low, close):
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

        self.ma_check(close_finished, high_finished,
                      low_finished, close_array, symbol, interval)

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
                txt_db.New_data(symbol, interval, resistance_level,
                                support_level, stop_level)
            else:
                pass  # bulamazsa ne yapsın?
