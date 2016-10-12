'''
Description:

Linked Lists - Length & Count

Implement Length() to count the number of nodes in a linked list.

length(null) === 0
length(1 -> 2 -> 3 -> null) === 3
Implement Count() to count the occurrences of an integer in a linked list.

count(null, 1) === 0
count(1 -> 2 -> 3 -> null, 1) === 1
count(1 -> 1 -> 1 -> 2 -> 2 -> 2 -> 2 -> 3 -> 3 -> null, 2) === 4
I've decided to bundle these two functions within the same Kata since they are both very similar.

The push() and buildOneTwoThree() functions do not need to be redefined.

Related Kata in order of expected completion (increasing difficulty):
'''
class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None
    
def length(node):
    # Your code goes here.
    count = 0
    while node != None:
        count += 1
        node = node.next
    return count
  
def count(node, data):
    # Your code goes here.
    count = 0
    while node != None:
        if node.data == data:
            count += 1
        node = node.next
    return count