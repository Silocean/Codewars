'''
Description:

Write a function that will encrypt a given sentence into International Morse Code, both the input and out puts will be strings.

Characters should be separated by a single space. Words should be separated by a triple space.

For example, "HELLO WORLD" should return -> ".... . .-.. .-.. --- .-- --- .-. .-.. -.."

To find out more about Morse Code follow this link: https://en.wikipedia.org/wiki/Morse_code

A preloaded object/dictionary/hash called CHAR_TO_MORSE will be provided to help convert characters to Morse Code.
'''
#CHAR_TO_MORSE preloaded to convert characters into Morse code
def encryption(string):
    #your code here

    s = ''
    for x in string:
        if CHAR_TO_MORSE.get(x, ' '):
            s += CHAR_TO_MORSE.get(x, ' ') + " "
    return s.strip()