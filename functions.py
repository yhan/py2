from typing import Any, Tuple

import matplotlib.pyplot as plt
import numpy as np


def graph_array(W: np.ndarray) -> None:
    # Plot
    plt.figure(figsize=(12, 5))
    plt.plot(W, label="Standard Normal Noise (W)", linewidth=1)
    plt.title("Standard Normal Random Noise (Intraday)")
    plt.xlabel("Minute Index")
    plt.ylabel("Value")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()

def simulate_intraday_gbm(S0=100, mu=0.001, sigma=0.02, minutes=390):
    dt = 1 / minutes
    t = np.linspace(0, 1, minutes)
    W = np.random.standard_normal(size=minutes)
    W = np.cumsum(W) * np.sqrt(dt)
    drift = (mu - 0.5 * sigma**2) * t
    diffusion = sigma * W
    mid_price = S0 * np.exp(drift + diffusion)
    return t, mid_price

def simulate_bid_ask(mid_price: np.ndarray, base_spread=0.05, random_spread=True) -> Tuple[np.ndarray, np.ndarray]:
    if random_spread:
        spread = base_spread * (10 + 2 * np.random.randn(len(mid_price)))
        spread = np.clip(spread, 0.005, 2)  # prevent negative/too large spreads
    else:
        spread = np.full_like(mid_price, base_spread)

    bid: float | Any = mid_price - spread / 2
    ask: float | Any = mid_price + spread / 2
    return bid, ask

