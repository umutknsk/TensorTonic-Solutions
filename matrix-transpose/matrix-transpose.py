import numpy as np

def matrix_transpose(A):
    """
    Return the transpose of matrix A (swap rows and columns).
    """    
    # M, N = A.shape

    # result_matrix = np.empty((N, M), dtype=A.dtype)

    # for i in range(M):
    #     for j in range(N):
    #         result_matrix[j, i] = A[i, j]

    result_matrix = []

    for col in range(len(A[0])):
        new_row = []
        for row in A:
            new_row.append(row[col])

        result_matrix.append(new_row)

    return np.asarray(result_matrix)
