'''
Description:

Create a function that returns the lowest product of 4 consecutive numbers in a given string of numbers.

This should only work is the number has 4 digits of more. If not, return "Number is too small".

Example

lowest_product("123456789")--> 24 (1x2x3x4)
lowest_product("35") --> "Number is too small"
'''
def lowest_product(input):
    if len(input) < 4: return "Number is too small"
    return min([reduce(lambda x, y:x*y, map(int, input[i:i+4])) for i in range(len(input)-3)])