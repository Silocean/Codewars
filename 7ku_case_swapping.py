'''
Description:

Given a string, swap the case for each of the letters.

e.g. CodEwArs --> cODeWaRS
'''
def swap(string_):
    #your code here
    return ''.join([x.swapcase() for x in string_])