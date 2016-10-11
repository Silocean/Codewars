'''
Description:

Basic regex tasks. Write a function that takes in a numeric code of any lenght. The function will check if the code begins with 1, 2, or 3 and return true if so. Return false otherwise.

You can assume the input will always be a nuber.
'''
def validate_code(code):
    #your code here
    return str(code)[0:1] == '1' or str(code)[0:1] == '2' or str(code)[0:1] == '3'