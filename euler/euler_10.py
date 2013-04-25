__author__ = 'artemr'

import math
# Summation of primes
# Problem 10
# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
#
# Find the sum of all the primes below two million.


def is_prime(num):
    if num <= 1:
        return False
    elif num == 2:
        return True
    elif num % 2 == 0:
        return False
    for i in xrange(3, int(math.sqrt(num) + 1), 2):
        if num % i == 0:
            return False
    return True


def euler_10_while(endOfRange):
    res = 0
    curr = 0
    while curr < endOfRange:
        if is_prime(curr):
            res += curr
        curr += 1
    return res


def get_primes(curr):
    while True:
        if is_prime(curr):
            yield curr
        curr += 1


def euler_10_yield(endOfRange):
    res = 2
    for val in get_primes(3):
        if val >= endOfRange:
            break
        res += val
    return res


from datetime import datetime

start = datetime.today()
print euler_10_while(2000000)
print 'euler_10_while', (datetime.today() - start).total_seconds()

start = datetime.today()
print euler_10_yield(2000000)
print 'euler_10_yield', (datetime.today() - start).total_seconds()
