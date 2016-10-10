'''
Description:

In this kata, you will create an object that returns the positions and the values of the "peaks" (or local maxima) of a numeric array.

For example, the array arr = [ 0 , 1 , 2 , 5 , 1 , 0 ] has a peak in position 3 with a value of 5 (arr[3] = 5)

The output will be returned as an object with two properties: pos and peaks. Both of these properties should be arrays. If there is no peak in the given array, then the output should be {pos: [], peaks: []}.

Example: pickPeaks([3,2,3,6,4,1,2,3,2,1,2,3]) returns {pos:[3,7],peaks:[6,3]}

All input arrays will be valid numeric arrays (although it could still be empty), so you won't need to validate the input.

The first and last elements of the array will not be considered as peaks (in the context of a mathematical function, we don't know what is after and before and therefore, we don't know if it is a peak or not).

Also, beware of plateaus !!! [1,2,2,2,1] has a peak while [1, 2, 2, 2, 3] does not. In case of a plateau-peak, please only return the position and value of the beginning of the plateau. For example: pickPeaks([1,2,2,2,1]) returns {pos:[1],peaks:[2]}

have fun!

'''
def pick_peaks(arr):
    #your code here
    import collections
    d = collections.OrderedDict()
    tmp = False
    for i in xrange(1, len(arr)):
        if arr[i] > arr[i - 1]:
            tmp = i
        elif arr[i] < arr[i - 1] and tmp:
            d[tmp] = arr[tmp]
            tmp = False
    a = []
    b = []
    for k, v in d.items():
        a.append(k)
        b.append(v)
    result = {'pos': a, 'peaks': b}
    return result