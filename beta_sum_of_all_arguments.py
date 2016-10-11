'''
Description:

Calculate the sum of all the arguments passed to a function.

Note: If any of the arguments is not a finite number the function should return false/False instead of the sum of the arguments.

For example:

sum(1,2,3,4)         should return 10
sum(1, "two", 3)     should return false
sum(1, 2, [3], NaN)  should return false
'''
def sum_all(*args):
    #your code here
    if any(type(x)!=int for x in args):
        return False
    else:
        return sum(args)