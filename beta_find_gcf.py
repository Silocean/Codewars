'''
Description:

Create a simple algorithm to find the Greatest Comon Factor (GCF) between two number. Your function should accept two integers and should return an integer as GCF between inputs.

For example:

largest_factor(50,25)
should return 25
This was because 50 and 25 are both divisible by 25 which is the possible largest factor between the two.

largest_factor(81,63)
should return 9

largest_factor(24,54)
should return 6

largest_factor(67,19)
should return 1
Acceptable return value is greater or equal to 1, also, num1 and num2 should be an integer greater than 0.
'''
def largest_factor(num1, num2):
    # Code goes here
    import fractions
    return fractions.gcd(num1, num2)