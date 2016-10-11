'''
Description:

Write a function that returns a string in which firstname is swapped with last name.

name_shuffler('john McClane'); => "McClane john"
'''
def name_shuffler(str_):
    #your code here
    return " ".join(reversed(str_.split(" ")))