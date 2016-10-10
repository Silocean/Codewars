'''
Description:

For any given linear sequence, calculate the function [f(x)] and return it as a string.

For example:

get_function([0, 1, 2, 3, 4]) => "f(x) = x"
get_function([0, 3, 6, 9, 12]) => "f(x) = 3x"
get_function([1, 4, 7, 10, 13]) => "f(x) = 3x + 1"
Assumptions for this kata are:

the sequence argument will always contain 5 values equal to f(0) - f(4).
the function will always be in the format "nx +/- m", 'x +/- m', 'nx', 'x' or 'm'
if a non-linear sequence simply return 'Non-linear sequence' or Nothing in Haskell.
'''
def get_function(sequence):
    m = sequence[0]
    n = sequence[1] - m
    if [n*x+m for x in range(5)] != sequence:
        return 'Non-linear sequence'
    return 'f(x) = {}'.format(format_function(n, m))
    
def format_function(n, m):
    if not n:
        return m
    n_string = '{}{}x'.format('-' if n < 0 else '', abs(n) if abs(n) != 1 else '')
    m_string = ' {} {}'.format('+' if m > 0 else '-', abs(m)) if m else ''
    return ''.join([n_string, m_string])