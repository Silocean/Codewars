'''
Description:

Given an array of integers of any length, return an array that has 1 added to the value represented by the array.

For example an array [2, 3, 9] equals 239, add one would return an array [2, 4, 0].

[4, 3, 2, 5] would return [4, 3, 2, 6]

The array can't be empty and only positive, single digit integers are allowed. The function should return null if the array is empty or any of the array values are negative or more than 10.

[1, -9] would return null/nil/None (according to the language implemented).
'''

def up_array(arr):
    #your code here
    if any(x < 0 for x in arr) or not arr or any(x>=10 for x in arr):
        return None
    else:
        return [int(x) for x in str(int(''.join(map(str, arr)))+1)]