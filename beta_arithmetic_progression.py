'''
Description:

In Your class You have started lessons about Arithmetic Progression Because You are also a programmer, You have decided to write a function arithmetic_sequence_elements(a, r, n) that will print first n elementh of the sequence with the given common difference r and first elementh a, separated by comma and space.

For example arithmetic_sequence_elements(1, 2, 5)

Should return: '1, 3, 5, 7, 9'

More info: https://en.wikipedia.org/wiki/Arithmetic_progression
'''
def arithmetic_sequence_elements(a, r, n):
    #Your code here!:)
    return ', '.join(str(a + b * r) for b in xrange(n))