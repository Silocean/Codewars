/*
Description:

Your grandfather criticises your overuse of the word 'like', claiming that it makes up more than 5% of the total words you speak.

You argue that it is much lower than this and so to settle the debate, you have been fitted with a recorder that stores every word you say as a string in an array.

Your task is to make an algorithm that returns true if 'like' accounts for more than 5% of words in the array, otherwise false (if no words are spoken, return false also).

eval_likes(['I','am','sooo','like','tired']) # ==> true;
eval_likes(['THIS','IS','LIKE','TERRIBLE']) # ==> true;
eval_likes(['likely','story']) # ==> false;
Your solution must be case-insensitive but you do not need to worry about punctuation (the device you have been fitted with automatically filters this out).
 */
class Kata {
  public static boolean evalLikes(String[] words) {
    // Your code here
    int count = 0;
        for (String s : words) {
            if (s.toLowerCase().equals("like")) count++;
        }
        if ((float) count / words.length > 0.05) {
            return true;
        } else {
            return false;
        }
  }
}