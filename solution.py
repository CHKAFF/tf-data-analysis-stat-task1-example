import pandas as pd
import numpy as np


chat_id = 303247798 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array) -> float:
    n = len(x)
    t = 41
    x_bar = np.mean(x)
    sum_abs_dev = np.sum(np.abs(x - x_bar))
    s = sum_abs_dev / n
    a = 2 * x_bar / (t ** 2)
    return a
