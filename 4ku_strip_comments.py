'''
Description:

Complete the solution so that it strips all text that follows any of a set of comment markers passed in. Any whitespace at the end of the line should also be stripped out.

Example:

Given an input string of:

apples, pears # and bananas
grapes
bananas !apples
The output expected would be:

apples, pears
grapes
bananas
The code would be called like so:

result = solution("apples, pears # and bananas\ngrapes\nbananas !apples", ["#", "!"])
# result should == "apples, pears\ngrapes\nbananas"
'''
def solution(string,markers):
    #your code here
    l = []
    for x in string.split('\n'):
        for y in markers:
            if y in x:
                x = x[:x.index(y)].strip()
        l.append(x)
    return '\n'.join(l)