'''
Description:

Write function toAcronym which takes a string and make an acronym of it.

Rule of making acronym in this kata:

1.split string to words by space char
2.take every first letter from word in given string
3.uppercase it
4.join them toghether

Eg:

Code wars -> C, w -> C W -> CW
'''
def to_acronym(input):
    return ''.join(x[0].upper() for x in input.split(' '))