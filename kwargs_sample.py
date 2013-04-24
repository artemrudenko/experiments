__author__ = 'artemr'

def foo(a, b):
    print a + b

def bar(c=0, d=0, e=0):
    print c + d + e

def my_func(*args):
    if len(args) == 2:
        return foo(*args)
    elif len(args) == 3:
        return bar(*args)
    else:
        return bar(*args)

my_func(*[1,2])
my_func(*[1,2,3])
my_func(1)