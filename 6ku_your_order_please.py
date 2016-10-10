'''
Description:

Your task is to sort a given string. Each word in the String will contain a single number. This number is the position the word should have in the result.

Note: Numbers can be from 1 to 9. So 1 will be the first word (not 0).

If the input String is empty, return an empty String. The words in the input String will only contain valid consecutive numbers.

For an input: "is2 Thi1s T4est 3a" the function should return "Thi1s is2 3a T4est"
'''
def order(sentence):
    return ' '.join(sorted(sentence.split(' '), cmp=compare))
def compare(x, y):
    a = [k for k in x if k.isdigit()][0]
    b = [k for k in y if k.isdigit()][0]
    if a>b:
        return 1
    elif a<b:
        return -1
    else:
        return 0