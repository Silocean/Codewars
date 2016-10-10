'''
Description:

Create a Vector object that supports addition, subtraction, dot products, and norms. So, for example:

a = Vector([1,2,3])
b = Vector([3,4,5])
c = Vector([5,6,7,8])
a.add(b) # should return Vector([4,6,8])
a.subtract(b) # should return Vector([-2,-2,-2])
a.dot(b) # should return 1*3+2*4+3*5 = 26
a.norm() # should return sqrt(1^2+2^2+3^2)=sqrt(14)
a.add(c) # raises an exception
If you try to add, subtract, or dot two vectors with different lengths, you must throw an error!

Also provide:

a toString function, so that using the vectors from above, a.toString() === '(1,2,3)' (in Python, this is a __str__ method, so that str(a) == '(1,2,3)')
an equals function, so that two vectors who have the same components are equal
The test cases will utilize the user-provided equals method.
'''
class Vector:
    def __init__(self, lst):
        self.lst = lst

    def add(self, l):
        if len(l.lst) != len(self.lst):
            raise Exception
        return Vector([self.lst[i] + l.lst[i] for i in xrange(len(self.lst))])

    def subtract(self, l):
        if len(l.lst) != len(self.lst):
            raise Exception
        return Vector([self.lst[i] - l.lst[i] for i in xrange(len(self.lst))])

    def dot(self, l):
        if len(l.lst) != len(self.lst):
            raise Exception
        return sum(self.lst[i] * l.lst[i] for i in xrange(len(self.lst)))

    def norm(self):
        import math
        return math.sqrt(sum(x ** 2 for x in self.lst))

    def __str__(self):
        return '(' + ','.join(str(x) for x in self.lst) + ')'

    def equals(self, l):
        return self.lst == l.lst