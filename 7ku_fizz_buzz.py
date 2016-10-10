'''
Description:

Return an array containing the numbers from 1 to N, where N is the parametered value. N will never be less than 1.

Replace certain values however if any of the following conditions are met:

If the value is a multiple of 3: use the value 'Fizz' instead
If the value is a multiple of 5: use the value 'Buzz' instead
If the value is a multiple of 3 & 5: use the value 'FizzBuzz' instead
'''
def fizzbuzz(n):
    # your code here
    l = []
    for i, x in enumerate(range(1,n+1), 1):
        if i%15==0:
            l.append('FizzBuzz')
        elif i%5==0:
            l.append('Buzz')
        elif i%3==0:
            l.append('Fizz')
        else:
            l.append(x)
    return l