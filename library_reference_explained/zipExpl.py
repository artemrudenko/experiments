__author__ = 'artemr'

a = range(10)
b = range(10, 20)
c = range(5)

resA = zip(a, b)
print resA
resB = zip(a, c)
print resB


def zip_impl(lA, lB):
    res = []
    for idx in range(len(lA)):
        if idx >= len(lB):
            break
        res.append((lA[idx], lB[idx]))
    return res


resAA = zip_impl(a, b)
resBB = zip_impl(a, c)

from itertools import izip, izip_longest

res = izip(a, b)
print list(res)
res = izip_longest(a, c, fillvalue=-1)
print list(res)
