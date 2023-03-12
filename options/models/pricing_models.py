import numpy as np

from scipy.stats import norm

def black_scholes_call_price(S: float, K: float, sigma: float, r: float, T: float, q: float = 0) -> float:

    d_one = d1(S, K, sigma, r, T)
    d_two = d2(S, K, sigma, r, T)

    return S * np.exp(-q * T) * norm.cdf(d_one) - K * np.exp(-r * T) * norm.cdf(d_two)

def black_scholes_put_price(S: float, K: float, sigma: float, r: float, T: float, q: float = 0) -> float:
    d_one = d1(S, K, sigma, r, T)
    d_two = d2(S, K, sigma, r, T)

    return -S * np.exp(-q * T) * norm.cdf(-d_one) + K * np.exp(-r * T) * norm.cdf(-d_two)


def d1(S: float, K: float, sigma: float, r: float, T: float) -> float:
    # assert S > 0, "Underlying price must be greater than 0"
    # assert K > 0, "Strike price must be greater than 0"
    # assert sigma > 0, "Volatility must be greater than 0"
    # assert T > 0, "Time to expiry must be greater than 0"
    num = np.log(S/K) + (r + (sigma **2))*(T)
    denom = sigma * (T ** 0.5)

    return num/denom

def d2(S: float, K: float, sigma: float, r: float, T: float) -> float:

    d = d1(S, K, sigma, r, T)

    return d - sigma * (T ** 0.5)

def bjerskund_stensland_2002_call(S: float, K: float, T: float, r: float, b: float, sigma: float, X: float) -> float:

    def beta() -> float:
        return (0.5 - (b/(sigma**2))) + ((2*r)/(sigma**2) + ((b/sigma**2) - 0.5)**2)**0.5

    def alpha(X: float) -> float:

        b = beta()
        return (X - K) * X ** (-b)

    def phi(gamma: float, H: float) -> float:

        def lam_da() -> float:
            return -r + gamma*b + 0.5*gamma*(gamma-1)*sigma**2

        def kappa() -> float:
            return (2*b/sigma**2) + (2 * gamma - 1)

        lam = lam_da()
        kap = kappa()

        outer = np.exp(lam * T) * S ** gamma
        first = norm.cdf(-(np.log(S/H) + (b + (gamma-0.5)*sigma**2)*T)/(sigma * (T**0.5)))
        second = (X/S)**kap * norm.cdf(-(np.log(X**2/S*H) + (b + (gamma-0.5)*sigma**2)*T)/(sigma * (T**0.5)))

        return outer * (first - second)

    a = alpha(X)
    b = beta()

    first_term = a*S**b
    second_term = a*phi(gamma = b, H = X)
    third_term = phi(gamma = 1, H = X)
    fourth_term = phi(gamma = 1, H = K)
    fifth_term = K * phi(gamma = 0, H = X)
    sixth_term = K * phi(gamma = 0, H = K)

    total = first_term - second_term + third_term - fourth_term - fifth_term + sixth_term

    return total