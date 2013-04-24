__author__ = 'artemr'

from functools import wraps


def decor(func):
    @wraps(func)
    def __wrapper(*args, **kwargs):
        newArgs = []
        for arg in args:
            newArgs.append(arg + 10)
        res = func(*newArgs, **kwargs)
        return res
    return __wrapper

@decor
def summ(*vals):
    return sum(vals)


print summ(*[1,2,3,4])

MyObjectB()
