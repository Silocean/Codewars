'''
Description:

Find the second-to-last element of a list.

Example:

```python penultimate([1,2,3,4]) # => 3 penultimate("Python is dynamic") # => 'i' (courtesy of [haskell.org)
'''
def penultimate(a):
  return a[len(a)-2]