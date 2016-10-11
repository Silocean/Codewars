'''
Description:

DropCaps means that the first letter of the starting word of the paragraph should be in caps and the remaining lowercase, same like you see in the newspaper.

But for a change lets do that for each and every word of the given String. Your task is to capitalize very word that has length greater than 2, leaving smaller words as they are.

*should work also on Leading and Trailing Spaces and caps.

drop_cap('apple') => "Apple"
drop_cap('apple of banana'); => "Apple of Banana"
drop_cap('one   space'); => "One   Space" 
drop_cap('   space WALK   '); => "   Space Walk   "
Note: you will be provided atleast one word and should take string as input and return string as output.
'''
def drop_cap(str_):
    #your code here
    l = []
    for x in str_.split(' '):
        if len(x)>2:
            l.append(x.capitalize())
        else:
            l.append(x)
    return ' '.join(l)