import pandas as pd
import numpy as np



def SMA(data, trend_period_days=21):
    """
    STATUS: VERIFIED (with Investing.com) on NVDA between 10-06-2019 & 14-06-2019
    The Simple Moving Average (Rolling Window) Indicator
    :param data: The original OHCLV and VWAP pandas DataFrame output of i.e. the data_loader.data_sources.get_stocks_data()
    :param trend_period_days: Int of the time period for computing the trend line values. Is 21 by default
    :return: A pandas Series
    """
    trend_period_name = str(trend_period_days) + "d"
    pd_dt_idx = data.index
    dt_dates_list = data.index.date.tolist()
    close = data.Close
    trend = data.Close.rolling(window=trend_period_days).mean()
    # sma_trend = pd.DataFrame({"Dates":dt_dates_list, "Close":close.values, trend_period_name:trend.values}, index=pd_dt_idx)
    sma_trend = pd.Series(trend.values, index=pd_dt_idx, name=trend_period_name)
    return sma_trend


def RSI_Timo(dataframe, column="Close", period=14):
    """
    STATUS: VERIFIED (with Investing.com) on NVDA between 10-06-2019 & 14-06-2019
    Relative Strength Index
    """

    delta = dataframe[column].diff()
    up, down = delta.copy(), delta.copy()

    up[up < 0] = 0
    down[down > 0] = 0

    roll_up = up.ewm(com=period - 1, adjust=False).mean()
    roll_down = down.ewm(com=period - 1, adjust=False).mean().abs()

    rsi = 100 - 100 / (1 + roll_up / roll_down)

    # return dataframe.join(rsi.to_frame('RSI'))
    return rsi


def EMA(data, trend_period_days=21, return_data=False, macd=False):
    """
    Exponential Moving Average
    """
    trend_period_name = str(trend_period_days) + "d"
    dt_dates_list = data.index.date.tolist()
    
    if return_data == False and macd == False:
        close = data.Close
        trend = data.Close.ewm(span=trend_period_days).mean()
        ema_trend = pd.DataFrame({"Dates":dt_dates_list, "Close":close.values, trend_period_name:trend.values}, index=range(len(dt_dates_list)))
        return ema_trend
    
    elif return_data == True and macd == False:
        trend = data.Close.ewm(span=trend_period_days).mean()
        return trend
    
    else:
        trend = data.ewm(span=trend_period_days).mean()
        return trend



def MACD(data, ema_days_upper=26, ema_days_lower=12, return_data=False):
    """
    Moving Average Convergence Divergence
    """
    dt_dates_list = data.index.date.tolist()
    close = data.Close
    
    ema_trend_26d = EMA(data, trend_period_days=ema_days_upper, return_data=True)
    ema_trend_12d = EMA(data, trend_period_days=ema_days_lower, return_data=True)
    trend = ema_trend_26d - ema_trend_12d
    macd_trend = pd.DataFrame({"Dates":dt_dates_list, "Close":close.values, "MACD":trend.values }, index=range(len(dt_dates_list)))

    if return_data == False:
        return macd_trend
    elif return_data == True:
        return trend


def MACD_signal_line(data):
    """
    Moving Average Convergence Divergence signal line. The MACD signal line is the difference between the MACD and the 9-day EMA of the MACD series,
    where the MACD is the difference between the 12-day an 26-day EMA. A positive signal line indicates a buy signal. A negative signal line a sell signal.  
    """
    dt_dates_list = data.index.date.tolist()
    close = data.Close
    
    macd = MACD(data, return_data=True)
    ema_9d = EMA(macd, trend_period_days=9, return_data=True, macd=True)
    signal_line = macd - ema_9d
    signal_line_trend = pd.DataFrame({"Dates":dt_dates_list, "Close":close.values, "MACD":macd.values, "9d EMA":ema_9d.values, "Signal Line":signal_line.values}, index=range(len(dt_dates_list)))
    
    return signal_line_trend
    

    return macd_trend


def moving_average_crossover(data, short_trend = 5, long_trend = 21):

    short_term_trend_col_name = str(short_trend) + "d"
    long_term_trend_col_name = str(long_trend) + "d"

    # short_long_term_trend_diff_name = short_term_trend_col_name + "-" + long_term_trend_col_name

    # short_long_term_trend_diff_name = short_term_trend_col_name + "-" + long_term_trend_col_name
    short_long_term_trend_diff_name = "-".join([short_term_trend_col_name, long_term_trend_col_name])

    close = data.Close
    dates = data.index

    short_term_trend = np.round(close.rolling(window=short_trend).mean(), 2)
    long_term_trend = np.round(close.rolling(window=long_trend).mean(), 2)


    short_long_term_trend_diff = short_term_trend - long_term_trend

    threshold = 5
    signal = np.where(short_long_term_trend_diff > threshold, "buy", "hold")
    signal = np.where(short_long_term_trend_diff < threshold, "sell", signal)
    resultdf = pd.DataFrame({"Close":close,"Signal":signal}, index=dates)
    return resultdf


def RSI_Xavier(datadf, period=14):
    """
    WARNING: THIS SEEMS TO MISCALCULATE THE RSI WHEN COMPARED TO Investing.com
    Relative Strength Index (RSI) is a momentum oscillator that measures the speed and change of price movements.
    RSI oscillates between zero and 100. Traditionally, and according to Wilder, RSI is considered overbought when above 70 and oversold when below 30.
    Signals can also be generated by looking for divergences, failure swings and centerline crossovers.
    RSI can also be used to identify the general trend."""

    ## get the price diff
    delta = datadf["Close"].diff()[1:]

    ## positive gains (up) and negative gains (down) Series
    up, down = delta.copy(), delta.copy()
    up[up < 0] = 0
    down[down > 0] = 0

    # EMAs of ups and downs
    _gain = up.ewm(span=period, min_periods=period).mean()
    _loss = down.abs().ewm(span=period, min_periods=period).mean()

    rs = _gain / _loss
    result = pd.Series(100 - (100 / (1 + rs)), name="RSI")
    return result



