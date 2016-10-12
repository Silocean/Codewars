/*
Description:

Write a function which takes two arguments and returns all number, which are divisible by given divisor. First argument is array of numbers and the second is divisor.

Example

divisible_by([1,2,3,4,5,6], 2) == [2,4,6]
 */
import java.util.ArrayList;
import java.util.List;
public class EvenNumbers {
  public static int[] divisibleBy(int[] numbers, long divider) {
        List<Integer> list = new ArrayList<>();
        for (int number : numbers) {
            if(number % divider == 0) {
                list.add(number);
            }
        }
        int[] re = new int[list.size()];
        for (int i = 0; i < list.size(); i++) {
            re[i] = list.get(i);
        }
        return re;
    }
}