'''
Description:

In this kata you have to write a method to verify the validity of IPv4 addresses.

Example of valid inputs:

"1.1.1.1"

"127.0.0.1"

"255.255.255.255"

Example of invalid input:

"1444.23.9"

"153.500.234.444"

"-12.344.43.11"
'''
from ipaddress import ip_address
def ipValidator(address):
    try:
        ip_address(address)
        return True
    except ValueError:
        return False