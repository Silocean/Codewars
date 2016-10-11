'''
Description:

Just as the title suggestes :D . For example ->

largest(1); //Should return 7
largest(2); //Should return 97
....
Do not mind the pattern as it is just an incident ! And make sure to return false if the input is not an integer :D This might seem simple at first, it is, but keep an eye on the performance. Go for it !
'''
def largest(n):
    #Good luck, keep an eye on performance
    if n <= 0 or type(n) != int:
        return False
    i = 10 ** n
    while i >= 1:
        if is_prime(i):
            return i
        i -= 1
    return False


def is_prime(num):
    for x in range(2, num):
        if num % x == 0:
            return False
    return True