/*
Description:

Welcome. In this kata, you are asked to square every digit of a number.

For example, if we run 9119 through the function, 811181 will come out.

Note: The function accepts an integer and returns an integer
 */
public class SquareDigit {

  public int squareDigits(int n) {
    // TODO Implement me
    String str = String.valueOf(n);
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < str.length(); i++) {
            sb.append((int) Math.pow(Character.getNumericValue(str.charAt(i)), 2));
        }
        return Integer.parseInt(sb.toString());
  }

}