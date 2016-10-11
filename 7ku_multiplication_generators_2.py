'''
Description:

Multiplication - Generators #2

Generators can be used to wonderful things, you can use them for numerous things but here is one specific example. You are studying for a test so you must practice your multiplication but you don't have a multiplication table showing the different examples. You have decided to create a generator that prints out a limitless list of time tables.
Task

Your generator must take one parameter a then everytime the generator is called you must return a string in the format of: 'a x b = c' where c is the answer also where b which starts at 1 must increment by 1 each time

More Info: Generators
'''
def generator(a, b=1):
    pass
    while True:
        yield "%s x %s = %s" % (a, b, a * b)
        b += 1