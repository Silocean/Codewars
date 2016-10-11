'''
Description:

Find the greatest common divisor of two positive integers. The integers can be large, so you need to find a clever solution.

The inputs x and y are always greater or equal to 1, so the the greatest common divisor will always be an integer that is also greater or equal to 1.
'''
#Try to make your own gcd method without importing stuff
def mygcd(x,y):
    #GOOD LUCK
    t = 0
    while x % y != 0:
        t = x % y
        x = y
        y = t
    return y