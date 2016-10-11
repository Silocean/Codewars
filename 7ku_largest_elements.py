'''
Description:

Write a program that outputs the top n elements from a list.

Example:

largest(2, [7,6,5,4,3,2,1])
# => [6,7]
'''
def largest(n,xs):
  """Find the n highest elements in a list"""
  return sorted(xs, reverse = True)[:n][::-1]