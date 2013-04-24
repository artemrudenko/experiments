__author__ = 'artemr'


def substact(matr_a, matr_b):
    """return matrix that is a result of subtracting two square matrices"""
    return map(lambda i: map(lambda x, y: x - y, matr_a[i], matr_b[i]),
               xrange(len(matr_a)))


assert substact([[6,7,8],
                 [5,4,5],
                 [1,1,1]], [[1,2,3],
                            [1,2,3],
                            [1,2,3]]
               ) ==  [[5, 5, 5],
                      [4, 2, 2],
                      [0, -1, -2]]

