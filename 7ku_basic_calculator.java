/*
Description:

Write a function called calculate that takes 3 values. The first and third values are numbers. The second value is a character. If the character is "+" , "-", "*", or "/", the function will return the result of the corresponding mathematical function on the two numbers. If the string is not one of the specified characters, the function should return null.

calculate(2,"+", 4); //Should return 6
calculate(6,"-", 1.5); //Should return 4.5
calculate(-4,"*", 8); //Should return -32
calculate(49,"/", -7); //Should return -7
calculate(8,"m", 2); //Should return null
calculate(4,"/",0) //should return null
Keep in mind, you cannot divide by zero. If an attempt to divide by zero is made, return null.
 */
public class Calculator
{
  public static Double calculate(final double numberOne, final String operation, final double numberTwo)
  {
    Double result = null;

        if (operation.equals("+")) {
            result = numberOne + numberTwo;
        } else if (operation.equals("-")) {
            result = numberOne - numberTwo;
        } else if (operation.equals("*")) {
            if(numberOne == 0 || numberTwo == 0) {
                result = 0.0;
            } else {
                result = numberOne * numberTwo;
            }
        } else if (operation.equals("/")) {
            if (numberTwo == 0) {
                result = null;
            } else {
                result = numberOne / numberTwo;
            }
        } else {
            result = null;
        }

        return result;
  }
}