import numpy as np

def sample_var_std(x):
    """
    Compute sample variance and standard deviation.
    """
    sample_var = (np.sum((x - np.mean(x)) ** 2) / (len(x) - 1))
    stndrd_dev = np.sqrt(sample_var)

    return (sample_var, stndrd_dev)