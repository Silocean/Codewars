'''
tion

providing i=4:

def methodFunc(i)
then function number 4 is called (get x, return x+4) so:

methodFunc(1)(100) = 101
Write your function so that any call such as MethodFunc(x)(y) outputs x+y. (1<=x<=4)
'''
def methodFunc(i):
    #your code here
    def func(x):
        return i+x
    return func