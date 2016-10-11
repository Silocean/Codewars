'''
Description:

Given a time in a time format class, return it without year, month and day.

It should return a string including milliseconds with 3 decimals.

Example:

datetime(2016, 2, 8, 16, 42, 59)
#Should return: 
"16:42:59,000"
'''
def convert(time):
    #Your code here!
    return '{:02}:{:02}:{:02},{:03}'.format(
        time.hour, time.minute, time.second, time.microsecond / 1000)