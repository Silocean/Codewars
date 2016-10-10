'''
Description:

How can you tell an extrovert from an introvert at NSA? Va gur ryringbef, gur rkgebireg ybbxf ng gur BGURE thl'f fubrf.

I found this joke on USENET, but the punchline is scrambled. Maybe you can decipher it? According to Wikipedia, ROT13 (http://en.wikipedia.org/wiki/ROT13) is frequently used to obfuscate jokes on USENET.

Hint: For this task you're only supposed to substitue characters. Not spaces, punctuation, numbers etc. Test examples:

Test.expect(rot13("EBG13 rknzcyr.") == "ROT13 example.");
Test.expect(rot13("This is my first ROT13 excercise!") == "Guvf vf zl svefg EBG13 rkprepvfr!")
'''
def rot13(message):
    #your code here
    import string
    a = string.lowercase
    b = string.uppercase
    return ''.join(
        a[(a.index(x) + 13) % 26] if x.islower() else b[(b.index(x) + 13) % 26] if x.isupper() else x for x in message)