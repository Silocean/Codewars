'''
Description:

Make a program that caluclates the tax rate and adds it to the total (x). If the input is a string return "Error 404". Make the tax rate 5%.

Ex: If the input is 100 the program shoud return 105 (because the tax rate added to 100 is equal to 105)

Ex2: If the input is "Bob" the program should return "Error 404" (becayse "Bob" is a string and not an int value)
'''
def tax(x):
    return 'Error 404' if type(x) == str else round(x*1.05, 2)