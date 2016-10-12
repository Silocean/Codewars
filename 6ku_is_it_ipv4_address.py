'''
Description:

Implement String#ipv4_address?, which should return true if given object is an IPv4 address - four numbers (0-255) separated by dots.

It should only accept addresses in canonical representation, so no leading 0s, spaces etc.
'''
def ipv4_address(address):
    #your code here
    import re
    if re.match(r'\A(?:(?!00)(?!2[6-9]\d)(?!25[6-9])[12]?\d{1,2}\.){3}(?!00)(?!2[6-9]\d)(?!25[6-9])[12]?\d{1,2}\Z', address):
        return True
    return False