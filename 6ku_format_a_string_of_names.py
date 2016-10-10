'''
Description:

Given: an array containing hashes of names

Return: a string formatted as a list of names separated by commas except for the last two names, which should be separated by an ampersand.

Example:

namelist([ {'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'} ])
# returns 'Bart, Lisa & Maggie'

namelist([ {'name': 'Bart'}, {'name': 'Lisa'} ])
# returns 'Bart & Lisa'

namelist([ {'name': 'Bart'} ])
# returns 'Bart'

namelist([])
# returns ''
Note: all the hashes are pre-validated and will only contain A-Z, a-z, '-' and '.'.
'''

def namelist(names):
    #your code here
    if len(names) == 0:
        return ''
    elif len(names) == 1:
        return names[0].get('name')
    elif len(names) == 2:
        return names[0].get('name') + ' & ' + names[1].get('name')
    else:
        return ', '.join(x.get('name') for x in names[:-1]) + ' & ' +names[-1].get('name')