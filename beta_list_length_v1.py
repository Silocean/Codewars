'''
Description:

Try to make a function that counts the length of a list, without the len function, which is removed. Should be quite simple, but this is my first Kata!

In this example, the for loop can be quite important. Here is an example of looping through a string:

for character in string:
  # do something...
'''
def count(lst):
    return sum(1 for x in lst)