'''
Description:

At a job interview, you are challenged to write an algorithm to check if a given string, s, can be formed from two other strings, part1 and part2.

The restriction is that the characters in part1 and part2 are in the same order as in s.

The interviewer gives you the following example and tells you to figure out the rest from the given test cases.

For example:

'codewars' is a merge from 'cdw' and 'oears':

    s:  c o d e w a r s   = codewars
part1:  c   d   w         = cdw
part2:    o   e   a r s   = oears
'''
def is_merge(s, part1, part2):
    if sorted(s) == sorted(part1 + part2):
        a = []
        i = 0
        try:
            for x in part1:
                tmp = s.index(x, i)
                a.append(tmp)
                i = tmp + 1
            b = []
            i = 0
            for x in part2:
                tmp = s.index(x, i)
                b.append(tmp)
                i = tmp + 1
            print b
        except Exception:
            return False
        if a == sorted(a) and b == sorted(b):
            return True
        return False
    else:
        return False