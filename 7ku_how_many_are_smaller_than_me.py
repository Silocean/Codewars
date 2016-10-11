'''
Description:

Write

smaller(arr)
that given an array arr, you have to return the amount of numbers that are smaller than arr[i] to the right.

For example:

smaller([5, 4, 3, 2, 1]) == [4, 3, 2, 1, 0]
smaller([1, 2, 0]) == [1, 1, 0]
If you've completed this one and you feel like testing your performance tuning of this same kata, head over to the much tougher version How many are smaller than me II?
'''
def smaller(arr):
    # Good Luck!
    l = []
    for x in range(len(arr)):
        l.append(len(filter(lambda n:n<arr[x], arr[x+1:])))
    return l