'''
Description:

Write a function called validBraces that takes a string of braces, and determines if the order of the braces is valid. validBraces should return true if the string is valid, and false if it's invalid.

This Kata is similar to the Valid Parentheses Kata, but introduces four new characters. Open and closed brackets, and open and closed curly braces. Thanks to @arnedag for the idea!

All input strings will be nonempty, and will only consist of open parentheses '(' , closed parentheses ')', open brackets '[', closed brackets ']', open curly braces '{' and closed curly braces '}'.

What is considered Valid? A string of braces is considered valid if all braces are matched with the correct brace. 
For example:
'(){}[]' and '([{}])' would be considered valid, while '(}', '[(])', and '[({})](]' would be considered invalid.

Examples: 
validBraces( "(){}[]" ) => returns true 
validBraces( "(}" ) => returns false 
validBraces( "[(])" ) => returns false 
validBraces( "([{}])" ) => returns true 
'''
def validBraces(string):
    l = []
    for x in string:
        if x in '([{':
            l.append(x)
        elif x == ')':
            if len(l) == 0:
                return False
            if l.pop() != '(':
                return False
        elif x == ']':
            if len(l) == 0:
                return False
            if l.pop() != '[':
                return False
        elif x == '}':
            if len(l) == 0:
                return False
            if l.pop() != '{':
                return False
    if len(l) != 0:
        return False
    return True