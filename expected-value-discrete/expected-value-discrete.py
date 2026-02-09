import numpy as np

def expected_value_discrete(x, p):
    """
    Returns: float expected value
    """
    if np.sum(p) != 1:
        raise ValueError("Probabilities do not sum to 1")
        
    return float(np.sum(np.multiply(x, p)))