'''
Description:

Write a function countVowels or count_vowels to count the number of vowels in a given string.

Notes:

Ignore the case.
Return nil or None for non-string inputs.
Examples:

countVowels("abcdefg") => 2
countVowels(12) => nil

count_vowels("abcdefg") => 2
count_vowels(12) => nil
'''
def count_vowels(s = ''):
    # your code
    if type(s) != str:
        return None
    else:
        count = 0
        for x in s.lower():
            if x in 'aeiou':
                count +=1
        return count