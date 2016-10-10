'''
Description:

Given a certain array of integers, create a function that may give the minimum number that may be divisible for all the numbers of the array.

min_special_mult([2, 3 ,4 ,5, 6, 7]) == 420
The array may have integers that occurs more than once:

min_special_mult([18, 22, 4, 3, 21, 6, 3]) == 2772
The array should have all its elements integer values. If the function finds an invalid entry (or invalid entries) like strings of the alphabet or symbols will not do the calculation and will compute and register them, outputting a message in singular or plural, depending on the number of invalid entries.

min_special_mult([16, 15, 23, 'a', '&', '12']) == "There are 2 invalid entries: ['a', '&']"

min_special_mult([16, 15, 23, 'a', '&', '12', 'a']) == "There are 3 invalid entries: ['a', '&', 'a']"

min_special_mult([16, 15, 23, 'a', '12']) == "There is 1 invalid entry: a"
If the string is a valid number, the function will convert it as an integer.

min_special_mult([16, 15, 23, '12']) == 5520

min_special_mult([16, 15, 23, '012']) == 5520
All the None/nil elements of the array will be ignored:

min_special_mult([18, 22, 4, , None, 3, 21, 6, 3]) == 2772
If the array has a negative number, the function will convert to a positive one.

min_special_mult([18, 22, 4, , None, 3, -21, 6, 3]) == 2772

min_special_mult([16, 15, 23, '-012']) == 5520
Enjoy it
'''
from fractions import gcd
import re

def min_special_mult(arr):
    l = [e for e in arr if not re.match('(None)|([+-]?\d+)', str(e))]
    if len(l) == 1:
        return 'There is 1 invalid entry: {}'.format(l[0])
    if len(l) > 1:
        return 'There are {} invalid entries: {}'.format(len(l), l)
    
    return reduce(lambda s, e: s * int(e) / gcd(s, int(e)) if e else s, arr, 1)