/*
Description:

Vicky is quite the small wonder. Most people don't even realize she's not a real girl, but a robot living amongst us. Sure, if you stick around her home for a while you might see her creator open up her back and make a few tweaks and even see her recharge in the closet instead of sleeping in a bed.

In this kata, we're going to help Vicky keep track of the words she's learning.

Write a function, learnWord(word) which is a method of the Robot object. The function should report back whether the word is now stored, or if she already knew the word.

Example:

Case shouldn't matter. Only alpha characters are valid. There's also a little trick here. Enjoy!
 */
import java.util.Arrays;
import java.util.Set;
import java.util.HashSet;

public class Robot {
  private static final String[] DEFAULT_WORDS = new String[] {
    "thank", "you", "for", "teaching", "me", "i", "already",
    "know", "the", "word", "do", "not", "understand", "input"
  };
  
  private Set<String> words;
  
  public Robot() {
    words = new HashSet<>(Arrays.asList(DEFAULT_WORDS));
  }
  
  public String learnWord(String word) {
    if (word.matches("\\A[a-zA-Z]+\\z")) {
      return (words.add(word.toLowerCase()) ? "Thank you for teaching me " : "I already know the word ") + word;
    }
    return "I do not understand the input";
  }  
}