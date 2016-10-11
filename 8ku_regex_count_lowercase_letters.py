'''
Description:

Your task is simply to count the total number of lowercase letters in a string.
'''
def lowercase_count(strng):
    # Your code here
    return len(filter(lambda x:str(x).islower(), strng))