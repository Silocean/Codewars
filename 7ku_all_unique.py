'''
Description:

Write a program to determine if a string contains all unique characters. Return True/true if it does and False/false otherwise.

The string may contain any of the 128 ASCII characters.
'''
def has_unique_chars(str):
  # TODO: complete
  for x in str:
      if str.count(x) > 1:
          return False
  return True