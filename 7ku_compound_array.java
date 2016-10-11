/*
Description:

You have to create a method "compoundArray" which should take as input two int arrays of different length and return one int array with numbers of both arrays shuffled one by one. Example: Input - {1,2,3,4,5,6} and {9,8,7,6} Output - {1,9,2,8,3,7,4,6,5,6}
 */
public class CompoundArray {
    
    public static int[] compoundArray(int[] a, int[] b){
    //Who Dares wins!
      int[] arr = new int[a.length + b.length];
        int index = 0;
        while (index / 2 < a.length && index / 2 < b.length) {
            if (index % 2 == 0) {
                arr[index] = a[index / 2];
            } else {
                arr[index] = b[index / 2];
            }
            index++;
        }
        if (index / 2 == a.length) {
            for (int i = a.length; i < b.length; i++) {
                arr[index/2+i] = b[i];
            }
        } else {
            for (int i = b.length; i < a.length; i++) {
                arr[index / 2 + i] = a[i];
            }
        }
        return arr;
    }
}