'''
Description:

Your job is to create a calculator which evaluates expressions in Reverse Polish notation.

For example expression 5 1 2 + 4 * + 3 - (which is equivalent to 5 + ((1 + 2) * 4) - 3 in normal notation) should evaluate to 14.

Note that for simplicity you may assume that there are always spaces between numbers and operations, e.g. 1 3 + expression is valid, but 1 3+ isn't.

Empty expression should evaluate to 0.

Valid operations are +, -, *, /.

You may assume that there won't be exceptional situations (like stack underflow or division by zero).
'''
def calc(expr):
    from operator import add, div, sub, mul
    from string import atof
    if expr == '':
        return 0
    digits = []
    d = {'+': add, '-': sub, '*': mul, '/': div}
    for x in expr.split(' '):
        if x in '+-*/':
            a = digits.pop()
            b = digits.pop()
            digits.append(d[x](b, a))
        else:
            digits.append(atof(x))
    return int(digits[-1]) if float.is_integer(digits[-1]) else digits[-1]