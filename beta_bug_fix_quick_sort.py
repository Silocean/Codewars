'''
Description:

There is an implementation of quicksort algorithm. Your task is to fix it. All inputs are correct.

See also: https://en.wikipedia.org/wiki/Quicksort
'''
def quicksort(arr):
  if len(arr) < 1:
      return arr
  p = arr[0]
  return quicksort(filter(lambda x: x < p, arr)) + [p] + quicksort(filter(lambda x: x >= p, arr[1:]))