'''
Description:

An anagram is the result of rearranging the letters of a word to produce a new word. (Ref wikipedia).

Note: anagrams are case insensitive

Examples

foefet is an anagram of toffee
Buckethead is an anagram of DeathCubeK
The challenge is to write the function isAnagram (or is_anagram in Python) to return true if the word test is an anagram of the word original and false otherwise. The function prototype is as given below:

def is_anagram(test, original):
  pass
'''
# write the function is_anagram
def is_anagram(test, original):
    return sorted(list(test.lower())) == sorted(list(original.lower()))