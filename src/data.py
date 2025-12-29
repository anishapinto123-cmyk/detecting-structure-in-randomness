import numpy as np

def pure_noise(n, d):
    """
    Generate n points in R^d with no structure.
    """
    return np.random.randn(n, d)
