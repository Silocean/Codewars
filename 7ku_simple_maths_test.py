'''
Description:

Create a function which checks a number for three different properties.

is the number prime?
is the number even?
is the number a multiple of 10?
Each should return either true or false, which should be given as an array. Remark: The Haskell variant uses data Property.

Examples

number_property(7)  # ==> [true,  false, false] 
number_property(10) # ==> [false, true,  true]
The number will always be an integer, either positive or negative. Note that negative numbers cannot be primes, but they can be multiples of 10:

number_property(-7)  # ==> [false, false, false] 
number_property(-10) # ==> [false, true,  true]
'''
def number_property(n):
    # your code here
    return [is_prime(n), is_even(n), is_mul_ten(n)]


def is_prime(n):
    if n <= 1:
        return False
    for x in xrange(2, int(n**0.5)+1):
        if n % x == 0:
            return False
    return True


def is_even(n):
    return n % 2 == 0


def is_mul_ten(n):
    return n % 10 == 0