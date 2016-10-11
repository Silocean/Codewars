'''
Description:

Write a function that accepts two parameters, i) a string (containing a list of words) and ii) an integer (n). The function should alphabetize the list based on the nth letter of each word.

example:

function sortIt('bid, zag', 2) #=> 'zag, bid'
The length of all words provided in the list will be >= n. The format will be "x, x, x". In Haskell you'll get a list of Strings instead.
'''
def sort_it(list_, n):
    #your code here
    def compare(a, b):
        if a[n-1] > b[n-1]:
            return 1
        elif a[n-1] < b[n-1]:
            return -1
        else:
            return 0
    return ', '.join(sorted(list_.split(', '), cmp=compare))