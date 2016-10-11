'''
Description:

The Hamming weight of a string is the number of symbols that are different from the zero-symbol of the alphabet used. There are several algorithms for efficient computing of the Hamming weight for numbers. In this Kata, speaking technically, you have to find out the number of '1' bits in a binary representation of a number. Thus,

The interesting part of this task is that you have to do it without string operation (hey, it's not really interesting otherwise)

;)
'''
def hamming_weight(x):
    # have you already looked it up?
    return bin(x)[2:].count('1')