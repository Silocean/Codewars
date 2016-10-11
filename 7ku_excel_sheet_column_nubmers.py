'''
Description:

Write a function

titleToNumber(title) or title_to_number(title) or titleToNb title ...

(depending on the language)

that given a column title as it appears in an Excel sheet, returns its corresponding column number. All column titles will be uppercase.
'''
def title_to_number(title):
    #your code here
    result = 0
    for i, x in enumerate(title, 0):
        result += 26**(len(title)-1-i) * (ord(x)-64)
    return result