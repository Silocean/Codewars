'''
Description:

What is the answer to life the universe and everything

Create a function that will make anything true

    anything({}) != [],          'True'
    anything('Hello') < 'World', 'True'
    anything(80) > 81,           'True'
    anything(re) >= re,          'True'
    anything(re) <= math,        'True'
    anything(5) == ord,          'True'
'''
class anything(object):
    def __init__(self, foo): pass
    def __eq__(self, other): return True
    __ne__ = __lt__ = __le__ = __gt__ = __ge__ = __eq__