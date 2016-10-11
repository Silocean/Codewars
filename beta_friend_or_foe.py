'''
Description:

Make a program that filters a list of strings and returns a list with only your friends name in it.

If a name has 4 letters in it, you can be sure that it has to be a friend of yours!

Ex: Input = ["Ryan", "Kieran", "Jason", "Yous"], Output = ["Ryan", "Yous"]
FUNDAMENTALS
'''
def friend(x):
    #Code
    return [i for i in x if len(i)==4]