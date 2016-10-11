'''

6680721?v=3
3 kyu
944
7 kyu
Next Featured Number Higher than a Given Value

170100% of 1382 of 198raulbc777
PythonTRAIN AGAINNEXT KATA
Details
Solutions
Forks (4)
Discourse (21)
Description:

Make a function that receives a value, val and outputs the smallest higher number than the given value, and this number belong to a set of positive integers that have the following properties:

their digits occur only once
they are odd
they are multiple of three
next_numb(12) == 15

next_numb(13) == 15

next_numb(99) == 105

next_numb(999999) == 1023459

next_number(9999999999) == "There is no possible number that
fulfills those requirements"
Enjoy the kata!!
'''
def next_numb(val):
    # your code here
    if len(str(val)) >=10:
        return "There is no possible number that fulfills those requirements"
    val += 1
    while True:
        if val %2 != 0 and val %3 == 0 and len(set(list(str(val)))) == len(list(str(val))):
            return val
        val += 1