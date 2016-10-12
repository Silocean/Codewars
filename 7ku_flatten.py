'''
Description:

Write a function that flattens an Array of Array objects into a flat Array. Your function must only do one level of flattening.

flatten [1,2,3] # => [1,2,3]
flatten [[1,2,3],["a","b","c"],[1,2,3]]  # => [1,2,3,"a","b","c",1,2,3]
flatten [[[1,2,3]]] # => [[1,2,3]]
'''
def flatten(lst):
    #your code here
    result = []
    for l in lst:
        if isinstance(l, list):
            for x in l:
                result.append(x)
        else:
            result.append(l)
    return result