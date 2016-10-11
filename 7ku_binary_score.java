/*
Description:

Objective

Given a number n we will define it's scORe to be 0 | 1 | 2 | 3 | ... | n, where | is the bitwise OR operator.

Write a function that takes n and finds it's scORe.

Examples

n	scORe n
0	0
1	1
49	63
1000000	1048575
Any feedback would be much appreciated
 */
import java.math.BigInteger;

public class BinaryScore {
  public static BigInteger score (BigInteger n) {
    // Good Luck!
    return n.compareTo(BigInteger.ZERO)==0 ? n: new BigInteger(n.toString(2).replace('0','1'),2);
  }
}