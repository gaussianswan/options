import numpy as np

from scipy.stats import norm
from pricing_models import d1, d2

def delta_bs(option_type: str, S: float, K: float, sigma: float, r: float, T: float, q: float) -> float:
    assert option_type in ['call', 'put'], "The name of the option type must be either call or put."
    d_one = d1(S, K, sigma, r, T)

    if option_type == 'call':

        delta = np.exp(-q * T) * norm.cdf(d_one)

    elif option_type == 'put':

        delta = np.exp(-q*T) * (norm.cdf(d1) - 1)

    return delta

def gamma_bs(S: float, K: float, sigma: float, r: float, T: float, q: float) -> float:

    d_one = d1(S, K, sigma, r, T)

    numerator = np.exp(-q*T) * norm.pdf(d_one)
    denominator = sigma * S * np.sqrt(T)

    return numerator/denominator

def theta_bs(option_type: str, S: float, K: float, sigma: float, r: float, T: float, q: float) -> float:
    d_one = d1(S, K, sigma, r, T)
    d_two = d_one - sigma * (T ** 0.5)

    first = -(sigma * S * np.exp(-q*T))/(2*np.sqrt(T))
    second = q*S*np.exp(-q*T)
    third = r*K*np.exp(-r*T)
    if option_type == 'call':
        theta = -first * norm.pdf(d_one) + second * norm.cdf(d_one) - third * norm.cdf(d_two)
    elif option_type == 'put':
        theta = -first*norm.pdf(-d_one) - second*norm.cdf(-d_one) + third*norm.cdf(-d_two)

    return theta


def vega_bs(S: float, K: float, sigma: float, r: float, T: float, q: float) -> float:

    d_one = d1(S, K, sigma, r, T)
    vega = S * np.sqrt(T) * np.exp(-q*T) * norm.pdf(d_one)

    return vega

def rho_bs(option_type: str, S: float, K: float, sigma: float, r: float, T: float, q: float) -> float:

    d_two = d2(S, K, sigma, r, T)

    if option_type == 'call':
        rho = K * T * np.exp(-r * T) * norm.cdf(d_two)
    elif option_type == 'put':
        rho = -K * T * np.exp(-r * T) * norm.cdf(-d_two)

    return rho
