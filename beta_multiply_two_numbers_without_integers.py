'''
Description:

Given two strings representing positive integers, such as "12" and "35", return a string containing their product.

Disabled

1. use of `eval`
2. use of ints
3. use of floats
4. use of unsigned longs
5. use of bitwise operators
Accepted

strings
booleans
arrays
Inputs will never have leading zeros, and neither should your output. Your function, multiplyMyNumbers, should handle numbers with up to 5 characters, "13255" for example.
'''
def multiplyMyNumbers(a, b):
    # Work your magic!
    m = sum((ord(a[x])-48)*(10**(len(a)-x-1)) for x in range(len(a)))
    n = sum((ord(b[x])-48)*(10**(len(b)-x-1)) for x in range(len(b)))
    return str(m*n)