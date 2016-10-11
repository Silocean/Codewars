'''
Description:

Generating Permutations:

Write a generator function named permutations that returns all permutations of the supplied list.

This function cannot modify the list that is passed in, or modify the lists that it returns inbetween iterations.

In Python a generator function is a function that uses the yield keyword instead of return to return an iterable set of results.

example output:

for p in permutations([1, 2, 3]):
  print p

[1, 2, 3]
[1, 3, 2]
[2, 1, 3]
[2, 3, 1]
[3, 2, 1]
[3, 1, 2]
Note 1: itertools.permutations has been disabled for this kata.

Note 2: The function must be a real generator function, not just an iterator. All generators are iterators, but not all iterators are generators.
'''
def permutations(l):
  if len(l) <= 1: yield l
  else:
    for perm in permutations(l[1:]):
      for i in xrange(len(perm)+1):
        yield perm[:i] + l[0:1] + perm[i:]