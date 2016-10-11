'''
Description:

Write a function that takes an integer in input and outputs a string with currency format.

Integer in currency format is expressed by a string of number where every three characters are separated by comma.

Ex. 123456 -> "123,456"

Input will always be an positive integer, so don't worry about type checking or negative/float values.
'''
def to_currency(price):
    #your code here
    s = ''
    for x in range(len(str(price))):
        if x > 0 and x % 3 == 0:
            s += ',' + str(price)[::-1][x]
        else:
            s += str(price)[::-1][x]
    return s[::-1]