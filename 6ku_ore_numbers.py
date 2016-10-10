'''
Description:

Ore Numbers (Also called Harmonic Divisor Numbers) are numbers for which the harmonic mean (https://en.wikipedia.org/wiki/Harmonic_mean) of all their divisors (including the number itself) equals an integer.

For example, 6 is an Ore Number because its harmonic mean is exactly 2.

harmonic_mean(6) = 4/(1/1+1/2+1/3+1/6) = 2

Your task is to write a function isOre(n) that returns True (JS true) if n is an Ore Number and False (JS false) otherwise.

(Hint: The harmonic mean is the total number of divisors divided by the sum of their reciprocals.)

You can assume all inputs will be valid positive integers.
'''
def is_ore(n):
    #Your function here!
    #l = [1/float(x) for x in xrange(1, n+1) if n%x==0]
    #return float.is_integer(len(l) / sum(l))
    
    d = [f for f in xrange(1,n+1) if not n%f]
    return (n*len(d))%sum(d) == 0