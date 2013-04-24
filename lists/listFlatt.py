__author__ = 'artemr'

initList = [[1], [2, 3, [4, [5, 6, 7], 8], [9]], 10, [11, [12], 13], 14]


def get_flat(lVals):
    while any(isinstance(x, list) for x in lVals):
        tmp = []
        for val in lVals:
            tmp.extend(val) if isinstance(val, list) else tmp.append(val)
        lVals = tmp[:]
    return lVals[:]

print get_flat(initList)
