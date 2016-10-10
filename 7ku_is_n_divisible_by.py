'''
Description:

Create a function isDivisible(n,...) that checks if the first agrument n is divisible by all other arguments (return true if no other arguments)

Example:

This kata is following kata: http://www.codewars.com/kata/is-n-divisible-by-x-and-y
'''
def is_divisible(*args):
    #your code here
    for i in xrange(1, len(args)):
        if args[0]%args[i]!=0:
            return False
    return True