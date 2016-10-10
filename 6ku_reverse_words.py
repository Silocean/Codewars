'''
Description:

Write a reverseWords function that accepts a string a parameter, and reverses each word in the string. Every space should stay, so you cannot use words from Prelude.

Example:

reverse_words("This is an example!") # returns  "sihT si na !elpmaxe"
'''

def reverse_words(str):
    return ' '.join(x[::-1] for x in str.split(' '))