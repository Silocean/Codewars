'''
Description:

your task is to implement a method/function that takes a posistive integer and returns its single digit sum of digits **i.e. keep summing the digits till only one digit remains.

Examples: //for Java 
sumDigits(4523) = 4 + 5 + 2 +3 = 14 = 1 + 4 = 5 
here sumDgits(4523) should return 5 
sumDigits(65536) = 6 + 5 + 5 + 3 + 6 = 25 = 2 + 5 = 7
here sumDgits(65536) should return 7 

Examples: //for Ruby and Python 
sum_digits(4523) = 4 + 5 + 2 +3 = 14 = 1 + 4 = 5 
here sum_digits(4523) should return 5 
sum_digits(65536) = 6 + 5 + 5 + 3 + 6 = 25 = 2 + 5 = 7 
here sum_digits(65536) should return 7 
'''
def sum_digits(n):
    while n>=10:
        n = sum(int(x) for x in str(n))
    return n