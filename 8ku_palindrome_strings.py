'''
Description:

Palindrome strings

A palindrome is a word, phrase, number, or other sequence of characters which reads the same backward or forward. Allowances may be made for adjustments to capital letters, punctuation, and word dividers.

true == is_palindrome("anna")
false == is_palindrome("walter")
'''
def is_palindrome(string):
    string = str(string)
    return string == string[::-1]