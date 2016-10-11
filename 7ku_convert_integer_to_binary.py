'''
Description:

Convert integers to binary as simple as that. You would be given an integer as a argument and you have to return its binary form. To get an idea about how to convert a decimal number into a binary number, visit here.

Notes: negative numbers should be handled as two's complement; assume all numbers are integers stored using 4 bytes (or 32 bits) in any language.

Your output should ignore leading 0s.

So, for example:

to_binary(3)=="11"
to_binary(-3)=="11111111111111111111111111111101"
Be Ready for Large Numbers. Happy Coding ^_^
'''
def to_binary(n):
    # Happy Coding ^_^
    return bin(n if n >= 0 else 2 ** 32 + n)[2:]