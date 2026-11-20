import numpy as np

def matrix_transpose(A: list) -> np.ndarray:
    arr = np.array(A)
    n,m = arr.shape
    out = np.zeros((m,n), dtype = arr.dtype)

    for i in range(n):
        for j in range(m):
            out[j,i] = arr[i,j]

    return out