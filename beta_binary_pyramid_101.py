'''
Description:

Eg: if m=1 and n=4

   1 //1
+ 10 //2
+ 11 //3
+100 //4
----
 122 // Binary(122) => "1111010"
So BinaryPyramid ( 1 , 4 ) should return "1111010" Note: value returned should be in string format

range should be ascending in order
'''
def binary_piramid(m,n):
    #your code here
    return bin(sum(int(bin(x)[2:]) for x in xrange(m, n+1)))[2:]