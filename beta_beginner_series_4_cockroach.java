/*
Description:

Cockroach is one of the fastest insects. Write a function which takes its speed in km per hour and returns the number of whole (floored) cm it moves per second.

Example: 
cockroach_speed(1.08) == 30
Note! The input is a Real number (actual type is language dependent) and is >= 0. The result should be an Integer.

Waiting for translations and Feedback!
 */

public class Cockroach{
  public int cockroachSpeed(double x){
    // Good Luck!
    return (int) (x*100000/(60*60));
  }
}