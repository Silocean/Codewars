'''
Description:

Sum of 'n' Numbers

sum_of_n (or SequenceSum.sumOfN in Java, SequenceSum.SumOfN in C#) takes an integer n and returns a List (an Array in Java/C#) of length abs(n) + 1. The List/Array contains the numbers in the arithmetic series produced by taking the sum of the consecutive integer numbers from 0 to n inclusive.

n can also be 0 or a negative value.
Wikipedia reference for abs value is available here.

Example:

5 -> [0, 1, 3, 6, 10, 15]

-5 -> [0, -1, -3, -6, -10, -15]

7 -> [0, 1, 3, 6, 10, 15, 21, 28]
'''
def sum_of_n(n):
  # your code goes here
  if n>=0:
      l = [0]
      for x in range(n+1):
          l.append(l[x] + x)
      return l[1:]
  else:
      n = -n
      l = [0]
      for x in range(n+1):
          l.append(l[x] - x)
      return l[1:]