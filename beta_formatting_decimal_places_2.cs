/*
Description:

Now you get two integers. The two integers should be pasted together as one number, but not to an integer! Just look at the examples. You don't need to check whether the input is a valid number because only valid numbers are used in the tests. The second number is always in the range 0 through 99.

Examples:
First integer: 438474
Second integer: 47
Result: 438474.47

First integer: 8473
Second integer: 94
Result: 8473.94
 */
using System;

public class Numbers
{
  public static double Paste(int numberOne, int numberTwo)
  {
    //Write your code here
    return numberOne + numberTwo * 0.01;
  }
}