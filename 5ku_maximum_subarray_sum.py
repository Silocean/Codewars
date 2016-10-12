'''
Description:

The maximum sum subarray problem consists in finding the maximum sum of a contiguous subsequence in an array or list of integers:

maxSequence([-2, 1, -3, 4, -1, 2, 1, -5, 4])
# should be 6: [4, -1, 2, 1]
Easy case is when the list is made up of only positive numbers and the maximum sum is the sum of the whole array. If the list is made up of only negative numbers, return 0 instead.

Empty list is considered to have zero greatest sum. Note that the empty list or array is also a valid sublist/subarray.
'''
def maxSequence(arr):
	# ... 
    if not arr:
        return 0
    max_num = -2147483647
    cur_num = 0
    for x in arr:
        cur_num += x
        if cur_num > max_num:
            max_num = cur_num
        if cur_num < 0:
            cur_num = 0
    return max_num