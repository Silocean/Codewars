'''
Description:

Write a simple regex to validate a username.

Allowed characters are:

-lowercase letters -numbers -underscore

length shoould be between 4 and 16 characters.
'''
def validate_usr(username):
    import re
    return bool(re.match(r'^[a-z_0-9]{4,16}$', username))