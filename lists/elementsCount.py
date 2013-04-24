__author__ = 'artemr'

from collections import Counter
orig = ['a', 'b', 'a', 'c', 'b', 'a', 'c']
res = Counter(['a', 'b', 'a', 'c', 'b', 'a', 'c'])
print res

from collections import defaultdict

d = defaultdict(int)
for x in orig:
    d[x] += 1
print d

def get_cnt(lVals):
    d = dict(zip(lVals, [0] * len(lVals)))
    for x in lVals:
        d[x] += 1
    return d

print get_cnt(orig)