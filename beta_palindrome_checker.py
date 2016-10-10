'''
Description:

According to wiki palindrome is a word, phrase, number, or other sequence of characters which reads the same backward or forward. Allowances may be made for adjustments to capital letters, punctuation, and word dividers. Famous examples include "A man, a plan, a canal, Panama!", "Amor, Roma", "race car" and "No 'x' in Nixon".

All requirements from definition should be fulfilled. In case of null input (None for Python) return false.
'''
def is_palindrome(s):
    if not s:
        return False
    str = ''.join(x for x in s.lower() if x.isalnum())
    return str == str[::-1]