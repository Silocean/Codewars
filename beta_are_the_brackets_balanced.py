'''
Description:

Given a string which may include opening or closing round brackets, can you tell whether the string contains a balanced pair(s) of round brackets, that is there are no brackets which are either opened & not closed, or vice versa. Opening round brackets always have to come before closing bracket. An empty string is balanced.
'''
def isBalanced(str):
	# TODO: return True or False
    stack = []
    for x in str:
        if x == '(':
            stack.append(x)
        elif x == ')':
            if len(stack) == 0:
                return False
            else:
                stack.pop()
    if len(stack) >0:
        return False
    return True