import numpy as np

def geometric_pmf_mean(k, p):
    """
    Compute Geometric PMF and Mean.
    """
    k = np.asarray(k)
    
    pmf = np.power(1 - p, k - 1) * p

    mean = float(1 / p)
    
    return (pmf, mean)