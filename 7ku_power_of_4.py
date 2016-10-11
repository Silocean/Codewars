'''
Description:

Write a method that returns true if a given parameter is a power of 4, and false if it's not. If parameter is not an Integer (eg String, Array) method should return false as well. (In C# Integer means all integer Types like Int16,Int32,.....)

Examples

isPowerOf4 1024 #should return True
isPowerOf4  102 #should return False
isPowerOf4   64 #should return True
'''
def powerof4(n):
    if type(n) != int:
        return False
    while n%4==0:
        n /= 4
    return True if n==1 else False