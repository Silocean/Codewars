'''
Description:

Linked Lists - Append

Write an Append() function which appends one linked list to another. The head of the resulting list should be returned.

If both listA and listB are null/None/nil, return null/None/nil. If one list is null/None/nil and the other is not, simply return the non-null/None/nil list.

The push() and buildOneTwoThree() functions need not be redefined.
'''
class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None


def append(listA, listB):
    if not listA and not listB:
        return None
    elif not listA and listB:
        return listB
    elif not listB and listA:
        return listA
    else:
        current = listA
        while current.next:
            current = current.next
        current.next = listB
    return listA