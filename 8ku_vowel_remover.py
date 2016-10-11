'''
Description:

Create a function called shortcut to remove all the lowercase vowels in a given string.

Examples

shortcut("codewars") # --> cdwrs
shortcut("goodbye")  # --> gdby
Don't worry about uppercase vowels.
'''
def shortcut(s):
    # ...
    return "".join([x for x in s if x not in 'aeiou'])