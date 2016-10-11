'''
Description:

In this kata you have to implement a basic stack(LIFO) data structure. You have to implement the following methods:

__str__
      return a string "Stack of size: stack_size"  where stack_size is the current size of the stack

isEmpty
      return true if its empty and false otherwise

push
      add an element

pop
      remove the top element and return it

top
   return the top element without removing it or None if empty
You should then implement the reverse_str method that takes as input a string and a stack object and uses the stack to reverse the string.
'''
class CWStack(object):
    def __init__(self):
        self.l = []


    def isEmpty(self):
        return self.l == []

    def push(self, x):
        self.l.append(x)

    def top(self):
        if self.isEmpty():
            return None
        return self.l[len(self.l)-1]

    def pop(self):
        if self.isEmpty():
            return None
        a = self.l[len(self.l)-1]
        self.l = self.l[:-1]
        return a

    def __str__(self):
        return 'Stack of size: {}'.format(len(self.l))
        
def reverse_str(s, stack):
    for x in s:
        stack.push(x)
    s = ''
    while not stack.isEmpty():
        s += stack.pop()
    return s