'''
Description:

After calling the function findSum() with any number of non-negative integer arguments, it should return the sum of all those arguments. If no arguments are given, the function should return 0, if negative arguments are given, it should return -1.

eg

find_sum(1,2,3,4); # returns 10 
find_sum(1,-2);    # returns -1 
find_sum();        # returns 0
Hint: research the arguments object on google or read Chapter 4 from Eloquent Javascript
'''
def find_sum(*args):
    #your code here
    for x in args:
        if x<0:
            return -1
    return sum(args)