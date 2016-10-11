'''
Description:

A "Perfect Number" is a number in which the sum of its factors (excluding itself) are equal to itself.

Example: 28

28 has factors of 1, 2, 4, 7, 14
1 + 2 + 4 + 7 + 14 = 28
Therefore, 28 is a perfect number!

Write a program that can verify if the given integer is a perfect number.
'''

#Should return whether or not n is a perfect number
def isPerfect(n):
    tot=1
    d=2
    j=n/2+1
    while d<j:
        if n%d==0: 
            tot= tot+n/d + d 
        d+=1
        j=n/d
    if n==1: return False
    return tot==n    