'''
Description:

sort array by last character

write a function sortMe (sort_me in Python) to sort a given array by last character of the element. Element can be an integer or a string.

Example:

sortMe(['acvd','bcc']) => ['bcc','acvd'] As the last characters of strings are d and c. As, c comes before d, sorting by last character will give ['bcc', 'acvd']

if two elements don't differ in the last character, that then they should be sorted by the order they come in the array.
'''
def sort_me(arr):
    # Good Luck!
    return sorted(arr, key=lambda x:str(x)[-1])