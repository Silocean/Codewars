'''
Description:

In computer science and discrete mathematics, an inversion is a pair of places in a sequence where the elements in these places are out of their natural order. So, if we use ascending order for a group of numbers, then an inversion is when larger numbers appear before lower number in a sequence.

Check out this example sequence: (1, 2, 5, 3, 4, 7, 6) and we can see here three inversions 5 and 3; 5 and 4; 7 and 6.

You are given a sequence of unique numbers and you should count the number of inversions in this sequence.

Input: A sequence as a tuple of integers.

Output: The inversion number as an integer.

Example:

  count_inversion((1, 2, 5, 3, 4, 7, 6)) == 3
  count_inversion((0, 1, 2, 3)) == 0
'''
def count_inversion(sequence):
    """
        Count inversions in a sequence of numbers
    """
    count = 0
    for x in range(len(sequence)):
        for y in range(x+1, len(sequence)):
            if sequence[y] < sequence[x]:
                count += 1
    return count