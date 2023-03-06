from options.options import CallOption, PutOption
from options.enums import TradeSide
from options.positions import Position
from options.enums import OptionExerciseType
from datetime import date

class Staddle:

    def __init__(self, underlying: str, strike: float, quantity: int, exercise_type: OptionExerciseType, expiry_date: date, trade_side: TradeSide = TradeSide.LONG) -> None:
        self.underlying = underlying
        self.strike = strike
        self.trade_side = trade_side
        self.quantity = quantity
        self.exercise_type = exercise_type
        self.expiry_date = expiry_date

        call = self._create_call()
        put = self._create_put()

        self.call_position = Position(side = self.trade_side, quantity = self.quantity, option = call)
        self.put_position = Position(sdie = self.trade_side, quantity = self.quantity, option=put)

        self.positions = [self.call_position, self.put_position]

    def _create_call(self) -> CallOption:
        call_option = CallOption(
            underlying=self.underlying,
            strike=self.strike,
            exercise_type=self.exercise_type,
            expiry_date=self.expiry_date
        )

        return call_option

    def _create_put(self) -> PutOption:
        put_option = PutOption(
            underlying=self.underlying,
            strike=self.strike,
            exercise_type=self.exercise_type,
            expiry_date=self.expiry_date
        )

        return put_option

    def intrinsic_value(self, price: float) -> float:
        value = 0
        for pos in self.positions:
            value +=  pos.intrinsic_value(price = price)

        return value

    def delta(self) -> float:
        pass

    def vega(self) -> float:
        pass

    def rho(self) -> float:
        pass

    def theta(self) -> float:
        pass


class Strangle:

    def __init__(self) -> None:
        pass


class Butterfly:

    def __init__(self) -> None:
        pass

class Condor:

    def __init__(self) -> None:
        pass

class CalendarSpread:

    def __init__(self) -> None:
        pass

class BullSpread:

    def __init__(self) -> None:
        pass

class BearSpread:

    def __init__(self) -> None:
        pass