'''
Description:

Snail Sort

Given an n x n array, return the array elements arranged from outermost elements to the middle element, traveling clockwise.

array = [[1,2,3],
         [4,5,6],
         [7,8,9]]
snail(array) #=> [1,2,3,6,9,8,7,4,5]
For better understanding, please follow the numbers of the next array consecutively:

array = [[1,2,3],
         [8,9,4],
         [7,6,5]]
snail(array) #=> [1,2,3,4,5,6,7,8,9]

NOTE: The idea is not sort the elements from the lowest value to the highest; the idea is to traverse the 2-d array in a clockwise snailshell pattern.

NOTE 2: The 0x0 (empty matrix) is represented as [[]]
'''
def snail(array):
    l = []
    height = len(array)
    width = len(array[0])
    helper(0, width, height, array, l)
    return l


def helper(index, width, height, arr, l):
    if width <= 0 or height <= 0:
        return
    for i in range(width):
        l.append(arr[index][index + i])
    for i in range(1, height):
        l.append(arr[index + i][index + width - 1])
    for i in range(width - 2, -1, -1):
        l.append(arr[index + height - 1][index + i])
    for i in range(height - 2, 0, -1):
        l.append(arr[index + i][index])
    helper(index + 1, width - 2, height - 2, arr, l)