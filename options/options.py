import numpy as np

from options.funcs import time_to_expiry
from options.models.pricing_models import black_scholes_call_price, black_scholes_put_price
from datetime import date
from options.enums import OptionClass, OptionExerciseType

class CallOption:

    def __init__(self, underlying: str, strike: float, exercise_type: OptionExerciseType, expiry_date: date) -> None:
        self.underlying =underlying
        self.strike = strike
        self.exercise_type = exercise_type
        self.expiry_date = expiry_date

        self.option_class = OptionClass.CALL

    def intrinsic_value(self, price: float) -> float:
        return max(0, price - self.strike)

    def values_at_expiry(self, prices: np.array) -> np.array:
        return np.maximum(prices - self.strike, 0)

    def time_to_expiry(self, start_date: date) -> float:
        return time_to_expiry(expiry_date=self.expiry_date, start_date=start_date)

    def black_scholes_price(self, S: float, sigma: float, r: float, T: float = None, q: float = 0) -> float:
        if T is None:
            T = self.time_to_expiry(start_date=date.today())

        if OptionExerciseType.EUROPEAN:
            vals = black_scholes_call_price(S = S, K = self.strike, sigma = sigma, r = r, T = T, q = q)
        elif OptionExerciseType.AMERICAN:
            # TODO implement the american call option scheme
            vals = black_scholes_call_price(S = S, K = self.strike, sigma = sigma, r = r, T = T, q = q)

        return vals

    def delta(self) -> float:
        #TODO
        pass

    def gamma(self) -> float:
        #TODO
        pass

    def vega(self) -> float:
        #TODO
        pass

    def rho(self) -> float:
        #TODO
        pass

    def theta(self) -> float:
        #TODO
        pass

class PutOption:

    def __init__(self, underlying: str, strike: float, exercise_type: OptionExerciseType, expiry_date: date) -> None:
        self.underlying = underlying
        self.strike = strike
        self.exercise_type = exercise_type
        self.expiry_date = expiry_date

        self.option_class = OptionClass.PUT

    def intrinsic_value(self, price: float) -> float:

        return max(0, self.strike - price)

    def values_at_expiry(self, prices: np.array) -> np.array:

        return np.maximum(self.strike - prices, 0)

    def time_to_expiry(self, start_date: date) -> float:
        return time_to_expiry(expiry_date=self.expiry_date, start_date=start_date)

    def black_scholes_price(self, S: float, sigma: float, r: float, T: float = None, q: float = 0) -> float:
        if T is None:
            T = self.time_to_expiry(start_date=date.today())

        if OptionExerciseType.EUROPEAN:
            black_scholes_put_price(S = S, K = self.strike, sigma = sigma, r = r, T = T, q = q)
        elif OptionExerciseType.AMERICAN:
            # TODO implement the american call option scheme
            black_scholes_put_price(S = S, K = self.strike, sigma = sigma, r = r, T = T, q = q)

    def delta(self) -> float:
        #TODO
        pass

    def gamma(self) -> float:
        #TODO
        pass

    def vega(self) -> float:
        #TODO
        pass

    def rho(self) -> float:
        #TODO
        pass

    def theta(self) -> float:
        #TODO
        pass

