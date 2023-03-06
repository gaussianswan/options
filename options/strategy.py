from options.positions import Position
from typing import List

def get_total_delta(positions: List[Position]) -> float:

    delta = 0
    for pos in positions:
        delta += pos.delta()

    return delta

def get_total_gamma(positions: List[Position]) -> float:

    gamma = 0
    for pos in positions:
        gamma += pos.gamma()

    return gamma

def get_total_vega(positions: List[Position]) -> float:

    vega = 0
    for pos in positions:
        vega += pos.vega()

    return vega

def get_total_rho(positions: List[Position]) -> float:
    rho = 0
    for pos in positions:
        rho += pos.rho()

    return rho

def get_total_theta(positions: List[Position]) -> float:
    theta = 0
    for pos in positions:
        theta += pos.theta()

    return theta

class Strategy:

    def __init__(self, positions: List[Position]) -> None:
        self.positions = positions

    def intrinsic_value(self, price: float) -> float:

        value = 0
        for pos in self.positions:
            value += pos.quantity * pos.side.value * pos.intrinsic_value(price=price)

        return value

    def delta(self) -> float:
        return get_total_delta(positions=self.positions)

    def gamma(self) -> float:
        return get_total_gamma(positions=self.positions)

    def vega(self) -> float:
        return get_total_vega(positions=self.positions)

    def rho(self) -> float:
        return get_total_rho(positions=self.positions)

    def theta(self) -> float:
        return get_total_theta(positions=self.positions)


