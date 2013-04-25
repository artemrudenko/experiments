__author__ = 'artemr'

# Largest palindrome product
# Problem 4
# A palindromic number reads the same both ways. The largest palindrome made from the product of
# two 2-digit numbers is 9009 = 91 99.
#
# Find the largest palindrome made from the product of two 3-digit numbers.

from itertools import product
from datetime import datetime


def euler_4_product(start, end):
    res = 0
    for x, y in product(xrange(end, start, -1), xrange(end, start, -1)):
        val = x*y
        if str(val) == str(val)[::-1] and val > res:
            res = val
    return res


start = datetime.today()
print euler_4_product(100, 999)
print 'euler_4_product: ', (datetime.today() - start).total_seconds()


def euler_4(start, end):
    res = 0
    for x in xrange(end, start, -1):
        for y in xrange(end, start, -1):
            val = x*y
            if str(val) == str(val)[::-1] and val > res:
                print x, y, val
                res = val
                break
    return res

start = datetime.today()
print euler_4(100, 999)
print 'euler_4: ', (datetime.today() - start).total_seconds()


def euler_4_(end):
    res, x = 0, end
    while x > 0:
        val = x * end
        if str(val) == str(val)[::-1] and val > res:
            res = val
            break
        x -= 1
    return res


start = datetime.today()
print euler_4_(99999)
print 'euler_4_: ', (datetime.today() - start).total_seconds()