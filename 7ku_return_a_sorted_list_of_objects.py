'''
Description:

You'll be passed an array of objects - you must sort them in descending order based on the value of an arbitrarily specified property. For example, when sorted by a, this:

[
  {a: 1, b: 3},
  {a: 3, b: 2},
  {a: 2, b: 40},
  {a: 4, b: 12}
]
should return:

[
  {a: 4, b: 12},
  {a: 3, b: 2},
  {a: 2, b: 40},
  {a: 1, b: 3}
]
your function must take the form function sortList (sortBy, list)

The values will always be numbers, and the properties will always exist.
'''
def sort_list(sort_key, l):
    return sorted(l, key=lambda x: x[sort_key], reverse=True)