'''
Description:

In this kata you will create a function to check a non-negative input to see if it is a prime number.

The function will take in a number and will return True if it is a prime number and False if it is not.

A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself.

Examples

isPrime(0) is false
isPrime(1) is false
isPrime(2) is true
isPrime(11) is true
isPrime(12) is false
'''
def is_prime(n):
  'Return True if n is a prime number otherwise return False'
  if n <=1:
      return False
  if n == 2:
      return True
  for x in range(2,n):
      if n%x==0:
          return False
  return True