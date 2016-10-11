'''
Description:

Write a function sum that accepts an unlimited number of integer arguments, and adds all of them together.

The function should reject any arguments that are not integers, and sum the remaining integers.

sum(1,2,3) # => 6
```
'''
def sum(*args):
    l = [x for x in args if type(x) == int]
    a = 0
    for x in l:
        a += x
    return a