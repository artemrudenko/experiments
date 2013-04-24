__author__ = 'artemr'

from itertools import product


def multiply(matr_a, matr_b):
    """Return product of an MxP matrix A with an PxN matrix B."""
    cols, rows = len(matr_b[0]), len(matr_b)
    resRows = xrange(len(matr_a))
    rMatrix = [[0] * cols for _ in resRows]
    for idx in resRows:
        for j, k in product(xrange(cols), xrange(rows)):
            rMatrix[idx][j] += matr_a[idx][k] * matr_b[k][j]
    return rMatrix


assert multiply([[6, 7, 8],
                 [5, 4, 5],
                 [1, 1, 1]],
                [[1, 2, 3],
                 [1, 2, 3],
                 [1, 2, 3]]) == [[21, 42, 63],
                                 [14, 28, 42],
                                 [3, 6, 9]]
