'''
Description:

You have two arrays in this kata, every array contain only unique elements. Your task is to calcualate number of elements in first array which also are in second array.
'''
def match_arrays(v, r):
    # Good Luck!
    return sum(1 for x in v if x in r)
# DON'T remove
verbose = False # set to True to diplay arrays being tested in the random tests