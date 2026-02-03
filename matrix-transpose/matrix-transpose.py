import numpy as np

def matrix_transpose(A):
    """
    Return the transpose of matrix A (swap rows and columns).
    """
    # result_matrix = np.zeros(A.shape[1], A.shape[0])

    result_matrix = []

    for col in range(len(A[0])):
        new_row = []
        for row in A:
            new_row.append(row[col])

        result_matrix.append(new_row)

    return np.asarray(result_matrix)
