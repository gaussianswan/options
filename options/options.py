import numpy as np

from options.funcs import time_to_expiry
from options.models.pricing_models import black_scholes_call_price, black_scholes_put_price
from options.models.greeks import delta_bs, gamma_bs, vega_bs, theta_bs, rho_bs
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

    def delta(self, S, sigma: float, r: float, T: float, q: float):

        if self.exercise_type == OptionExerciseType.AMERICAN:
            # Need to implement a method for getting the delta for american options that is not black scholes
            delta = delta_bs(option_type='call', S = S, sigma = sigma, K = self.strike, r = r, T = T, q = q)

        elif self.exercise_type == OptionExerciseType.EUROPEAN:
            delta = delta_bs(option_type='call', S = S, sigma = sigma, K = self.strike, r = r, T = T, q = q)

        return delta

    def gamma(self, S, sigma: float, r: float, T: float, q: float) -> float:

        if self.exercise_type == OptionExerciseType.AMERICAN:
            gamma = gamma_bs(S, self.strike, sigma, r, T, q)

        elif self.exercise_type == OptionExerciseType.EUROPEAN:
            gamma = gamma_bs(S, self.strike, sigma, r, T, q)

        return gamma

    def vega(self, S, sigma: float, r: float, T: float, q: float) -> float:
        if self.exercise_type == OptionExerciseType.AMERICAN:
            vega = vega_bs(S, self.strike, sigma, r, T, q)

        elif self.exercise_type == OptionExerciseType.EUROPEAN:
            vega = vega_bs(S, self.strike, sigma, r, T, q)

        return vega

    def rho(self, S, sigma: float, r: float, T: float, q: float) -> float:
        if self.exercise_type == OptionExerciseType.AMERICAN:
            rho = rho_bs('call', S, self.strike, sigma, r, T, q)

        elif self.exercise_type == OptionExerciseType.EUROPEAN:
            rho = rho_bs('call', S, self.strike, sigma, r, T, q)

        return rho

    def theta(self, S, sigma: float, r: float, T: float, q: float) -> float:
        if self.exercise_type == OptionExerciseType.AMERICAN:
            theta = theta_bs('call', S, self.strike, sigma, r, T, q)

        elif self.exercise_type == OptionExerciseType.EUROPEAN:
            theta = theta_bs('call', S, self.strike, sigma, r, T, q)

        return theta

    def __repr__(self) -> str:
        if self.option_class == OptionClass.CALL:
            option_letter = 'C'
        elif self.option_class == OptionClass.PUT:
            option_letter = 'P'

        representation = f"{self.underlying} {self.strike} {option_letter} {str(self.expiry_date)}"
        return representation

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

    def delta(self, S, sigma: float, r: float, T: float, q: float):

        if self.exercise_type == OptionExerciseType.AMERICAN:
            # Need to implement a method for getting the delta for american options that is not black scholes
            delta = delta_bs(option_type='put', S = S, sigma = sigma, K = self.strike, r = r, T = T, q = q)

        elif self.exercise_type == OptionExerciseType.EUROPEAN:
            delta = delta_bs(option_type='put', S = S, sigma = sigma, K = self.strike, r = r, T = T, q = q)

        return delta

    def gamma(self, S, sigma: float, r: float, T: float, q: float) -> float:

        if self.exercise_type == OptionExerciseType.AMERICAN:
            gamma = gamma_bs(S, self.strike, sigma, r, T, q)

        elif self.exercise_type == OptionExerciseType.EUROPEAN:
            gamma = gamma_bs(S, self.strike, sigma, r, T, q)

        return gamma

    def vega(self, S, sigma: float, r: float, T: float, q: float) -> float:
        if self.exercise_type == OptionExerciseType.AMERICAN:
            vega = vega_bs(S, self.strike, sigma, r, T, q)

        elif self.exercise_type == OptionExerciseType.EUROPEAN:
            vega = vega_bs(S, self.strike, sigma, r, T, q)

        return vega

    def rho(self, S, sigma: float, r: float, T: float, q: float) -> float:
        if self.exercise_type == OptionExerciseType.AMERICAN:
            rho = rho_bs('put', S, self.strike, sigma, r, T, q)

        elif self.exercise_type == OptionExerciseType.EUROPEAN:
            rho = rho_bs('put', S, self.strike, sigma, r, T, q)

        return rho

    def theta(self, S, sigma: float, r: float, T: float, q: float) -> float:
        if self.exercise_type == OptionExerciseType.AMERICAN:
            theta = theta_bs('put', S, self.strike, sigma, r, T, q)

        elif self.exercise_type == OptionExerciseType.EUROPEAN:
            theta = theta_bs('put', S, self.strike, sigma, r, T, q)

        return theta

    def __repr__(self) -> str:
        if self.option_class == OptionClass.CALL:
            option_letter = 'C'
        elif self.option_class == OptionClass.PUT:
            option_letter = 'P'

        representation = f"{self.underlying} {self.strike} {option_letter} {str(self.expiry_date)}"

        return representation
