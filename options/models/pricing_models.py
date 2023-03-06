import numpy as np

from scipy.stats import norm

def black_scholes_call_price(S: float, K: float, sigma: float, r: float, T: float, q: float = 0) -> float:

    d_one = d1(S, K, sigma, r, T)
    d_two = d2(S, K, sigma, r, T)

    return S * np.exp(-q * T) * norm.cdf(d_one) - K * np.exp(-r * T) * norm.cdf(d_two)

def black_scholes_put_price(S: float, K: float, sigma: float, r: float, T: float, q: float = 0) -> float:
    d_one = d1(S, K, sigma, r, T)
    d_two = d2(S, K, sigma, r, T)

    return S * np.exp(-q * T) * norm.cdf(1 - d_one) - K * np.exp(-r * T) * norm.cdf(1 - d_two)


def d1(S: float, K: float, sigma: float, r: float, T: float) -> float:
    assert S > 0, "Underlying price must be greater than 0"
    assert K > 0, "Strike price must be greater than 0"
    assert sigma > 0, "Volatility must be greater than 0"
    assert T > 0, "Time to expiry must be greater than 0"
    num = np.log(S/K) + (r + (sigma **2))*(T)
    denom = sigma * (T ** 0.5)

    return num/denom

def d2(S: float, K: float, sigma: float, r: float, T: float) -> float:

    d = d1(S, K, sigma, r, T)

    return d - sigma * (T ** 0.5)

