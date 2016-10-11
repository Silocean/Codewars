'''
Description:

Find the most frequent element or elements in the list.

Example:

find_most_frequent([1, 1, 2, 3]) == set([1])
find_most_frequent([1, 1, 2, 2, 3]) == set([1, 2])
find_most_frequent([1, 1, '2', '2', 3]) == set([1, '2'])
'''
def find_most_frequent(l):
	# Write your code here.
  return set([x for x in set(l) if l.count(x) == max([l.count(y) for y in l])])