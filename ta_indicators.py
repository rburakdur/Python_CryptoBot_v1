import talib as ta
import numpy as np
import telegram_bot as tbot


class TechnicalAnylysis:

    ma1_value = 9
    ma2_value = 34
    ma_cross_up = False
    stop_space = 1  # %
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
        self.ma_check(close_finished)

        if self.ma_cross_up:
            resistance_level = high_finished[-1]
            support_level = low_finished[-1]
            stop_level = support_level*(1.00 - self.stop_space/100)
            current_value = close_array[-1]

            # STATUS

            if current_value > resistance_level:
                status = "Al"
            elif current_value < support_level:
                status = "Sat"
            else:
                status = "Toplama Bölgesinde"

            # TO TELEGRAM
            tbot.telegram_bot_sendtext(symbol, interval, current_value,
                                       resistance_level, support_level, stop_level, status)
        # else:
        #    tbot.telegram_bot_sendtext(symbol, close_array[-1])

    def ma_check(self, close_finished):
        ma1 = ta.SMA(close_finished, self.ma1_value)
        ma2 = ta.SMA(close_finished, self.ma2_value)
        last_ma1 = ma1[-1]
        last_ma2 = ma2[-1]
        prev_ma1 = ma1[-2]
        prev_ma2 = ma2[-2]
        self.ma_cross_up = last_ma1 > last_ma2 and prev_ma1 < prev_ma2
