'''
Description:

Given an array, find the duplicates in that array, and return a new array of those duplicates.

Note: numbers and their corresponding string representations should not be treated as duplicates (i.e., '1' !== 1).
'''
def duplicates(array):
    #your code here
    dupes = []
    for i in xrange(len(array)):
        if array[i] in array[:i] and array[i] not in dupes:
            dupes.append(array[i])
    return dupes