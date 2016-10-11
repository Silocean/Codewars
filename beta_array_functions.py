'''
Description:

A dumb error I had that actually costed me 15 minutes.. since I cannot copy and paste my code, enjoy this contrived recreation of the problem.

After finding this error, I felt that I had to share it with the world..
'''
from functools import partial
class Foo(object):
	def __init__(self):
		self.func = int
		self.arr_of_funcs = [
			partial(int, base=2),
			partial(int, base=8),
		]
	def convert(self, num, base):
		return self.arr_of_funcs[base](num)