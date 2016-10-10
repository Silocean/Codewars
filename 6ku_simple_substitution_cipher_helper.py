'''
Description:

A simple substitution cipher replaces one character from an alphabet with a character from an alternate alphabet, where each character's position in an alphabet is mapped to the alternate alphabet for encoding or decoding.

E.g.

map1 = "abcdefghijklmnopqrstuvwxyz";
map2 = "etaoinshrdlucmfwypvbgkjqxz";

cipher = Cipher(map1, map2);
cipher.encode("abc") # => "eta"
cipher.encode("xyz") # => "qxz"
cipher.encode("aeiou") # => "eirfg"

cipher.decode("eta") # => "abc"
cipher.decode("qxz") # => "xyz"
cipher.decode("eirfg") # => "aeiou"
If a character provided is not in the opposing alphabet, simply leave it as be.
'''
class Cipher(object):
    def __init__(self, map1, map2):
        self.map1 = map1
        self.map2 = map2
        pass
    
    def encode(self, string):
        return ''.join(map2[map1.index(x)] if x in map1 else x for x in string)
    
    def decode(self, string):
        return ''.join(map1[map2.index(x)] if x in map2 else x for x in string)