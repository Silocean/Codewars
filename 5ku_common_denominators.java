/*
Description:

Common denominators

You will have a list of rationals in the form

 [ [numer_1, denom_1] , ... [numer_n, denom_n] ]
where all numbers are positive ints.

You have to produce a result in the form

 [ [N_1, D] ... [N_n, D] ]
in which D is as small as possible and

 N_1/D == numer_1/denom_1 ... N_n/D == numer_n,/denom_n.
Example :

 [ [1, 2], [1, 3], [1, 4] ] produces the array [ [6,12], [4,12], [3,12] ]
 */
public class Fracts {
  static long gcd(long a, long b) {
        return b == 0 ? a : gcd(b, a % b);
    }

    static long lcm(long a, long b) {
        return a * b / gcd(a, b);
    }

    public static String convertFrac(long[][] lst) {
        long lcmall = 1;
        for (long[] item : lst) {
            lcmall = lcm(lcmall, item[1]);
        }
        String result = "";
        for (long[] item : lst) {
            result += "(" + (item[0] * lcmall / item[1]) + "," + lcmall + ")";
        }
        return result;
    }
}