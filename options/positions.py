from typing import Union
from options.options import CallOption, PutOption
from options.enums import TradeSide

class Position:

    def __init__(self, side: TradeSide, quantity: int, option: Union[CallOption, PutOption]) -> None:
        self.side = side
        self.quantity = quantity
        self.option = option

    def intrinsic_value(self, price: float) -> float:
        return self.side.value * self.quantity * self.option.intrinsic_value(price = price)

    def delta(self) -> float:
        return self.side.value * self.quantity * self.option.delta()

    def gamma(self) -> float:
        return self.side.value * self.quantity * self.option.gamma()

    def vega(self) -> float:
        return self.side.value * self.quantity * self.vega()

    def rho(self) -> float:
        return self.side.value * self.quantity * self.rho()

    def theta(self) -> float:
        return self.side.value * self.quantity * self.theta()

