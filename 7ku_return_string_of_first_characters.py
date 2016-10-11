'''
Description:

In this exercise, a string is passed to a method and a new string has to be returned with the first character of each word in the string

example: 'This Is A Test' will return 'TIAT'
'''
def make_string(s):
    # Your code here
    return ''.join(x[0] for x in s.split(' '))