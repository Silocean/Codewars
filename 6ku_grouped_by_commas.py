'''
Description:

Finish the solution so that it takes an input 'n' (integer) and returns a string that is the decimal representation of the number grouped by commas after every 3 digits.

Assume: 0 <= n < 1000000000

       1  ->           "1"
      10  ->          "10"
     100  ->         "100"
    1000  ->       "1,000"
   10000  ->      "10,000"
  100000  ->     "100,000"
 1000000  ->   "1,000,000"
35235235  ->  "35,235,235"
'''
def group_by_commas(n):
    #your code here
    s = ''
    for i, x in enumerate(str(n)[::-1]):
        if i % 3 == 0:
            s += ',' + x
        else:
            s += x
    return s[::-1][:-1]