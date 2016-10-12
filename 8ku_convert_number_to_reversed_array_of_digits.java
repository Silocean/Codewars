/*
Description:

Convert number to reversed array of digits

Given a random number:

C#: long;
C++: unsigned long;
You have to return the digits of this number within an array in reverse order.
Example:

348597 => [7,9,5,8,4,3]
 */
public class Kata {
  public static int[] digitize(long n) {
    // Code here
    String str = String.valueOf(n);
    int[] arr = new int[str.length()];
    for(int i=str.length()-1; i>=0; i--){
            arr[i] = Character.getNumericValue(str.charAt(str.length()-i-1));
        }
    return arr;
  }
}