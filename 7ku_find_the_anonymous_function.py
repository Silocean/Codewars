'''
Description:

Find the anonymous function in the array

Find the anonymous function in the given array and use the function to filter the array
Input

Your input. First Parameter will be an array with an anonymous function somewhere in the lot, The second Parameter will be an array which you will filter using the anonymous function you find.
Output

Your output. Output a filtered version of the second parameter using the function found in the first parameter.
Reference: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/Arrow_functions
'''
def find_function(func,arr):
    #your code here
    import types
    f = None
    for x in func:
        if type(x) == types.FunctionType:
            f = x
    return filter(f, arr)