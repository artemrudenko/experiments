__author__ = 'artemr'

import math

# Largest prime factor
# Problem 3
# The prime factors of 13195 are 5, 7, 13 and 29.
#
# What is the largest prime factor of the number 600851475143 ?


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


def get_primes(curr):
    while True:
        if is_prime(curr):
            yield curr
        curr += 1


def euler_3(value):
    max_factor = 0
    for prime in get_primes(2):
        factor, rest = divmod(value, prime)
        if factor and not rest:
            max_factor = prime
            value = factor
        elif not factor and rest:
            break
    return max_factor

print euler_3(600851475143)