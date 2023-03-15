import pandas as pd
import numpy as np

def gk_element(bar: pd.Series) -> float:

    elem = 0.511 * (np.log(bar.high/bar.low))**2 - 0.019*np.log(bar.close/bar.open)*np.log(bar.high*bar.low/bar.open**2) - 2*np.log(bar.high/bar.open)*np.log(bar.low/bar.open)

    return elem

def parkinson_element(bar: pd.Series) -> float:

    element = np.log(bar.high/bar.low)**2

    return element

def roger_satchell_element(bar: pd.Series) -> float:

    return np.log(bar.high/bar.close)*np.log(bar.high/bar.open) + np.log(bar.low/bar.close)*np.log(bar.low/bar.open)


def garman_klass_vol(ohlc_bars: pd.DataFrame, trading_days: int = 21, rolling_period: int = 30) -> float:

    assert trading_days >= 1

    gk_elements = ohlc_bars.apply(ohlc_bars, axis = 0)
    gk_variances = gk_elements.rolling(rolling_period).mean()
    gk_vol = gk_variances.apply(np.sqrt) * np.sqrt(trading_days)

    return gk_vol


def parkinson_vol(ohlc_bars: pd.DataFrame, trading_days: int = 21, rolling_period: int = 30) -> float:

    assert trading_days >= 1, "The trading days have to be greater than or equal to 1"
    parkinson_variances = (1/(4*np.log(2)))*ohlc_bars.apply(parkinson_element, axis = 1).rolling(rolling_period).mean()
    parkinson_vol = (parkinson_variances ** 0.5 ) * np.sqrt(trading_days)

    return parkinson_vol

def roger_satchell_vol(ohlc_bars: pd.DataFrame, trading_days: int = 21, rolling_period: int = 30) -> float:

    assert trading_days >= 1, "The trading days have to be greater than or equal to 1"
    roger_satchell_variances = ohlc_bars.apply(roger_satchell_element, axis = 1).rolling(rolling_period).mean()
    roger_satchell_vol = roger_satchell_variances ** 0.5 * np.sqrt(trading_days)

    return roger_satchell_vol


