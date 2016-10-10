'''
Description:

Find the last element of a list.

Example:

last([1,2,3,4]) # => 4
last("xyz") # => z
last(1,2,3,4) # => 4
In javascript and CoffeeScript a list will be an array, a string or the list of arguments.
'''
def last(*args):
    return args[-1] if not hasattr(args[-1], "__getitem__") else args[-1][-1]