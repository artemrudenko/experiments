__author__ = 'artemr'

# Multiples of 3 and 5
# Problem 1
# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
# The sum of these multiples is 23.
#
# Find the sum of all the multiples of 3 or 5 below 1000.


def euler_1(end, multiples=[3, 5]):
    curr = multiples[0]
    res = 0
    while curr < end:
        if not all(divmod(curr, x)[1] for x in multiples):
            res += curr
        curr += 1
    return res


print euler_1(20)
print euler_1(1000)