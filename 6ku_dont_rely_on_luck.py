'''
Description:

The test fixture I use for this kata is pre-populated.

It will compare your guess to a random number generated in Ruby by:

(Kernel::rand() * 100 + 1).floor
In Javascript/CoffeeScript by:

Math.floor(Math.random() * 100 + 1)
In Python by:

randint(1,100)
You can pass by relying on luck or skill but try not to rely on luck.

"The power to define the situation is the ultimate power." - Jerry Rubin

Good luck!
'''
from random import randint,seed
seed(1)
guess = randint(1,100)
seed(1)