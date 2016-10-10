'''
Description:

Compare two strings by comparing the sum of their letter-Values (char-Value).
For comparing treat all letters as UpperCase.

Null-Strings should be treated as if they are empty strings.
If the string contains other characters than letters, treat the whole string as it would be empty.

Examples:

"AD","BC" -> equal

"AD","DD" -> not equal

"gf","FG" -> equal

"zz1","" -> equal

"ZzZz", "ffPFF" -> equal

"kl", "lz" -> not equal

null, "" -> equal
'''
def compare(s1,s2):
    #your code here
    if any(x for x in s1 if not x.isalpha()):
        s1 = ''
    if any(x for x in s2 if not x.isalpha()):
        s2 = ''
    if not s1 and not s2:
        return True
    a = sum(ord(x.upper()) for x in s1)
    b = sum(ord(x.upper()) for x in s2)
    if a == b:
        return True
    return False