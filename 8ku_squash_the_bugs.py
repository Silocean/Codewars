'''
Description:

Simple challenge - eliminate all bugs from the supplied code so that the code runs and outputs the expected value. Output should be the length of the longest word, as a number.

There will only be one 'longest' word.
'''
def find_longest(string):
    
    return max([len(x) for x in string.split(' ')])