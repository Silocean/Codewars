/*
Description:

Write a program to find count of the most frequent item of an array.

Assume that input is array of integers.

Ex.:

input array: [3, -1, -1, -1, 2, 3, -1, 3, -1, 2, 4, 9, 3]
ouptut: 5
Most frequent number in example array is -1. It occurs 5 times in input array.
 */
import java.util.HashMap;
import java.util.Map;
public class Kata {
  public static int mostFrequentItemCount(int[] collection) {
    // Do your magic :)
    Map<Integer, Integer> map = new HashMap<>();
        for (int i = 0; i < collection.length; i++) {
            if (map.get(collection[i]) == null) {
                map.put(collection[i], 1);
            } else {
                map.put(collection[i], map.get(collection[i]) + 1);
            }
        }
        int max = 0;
        for (Integer x : map.values()) {
            if (x > max) max = x;
        }
        return max;
  }
}