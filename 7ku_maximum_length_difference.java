/*
Description:

You are given two arrays a1 and a2 of strings. Each string is composed with letters from a to z. Let x be any string in the first array and y be any string in the second array.

Find max(abs(length(x) − length(y)))

If a1 or a2 are empty return -1 in each language except in Haskell where you will return Nothing.

Example:

s1 = ["hoqq", "bbllkw", "oox", "ejjuyyy", "plmiis", "xxxzgpsssa", "xxwwkktt", "znnnnfqknaz", "qqquuhii", "dvvvwz"]
s2 = ["cccooommaaqqoxii", "gggqaffhhh", "tttoowwwmmww"]
mxdiflg(s1, s2) --> 13
 */
class MaxDiffLength {
    
    public static int mxdiflg(String[] a1, String[] a2) {
        // your code
        if(a1.length == 0 || a2.length == 0) return -1;
        int aMin = Integer.MAX_VALUE;
        int aMax = Integer.MIN_VALUE;
        int bMin = Integer.MAX_VALUE;
        int bMax = Integer.MIN_VALUE;
        for (String s : a1) {
            if (s.length() > aMax) aMax = s.length();
            if (s.length() < aMin) aMin = s.length();
        }
        for (String s : a2) {
            if (s.length() > bMax) bMax = s.length();
            if (s.length() < bMin) bMin = s.length();
        }
        System.out.println(aMin + ","+aMax);
        System.out.println(bMin +"," + bMax);
        int a = Math.abs(aMax - bMin);
        int b = Math.abs(aMin - bMax);
        return a > b ? a : b;
    }
}
