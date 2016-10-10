/*
Description:

Given an array of integers.

Return an array, where the first element is the count of positives numbers and the second element is sum of negative numbers.

If the input array is empty or null, return an empty array:

C#/Java: new int[] {} / new int[0];
C++: std::vector<int>();
JavaScript/CoffeeScript/PHP: [];
 */
using System;
using System.Collections.Generic;
using System.Linq;

public class Kata
{
    public static int[] CountPositivesSumNegatives(int[] input)
    {
        if (input == null || input.Length==0) return new int[]{};
        int sum = 0;
        int count = 0;
        for (int i=0; i<input.Length; i++){
            if (input[i]>0) count++;
            if (input[i]<0){
                sum += input[i];
            }
        }
        return new int[]{count, sum}; //return an array with count of positives and sum of negatives
    }
}