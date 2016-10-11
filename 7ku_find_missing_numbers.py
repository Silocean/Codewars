'''
Description:

You will get an array of numbers.

Every preceding number is smaller than the one following it.

Some numbers will be missing, for instance:

[-3,-2,1,5] //missing numbers are: -1,0,2,3,4
Your task is to return an array of those missing numbers:

[-1,0,2,3,4]
'''
def find_missing_numbers(arr):
    #your code here
    if len(arr)<=1:
        return []
    return sorted(set(range(arr[0], arr[len(arr)-1]+1)).difference(set(arr)))