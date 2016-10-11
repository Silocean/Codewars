'''
Description:

Given an array containing only integers, add all the elements and return the binary equivalent of that sum.

If the array contains any non-integer element (e.g. an object, a float, a string and so on), return false.

Note: The sum of an empty array is zero.

arr2bin([1,2]) == '11'
arr2bin([1,2,'a']) == False
'''
def arr2bin(arr):
    #your code here
    for x in arr:
        if type(x)!=int:
            return False
    return bin(sum(arr))[2:]