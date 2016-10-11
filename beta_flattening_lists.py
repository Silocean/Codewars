'''
Description:

In this Kata you will create a function that takes a list of lists as an input and returns a flat list.

Example:

flatten [[1,2],[3,4]] == [1,2,3,4]
flatten [[1],[2],[3],[4]] == [1,2,3,4]
'''
def flatten(l):
    r = []
    for x in l:
        for m in x:
            r.append(m)
    return r