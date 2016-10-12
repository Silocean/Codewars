/*
Description:

Numbers ending with zeros are boring.

They might be fun in your world, but not here.

Get rid of them. Only the ending ones.

1450 -> 145
960000 -> 96
1050 -> 105
-1050 -> -105
Zero alone is fine, don't worry about it. Poor guy anyway
 */
public class NoBoring {
    public static int noBoringZeros(int n) {
        // your code
        if(n==0) return 0;
        while(n%10==0) {
          n = n/10;
        }
        return n;
    }
}