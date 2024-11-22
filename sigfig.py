import numpy as np

def round(x, n):
    order = int(np.ceil(np.log10(x)))
    result = np.round(x, n-order)
    return f"{result:.0f}" if order >= n else f"{result}"