import numpy as np

def swish(x):
    """
    Implement Swish activation function.
    """
    x = np.asarray(x)

    clipped_x = np.clip(x, -500, 500)
    
    sigmoid = 1 / (1 + np.exp(-clipped_x))

    return x * sigmoid