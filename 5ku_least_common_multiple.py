'''
Description:

Write a function that calculates the least common multiple of its arguments; each argument is assumed to be a non-negative integer.
'''
from fractions import gcd


def lcm(*args):
    return reduce(lambda x, y: f(x, y), args)


def f(x, y):
    return x * y / gcd(x, y)