'''
Description:

Clock shows 'h' hours, 'm' minutes and 's' seconds after midnight.

Your task is to make 'Past' function which returns time converted to miliseconds.

Example:

past(0, 1, 1) == 61000
Note! h, m and s will be only Natural numbers! Waiting for translations and Feedback! Thanks!
'''
def past(h, m, s):
    # Good Luck!
    return (h*60*60 + m*60 + s) * 1000