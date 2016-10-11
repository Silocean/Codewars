'''
Description:

You should write a function that takes a string and a positive integer n, splits the string into parts of n length and returns them in an array. It is ok for the last element to have less characters than n.

If n is not a valid size(> 0) (or is absent), you should return an empty array.

If n is greater than the lenght of the string, you should return an array with the only element being the same string.

Examples:

string_chunk('codewars', 2) # ['co', 'de', 'wa', 'rs']
string_chunk('thiskataeasy', 4) # ['this', 'kata', 'easy']
string_chunk('hello world', 3) # ['hel', 'lo ', 'wor', 'ld']
string_chunk('sunny day', 0) # []
'''
def string_chunk(string, n=0):
    if string == "" or n<=0 or type(n) != int:
        return []
    x = 0
    l = []
    for i in range(1, len(string)+1):
        if i%n==0:
            l.append(string[x:i])
            x = i
    if x<len(string):
        l.append(string[x:])
    return l