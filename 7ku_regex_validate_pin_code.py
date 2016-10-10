'''
Description:

ATM machines allow 4 or 6 digit PIN codes and PIN codes cannot contain anything but exactly 4 digits or exactly 6 digits.

If the function is passed a valid PIN string, return true, else return false.

eg:

validate_pin("1234") == True
validate_pin("12345") == False
validate_pin("a234") == False
'''
def validate_pin(pin):
    #return true or false
    import re
    return bool(re.match(r'^\d{4}$', pin)) or bool(re.match(r'^\d{6}$', pin))