'''
Description:

Move the first letter of each word to the end of it, then add 'ay' to the end of the word.

pig_it('Pig latin is cool') # igPay atinlay siay oolcay
'''
def pig_it(text):
    #your code here
    return ' '.join(x[1:]+x[0]+'ay' if x.isalpha() else x for x in text.split(' '))