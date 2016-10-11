'''
Description:

One suggestion to build a satisfactory password is to start with a memorable phrase or sentence and make a password by extracting some letters from it.

Even better is to replace some of those letters with numbers (e.g., the letter “O” can be replaced with the number “0”).

• instead of including “i” or “I” put the number “1” in the password;

• instead of including “o” or “O” put the number “0” in the password;

• instead of including “s” or “S” put the number “5” in the password.

Examples: makePassword "Give me liberty or give me death" -> "Gml0gmd" makePassword "Keep Calm and Carry On " -> "KCaC0"
'''
def make_password(phrase):
    # Your code here
    a = ''.join(x[0] for x in phrase.split(' '))
    s = ''
    for x in a:
        if x.lower() == 'i':
            s += '1'
        elif x.lower() == 'o':
            s += '0'
        elif x.lower() == 's':
            s += '5'
        else:
            s += x
    return s