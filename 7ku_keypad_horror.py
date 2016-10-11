'''
Description:

Having two standards for a keypad layout is inconvenient!
Computer keypad's layout:
7 8 9  \n
4 5 6  \n
1 2 3  \n
  0 \n

Cell phone keypad's layout:
1 2 3\n 
4 5 6\n  
7 8 9\n  
  0\n

Solve the horror of unstandartized keypads by providing a function that converts computer input to a number as if it was typed by a phone.

Example:
"789" -> "123"

Notes:
You get a string with numbers only
'''
def computer_to_phone(numbers):
    #your code here
    dic = {'7':'1','8':'2','9':'3','4':'4','5':'5','6':'6','1':'7','2':'8','3':'9','0':'0'}
    return ''.join([dic.get(x) for x in numbers])