'''
Description:

Write a function called validParentheses that takes a string of parentheses, and determines if the order of the parentheses is valid. validParentheses should return true if the string is valid, and false if it's invalid.

Examples: 
validParentheses( "()" ) => returns true 
validParentheses( ")(()))" ) => returns false 
validParentheses( "(" ) => returns false 
validParentheses( "(())((()())())" ) => returns true 

All input strings will be nonempty, and will only consist of open parentheses '(' and/or closed parentheses ')'
'''
def valid_parentheses(string):
    l = []
    for x in string:
        if x == '(':
            l.append(x)
        elif x == ')':
            if len(l)==0:
                return False
            l.pop()
    return len(l) == 0