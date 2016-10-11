'''
Description:

Make a program that takes a list of a random amount (but will always have atleast 1 number in) of numbers and returns the average, or mean, of the numbers. Also the program should return "Incorrect" if the value entered is a string.

(Use integer division to divide the numbers, (if you actually use the division method))

Ex: If input is [70, 70, 70, 70, 70] the program should return 70 (for obvious reasons)
'''
def average(x):
    #Good luck
    if type(x) == str:
        return "Incorrect"
    else:
        return int(sum(x)/len(x))