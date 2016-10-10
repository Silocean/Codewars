'''
Description:

Given a string of words and numbers. Extract the expression including: 1. the operator: either addition or subtraction 2. the two numbers that we are operating on

Return the result of the calculation.

Example:

"Panda has 48 apples and loses 4" returns 44

"Jerry has 34 apples and gains 6" returns 40

"loses" and "gains" are the only two words describing operators.

Should be a nice little kata for you :)

Note: No fruit debts nor bitten apples = The numbers are integers and no negatives
'''
def calculate(string):
    #your code here
    import re
    l = re.findall('\d+|gains|loses', string)
    return int(l[0]) + int(l[2]) if l[1]=='gains' else int(l[0]) - int(l[2])