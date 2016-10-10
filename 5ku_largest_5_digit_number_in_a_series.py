'''
Description:

In the following 6 digit number:

283910
91 is the greatest sequence of 2 digits.

Complete the solution so that it returns the largest five digit number found within the number given.. The number will be passed in as a string of only digits. It should return a five digit integer. The number passed may be as large as 1000 digits.

Adapted from ProjectEuler.net
'''
def solution(digits):
    max = 0
    for x in xrange(len(digits)-4):
        if int(digits[x:x+5]) > max:
            max = int(digits[x:x+5])
    return max