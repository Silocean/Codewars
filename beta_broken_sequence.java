/*
Description:

You have a sequence of positive numbers starting with 1, but one number is missing!

Find out the missing number; if the sequence is not broken, you should return 0. Each sequence always increments by 1.

In short: an invalid sequence (a string with non numeric character) must return 1, an already complete (or empty) sequence must return 0; a broken sequence with more than one number missing should return the lowest missing number; otherwise return the missing number.

Note that the sequence may be with random order.

E.g.

find_missing_number("1 3 2 5") # returns 4, because 4 is missing
find_missing_number("1 2 3 4") # returns 0, because the sequence isn't broken
find_missing_number("1 5") # returns 2, because the sequence is missing more than one number and 2 is the lowest between 2, 3 and 4

 */
import java.util.Arrays;
import java.util.List;
public class BrokenSequence {
		public int findMissingNumber(String sequence) {	
    if (sequence.equals("")){
            return 0;
        }
      String[] arr = sequence.split(" ");
        Arrays.sort(arr);
        List<String> list = Arrays.asList(arr);
        int i = 1;
        for (String s : arr) {
            if (!list.contains(i+"")) {
                return i;
            }
            i++;
        }
        return 0;
    }
    
}