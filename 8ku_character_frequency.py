'''
Description

Welcome, Warrior! In this kata, you will get a message and you will need to get the frequency of each and every character!

Explanation (Python)

Your function will be called char_freq and you will get passed a string, you will then return a dictionary with as keys the characters, and as values how many times that character is in the string. You can assume you will be given valid input.

Example

char_freq("I like cats") # Returns {'a': 1, ' ': 2, 'c': 1, 'e': 1, 'I': 1, 'k': 1, 'l': 1, 'i': 1, 's': 1, 't': 1}
'''
def char_freq(message):
    dic = {}
    for x in message:
        if dic.get(x):
            dic[x] = dic.get(x)+1
        else:
            dic[x] = 1
    return dic