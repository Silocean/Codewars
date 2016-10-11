'''
Description:

Terminal game move function

In this game, the hero moves from left to right. The player rolls the dice and moves the number of spaces indicated by the dice times 2.

Create a function for the terminal game that takes the current position of the hero and the roll (1-6) and return the new position.
'''
def move(start,step):
    #your code here
    return start + step*2