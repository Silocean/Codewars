'''
Description:

Write the function resistor_parallel that recieve an undefined number of resistances parallel resistors and return the total resistance.

You can assume that there will be no 0 as parameter. Also there will be at least 2 arguments.

Formula: 1/total = 1/r1 + 1/r2 + .. + 1/rn total = 1 / (1/r1 + 1/r2 + .. + 1/rn)

Examples: resistor_parallel(20, 20) will return 10.0 resistor_parallel(20,20, 40): will return 8.0
'''
def resistor_parallel(*args):
    return 1/sum(1/float(x) for x in args)
    # it take an unlimited number of arguments 
    # create the function resistor_parallel