"""
Question 3: Area Calculation by Monte Carlo Idea
@author: Aryan Ahadinia
"""

import numpy as np


def f(x: float) -> float:
    return np.sqrt(x)


def g(x: float) -> float:
    return x / (1 - x**2)


def h(x: float) -> float:
    return 1 / (2 + np.exp(-x))


def area_calculate(f, g, h) -> float:
    x_0, x_1 = 0, 1
    y_0, y_1 = 0, 1
    N = 1000000
    X = np.random.uniform(x_0, x_1, N)
    Y = np.random.uniform(y_0, y_1, N)
    points = np.logical_and(Y < f(X), Y > g(X)), Y > h(X)
    total_area = (x_1 - x_0) * (y_1 - y_0)
    return round(points.sum() * total_area / N, 4)
