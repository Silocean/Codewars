'''
Description:

Like my last kata, try to make a function that counts the length of a list, but this time, without any of the default len functions, which are removed.

In this example, the for loop is quite important. Here is an example of looping through a list:

for character in thelist:
  # do something...
'''
def count(lst):
  return sum(1 for x in lst)