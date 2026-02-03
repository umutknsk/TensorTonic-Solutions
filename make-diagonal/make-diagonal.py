import numpy as np

def make_diagonal(v):
    """
    Returns: (n, n) NumPy array with v on the main diagonal
    """
    length = len(v)

    result_array = np.zeros((length, length))

    for i in range(length):
        result_array[i, i] = v[i]

    return result_array
    