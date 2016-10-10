'''
Description:

Write a function

triple_double(num1, num2)
which takes in numbers num1 and num2 and returns 1 if there is a straight triple of a number at any place in num1 and also a straight double of the same number in num2.
For example:
triple_double(451999277, 41177722899) == 1 // num1 has straight triple 999s and 
                                          // num2 has straight double 99s

triple_double(1222345, 12345) == 0 // num1 has straight triple 2s but num2 has only a single 2

triple_double(12345, 12345) == 0

triple_double(666789, 12345667) == 1
If this isn't the case, return 0
'''
def triple_double(num1, num2):
    #code me ^^
    num1 = str(num1)
    num2 = str(num2)
    a = ''
    flag = False
    for i in range(len(num1) - 2):
        if len(set(num1[i:i+3])) == 1:
            a = num1[i]
            flag = True
            break
    if flag:
        for j in range(len(num2)-1):
            if len(set(num2[j:j+2])) == 1 and num2[j] == a:
                return 1
        return 0
    else:
        return 0