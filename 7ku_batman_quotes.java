/*
Description:

Batman & Robin have gotten into quite a pickle this time. The Joker has mixed up their iconic quotes and also replaced one of the characters in their names, with a number. They need help getting things back in order.

Implement the getQuote method which takes in an array of quotes, and a string comprised of letters and a single number (e.g. "Rob1n") where the number corresponds to their quote indexed in the passed in array.

Return the quote along with the character who said it:

Hint: You are guaranteed that the number in the passed in string is placed somewhere after the first 3 characters of the string. The quotes either belong to Batman, Robin, or Joker.
 */
public class BatmanQuotes{
  
  public static String getQuote(String[] quotes, String hero){
    String returnString = "";
    //FILL ME IN
    int index = 0;
    for(int i=0; i<hero.length(); i++){
      if(hero.charAt(i)>=48 && hero.charAt(i)<=57) index = hero.charAt(i) - 48;
    }
    if(hero.startsWith("B")) {
            returnString = "Batman: " + quotes[index];
        } else if(hero.startsWith("R")) {
            returnString = "Robin: " + quotes[index];
        }else {
            returnString = "Joker: " + quotes[index];
        }
    return returnString;
  }

}