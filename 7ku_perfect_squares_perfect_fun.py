'''
Description:

Given an integer, if the length of it's digits is a perfect square, return a square block of sqroot(length) * sqroot(length). If not, simply return "Not a perfect square!".

Examples:

1212 returns:

12
12
Note: 4 digits so 2 squared (2x2 perfect square). 2 digits on each line.

123123123 returns:

123
123
123
Note: 9 digits so 3 squared (3x3 perfect square). 3 digits on each line.
'''
import math


def square_it(digits):
    # Your code here
    a = is_square(len(str(digits)))
    if a:
        s = ''
        for x in range(1, len(str(digits)) + 1):
            if x % a == 0:
                s += str(digits)[x - 1] + '\n'
            else:
                s += str(digits)[x - 1]
        return s[:-1]
    else:
        return "Not a perfect square!"


def is_square(num):
    if int(math.sqrt(num)) == math.sqrt(num):
        return int(math.sqrt(num))
    return False