'''
Description:

You have to create a function that takes a positive integer number and returns the next bigger number formed by the same digits:

next_bigger(12)==21
next_bigger(513)==531
next_bigger(2017)==2071
If no bigger number can be composed using those digits, return -1:

next_bigger(9)==-1
next_bigger(111)==-1
next_bigger(531)==-1
'''
def next_bigger(n):
    #your code here
    for i in xrange(len(str(n)) - 1, 0, -1):
        if str(n)[i] > str(n)[i - 1]:
            s = str(n)[:i]

            l = sorted(str(n)[i:])
            for x in l:
                if x > s[-1]:
                    tmp = s[-1]
                    s = s[:-1] + x
                    l.remove(x)
                    l.append(tmp)
                    s += ''.join(sorted(l))

            return int(s)
    return -1