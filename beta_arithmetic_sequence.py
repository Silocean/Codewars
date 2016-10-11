'''
Description:

In Your class You have started lessons about Arithmetic Progression. Because You are also a programmer, You have decided to write a function arithmetic_sequence_sum(a, r, n), that will print SUM of the first n elementh of the sequence with the given constant r and first elementh a

For example arithmetic_sequence_sum(2, 3, 5)

Should return: 40
becaouse:
2+(2+3)+(2+3+3)+(2+3+3+3)+(2+3+3+3+3)
=2+5+8+11+14
=40

More info: https://en.wikipedia.org/wiki/Arithmetic_progression
'''
def arithmetic_sequence_sum(a, r, n):
    #Your code here!:)
    return sum(a+r*x for x in xrange(n))