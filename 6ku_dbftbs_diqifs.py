'''
Description:

Caesar Ciphers are one of the most basic forms of encryption. It consists of a message and a key, and it shifts the letters of the message for the value of the key.

Your task is to create a function encryptor that takes 2 arguments - key and message - and returns the encrypted message.

A message 'Caesar Cipher' and a key of 1 returns 'Dbftbs Djqifs'.

A message 'Caesar Cipher' and a key of -1 returns 'Bzdrzq Bhogdq'.

Make sure to only shift letters, and be sure to keep the cases of the letters the same. All punctuation, numbers, spaces, and so on should remain the same.

Also be aware of keys greater than 26 and less than -26. There's only 26 letters in the alphabet!
'''
def encryptor(key, message):
    #Program me!
    key = key % 26
    result = ''
    for c in message:
        if c >= 'A' and c <= 'Z':
            result += chr(((ord(c) - ord('A')) + key) % 26 + ord('A'))
        elif c >= 'a' and c <= 'z':
            result += chr(((ord(c) - ord('a')) + key) % 26 + ord('a'))
        else:
            result += c
    return result