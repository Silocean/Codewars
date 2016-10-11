'''
Description:

Given few numbers, you need to print out the digits that are not being used.

Example:

unused_digits(12, 34, 56, 78) # "09"
unused_digits(2015, 8, 26) # "3479"
Note:

Result string should be sorted
The test case won't pass Integer with leading zero
'''
def unused_digits(*args):
    #your code here
    s = ''.join(str(x) for x in args)
    return ''.join(x for x in '0123456789' if x not in s)