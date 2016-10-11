'''
Description:


This is the simple version of Shortest Code series. If you need some challenges, please try the challenge version.

Task:

Find out "B"(Bug) in a lot of "A"(Apple).

There will always be one bug in apple, not need to consider the situation that without bug or more than one bugs.

input: string Array apple

output: Location of "B", [x,y]
'''
def sc(apple):
    for line in apple:
        for x in line:
            if apple[apple.index(line)][line.index(x)] == 'B':
                return [apple.index(line), line.index(x)]
    return None