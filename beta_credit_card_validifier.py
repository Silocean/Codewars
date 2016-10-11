'''
Description:

Make a program that sees if a credit card number is valid or not. Also the program should tell you what type of credit card it is if it is valid.

The five things you should consider in your program is: AMEX, Discover, VISA, Master, and Invalid

Discover starts with 6011 and has 16 digits, AMEX starts with 34 or 37 and has 15 digits, Master Card starts with 51-55 and has 16 digits, VISA starts with 4 and has 13 or 16 digits.

Ex: Input: 6011364837263748 --> Output: "Discover" Ex: Input: 5318273647283745 --> Output: "MasterCard" Ex: Input: 12345678910 --> Output: "Invalid" Ex: Input: 371236473823676 --> Output: "AMEX" Ex: Input: 4128374839283 --> Output: "VISA"
'''
def credit(num):
    num = str(num)
    if num.startswith('6011') and len(num) == 16:
        return 'Discover'
    elif num.startswith('34') or num.startswith('37') and len(num)==15:
        return 'AMEX'
    elif num.startswith('4') and (len(num)==13 or len(num) == 16):
        return 'VISA'
    elif num.startswith('5') and num[1] in '12345' and len(num) == 16:
        return 'MasterCard'
    else:
        return 'Invalid'