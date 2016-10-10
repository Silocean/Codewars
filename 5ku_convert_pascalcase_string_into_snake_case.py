'''
Description:

Complete the function/method so that it takes CamelCase string and returns the string in snake_case notation. Lowercase characters can be numbers. If method gets number, it should return string.
'''
def to_underscore(string):
    s = ''.join('_'+x.lower() if x.isupper() else x for x in str(string))
    return s[1:] if s.startswith('_') else s