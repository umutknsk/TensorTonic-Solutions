import numpy as np
from collections import Counter

def mean_median_mode(x):
    """
    Compute mean, median, and mode.
    """
    x = np.asarray(x)

    mean = np.mean(x)
    median = np.median(x)
    ctr = Counter(x)
    mode = ctr.most_common(1)

    return (mean, median, mode)