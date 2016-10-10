'''
Description:

In this Kata you need to will need to write two methods.

Method 1

The first method takes in a valid int (positive or negative) and returns the following:

for any multiple of 3 the string "THREE",
for any multiple of 5 the string "FIVE",
for any multiple of both the string "BOTH",
for all other numbers the original int.
Method 2

The second method takes valid ints (positive or negative) and returns a list of the values that follow the above rules.

The first value may be greater than or less than the second and the list should increment/decrement appropriately

For example an input of 10,13 should generate a response of ['FIVE', 11, 'THREE', 13].

Remarks

The Haskell variant uses Either Integer String in order to create the same behaviour as in the dynamic languages.
'''
def getNumber(number):
    """This method should return the single value"""
    if number%15==0:
        return 'BOTH'
    elif number%5==0:
        return 'FIVE'
    elif number%3==0:
        return 'THREE'
    else:
        return number
    
def getNumberRange(first, last):
    """This method should return a list of values"""
    l = []
    if first < last:
        for x in range(first, last+1):
            if x%15==0:
                l.append('BOTH')
            elif x%5==0:
                l.append('FIVE')
            elif x%3==0:
                l.append('THREE')
            else:
                l.append(x)
    elif first > last:
        for x in range(first, last-1, -1):
            if x%15==0:
                l.append('BOTH')
            elif x%5==0:
                l.append('FIVE')
            elif x%3==0:
                l.append('THREE')
            else:
                l.append(x)
    return l