'''
Description:

You are given an array strarr of strings and an integer k. Your task is to return the first longest string consisting of k consecutive strings taken in the array.

Example:

longest_consec(["zone", "abigail", "theta", "form", "libe", "zas", "theta", "abigail"], 2) --> "abigailtheta"

n being the length of the string array, if n = 0 or k > n or k <= 0 return "".
'''
def longest_consec(strarr, k):
    # your code
    if k<=0:return ''
    maxlen = -1
    s = ''
    for i in xrange(0, len(strarr)-k+1):
        tmpstr = ''.join(strarr[i:i+k])
        if len(tmpstr) > maxlen:
            maxlen = len(tmpstr)
            s = tmpstr
    return s