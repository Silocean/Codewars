'''
Description:

Make a program that will take an int (x) and give you the summation of all numbers from 1 up to x included. If the given input is not an integer, return "Error 404".

Examples:

summation(25)==325
summation(2.56)=="Invalid Value"
The next problem in this series: Summation:2 (Link will be soon in once it is created)
'''
def summation(x):
    #Code here
    return sum(range(1, x+1)) if type(x) == int else 'Error 404'