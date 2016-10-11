'''
Description:

The numberOfOccurrences function must return the number of occurrences of an element in an array.

sample = [0,1,2,2,3]
number_of_occurrences(0) == 1
number_of_occurrences(4) == 0
number_of_occurrences(2) == 2
number_of_occurrences(3) == 1
'''
def number_of_occurrences(s, xs):
    d = {}
    for x in xs:
        if d.get(x):
            d[x] = d.get(x)+1
        else:
            d[x] = 1
    return d.get(s) if d.get(s) else 0