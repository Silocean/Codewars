'''
Description:

Write a function that takes an array and counts the number of each unique element present.
'''
def count(array):
    #your code here
    d = {}
    for x in array:
        if d.get(x):
            d[x] = d.get(x) + 1
        else:
            d[x] = 1
    return d