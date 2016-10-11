'''
Description:

Generate user links

Your task is to create userlinks for the url, you will be given a username and must return a valid link.

Example

generate_link('matt c')
http://www.codewars.com/users/matt%20c
reference

use this as a reference encoding
'''
def generate_link(user):
    import urllib
    return 'http://www.codewars.com/users/{}'.format(urllib.quote(user))