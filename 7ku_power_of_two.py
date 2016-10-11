'''
Description:

Write a function that determines if given number is a power of two. A power of two means a number of the form 2^n where n is an integer, i.e. the result of exponentiation with number two as the base and integer n as the exponent. I.e. 1024 is a power of two: it 2^10.

power_of_two(4096) # true

power_of_two(333) # false
Pay attention: hidden tests are using extremmely big numbers
'''
def power_of_two(x):
  # your code here
  b = bin(x)[2:]
  return b.startswith('1') and b[1:].count('0') == len(b[1:])