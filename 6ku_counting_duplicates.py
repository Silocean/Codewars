'''
Description:

Count the number of Duplicates

Write a function that will return the count of distinct case-insensitive alphabetic characters that occur more than once in the input string. The input string can be assumed to contain only alphanumeric characters, including digits, uppercase and lowercase alphabets.

Example

"abcde" -> 0 # no characters repeats more than once
"aabbcde" -> 2 # 'a' and 'b'
"aabbcdeB" -> 2 # 'a' and 'b'
"indivisibility" -> 1 # 'i'
"Indivisibilities" -> 2 # 'i' and 's'
'''
def duplicate_count(text):
    # Your code goes here
    text = text.lower()
    return len(set(x for x in text if text.count(x)>1))