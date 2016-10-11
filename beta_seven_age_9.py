'''
Description:

Write a function that removes each 9 that it is in between 7s.

seven_ate9('79712312') => '7712312'
seven_ate9('79797') => '777'
Input: String Output: String
'''
def seven_ate9(str_):
    #your code here
    while str_.find('797') != -1:
        str_ = str_.replace('797', '77')
    return str_