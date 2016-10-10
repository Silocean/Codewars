'''
Description:

Given a string, determine if it's a valid identifier.

Here is the syntax for valid identifiers:

Each identifier must have at least one character.
The first character must be picked from: alpha, underscore, or dollar sign. The first character can not be a digit.
The rest of the characters (besides the first) can be from: alpha, digit, underscore, or dollar sign. In other words, it can be any valid identifier character.
Examples of valid identifiers:

i
wo_rd
b2h
Examples of invalid identifiers:

1i
wo rd
!b2h
'''
def is_valid(idn):
    # Your code here
    if len(idn) < 1:
        return False
    elif (not idn[0].isalpha()) and idn[0] != '_' and idn[0] != '$':
        return False
    else:
        if idn[1:] != '':
            return all((x.isalnum() or x == '_' or x == '$') for x in idn[1:])
        return True