'''
Description:

Write a function that accepts two arguments: an array of integers and another integer n.

Determine the number of times where two integers in the array have a difference of n.

For example:

int_diff([1, 1, 5, 6, 9, 16, 27], 4) # 3 ([1, 5], [1, 5], [5, 9])
int_diff([1, 1, 3, 3], 2) # 4 ([1, 3], [1, 3], [1, 3], [1, 3])
Note: your code should not modify the input array.
'''

def int_diff(arr, n):
    # your code goes here
    l = []
    for x in range(len(arr)):
        for y in range(x+1, len(arr)):
            if abs(arr[x] - arr[y]) == n:
                l.append([arr[x], arr[y]])
    return len(l)