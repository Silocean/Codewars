'''
Description:

Implement String#whitespace?(str) (Ruby), String.prototype.whitespace(str) (JavaScript), String::whitespace(str) (CoffeeScript), or whitespace(str) (Python), which should return true/True if given object consists exclusively of zero or more whitespace characters, false/False otherwise.
'''
def whitespace(string):
    #your code here
    import re
    return bool(re.match(r'^\s*$',string))