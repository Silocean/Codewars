'''
Description:

Given A, B, and C, your job is to plug it into the Quadratic formula and return both the roots. The Quadratic formula can be found here: https://en.wikipedia.org/wiki/Quadratic_formula

NOTE: It should return None/null if the roots are imaginary, and the first number it returns should be the smallest number.

quadrad(1,0,-4) => -2,2

quadrad(1,-1,-30) => -5,6

quadrad(1,2,-8) => -4,2

quadrad(1,4,5) => None
'''
import math
def quadrad(a, b, c):
    if b*b-4*a*c<0:
        return None
    else:
        root1 = (-b-math.sqrt(b*b-4*a*c))/(2*a)
        root2 = (-b+math.sqrt(b*b-4*a*c))/(2*a)
    return root1, root2