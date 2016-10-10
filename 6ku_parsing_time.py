'''
Description:

Implement String#to_seconds, which should parse time expressed as HH:MM:SS, or nil otherwise.

Any extra characters, or numbers of minutes/seconds higher than 59, should result in nil being returned.
'''
def to_seconds(time):
    #your code here
    if '\n' in time: return None
    print time
    import re
    if bool(re.match(r'\d\d:[0-5]\d:[0-5]\d$', time)):
        l = [int(x) for x in time.split(':')]
        return l[0]*60*60 + l[1]*60 + l[2]
    else:
        return None