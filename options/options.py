import numpy as np

from options.funcs import time_to_expiry
from datetime import date
from enums import OptionClass, OptionExerciseType

class CallOption:

    def __init__(self, underlying: str, strike: float, exercise_type: OptionExerciseType, expiry_date: date) -> None:
        self.underlying =underlying
        self.strike = strike
        self.exercise_type = exercise_type
        self.expiry_date = expiry_date

        self.option_class = OptionClass.CALL

    def intrinsic_value(self, price: float) -> float:
        return max(0, price - self.strike)

    def time_to_expiry(self, start_date: date) -> float:
        return time_to_expiry(expiry_date=self.expiry_date, start_date=start_date)

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

    def time_to_expiry(self, start_date: date) -> float:
        return time_to_expiry(expiry_date=self.expiry_date, start_date=start_date)

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

