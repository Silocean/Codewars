'''
Description:

Given an input n, write a function always that returns a function which returns n. Ruby should return a lambda or a proc.

three = always(3)
three() /* returns 3 */
'''
def always(n=0):
    # ...
    def func():
        return n
    return func