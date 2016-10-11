'''
Description:

This is a follow up from my kata Insert Dashes. 
Write a function insertDashII(num) that will insert dashes ('-') between each two odd numbers and asterisk ('*') between each even numbers in num 
For example: 
insertDashII(454793) --> 4547-9-3 
insertDashII(1012356895) --> 10123-56*89-5 

Zero shouldn't be considered even or odd.
'''
def insert_dash2(num):
    #your code here
    num = str(num)
    s = ''
    if len(num) == 1:
        return str(num)
    for x in range(0, len(num) - 1):
        if num[x]!='0' and num[x+1] != '0' and int(num[x]) % 2 == 0 and int(num[x + 1]) % 2 == 0:
            s += num[x] + '*'
        elif int(num[x]) % 2 != 0 and int(num[x + 1]) % 2 != 0:
            s += num[x] + '-'
        else:
            s += num[x]
        if x+1 == len(num)-1:
            s += num[-1:]
    return s