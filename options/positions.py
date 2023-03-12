import numpy as np

from datetime import date
from typing import Union, List
from options.options import CallOption, PutOption
from options.enums import TradeSide

class Position:

    def __init__(self, side: TradeSide, quantity: int, option: Union[CallOption, PutOption]) -> None:
        self.side = side
        self.quantity = quantity
        self.option = option
        self.underlying = option.underlying

    def intrinsic_value(self, price: float) -> float:
        return self.side.value * self.quantity * self.option.intrinsic_value(price = price)

    def values_at_expiry(self, prices: np.array) -> np.array:
        return self.side.value * self.option.values_at_expiry(prices=prices)

    def black_scholes_value(self, S: float, sigma: float, r: float, T: float = None, q: float = 0) -> float:
        return self.side.value * self.option.black_scholes_price(S, sigma, r, T, q)

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


class Trade:

    def __init__(self, side: TradeSide, quantity: int, option: Union[CallOption, PutOption], cost: float, transaction_cost: float = 0) -> None:
        self.side = side
        self.quantity = quantity
        self.transaction_cost = transaction_cost
        self.position = Position(side = side, quantity=quantity, option = option)
        self.cost = cost

    def profit_at_expiry(self, price: float) -> float:
        """Calculates the profit at expiry for this trade

        Args:
            price (float): price at expiration as a float

        Returns:
            float: Payoff at expiry
        """

        intrinsic_value = self.intrinsic_value(price=price)
        return intrinsic_value - self.side.value * self.cost - self.transaction_cost

    def profits_at_expiry(self, prices: np.array) -> np.array:
        """Generates the profit at expiry for an array of values

        Args:
            prices (np.array): Array of prices as a numpy array

        Returns:
            np.array: Profits at expiry as a numpy array
        """
        values_at_expiry = self.position.values_at_expiry(prices=prices)

        return values_at_expiry - self.side.value * self.cost - self.transaction_cost

    def black_scholes_profit(self, S: float, sigma: float, r: float, T: float = None, q: float = 0):

        position_value = self.position.black_scholes_value(S, sigma, r, T, q)

        return position_value - self.side.value * self.cost

    def intrinsic_value(self, price: float) -> float:
        """Returns the intrinsic value of this trade which is inherited by the underlying position object

        Args:
            price (float): _description_

        Returns:
            float: _description_
        """

        return self.position.intrinsic_value(price=price)

class CombinationTrade:

    def __init__(self, trades: List[Trade]) -> None:
        self.trades = trades

    def profit_at_expiry(self, price: float) -> float:

        profit = 0
        for trade in self.trades:
            profit += trade.profit_at_expiry(price=price)

        return profit

    def profits_at_expiry(self, prices: np.array) -> np.array:

        profits = np.zeros(shape = prices.shape)

        for trade in self.trades:
            profits += trade.profits_at_expiry(prices=prices)

        return profits


    def black_scholes_profit_vary_underlying(self, S: np.array, sigma: float, r: float, T: float = None, q: float = 0):
        strategy_profits = np.zeros(shape = S.shape)
        for trade in self.trades:
            bs_profit = trade.black_scholes_profit(S, sigma, r, T, q)
            strategy_profits += bs_profit

        return strategy_profits


