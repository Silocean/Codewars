'''
Description:

Write a function which reduces fractions to their simplest form! Fractions will be presented as an array, and the reduced fraction must be returned as an array:

input: [numerator, denominator]   output: [newNumerator, newDenominator]
                    Eg: [45, 120] --> [3, 8]
All numerators and denominators will be positive integers.

Note: This is an introductory Kata for a series... coming soon!
'''
def reduce(fraction):
    # your code here
    import fractions
    g = fractions.gcd(fraction[0], fraction[1])
    return [fraction[0]/g, fraction[1]/g]