/*
Description:

Can you find the needle in the haystack?

Write a function findNeedle() that takes an array full of junk but containing one "needle"

After your function finds the needle it should return a message (as a string) that says:

"found the needle at position " plus the index it found the needle

So

should return
 */
public class Kata {
  public static String findNeedle(Object[] haystack) {
    // Your code here
    int index = 0;
    for(int i=0; i<haystack.length; i++) {
      if(haystack[i] instanceof String && haystack[i].equals("needle")){
        index = i;
      }
    }
    return "found the needle at position " + index;
  }
}