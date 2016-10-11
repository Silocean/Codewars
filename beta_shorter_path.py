'''
Description:

You are given a list of directions in the form of a list:

goal = ["N", "S", "E", "W"]

Pretend that each direction counts for 1 step in that particular direction.

Your task is to create a function called directions, that will return a reduced list that will get you to the same point.The order of directions must be returned as N then S then E then W.

If you get back to beginning, return an empty array.
'''
def directions(goal):
    #Code goes here! :)
    x = 0
    y = 0
    for i in goal:
        if i == 'N':
            x += 1
        elif i == 'S':
            x -= 1
        elif i == 'E':
            y += 1
        elif i == 'W':
            y -= 1
    if x==0 and y==0:
        return []
    else:
        l = []
        if x > 0:
            for i in range(x):
                l.append('N')
        elif x < 0:
            for i in range(abs(x)):
                l.append('S')
        if y > 0:
            for i in range(y):
                l.append('E')
        elif y < 0:
            for i in range(abs(y)):
                l.append('W')
        return l