/*
Description:

You are given a string with a length of 0 or greater. You should transform this string so its characters alternate between uppercase and lowercase.

-This input will never be null. -The first letter of the input might be uppercase or lowercase. -There will be no special characters or numbers. -The input will always consist of one word (no spaces).
 */
public class CamelCase {

	public static String cAmEl(String yourName) {
    String[] str = yourName.split("");
    String result = "";
    for (int i = 0; i<str.length; i++){
      if(i%2==0){
        result += str[i].toUpperCase();
      }else{
        result += str[i].toLowerCase();
      }
    }
    return result;
	}
}