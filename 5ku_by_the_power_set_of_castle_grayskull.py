'''
Description:

Write a function that returns all of the sublists of a list or Array.

Your function should be pure; it cannot modify its input.

Example:

power([1,2,3])
# => [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]
For more details regarding this, see the power set entry in wikipedia.
'''
from itertools import combinations
def power(s):
    return [list(c) for i in range(len(s)+1) for c in combinations(s, i)]