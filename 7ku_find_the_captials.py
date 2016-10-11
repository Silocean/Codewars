'''
Description:

Instructions

Write a function that takes a single string (word) as argument. The function must return an ordered list containing the indexes of all capital letters in the string.
'''
def capitals(word):
    #your code here
    return [x for x in range(len(word)) if word[x].isupper()]