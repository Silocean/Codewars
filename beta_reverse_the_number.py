'''
Description:

Reverse the integer without using strings or lists

reverse(123456) -> 654321
'''

def reverse(n):
    return int(str(n)[::-1])