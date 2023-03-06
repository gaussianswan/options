import numpy as np
import pandas_market_calendars as mcal

from options.constants import NUMBER_OF_TRADING_DAYS
from options.positions import Position

from datetime import date
from typing import List

nyse_calendar = mcal.get_calendar("NYSE")

def time_to_expiry(expiry_date: date, start_date: date, calendar = nyse_calendar) -> float:

    market_calendar = calendar.schedule(start_date = start_date, end_date = expiry_date)
    number_of_days = market_calendar

    tte = number_of_days / NUMBER_OF_TRADING_DAYS

    return tte

