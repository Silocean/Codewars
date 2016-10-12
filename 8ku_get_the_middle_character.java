/*
Description:

You are going to be given a word. Your job is to return the middle character of the word. If the word's length is odd, return the middle character. If the word's length is even, return the middle 2 characters.

Examples:

Kata.getMiddle("test") should return "es"

Kata.getMiddle("testing") should return "t"

Kata.getMiddle("middle") should return "dd"

Kata.getMiddle("A") should return "A"
Input

A word (string) of length 0 < str < 1000

Output

The middle character(s) of the word represented as a string.
 */
class Kata {
  public static String getMiddle(String word) {
    //Code goes here!
    if(word.length()%2==0) {
      return word.substring(word.length()/2-1, word.length()/2+1);
    } else {
      return word.charAt(word.length()/2)+"";
    }
  }
}