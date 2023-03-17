from options.options import CallOption, PutOption
from options.positions import Position
from options.enums import OptionExerciseType, TradeSide, OptionClass
from datetime import date
from typing import List

class VerticalSpread:

    def __init__(self, underlying: str, expiry: date, low_strike: float, high_strike: float, low_strike_side: TradeSide, high_strike_side: TradeSide,
                 option_class: OptionClass, low_strike_cost: float = 0, high_strike_cost: float = 0, low_strike_transaction_cost: float = 0, high_strike_transaction_cost: float = 0,
                 option_exercise_type: OptionExerciseType = OptionExerciseType.EUROPEAN, quantity: int = 1) -> None:

        assert low_strike < high_strike, "The low strike has to be strictly less than the high strike!"
        assert low_strike_side != high_strike_side, "You have to take opposing sides for this strategy to make sense!"

        self.underlying = underlying
        self.expiry = expiry
        self.low_strike = low_strike
        self.high_strike = high_strike
        self.low_strike_side = low_strike_side
        self.high_strike_side = high_strike_side
        self.option_class = option_class
        self.low_strike_cost = low_strike_cost
        self.high_strike_cost = high_strike_cost
        self.low_strike_transaction_cost = low_strike_transaction_cost
        self.high_strike_transaction_cost = high_strike_transaction_cost
        self.option_exercise_type = option_exercise_type
        self.quantity = quantity

        self.positions = self._create_options_positions()

    def _create_options_positions(self) -> List[Position]:

        if self.option_class == OptionClass.CALL:

            low_strike_option = CallOption(
            underlying=self.underlying,
            strike = self.low_strike,
            exercise_type=self.exercise_type,
            expiry_date=self.expiry
            )

            high_strike_option = CallOption(
                underlying=self.underlying,
                strike=self.low_strike,
                exercise_type=self.exercise_type,
                expiry_date=self.expiry
            )

        elif self.option_class == OptionClass.PUT:
            low_strike_option = PutOption(
                underlying=self.underlying,
                strike = self.low_strike,
                exercise_type=self.exercise_type,
                expiry_date=self.expiry
                )

            high_strike_option = PutOption(
                underlying=self.underlying,
                strike=self.low_strike,
                exercise_type=self.exercise_type,
                expiry_date=self.expiry
            )



        # Taking these options and creating positions

        low_strike_position = Position(
            side = self.low_strike_side,
            quantity=self.quantity,
            option = low_strike_option,
            cost = self.low_strike_cost,
            transaction_cost=self.low_strike_transaction_cost
        )

        high_strike_position = Position(
            side = self.high_strike_side,
            quantity=self.quantity,
            option=high_strike_option,
            cost = self.high_strike_cost,
            transaction_cost=self.high_strike_transaction_cost
        )

        return [low_strike_position, high_strike_position]

class LongCallVerticalSpread(VerticalSpread):

    def __init__(self, underlying: str, expiry: date, low_strike: float, high_strike: float, low_strike_cost: float = 0, high_strike_cost: float = 0, low_strike_transaction_cost: float = 0, high_strike_transaction_cost: float = 0, option_exercise_type: OptionExerciseType = OptionExerciseType.EUROPEAN, quantity: int = 1) -> None:
        super().__init__(underlying, expiry, low_strike, high_strike, TradeSide.LONG, TradeSide.SHORT, OptionClass.CALL, low_strike_cost, high_strike_cost, low_strike_transaction_cost, high_strike_transaction_cost, option_exercise_type, quantity)


class LongPutVerticalSpread(VerticalSpread):

    def __init__(self, underlying: str, expiry: date, low_strike: float, high_strike: float, low_strike_cost: float = 0, high_strike_cost: float = 0, low_strike_transaction_cost: float = 0, high_strike_transaction_cost: float = 0, option_exercise_type: OptionExerciseType = OptionExerciseType.EUROPEAN, quantity: int = 1) -> None:
        super().__init__(underlying, expiry, low_strike, high_strike, TradeSide.LONG, TradeSide.SHORT, OptionClass.PUT, low_strike_cost, high_strike_cost, low_strike_transaction_cost, high_strike_transaction_cost, option_exercise_type, quantity)


class ShortCallVerticalSpread(VerticalSpread):

    def __init__(self, underlying: str, expiry: date, low_strike: float, high_strike: float, low_strike_cost: float = 0, high_strike_cost: float = 0, low_strike_transaction_cost: float = 0, high_strike_transaction_cost: float = 0, option_exercise_type: OptionExerciseType = OptionExerciseType.EUROPEAN, quantity: int = 1) -> None:
        super().__init__(underlying, expiry, low_strike, high_strike, TradeSide.SHORT, TradeSide.LONG, OptionClass.CALL, low_strike_cost, high_strike_cost, low_strike_transaction_cost, high_strike_transaction_cost, option_exercise_type, quantity)


class ShortPutVerticalSpread(VerticalSpread):

    def __init__(self, underlying: str, expiry: date, low_strike: float, high_strike: float, low_strike_cost: float = 0, high_strike_cost: float = 0, low_strike_transaction_cost: float = 0, high_strike_transaction_cost: float = 0, option_exercise_type: OptionExerciseType = OptionExerciseType.EUROPEAN, quantity: int = 1) -> None:
        super().__init__(underlying, expiry, low_strike, high_strike, TradeSide.SHORT, TradeSide.LONG, OptionClass.PUT, low_strike_cost, high_strike_cost, low_strike_transaction_cost, high_strike_transaction_cost, option_exercise_type, quantity)